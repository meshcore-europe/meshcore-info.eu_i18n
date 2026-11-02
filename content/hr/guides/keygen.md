---
title: Generiraj ključ
layout: keygen
lead: Daj svom repetitoru prefiks koji ne koristi nijedan repetitor u tvojoj blizini. Pronađi slobodan prefiks, napravi ključ koji njime počinje i postavi ga.
description: Napravi MeshCore ključ s prefiksom po svom izboru u pregledniku, tako da nijedan repetitor blizu tvojeg nema isti prefiks u putanji.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-11-02'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

Repetitor prosljeđuje poruke za sve oko sebe. U putanji MeshCore označava
svaki repetitor prvim bajtovima njegova javnog ključa: to je njegov prefiks.
Ako repetitor u tvojoj blizini ima isti prefiks, putanja ne pokazuje
koji je od ta dva repetitora proslijedio poruku. MeshCore bira ključ nasumično. Ovdje
izrađuješ ključ s prefiksom koji želiš.

Uzmi 2 bajta. [MeshCore Analyzer](https://meshcore-analyzer.eu/) utvrdio je 13. listopada 2026.
da u Europi više repetitora dijeli svaki prefiks od 1 bajta. Veličina hasha putanje,
postavka pošiljatelja, određuje koliko bajtova svakog prefiksa ulazi u putanju; pogledaj [CLI naredbe](/guides/cli/).
