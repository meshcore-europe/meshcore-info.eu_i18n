---
title: Comandos CLI
layout: cli
lead: Todos os comandos do teu repetidor, servidor de sala, sensor ou companion, agrupados segundo o que queiras facer. Le que fai cada un e con que valor comeza, enche o teu e cópiao.
description: 'Todos os comandos do firmware 1.18.0 de MeshCore para repetidores, servidores de sala, sensores e companions, agrupados por tarefa: que fai cada un, con que valor comeza no firmware e que nodos o teñen.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-11-02'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Estes comandos corresponden ao firmware 1.18.0 de MeshCore e tomámolos do seu código fonte. Os comandos engadidos nunha versión recente indican que versión necesitan. Un repetidor reenvía as mensaxes, un servidor de sala garda publicacións para un grupo e un sensor envía lecturas. Os servidores de sala, os sensores e os companions comparten moitos comandos. En cada comando indícase que nodos o teñen. En "Que nodo?" podes ver só os comandos do teu.

Nun repetidor, servidor de sala ou sensor, escríbelos desde o teu ordenador por USB, por exemplo na [consola serie](/firmware/console/) deste sitio. A app de MeshCore envíaos pola malla. Na [guía do repetidor](/repeater-guide/#config) explícanse as dúas formas.

Desde a versión 1.18, un companion (o nodo desde o que envías mensaxes, emparellado co teu teléfono ou portátil, ou coa súa propia pantalla) tamén ten liña de comandos. Abre Command Line na configuración da app de MeshCore, versión 1.50 ou posterior. Un contacto co permiso Remote CLI pode enviarlle ao teu companion os mesmos comandos pola malla. Entre eles están os comandos de WiFi e de PIN.

O valor inicial dun comando é o do repetidor. Nun servidor de sala, sensor ou companion, o valor inicial pode ser outro. Un comando que só ten o companion mostra o seu propio valor.
