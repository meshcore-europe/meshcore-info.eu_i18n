---
title: Seriekonsoll
layout: console
lead: Skriv kommandoer til repeateren din fra nettleseren, over USB.
description: Sett opp en MeshCore-repeater, en romserver eller en sensor over USB fra Chrome, Edge eller Opera. Seriekonsollen kjører i nettleseren, og du trenger ikke installere noe.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-31'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

En repeater (den sender meldinger videre), en romserver (den lagrer innlegg for en gruppe) eller en sensor (den rapporterer måleverdier) har ingen app. Derfor setter du den opp ved å skrive kommandoer over USB. Koble noden til datamaskinen, og åpne denne siden i Chrome, Edge eller Opera på datamaskinen. Velg så porten til noden din. Konsollen sender først `get role` og `ver`, slik at den vet hva slags node du har. Begge kommandoene leser bare. Deretter viser konsollen det noden svarer. Skriv en kommando som `get name`, og trykk Enter. Mens du skriver, foreslår konsollen kommandoene noden din forstår, og Tab fyller inn den første.

En companion, noden du sender meldinger fra, snakker i stedet med appen over USB. Kommandolinjen for den finner du i MeshCore-appen, versjon 1.50 eller nyere.
