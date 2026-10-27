---
title: Comandos CLI
layout: cli
lead: Todos os comandos do teu repetidor, room server, sensor ou companion, agrupados por tarefa. Lê o que cada um faz e o valor com que começa, preenche o teu e copia-o.
description: 'Todos os comandos do firmware MeshCore 1.18.0 para repetidores, room servers, sensores e companions, agrupados por tarefa: o que fazem, o valor com que o firmware começa e que nós os têm.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-26'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
---

Estes comandos seguem o firmware MeshCore 1.18.0, lidos a partir do código fonte do firmware. Um comando acrescentado numa versão recente indica a versão de que precisa. Um repetidor reencaminha mensagens, um room server guarda publicações de um grupo, um sensor comunica leituras. Room servers, sensores e companions partilham muitos comandos. Cada comando indica que nós o têm. "Que nó?" mostra apenas os comandos do teu.

Num repetidor, room server ou sensor, escreves os comandos por USB a partir do teu computador, por exemplo na [consola série](/firmware/console/) deste site. A app MeshCore envia-os pela mesh. O [guia do repetidor](/repeater-guide/#config) mostra as duas formas.

Desde a versão 1.18, um companion (o nó a partir do qual envias mensagens, emparelhado com o teu telemóvel ou portátil, ou com ecrã próprio) também tem uma linha de comandos. Abre Command Line nas definições da app MeshCore, versão 1.50 ou posterior. Um contacto com a permissão Remote CLI pode enviar ao teu companion os mesmos comandos pela mesh. Isso inclui os comandos de WiFi e de PIN.

O valor com que um comando começa é o do repetidor. Um room server, sensor ou companion pode começar com outro valor. Um comando que só um companion tem mostra o seu próprio valor.
