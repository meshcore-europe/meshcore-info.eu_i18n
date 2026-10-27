---
title: Seriell konsoll
layout: console
lead: Skriv kommandoer til repeateren din fra nettleseren, over USB.
description: Sett opp en MeshCore-repeater, romserver eller sensor over USB fra Chrome, Edge eller Opera, med en seriell konsoll i nettleseren. Ingen program å installere.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-26'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: 'a2fe0704'}
  sections: ['c33167ce']
---

En repeater (den sender meldinger videre), en romserver (den lagrer innlegg for en gruppe) eller en sensor (den rapporterer målinger) har ingen app. Derfor setter du den opp ved å skrive kommandoer over USB. Koble noden din til datamaskinen, åpne denne siden i Chrome, Edge eller Opera på en datamaskin, og velg porten til noden din. Konsollen sender først `get role` og `ver`, så den vet hva noden din er. Begge bare leser. Deretter viser den det noden din sier. Skriv en kommando som `get name` og trykk Enter. Mens du skriver, foreslår den kommandoene noden din forstår, og Tab fyller inn den første.

En companion, noden du sender meldinger fra, snakker i stedet med appen over USB. Kommandolinjen dens ligger i MeshCore-appen, versjon 1.50 eller nyere.
