---
title: Générer une clé
layout: keygen
lead: Donne à ton répéteur un préfixe qu'aucun répéteur près de chez toi n'utilise. Trouve un préfixe libre, crée une clé qui commence par ce préfixe, puis applique-la.
description: Crée une clé MeshCore avec le préfixe de ton choix, dans ton navigateur, pour qu'aucun répéteur près du tien ne partage son préfixe dans un chemin.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-26'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
---

Un répéteur transmet les messages pour tous ceux qui l'entourent. Dans un chemin, MeshCore
désigne chaque répéteur par les premiers octets de sa clé publique :
son préfixe. Si un répéteur près de chez toi a le même préfixe, le chemin ne montre pas
lequel des deux a transmis un message. MeshCore choisit la clé au hasard. Ici,
tu en crées une avec le préfixe que tu veux.

Prends 2 octets. Le 13 octobre 2026, le [MeshCore Analyzer](https://meshcore-analyzer.eu/)
a constaté que chaque préfixe de 1 octet était partagé en Europe. La taille du hachage de chemin, un réglage de
l'expéditeur, décide combien d'octets de chaque préfixe entrent dans un chemin ; voir [Commandes CLI](/guides/cli/).
