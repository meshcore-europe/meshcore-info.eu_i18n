---
title: Contribuer
lead: Des bénévoles rédigent, vérifient et traduisent ce guide. Voici comment tu peux aider, avec ou sans compte GitHub.
description: Ajoute ta communauté, un appareil ou un projet, relis une traduction ou améliore un guide sur meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-31'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Tout le contenu de ce site se trouve dans un
[dépôt GitHub](https://github.com/meshcore-europe/meshcore-info.eu) public. Pour les petites modifications, tu passes par un formulaire sur GitHub (une issue). Les changements plus importants passent par une pull request : une proposition de modification des fichiers, qu'un mainteneur examine. Un mainteneur vérifie chaque modification avant sa mise en ligne.

Pas de compte GitHub ? Écris-nous sur [Discord](https://discord.meshcore-info.eu/) : un groupe manquant, une information fausse ou une traduction qui sonne bizarrement. Un bénévole s'en charge ensuite.

## Ajouter ta communauté {#community}

Tu animes un groupe MeshCore local ouvert à tous ? Remplis le
[formulaire communauté](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
avec le nom, la zone et les liens publics. Une fois ajouté, ton groupe apparaît sur la page [Groupes locaux](/community/) dans toutes les langues.

## Proposer un appareil ou un projet {#device-project}

La [page des appareils](/devices/) reprend les caractéristiques de la documentation des fabricants. Elle ne renvoie jamais vers des boutiques. Pour proposer du matériel, utilise le
[formulaire appareil](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Tu as créé une application, un outil, une passerelle ou une conception matérielle pour MeshCore, avec un code source public ? Ajoute-le avec le
[formulaire projet](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Relire une traduction {#translate}

Les pages dans les autres langues sont d'abord traduites automatiquement. Un avertissement en haut de page l'indique. Les traductions se trouvent dans leur propre dépôt,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n). Tu n'as donc jamais besoin de toucher au code du site. Si tu maîtrises bien l'une des langues, tu peux l'améliorer :

1. Ouvre la page et clique sur « Help improve this translation ». Le fichier s'ouvre sur GitHub, et tu peux le modifier dans ton navigateur.
2. Corrige la formulation. Garde les liens, le code, les nombres et les noms comme MeshCore exactement tels quels.
3. Dans le bloc `translation` en haut, remplace `status: ai` par
   `status: human`, puis propose la modification.

Tu as repéré un mot erroné, mais tu n'as pas le temps de le corriger ? Signale-le avec le
[formulaire de traduction](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Améliorer un guide {#guides}

Les guides sont d'abord rédigés en anglais, puis traduits à partir de cette version. Les corrections et les nouveaux sujets sont les bienvenus, via le
[formulaire de contenu](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
ou une pull request. Chaque information doit avoir une source : le micrologiciel MeshCore et sa documentation, une autorité de régulation radio ou un fabricant. Écris avec tes propres mots. Une courte citation avec sa source est permise.

Le [guide du contributeur](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
explique comment travailler sur le site depuis ton propre ordinateur.

## État des traductions {#coverage}

« Reviewed » signifie qu'une personne a vérifié la traduction. « Machine » signifie que la page est traduite automatiquement et pas encore relue. « Outdated » signifie que le texte anglais a changé après la traduction. « Missing » signifie que la page n'a pas encore de traduction.

{{< coverage >}}

## Crédits {#credits}

Le site est construit avec [Astro](https://astro.build/). Il utilise les polices IBM Plex Sans et IBM Plex Mono, sous licence SIL Open Font License. Les traductions suivent les conventions de [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) et partagent ses glossaires MeshCore. MeshCore lui-même est développé sur
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Les textes et les traductions sont sous licence CC BY 4.0, le code sous licence MIT.
