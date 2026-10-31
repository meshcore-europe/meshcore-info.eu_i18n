---
title: Generér en nøgle
layout: keygen
lead: Giv din repeater et præfiks, som ingen repeater i nærheden bruger. Find et ledigt præfiks, lav en nøgle, der starter med det, og indstil den.
description: Lav en MeshCore-nøgle med et præfiks, du selv vælger, i din browser, så ingen repeater i nærheden har samme præfiks i en sti.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-31'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

En repeater sender beskeder videre for alle omkring sig. I en sti angiver MeshCore
hver repeater med de første bytes af dens offentlige nøgle:
dens præfiks. Har en repeater i nærheden samme præfiks, kan du ikke se i stien,
hvilken af de to der sendte en besked videre. MeshCore vælger nøglen tilfældigt. Her
laver du en med det præfiks, du vil have.

Brug 2 bytes. Den 13. oktober 2026 så [MeshCore Analyzer](https://meshcore-analyzer.eu/),
at alle præfikser på 1 byte var i brug mere end én gang i Europa. Indstillingen path hash size hos afsenderen
bestemmer, hvor mange bytes af hvert præfiks der kommer med i en sti. Se [CLI-kommandoer](/guides/cli/).
