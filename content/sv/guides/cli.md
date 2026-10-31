---
title: CLI-kommandon
layout: cli
lead: Alla kommandon för din repeater, room server, sensor eller companion, sorterade efter vad du vill göra. Läs vad kommandot gör och vilket värde det har från början, fyll i ditt eget och kopiera det.
description: 'Alla kommandon i MeshCore firmware 1.18.0 för repeaters, room servers, sensorer och companions, sorterade efter uppgift: vad de gör, vilket värde firmware har från början och vilka noder som har dem.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-31'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Kommandona följer MeshCore firmware 1.18.0 och är hämtade ur källkoden till firmware.
Kommer ett kommando från en nyare version, står det vilken version det kräver. En
repeater skickar vidare meddelanden, en room server sparar inlägg för en grupp och en sensor
rapporterar mätvärden. Room servers, sensorer och companions har många kommandon gemensamt.
Vid varje kommando står det vilka noder som har det. Med "Vilken nod?" ser du bara kommandona
för dina noder.

På en repeater, room server eller sensor skriver du kommandona via USB från din
dator, till exempel i [seriekonsolen](/firmware/console/) här på sajten. MeshCore-appen skickar dem via meshen.
[Repeaterguiden](/repeater-guide/#config) visar båda sätten.

Sedan 1.18 har även en companion en kommandorad. En companion är noden du skickar meddelanden från. Den är parkopplad med din telefon eller laptop, eller
har en egen skärm.
Öppna Command Line i inställningarna i MeshCore-appen, version 1.50 eller
senare. En kontakt med behörigheten Remote CLI kan skicka samma kommandon till din companion via meshen.
Det gäller även kommandona för WiFi och PIN.

Värdet som ett kommando börjar med är repeaterns. En room server, sensor eller
companion kan börja med ett annat värde. Ett kommando som bara finns på en companion visar sitt eget värde.
