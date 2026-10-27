---
title: Console série
layout: console
lead: Envoie des commandes à ton répéteur depuis ton navigateur, par USB.
description: Configure un répéteur, un room server ou un capteur MeshCore par USB depuis Chrome, Edge ou Opera, avec une console série dans le navigateur. Rien à installer.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-26'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: 'a2fe0704'}
  sections: ['c33167ce']
---

Un répéteur (il relaie les messages), un room server (il conserve les messages d'un groupe) ou un capteur (il transmet des mesures) n'a pas d'appli. Tu le configures donc en tapant des commandes par USB. Branche ton nœud à ton ordinateur, ouvre cette page dans Chrome, Edge ou Opera sur un ordinateur, et choisis le port de ton nœud. La console envoie d'abord `get role` et `ver` pour savoir ce qu'est ton nœud. Ces deux commandes ne font que lire. Ensuite, elle affiche ce que ton nœud répond. Tape une commande comme `get name` et appuie sur Entrée. Pendant que tu tapes, elle te propose les commandes que ton nœud comprend. La touche Tab complète avec la première.

Un companion, le nœud depuis lequel tu envoies tes messages, communique lui avec l'appli par USB. Sa ligne de commande se trouve dans l'appli MeshCore, version 1.50 ou plus récente.
