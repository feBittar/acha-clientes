# Fontes e créditos

Consultadas em 14/11/2026. Preço e regra de plataforma mudam: confira na fonte antes de decidir.

## Método, com crédito

Nenhum trecho foi copiado. Foi usado o método, reescrito.

1. **coreyhaines31/marketingskills**, https://github.com/coreyhaines31/marketingskills. 60.322 estrelas, licença
   MIT (API do GitHub, 14/11/2026). Skills `customer-research`, `prospecting` e `offers`. Usado: começar pela pesquisa
   do cliente e deixar a oferta para depois.
2. **ScrapeCreators/social-media-research-skills**, https://github.com/ScrapeCreators/social-media-research-skills.
   6.465 estrelas, MIT (14/11/2026). Skills `comment-mining` e `outlier-post-finder`. Depende de uma API paga; só o
   método serve: achar posts que fogem da média e minerar os comentários.
3. **cmj-hub/claude-psp**, https://github.com/cmj-hub/claude-psp. 3 estrelas, MIT (14/11/2026). Usado: o perfil de
   sinal de dor, com a frase exata da pessoa.
4. **anthropics/skills**, https://github.com/anthropics/skills. 194.573 estrelas (14/11/2026), sem licença no nível
   do repositório. Usado só como referência de formato de skill; nada foi copiado.
5. **yt-dlp**, https://github.com/yt-dlp/yt-dlp. Programa livre usado para buscar vídeos e baixar comentários
   (versão 2026.10.26 nos testes). O número de estrelas é só um sinal de popularidade, e não de qualidade.
6. **egbertbouman/youtube-comment-downloader**, https://github.com/egbertbouman/youtube-comment-downloader.
   1.275 estrelas, licença MIT (API do GitHub, 14/11/2026); versão 0.1.84 no PyPI. Usado como instalação, sem
   cópia de código: baixa os comentários do YouTube sem login e funcionou onde o yt-dlp falhou.

## Preços, cotas e documentação

- Apify, planos: https://apify.com/pricing. Free com US$ 5 de uso por mês, sem cartão (só se a conta for do plano gratuito; consulte `GET https://api.apify.com/v2/users/me/limits`, campos `data.limits.maxMonthlyUsageUsd` e `data.current.monthlyUsageUsd`, funcionou no teste).
- Actors e preços por 1.000 itens (14/11/2026): `apify/instagram-comment-scraper` US$ 2,60;
  `apify/instagram-scraper` US$ 2,70; `apify/instagram-hashtag-scraper` US$ 2,60; `clockworks/tiktok-scraper` "a
  partir de" US$ 1,70; `clockworks/tiktok-comments-scraper` "a partir de" US$ 0,50 (a página mostra também um valor
  antigo de US$ 5 por 1.000 na FAQ; preço no plano Free não verificado).
  Campos de entrada e saída conferidos nas páginas `https://apify.com/<dono>/<actor>/input-schema`.
- API síncrona da Apify: https://docs.apify.com/api/v2/act-run-sync-get-dataset-items-post (rota
  `/v2/actors/<dono>~<actor>/run-sync-get-dataset-items`, parâmetros `timeout`, `limit`, `format`; resposta 201; 408
  acima de 300 s). A mesma página lista o parâmetro `maxTotalChargeUsd` ("custo máximo total do run"), não testado
  aqui. Formato exato do cabeçalho de autenticação não confirmado na página lida.
- MCP da Apify: https://docs.apify.com/platform/integrations/mcp (servidor `https://mcp.apify.com`, OAuth ou token).
  Comando para Claude Code não verificado.
- Cota do YouTube Data API: https://developers.google.com/youtube/v3/determine_quota_cost (10.000 unidades por dia;
  `commentThreads.list` custa 1).
- Termos: https://www.youtube.com/t/terms (YouTube); termos do TikTok, seção 5; User Agreement do LinkedIn, item 8.2;
  Instagram, cláusula não verificada ao vivo.
- LGPD, art. 7º, §§ 3º e 4º: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm

## Testes de 14/11/2026

- yt-dlp: busca (`ytsearch5`) funcionou; coleta de comentários falhou em IP de datacenter com "Sign in to confirm
  you’re not a bot" (apóstrofo curvo) e aviso de JavaScript runtime ausente (ignorável na busca).
- youtube-comment-downloader 0.1.84: `--limit 100 --sort 0` baixou 30 comentários em 2 s, sem login, na mesma
  máquina onde o yt-dlp falhou nos comentários.
- Apify: busca por hashtag, 10 posts, US$ 0,023; 16 comentários de 4 posts, US$ 0,037; `usageTotalUsd` demorou
  alguns minutos para aparecer. Instagram: 1 comentário útil em 16.
- Reddit: o JSON público respondeu 403; o RSS de subreddit respondeu 200.
- Rodada 2 (YouTube, 3 vídeos, 93 comentários, sem Apify): `yt-dlp ... --print "%(comment_count)s"` falhou com o erro
  de bot nos 12 vídeos; o `youtube-comment-downloader` só dá tempo relativo ("4 years ago", às vezes "(edited)").
- `--sort 1` (recentes) do `youtube-comment-downloader` funcionou (8 comentários, ordem diferente de `--sort 0`).
- `yt-dlp --extractor-args "youtube:lang=pt"` na busca `ytsearch5` devolveu títulos em português, com aviso e o
  canal como `NA`; `lang=pt-BR` deu erro (a lista de códigos aceitos inclui `pt` e `pt-PT`). O filtro de idioma da
  busca não existe, então o idioma se confere pelo título e pela amostra.
- `curl` na página `https://www.youtube.com/channel/<ID>` de um canal grande trouxe `og:title` e `og:description`
  (HTTP 200, sem login). Não testado com canal de pessoa comum.

## Não verificado

Leitura do canal de pessoa comum (sem descrição, consentimento, limite de chamadas); `--sort 1` em vídeo com muito
comentário novo; Windows e PowerShell; "Sem terminal" e "Modo demonstração" em uso real; preço exato do TikTok no plano Free; cláusula do Instagram; comando do MCP da Apify no Claude Code; cabeçalho de
autenticação na página da API; `maxTotalChargeUsd` em uso real; `youtube-comment-downloader` e yt-dlp em
computador doméstico e no Windows; link individual de comentário no
Instagram e no TikTok.

O jeito de agir (entender antes de instalar) vem do posicionamento do @ofelipemart.
