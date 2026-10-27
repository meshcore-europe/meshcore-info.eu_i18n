---
title: Een bridge-config maken
lead: 'Stuur wat je repeater hoort naar elke MQTT-broker: je eigen broker, of de Analyzer. Een computer naast de repeater doet het versturen.'
description: Draai meshcoretomqtt op een Raspberry Pi of een andere computer om wat een MeshCore-repeater hoort via USB naar je eigen MQTT-broker, de MeshCore Analyzer, of allebei te sturen.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-26'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
---

Een repeater is een node die berichten doorgeeft. Je wilt zijn verkeer op een
MQTT-broker hebben: je eigen broker voor een dashboard of een database, of die
van de [MeshCore Analyzer](https://meshcore-analyzer.eu/). Of je repeater heeft
zelf geen Wi-Fi, maar er staat een Raspberry Pi of een server naast.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), een tool van de
community, is de bridge: die stuurt het verkeer vanaf die computer. Je repeater
blijft gewoon doorgeven, want de bridge leest alleen wat hij via USB logt.

## Wat je nodig hebt {#need}

- Een repeater die gebouwd is met packet logging (zie hieronder).
- Een Raspberry Pi Zero, 2, 3 of 4, of een willekeurige Linux- of
  macOS-computer, met Python 3.11 of nieuwer.
- Een USB-datakabel tussen die twee.

De standaard repeater-firmware uit de flasher logt geen pakketten. Bouw de
repeater-firmware zelf uit de
[MeshCore-broncode](https://github.com/meshcore-dev/MeshCore) en voeg deze
vlag toe aan de build van je board:

```text
-D MESH_PACKET_LOGGING=1
```

## Installeren {#install}

Sluit de repeater aan op de computer en voer op die computer het
installatiescript van meshcoretomqtt uit:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Het script installeert de bridge als een service die meestart met de computer
en vraagt naar welke brokers je wilt sturen. De Analyzer staat niet in die
lijst; die voeg je hieronder toe in het configbestand. Je eigen instellingen
staan in `/etc/mctomqtt/config.d/99-user.toml`; een update overschrijft dat
bestand nooit.

## Brokers {#brokers}

Elke broker krijgt zijn eigen `[[broker]]`-blok, zodat één repeater meerdere
brokers tegelijk kan voeden. Je eigen broker werkt met een gebruikersnaam en
een wachtwoord, of helemaal zonder login (`method = "none"`).
De MeshCore Analyzer werkt in plaats daarvan met een token, dat de sleutel van
je repeater ondertekent:

- adres `mqtt.meshcore-analyzer.eu`, poort `443`, over een beveiligde websocket;
- de audience van het token is hetzelfde adres.

## Je configbestand {#config}

Vervang de inhoud van `/etc/mctomqtt/config.d/99-user.toml` door het volgende.
Vul de luchthavencode in die het dichtst bij je repeater ligt (bijvoorbeeld
`AMS`) en de USB-poort waar je repeater op zit. Voeg daarna je eigen broker
toe. Een blok dat je niet nodig hebt, laat je weg.

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

Herstart de service na een wijziging (`sudo systemctl restart mctomqtt` op
Linux). Je repeater verschijnt dan op de Analyzer als observer, een node die
uploadt wat hij hoort, onder de eigen naam van je repeater. In de
[README van meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) vind je
alle andere instellingen.
