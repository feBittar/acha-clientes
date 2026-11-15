# Acha clientes

Uma skill que acha clientes pelo avatar, e não pela oferta. Ela começa por quem é a pessoa que compraria, acha os
posts onde essa gente fala do problema, lê os comentários públicos e monta uma lista de leads com as palavras de
cada um. Só depois pergunta da sua oferta.

O que acontece na conversa:

1. Ela te faz 6 perguntas, uma de cada vez, sobre o seu cliente ideal: quem é, onde você atende, o momento, o que
   tenta resolver, onde fala disso e quem não é. Isso vira um `avatar.md`, marcado como hipótese.
2. Acha posts feitos para o seu avatar, com muita conversa nos comentários, e você aprova a lista antes da coleta.
   A escolha de onde coletar (YouTube, Instagram, TikTok ou colar) vem depois que ela entende quem é o seu cliente.
3. Coleta os comentários públicos desses posts e tira o ruído.
4. Agrupa em 2 a 4 perfis. Cada um com a dor, o desejo e a trava, em citação literal com link, e revisa o avatar
   com o que os comentários mostraram.
5. Monta o `leads.csv`: uma linha por pessoa, com o perfil, a dor, o desejo, a trava (só o que a frase dela
   sustenta), a frase, o sinal (quente, morno ou frio), o link do perfil e o link de onde veio. Daí sai uma lista
   curta de quem vale abordar: só gente dentro do seu avatar e com comentário recente. Se ninguém passar, ela diz
   "não há lead abordável nesta coleta" e propõe coletar comentários recentes.
6. Só aqui pergunta da sua oferta, cruza com os perfis, diz o que falta e rascunha uma mensagem por pessoa da
   lista curta. Você envia à mão.

## Como usar

**No Claude Code**

Copie a pasta `acha-clientes` para `~/.claude/skills/` (vale para todos os projetos) ou para `.claude/skills/`
dentro do projeto. Depois escreva: "quero achar clientes". Ela vê o que o seu computador tem e te guia na
instalação da base gratuita do YouTube (yt-dlp e youtube-comment-downloader), sempre pedindo confirmação antes. Os arquivos saem na pasta `acha-clientes/` de onde você está.

**No claude.ai**

Vá em Customize > Skills e envie o arquivo `acha-clientes.zip`. Se a opção de skills não aparecer, ligue a execução
de código nas configurações. Depois escreva: "quero achar clientes". Aqui não há terminal: você cola os comentários,
ou conecta a Apify como conector. Os arquivos saem para baixar.

**No ChatGPT ou no Gemini**

Abra o `para-chatgpt.md` e siga o que está no começo dele. A coleta é só colando.

## O que é grátis e onde acaba

| Caminho | Custo | Onde acaba |
|---|---|---|
| YouTube (caminho principal) | zero | em alguns computadores ou redes o YouTube pede verificação de robô; aí volta para colar |
| Colar os comentários | zero | o seu tempo |
| Instagram e TikTok com Apify | usa o crédito gratuito da Apify (US$ 5 por mês, sem cartão, se a conta for do plano gratuito); a skill estima antes e só roda com o seu "pode" | perto de 1.900 comentários do Instagram por mês; acabou o crédito, só no mês seguinte |
| LinkedIn e Reddit | zero | só colando; os termos do LinkedIn proíbem robô |

No Instagram, a maior parte dos comentários costuma ser elogio e marcação de amigo. Vídeos do YouTube sobre o
problema do seu cliente rendem mais texto por comentário, e de graça.

Preços lidos em 14/11/2026 e podem mudar. O preço exato do TikTok no plano grátis não foi verificado.

## O que esperar, com honestidade

- **A primeira mensagem não vende.** Ela não cita produto, preço nem o seu negócio: é uma pergunta ou uma ajuda
  ligada ao que a pessoa escreveu. No YouTube só existe resposta pública ao comentário, e ali vale só responder
  ajudando. Comentário com mais de 6 meses fica sem rascunho.
- **Negócio local pede fonte local.** Se você atende só uma cidade, vídeos e posts nacionais servem para entender o
  seu cliente e aprender as palavras dele, mas quase ninguém ali é da sua cidade. Lead de verdade vem de página ou
  grupo da cidade, posts de negócios e eventos locais, colados ou coletados pela Apify.
- **Comentário antigo não é lead.** O YouTube só informa "há 4 anos", e a skill respeita isso. Para achar gente
  recente, ela coleta também os comentários mais novos.

## O que ela não faz, e por quê

- **Não envia mensagem, não comenta, não segue.** Disparo em massa é spam, trava a sua conta e esbarra na LGPD. A
  skill escreve o rascunho; você envia.
- **Não entra na conta de ninguém** e não pede senha. Só dado público.
- **Não caça e-mail nem telefone.** Só entra o que a pessoa deixou público no próprio perfil.
- **Não inventa citação.** Sem comentário real, ela para e pede mais material.
- **Não transforma em lead quem falou de saúde** ou de outro tema sensível.
- **Não promete cliente.** Ela te dá a leitura do que o seu público escreve. Fechar a venda é com você.

Os termos do YouTube, do Instagram e do TikTok restringem coleta automatizada. A skill coleta pouco, só público, e a
decisão é sua. Os detalhes ficam em `acha-clientes/references/limites-e-privacidade.md`.

## O que tem aqui

- `acha-clientes/`: a skill (o `SKILL.md`, as referências que ela lê em cada fase e dois scripts: um junta os
  comentários, o outro confere se toda citação e todo link existem no `comentarios.csv`).
- `acha-clientes.zip`: a mesma pasta, pronta para enviar no claude.ai.
- `para-chatgpt.md`: a versão para colar no ChatGPT ou no Gemini.
- `acha-clientes/references/fontes.md`: de onde vem cada preço, regra e crédito.

Sem comentário real suficiente, a skill pode mostrar uma demonstração, em `acha-clientes/exemplo/`, com comentários
inventados de outro nicho (salão). Serve só para ver o formato.

Feito pelo [@ofelipemart](https://instagram.com/ofelipemart). O método de ler comentários e achar sinal de dor tem
inspiração em skills de código aberto, creditadas em `fontes.md`.
