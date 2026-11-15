# Modelos de saída

Preencha só com o que a pessoa decidiu ou o que os comentários mostraram. Onde não houver, escreva "a decidir" ou
"não apareceu". Se usou `exemplo-comentarios.md`, ponha `EXEMPLO` no título de cada arquivo e em cada linha, e grave tudo em `acha-clientes/exemplo/`, nunca junto das saídas reais.

## avatar.md

~~~~markdown
# Avatar ideal (hipótese, [data])

> Palpite da pessoa, a confirmar com comentários reais. Revisado na fase 4.

**Em uma frase:** [resumo]
- Quem é: ...
- Onde atende: ... (uma cidade ou região, ou qualquer lugar)
- Momento: ...
- O que tenta resolver (nas palavras dela): ...
- Onde fala disso: ...
- Quem não é: ...

Respostas escolhidas entre opções que a IA sugeriu levam "(sugerido, a confirmar)".

## Termos de busca
1. ... (5 a 10, como a pessoa fala do problema)

## Para a fase 6 (o que ela comentou sobre a oferta)
- ...

## O que os comentários mostraram (fase 4)
Base: N comentários úteis de M posts, coletados em [data].
- Confirmou: ...
- Mudou: ...
- Não apareceu: ...
~~~~

## perfis.md

~~~~markdown
# Perfis ideais ([data], base de N comentários úteis)

## Perfil 1: [nome curto]
**Quem é:** [2 linhas]
**Dor:** [frase] (sustentam: X comentários)
- "citação literal" (@usuario, [link do comentário])
**Desejo:** [frase] (sustentam: X)
- "citação" (@usuario, [link])
**Trava:** [frase] (sustentam: X)
- "citação" (@usuario, [link])
**Ainda é palpite:** [o que veio de menos de 3 comentários]
~~~~

Repita por perfil (2 a 4). Se a base é pequena, ponha no topo: "base pequena, leia como indício". Dor, desejo ou
trava com menos de 2 comentários: "não apareceu nos comentários". Nota de data ("datas aproximadas") em linha
que começa com ">", sem aspas.

## Colunas dos CSV (nesta ordem, com cabeçalho)

- `posts.csv`: `plataforma, link, titulo, autor, data, comentarios, por_que_entrou` (`comentarios` é o número
  coletado, não o total do vídeo)
- `comentarios.csv`: `plataforma, link_post, link_comentario, usuario, link_perfil, texto, curtidas, data,
  idade_aprox, coletado_em`
- `leads.csv`: `id, plataforma, usuario, link_perfil, link_origem, citacao, perfil, dor, desejo, trava, sinal,
  dados_publicos, coletado_em, observacao`

Regras do `comentarios.csv`: `data` só quando a fonte dá a data exata (yt-dlp, Apify), AAAA-MM-DD. O
`youtube-comment-downloader` só dá tempo relativo: `data` fica vazia e `idade_aprox` recebe "há 4 anos". Sem
duplicata de mesmo usuário e mesmo texto. `link_perfil` vem do canal (YouTube) ou do usuário
(`https://www.instagram.com/<usuario>/`, `https://www.tiktok.com/@<usuario>`).

Regras do `leads.csv`: `id` é L001, L002...; só comentário de até 12 meses vira linha; `link_origem` é
obrigatório (link do comentário, ou do post se não houver, com "link do post" na `observacao`); com mais de uma
citação, `citacao` e `link_origem` levam os itens na mesma ordem, separados por " || "; `citacao` é literal; `perfil` é o nome do `perfis.md`; `sinal` é
quente, morno ou frio (regra em `ler-comentarios.md`); `dados_publicos` só o que está no perfil público (nome
exibido, descrição), ou o que a pessoa disse de si no comentário, marcado "(do comentário)"; vazio se não houver;
`link_perfil` vem do `comentarios.csv`; `dor`, `desejo` e `trava` só preenchidos se a citação daquela pessoa
sustenta (vazio está certo); `observacao` diz "lista curta", "fora: antigo" (de 6 a 12 meses), "fora: fora do avatar" ou "fora: lugar não
declarado"; se cabe mais de um "fora", use o primeiro nesta ordem: fora do avatar, lugar não declarado, antigo; `coletado_em` AAAA-MM-DD.

Datas sempre AAAA-MM-DD. Campos com vírgula ou quebra de linha, entre aspas duplas.

## oferta.md

~~~~markdown
# Oferta ([data])

## A oferta, nas palavras da pessoa
O que vende, para quem, preço, resultado que consegue provar.

## Cruzamento com cada perfil
| Perfil | A oferta resolve a dor? | Responde ao desejo? | Atravessa a trava? | O que falta |
|---|---|---|---|---|

## O que falta na oferta
- ...

## Perfis que a oferta não atende
- ...
~~~~

## abordagens.md

~~~~markdown
# Abordagens (rascunhos, [data])

> Rascunhos para você ler, mudar e enviar à mão, de uma conta sua, poucos por dia. Nada aqui é enviado sozinho.
> A primeira mensagem não cita produto, preço nem negócio. No YouTube, só resposta pública ao comentário.
> Só a lista curta recebe rascunho.

## L003 | @usuario | perfil: [nome] | sinal: quente
Origem: [link do comentário]
Ela escreveu: "citação literal"
Mensagem:
> [texto curto]
Enviada em: ___  Respondeu: ___
~~~~

Lead fora da lista curta não entra em `abordagens.md`.
