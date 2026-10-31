---
title: Comandos CLI
layout: cli
lead: Todos os comandos do teu repetidor, room server, sensor ou companion, agrupados pelo que queres fazer. Lê o que cada um faz e o valor com que começa, preenche o teu e copia-o.
description: 'Todos os comandos do firmware MeshCore 1.18.0 para repetidores, room servers, sensores e companions, agrupados por tarefa: o que fazem, o valor com que o firmware começa e que nós os têm.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-31'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Estes comandos seguem o firmware MeshCore 1.18.0 e foram lidos no código-fonte
do firmware. Se um comando surgiu numa versão recente, indicamos a versão de que
precisa. Um repetidor reencaminha mensagens, um room server guarda publicações
para um grupo e um sensor envia leituras. Os room servers, os sensores e os
companions partilham muitos comandos. Em cada comando indicamos que nós o têm.
Em "Que nó?" vês só os comandos do teu.

Num repetidor, room server ou sensor, escreves os comandos por USB a partir do
teu computador, por exemplo na [consola série](/firmware/console/) deste site. A app MeshCore envia-os pela mesh. O
[guia do repetidor](/repeater-guide/#config) mostra as duas formas.

Desde a 1.18, um companion (o nó a partir do qual envias mensagens, emparelhado com o teu telemóvel ou portátil, ou
com ecrã próprio) também tem linha de comandos. Abre Command Line nas definições da app MeshCore, versão 1.50 ou
posterior. Um contacto com a permissão Remote CLI pode enviar os mesmos comandos
ao teu companion pela mesh. Isso inclui os comandos de WiFi e de PIN.

O valor com que um comando começa é o do repetidor. Num room server, sensor ou
companion, o valor inicial pode ser outro. Um comando que só o companion tem mostra o seu próprio valor.
