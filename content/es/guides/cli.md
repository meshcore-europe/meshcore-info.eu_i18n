---
title: Comandos CLI
layout: cli
lead: Todos los comandos de tu repetidor, servidor de sala, sensor o companion, agrupados según lo que quieres hacer. Lee qué hace cada uno y el valor con el que empieza, pon el tuyo y cópialo.
description: 'Todos los comandos del firmware MeshCore 1.18.0 para repetidores, servidores de sala, sensores y companions, agrupados por tarea: qué hace cada uno, el valor con el que empieza el firmware y qué nodos lo tienen.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-26'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
---

Estos comandos siguen el firmware MeshCore 1.18.0, leídos del código fuente del firmware. Si un comando se añadió en una versión reciente, indica qué versión necesita. Un repetidor reenvía mensajes, un servidor de sala guarda publicaciones para un grupo, un sensor informa de sus lecturas. Los servidores de sala, los sensores y los companions comparten muchos comandos. Cada comando indica qué nodos lo tienen. "¿Qué nodo?" muestra solo los comandos del tuyo.

En un repetidor, servidor de sala o sensor, los escribes por USB desde tu ordenador, por ejemplo en la [consola serie](/firmware/console/) de este sitio. La app de MeshCore los envía por la malla. La [guía del repetidor](/repeater-guide/#config) explica las dos formas.

Desde la 1.18, un companion (el nodo desde el que envías mensajes, emparejado con tu teléfono o portátil, o con pantalla propia) también tiene línea de comandos. Abre Command Line en los ajustes de la app de MeshCore, versión 1.50 o posterior. Un contacto con el permiso Remote CLI puede enviar a tu companion los mismos comandos por la malla. Eso incluye los comandos de WiFi y de PIN.

El valor con el que empieza un comando es el del repetidor. Un servidor de sala, un sensor o un companion pueden empezar con otro valor. Un comando que solo tiene un companion muestra el suyo.
