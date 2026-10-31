---
title: Een bridge-configuratie maken
lead: 'Stuur wat je repeater hoort naar elke MQTT-broker: je eigen broker of die van de Analyzer. Een computer naast de repeater verstuurt het.'
description: Draai meshcoretomqtt op een Raspberry Pi of een andere computer. Zo stuur je wat een MeshCore-repeater via USB hoort naar je eigen MQTT-broker, naar de MeshCore Analyzer of naar allebei.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-31'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Een repeater is een node die berichten doorgeeft. Je wilt het verkeer ervan op een MQTT-broker hebben: op je eigen broker voor een dashboard of een database, of op die van de [MeshCore Analyzer](https://meshcore-analyzer.eu/). Of je repeater heeft zelf geen Wi-Fi, maar er staat een Raspberry Pi of een server naast. [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), een tool uit de community, is de bridge: die verstuurt het verkeer vanaf die computer. Je repeater blijft doorgeven, want de bridge leest alleen wat de repeater via USB logt.

## Wat je nodig hebt {#need}

- Een repeater met packet logging in de build (zie hieronder).
- Een Raspberry Pi Zero, 2, 3 of 4, of een andere computer met Linux of macOS, met Python 3.11 of nieuwer.
- Een USB-datakabel tussen die twee.

De standaard repeater-firmware uit de flasher logt geen pakketten. Bouw de repeater-firmware daarom zelf vanuit de [MeshCore-broncode](https://github.com/meshcore-dev/MeshCore). Voeg deze vlag toe aan de build van je board:

```text
-D MESH_PACKET_LOGGING=1
```

## Installeren {#install}

Sluit de repeater aan op de computer. Draai daarna op die computer het installatiescript van meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Het script installeert de bridge als service die met de computer meestart. Het vraagt ook naar welke brokers het moet versturen. De Analyzer staat niet in die lijst. Die voeg je toe in het configuratiebestand hieronder. Je eigen instellingen staan in `/etc/mctomqtt/config.d/99-user.toml`. Een update overschrijft dat bestand nooit.

## Brokers {#brokers}

Elke broker krijgt een eigen `[[broker]]`-blok. Zo kan één repeater meerdere brokers tegelijk voeden. Voor je eigen broker gebruik je een gebruikersnaam en een wachtwoord, of helemaal geen login (`method = "none"`).
De MeshCore Analyzer werkt in plaats daarvan met een token, dat je repeater met zijn sleutel ondertekent:

- adres `mqtt.meshcore-analyzer.eu`, poort `443`, via een beveiligde websocket;
- de audience van het token is hetzelfde adres.

## Je configuratiebestand {#config}

Vervang de inhoud van `/etc/mctomqtt/config.d/99-user.toml` door de tekst hieronder. Vul de luchthavencode in die het dichtst bij je repeater ligt (bijvoorbeeld `AMS`). Vul ook de USB-poort in waarop je repeater zit. Voeg daarna je eigen broker toe. Een blok dat je niet nodig hebt, laat je weg.

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

Herstart de service na een wijziging (`sudo systemctl restart mctomqtt` op Linux). Je repeater verschijnt dan op de Analyzer als observer, een node die uploadt wat hij hoort. Hij staat daar onder de eigen naam van je repeater. Alle andere instellingen vind je in de [README van meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt).
