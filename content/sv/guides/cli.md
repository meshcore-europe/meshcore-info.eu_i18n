---
title: CLI-kommandon
layout: cli
lead: Alla kommandon för din repeater, rumsserver, sensor eller companion, grupperade efter vad du vill göra. Läs vad kommandot gör och vilket värde det börjar med, fyll i ditt eget och kopiera det.
description: 'Alla kommandon i MeshCore firmware 1.18.0 för repeatrar, rumsservrar, sensorer och companions, grupperade efter uppgift: vad kommandot gör, vilket värde firmware börjar med och vilka noder som har det.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-26'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
---

Kommandona här följer MeshCore firmware 1.18.0 och kommer från firmwarens källkod. Ett kommando som tillkom i en nyare version anger vilken version det kräver. En repeater skickar meddelanden vidare, en rumsserver sparar inlägg för en grupp, en sensor rapporterar mätvärden. Rumsservrar, sensorer och companions har många kommandon gemensamt. Vid varje kommando står vilka noder som har det. Under "Vilken nod?" ser du bara kommandona för din egen.

På en repeater, rumsserver eller sensor skriver du kommandona via USB från din dator, till exempel i [seriekonsolen](/firmware/console/) här på sidan. MeshCore-appen skickar dem över meshen. [Repeaterguiden](/repeater-guide/#config) visar båda sätten.

Sedan 1.18 har även en companion en kommandorad. En companion är noden du skickar meddelanden från, parkopplad med din telefon eller dator, eller med egen skärm. Öppna Command Line i inställningarna i MeshCore-appen, version 1.50 eller senare. En kontakt med behörigheten Remote CLI kan skicka samma kommandon till din companion över meshen. Det gäller även kommandona för WiFi och PIN.

Startvärdet som anges för ett kommando gäller repeatern. En rumsserver, sensor eller companion kan börja med ett annat värde. Ett kommando som bara en companion har visar sitt eget värde.
