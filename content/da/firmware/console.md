---
title: Seriel konsol
layout: console
lead: Skriv kommandoer til din repeater fra din browser, over USB.
description: Konfigurer en MeshCore repeater, room server eller sensor over USB fra Chrome, Edge eller Opera, med en seriel konsol i browseren. Intet program at installere.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-26'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: 'a2fe0704'}
  sections: ['c33167ce']
---

En repeater (den sender beskeder videre), en room server (den gemmer indlæg til en gruppe) eller en sensor (den rapporterer målinger) har ingen app, så du sætter den op ved at skrive kommandoer over USB. Sæt din node til din computer, åbn denne side i Chrome, Edge eller Opera på en computer, og vælg din nodes port. Konsollen sender først `get role` og `ver`, så den ved, hvad din node er. Begge læser kun. Derefter viser den, hvad din node svarer; skriv en kommando som `get name` og tryk på Enter. Mens du skriver, foreslår den de kommandoer, din node forstår, og Tab udfylder den første.

En companion, den node du sender beskeder fra, taler i stedet med appen over USB. Dens kommandolinje findes i MeshCore-appen, version 1.50 eller nyere.
