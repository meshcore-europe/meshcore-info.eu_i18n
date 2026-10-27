---
title: Commandes CLI
layout: cli
lead: Toutes les commandes de ton répéteur, serveur de salon, capteur ou compagnon, groupées selon ce que tu veux faire. Lis ce que chacune fait et sa valeur de départ, mets la tienne et copie-la.
description: 'Toutes les commandes du micrologiciel MeshCore 1.18.0 pour les répéteurs, serveurs de salon, capteurs et compagnons, groupées par tâche : ce qu''elles font, la valeur de départ du micrologiciel, et quels nœuds les possèdent.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-26'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
---

Ces commandes suivent le micrologiciel MeshCore 1.18.0, lues dans le code source du micrologiciel. Une commande ajoutée dans une version récente indique la version qu'elle demande. Un répéteur relaie les messages, un serveur de salon conserve les messages d'un groupe, un capteur transmet des mesures. Les serveurs de salon, les capteurs et les compagnons partagent beaucoup de commandes. Chaque commande indique quels nœuds la possèdent. « Quel nœud ? » montre seulement les commandes du tien.

Sur un répéteur, un serveur de salon ou un capteur, tu les tapes par USB depuis ton ordinateur, par exemple dans la [console série](/firmware/console/) de ce site. L'application MeshCore les envoie par le maillage. Le [guide du répéteur](/repeater-guide/#config) montre les deux méthodes.

Depuis la 1.18, un compagnon (le nœud depuis lequel tu envoies tes messages, appairé à ton téléphone ou à ton ordinateur portable, ou doté de son propre écran) a aussi une ligne de commande. Ouvre Command Line dans les réglages de l'application MeshCore, version 1.50 ou plus récente. Un contact avec la permission Remote CLI peut envoyer à ton compagnon les mêmes commandes par le maillage. Cela inclut les commandes WiFi et PIN.

La valeur de départ d'une commande est celle du répéteur. Un serveur de salon, un capteur ou un compagnon peut partir d'une autre valeur. Une commande que seul un compagnon possède montre la sienne.
