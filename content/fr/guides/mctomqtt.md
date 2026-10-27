---
title: Créer une config de passerelle
lead: 'Envoie ce que ton répéteur entend vers n’importe quel broker MQTT : le tien, ou celui de l’Analyzer. Un ordinateur à côté du répéteur se charge de l’envoi.'
description: Fais tourner meshcoretomqtt sur un Raspberry Pi ou un autre ordinateur pour envoyer ce qu’un répéteur MeshCore entend, via USB, vers ton propre broker MQTT, le MeshCore Analyzer, ou les deux.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-26'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
---

Un répéteur est un nœud qui relaie les messages. Tu veux retrouver son trafic
sur un broker MQTT : le tien, pour un tableau de bord ou une base de données,
ou celui du [MeshCore Analyzer](https://meshcore-analyzer.eu/). Ou bien ton
répéteur n’a pas de Wi-Fi, mais un Raspberry Pi ou un serveur se trouve juste
à côté. [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), un outil
de la communauté, sert de passerelle : il envoie le trafic depuis cet
ordinateur. Ton répéteur continue de relayer, car la passerelle se contente de
lire ce qu’il journalise sur l’USB.

## Ce qu’il te faut {#need}

- Un répéteur compilé avec la journalisation des paquets (voir ci-dessous).
- Un Raspberry Pi Zero, 2, 3 ou 4, ou n’importe quel ordinateur Linux ou
  macOS, avec Python 3.11 ou plus récent.
- Un câble USB de données entre les deux.

Le micrologiciel répéteur standard du flasher ne journalise pas les paquets.
Compile toi-même le micrologiciel répéteur à partir des
[sources de MeshCore](https://github.com/meshcore-dev/MeshCore), en ajoutant
ce drapeau à la compilation de ta carte :

```text
-D MESH_PACKET_LOGGING=1
```

## Installation {#install}

Branche le répéteur sur l’ordinateur, puis lance le script d’installation de
meshcoretomqtt sur cet ordinateur :

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Le script installe la passerelle comme un service qui démarre avec
l’ordinateur, et te demande vers quels brokers envoyer. L’Analyzer n’est pas
dans cette liste ; tu l’ajoutes dans le fichier de config ci-dessous. Tes
propres réglages se trouvent dans `/etc/mctomqtt/config.d/99-user.toml` ;
une mise à jour n’écrase jamais ce fichier.

## Brokers {#brokers}

Chaque broker a son propre bloc `[[broker]]`, donc un seul répéteur peut en
alimenter plusieurs en même temps. Ton propre broker accepte un nom
d’utilisateur et un mot de passe, ou aucune identification
(`method = "none"`).
Le MeshCore Analyzer accepte à la place un jeton, que la clé de ton répéteur
signe :

- adresse `mqtt.meshcore-analyzer.eu`, port `443`, via un websocket sécurisé ;
- l’audience du jeton est cette même adresse.

## Ton fichier de config {#config}

Remplace le contenu de `/etc/mctomqtt/config.d/99-user.toml` par ceci.
Renseigne le code d’aéroport le plus proche de ton répéteur (`AMS`, par
exemple) et le port USB sur lequel ton répéteur est branché. Ajoute ensuite ton
propre broker. Supprime un bloc dont tu n’as pas besoin.

```toml
[general]
iata = "AMS"

[serial]
ports = ["/dev/ttyACM0"]

# Your own broker
[[broker]]
name = "my-broker"
enabled = true
server = "mqtt.example.org"
port = 1883

[broker.auth]
method = "password"
username = "my_username"
password = "my_password"

# The MeshCore Analyzer
[[broker]]
name = "meshcore-analyzer"
enabled = true
server = "mqtt.meshcore-analyzer.eu"
port = 443
transport = "websockets"

[broker.tls]
enabled = true
verify = true

[broker.auth]
method = "token"
audience = "mqtt.meshcore-analyzer.eu"
```

Redémarre le service après chaque modification (`sudo systemctl restart mctomqtt`
sous Linux). Ton répéteur apparaît alors sur l’Analyzer comme observateur, un
nœud qui envoie ce qu’il entend, sous le nom de ton répéteur. Le
[README de meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) décrit
tous les autres réglages.
