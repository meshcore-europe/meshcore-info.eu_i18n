---
title: Een sleutel maken
layout: keygen
lead: Geef je repeater een prefix die geen repeater bij jou in de buurt gebruikt. Zoek een vrije prefix, maak een sleutel die ermee begint en stel die in.
description: Maak in je browser een MeshCore-sleutel met een prefix die je zelf kiest. Dan deelt geen repeater bij de jouwe zijn prefix in een pad.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-31'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

Een repeater stuurt berichten door voor iedereen om hem heen. In een pad
geeft MeshCore elke repeater aan met de eerste bytes van zijn publieke sleutel:
zijn prefix. Als een repeater bij jou in de buurt dezelfde prefix heeft, zie
je in een pad niet welke van de twee een bericht doorstuurde. MeshCore kiest
de sleutel willekeurig. Hier maak je er een met de prefix die jij wilt.

Neem 2 bytes. Op 13 oktober 2026 zag de [MeshCore Analyzer](https://meshcore-analyzer.eu/)
dat in Europa elke prefix van 1 byte meer dan eens voorkwam. De afzender bepaalt met de
instelling path hash size hoeveel bytes van elke prefix in een pad komen. Zie
[CLI-commando's](/guides/cli/).
