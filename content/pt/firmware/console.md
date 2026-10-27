---
title: Consola série
layout: console
lead: Envia comandos ao teu repetidor a partir do browser, por USB.
description: Configura um repetidor, um room server ou um sensor MeshCore por USB a partir do Chrome, Edge ou Opera, com uma consola série no browser. Sem nada para instalar.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-26'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: 'a2fe0704'}
  sections: ['c33167ce']
---

Um repetidor (reencaminha mensagens), um room server (guarda publicações para um grupo) ou um sensor (comunica leituras) não tem app, por isso configuras cada um deles escrevendo comandos por USB. Liga o teu nó ao computador, abre esta página no Chrome, Edge ou Opera num computador e escolhe a porta do teu nó. A consola envia primeiro `get role` e `ver`, para saber o que é o teu nó. Ambos apenas leem. Depois mostra o que o teu nó responde; escreve um comando como `get name` e carrega em Enter. Enquanto escreves, a consola sugere os comandos que o teu nó entende, e com Tab preenches o primeiro.

Um companion, o nó a partir do qual envias mensagens, fala com a app por USB. A sua linha de comandos está na app MeshCore, versão 1.50 ou posterior.
