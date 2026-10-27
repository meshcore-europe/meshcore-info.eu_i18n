---
title: Filtre de paquets
lead: 'Empêche ton répéteur de relayer les déchets : diffusions venues de loin, un bot qui ne s''arrête jamais, un canal bruyant. Teste d''abord un réglage, puis active-le.'
description: 'Le filtre de paquets du micrologiciel répéteur DMC : ce qu''il rejette, des réglages prêts à l''emploi pour un répéteur normal et un répéteur chargé, chaque commande de filtre avec sa valeur par défaut, et comment voir ce qu''il a rejeté.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '2bf23d24'
  seeded: '2026-10-26'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['0625daa2', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', 'ffc3f3a0', '3fa1bb28', '09511608']
---

Un répéteur (un nœud qui relaie les messages) répète tout ce qu'il entend.
Sur un maillage chargé, cela inclut des déchets. Un bot publie toutes les
minutes. Un nœud envoie son annonce, le signal qui permet aux autres de le
trouver, toutes les quelques minutes. Des messages arrivent après avoir
traversé la moitié du pays. Chaque répétition prend du temps d'antenne à tout
le monde autour de toi. Le filtre de paquets permet à ton répéteur de rejeter
ce trafic au lieu de le relayer.

{{< callout type="warning" >}}
Le filtre de paquets fait partie du **micrologiciel répéteur DMC**, la
version répéteur de [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore).
Le MeshCore d'origine n'a pas de filtre de paquets ; il propose
`region denyf *` et `set flood.max.unscoped`, décrits sur la page
[Commandes CLI](/guides/cli/). Ce guide suit la version de développement
1.18.0 `ecfb2d4` du 19 octobre 2026. La version stable 1.17.1 n'a que les
filtres de sauts, de débit, de canal, de hachage et de messages corrompus.
Elle n'a pas non plus de mode test.
{{< /callout >}}

## Ce que fait le filtre {#what}

Le filtre ne regarde que les paquets que ton répéteur relaie par diffusion
(envoi à tous les nœuds à portée). Il ne touche jamais à ce que ton répéteur
envoie lui-même, ni aux paquets qui suivent une route connue vers un nœud.
Les messages directs et les requêtes vers et depuis tes propres contacts
passent aussi. Il peut rejeter :

- les paquets qui ont déjà traversé autant de répéteurs (sauts) que tu
  autorises, par type de paquet ;
- les paquets d'un type au-delà du nombre que tu autorises par minute ;
- une annonce d'un nœud qui s'est déjà annoncé ces dernières heures ;
- les messages sur un canal que tu bloques ;
- tout ce qui est passé par un répéteur que tu bloques ;
- les messages de groupe d'un expéditeur ou contenant un mot, en totalité ou
  en partie ;
- les messages de groupe corrompus, ou plus anciens que ce que tu autorises.

Le filtre est **désactivé** tant que tu ne l'actives pas. Tu le règles avec
des commandes. Tape-les par USB dans la [console série](/firmware/console/)
de ce site. Ou envoie-les depuis l'application MeshCore, comme dans le
[guide du répéteur](/repeater-guide/#config).

## Obtenir le micrologiciel {#firmware}

Flashe **DutchMeshCore Repeater** depuis l'outil de flashage de la
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Le micrologiciel
observateur de [MQTT sur ton observateur](/guides/mqtt/) a le même filtre.

## Teste d'abord {#dryrun}

En mode test, le filtre compte chaque paquet qu'il rejetterait, mais le
relaie quand même. Calibre ainsi un réglage avant qu'il ne rejette quoi que
ce soit :

```text
filter on
filter dryrun on
```

Tant que le mode test est actif, la ligne d'état de `filter` se termine par
`(dry-run)`. Les compteurs indiquent ce qu'il aurait rejeté. Laisse-le
tourner une journée, puis regarde-les (voir [Ce qu'il a rejeté](#stats)).
Quand les chiffres te semblent bons, applique-le :

```text
filter dryrun off
```

## Configurations recommandées {#configs}

### Un répéteur normal {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Les messages de groupe passent jusqu'à 20 par minute, les messages directs
jusqu'à 5 par minute, et les messages de groupe corrompus sont rejetés. La
configuration normale du micrologiciel lui-même autorise 20 messages directs
par minute. Cette page retient les 5 qu'il conseille depuis une vague de
messages directs en juillet 2026.

### Un répéteur chargé {#busy}

Pour un répéteur sur un point haut qui entend toute une région, ou un
répéteur inondé :

```text
filter on
filter malformed on
filter rate 05 10 60
filter rate 02 5 60
filter rate 04 5 60
filter advert 24
filter hops 05 16
filter hops 02 16
filter hops 04 8
```

Cela divise par deux les messages de groupe et les annonces, et laisse passer
l'annonce de chaque nœud une fois par jour. Les messages qui ont déjà
traversé 16 répéteurs sont rejetés. Après un redémarrage, chaque nœud fait
passer une annonce. La documentation du micrologiciel ajoute ici
`filter hash 2` ; cette page l'omet (voir [Chaque réglage](#settings) pour la
raison).

### Bloquer un canal bruyant {#channel}

```text
filter channel add #bot
```

Ton répéteur entend toujours le canal. Il ne le relaie plus aux autres
répéteurs ni aux compagnons (les nœuds depuis lesquels les gens envoient
leurs messages). Jusqu'à 16 canaux.

### Ralentir un expéditeur {#sender}

Un bot qui publie trop souvent sur un canal que tu veux garder :

```text
filter watch add #test
filter sender add Bob 60
```

Les messages de Bob sur le canal Public et sur `#test` passent désormais une
fois par minute ; le reste est rejeté. Le filtre compare le nom contenu dans
le message, donc un expéditeur qui se renomme passe à travers.

### Bloquer un répéteur en amont {#path}

Quand les déchets arrivent par un seul répéteur, bloque son préfixe : le
début de son identifiant, en hexadécimal (hex).

```text
filter path add a1b2
```

Un préfixe court comme `a1` bloque aussi tous les autres répéteurs dont
l'identifiant commence par `a1`. Utilise le préfixe le plus long possible.
Jusqu'à 8 préfixes.

## Chaque réglage {#settings}

Les types de paquets sont désignés par un numéro. Sur le répéteur,
`filter types` affiche les mêmes numéros avec les noms du micrologiciel,
comme `TXT_MSG` et `GRP_TXT` :

| Numéro | Type | Numéro | Type |
| --- | --- | --- | --- |
| `00` | requête | `06` | données de groupe |
| `01` | réponse | `07` | requête anonyme |
| `02` | message direct | `08` | chemin |
| `03` | accusé de réception | `09` | trace |
| `04` | annonce | `10` | multipart |
| `05` | message de groupe | `11` | contrôle |

| Commande | Ce qu'elle fait | Valeur de départ |
| --- | --- | --- |
| `filter on` / `filter off` | Active ou désactive le filtre. | off |
| `filter dryrun on` / `off` | Compte les rejets mais relaie quand même tout. | off |
| `filter hops <type> <max>` | Rejette un type qui a déjà traversé ce nombre de répéteurs, 0 à 64. | 32 pour les messages de groupe, 8 pour le reste |
| `filter rate <type> <limit> <secs> [soft]` | Laisse passer au plus `limit` paquets d'un type par `secs`. Avec `soft`, le passage décroît progressivement de `soft` à `limit`. `0` désactive la limite. | 20 par 60 s pour les messages directs et de groupe, 10 pour les annonces, 5 pour le reste |
| `filter advert <hours>` | Laisse passer l'annonce de chaque nœud une fois par ce nombre d'heures, jusqu'à 720. | 0 (off) |
| `filter channel add <#name>` | Cesse de relayer un canal. | aucun |
| `filter path add <hex>` | Rejette tout ce qui est passé par un répéteur avec ce préfixe, 2 à 8 chiffres hex. | aucun |
| `filter sender add <name> [secs] [prob]` | Rejette les messages de groupe d'un expéditeur, sur Public et les canaux surveillés. `Bot*` correspond à tout nom qui commence par Bot. | aucun |
| `filter text add <word> [secs] [prob]` | Rejette les messages de groupe contenant un mot, sur Public et les canaux surveillés. `^word` ne correspond qu'en début de message. | aucun |
| `filter watch add <#name>` | Fait lire ce canal aussi par les règles d'expéditeur et de texte, jusqu'à 4. Public est toujours lu. | Public |
| `filter malformed on` / `off` | Rejette les messages Public vides, corrompus ou datés avec plus d'une semaine d'écart (le contrôle de date attend que l'horloge soit réglée). | off |
| `filter age <minutes>` / `off` | Rejette les messages de groupe plus anciens que cette durée, sur Public et les canaux surveillés, 1 à 10080. | off |
| `filter hash <bytes>` | Rejette les paquets dont l'identifiant de chemin est plus court que cela, 1 à 3. | 1 |
| `filter reset` | Remet chaque réglage à sa valeur par défaut. | |

Chaque `add` a son `remove` et son `list`, comme `filter channel remove #bot`.
Dans les règles d'expéditeur et de texte, `secs` laisse passer un message
par ce nombre de secondes. `prob` n'applique la règle qu'à cette part des
correspondances, 1 à 100. Jusqu'à 8 règles d'expéditeur et 8 règles de
texte. Les noms et les mots distinguent majuscules et minuscules ; un nom
fait jusqu'à 15 caractères, un mot jusqu'à 23.

Deux réglages rejettent plus que tu ne le penses :

- `filter hash 2` rejette presque tout le trafic. Les nœuds envoient par
  défaut des identifiants de chemin de 1 octet.
- `filter age` se fie à l'horloge de ton répéteur. Règle-la avec `clock sync`
  depuis l'application, vérifie-la avec `clock`, et commence large :
  `filter age 60`.

Chaque réglage est conservé après un redémarrage.

## Ce qu'il a rejeté {#stats}

`filter` affiche les totaux par motif :

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` affiche le détail d'un réglage. Les sujets sont
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` et `age`. `filter stats top` affiche le premier octet des identifiants
de nœud à l'origine du plus grand nombre de rejets, une piste plutôt qu'une
preuve. `filter stats air` affiche le temps d'antenne que ton répéteur a
économisé en ne relayant pas ces paquets.

Les compteurs repartent de 0 après un redémarrage et après `clear stats`.
