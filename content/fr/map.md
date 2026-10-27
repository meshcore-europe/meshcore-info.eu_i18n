---
title: Cartes de couverture
layout: map
lead: Vois jusqu'où s'étend le maillage, où se trouvent les nœuds et comment circulent les messages. Des communautés partout en Europe gèrent ces cartes.
description: Cartes MeshCore en direct, cartes de couverture et analyseurs de paquets pour l'Europe et chaque pays.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '550066cc'
  seeded: '2026-10-26'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['550066cc']
---

Un nœud apparaît sur ces cartes quand son propriétaire le publie, ou quand
un *observateur* le capte : un nœud qui transmet via MQTT ce qu'il entend.
Aucune carte n'est donc complète. Les analyseurs montrent le trafic que
reçoivent leurs observateurs : paquets, routes et activité des canaux. Les
messages directs restent chiffrés, donc aucun analyseur n'en révèle le
contenu.

Ces cartes ont besoin d'internet, le maillage non. [Pourquoi](/network/)

Tu fais tourner un répéteur, un nœud qui relaie les messages ? Définis sa position avec `set lat` et `set lon`, et les cartes
pourront le placer. Le [guide du répéteur](/repeater-guide/#config) explique comment.
