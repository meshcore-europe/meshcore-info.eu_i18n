---
title: Consola serie
layout: console
lead: Escribe comandos a tu repetidor desde el navegador, por USB.
description: Configura un repetidor, un room server o un sensor MeshCore por USB desde Chrome, Edge u Opera, con una consola serie en el navegador y sin instalar nada.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-31'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Un repetidor (reenvía los mensajes), un room server (guarda las publicaciones
de un grupo) o un sensor (envía sus lecturas) no tiene app. Por eso lo
configuras escribiendo comandos por USB. Conecta tu nodo al ordenador, abre
esta página en Chrome, Edge u Opera en un ordenador y elige el puerto de tu
nodo. Primero, la consola envía `get role` y `ver` para saber qué es tu nodo.
Los dos comandos solo leen. Después, la consola muestra lo que dice tu nodo. Escribe un
comando como `get name` y pulsa Enter. Mientras escribes, la consola te
sugiere los comandos que entiende tu nodo, y con Tab completas el primero.

En cambio, un companion, el nodo desde el que envías tus mensajes, se comunica con la app por USB. Su línea de comandos está en la
app de MeshCore, versión 1.50 o posterior.
