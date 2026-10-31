---
title: MQTT sur ton observateur
lead: Ton répéteur transmet ce qu'il entend au MeshCore Analyzer via Wi-Fi. Il continue de relayer les messages comme avant.
description: Transforme un répéteur ESP32 en observateur MeshCore avec le micrologiciel DMC observer. Flashe-le, règle le Wi-Fi et ton code d'aéroport, choisis les brokers et vérifie qu'il transmet bien au MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-31'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Un observateur est un nœud qui transmet aussi ce qu'il entend par MQTT, via
le Wi-Fi. Chaque observateur dévoile un peu plus du maillage sur le
[MeshCore Analyzer](https://meshcore-analyzer.eu/) et sur les
[cartes de couverture](/map/). Avec ce guide, tu transformes un répéteur (un
nœud qui relaie les messages) en observateur. Il continue de relayer. Les
rapports partent dans un seul sens : rien ne revient sur le maillage.

{{< callout type="warning" >}}
Ce guide porte sur le **micrologiciel DMC observer**, la version observateur
de [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), basée sur
MeshCore 1.18.0. Le MeshCore d'origine n'a pas de MQTT. Toutes les commandes
ci-dessous viennent du code source du micrologiciel, version `32dd8ad` du
19 octobre 2026.
{{< /callout >}}

## Ce qu'il te faut {#need}

- Une carte ESP32 avec Wi-Fi, comme une Heltec V3 ou V4, une LilyGo T3S3 ou
  une Xiao S3. La [release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  liste toutes les cartes. Les cartes nRF52 comme la RAK4631 n'ont pas de Wi-Fi.
- Un réseau Wi-Fi 2.4 GHz à l'endroit où se trouve la carte.
- Un câble USB de données, et Chrome, Edge ou Opera sur ton ordinateur.
- Le code d'aéroport le plus proche de ton nœud, 3 lettres comme `AMS` ou
  `BRU`. Grâce à lui, les brokers (les serveurs qui reçoivent tes rapports)
  savent dans quelle zone se trouve ton observateur.

Pas de Wi-Fi près de ton répéteur, mais un ordinateur à côté ?
[Crée plutôt une configuration de passerelle](/guides/mctomqtt/).

## Flasher le micrologiciel {#flash}

Le [flasheur](/firmware/flasher/) de ce site ne propose que le MeshCore
d'origine. Tu trouves le micrologiciel observateur dans le flasheur de la
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/) :

1. Choisis ta carte, puis **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Choisis **Full flash** la première fois : tout le contenu de la carte est
   remplacé, table des partitions comprise. La mise à jour de l'application
   garde ce qui est en place et sert aux mises à jour suivantes.
3. Configure ton répéteur comme d'habitude : nom, préréglage radio et mot de
   passe admin, comme dans le [guide du répéteur](/repeater-guide/#config).

Ce micrologiciel est la version **dev**. Quand tu tapes `ota update`, il se
met à jour depuis le canal dev. Le canal stable propose encore la 1.17.1,
alors reste sur dev pour ce guide.

## Réglages {#settings}

Ouvre la [console série](/firmware/console/) de ce site et connecte ta carte.
Remplace le réseau Wi-Fi, le mot de passe et le code d'aéroport par les tiens,
puis colle ces lignes une par une :

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Après le redémarrage, la carte rejoint ton Wi-Fi et règle son horloge via
internet. Les brokers ont besoin de cette horloge pour vérifier l'identité de
ton observateur. Sans code d'aéroport, la carte ne transmet rien.

Tu préfères cliquer plutôt que taper ? `start webconfig` ouvre une page de
réglages sur la carte, à l'adresse qu'affiche la console. Connecte-toi avec
ton mot de passe admin.

## Emplacements de broker {#brokers}

Un emplacement contient un broker. Au départ, le micrologiciel remplit ces
emplacements :

| Emplacement | Broker | Géré par |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Une carte sans mémoire supplémentaire (PSRAM), comme la Heltec V3, a
3 emplacements. Elle se connecte à 2 d'entre eux en même temps. L'Analyzer de
l'emplacement 3 ne se connecte donc jamais. Déplace-le vers l'emplacement 1 :

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Une carte avec PSRAM, comme la Heltec V4, a 6 emplacements et se connecte à
5 en même temps. Tu n'as rien à changer.

Ton nœud se connecte à chaque broker avec sa propre clé, donc tu n'as pas
besoin de compte. `get mqtt.presets` liste les autres brokers communautaires
que le micrologiciel connaît.

### Ton propre broker {#own}

Place ton propre broker dans un emplacement libre. Indique son adresse, son
port, ton nom d'utilisateur et ton mot de passe. Sur une carte avec PSRAM,
l'emplacement 4 est libre :

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Sur une carte sans PSRAM, utilise plutôt l'emplacement 2 : remplace `mqtt4`
par `mqtt2`. Ton broker prend alors la place de `dutchmeshcore-2`.

Avec le port `8883`, la connexion est chiffrée (TLS). Avec le port `443`,
elle est chiffrée via une connexion web (websocket). Tout autre port donne une
connexion non chiffrée. Tu peux aussi indiquer l'adresse complète, comme
`wss://mqtt.example.org:9002/mqtt`. Dans ce cas, la règle des ports ne
s'applique pas.

## Vérifier que ça marche {#check}

Tape `get mqtt.status`. Chaque emplacement affiche son état :

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok` : connecté.
- `wait` : il manque un réglage à l'emplacement, comme le code d'aéroport.
- `disc` : pas encore connecté. Vérifie ton Wi-Fi avec `get wifi.status`.
- `fail` : l'emplacement a échoué 7 fois de suite, sur environ 20 minutes. Il
  réessaie maintenant une fois toutes les 30 minutes. Vérifie l'adresse et
  les identifiants du broker.
- `inactive` : la carte n'a pas de place pour cet emplacement. Consulte
  [Emplacements de broker](#brokers).

Cherche ensuite le nom de ton répéteur sur la
[page des observateurs de l'Analyzer](https://meshcore-analyzer.eu/#observers).
Il y apparaît en 5 minutes maximum, avec ce qu'il a entendu.
