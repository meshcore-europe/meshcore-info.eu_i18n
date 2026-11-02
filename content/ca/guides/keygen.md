---
title: Genera una clau
layout: keygen
lead: Dona al teu repetidor un prefix que no faci servir cap repetidor proper. Busca un prefix lliure, crea una clau que comenci així i configura-la.
description: Crea al navegador una clau de MeshCore amb el prefix que triïs, perquè cap repetidor proper comparteixi el prefix del teu en un camí.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-11-02'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

Un repetidor retransmet els missatges per a tothom que té al voltant. En un camí,
MeshCore identifica cada repetidor pels primers bytes de la seva clau pública:
el prefix. Si un repetidor a prop teu té el mateix prefix, el camí no mostra
quin dels dos ha retransmès el missatge. MeshCore tria la clau a l'atzar. Aquí
en crees una amb el prefix que vols.

Tria 2 bytes. El 13 d'octubre de 2026, el [MeshCore Analyzer](https://meshcore-analyzer.eu/)
va detectar que a Europa tots els prefixos d'1 byte estaven compartits. La mida del hash del camí, un ajust del
remitent, decideix quants bytes de cada prefix van a un camí; consulta [ordres de la CLI](/guides/cli/).
