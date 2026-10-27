---
title: Een sleutel genereren
layout: keygen
lead: Geef je repeater een prefix die geen enkele repeater bij jou in de buurt gebruikt. Zoek een vrije prefix, maak een sleutel die ermee begint, en stel die in.
description: Maak in je browser een MeshCore-sleutel met een prefix die je zelf kiest, zodat geen repeater bij de jouwe dezelfde prefix in een pad heeft.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-26'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
---

Een repeater geeft berichten door voor iedereen in de omgeving. In een pad
noemt MeshCore elke repeater bij de eerste bytes van zijn publieke sleutel:
de prefix. Heeft een repeater bij jou in de buurt dezelfde prefix, dan laat een
pad niet zien welke van de twee een bericht heeft doorgegeven. MeshCore kiest
de sleutel willekeurig. Hier maak je er een met de prefix die jij wilt.

Neem 2 bytes. Op 13 oktober 2026 zag de [MeshCore Analyzer](https://meshcore-analyzer.eu/)
dat elke prefix van 1 byte in Europa door meerdere repeaters werd gedeeld. De
path hash size, een instelling van de zender, bepaalt hoeveel bytes van elke
prefix in een pad komen; zie [CLI-commando's](/guides/cli/).
