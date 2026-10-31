---
title: Gerar uma chave
layout: keygen
lead: Dá ao teu repetidor um prefixo que nenhum repetidor perto de ti usa. Procura um prefixo livre, cria uma chave que comece por ele e configura-a.
description: Cria no teu browser uma chave MeshCore com o prefixo que escolheres, para que nenhum repetidor perto do teu partilhe o prefixo num caminho.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-31'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

Um repetidor reencaminha as mensagens de todos à sua volta. Num caminho, o MeshCore
identifica cada repetidor pelos primeiros bytes da sua chave pública:
o seu prefixo. Se um repetidor perto de ti tiver o mesmo prefixo, o caminho não mostra
qual dos dois reencaminhou a mensagem. O MeshCore escolhe a chave ao acaso. Aqui
crias uma com o prefixo que queres.

Usa 2 bytes. A 13 de outubro de 2026, o [MeshCore Analyzer](https://meshcore-analyzer.eu/)
registou que todos os prefixos de 1 byte estavam partilhados na Europa. O tamanho do hash do caminho,
uma definição de quem envia, decide quantos bytes de cada prefixo entram num caminho; consulta os [comandos CLI](/guides/cli/).
