---
title: MQTT sur ton observateur
lead: Laisse ton répéteur signaler ce qu'il entend au MeshCore Analyzer via le Wi-Fi. Il continue à relayer les messages comme avant.
description: Transforme un répéteur ESP32 en observateur MeshCore avec le micrologiciel observateur DMC. Flashe-le, règle le Wi-Fi et ton code d'aéroport, choisis les brokers et vérifie qu'il envoie ses rapports au MeshCore Analyzer.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-26'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
---

Un observateur est un nœud qui signale aussi ce qu'il entend via MQTT, par
le Wi-Fi. Chaque observateur montre un peu plus du maillage sur le
[MeshCore Analyzer](https://meshcore-analyzer.eu/) et sur les
[cartes de couverture](/map/). Ce guide transforme un répéteur (un nœud qui
relaie les messages) en observateur. Il continue à répéter, et le rapport ne
va que dans un sens : rien ne revient sur le maillage.

{{< callout type="warning" >}}
Ce guide concerne le **micrologiciel observateur DMC**, la version observateur de
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), basée sur
MeshCore 1.18.0. Le MeshCore d'origine n'a pas de MQTT. Chaque commande ci-dessous
vient du code source du micrologiciel, build `32dd8ad` du 19 octobre 2026.
{{< /callout >}}

## Ce qu'il te faut {#need}

- Une carte ESP32 avec Wi-Fi, comme une Heltec V3 ou V4, une LilyGo T3S3 ou une
  Xiao S3. La [release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  liste toutes les cartes. Les cartes nRF52 comme la RAK4631 n'ont pas de Wi-Fi.
- Un réseau Wi-Fi 2.4 GHz à l'endroit où se trouve la carte.
- Un câble USB de données, et Chrome, Edge ou Opera sur ton ordinateur.
- Le code d'aéroport le plus proche de ton nœud, 3 lettres comme `AMS` ou `BRU`.
  Il indique aux brokers (les serveurs qui reçoivent tes rapports) dans quelle
  zone se trouve ton observateur.

Pas de Wi-Fi à l'endroit où se trouve ton répéteur, mais un ordinateur à côté ?
[Construis plutôt une config de passerelle](/guides/mctomqtt/).

## Flasher le micrologiciel {#flash}

Le [flasheur](/firmware/flasher/) de ce site ne propose que le MeshCore d'origine.
Le micrologiciel observateur vient du flasheur de la
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/) :

1. Choisis ta carte, puis **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Choisis **Full flash** la première fois : cela remplace tout ce qui est sur
   la carte, y compris la table des partitions. L'app update garde ce qui est
   déjà là et sert aux mises à jour suivantes.
3. Configure ton répéteur comme d'habitude : nom, préréglage radio et mot de
   passe admin, comme dans le [guide du répéteur](/repeater-guide/#config).

Ce micrologiciel est la version **dev** et se met à jour depuis le canal dev
quand tu tapes `ota update`. Le canal stable est encore en 1.17.1, donc reste
sur dev pour ce guide.

## Réglages {#settings}

Ouvre la [console série](/firmware/console/) de ce site et connecte ta carte.
Renseigne ton propre réseau Wi-Fi, ton mot de passe et ton code d'aéroport, puis
colle ces lignes une par une :

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Après le redémarrage, la carte rejoint ton Wi-Fi et règle son horloge depuis
internet. Les brokers ont besoin de cette horloge pour vérifier qui est ton
observateur. Sans code d'aéroport, rien n'est signalé.

Tu préfères cliquer plutôt que taper ? `start webconfig` ouvre une page de
réglages sur la carte, à l'adresse que la console affiche. Connecte-toi avec
ton mot de passe admin.

## Emplacements de brokers {#brokers}

Un emplacement contient un broker. Au départ, le micrologiciel remplit ces
emplacements :

| Emplacement | Broker | Géré par |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Une carte sans mémoire supplémentaire (PSRAM), comme la Heltec V3, a 3
emplacements. Elle se connecte à 2 d'entre eux à la fois, donc l'Analyzer en
emplacement 3 ne se connecte jamais. Déplace-le vers l'emplacement 1 :

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Une carte avec PSRAM, comme la Heltec V4, a 6 emplacements et se connecte à 5
à la fois. Elle n'a besoin d'aucun changement.

Ton nœud se connecte à chaque broker avec sa propre clé, donc tu n'as pas
besoin de compte. `get mqtt.presets` liste les autres brokers communautaires que
le micrologiciel connaît.

### Ton propre broker {#own}

Mets ton propre broker dans un emplacement libre. Renseigne son adresse, son
port, son nom d'utilisateur et son mot de passe. Sur une carte avec PSRAM,
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

Le port `8883` se connecte en chiffré (TLS), le port `443` en chiffré via une
connexion web (websocket), et tout autre port en clair. Tu peux aussi donner
l'adresse complète, comme `wss://mqtt.example.org:9002/mqtt` ; dans ce cas la
règle du port ne s'applique pas.

## Vérifier que ça marche {#check}

Tape `get mqtt.status`. Chaque emplacement affiche son état :

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok` : connecté.
- `wait` : il manque un réglage à l'emplacement, comme le code d'aéroport.
- `disc` : pas encore connecté. Vérifie ton Wi-Fi avec `get wifi.status`.
- `fail` : l'emplacement a échoué 7 fois de suite, sur environ 20 minutes, et
  réessaie maintenant une fois toutes les 30 minutes. Vérifie l'adresse et les
  identifiants du broker.
- `inactive` : la carte n'a pas de place pour cet emplacement. Voir
  [Emplacements de brokers](#brokers).

Cherche ensuite le nom de ton répéteur sur la
[page des observateurs de l'Analyzer](https://meshcore-analyzer.eu/#observers).
Il apparaît en moins de 5 minutes, avec ce qu'il a entendu.
