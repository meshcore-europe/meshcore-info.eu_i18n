---
title: Consola série
layout: console
lead: Escreve comandos para o teu repetidor a partir do browser, por USB.
description: Configura um repetidor, room server ou sensor MeshCore por USB no Chrome, Edge ou Opera, com uma consola série no browser e sem instalar nada.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-31'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Um repetidor (reencaminha mensagens), um room server (guarda publicações para
um grupo) ou um sensor (envia leituras) não tem app. Por isso, configuras-o
escrevendo comandos por USB. Liga o teu nó ao computador. Abre esta página no
Chrome, Edge ou Opera num computador e escolhe a porta do teu nó. Primeiro, a
consola envia `get role` e `ver` para saber que tipo de nó tens. Os dois
comandos só leem dados. Depois, a consola mostra o que o teu nó responde.
Escreve um comando como `get name` e carrega em Enter. Enquanto escreves, a
consola sugere os comandos que o teu nó entende. A tecla Tab preenche o primeiro.

Um companion, o nó a partir do qual envias mensagens, comunica antes com a app por USB. A linha de comandos dele está na
app MeshCore, versão 1.50 ou posterior.
