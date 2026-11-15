#!/usr/bin/env python3
"""Junta comentarios publicos coletados em um unico comentarios.csv.

Le, numa pasta:
  - arquivos *.jsonl do youtube-comment-downloader (YouTube, padrao): um JSON por linha com cid, text,
    time_parsed, author, channel, votes, reply. O id do video vem do nome do arquivo (os 11 primeiros
    caracteres, ex.: ID.jsonl ou ID_recentes.jsonl). Respostas (reply: true) sao ignoradas, a menos que
    se use --com-respostas;
  - arquivos *.info.json do yt-dlp (YouTube, alternativa), campo "comments";
  - arquivos .json de dataset da Apify (lista de itens), Instagram ou TikTok.
Escreve (ou acrescenta, sem repetir) em comentarios.csv com as colunas:
  plataforma, link_post, link_comentario, usuario, link_perfil, texto, curtidas, data, idade_aprox,
  coletado_em

`data` so e preenchida quando a fonte da data exata (yt-dlp, Apify). O youtube-comment-downloader so da tempo
relativo ("4 years ago"): nesse caso `data` fica vazia e `idade_aprox` recebe "ha 4 anos". Comentario repetido
(mesmo usuario e mesmo texto) e removido.

So usa a biblioteca padrao do Python 3. Campos ausentes viram vazio.
"""
import argparse
import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

COLUNAS = ["plataforma", "link_post", "link_comentario", "usuario", "link_perfil",
           "texto", "curtidas", "data", "idade_aprox", "coletado_em"]

UNIDADES = {"second": ("segundo", "segundos"), "minute": ("minuto", "minutos"),
            "hour": ("hora", "horas"), "day": ("dia", "dias"), "week": ("semana", "semanas"),
            "month": ("mês", "meses"), "year": ("ano", "anos")}


def idade_aprox(v):
    """'4 years ago' vira 'ha 4 anos'. Texto que nao entender volta como veio (sem '(edited)')."""
    t = re.sub(r"\(edited\)", "", str(v or ""), flags=re.I).strip()
    if not t:
        return ""
    m = re.match(r"^(?:streamed\s+)?(\d+)\s+(second|minute|hour|day|week|month|year)s?\s+ago$", t, re.I)
    if not m:
        return t
    n = int(m.group(1))
    um, mais = UNIDADES[m.group(2).lower()]
    return f"há {n} {um if n == 1 else mais}"


def perfil_yt(canal):
    c = str(canal or "")
    if c.startswith("http"):
        return c
    return f"https://www.youtube.com/channel/{c}" if c else ""


def perfil_rede(plataforma, usuario):
    u = str(usuario or "").lstrip("@").strip()
    if not u:
        return ""
    if plataforma == "tiktok":
        return f"https://www.tiktok.com/@{u}"
    return f"https://www.instagram.com/{u}/"


def primeiro(d, *chaves):
    """Primeiro valor nao vazio entre as chaves, ou ''."""
    for k in chaves:
        v = d.get(k)
        if v not in (None, ""):
            return v
    return ""


def data_iso(v):
    """Aceita timestamp em segundos, em milissegundos ou texto ISO."""
    if v in (None, ""):
        return ""
    try:
        n = float(v)
        if n > 1e11:
            n /= 1000.0
        return datetime.fromtimestamp(n, timezone.utc).strftime("%Y-%m-%d")
    except (TypeError, ValueError):
        return str(v)[:10]


def inteiro(v):
    try:
        return str(int(v))
    except (TypeError, ValueError):
        return ""


def linhas_ytdlp(dados, agora):
    vid = dados.get("id", "")
    link_post = primeiro(dados, "webpage_url") or (
        f"https://www.youtube.com/watch?v={vid}" if vid else "")
    for c in dados.get("comments") or []:
        if not isinstance(c, dict) or not c.get("text"):
            continue
        cid = c.get("id", "")
        link_c = f"https://www.youtube.com/watch?v={vid}&lc={cid}" if vid and cid else link_post
        yield {
            "plataforma": "youtube",
            "link_post": link_post,
            "link_comentario": link_c,
            "usuario": primeiro(c, "author", "author_id"),
            "link_perfil": perfil_yt(primeiro(c, "author_url", "author_id")),
            "texto": c["text"],
            "curtidas": inteiro(c.get("like_count")),
            "data": data_iso(c.get("timestamp")),
            "idade_aprox": "",
            "coletado_em": agora,
        }


def votos(v):
    """Converte '41', '1.2K', '3,4 mil', '2M' em inteiro; vazio se nao entender."""
    if v in (None, ""):
        return ""
    t = str(v).strip().lower().replace(",", ".")
    mult = 1
    for suf, m in (("mil", 1000), ("k", 1000), ("m", 1000000)):
        if t.endswith(suf):
            mult, t = m, t[: -len(suf)].strip()
            break
    try:
        return str(int(round(float(t) * mult)))
    except ValueError:
        return ""


def linhas_ycd(arquivo, agora, com_respostas):
    """Le um .jsonl do youtube-comment-downloader. O id do video vem do nome do arquivo."""
    vid = arquivo.stem[:11]
    link_post = f"https://www.youtube.com/watch?v={vid}"
    ruins = 0
    for linha in arquivo.read_text(encoding="utf-8").splitlines():
        if not linha.strip():
            continue
        try:
            c = json.loads(linha)
        except ValueError:
            ruins += 1
            continue
        if not isinstance(c, dict) or not c.get("text"):
            continue
        if c.get("reply") and not com_respostas:
            continue
        cid = c.get("cid", "")
        canal = c.get("channel", "")
        yield {
            "plataforma": "youtube",
            "link_post": link_post,
            "link_comentario": f"{link_post}&lc={cid}" if cid else link_post,
            "usuario": primeiro(c, "author", "channel"),
            "link_perfil": perfil_yt(canal),
            "texto": c["text"],
            "curtidas": votos(c.get("votes")),
            "data": "",  # so ha tempo relativo; nao inventar data exata
            "idade_aprox": idade_aprox(c.get("time")),
            "coletado_em": agora,
        }
    if ruins:
        print(f"Aviso: {arquivo.name}: {ruins} linha(s) invalida(s) ignorada(s)", file=sys.stderr)


def itens_apify(dados):
    if isinstance(dados, list):
        return [i for i in dados if isinstance(i, dict)]
    if isinstance(dados, dict):
        for k in ("items", "data", "results"):
            if isinstance(dados.get(k), list):
                return [i for i in dados[k] if isinstance(i, dict)]
    return []


def linhas_apify(dados, agora, plataforma, link_post_padrao):
    for i in itens_apify(dados):
        texto = primeiro(i, "text", "comment")
        if not texto or "error" in i and "text" not in i:
            continue
        plat = plataforma
        if not plat:
            plat = "tiktok" if ("uniqueId" in i or "diggCount" in i
                                or "videoWebUrl" in i) else "instagram"
        link_post = (link_post_padrao
                     or primeiro(i, "videoWebUrl", "postUrl", "inputUrl", "postURL"))
        link_c = primeiro(i, "commentUrl", "comment_url") or link_post
        usuario = primeiro(i, "ownerUsername", "uniqueId", "username")
        yield {
            "plataforma": plat,
            "link_post": link_post,
            "link_comentario": link_c,
            "usuario": usuario,
            "link_perfil": perfil_rede(plat, usuario),
            "texto": texto,
            "curtidas": inteiro(primeiro(i, "likesCount", "diggCount", "likes")),
            "data": data_iso(primeiro(i, "timestamp", "createTimeISO", "createTime")),
            "idade_aprox": "",
            "coletado_em": agora,
        }


def ler_existentes(caminho):
    if not caminho.exists():
        return []
    with caminho.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def chave(l):
    """Mesmo usuario e mesmo texto (espacos normalizados) e o mesmo comentario.
    Sem usuario, o link do comentario entra na chave para nao fundir gente diferente."""
    texto = " ".join(l["texto"].split())
    usuario = l["usuario"].strip().lower()
    return (l["plataforma"], usuario, "" if usuario else l["link_comentario"], texto)


def main():
    ap = argparse.ArgumentParser(
        description="Junta comentarios do youtube-comment-downloader (*.jsonl), do yt-dlp (*.info.json) e da Apify (JSON de dataset) em comentarios.csv.")
    ap.add_argument("pasta", help="pasta com os arquivos coletados")
    ap.add_argument("-o", "--saida", default="comentarios.csv",
                    help="CSV de saida; se existir, acrescenta sem repetir (padrao: comentarios.csv)")
    ap.add_argument("--plataforma", choices=["instagram", "tiktok"],
                    help="forca a plataforma dos JSON da Apify (padrao: adivinha pelos campos)")
    ap.add_argument("--com-respostas", action="store_true",
                    help="mantem respostas (reply: true) dos .jsonl do YouTube; por padrao sao ignoradas")
    ap.add_argument("--link-post",
                    help="link do post para JSON da Apify que nao traz o link (use com uma pasta de um post so)")
    a = ap.parse_args()

    pasta = Path(a.pasta)
    if not pasta.is_dir():
        sys.exit(f"Pasta nao encontrada: {pasta}")
    saida = Path(a.saida)
    agora = datetime.now().strftime("%Y-%m-%d")

    novas, ignorados = [], []
    for arq in sorted(pasta.glob("*.jsonl")):
        try:
            novas.extend(linhas_ycd(arq, agora, a.com_respostas))
        except OSError as e:
            ignorados.append(f"{arq.name} ({e.__class__.__name__})")
    for arq in sorted(pasta.glob("*.json")):
        try:
            dados = json.loads(arq.read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            ignorados.append(f"{arq.name} ({e.__class__.__name__})")
            continue
        if isinstance(dados, dict) and "comments" in dados and arq.name.endswith(".info.json"):
            novas.extend(linhas_ytdlp(dados, agora))
        elif arq.name.endswith(".info.json"):
            ignorados.append(f"{arq.name} (sem comentarios)")
        else:
            novas.extend(linhas_apify(dados, agora, a.plataforma, a.link_post))

    existentes = ler_existentes(saida)
    vistos = {chave({c: (l.get(c) or "") for c in COLUNAS}) for l in existentes}
    acrescentadas = 0
    todas = [{c: (l.get(c) or "") for c in COLUNAS} for l in existentes]
    for l in novas:
        k = chave(l)
        if k in vistos:
            continue
        vistos.add(k)
        todas.append(l)
        acrescentadas += 1

    saida.parent.mkdir(parents=True, exist_ok=True)
    with saida.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUNAS)
        w.writeheader()
        w.writerows(todas)

    print(f"{acrescentadas} comentarios novos; {len(todas)} no total em {saida}")
    if ignorados:
        print("Ignorados: " + "; ".join(ignorados))


if __name__ == "__main__":
    main()
