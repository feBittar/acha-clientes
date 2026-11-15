# Ler os comentários

Método das fases 3, 4 e 5. A ideia: o valor está nas palavras da pessoa. Seu trabalho é achar, separar e
agrupar, sem reescrever.

## Filtrar o ruído (fase 3)

Marque como ruído e tire da análise, sem apagar do arquivo bruto:

- elogio vazio ("top", "amei", só emoji, "primeiro") e elogio ao vídeo ("ótima ideia", "amei as dicas");
- divulgação e spam ("me chama no direct", links, "ganhe dinheiro");
- resposta de quem postou (`autor é o dono do vídeo`);
- comentário de colega de profissão (quem também vende o mesmo serviço e comenta para aparecer);
- comentário sobre o vídeo e não sobre o problema ("a edição ficou boa");
- texto curto demais para entender (menos de 4 palavras), a não ser que seja uma pergunta clara;
- repetido (mesmo texto, mesma pessoa).

Sobra o **comentário útil**: fala de problema, desejo, dúvida, tentativa ou frustração. Conte. A fase 4 pede cerca
de 40; menos que isso, perfil fraco.

## O que procurar em cada comentário (fase 4)

- **Dor:** uma queixa dita, com o contexto. "Já gastei com anúncio e ninguém chama." "Ficou caro." "Não tô
  podendo gastar." **Preço citado sem queixa não é dor** ("gastei 350 numa festa de 20" só conta o que foi feito).
- **Desejo:** o que a pessoa quer que aconteça, o resultado, não a ferramenta. "Queria a agenda cheia sem depender
  de indicação."
- **Trava:** um obstáculo dito. "Não consegui", "não tenho tempo", "não sei quanto fazer", "já tentei e não deu",
  "isso é caro", "isso não funciona pra mim". Falar do que a pessoa faz não é trava, e você não deduz trava de um
  comportamento.

Um comentário pode ter os três, um só ou nenhum. Não force: campo sem citação fica vazio. **Com menos de 2
comentários sustentando** uma dor, desejo ou trava do perfil, escreva "não apareceu nos comentários" em vez de
preencher. O perfil pode seguir sem trava, com isso dito. Em `leads.csv`, a célula de dor, desejo ou trava só é
preenchida se a citação **daquela pessoa** sustenta; senão fica vazia, e está certo.

## Agrupar em perfis

- Agrupe pela **situação**, não pela rede nem pelo post: quem está começando, quem já tentou e desistiu, quem tem
  cliente mas não consegue crescer.
- De 2 a 4 perfis. Um perfil só com 1 ou 2 comentários vira "palpite", não perfil.
- Nome curto e concreto. Um parágrafo de 2 linhas diz quem é.
- Para cada perfil: dor, desejo e trava, com 3 a 5 citações e o número de comentários que sustentam cada um
  ("sustentam: 14 de 52 úteis").

## Regra da citação literal

Uma citação é o texto exato do comentário, entre aspas, sem corrigir, sem cortar o sentido, com o link do
comentário ao lado. Pode cortar o começo ou o fim com "[...]" quando o trecho é longo. Não junte duas frases de
pessoas diferentes. Não traduza (se for em inglês, cite no original e traduza em seguida, marcando "tradução
minha"). Se você não achou a frase, não escreva: diga "não apareceu".

Antes de mostrar `perfis.md`, `leads.csv` e `abordagens.md`, rode `scripts/conferir_saidas.py` (confere cada citação
e cada link contra o `comentarios.csv`). Se falhar, corrija ou tire. Sem terminal, confira à mão por amostragem e
diga que foi à mão. Nota sobre a data do comentário vai em linha que começa com ">", sem aspas.

## Sinal quente, morno, frio (fase 5)

A regra, para o lead e a coluna `sinal`:

A idade vem de `data` (quando a fonte dá a data exata) ou de `idade_aprox` ("há 4 anos", "há 3 meses"), que é
aproximada. **"Há 1 ano" ou mais conta como mais de 12 meses** (o YouTube arredonda: pode ser de 12 a 23 meses).
"Há 6 meses" ainda é até 6 meses; "há 7 meses" já não.

- **Quente:** a pessoa descreve a dor do perfil **e** pede ajuda ou diz que está procurando solução agora
  ("alguém indica...", "preciso resolver isso"), e o comentário é de até 90 dias atrás.
- **Morno:** descreve a dor ou o desejo com clareza, mas não pede nada, ou é mais antigo que 90 dias.
- **Frio:** concorda com outro comentário ou toca no assunto de passagem ("também!"). Entra na lista só se o
  perfil precisa de volume; senão, deixa fora.

Sinal descreve o comentário, não a pessoa. É um palpite sobre o momento, e não uma previsão de compra. Se o
comentário não tem `data` nem `idade_aprox`, o máximo é morno.

## Lista curta: quem vale abordar

Entra só o lead que passa nos dois testes:

- **Dentro do avatar:** tamanho do negócio ou da situação. Quem diz que mora fora da área atendida nem vira lead.
- **Do lugar certo, se o negócio é local:** se na fase 1 a pessoa disse que atende só uma cidade ou região, entra só
  quem declarou estar ali ou veio de fonte local (grupo público, página ou post da cidade). Comentário de vídeo ou
  post nacional sem lugar declarado serve para os perfis e fica fora, marcado "fora: lugar não declarado". Negócio
  que atende qualquer lugar não tem esse teste.
- **Recente:** comentário de até 6 meses (quente, até 90 dias). De 6 a 12 meses fica no `leads.csv` marcado "fora:
  antigo", sem rascunho. Mais de 12 meses nem vira linha.

Se ninguém passa, o resultado honesto é "não há lead abordável nesta coleta", e a saída é coletar comentários
recentes. Não se completa a lista com lead antigo para ter o que mostrar.

## Temas sensíveis

Comentário sobre saúde (inclusive gravidez, doença, remédio, deficiência), religião, política, orientação sexual,
origem ou filiação pode ajudar a entender o perfil, mas a pessoa não vira linha em `leads.csv` nem é citada com
nome em `perfis.md`. Na fase 3, apague o `usuario` e o `link_perfil` desse comentário no `comentarios.csv`. Dado de
menor de idade também não entra. Conta quando a pessoa fala de si (a doença dela, a gravidez dela, a fé dela).
Expressão ou metáfora ("Deus me livre", "pareço que tenho alzheimer") não conta.
