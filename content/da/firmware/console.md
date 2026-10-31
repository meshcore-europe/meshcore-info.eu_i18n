---
title: Seriel konsol
layout: console
lead: Skriv kommandoer til din repeater fra din browser via USB.
description: Konfigurer en MeshCore-repeater, en room server eller en sensor via USB fra Chrome, Edge eller Opera med en seriel konsol i browseren. Du skal ikke installere noget.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-31'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

En repeater (den sender beskeder videre), en room server (den gemmer indlæg for en gruppe) eller en sensor (den rapporterer målinger) har ingen app. Derfor sætter du den op ved at skrive kommandoer via USB. Slut din node til computeren, og åbn denne side i Chrome, Edge eller Opera på en computer. Vælg derefter din nodes port. Konsollen sender først `get role` og `ver`, så den ved, hvad din node er. Begge kommandoer læser kun. Derefter viser konsollen, hvad din node svarer. Skriv en kommando som `get name`, og tryk på Enter. Mens du skriver, foreslår konsollen de kommandoer, din node forstår. Med Tab udfylder du den første.

En companion er den node, du sender beskeder fra. Den taler i stedet med appen via USB. Dens kommandolinje finder du i MeshCore-appen, version 1.50 eller nyere.
