---
title: Générer une clé
layout: keygen
lead: Donne à ton répéteur un préfixe qu'aucun répéteur proche n'utilise. Trouve un préfixe libre, crée une clé qui commence par celui-ci, puis configure-la.
description: Crée dans ton navigateur une clé MeshCore avec le préfixe de ton choix, pour qu'aucun répéteur proche du tien ne partage son préfixe dans un chemin.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-31'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

Un répéteur relaie les messages pour tous ceux qui l'entourent. Dans un chemin,
MeshCore désigne chaque répéteur par les premiers octets de sa clé publique :
son préfixe. Si un répéteur proche de toi a le même préfixe, le chemin ne montre
pas lequel des deux a relayé un message. MeshCore choisit la clé au hasard. Ici,
tu en crées une avec le préfixe que tu veux.

Prends 2 octets. Le 13 octobre 2026, le [MeshCore Analyzer](https://meshcore-analyzer.eu/)
a constaté que chaque préfixe de 1 octet était partagé en Europe. La taille du hash de chemin,
un réglage de l'expéditeur, fixe le nombre d'octets de chaque préfixe qui entrent dans
un chemin ; consulte les [commandes CLI](/guides/cli/).
