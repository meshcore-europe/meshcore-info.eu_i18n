---
title: Gerar uma chave
layout: keygen
lead: Dá ao teu repetidor um prefixo que nenhum repetidor perto de ti usa. Encontra um prefixo livre, cria uma chave que começa por ele e define-a.
description: Cria uma chave MeshCore com um prefixo à tua escolha, no teu browser, para que nenhum repetidor perto do teu partilhe o prefixo num caminho.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-26'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
---

Um repetidor reencaminha mensagens para todos à sua volta. Num caminho, o MeshCore
identifica cada repetidor pelos primeiros bytes da sua chave pública:
o prefixo. Quando um repetidor perto de ti tem o mesmo prefixo, o caminho não mostra
qual dos dois reencaminhou a mensagem. O MeshCore escolhe a chave ao acaso. Aqui
crias uma com o prefixo que quiseres.

Usa 2 bytes. Em 13 de outubro de 2026, o [MeshCore Analyzer](https://meshcore-analyzer.eu/)
viu todos os prefixos de 1 byte partilhados na Europa. O tamanho do hash do caminho, uma definição
do remetente, decide quantos bytes de cada prefixo entram num caminho; vê [Comandos CLI](/guides/cli/).
