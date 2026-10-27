---
title: Lag en nøkkel
layout: keygen
lead: Gi repeateren din et prefiks som ingen repeater i nærheten bruker. Finn et ledig prefiks, lag en nøkkel som starter med det, og sett den.
description: Lag en MeshCore-nøkkel med et prefiks du velger selv, i nettleseren, slik at ingen repeater nær din deler prefiks i en sti.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-26'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
---

En repeater sender meldinger videre for alle rundt seg. I en sti
navngir MeshCore hver repeater med de første bytene i den offentlige nøkkelen:
prefikset. Når en repeater i nærheten har samme prefiks, viser ikke stien
hvilken av de to som sendte meldingen videre. MeshCore velger nøkkelen tilfeldig. Her
lager du en med det prefikset du ønsker.

Bruk 2 byte. Den 13. oktober 2026 så [MeshCore Analyzer](https://meshcore-analyzer.eu/)
at alle 1-byte-prefikser i Europa var delt. Stihash-størrelsen, en innstilling hos
avsenderen, bestemmer hvor mange byte av hvert prefiks som tas med i en sti; se [CLI-kommandoer](/guides/cli/).
