---
title: Consola serie
layout: console
lead: Escribe comandos a tu repetidor desde el navegador, por USB.
description: Configura un repetidor, un room server o un sensor de MeshCore por USB desde Chrome, Edge u Opera, con una consola serie en el navegador. No hay nada que instalar.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-26'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: 'a2fe0704'}
  sections: ['c33167ce']
---

Un repetidor (reenvía mensajes), un room server (guarda publicaciones para un grupo) o un sensor (envía lecturas) no tiene app, así que lo configuras escribiendo comandos por USB. Conecta tu nodo al ordenador, abre esta página en Chrome, Edge u Opera en un ordenador y elige el puerto de tu nodo. La consola envía primero `get role` y `ver`, para saber qué es tu nodo. Ambos solo leen. Después muestra lo que responde tu nodo; escribe un comando como `get name` y pulsa Enter. Mientras escribes, te sugiere los comandos que tu nodo entiende, y con Tab completas el primero.

Un companion, el nodo desde el que envías mensajes, habla con la app por USB en su lugar. Su línea de comandos está en la app de MeshCore, versión 1.50 o posterior.
