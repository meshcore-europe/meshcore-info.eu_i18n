---
title: Console série
layout: console
lead: Envoie des commandes à ton répéteur depuis ton navigateur, par USB.
description: Configure un répéteur, un room server ou un capteur MeshCore par USB depuis Chrome, Edge ou Opera, avec une console série dans le navigateur, sans rien installer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-31'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Un répéteur (il relaie les messages), un room server (il garde les messages d'un
groupe) ou un capteur (il transmet ses mesures) n'a pas d'application. Tu le
configures donc en tapant des commandes par USB. Branche ton nœud sur ton
ordinateur. Ouvre cette page dans Chrome, Edge ou Opera sur un ordinateur, puis
choisis le port de ton nœud. La console envoie d'abord `get role` et `ver` pour
savoir ce qu'est ton nœud. Ces deux commandes ne font que lire. Ensuite, la console
affiche ce que répond ton nœud. Tape une commande comme `get name` et appuie
sur Entrée. Pendant que tu tapes, la console te propose les commandes que ton
nœud comprend. La touche Tab complète la première.

Un companion, le nœud depuis lequel tu envoies tes messages, communique plutôt
avec l'application par USB. Sa ligne de commande se trouve dans l'application
MeshCore, version 1.50 ou ultérieure.
