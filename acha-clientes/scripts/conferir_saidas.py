#!/usr/bin/env python3
"""Confere as saidas da skill acha-clientes contra o comentarios.csv.

Confere que:
  - toda citacao entre aspas em perfis.md e abordagens.md existe literalmente em algum `texto` de comentarios.csv.
    So entram as linhas de citacao: em perfis.md, as que tem o link ao lado (http); em abordagens.md, as que comecam
    com "Ela escreveu:" ou tem link. Aspas na prosa (titulos, notas) nao contam;
  - toda `citacao` de leads.csv (varias separadas por " || ") existe literalmente em algum `texto`;
  - todo `link_origem` de leads.csv (varios separados por " || ", na ordem das citacoes) esta preenchido, existe em
    comentarios.csv (como link_comentario ou link_post) e, quando os numeros batem, cada citacao esta no comentario
    do seu link;
  - em abordagens.md, so leads com "lista curta" na observacao do leads.csv tem rascunho, e nenhum rascunho cita
    preco (R$ ou "reais").

Em perfis.md, linhas de nota (que comecam com ">") nao entram na conferencia.
Normaliza so espacos e aspas/apostrofos curvos. Aceita "[...]" no meio da citacao: cada pedaco precisa existir.
Lista o que falhar e sai com codigo 1; sem falha, sai com 0. So usa a biblioteca padrao.

Uso: python3 conferir_saidas.py [pasta]   (padrao: acha-clientes)
"""
import csv
import re
import sys
from pathlib import Path

CURVAS = str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'", " ": " "})


def norm(s):
    return " ".join(str(s).translate(CURVAS).split())


def existe(citacao, textos):
    """Cada pedaco da citacao (separado por [...] ou ...) precisa estar em algum texto."""
    pedacos = [p.strip(" .,;") for p in re.split(r"\[\.\.\.\]|\[…\]|…|\.\.\.", citacao)]
    pedacos = [p for p in pedacos if p]
    return all(any(p in t for t in textos) for p in pedacos) if pedacos else True


def linha_de_citacao(linha, abordagens):
    l = linha.strip()
    if not l or l.startswith("#"):
        return False
    if abordagens and l.lower().startswith("ela escreveu"):
        return True
    return "http" in l


def citacoes_md(caminho, pula_notas):
    """Trechos entre aspas nas linhas de citacao (aspas retas ou curvas).
    Em perfis.md, linhas de nota (comecam com ">") ficam de fora: ali nao vai citacao."""
    achadas = []
    abordagens = caminho.name == "abordagens.md"
    for n, linha in enumerate(caminho.read_text(encoding="utf-8").splitlines(), 1):
        if pula_notas and linha.lstrip().startswith(">"):
            continue
        if not linha_de_citacao(linha, abordagens):
            continue
        l = linha.translate(CURVAS)
        for m in re.finditer(r'"([^"\n]+)"', l):
            achadas.append((n, m.group(1)))
    return achadas


def main():
    pasta = Path(sys.argv[1] if len(sys.argv) > 1 else "acha-clientes")
    csv_c = pasta / "comentarios.csv"
    if not csv_c.exists():
        sys.exit(f"Nao achei {csv_c}")
    with csv_c.open(newline="", encoding="utf-8") as f:
        comentarios = list(csv.DictReader(f))
    textos = [norm(c.get("texto", "")) for c in comentarios]
    links = set()
    textos_do_link = {}
    for c, t in zip(comentarios, textos):
        for k in ("link_comentario", "link_post"):
            v = (c.get(k) or "").strip()
            if v:
                links.add(v)
                textos_do_link.setdefault(v, []).append(t)

    falhas, total = [], 0

    for nome in ("perfis.md", "abordagens.md"):
        arq = pasta / nome
        if not arq.exists():
            print(f"(sem {nome}, pulei)")
            continue
        for n, c in citacoes_md(arq, nome == "perfis.md"):
            total += 1
            if not existe(norm(c), textos):
                falhas.append(f"{nome} linha {n}: citacao nao achada em comentarios.csv: \"{c}\"")

    arq = pasta / "leads.csv"
    curta = set()
    if arq.exists():
        with arq.open(newline="", encoding="utf-8") as f:
            leads = list(csv.DictReader(f))
        for l in leads:
            lid = l.get("id", "?")
            if "lista curta" in (l.get("observacao") or "").lower():
                curta.add(lid)
            ls = [x.strip() for x in (l.get("link_origem") or "").split("||") if x.strip()]
            total += 1
            if not ls:
                falhas.append(f"leads.csv {lid}: link_origem vazio")
            for link in ls:
                if link not in links:
                    falhas.append(f"leads.csv {lid}: link_origem nao existe em comentarios.csv: {link}")
            partes = [p.strip() for p in (l.get("citacao") or "").split("||") if p.strip()]
            if not partes:
                falhas.append(f"leads.csv {lid}: citacao vazia")
            for i, p in enumerate(partes):
                total += 1
                if not existe(norm(p), textos):
                    falhas.append(f"leads.csv {lid}: citacao nao achada em comentarios.csv: \"{p}\"")
                elif len(ls) == len(partes) and ls[i] in textos_do_link and not existe(norm(p), textos_do_link[ls[i]]):
                    falhas.append(f"leads.csv {lid}: a citacao {i + 1} nao esta no comentario do link {ls[i]}")
            if len(partes) > 1 and len(ls) != len(partes):
                print(f"AVISO leads.csv {lid}: {len(partes)} citacoes e {len(ls)} link(s); separe os links com ' || ', na ordem")
    else:
        print("(sem leads.csv, pulei)")

    arq = pasta / "abordagens.md"
    if arq.exists() and (pasta / "leads.csv").exists():
        atual, tem_msg, na_msg = None, {}, False
        for n, linha in enumerate(arq.read_text(encoding="utf-8").splitlines(), 1):
            m = re.match(r"##\s+(L\d+)", linha)
            if m:
                atual, na_msg = m.group(1), False
                continue
            if atual and linha.strip().lower().startswith("mensagem"):
                tem_msg[atual], na_msg = n, True
                continue
            if na_msg and linha.lstrip().startswith(">"):
                total += 1
                if re.search(r"R\$\s?\d|\d+\s?reais|\breais\b", linha, re.I):
                    falhas.append(f"abordagens.md linha {n}: o rascunho de {atual} cita preco")
            elif na_msg and linha.strip() and not linha.lstrip().startswith(">"):
                na_msg = False
        for lid, n in tem_msg.items():
            total += 1
            if lid not in curta:
                falhas.append(f"abordagens.md linha {n}: {lid} tem rascunho mas nao esta na lista curta do leads.csv")

    print(f"{total} itens conferidos; {len(falhas)} falha(s)")
    for f in falhas:
        print("FALHA " + f)
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
