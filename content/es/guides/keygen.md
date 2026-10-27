---
title: Generar una clave
layout: keygen
lead: Dale a tu repetidor un prefijo que ningún repetidor cercano use. Busca un prefijo libre, crea una clave que empiece por él y configúrala.
description: Crea una clave MeshCore con el prefijo que elijas, en tu navegador, para que ningún repetidor cercano comparta su prefijo en una ruta.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-26'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
---

Un repetidor reenvía los mensajes de todos los que tiene alrededor. En una ruta, MeshCore
identifica cada repetidor por los primeros bytes de su clave pública:
su prefijo. Si un repetidor cercano tiene el mismo prefijo, la ruta no muestra
cuál de los dos reenvió el mensaje. MeshCore elige la clave al azar. Aquí
creas una con el prefijo que tú quieras.

Usa 2 bytes. El 13 de octubre de 2026, el [MeshCore Analyzer](https://meshcore-analyzer.eu/)
detectó que todos los prefijos de 1 byte estaban repetidos en Europa. El tamaño del hash de ruta, un ajuste
del emisor, decide cuántos bytes de cada prefijo entran en una ruta; consulta [Comandos CLI](/guides/cli/).
