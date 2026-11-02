---
title: Mapes de cobertura
layout: map
lead: Mira fins on arriba la xarxa mesh, on són els nodes i com viatgen els missatges. Comunitats de tot Europa mantenen aquests mapes.
description: Mapes de MeshCore en directe, mapes de cobertura i analitzadors de paquets per a Europa i per a països concrets.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '351071aa'
  seeded: '2026-11-02'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['351071aa']
  blocks: ['dd5f039e', '9d4a2ad8', '70c417f2', '9fef7e16']
---

Un node apareix en aquests mapes quan el propietari el publica o quan
l'escolta un *observador*: un node que reenvia per MQTT tot el que escolta. Per
això cap mapa és complet. Els analitzadors mostren el trànsit que reben els seus
observadors: paquets, rutes i activitat dels canals. Els missatges directes
continuen xifrats, i per això cap analitzador en mostra el contingut.

Cada node surt al mapa on l'ha posat el propietari, i aquesta posició pot
ser errònia o estar desactualitzada. Un missatge per inundació (flood) viatja per
diversos camins alhora. Una ruta al mapa és el camí de la còpia que ha arribat
primer; els altres camins no queden registrats.

Aquests mapes necessiten internet; la xarxa mesh, no. [Per què](/network/)

Tens un repetidor, un node que retransmet missatges? Indica'n la posició amb `set lat` i `set lon`, i els mapes el podran situar. La [guia del repetidor](/repeater-guide/#config) t'explica com fer-ho.
