---
title: Commandes CLI
layout: cli
lead: Toutes les commandes de ton répéteur, room server, capteur ou companion, classées selon ce que tu veux faire. Lis ce que fait chaque commande et sa valeur de départ, saisis la tienne et copie-la.
description: 'Toutes les commandes du micrologiciel MeshCore 1.18.0 pour répéteurs, room servers, capteurs et companions, classées par tâche : ce que fait chaque commande, la valeur de départ du micrologiciel et les nœuds qui la proposent.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-31'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Ces commandes suivent le micrologiciel MeshCore 1.18.0. Nous les avons relevées dans le code source du
micrologiciel. Pour une commande ajoutée récemment, la page indique la version
nécessaire. Un répéteur relaie les messages, un room server conserve les publications
d'un groupe, un capteur transmet ses mesures. Les room servers, capteurs et
companions partagent beaucoup de commandes. Chaque commande indique les nœuds qui
la proposent. Avec « Quel nœud ? », tu n'affiches que les commandes du tien.

Sur un répéteur, un room server ou un capteur, tu les tapes depuis ton
ordinateur via USB, par exemple dans la [console série](/firmware/console/) de ce site. L'app MeshCore les envoie par le maillage. Le
[guide du répéteur](/repeater-guide/#config) montre les deux méthodes.

Depuis la 1.18, un companion (le nœud depuis lequel tu envoies tes messages, appairé avec ton téléphone ou ton ordinateur portable, ou
doté de son propre écran) a aussi une ligne
de commande. Ouvre Command Line dans les réglages de l'app MeshCore, version 1.50 ou
ultérieure. Un contact qui a l'autorisation Remote CLI peut envoyer ces
mêmes commandes à ton companion par le maillage. Cela comprend les commandes WiFi et PIN.

La valeur de départ d'une commande est celle du répéteur. Sur un room server, un capteur ou un
companion, elle peut être différente. Une commande réservée au companion indique sa propre valeur.
