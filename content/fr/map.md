---
title: Cartes de couverture
layout: map
lead: Vois jusqu'où porte le maillage, où se trouvent les nœuds et quel chemin suivent les messages. Des communautés partout en Europe tiennent ces cartes à jour.
description: Cartes MeshCore en direct, cartes de couverture et analyseurs de paquets pour l'Europe et pour chaque pays.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '351071aa'
  seeded: '2026-10-31'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['351071aa']
  blocks: ['dd5f039e', '9d4a2ad8', '70c417f2', '9fef7e16']
---

Un nœud apparaît sur ces cartes quand son propriétaire le publie, ou quand un
*observateur* le capte : c'est un nœud qui relaie ce qu'il entend via MQTT. Aucune carte
n'est donc complète. Les analyseurs montrent le trafic que reçoivent leurs observateurs : paquets,
routes et activité des canaux. Les messages directs restent chiffrés. Aucun analyseur
n'en affiche donc le contenu.

Un nœud figure sur une carte à l'endroit où son propriétaire l'a placé. Cette position peut être fausse ou
périmée. Un message en diffusion emprunte plusieurs chemins à la fois. La route affichée sur une carte est le chemin
de la copie arrivée en premier. Les autres ne sont pas enregistrées.

Ces cartes ont besoin d'internet, le maillage non. [Pourquoi](/network/)

Tu fais tourner un répéteur, un nœud qui transmet les messages ? Indique sa position avec `set lat` et `set lon`, et les cartes
pourront le placer. Le [guide du répéteur](/repeater-guide/#config) t'explique comment faire.
