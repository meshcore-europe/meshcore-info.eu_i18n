---
title: Lag en nøkkel
layout: keygen
lead: Gi repeateren din et prefiks som ingen repeater i nærheten bruker. Finn et ledig prefiks, lag en nøkkel som begynner med det, og legg den inn.
description: Lag en MeshCore-nøkkel med et prefiks du velger selv, i nettleseren, slik at ingen repeater nær din deler prefikset i en sti.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-31'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

En repeater sender meldinger videre for alle rundt seg. I en sti navngir MeshCore
hver repeater etter de første bytene i den offentlige nøkkelen:
prefikset. Har en repeater i nærheten samme prefiks, viser ikke stien
hvilken av de to som sendte en melding videre. MeshCore velger nøkkelen tilfeldig. Her
lager du en med prefikset du ønsker.

Bruk 2 byte. Den 13. oktober 2026 så [MeshCore Analyzer](https://meshcore-analyzer.eu/)
at hvert prefiks på 1 byte var delt i Europa. Innstillingen path hash size hos avsenderen
bestemmer hvor mange byte av hvert prefiks som havner i en sti. Se [CLI-kommandoer](/guides/cli/).
