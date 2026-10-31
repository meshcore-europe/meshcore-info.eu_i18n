---
title: CLI-kommandoer
layout: cli
lead: Alle kommandoene til repeateren, romserveren, sensoren eller companion-enheten din, sortert etter hva du vil gjøre. Les hva kommandoen gjør og hvilken verdi den starter med, fyll inn din egen og kopier den.
description: 'Alle kommandoene i MeshCore-firmware 1.18.0 for repeatere, romservere, sensorer og companion-enheter, sortert etter oppgave: hva de gjør, verdien firmwaren starter med, og hvilke noder som har dem.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-31'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Kommandoene følger MeshCore-firmware 1.18.0, hentet fra kildekoden til firmwaren.
Er en kommando lagt til i en nyere versjon, står det hvilken versjon den krever. En
repeater sender meldinger videre, en romserver lagrer innlegg for en gruppe, og en sensor
rapporterer måleverdier. Romservere, sensorer og companion-enheter har mange kommandoer felles.
Ved hver kommando står det hvilke noder som har den. Med «Hvilken node?» ser du bare kommandoene
for noden din.

På en repeater, romserver eller sensor skriver du dem inn over USB fra datamaskinen,
for eksempel i [seriekonsollen](/firmware/console/) her på nettstedet. Med MeshCore-appen sender du dem over meshen.
[Repeater-guiden](/repeater-guide/#config) viser begge måtene.

Fra og med 1.18 har også en companion-enhet (noden du sender meldinger fra, paret med telefonen eller den bærbare PC-en din, eller
med egen skjerm) en kommandolinje. Åpne Command Line i innstillingene i MeshCore-appen, versjon 1.50 eller
nyere. En kontakt med tillatelsen Remote CLI kan sende de samme kommandoene til companion-enheten din over meshen.
Det gjelder også WiFi- og PIN-kommandoene.

Startverdien som står ved en kommando, er repeaterens. En romserver, sensor eller
companion-enhet kan starte med en annen verdi. En kommando som bare finnes på en companion-enhet, viser sin egen startverdi.
