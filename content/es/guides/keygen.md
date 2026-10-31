---
title: Genera una clave
layout: keygen
lead: Dale a tu repetidor un prefijo que no use ningún repetidor cercano. Busca un prefijo libre, crea una clave que empiece por él y configúrala.
description: Crea en tu navegador una clave de MeshCore con el prefijo que elijas. Así ningún repetidor cercano al tuyo comparte su prefijo en una ruta.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-31'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

Un repetidor reenvía mensajes para todos los que tiene alrededor. En una ruta,
MeshCore identifica cada repetidor por los primeros bytes de su clave pública:
su prefijo. Si un repetidor cercano tiene el mismo prefijo, la ruta no muestra
cuál de los dos reenvió un mensaje. MeshCore elige la clave al azar. Aquí
creas una con el prefijo que quieras.

Usa 2 bytes. El 13 de octubre de 2026, el [MeshCore Analyzer](https://meshcore-analyzer.eu/)
vio que todos los prefijos de 1 byte estaban repetidos en Europa. El tamaño del hash de ruta es un ajuste del remitente.
Ese ajuste decide cuántos bytes de cada prefijo entran en una ruta. Consulta [Comandos de la CLI](/guides/cli/).
