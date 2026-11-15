# Coleta no Instagram e no TikTok com a Apify (caminho C)

Leia nas fases 2, 3 e 5, só se o caminho escolhido no fecho da fase 1 for a Apify. A Apify é uma plataforma que roda "actors", pequenos programas de
coleta feitos por terceiros. Você manda a entrada, ela roda na nuvem e devolve uma tabela.

## 1. Conta e custo (preços lidos em 14/11/2026)

- Se a conta for do plano Free, são US$ 5 de uso por mês, sem cartão. Se acabar, bloqueia até o ciclo seguinte (https://apify.com/pricing). Outros planos têm outro teto: por isso se consulta a conta (seção 2).
- Preços por 1.000 itens, lidos nas páginas dos actors:

| Actor | Para quê | Preço |
|---|---|---|
| `apify/instagram-hashtag-scraper` | achar posts por hashtag ou palavra | US$ 2,60 |
| `apify/instagram-scraper` | posts e perfis | US$ 2,70 |
| `apify/instagram-comment-scraper` | comentários de posts | US$ 2,60 |
| `clockworks/tiktok-scraper` | vídeos | "a partir de" US$ 1,70 |
| `clockworks/tiktok-comments-scraper` | comentários de vídeos | "a partir de" US$ 0,50 |

- Num plano Free, com US$ 5 saem perto de **1.900 comentários do Instagram por mês** (5 ÷ 2,60 × 1.000). Isso é tudo, somando
  busca e comentários. No TikTok, o preço exato no plano Free não foi verificado; confira na página do actor.
  A página do `tiktok-comments-scraper` mostra "a partir de US$ 0,50" e uma FAQ com valor antigo mais alto, então
  use o maior para estimar.
- Preços mudam. Antes de rodar, abra a página do actor e confira.

## 2. Quanto resta e estimar antes de rodar (sempre)

**Primeiro, quanto resta no mês.** Com o token já na variável de ambiente (nunca no chat):

```
curl -s -H "Authorization: Bearer $APIFY_TOKEN" https://api.apify.com/v2/users/me/limits
```

Leia `data.limits.maxMonthlyUsageUsd` (o teto do mês) e `data.current.monthlyUsageUsd` (o que já foi usado). Diga à
pessoa: "Sua conta tem teto de US$ X por mês e já usou US$ Y; restam US$ Z." No teste, a conta tinha teto de US$ 19
e US$ 12,79 já usados, e não os US$ 5 do plano gratuito. Sem esse número, a promessa dos US$ 5 pode estar errada.

**Depois, a estimativa.** Conta simples: itens esperados ÷ 1.000 × preço, mais a busca de posts, que também cobra.
Custos reais do teste de 14/11/2026, para calibrar:

- 10 posts de uma busca por hashtag: US$ 0,023;
- 16 comentários de 4 posts: US$ 0,037.

Exemplo: 6 posts × 100 comentários = 600 comentários × 2,60 ÷ 1.000 = cerca de US$ 1,56. Mostre a conta, o total e
o que sobra, e peça o "pode". Depois da rodada, diga o custo real. O campo `usageTotalUsd` do run **demora alguns
minutos para aparecer** (logo depois da rodada saiu 0 no teste); se vier 0, consulte de novo mais tarde ou compare
o `monthlyUsageUsd` de antes e depois.

**Teto.** Ponha limite de itens na entrada (`resultsLimit`). Na API também existe o parâmetro de consulta
`maxTotalChargeUsd`, que "especifica o custo máximo total do run"
(https://docs.apify.com/api/v2/act-run-sync-get-dataset-items-post); por exemplo `...?timeout=240&maxTotalChargeUsd=0.5`.
Não foi testado aqui. Rode primeiro 1 post com 20 comentários para ver a saída e o custo real.

## 3. Conta e token (a pessoa faz)

1. Criar a conta em apify.com (plano Free, sem cartão).
2. No Console, em Settings > API & Integrations, copiar o token pessoal.
3. Guardar em variável de ambiente, nunca no chat:
   - Mac e Linux: `export APIFY_TOKEN="..."` (para ficar, no arquivo do terminal)
   - Windows (PowerShell): `setx APIFY_TOKEN "..."`, e abrir um terminal novo.
   Você só testa se a variável existe, sem mostrar o valor.

## 3b. Achar posts com conversa de verdade (fase 2)

A busca de posts **já é uma coleta que cobra**: estime e peça o "pode" antes, como em qualquer rodada.

- Procure conteúdo feito **para o avatar**: criadores e páginas que falam do problema dele, com termos nas palavras
  do avatar. **Não use hashtag de produto** (`#bolonopote`, `#festinha`): traz post de vendedor, com foto bonita e
  quase nenhum comentário de cliente. No teste, 10 posts de hashtag de produto tiveram 0 a 4 comentários cada.
- Rode `apify~instagram-hashtag-scraper` com `"keywordSearch": true` e termos do problema, e ordene o resultado por
  `commentsCount`. Piso sugerido: 30 ou mais comentários. Os campos `commentsCount` e `latestComments` servem de
  amostra sem custo extra. Atenção: `latestComments` pode vir vazio mesmo com `commentsCount` alto (no teste, veio
  vazio em todos os 20 posts), então não conte com ele.
- **Duas buscas por rede, no máximo.** Se nenhum post tiver conversa, diga isso e ofereça o YouTube (grátis) ou
  colar.
- Avise: no Instagram a maior parte dos comentários costuma ser elogio e marcação de amigo (no teste, 1 útil em 16).
  Vídeos do YouTube sobre o problema rendem mais texto por comentário.

## 4. Caminho C1: pelo terminal (API)

Rota síncrona, que roda o actor e devolve a tabela na mesma chamada
(https://docs.apify.com/api/v2/act-run-sync-get-dataset-items-post):

```
curl -s -X POST "https://api.apify.com/v2/actors/DONO~ACTOR/run-sync-get-dataset-items?timeout=240&maxTotalChargeUsd=0.5" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{ ...entrada... }' -o acha-clientes/bruto/ARQUIVO.json
```

Pontos: o nome do actor usa `~` no lugar da barra (`apify~instagram-comment-scraper`). A resposta de sucesso é 201.
A chamada síncrona dá erro 408 se passar de 300 segundos; use poucos itens por chamada. Erros: 401 token ruim, 402
sem crédito, 400 entrada inválida. A documentação oficial não detalha o cabeçalho de autenticação na página que
consultei; o `Authorization: Bearer` é o formato do Apify para o token, e se der 401 confira o token. No Windows
sem `curl`, peça para usar `curl.exe` no PowerShell.

**Entradas, lidas nas páginas oficiais dos actors em 14/11/2026.** Antes de rodar, abra o input schema do actor
(`https://apify.com/DONO/ACTOR/input-schema`) e confirme que os nomes não mudaram. Se não conseguir abrir, leia o
schema pelo MCP da Apify (ferramenta de detalhes do actor) ou pergunte à pessoa antes de rodar.

- Comentários do Instagram (`apify~instagram-comment-scraper`):
  `{"directUrls": ["https://www.instagram.com/p/CODIGO/"], "resultsLimit": 50}`.
  `resultsLimit` é por URL. Respostas aninhadas só em plano pago, então ficam de fora.
  Saída: `id`, `text`, `ownerUsername`, `timestamp`, `likesCount`, `repliesCount`.
- Posts do Instagram por hashtag (`apify~instagram-hashtag-scraper`):
  `{"hashtags": ["termo"], "resultsType": "posts", "resultsLimit": 20}`. Com `"keywordSearch": true`, busca por
  palavra e não por hashtag. Saída: `url`, `caption`, `commentsCount`, `likesCount` (-1 se oculto),
  `ownerUsername`, `timestamp`, `type`.
- Comentários do TikTok (`clockworks~tiktok-comments-scraper`):
  `{"postURLs": ["https://www.tiktok.com/@usuario/video/ID"], "commentsPerPost": 50}`.
  Saída: `text`, `diggCount`, `createTimeISO`, `uniqueId`, `cid`, `videoWebUrl`.
- Busca de vídeos no TikTok (`clockworks~tiktok-scraper`): não conferi a entrada de busca; leia o input schema.

O script `juntar_comentarios.py` (na pasta da skill, a pasta onde está o `SKILL.md`) entende essas saídas. Se o JSON dos comentários do Instagram não trouxer o link do
post, rode com `--link-post URL` numa pasta que tenha só aquele post. Isso é importante: o `link_origem` é
obrigatório. O link do comentário pode não existir no Instagram e no TikTok; nesse caso use o link do post e
escreva "link do post" em `observacao` na fase 5.

## 5. Caminho C2: pelo MCP da Apify (claude.ai ou ferramentas)

O servidor MCP da Apify fica em `https://mcp.apify.com`, com login por OAuth (sem colar token), e também aceita
token no cabeçalho (https://docs.apify.com/platform/integrations/mcp). No claude.ai, entra como conector
personalizado em Customize > Connectors, com esse endereço. No Claude Code, o comando exato não foi verificado:
peça ao Claude para "adicionar o servidor MCP da Apify (https://mcp.apify.com)" e siga o que ele mostrar. Com o
conector ligado, você chama os mesmos actors pelas ferramentas, com a mesma estimativa e a mesma confirmação, e
salva o resultado em `acha-clientes/bruto/` (ou, no claude.ai, vai direto para o `comentarios.csv`).

## 6. Dados do perfil público dos leads quentes (fase 5, opcional)

Só com confirmação, e só para os leads quentes. Use `apify~instagram-scraper` (US$ 2,70 por 1.000) ou o actor de
perfil do TikTok com a lista de perfis, leia o input schema antes, e traga apenas nome exibido e descrição.
Estime: 20 perfis custam bem menos de US$ 0,10 nesses preços, mas confira o schema, porque alguns modos cobram
também por posts do perfil. Não colete e-mail, telefone nem lista de seguidores.
