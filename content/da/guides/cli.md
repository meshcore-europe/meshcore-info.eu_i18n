---
title: CLI-kommandoer
layout: cli
lead: Alle kommandoer til din repeater, room server, sensor eller companion, grupperet efter det du vil gøre. Læs hvad den gør og hvilken værdi den starter med, indsæt din egen og kopier den.
description: 'Alle kommandoer i MeshCore firmware 1.18.0 til repeatere, room servere, sensorer og companions, grupperet efter opgave: hvad den gør, hvilken værdi firmwaren starter med, og hvilke noder der har den.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-26'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
---

Disse kommandoer følger MeshCore firmware 1.18.0 og er læst fra firmwarens kildekode. En kommando, der er tilføjet i en nyere version, angiver hvilken version den kræver. En repeater sender beskeder videre, en room server gemmer indlæg for en gruppe, en sensor rapporterer målinger. Room servere, sensorer og companions deler mange kommandoer. Hver kommando angiver hvilke noder der har den. "Hvilken node?" viser kun kommandoerne til din.

På en repeater, room server eller sensor skriver du dem over USB fra din computer, for eksempel i [seriel-konsollen](/firmware/console/) her på siden. MeshCore-appen sender dem over meshen. [Repeater-guiden](/repeater-guide/#config) viser begge dele.

Siden 1.18 har en companion (den node du sender beskeder fra, parret med din telefon eller laptop, eller med sin egen skærm) også en kommandolinje. Åbn Command Line i indstillingerne i MeshCore-appen, version 1.50 eller nyere. En kontakt med tilladelsen Remote CLI kan sende din companion de samme kommandoer over meshen. Det gælder også WiFi- og PIN-kommandoerne.

Den værdi, en kommando starter med, er repeaterens. En room server, sensor eller companion kan starte med en anden værdi. En kommando, som kun en companion har, viser sin egen.
