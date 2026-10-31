---
title: Generează o cheie
layout: keygen
lead: Dă-i repetorului tău un prefix pe care nu-l folosește niciun repetor din apropiere. Găsește un prefix liber, creează o cheie care începe cu el și seteaz-o.
description: Creează în browser o cheie MeshCore cu un prefix ales de tine, ca niciun repetor din apropiere să nu aibă același prefix într-o rută.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-31'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

Un repetor transmite mai departe mesajele pentru toți cei din jurul lui. Într-o rută,
MeshCore numește fiecare repetor după primii octeți ai cheii lui publice:
prefixul lui. Dacă un repetor din apropierea ta are același prefix, ruta nu arată
care dintre cele două a transmis mesajul. MeshCore alege cheia la întâmplare. Aici
îți creezi tu o cheie cu prefixul pe care îl vrei.

Folosește 2 octeți. Pe 13 octombrie 2026, [MeshCore Analyzer](https://meshcore-analyzer.eu/)
a găsit fiecare prefix de 1 octet folosit de mai multe noduri în Europa. Expeditorul alege în setări dimensiunea hash-ului de rută. De ea depinde câți octeți din fiecare prefix intră într-o rută. Vezi [comenzile CLI](/guides/cli/).
