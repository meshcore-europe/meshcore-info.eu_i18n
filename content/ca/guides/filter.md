---
title: Filtre de paquets
lead: 'Evita que el teu repetidor reenviï brossa: inundacions des de lluny, un bot que no para mai, un canal sorollós. Primer prova una configuració i després activa-la.'
description: 'El filtre de paquets del firmware de repetidor DMC: què descarta, configuracions a punt per a un repetidor normal i un de molt transitat, cada ordre del filtre amb el seu valor predeterminat i com veure què ha descartat.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-11-02'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Un repetidor (un node que reenvia missatges) repeteix tot el que sent.
En una malla amb molt de trànsit, això inclou brossa. Un bot publica cada minut. Un node
torna a enviar el seu anunci, la salutació que permet als altres trobar-lo, cada pocs minuts.
Arriben missatges que han travessat mig país. Cada repetició treu temps d'aire
a tothom que tens al voltant. Amb el filtre de paquets, el teu repetidor descarta
aquest trànsit en lloc de reenviar-lo. Per saber primer què inunda la teva malla,
i què més ajuda a part del filtre, consulta
[Fes la malla resistent](/guides/resilient/).

{{< callout type="warning" >}}
El filtre de paquets forma part del **firmware de repetidor DMC**, la compilació per a repetidors
de [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). El MeshCore
estàndard no té filtre de paquets: té `region denyf *` i
`set flood.max.unscoped`, a la pàgina d'[ordres de la CLI](/guides/cli/). Aquesta
guia segueix la compilació de desenvolupament 1.18.0 `ecfb2d4` del 19 d'octubre de 2026. La compilació estable
1.17.1 només té els filtres de salts, de ritme, de canal, de hash i de missatges malformats. Tampoc
té dry-run.
{{< /callout >}}

## Què fa el filtre {#what}

El filtre només mira els paquets que el teu repetidor reenvia per inundació (els envia
a tots els nodes a l'abast). No toca mai el que envia el teu repetidor,
ni els paquets que segueixen una ruta coneguda cap a un node. Els missatges directes i les
peticions que van als teus contactes o en vénen també passen. Pot descartar:

- els paquets que ja han passat per tants repetidors (salts) com permets, per
  tipus de paquet;
- els paquets d'un tipus que superin el nombre que permets per minut;
- l'anunci d'un node que ja s'ha anunciat durant les últimes hores;
- els missatges d'un canal que bloqueges;
- tot el que ha arribat a través d'un repetidor que bloqueges;
- els missatges de grup d'un remitent o amb una paraula, o només una part d'aquests;
- els missatges de grup malmesos o més antics del que permets.

El filtre està **desactivat** fins que l'activis. El configures amb ordres. Escriu-les
per USB a la [consola sèrie](/firmware/console/) d'aquest lloc web. També
pots enviar-les des de l'app de MeshCore, tal com explica la
[guia del repetidor](/repeater-guide/#config).

## Aconsegueix el firmware {#firmware}

Grava **DutchMeshCore Repeater** amb el flasher de la
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). El firmware d'observador
de [MQTT al teu observador](/guides/mqtt/) té el mateix filtre.

## Prova'l primer {#dryrun}

En mode dry-run, el filtre compta cada paquet que descartaria, però el reenvia
igualment. Així pots ajustar una configuració abans que descarti res:

```text
filter on
filter dryrun on
```

Mentre el dry-run està activat, la línia d'estat de `filter` acaba en `(dry-run)`. Els
comptadors indiquen què hauria descartat. Deixa'l funcionar un dia i després
consulta'ls (mira [Què ha descartat](#stats)). Quan els números et semblin correctes, fes-lo
efectiu:

```text
filter dryrun off
```

## Configuracions recomanades {#configs}

### Un repetidor normal {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Passen fins a 20 missatges de grup per minut i fins a 5 missatges directes per minut.
El filtre descarta els missatges de grup malmesos. La configuració normal del mateix firmware
permet 20 missatges directes per minut. Aquesta pàgina adopta els 5 que el firmware
aconsella des d'una inundació de missatges directes el juliol de 2026.

### Un repetidor amb molt de trànsit {#busy}

Per a un repetidor situat en un lloc alt que sent tota una regió, o per a un que pateix
una inundació:

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

Aquesta configuració redueix a la meitat els missatges de grup i els anuncis, i deixa passar l'anunci de cada node
un cop al dia. Descarta els missatges que ja han passat per 16 repetidors. Després d'un
reinici, cada node pot fer passar un anunci. La documentació del mateix firmware també hi posa
`filter hash 2`. Aquesta pàgina no ho fa (el motiu és a
[Totes les opcions](#settings)).

### Bloqueja un canal sorollós {#channel}

```text
filter channel add #bot
```

El teu repetidor continua sentint el canal. Ja no el reenvia a altres
repetidors ni a companions (els nodes des dels quals la gent envia missatges). Fins a 16 canals.

### Frena un remitent {#sender}

Un bot que publica massa sovint en un canal que vols conservar:

```text
filter watch add #test
filter sender add Bob 60
```

Ara els missatges d'en Bob al canal Public i a `#test` passen un cop per minut. El filtre
descarta la resta. El filtre es fixa en el nom que apareix al missatge, així que un remitent que
es canvia el nom se'l salta.

### Bloqueja un repetidor previ de la ruta {#path}

Quan la brossa entra a través d'un repetidor, bloqueja'n el prefix: la primera
part del seu ID, en hexadecimal (hex). Necessites la compilació de desenvolupament 1.18. La 1.17.1
no té filtre de rutes.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` mostra els prefixos que bloqueges, i `filter stats path` quant
ha descartat cadascun. `filter path remove a1b2` el torna a deixar passar.
Un prefix curt com `a1` també bloqueja tots els altres repetidors amb un ID que comenci
per `a1`. Fes servir el prefix més llarg que puguis. Fins a 8 prefixos.

## Totes les opcions {#settings}

Els tipus de paquet s'indiquen amb un número. Al repetidor, `filter types` mostra els mateixos
números amb els noms del firmware, com ara `TXT_MSG` i `GRP_TXT`:

| Número | Tipus | Número | Tipus |
| --- | --- | --- | --- |
| `00` | petició | `06` | dades de grup |
| `01` | resposta | `07` | petició anònima |
| `02` | missatge directe | `08` | ruta |
| `03` | confirmació | `09` | traça |
| `04` | anunci | `10` | multipart |
| `05` | missatge de grup | `11` | control |

| Ordre | Què fa | Valor inicial |
| --- | --- | --- |
| `filter on` / `filter off` | Activa o desactiva el filtre. | desactivat |
| `filter dryrun on` / `off` | Compta els descartaments, però ho reenvia tot igualment. | desactivat |
| `filter hops <type> <max>` | Descarta els paquets d'un tipus que ja han passat per aquest nombre de repetidors, de 0 a 64. | 32 per als missatges de grup, 8 per a la resta |
| `filter rate <type> <limit> <secs> [soft]` | Deixa passar com a màxim `limit` paquets d'un tipus per cada `secs`. Amb `soft`, el pas es redueix progressivament de `soft` a `limit`. `0` desactiva el límit. | 20 per 60 s per als missatges directes i de grup, 10 per als anuncis, 5 per a la resta |
| `filter advert <hours>` | Deixa passar l'anunci de cada node un cop cada tantes hores, fins a 720. | 0 (desactivat) |
| `filter channel add <#name>` | Deixa de reenviar un canal. | cap |
| `filter path add <hex>` | Descarta tot el que ha arribat a través d'un repetidor amb aquest prefix, de 2 a 8 dígits hexadecimals. | cap |
| `filter sender add <name> [secs] [prob]` | Descarta els missatges de grup d'un remitent, a Public i als canals vigilats. `Bot*` coincideix amb tots els noms que comencen per Bot. | cap |
| `filter text add <word> [secs] [prob]` | Descarta els missatges de grup que contenen una paraula, a Public i als canals vigilats. `^word` només coincideix a l'inici. | cap |
| `filter watch add <#name>` | Fa que les regles de remitent i de text també llegeixin aquest canal, fins a 4. Public sempre el llegeixen. | Public |
| `filter malformed on` / `off` | Descarta els missatges de Public buits, malmesos o amb una data desviada més d'una setmana (la comprovació de la data espera que el rellotge estigui configurat). | desactivat |
| `filter age <minutes>` / `off` | Descarta els missatges de grup més antics que aquest valor, a Public i als canals vigilats, d'1 a 10080. | desactivat |
| `filter hash <bytes>` | Descarta els paquets amb un ID de ruta més curt que aquest valor, d'1 a 3. | 1 |
| `filter reset` | Torna totes les opcions al valor predeterminat. | |

Cada `add` té un `remove` i un `list`, com ara `filter channel remove #bot`.
A les regles de remitent i de text, `secs` deixa passar un missatge cada tants segons.
`prob` aplica la regla només a aquest percentatge de les coincidències, d'1 a 100. Pots tenir fins a 8
regles de remitent i 8 de text. Els noms i les paraules distingeixen majúscules i minúscules. Un nom té fins a
15 caràcters, i una paraula, fins a 23.

Dues opcions descarten més del que potser esperes:

- `filter hash 2` descarta gairebé tot el trànsit. Els nodes envien ID de ruta d'1 byte
  de manera predeterminada.
- `filter age` confia en el rellotge del teu repetidor. Configura'l amb `clock sync` des de
  l'app, comprova'l amb `clock` i comença amb un marge ampli: `filter age 60`.

El repetidor conserva totes les opcions després d'un reinici.

## Què ha descartat {#stats}

`filter` mostra els totals per motiu:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` mostra el detall d'una opció. Els temes són
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` i `age`. `filter stats top` mostra el primer byte dels ID dels nodes
que causen més descartaments. Molts nodes comparteixen aquest byte.
`filter stats air` mostra el temps d'aire que el teu repetidor ha estalviat en no reenviar aquests
paquets.

Els comptadors tornen a començar de 0 després d'un reinici i després de `clear stats`.
