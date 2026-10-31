---
title: CLI-kommandoer
layout: cli
lead: Alle kommandoer til din repeater, room server, sensor eller companion, ordnet efter hvad du vil gøre. Læs hvad kommandoen gør og hvilken værdi den starter med, udfyld din egen og kopiér den.
description: 'Alle kommandoer i MeshCore firmware 1.18.0 til repeatere, room servere, sensorer og companions, ordnet efter opgave: hvad kommandoen gør, hvilken værdi firmwaren starter med, og hvilke noder der har den.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-31'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Kommandoerne følger MeshCore firmware 1.18.0 og er læst ud af firmwarens
kildekode. Er en kommando kommet til i en nyere version, står det, hvilken
version den kræver. En repeater sender beskeder videre. En room server gemmer
indlæg for en gruppe, og en sensor rapporterer målinger. Room servere, sensorer og
companions har mange kommandoer til fælles. Ved hver kommando står det, hvilke
noder der har den. Med "Hvilken node?" ser du kun kommandoerne for din egen node.

På en repeater, room server eller sensor skriver du kommandoerne over USB fra
din computer, for eksempel i [den serielle konsol](/firmware/console/) her på siden. MeshCore-appen sender dem over mesh'et. I
[repeater-guiden](/repeater-guide/#config) kan du se begge måder.

Siden 1.18 har en companion også en kommandolinje. En companion er den node,
du skriver beskeder fra, parret med din telefon eller bærbare eller med sin
egen skærm. Åbn Command Line i indstillingerne i MeshCore-appen, version 1.50
eller nyere. En kontakt med tilladelsen Remote CLI kan sende din companion de
samme kommandoer over mesh'et. Det gælder også WiFi- og PIN-kommandoerne.

Startværdien ved en kommando er repeaterens. En room server, sensor eller
companion kan starte med en anden værdi. Har kun en companion kommandoen, står
companionens egen værdi der.
