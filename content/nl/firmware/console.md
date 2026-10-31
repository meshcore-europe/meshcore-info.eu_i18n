---
title: Seriële console
layout: console
lead: Typ via USB opdrachten naar je repeater, vanuit je browser.
description: Stel een MeshCore-repeater, room server of sensor via USB in vanuit Chrome, Edge of Opera, met een seriële console in de browser. Je hoeft niets te installeren.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-31'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Een repeater (die geeft berichten door), een room server (die bewaart berichten
voor een groep) of een sensor (die meldt meetwaarden) heeft geen app. Je
stelt hem daarom in door via USB opdrachten te typen. Sluit je node aan op je
computer, open deze pagina in Chrome, Edge of Opera op een computer en kies de
poort van je node. De console stuurt eerst `get role` en `ver`, zodat hij weet
wat voor node je hebt. Beide lezen alleen gegevens uit. Daarna zie je wat je node
terugmeldt. Typ een opdracht zoals `get name` en druk op Enter. Terwijl je typt,
stelt de console de opdrachten voor die je node begrijpt. Met Tab vul je de
eerste in.

Een companion, de node waarmee je berichten verstuurt, praat in plaats daarvan
via USB met de app. De opdrachtregel daarvan vind je in de MeshCore-app, versie
1.50 of nieuwer.
