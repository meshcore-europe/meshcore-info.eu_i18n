---
title: Filtre de paquets
lead: 'Empêche ton répéteur de relayer du bruit : des diffusions venues de loin, un bot qui ne s’arrête jamais, un canal trop bavard. Teste d’abord un réglage, puis active-le.'
description: 'Le filtre de paquets du micrologiciel de répéteur DMC : ce qu’il rejette, des réglages prêts à l’emploi pour un répéteur normal et un répéteur chargé, chaque commande de filtre avec sa valeur par défaut, et comment voir ce qu’il a rejeté.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-10-31'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Un répéteur (un nœud qui relaie les messages) répète tout ce qu’il entend.
Sur un maillage chargé, cela inclut du trafic inutile. Un bot publie toutes les minutes.
Un nœud renvoie son annonce à quelques minutes d’intervalle. L’annonce est le
signal qui permet aux autres de le trouver. Des messages arrivent après avoir
traversé la moitié du pays. Chaque répétition prend du temps d’antenne à tous
ceux qui t’entourent. Avec le filtre de paquets, ton répéteur rejette ce trafic
au lieu de le relayer. Pour savoir d’abord ce qui inonde ton maillage, et ce
qui aide en plus du filtre, consulte
[Rendre le maillage résilient](/guides/resilient/).

{{< callout type="warning" >}}
Le filtre de paquets fait partie du **micrologiciel de répéteur DMC**, la
version répéteur de [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore).
MeshCore d’origine n’a pas de filtre de paquets. Il propose `region denyf *` et
`set flood.max.unscoped`, décrits sur la page [Commandes CLI](/guides/cli/). Ce
guide suit la version de développement 1.18.0 `ecfb2d4` du 19 octobre 2026. La
version stable 1.17.1 n’a que les filtres de sauts, de débit, de canal, de
hachage et de paquets malformés. Elle n’a pas non plus de mode dry-run.
{{< /callout >}}

## Ce que fait le filtre {#what}

Le filtre examine seulement les paquets que ton répéteur relaie par diffusion
(il les envoie à tous les nœuds à portée). Il ne touche jamais ce que ton
répéteur envoie lui-même. Il ne touche pas non plus les paquets qui suivent une
route connue vers un seul nœud. Les messages directs et les requêtes échangés
avec tes propres contacts passent aussi. Le filtre peut rejeter :

- les paquets qui ont déjà traversé autant de répéteurs (sauts) que tu le
  permets, par type de paquet ;
- les paquets d’un type au-delà du nombre que tu autorises par minute ;
- l’annonce d’un nœud qui s’est déjà annoncé dans les dernières heures ;
- les messages sur un canal que tu bloques ;
- tout ce qui est passé par un répéteur que tu bloques ;
- les messages de groupe d’un expéditeur ou contenant un mot, tous ou
  seulement une partie ;
- les messages de groupe corrompus, ou plus anciens que tu ne le permets.

Le filtre est **désactivé** tant que tu ne l’actives pas. Tu le règles avec des
commandes. Tape-les via USB dans la [console série](/firmware/console/) de ce
site. Tu peux aussi les envoyer depuis l’app MeshCore, comme dans le
[guide du répéteur](/repeater-guide/#config).

## Obtenir le micrologiciel {#firmware}

Flashe **DutchMeshCore Repeater** avec l’outil de flashage de la
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Le micrologiciel
d’observateur de [MQTT sur ton observateur](/guides/mqtt/) a le même filtre.

## Teste d’abord {#dryrun}

En mode dry-run, le filtre compte chaque paquet qu’il rejetterait, mais le
relaie quand même. Tu ajustes ainsi un réglage avant qu’il ne rejette quoi
que ce soit :

```text
filter on
filter dryrun on
```

Tant que le dry-run est actif, la ligne d’état de `filter` se termine par
`(dry-run)`. Les compteurs indiquent ce que le filtre aurait rejeté. Laisse-le
tourner une journée, puis regarde-les (voir [Ce qu’il a rejeté](#stats)). Quand
les chiffres te semblent corrects, applique le filtre pour de bon :

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

Les messages de groupe passent jusqu’à 20 par minute, les messages directs
jusqu’à 5 par minute. Les messages de groupe corrompus sont rejetés. La
configuration normale du micrologiciel autorise 20 messages directs par minute.
Cette page retient les 5 que le micrologiciel conseille depuis une diffusion
massive de messages directs en juillet 2026.

### Un répéteur chargé {#busy}

Pour un répéteur sur un point haut qui entend toute une région, ou un répéteur
inondé :

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

Cette configuration divise par deux les messages de groupe et les annonces. Elle
laisse passer l’annonce de chaque nœud une fois par jour. Elle rejette les
messages qui ont déjà traversé 16 répéteurs. Après un redémarrage, chaque nœud
fait passer une annonce. La documentation du micrologiciel ajoute aussi
`filter hash 2` ici. Cette page l’omet (voir [Tous les réglages](#settings)
pour la raison).

### Bloquer un canal bavard {#channel}

```text
filter channel add #bot
```

Ton répéteur entend toujours le canal. Il ne le relaie plus vers les autres
répéteurs et les companions (les nœuds depuis lesquels les gens envoient leurs
messages). Jusqu’à 16 canaux.

### Ralentir un expéditeur {#sender}

Un bot publie trop souvent sur un canal que tu veux garder :

```text
filter watch add #test
filter sender add Bob 60
```

Les messages de Bob sur le canal Public et sur `#test` passent maintenant une
fois par minute. Le reste est rejeté. Le filtre compare le nom dans le message.
Un expéditeur qui change de nom lui échappe donc.

### Bloquer un répéteur en amont {#path}

Quand le trafic inutile arrive par un seul répéteur, bloque son préfixe : le début de
son identifiant, en hexadécimal (hex). Il te faut la version de développement
1.18. La 1.17.1 n’a pas de filtre de chemin.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` affiche les préfixes que tu bloques, `filter stats path` ce
que chacun a rejeté. `filter path remove a1b2` le débloque.
Un préfixe court comme `a1` bloque aussi tous les autres répéteurs dont
l’identifiant commence par `a1`. Utilise le préfixe le plus long possible.
Jusqu’à 8 préfixes.

## Tous les réglages {#settings}

Les types de paquets se désignent par un numéro. Sur le répéteur,
`filter types` affiche les mêmes numéros avec les noms du micrologiciel, comme
`TXT_MSG` et `GRP_TXT` :

| Numéro | Type | Numéro | Type |
| --- | --- | --- | --- |
| `00` | requête | `06` | données de groupe |
| `01` | réponse | `07` | requête anonyme |
| `02` | message direct | `08` | chemin |
| `03` | accusé de réception | `09` | trace |
| `04` | annonce | `10` | multipart |
| `05` | message de groupe | `11` | contrôle |

| Commande | Ce qu’elle fait | Valeur initiale |
| --- | --- | --- |
| `filter on` / `filter off` | Active ou désactive le filtre. | désactivé |
| `filter dryrun on` / `off` | Compte les rejets mais relaie quand même tout. | désactivé |
| `filter hops <type> <max>` | Rejette un type qui a déjà traversé ce nombre de répéteurs, de 0 à 64. | 32 pour les messages de groupe, 8 pour le reste |
| `filter rate <type> <limit> <secs> [soft]` | Laisse passer au plus `limit` paquets d’un type par période de `secs`. Avec `soft`, le passage diminue progressivement de `soft` à `limit`. `0` désactive la limite. | 20 par 60 s pour les messages directs et de groupe, 10 pour les annonces, 5 pour le reste |
| `filter advert <hours>` | Laisse passer l’annonce de chaque nœud une fois par période de ce nombre d’heures, jusqu’à 720. | 0 (désactivé) |
| `filter channel add <#name>` | Arrête de relayer un canal. | aucun |
| `filter path add <hex>` | Rejette tout ce qui est passé par un répéteur avec ce préfixe, de 2 à 8 chiffres hex. | aucun |
| `filter sender add <name> [secs] [prob]` | Rejette les messages de groupe d’un expéditeur, sur Public et les canaux surveillés. `Bot*` correspond à tous les noms qui commencent par Bot. | aucun |
| `filter text add <word> [secs] [prob]` | Rejette les messages de groupe qui contiennent un mot, sur Public et les canaux surveillés. `^word` ne correspond qu’en début de message. | aucun |
| `filter watch add <#name>` | Permet aussi aux règles d’expéditeur et de texte de lire ce canal, jusqu’à 4. Public est toujours lu. | Public |
| `filter malformed on` / `off` | Rejette les messages Public vides, corrompus ou dont la date s’écarte de plus d’une semaine (la vérification de date attend que l’horloge soit réglée). | désactivé |
| `filter age <minutes>` / `off` | Rejette les messages de groupe plus anciens que cette durée, sur Public et les canaux surveillés, de 1 à 10080. | désactivé |
| `filter hash <bytes>` | Rejette les paquets dont l’identifiant de chemin est plus court que cette valeur, de 1 à 3. | 1 |
| `filter reset` | Remet chaque réglage à sa valeur par défaut. | |

Chaque `add` a un `remove` et un `list`, par exemple `filter channel remove #bot`.
Dans les règles d’expéditeur et de texte, `secs` laisse passer un message par
période de ce nombre de secondes. `prob` applique la règle à cette part seulement des
correspondances, de 1 à 100. Jusqu’à 8 règles d’expéditeur et 8 règles de
texte. Les noms et les mots sont sensibles à la casse. Un nom compte au plus
15 caractères, un mot au plus 23.

Deux réglages rejettent plus que tu ne t’y attends peut-être :

- `filter hash 2` rejette presque tout le trafic. Par défaut, les nœuds envoient
  des identifiants de chemin de 1 octet.
- `filter age` se fie à l’horloge de ton répéteur. Règle-la avec `clock sync`
  depuis l’app, vérifie-la avec `clock`, et commence large : `filter age 60`.

Chaque réglage est conservé après un redémarrage.

## Ce qu’il a rejeté {#stats}

`filter` affiche les totaux par motif :

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` affiche le détail d’un réglage. Les thèmes sont
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` et `age`. `filter stats top` affiche le premier octet des identifiants
des nœuds à l’origine du plus grand nombre de rejets. Beaucoup de nœuds
partagent cet octet.
`filter stats air` affiche le temps d’antenne que ton répéteur a économisé en
ne relayant pas ces paquets.

Les compteurs repartent de 0 après un redémarrage et après `clear stats`.
