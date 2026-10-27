---
title: Seriële console
layout: console
lead: Stuur vanuit je browser commando's naar je repeater, via USB.
description: Stel een MeshCore-repeater, room server of sensor via USB in vanuit Chrome, Edge of Opera, met een seriële console in de browser. Je hoeft geen programma te installeren.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-26'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: 'a2fe0704'}
  sections: ['c33167ce']
---

Een repeater (die geeft berichten door), een room server (die bewaart berichten voor een groep) of een sensor (die meldt meetwaarden) heeft geen app. Je stelt hem daarom in door via USB commando's te typen. Sluit je node aan op je computer, open deze pagina in Chrome, Edge of Opera op een computer en kies de poort van je node. De console stuurt eerst `get role` en `ver`, zodat hij weet wat voor node je hebt. Beide lezen alleen uit. Daarna zie je wat je node terugstuurt. Typ een commando zoals `get name` en druk op Enter. Terwijl je typt, stelt de console de commando's voor die je node begrijpt. Met Tab vul je het eerste voorstel in.

Een companion, de node waarmee je berichten stuurt, praat via USB met de app. Zijn commandoregel zit in de MeshCore-app, versie 1.50 of nieuwer.
