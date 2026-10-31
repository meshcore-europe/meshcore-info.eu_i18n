---
title: Genera una chiave
layout: keygen
lead: Dai al tuo ripetitore un prefisso che nessun ripetitore vicino a te usa. Trova un prefisso libero, crea una chiave che inizia con quel prefisso e impostala.
description: Crea nel tuo browser una chiave MeshCore con il prefisso che scegli tu, così nessun ripetitore vicino al tuo ha lo stesso prefisso in un percorso.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-31'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

Un ripetitore inoltra i messaggi per tutti quelli che ha intorno. In un percorso, MeshCore
identifica ogni ripetitore con i primi byte della sua chiave pubblica:
il suo prefisso. Se un ripetitore vicino a te ha lo stesso prefisso, il percorso non mostra
quale dei due ha inoltrato un messaggio. MeshCore sceglie la chiave a caso. Qui
ne crei una con il prefisso che vuoi tu.

Usa 2 byte. Il 13 ottobre 2026 il [MeshCore Analyzer](https://meshcore-analyzer.eu/)
ha rilevato in Europa ogni prefisso da 1 byte condiviso da più ripetitori. La dimensione dell'hash del percorso è un'impostazione del mittente.
Stabilisce quanti byte di ogni prefisso entrano in un percorso; vedi [comandi CLI](/guides/cli/).
