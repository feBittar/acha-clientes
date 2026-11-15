# Limites e privacidade

Leia quando a pessoa perguntar sobre termos ou LGPD, e antes da fase 5. Não é parecer jurídico. É o que a skill
faz para ficar do lado seguro, e onde a decisão é da pessoa.

## Termos das plataformas

- **YouTube** (vale para o yt-dlp e para o `youtube-comment-downloader`): os termos (https://www.youtube.com/t/terms) restringem acesso automatizado fora das ferramentas
  oficiais. A API oficial (`coleta-youtube.md`, seção 5) é o caminho mais certo.
- **TikTok:** os termos (seção 5) restringem acesso automatizado.
- **Instagram:** também restringe; a cláusula exata não foi conferida ao vivo.
- **LinkedIn:** o User Agreement, item 8.2, proíbe scripts, robôs e extensões para copiar dados. Só colar à mão.

Por isso a skill: coleta pouco (dezenas ou poucas centenas de comentários), só posts públicos, sem entrar na conta
da pessoa, sem contornar bloqueio e sem passar cookies. Se a plataforma barrar, ela para. A decisão de coletar é
da pessoa, e o caminho de colar à mão sempre existe.

## LGPD (Lei 13.709/2018)

O art. 7º, §§ 3º e 4º, diz que dado tornado público pela própria pessoa dispensa o consentimento, mas o uso
continua precisando de finalidade, boa-fé e respeito aos direitos do titular
(https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm). Na prática:

- Use a lista para entender e falar com quem escreveu sobre aquele problema, e para nada além disso.
- Não venda nem repasse a lista.
- Se alguém pedir para sair, apague a linha e não escreva mais.
- Guarde só o necessário. Quando terminar, a pasta `bruto/` pode ser apagada: o `link_perfil` já está no CSV.

## O que nunca entra

- E-mail, telefone ou endereço, mesmo achados em outro lugar.
- Dado sensível (saúde, religião, política, orientação sexual, origem racial ou étnica, filiação a sindicato) como
  motivo de uma pessoa virar lead.
- Dado de criança ou adolescente.
- Conteúdo de conta privada, grupo fechado ou mensagem direta.
- Senhas, tokens e cookies, no chat ou em arquivo.
