---
title: Seriell konsol
layout: console
lead: Skriv kommandon till din repeater från webbläsaren, över USB.
description: Konfigurera en MeshCore-repeater, rumsserver eller sensor över USB från Chrome, Edge eller Opera, med en seriell konsol i webbläsaren. Inget program att installera.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-26'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: 'a2fe0704'}
  sections: ['c33167ce']
---

En repeater (den skickar meddelanden vidare), en rumsserver (den sparar inlägg åt en grupp) eller en sensor (den rapporterar mätvärden) har ingen app, så du ställer in den genom att skriva kommandon över USB. Koppla in din nod i datorn, öppna den här sidan i Chrome, Edge eller Opera på en dator och välj din nods port. Konsolen skickar först `get role` och `ver`, så att den vet vad din nod är. Båda läser bara. Sedan visar den vad din nod svarar. Skriv ett kommando som `get name` och tryck på Enter. Medan du skriver föreslår den de kommandon som din nod förstår, och Tab fyller i det första.

En companion, noden du skickar meddelanden från, pratar i stället med appen över USB. Dess kommandorad finns i MeshCore-appen, version 1.50 eller senare.
