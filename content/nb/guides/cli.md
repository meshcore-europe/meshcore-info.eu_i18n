---
title: CLI-kommandoer
layout: cli
lead: Alle kommandoene til repeateren, romserveren, sensoren eller companionen din, sortert etter hva du vil gjøre. Les hva de gjør og hvilken verdi de starter med, fyll inn din egen og kopier den.
description: 'Alle kommandoene i MeshCore-firmware 1.18.0 for repeatere, romservere, sensorer og companioner, sortert etter oppgave: hva de gjør, hvilken verdi firmwaren starter med, og hvilke noder som har dem.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-26'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
---

Disse kommandoene følger MeshCore-firmware 1.18.0, hentet fra kildekoden til firmwaren. En kommando som kom til i en nyere versjon, oppgir hvilken versjon den krever. En repeater sender meldinger videre, en romserver lagrer innlegg for en gruppe, en sensor rapporterer målinger. Romservere, sensorer og companioner deler mange kommandoer. Hver kommando oppgir hvilke noder som har den. "Hvilken node?" viser bare kommandoene for din.

På en repeater, romserver eller sensor skriver du dem inn over USB fra datamaskinen, for eksempel i [seriekonsollen](/firmware/console/) på dette nettstedet. MeshCore-appen sender dem over meshen. [Repeaterguiden](/repeater-guide/#config) viser begge måtene.

Siden 1.18 har også en companion en kommandolinje. En companion er noden du sender meldinger fra, paret med telefonen eller laptopen din, eller med egen skjerm. Åpne Command Line i innstillingene i MeshCore-appen, versjon 1.50 eller nyere. En kontakt med tillatelsen Remote CLI kan sende companionen din de samme kommandoene over meshen. Det gjelder også WiFi- og PIN-kommandoene.

Verdien en kommando starter med, er repeaterens. En romserver, sensor eller companion kan starte på en annen verdi. En kommando som bare en companion har, viser sin egen verdi.
