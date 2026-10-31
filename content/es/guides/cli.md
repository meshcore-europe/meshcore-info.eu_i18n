---
title: Comandos CLI
layout: cli
lead: Todos los comandos de tu repetidor, room server, sensor o companion, agrupados según lo que quieras hacer. Lee qué hace cada uno y con qué valor empieza, pon el tuyo y cópialo.
description: 'Todos los comandos del firmware 1.18.0 de MeshCore para repetidores, room servers, sensores y companions, agrupados por tarea: qué hacen, con qué valor arranca el firmware y qué nodos los tienen.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-31'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Estos comandos corresponden al firmware 1.18.0 de MeshCore. Los hemos sacado
del código fuente del firmware. Si un comando llegó en una versión reciente,
indica qué versión necesita. Un repetidor reenvía los mensajes, un room server
guarda las publicaciones de un grupo y un sensor envía sus lecturas. Los room
servers, los sensores y los companions comparten muchos comandos. En cada
comando verás qué nodos lo tienen. Con "¿Qué nodo?" ves solo los comandos de
tu nodo.

En un repetidor, room server o sensor, los escribes por USB desde tu
ordenador, por ejemplo en la [consola serie](/firmware/console/) de esta web. Desde la app de MeshCore los envías por la malla. En la
[guía del repetidor](/repeater-guide/#config) encontrarás las dos formas.

Desde la versión 1.18, el companion (el nodo desde el que escribes tus mensajes, emparejado con tu móvil o tu portátil, o
con pantalla propia) también tiene línea de comandos. Ábrela en Command Line,
dentro de los ajustes de la app de MeshCore, versión 1.50 o posterior. Un
contacto con el permiso Remote CLI puede enviar a tu companion los mismos
comandos por la malla. Eso incluye los comandos de WiFi y de PIN.

El valor inicial de un comando es el del repetidor. En un room server,
sensor o companion puede tener otro valor inicial. Si un comando solo existe en
el companion, muestra su propio valor.
