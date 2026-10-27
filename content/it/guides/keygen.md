---
title: Genera una chiave
layout: keygen
lead: Dai al tuo ripetitore un prefisso che nessun ripetitore vicino a te usa. Trova un prefisso libero, crea una chiave che inizia con quel prefisso e impostala.
description: Crea una chiave MeshCore con un prefisso scelto da te, nel tuo browser, così nessun ripetitore vicino al tuo condivide il suo prefisso in un percorso.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-26'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
---

Un ripetitore inoltra i messaggi per tutti quelli intorno a lui. In un percorso, MeshCore
indica ogni ripetitore con i primi byte della sua chiave pubblica:
il suo prefisso. Se un ripetitore vicino a te ha lo stesso prefisso, il percorso non mostra
quale dei due ha inoltrato un messaggio. MeshCore sceglie la chiave a caso. Qui
ne crei una con il prefisso che vuoi tu.

Prendi 2 byte. Il 13 ottobre 2026 il [MeshCore Analyzer](https://meshcore-analyzer.eu/)
ha rilevato che in Europa ogni prefisso da 1 byte era condiviso. La dimensione dell'hash del percorso, un'impostazione
del mittente, decide quanti byte di ogni prefisso entrano in un percorso; vedi [Comandi CLI](/guides/cli/).
