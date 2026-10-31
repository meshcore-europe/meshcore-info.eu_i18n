---
title: Seriell konsol
layout: console
lead: Skriv kommandon till din repeater från webbläsaren, via USB.
description: Ställ in en MeshCore-repeater, room server eller sensor via USB i Chrome, Edge eller Opera, med en seriell konsol i webbläsaren och utan att installera något.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-31'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

En repeater (den skickar vidare meddelanden), en room server (den sparar inlägg
åt en grupp) eller en sensor (den rapporterar mätvärden) har ingen app. Därför ställer
du in den genom att skriva kommandon via USB. Anslut noden till datorn. Öppna
den här sidan i Chrome, Edge eller Opera på datorn och välj nodens port. Först
skickar konsolen `get role` och `ver`, så att den vet vad det är för nod. Båda
kommandona läser bara. Sedan visar konsolen vad noden svarar. Skriv ett kommando,
till exempel `get name`, och tryck på Enter. Medan du skriver föreslår konsolen de kommandon
som noden förstår, och med Tab fyller du i det första.

En companion, den nod du skickar meddelanden från, pratar i stället med appen via USB. Kommandoraden för den finns i
MeshCore-appen, version 1.50 eller senare.
