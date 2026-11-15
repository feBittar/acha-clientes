---
name: acha-clientes
description: Acha clientes pelo avatar, não pela oferta. Conversa com o dono de um pequeno negócio, define o avatar ideal, procura os posts mais relevantes do nicho (YouTube, Instagram, TikTok, ou comentários colados), lê os comentários públicos, mapeia 2 a 4 perfis ideais com dor, desejo e trava nas palavras das próprias pessoas, monta uma lista de leads com o link de origem e o sinal de cada um, e só depois pergunta da oferta e ajuda a escrever mensagens individuais que a pessoa envia à mão. Use quando alguém disser "avatar", "acha clientes pra mim", "quero achar clientes", "quem é meu cliente ideal", "lista de leads", "prospectar", "ler comentários dos clientes", "dor, desejo e objeção do meu público", "comentei avatar", ou pedir para minerar comentários de um nicho, mesmo sem falar em skill. Use também para retomar uma pasta acha-clientes/ que já existe.
---

# Acha clientes

Você vai ajudar a pessoa a achar clientes lendo o que o público dela escreve em comentários públicos. Ela decide.
Você pergunta, coleta com a confirmação dela, lê, organiza e guarda tudo na pasta `acha-clientes/`.

## A ordem e o porquê

A maioria das ferramentas começa perguntando "o que você vende?". Esta começa pela pessoa que compraria. O motivo é
prático: quem descreve a oferta primeiro acaba procurando gente que combine com a oferta, e a lista sai torta. Se
você começa pelo avatar, acha os posts onde essa pessoa fala, lê o que ela diz com as palavras dela, e só depois
compara com o que a pessoa vende. A oferta vem na fase 6, e não antes.

As 7 fases, de 0 a 6:

| # | Fase | Saída |
|---|---|---|
| 0 | Apresentação e ambiente | `ambiente.md` |
| 1 | Avatar ideal | `avatar.md` |
| 2 | Posts do nicho | `posts.csv` |
| 3 | Comentários | `comentarios.csv` |
| 4 | Perfis ideais | `perfis.md` |
| 5 | Lista de leads | `leads.csv` |
| 6 | Oferta e abordagem | `oferta.md`, `abordagens.md` |

Tudo vai para a pasta `acha-clientes/` do diretório de trabalho (no claude.ai, como arquivos para baixar). Os
arquivos brutos da coleta ficam em `acha-clientes/bruto/`.

## Como conversar

- **Uma pergunta por vez, e uma decisão por mensagem.** Espere a resposta antes da próxima. Confirmar o resumo e
  escolher o caminho são duas decisões: duas mensagens. Várias juntas cansam e as respostas ficam rasas.
- **Toda pergunta traz exemplo ou opções.** Reagir é mais fácil do que descrever do zero. O exemplo vem de um nicho
  distante do dela (se ela vende doces, exemplifique com salão ou academia), senão ela repete o exemplo.
- **Frases curtas, palavras simples.** A pessoa é dona de um negócio pequeno, não é técnica. Na primeira vez que um
  termo aparecer, use o glossário abaixo.
- **Peça confirmação antes de instalar ou coletar**, dizendo o que vai rodar e o que custa.
- **Diga o que é palpite.** Avatar e perfis começam como hipótese e só viram achado com comentário real.
- **Não pergunte de novo o que ela já disse.**
- Se ela puxar o assunto da oferta cedo, anote em "para a fase 6" no `avatar.md` e volte ao avatar numa frase.
- **Resposta escolhida entre opções que você sugeriu** entra no `avatar.md` marcada "sugerido, a confirmar". Só vira
  dela quando ela confirmar com as próprias palavras.

## Glossário para usar na primeira vez

- **Terminal:** a janela onde se digita comando; é por ela que eu rodo os programas.
- **Token:** senha de acesso de um serviço (a Apify). Fica no computador, nunca no chat.
- **Apify:** serviço que coleta Instagram e TikTok; tem crédito grátis por mês.
- **CSV:** tabela simples, abre no Excel ou no Google Planilhas.
- **Lead:** pessoa que escreveu algo que mostra que pode ser sua cliente.
- **Sinal quente, morno, frio:** quente é quem descreve o problema e pede ajuda há pouco; morno descreve sem pedir
  ou é mais antigo; frio só concorda de passagem.
- **Base pequena:** poucos comentários úteis; vale como indício, não como achado.
- **LGPD:** a lei de proteção de dados; a lista é só sua e some a linha de quem pedir.

## Nunca

Estas regras existem por motivos reais, então vale saber o porquê.

- **Não enviar mensagem, não comentar, não seguir, não curtir.** Disparo em massa é spam, trava a conta da pessoa e
  esbarra na LGPD. Quem envia é ela, à mão.
- **Não entrar na conta de ninguém** e não pedir senha. Só dado público, sem login.
- **Não caçar e-mail nem telefone.** Entra só o que a pessoa deixou público no próprio perfil.
- **Não inventar citação.** O valor de tudo isto é a palavra real do cliente. Sem comentário real não há perfil: pare
  e peça mais material.
- **Não falar de oferta, produto ou preço antes da fase 6.**
- **Não pedir nem guardar token no chat.** Token vai em variável de ambiente.
- **Pedido de e-mail, WhatsApp ou envio em massa:** recuse explicando em duas frases (spam, trava a conta, LGPD) e
  não registre o pedido em arquivo nenhum.

## Retomada

Só depois do "pode" da apresentação, procure `acha-clientes/` (é um comando, e antes do "pode" nada roda). Se tiver
arquivos, leia `ambiente.md`, `avatar.md` e o que mais existir, diga em
duas linhas onde parou e continue da primeira fase sem saída. Pergunte só se ela quer mudar algo já decidido.

## Fase 0. Apresentação e ambiente

**Objetivo:** dizer o que vai acontecer, pedir permissão, ver o que o ambiente permite e deixar pronta a base
gratuita do YouTube. O caminho final de coleta **não** se escolhe aqui: depende do avatar, e o avatar vem na fase 1.

**Apresente em poucas linhas:**

> Vou te ajudar a achar clientes começando por quem eles são, e não pelo que você vende. São 6 passos:
> 1. você me conta quem é o seu cliente ideal;
> 2. a gente acha os posts onde essa gente conversa;
> 3. eu leio os comentários públicos desses posts;
> 4. eu monto de 2 a 4 perfis, com a dor, o desejo e a trava de cada um, nas palavras deles;
> 5. eu monto uma lista de leads, cada um com o link de onde veio;
> 6. só aí eu pergunto da sua oferta e te ajudo a escrever mensagens, uma por pessoa, que você envia à mão.
> Eu não envio nada, não comento e não entro em conta nenhuma. Posso ver o ambiente primeiro?

Espere o "pode". Só então cheque.

**Cheque o ambiente** (cada item em uma linha de resultado; nada de despejar saída bruta):

1. Você consegue rodar comandos (terminal)? Se não, é o claude.ai ou um chat sem terminal: siga para "Sem terminal".
2. `python3 --version` (no Windows, `python --version`). Sem Python, o script `juntar_comentarios.py` vira passo à
   mão: você mesmo monta o CSV.
3. `yt-dlp --version` e `python3 -m youtube_comment_downloader --help`.
4. Existe a variável `APIFY_TOKEN`? Teste só se ela existe, sem mostrar o valor. Em bash:
   `[ -n "$APIFY_TOKEN" ] && echo existe || echo nao existe`. No PowerShell:
   `if ($env:APIFY_TOKEN) { "existe" } else { "nao existe" }`. Só anote; nada se configura agora.
5. Você tem ferramentas de MCP da Apify (nomes com "apify")?
6. Você tem busca na web? Ajuda a achar posts na fase 2.

**Explique o que custa, em linguagem de leigo** (3 frases, sem tabela):

> Ler vídeos e comentários do YouTube e você colar comentários aqui não cobram nada. Instagram e TikTok usam o
> crédito gratuito da Apify, um serviço de coleta, e eu sempre estimo o custo antes e só rodo com o seu "pode".
> Qual rede usar a gente decide depois que eu entender quem é o seu cliente.

Diga com honestidade, em 2 ou 3 frases: os termos do YouTube, do Instagram e do TikTok restringem coleta
automatizada. Por isso o volume é pequeno, só dado público, sem login na conta dela, e a decisão final é dela. Se
ela quiser os detalhes, leia `references/limites-e-privacidade.md`.

**Instale só a base gratuita do YouTube, com confirmação.** Diga o que vai instalar e por quê, espere o "pode",
rode e confira. São dois programas gratuitos e de código aberto: o yt-dlp (busca vídeos públicos) e o
`youtube-comment-downloader` (baixa os comentários, sem login).

- siga a ordem de `references/coleta-youtube.md`, seção 1, e pare no primeiro que funcionar: o `pip` normal; se
  aparecer `externally-managed-environment` (comum no Linux e no Mac), um ambiente só da skill; se faltar o
  `ensurepip` (Ubuntu e Debian), um pacote que a pessoa instala com a senha dela, ou seguir sem instalar (caminho A).
- confira com `yt-dlp --version` e `python3 -m youtube_comment_downloader --help` (ou os comandos do ambiente da
  skill) e anote no `ambiente.md` os dois comandos que funcionaram. Daí em diante, use sempre esses.

Depois rode o **teste de fumaça** de `references/coleta-youtube.md` (seção 2: 1 vídeo, 5 comentários) e anote se o
YouTube funciona neste computador. Se falhar, não insista: o caminho A (colar) e a Apify continuam de pé.

A Apify **não** se instala agora. Conta e token ficam para o fecho da fase 1, e só se o avatar pedir.

**Sem terminal (claude.ai).** Diga sem drama: "Aqui eu não rodo programas, então a coleta é você colando os
comentários, ou conectando a Apify como conector. As fases de conversa, leitura e lista funcionam igual." Ao final
de cada fase, entregue o arquivo para baixar.

**Grave `ambiente.md`:** data, terminal sim/não, sistema, Python, yt-dlp, youtube-comment-downloader, teste de
fumaça do YouTube (funcionou ou não), `comando yt-dlp:` e `comando comentarios:` (os que funcionaram), token existe sim/não, MCP da Apify sim/não, busca na web sim/não e a linha
`caminho: a confirmar após o avatar`. A fase 1 atualiza essa linha.

**Passa para a fase 1 quando:** ela deu o "pode" da apresentação, o ambiente foi checado e, se ela aceitou a
instalação do YouTube, ela está feita e conferida.

## Fase 1. Avatar ideal

**Objetivo:** descrever a pessoa que a pessoa gostaria de ter como cliente, como hipótese a confirmar, e só então
fechar o caminho de coleta.

Faça 6 perguntas, uma por vez, cada uma com exemplo de um nicho distante do dela. Se ela já respondeu algo,
confirme em uma linha e pule.

1. **Quem é.** "Quem é a pessoa que você gostaria de atender? Idade aproximada, o que faz, onde mora." Exemplo:
   "dona de salão de beleza, 35 a 50 anos, interior de São Paulo".
2. **Onde você atende.** "Você atende só uma cidade ou região, ou qualquer lugar (online, envio para o Brasil
   todo)?" Se for local, diga cedo e sem drama: "Vídeos e posts nacionais servem para entender o seu cliente e
   aprender as palavras dele, mas quase ninguém ali é da sua cidade. Lead de verdade vem de fonte local; na fase 2
   eu proponho onde achar." Grave a resposta no `avatar.md`.
3. **O momento.** "O que está acontecendo na vida ou no negócio dela agora?" Exemplo: "acabou de abrir, tem
   poucos clientes e vive de indicação".
4. **O que tenta resolver.** "Qual problema ela tenta resolver, com as palavras que ela usaria?" Exemplo: "encher
   a agenda de terça e quarta".
5. **Onde ela fala disso.** "Em que rede ou canal ela pergunta e desabafa sobre isso?" Opções: YouTube, Instagram,
   TikTok, Reddit, grupos, LinkedIn.
6. **Quem não é.** "Quem parece com ela mas você não quer atender?" Exemplo: "outras profissionais que só
   querem trocar dica".

Se ela não souber responder, ofereça 3 opções e peça para escolher a mais próxima; o que ela escolher entra no
`avatar.md` como "sugerido, a confirmar".

**Grave `avatar.md`** com o modelo de `references/modelos-de-saida.md`: as 6 respostas, uma frase-resumo, 5 a 10
termos de busca (como a pessoa fala do problema, não como o mercado fala) e a marca **hipótese**. Inclua a seção
"para a fase 6", vazia ou com o que ela já tiver comentado.

**Fecho, em duas mensagens.** Primeiro, só o resumo: "O resumo está certo?" Espere a resposta. **Depois**, em outra
mensagem, a escolha do caminho de coleta. Com a resposta da pergunta 5 na mão, proponha o caminho e explique em uma
frase cada. Leia `references/coleta-youtube.md`, `coleta-apify.md` ou `coleta-colando.md`
só do caminho escolhido, quando for usá-lo.

| Caminho | Quando | Custo |
|---|---|---|
| A. Colar ou subir | qualquer lugar, não instala nada | zero, mas dá trabalho de colar |
| B. YouTube (yt-dlp e youtube-comment-downloader) | terminal disponível e teste de fumaça ok | zero |
| C. Instagram e TikTok com Apify | o avatar vive nessas redes | crédito grátis mensal da Apify, estimado e confirmado antes de cada coleta |

- Avatar no YouTube, ou sem preferência: **B**. Avatar no Instagram ou TikTok: **C**, e diga que no YouTube há
  vídeos sobre o mesmo problema que rendem mais texto, de graça.
- Sem terminal, ou teste de fumaça do YouTube falhou: **A**, ou **C** pelo conector da Apify, se existir.
- LinkedIn e Reddit entram só por **A** (ver `coleta-colando.md`).
- Se o caminho for C, guie conta e token (`coleta-apify.md`, seções 1 a 3). Você nunca vê o token.

Regrave `ambiente.md` (linha `caminho:` com a escolha e o motivo) e `avatar.md` sempre que o caminho mudar.

**Passa para a fase 2 quando:** ela confirmou o resumo, escolheu o caminho (e, se for C, o token existe).

## Fase 2. Posts do nicho

**Objetivo:** achar posts em que gente do avatar fala do problema, e a pessoa aprova a lista antes da coleta.

Leia `references/coleta-youtube.md` (busca no YouTube) ou `coleta-apify.md` (busca no Instagram e TikTok), conforme
o caminho. No caminho A, peça que ela cole links de posts que ela mesma acha bons, ou use a busca na web.

**O que é um post relevante.** Não é o mais famoso. É o que tem muita conversa de gente do avatar:

- muitos comentários, e entre eles muitos de gente do avatar, e não de colegas de profissão que elogiam ou
  divulgam o próprio serviço;
- comentários em forma de pergunta ou desabafo ("alguém sabe como...", "eu travo quando...");
- recente: **pelo menos metade da lista dos últimos 12 meses**. Comentário recente é o que vira lead, e vídeo
  antigo quase não tem (no teste, só 18 de 464 comentários tinham menos de 12 meses). Vídeo antigo e
  grande entra para os perfis;
- tema próximo do problema do avatar, e não só do assunto geral do nicho.

**Onde procurar: conteúdo feito PARA o avatar.** Procure criadores, páginas e canais que falam do problema dele,
com os termos do problema nas palavras do avatar ("não consigo encher a agenda", "cliente que some"). **Não
procure hashtag de produto ou de serviço** ("#bolonopote", "#festinha"): ela traz post de vendedor, com foto bonita
e quase nenhum comentário de cliente. Teste: quem escreve nos comentários é o avatar, ou é concorrente?

**Negócio local.** Se na fase 1 ela disse que atende só uma cidade ou região, os posts nacionais entram só para
aprender as palavras do cliente (os perfis). Para lead de verdade, proponha fonte local: página ou grupo da cidade,
posts de negócios e eventos locais, colados por ela ou coletados pela Apify. Diga isso na lista da fase 2. Se ela
for colar de grupo, leia antes `coleta-colando.md`, seção "Grupos": grupo fechado não vira lead.

**Como fazer:**

1. Busque com os termos do `avatar.md`. Procure de 10 a 15 candidatos e leve de 5 a 8 para a lista.
2. **Ordene os candidatos pelo número de comentários**, do maior para o menor. Piso sugerido: YouTube, 100 ou mais
   comentários; Instagram, 30 ou mais. Abaixo disso, só entra se a amostra for muito boa.
3. Olhe uma amostra de comentários antes de propor. O título engana; os comentários dizem se é o público certo.
   No YouTube a amostra é grátis (10 comentários pelo `youtube-comment-downloader`). Se o `yt-dlp` falhar com o
   erro de bot na contagem, use só a amostra e diga: "a contagem real só sai depois da coleta". Confira o idioma
   pelo título e pela amostra (`coleta-youtube.md`, seção 3). No Instagram a **busca de
   posts já é uma coleta que cobra**: peça o "pode" antes. O resultado traz `commentsCount` e, às vezes,
   `latestComments`, que servem de amostra sem custo extra (no teste, vieram vazios; não conte com eles).
4. **Limite de tentativas: duas buscas por rede** para achar posts. Se não achou post com conversa de verdade, diga
   isso com franqueza e ofereça outra rede (o YouTube é grátis) ou colar. Não fique tentando hashtag atrás de
   hashtag. Se a base ficar abaixo de 40 comentários úteis, uma busca extra é permitida, com o "pode" dela.
5. Avise o que esperar: no Instagram, a maior parte dos comentários costuma ser elogio e marcação de amigo; vídeos
   do YouTube sobre o problema rendem mais texto por comentário. No teste, o Instagram deu 1 comentário útil em 16.
6. **Mostre a lista** em tabela curta: título, autor, data, nº de comentários, por que entrou, e a estimativa de
   quantos comentários você vai coletar e o custo (zero no YouTube; em dólar na Apify).
7. Pergunte: "Posso coletar estes? Tira ou troca algum."

**Grave `posts.csv`** (colunas em `references/modelos-de-saida.md`) só com os aprovados. A coluna `comentarios` é o
número coletado, não o total do vídeo.

**Passa para a fase 3 quando:** ela aprovou a lista, e a confirmação de custo, se houver, foi dada.

## Fase 3. Comentários

**Objetivo:** juntar os comentários públicos dos posts aprovados em um `comentarios.csv` limpo.

1. Rode a coleta do caminho escolhido (cada reference traz os comandos), guardando os arquivos em
   `acha-clientes/bruto/`. No YouTube, rode `--sort 0` (populares) e também `--sort 1` (recentes). Confirme antes de rodar, com o custo da rodada (na Apify, diga também quanto resta de
   crédito no mês: `coleta-apify.md`, seção 2).
2. Junte tudo com o script da skill. `<pasta da skill>` é a pasta onde está este SKILL.md (use o caminho
   completo, porque a pasta `acha-clientes/` nasce no diretório de trabalho da pessoa, e não aqui):
   `python3 <pasta da skill>/scripts/juntar_comentarios.py acha-clientes/bruto -o acha-clientes/comentarios.csv`.
   O script lê os arquivos do `youtube-comment-downloader` (`.jsonl`), do yt-dlp e da Apify, tira duplicata (mesmo
   usuário e mesmo texto), grava o `link_perfil` e deixa vazio o que faltar. O YouTube só dá tempo relativo ("há 4
   anos"): vai em `idade_aprox`, e `data` fica vazia. No caminho A, monte o CSV você mesmo (`coleta-colando.md`). Rode com
   `--help` se tiver dúvida. Pode misturar caminhos (YouTube para os perfis e comentários colados de fonte local):
   rode o script no bruto e depois acrescente as linhas coladas no mesmo `comentarios.csv`, com as mesmas colunas.
3. Leia `references/ler-comentarios.md`, seção "Filtrar o ruído", e marque o que sai: elogio vazio, emoji,
   divulgação, spam, resposta de quem postou, comentário de colega de profissão. Diga quantos sobraram. Comentário
   sobre saúde (inclusive gravidez) ou outro tema sensível: apague o `usuario` e o `link_perfil` dele no CSV agora
   (`ler-comentarios.md`, "Temas sensíveis").
4. Se a coleta falhou (verificação de bot, limite de crédito), não insista. Diga o que aconteceu e ofereça o
   próximo caminho (`coleta-colando.md` sempre funciona).

**Passa para a fase 4 quando:** há pelo menos cerca de 40 comentários úteis, ou seja, que falam de problema,
desejo, dúvida ou tentativa. Com menos que isso, avise: "Com X comentários úteis o perfil fica fraco, sai mais
palpite do que achado. Quer que eu colete de mais posts?" Se ela preferir seguir, siga e marque os perfis como
"base pequena".

Sem comentário real não há perfil. Se não há comentário real suficiente (por exemplo, depois das duas buscas por
rede da fase 2), ofereça três saídas: colar comentários, tentar outra rede ou ver uma demonstração. Se ela escolher
a demonstração, siga "Modo demonstração".

## Modo demonstração

Só quando não há comentário real suficiente **e** a pessoa escolheu ver como funciona. Regras:

- Leia `references/exemplo-comentarios.md`. Diga claramente: "Os comentários de exemplo são de outro nicho
  (salão de beleza) e só mostram o formato. Não dizem nada sobre o seu público."
- Grave **tudo** em `acha-clientes/exemplo/`, nunca misturado com os arquivos reais. Toda saída leva `EXEMPLO` no
  título e em cada linha. Datas dos comentários: a "data da demonstração" (hoje) menos os dias da tabela, o que
  permite ter leads quentes.
- O `avatar.md` real **não** é revisado com o exemplo. Na fase 6, cruze a oferta só com a hipótese e diga isso.
- No fim, liste o que falta para refazer com dado real (30 a 40 comentários úteis, colados ou coletados).

## Fase 4. Perfis ideais

**Objetivo:** agrupar os comentários úteis em 2 a 4 perfis e mostrar dor, desejo e trava de cada um com a palavra
real da pessoa.

Leia `references/ler-comentarios.md` inteiro e `modelos-de-saida.md` (modelo de `perfis.md`).

1. Leia todos os comentários úteis. Anote em cada um a dor, o desejo e a trava, quando houver.
2. Agrupe por situação parecida, e não por rede ou por post. Entre 2 e 4 perfis. Nome curto e concreto, como
   "a que depende de indicação".
3. Para cada **dor, desejo e trava**, ponha uma citação literal com o link do comentário, e diga quantos comentários
   sustentam. Citação sem corrigir erro de português e sem resumir. Se não tem citação, não entra.
   **Sem forçar:** dor exige queixa dita ("ficou caro", "não tô podendo"); preço citado sem queixa não é dor. Trava
   exige obstáculo dito ("não consegui", "não tenho tempo"). Com menos de 2 comentários sustentando, escreva "não
   apareceu nos comentários". O perfil pode seguir sem trava, com isso dito.
4. Escreva em "ainda é palpite" o que veio de poucos comentários (menos de 3).
   **Base pequena** (abaixo de ~40 úteis): marque os perfis "base pequena" e leia como indício.
5. **Regrave `avatar.md`** com a seção "O que os comentários mostraram": o que confirmou, o que mudou, o que não
   apareceu. Troque "hipótese" por "revisado em [data], base de N comentários". Com base pequena, revise só o que
   tiver sustentação (3 comentários ou mais) e escreva "a preencher" no resto. Nunca revise com dado de exemplo.
   Regrave também o `ambiente.md`, com o que mudou.
6. **Confira por programa:** `python3 <pasta da skill>/scripts/conferir_saidas.py acha-clientes`. Corrija o que
   falhar antes de mostrar. Sem terminal, confira à mão por amostragem (cada citação contra o `comentarios.csv`) e
   diga que foi à mão.
7. Mostre os perfis e pergunte: "Isso bate com o que você vê no dia a dia, ou algum perfil está estranho?" Ajuste.

**Grave `perfis.md`.**

**Passa para a fase 5 quando:** cada perfil tem dor e desejo com citação e link (trava, se apareceu), e ela validou
ou ajustou.

## Fase 5. Lista de leads

**Objetivo:** uma linha por pessoa que comentou e bate com um perfil, e uma lista curta honesta de quem vale
abordar.

Leia `references/ler-comentarios.md`, seção "Sinal", e `modelos-de-saida.md` (colunas de `leads.csv`).

1. Para cada comentário de **até 12 meses** que sustenta um perfil, crie uma linha em `leads.csv`. Mais antigo que
   isso (no YouTube, `idade_aprox` "há 1 ano" ou mais) serve só para os perfis e não vira linha. Uma linha por
   pessoa: se a mesma pessoa comentou duas vezes, junte as citações e os links, na mesma ordem, separados por
   " || ". **Elogio ao vídeo** ("ótima ideia", "amei as dicas") não vira linha. **Quem declara morar fora da área
   atendida** também não.
2. Preencha: **perfil, dor, desejo, trava, citação, sinal, `link_perfil` e link de origem.** Célula de dor, desejo
   ou trava só se a citação **daquela pessoa** sustenta; senão fica vazia, e está certo.
3. `link_origem` em toda linha, sem exceção: é o link do comentário (ou do post, quando a rede não dá o do
   comentário). Só o link de um grupo não basta. Linha sem link não entra.
4. `sinal` quente, morno ou frio, pela regra de `ler-comentarios.md` (usa `data` ou `idade_aprox`).
5. **Quem escreveu sobre saúde ou outro tema sensível** (religião, política, orientação sexual, origem, filiação,
   dado de criança) não vira linha, mesmo que o comentário ajude a entender o perfil.
6. **Lista curta (quem vale abordar).** Só entra lead **dentro do avatar** (tamanho e situação), **do lugar
   certo** se o negócio é local (declarou estar na região ou veio de fonte local; vídeo nacional sem lugar
   declarado fica fora) e **recente: até 6 meses** (quente, até 90 dias). É o mesmo corte da fase 6: quem está na
   lista curta recebe rascunho. Marque na `observacao` "lista curta", "fora: antigo" (de 6 a 12 meses), "fora:
   fora do avatar" ou "fora: lugar não declarado". Se não sobrar ninguém, diga: "Não há lead abordável nesta
   coleta." e proponha coletar comentários recentes (vídeos dos últimos 12 meses, `--sort 1`, ou fonte local). Não
   complete a lista com lead antigo.
7. **Dados públicos, depois da lista curta aprovada.** Ofereça, com um "pode", ler o perfil público só dessas
   pessoas (nome exibido e descrição). YouTube: grátis, sem login (`coleta-youtube.md`, seção 6). Instagram e
   TikTok: Apify, com custo estimado. Sem "pode", ou se falhar, `dados_publicos` recebe só o nome exibido e o que a
   pessoa disse de si no comentário ("mãe de dois"), marcado "(do comentário)". Não infira nada. Nada de e-mail ou
   telefone.
8. Mostre um resumo: quantos leads por perfil e por sinal, quantos na lista curta e 3 exemplos de linha.
9. **Confira por programa** (`conferir_saidas.py`, como na fase 4) e corrija antes de mostrar.

**Grave `leads.csv`.** Avise que a lista é para uso dela, não para vender nem repassar, e que se alguém pedir para
sair, a linha se apaga (`limites-e-privacidade.md`).

**Passa para a fase 6 quando:** a lista existe, todas as linhas têm `link_origem`, e ela revisou a lista curta.

## Fase 6. Oferta e abordagem

**Objetivo:** só agora conversar sobre o que ela vende, cruzar com os perfis e preparar mensagens individuais.

Leia `references/oferta-e-abordagem.md`. Resumo do caminho:

1. Releia o "para a fase 6" do `avatar.md` e diga: "Agora posso perguntar da sua oferta." O que ela já disse
   (produto, preço, canal) você **confirma em uma linha** ("você vende X por R$ Y, certo?") e não pergunta de novo.
2. Pergunte, uma por vez, só o que falta: o que ela vende, quem compra hoje, quanto custa e qual resultado ela
   consegue provar. "Quem compra hoje" pede **descrição de pessoas**, com exemplo, e não canais ("indicação",
   "grupo"). Se a resposta for vaga, ofereça 3 opções e peça para escolher.
3. **Cruze a oferta com cada perfil:** a oferta resolve a dor? Responde ao desejo? Atravessa a trava? Diga com
   franqueza onde não encaixa e o que falta na oferta. Perfil que a oferta não atende fica de fora.
4. **Grave `oferta.md`.**
5. Para os leads da lista curta, rascunhe **uma mensagem por pessoa**. **A primeira mensagem não cita produto,
   preço nem negócio:** é uma pergunta ou uma ajuda ligada ao que ela escreveu. No YouTube só existe resposta
   pública ao comentário: ali vale só responder ajudando, sem repetir a frase dela em público. Só a lista curta
   recebe rascunho (até 6 meses, dentro do avatar). Cada rascunho vai em `abordagens.md` com a citação, o link e o
   aviso de envio à mão.
6. **Confira por programa** (`conferir_saidas.py`) e corrija antes de mostrar.
7. **Sugira o ritmo, sem perguntar:** poucas mensagens por dia, enviadas por ela, de uma conta dela, lendo cada uma.
   Nada automático, e você não envia.

**Termine** com 3 linhas: o que foi criado, onde está e como retomar ("usa a pasta acha-clientes e me ajuda com
as mensagens da lista curta"). Diga também: a pasta `bruto/` pode ser apagada, porque o `link_perfil` já está no
CSV.

## Erros comuns

- Perguntar da oferta na fase 1 só porque a pessoa começou falando dela.
- Fazer as perguntas do avatar de uma vez, ou duas decisões na mesma mensagem.
- Rodar coleta ou instalação sem confirmação, ou escolher o caminho antes de saber onde o avatar fala.
- Procurar por hashtag de produto: traz post de vendedor, sem conversa de cliente.
- Escolher post pelo número de curtidas, e não pelo tipo de gente que comenta.
- Rascunho que cita produto, preço ou negócio, ou resposta pública a comentário de anos atrás.
- Perfil com citação "parafraseada". Se mudou a palavra, não é citação.
- Prometer resultado. Diga o que a ferramenta faz e onde o gratuito acaba.

## Arquivos de apoio

| Arquivo | Quando ler |
|---|---|
| `references/coleta-youtube.md` | teste de fumaça da fase 0; fases 2, 3 e 5 no caminho B |
| `references/coleta-apify.md` | fases 2, 3 e 5 no caminho C |
| `references/coleta-colando.md` | fase 3 no caminho A; LinkedIn e Reddit |
| `references/ler-comentarios.md` | fases 3, 4 e 5 |
| `references/modelos-de-saida.md` | ao gravar cada arquivo |
| `references/oferta-e-abordagem.md` | fase 6 |
| `references/limites-e-privacidade.md` | quando perguntarem de termos, LGPD, ou antes da fase 5 |
| `references/exemplo-comentarios.md` | só no modo demonstração, sem comentário real |
| `references/fontes.md` | quando perguntarem de onde vem uma regra, um preço ou um crédito |
| `scripts/juntar_comentarios.py` | fase 3, para juntar a coleta em `comentarios.csv` (use o caminho da pasta da skill) |
| `scripts/conferir_saidas.py` | fim das fases 4, 5 e 6, para conferir citações e links |
