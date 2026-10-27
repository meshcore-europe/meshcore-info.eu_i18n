---
title: Skapa en nyckel
layout: keygen
lead: Ge din repeater ett prefix som ingen repeater i din närhet använder. Hitta ett ledigt prefix, skapa en nyckel som börjar med det och ställ in den.
description: Skapa en MeshCore-nyckel med ett prefix du väljer själv, i din webbläsare, så att ingen repeater nära din delar prefix i en väg.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-26'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
---

En repeater skickar meddelanden vidare åt alla runt omkring. I en väg
anger MeshCore varje repeater med de första bytarna i dess offentliga nyckel:
prefixet. Om en repeater nära dig har samma prefix visar vägen inte
vilken av de två som skickade meddelandet vidare. MeshCore väljer nyckeln slumpmässigt. Här
skapar du en nyckel med det prefix du vill ha.

Välj 2 byte. Den 13 oktober 2026 såg [MeshCore Analyzer](https://meshcore-analyzer.eu/)
att varje prefix på 1 byte delades av flera repeatrar i Europa. Storleken på väghashen, en inställning hos
avsändaren, avgör hur många byte av varje prefix som hamnar i en väg; se [CLI-kommandon](/guides/cli/).
