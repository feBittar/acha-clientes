# Coleta colando (caminho A)

Leia na fase 3 quando não há terminal, quando a coleta automática falhou, ou para LinkedIn e Reddit. Sempre
funciona, em qualquer rede, e não custa nada. O preço é o tempo de quem cola.

## Como pedir

Peça uma coisa por vez e dê o exemplo:

1. "Abra um dos posts da lista, role até os comentários e copie de 30 a 50 deles (pode ser com Ctrl+A e Ctrl+C na
   área dos comentários). Cole aqui."
2. "Cole também o link do post." Sem o link, você não consegue preencher `link_post` nem `link_origem`.
3. Se a plataforma mostrar o link de cada comentário (no YouTube, clicar na data do comentário), peça o link de
   alguns. Sem ele, o link do comentário é o do post, e você avisa.
4. Dê um post de cada vez. Depois de cada um, diga quantos comentários úteis tem e quantos faltam para ~40.
5. Pode ser print, PDF ou arquivo de texto. Imagem: transcreva palavra por palavra e mostre a transcrição para
   conferir.

## Como virar `comentarios.csv`

Para cada comentário, uma linha com as colunas de `modelos-de-saida.md`: `plataforma, link_post, link_comentario,
usuario, link_perfil, texto, curtidas, data, idade_aprox, coletado_em`.

- `usuario`: o nome como aparece. Se a pessoa colou sem o nome, deixe vazio: o comentário ainda serve para os perfis,
  mas não vira lead, porque não dá para achar a pessoa.
- `texto`: exatamente como colado, sem corrigir.
- `link_perfil`: só se a pessoa colou ou a rede deixa montar pelo usuário. Se a data veio como "há 3 meses", ponha em
  `idade_aprox` e deixe `data` vazia.
- Campos que não vieram (curtidas, data): vazios. `coletado_em`: a data de hoje (AAAA-MM-DD).
- Se o texto tem vírgula ou quebra de linha, ponha entre aspas duplas; aspas dentro viram duas aspas.
- Se não tiver terminal, monte o CSV e entregue como arquivo. Se tiver, pode escrever o arquivo direto.

## Grupos (Facebook, WhatsApp, Telegram)

Antes de usar comentário colado de grupo, pergunte: "Esse grupo é público (qualquer pessoa vê os posts sem
entrar) ou fechado?"

- **Fechado, ou grupo de WhatsApp e Telegram:** o conteúdo não é público. Os comentários podem ajudar a entender o
  perfil, mas sem nome: grave `usuario` e `link_perfil` vazios, e ninguém dali vira lead. Diga isso em uma frase
  (termos da rede e LGPD).
- **Público:** peça o link do post de onde vieram os comentários (no Facebook, clicar na data do post e copiar o
  endereço). Ele vai em `link_post` e vira o `link_origem`. Só o link do grupo não basta: sem o link do post, o
  comentário serve para os perfis, mas não vira lead.
- **Facebook não tem leitura de perfil público na skill.** Não peça o "pode" da fase 5 para isso: `dados_publicos`
  recebe só o nome como apareceu e o que a pessoa disse de si, marcado "(do comentário)".
- **Abordagem:** responder no próprio post, só ajudando, ou mensagem da conta da pessoa, com as regras de
  `oferta-e-abordagem.md`.

## LinkedIn

Os termos do LinkedIn (User Agreement, item 8.2) proíbem scripts, robôs e extensões para copiar dados. Então
aqui é só colar, à mão, o que a pessoa vê na tela. Não use extensão, não peça login em ferramenta nenhuma. Copie
só comentários públicos de posts que o próprio usuário consegue ver.

## Reddit (opcional)

O JSON público do Reddit respondeu 403 no teste de 14/11/2026. O RSS de subreddit respondeu 200:
`https://www.reddit.com/r/NOME/.rss`. Se o usuário tiver terminal, você pode sondar com
`curl -s -A "acha-clientes" -o /dev/null -w "%{http_code}" https://www.reddit.com/r/NOME/.rss` (no PowerShell,
`curl.exe`). Se responder 200, o feed traz os posts recentes do subreddit, e você ajuda a escolher quais abrir. Os
comentários de cada post a pessoa cola. Se não responder 200, não insista: é colar.
