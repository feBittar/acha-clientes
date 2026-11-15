# Coleta no YouTube (caminho B)

Leia no teste de fumaça da fase 0 e nas fases 2 e 3, se o caminho for o YouTube. Dois programas gratuitos, de
código aberto, sem login:

- **yt-dlp**: busca vídeos públicos (título, canal, visualizações). Aqui não baixa o vídeo.
- **youtube-comment-downloader**: baixa os comentários. É o padrão, porque o yt-dlp falha em comentários em alguns
  IPs (seção 2). O `--write-comments` do yt-dlp fica como alternativa (seção 4).

## 1. Instalar e conferir

Peça confirmação antes. Tente nesta ordem e pare no primeiro que funcionar:

1. `python3 -m pip install -U yt-dlp youtube-comment-downloader` (no Windows, `python -m pip install -U ...`).
2. Se aparecer `externally-managed-environment` (comum no Linux e no Python do Homebrew no Mac), crie um ambiente
   só da skill: `python3 -m venv ~/.acha-clientes-py` e depois
   `~/.acha-clientes-py/bin/python -m pip install -U yt-dlp youtube-comment-downloader`. Daí em diante, troque
   `python3` por `~/.acha-clientes-py/bin/python` e `yt-dlp` por `~/.acha-clientes-py/bin/yt-dlp` nos comandos
   (o `juntar_comentarios.py` roda com qualquer Python).
3. Se o passo 2 falhar com `ensurepip is not available` (Ubuntu e Debian), falta um pacote do sistema que pede a
   senha do computador. Peça que a pessoa rode ela mesma, num terminal dela, `sudo apt install python3-venv`, e
   tente o passo 2 de novo. Se ela preferir não mexer, siga sem instalar: caminho A (colar).

Conferir: `yt-dlp --version` e `python3 -m youtube_comment_downloader --help` (ou os do ambiente da skill). Se
aparecer uma versão e a ajuda, está pronto. Anote no `ambiente.md` os dois comandos que funcionaram. Nos testes de
14/11/2026: yt-dlp 2026.10.26, youtube-comment-downloader 0.1.84.

## 2. Teste de fumaça (1 vídeo, 5 comentários)

Decide se o caminho B vale neste computador. Primeiro a busca:

```
yt-dlp "ytsearch1:como conseguir clientes" --flat-playlist --print "%(id)s | %(title)s"
```

Depois 5 comentários do id que apareceu:

```
python3 -m youtube_comment_downloader --youtubeid ID --output acha-clientes/bruto/teste-ID.jsonl --limit 5 --sort 0
```

Se o arquivo nasceu com 5 linhas, o caminho B funciona. Apague o `teste-ID.jsonl` depois (ou deixe: o script não
repete comentário).

**Se a busca ou os comentários falharem**, leia a mensagem. O yt-dlp pode avisar `No supported JavaScript runtime
could be found`: pode ignorar para a busca. Se aparecer `Sign in to confirm` (a frase completa, `Sign in to confirm
you’re not a bot`, usa apóstrofo curvo, então procure só o começo), o YouTube desconfiou da rede. Isso aconteceu
com os comentários pelo yt-dlp em alguns IPs, e o `youtube-comment-downloader` funcionou onde o yt-dlp falhou. Se
os dois falharem, não tente contornar e não passe cookies da conta da pessoa: ofereça colar (`coleta-colando.md`),
a chave oficial (seção 5) ou a Apify para outras redes.

## 3. Buscar posts (fase 2)

Procure vídeos feitos **para o avatar**, com o problema dele nas palavras dele ("não consigo encher a agenda do
salão"), e não termo de produto. Para cada termo do `avatar.md`:

```
yt-dlp --extractor-args "youtube:lang=pt" "ytsearch10:TERMO" --flat-playlist --print "%(id)s | %(title)s | %(view_count)s"
```

`ytsearch10` traz 10 resultados. Título e visualizações vêm de graça, mas não o número de comentários. Na segunda
busca, use `ytsearchdate10:TERMO`, que traz os mais novos primeiro: pelo menos metade da lista precisa ser dos
últimos 12 meses, porque é de vídeo novo que vem comentário recente (lead). Se a amostra vier vazia, o vídeo pode
estar com os comentários desligados: troque por outro.

**Idioma.** Sem opção, o yt-dlp traz os títulos traduzidos para o inglês e a busca mistura vídeo estrangeiro. Testado
em 14/11/2026: `--extractor-args "youtube:lang=pt"` devolve os títulos em português (aparece um aviso, ignorável),
mas o canal vem como `NA`. `lang=pt-BR` não existe (erro). O filtro de idioma da busca não existe: mesmo assim,
confira o idioma pelo título e pela amostra de comentários antes de propor o vídeo.

**Contagem de comentários.** Para ordenar por comentários, tente num vídeo por vez:

- `yt-dlp "https://www.youtube.com/watch?v=ID" --skip-download --print "%(comment_count)s"`.

Se falhar com `Sign in to confirm` (o erro de bot; aconteceu nos 12 vídeos do teste da rodada 2), não insista e
não passe cookies. Use a **amostra de 10 comentários** do `youtube-comment-downloader`, que serve para ver se quem
comenta é o avatar, mas **não dá a contagem nem a data**. Diga à pessoa: "a contagem real só sai depois da coleta".
No `posts.csv`, a coluna `comentarios` recebe o número coletado.

Piso sugerido: 100 ou mais comentários, quando a contagem existe. Prefira vídeos dos últimos 12 meses. Faça no
máximo duas buscas (termos diferentes) para achar posts antes de dizer à pessoa que não achou e oferecer colar ou
outra rede; se a base ficar abaixo de 40 comentários úteis, uma busca extra é permitida, com o "pode" dela. Link do
vídeo: `https://www.youtube.com/watch?v=ID`.

## 4. Coletar comentários (fase 3)

Depois de aprovada a lista, um vídeo por vez. **Padrão:**

```
python3 -m youtube_comment_downloader --youtubeid ID --output acha-clientes/bruto/ID.jsonl --limit 100 --sort 0
```

- `--sort 0` traz os mais populares; `--sort 1`, os recentes. **Rode os dois**: em vídeo grande e antigo há
  comentário novo, e é ele que dá lead recente. Use outro nome de arquivo para o segundo, como `ID_recentes.jsonl`
  (testado em 14/11/2026: `--sort 1` funciona e traz ordem diferente de `--sort 0`).
- `--limit 100` é um bom teto por vídeo. No teste, 30 comentários vieram em 2 segundos.
- Dê uma pausa de alguns segundos entre vídeos. Custo: zero.

O arquivo é JSON por linha (`.jsonl`). Campos: `cid` (id do comentário), `text`, `time` (relativo, "3 years
ago", às vezes com "(edited)"), `time_parsed` (epoch calculado a partir do texto relativo, **não é data exata**), `author` ("@usuario"), `channel` (id do canal), `votes` (texto, pode ser
"1.2K"), `replies`, `reply` (verdadeiro se for resposta), `heart`. Links:

- comentário: `https://www.youtube.com/watch?v=<ID do vídeo>&lc=<cid>`
- perfil: `https://www.youtube.com/channel/<channel>`

O script `juntar_comentarios.py` monta esses links e pega o id do vídeo do nome do arquivo: vale o começo do nome
(os 11 primeiros caracteres), então `ID.jsonl` e `ID_recentes.jsonl` funcionam. Ele traduz `time` para `idade_aprox` ("há 4 anos") e deixa `data` vazia, porque o YouTube só informa o tempo
relativo; converte `votes` em número (`1.2K` vira 1200), grava o `link_perfil`, tira duplicata (mesmo usuário e
mesmo texto) e **ignora as respostas** (`reply: true`), porque o que interessa é o
comentário de primeiro nível. Use `--com-respostas` para mantê-las.

**Alternativa, se o `youtube-comment-downloader` falhar mas o yt-dlp funcionar:**

```
yt-dlp "https://www.youtube.com/watch?v=ID" --skip-download --write-comments --extractor-args "youtube:max_comments=50,all,0,0;comment_sort=top" -o "acha-clientes/bruto/%(id)s"
```

Gera `<id>.info.json` com a lista `comments` (campos `id`, `text`, `like_count`, `author`, `author_id`, `timestamp`,
`parent`). `max_comments=50,all,0,0` pede até 50 de primeiro nível e nenhuma resposta; evite passar de 200 por
vídeo.

Junte (use o caminho da pasta da skill, a pasta onde está o `SKILL.md`):

```
python3 <pasta da skill>/scripts/juntar_comentarios.py acha-clientes/bruto -o acha-clientes/comentarios.csv
```

## 5. Plano B oficial: YouTube Data API v3

É a forma oficial. A chave é grátis e não pede cartão: cota de 10.000 unidades por dia, e `commentThreads.list` custa
1 unidade por chamada, com até 100 comentários cada (https://developers.google.com/youtube/v3/determine_quota_cost).
Passos: criar um projeto no Google Cloud, ativar "YouTube Data API v3", criar uma chave de API e guardá-la em uma
variável de ambiente (`YOUTUBE_API_KEY`), nunca no chat. Para cada vídeo, chame `commentThreads.list` com
`part=snippet`, `videoId=ID`, `maxResults=100`, `order=relevance`. Antes de escrever a chamada, leia a página
oficial da API para confirmar os campos, e peça ao usuário para criar a chave. O resultado precisa ser convertido
para `comentarios.csv` com as mesmas colunas (o script não lê esse formato).

## 6. Ler o perfil público de um canal (fase 5, só da lista curta aprovada)

Grátis, sem login, e só com o "pode" da pessoa. Para cada canal (o `link_perfil` do CSV), uma chamada, com pausa de
alguns segundos entre elas:

```
curl -sL -A "Mozilla/5.0" -H "Accept-Language: pt-BR,pt;q=0.9" "https://www.youtube.com/channel/ID_DO_CANAL" | python3 -I -c "
import sys,re,html
t=sys.stdin.read()
for p in ('og:title','og:description'):
    m=re.search(r'<meta property=\"'+p+r'\" content=\"(.*?)\"\s*>',t,re.S)
    v=html.unescape(m.group(1)) if m else ''
    v=re.sub(r'\S+@\S+|https?://\S+|www\.\S+|@\w[\w.]*|\+?\d[\d ().-]{7,}\d','[omitido]',v)
    print(p,'=',v[:300] if v else '(vazio)')"
```

`og:title` é o nome do canal; `og:description` é a descrição pública. Testado em 14/11/2026 com o canal de um criador
grande (nome e descrição vieram, em português). **Não testado com canal de pessoa comum**, que muitas vezes não tem
descrição: então vem `(vazio)`, e `dados_publicos` recebe só o nome exibido. Se o YouTube pedir consentimento ou
responder erro, não insista. O comando já troca e-mail, telefone, link e @ por `[omitido]`: grave só nome e
descrição, sem tentar recuperar o que foi omitido.
