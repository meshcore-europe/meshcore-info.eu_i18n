---
title: Skapa en nyckel
layout: keygen
lead: Ge din repeater ett prefix som ingen repeater nära dig använder. Hitta ett ledigt prefix, skapa en nyckel som börjar med det och ställ in den.
description: Skapa en MeshCore-nyckel med ett prefix du väljer, direkt i webbläsaren, så att ingen repeater nära din delar prefix med den i en väg.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-31'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

En repeater skickar vidare meddelanden åt alla omkring sig. I en väg
anger MeshCore varje repeater med de första bytena i dess offentliga nyckel:
dess prefix. Har en repeater nära dig samma prefix visar en väg inte
vilken av de två som skickade meddelandet vidare. MeshCore väljer nyckeln slumpmässigt. Här
skapar du en nyckel med det prefix du vill ha.

Välj 2 byte. Den 13 oktober 2026 såg [MeshCore Analyzer](https://meshcore-analyzer.eu/)
att varje prefix på 1 byte delades av flera i Europa. Path hash size är en inställning hos avsändaren.
Den avgör hur många byte av varje prefix som hamnar i en väg. Se [CLI-kommandon](/guides/cli/).
