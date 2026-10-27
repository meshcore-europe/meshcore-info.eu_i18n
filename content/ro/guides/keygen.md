---
title: Generează o cheie
layout: keygen
lead: Dă repetorului tău un prefix pe care niciun repetor din apropiere nu îl folosește. Găsește un prefix liber, creează o cheie care începe cu el și seteaz-o.
description: Creează o cheie MeshCore cu un prefix ales de tine, direct în browser, ca niciun repetor din apropierea ta să nu aibă același prefix într-o rută.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-26'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
---

Un repetor transmite mai departe mesajele tuturor din jurul lui. Într-o rută, MeshCore
identifică fiecare repetor prin primii octeți ai cheii sale publice:
prefixul. Când un repetor din apropierea ta are același prefix, ruta nu arată
care dintre cele două a transmis mesajul. MeshCore alege cheia la întâmplare. Aici
îți creezi una cu prefixul dorit.

Alege 2 octeți. Pe 13 octombrie 2026, [MeshCore Analyzer](https://meshcore-analyzer.eu/)
a văzut că fiecare prefix de 1 octet era folosit de mai multe repetoare în Europa. Dimensiunea hash-ului de rută, o setare a
expeditorului, stabilește câți octeți din fiecare prefix intră într-o rută; vezi [Comenzi CLI](/guides/cli/).
