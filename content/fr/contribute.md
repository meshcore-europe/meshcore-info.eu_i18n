---
title: Contribuer
lead: Ce guide est écrit, vérifié et traduit par des bénévoles. Voici comment aider, avec ou sans compte GitHub.
description: Ajoute ta communauté, un appareil ou un projet, relis une traduction ou améliore un guide sur meshcore-info.eu.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-26'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
---

Tout le contenu de ce site se trouve dans un
[dépôt GitHub](https://github.com/meshcore-europe/meshcore-info.eu) public. Les petites
modifications passent par un formulaire sur GitHub (une issue). Tout ce qui est plus
important passe par une pull request : une proposition de modification des fichiers
qu'un mainteneur relit. Un mainteneur vérifie chaque modification avant sa mise en ligne.

Pas de compte GitHub ? Signale-le sur [Discord](https://discord.meshcore-info.eu/) : un
groupe manquant, une erreur factuelle ou une traduction qui sonne bizarrement. Un bénévole
prend le relais.

## Ajoute ta communauté {#community}

Tu animes un groupe MeshCore local ouvert à tous ? Remplis le
[formulaire communauté](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
avec le nom, la zone géographique et les liens publics. Une fois ajouté, ton groupe apparaît
sur la page [Groupes locaux](/community/) dans toutes les langues.

## Propose un appareil ou un projet {#device-project}

La [page des appareils](/devices/) reprend les caractéristiques de la documentation des
fabricants et ne renvoie jamais vers des boutiques. Propose du matériel avec le
[formulaire appareil](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Tu as créé une application, un outil, une passerelle ou un design matériel pour MeshCore
avec un code source public ? Ajoute-le avec le
[formulaire projet](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Relis une traduction {#translate}

Les pages dans les autres langues commencent comme des traductions automatiques et
l'indiquent en haut. Les traductions vivent dans leur propre dépôt,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), donc
tu n'as jamais besoin de toucher au code du site. Si tu maîtrises bien l'une des
langues, tu peux l'améliorer :

1. Ouvre la page et suis « Aide à améliorer cette traduction ». Le lien ouvre le
   fichier sur GitHub, où tu peux le modifier dans ton navigateur.
2. Corrige la formulation. Garde les liens, le code, les chiffres et les noms comme
   MeshCore exactement tels quels.
3. Dans le bloc `translation` en haut, remplace `status: ai` par
   `status: human`, puis propose la modification.

Tu as trouvé un mot faux mais tu n'as pas le temps de le corriger ? Signale-le avec le
[formulaire traduction](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Améliore un guide {#guides}

Les guides sont d'abord écrits en anglais, puis traduits à partir de là. Les corrections
et les nouveaux sujets sont bienvenus via le
[formulaire contenu](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
ou une pull request. Chaque fait a besoin d'une source : le micrologiciel MeshCore et sa
documentation, un régulateur radio ou un fabricant. Écris avec tes propres mots. Une
courte citation avec sa source convient.

Le [guide du contributeur](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
explique comment travailler sur le site depuis ton propre ordinateur.

## État des traductions {#coverage}

« Relue » signifie vérifiée
par une personne ; « Automatique » signifie traduite automatiquement et pas encore relue ;
« Obsolète » signifie que le texte anglais a changé après la traduction ;
« Manquante » signifie que la page n'a pas encore de traduction.

{{< coverage >}}

## Crédits {#credits}

Le site est construit avec [Astro](https://astro.build/). Il utilise les polices
IBM Plex Sans et IBM Plex Mono, sous licence SIL Open Font License. Les traductions
suivent les
conventions de [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) et
partagent ses glossaires MeshCore. MeshCore lui-même est développé sur
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Les textes et les traductions sont sous licence CC BY 4.0, le code sous licence
MIT.
