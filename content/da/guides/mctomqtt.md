---
title: Byg en bridge-konfiguration
lead: 'Send det, din repeater hører, til en hvilken som helst MQTT-broker: din egen eller Analyzerens. En computer ved siden af repeateren står for afsendelsen.'
description: Kør meshcoretomqtt på en Raspberry Pi eller en anden computer for at sende det, en MeshCore-repeater hører over USB, til din egen MQTT-broker, MeshCore Analyzer eller begge.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-26'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
---

En repeater er en node, der sender beskeder videre. Du vil have dens trafik på en MQTT-broker: din egen til et dashboard eller en database, eller den hos [MeshCore Analyzer](https://meshcore-analyzer.eu/). Eller din repeater har ikke selv Wi-Fi, men der står en Raspberry Pi eller en server ved siden af den. [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), et værktøj fra fællesskabet, er broen: det sender trafikken fra den computer. Din repeater bliver ved med at repeate, fordi broen kun læser det, den logger over USB.

## Det skal du bruge {#need}

- En repeater bygget med pakkelogning (se nedenfor).
- En Raspberry Pi Zero, 2, 3 eller 4, eller en hvilken som helst Linux- eller macOS-computer med Python 3.11 eller nyere.
- Et USB-datakabel mellem de to.

Standardfirmwaren til repeatere fra flasheren logger ikke pakker. Byg selv repeater-firmwaren fra [MeshCore-kildekoden](https://github.com/meshcore-dev/MeshCore) med dette flag tilføjet til dit boards build:

```text
-D MESH_PACKET_LOGGING=1
```

## Installation {#install}

Sæt repeateren i computeren, og kør derefter installationsscriptet fra meshcoretomqtt på den computer:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Det installerer broen som en tjeneste, der starter sammen med computeren, og spørger, hvilke brokere der skal sendes til. Analyzeren står ikke på den liste; den tilføjer du i konfigurationsfilen nedenfor. Dine egne indstillinger ligger i `/etc/mctomqtt/config.d/99-user.toml`; en opdatering overskriver aldrig den fil.

## Brokere {#brokers}

Hver broker får sin egen `[[broker]]`-blok, så én repeater kan fodre flere på samme tid. Din egen broker tager et brugernavn og en adgangskode, eller slet intet login (`method = "none"`). MeshCore Analyzer tager i stedet et token, som din repeaters nøgle signerer:

- adresse `mqtt.meshcore-analyzer.eu`, port `443`, over en sikker websocket;
- tokenets audience er den samme adresse.

## Din konfigurationsfil {#config}

Erstat indholdet af `/etc/mctomqtt/config.d/99-user.toml` med dette. Udfyld lufthavnskoden nærmest din repeater (for eksempel `AMS`) og den USB-port, din repeater sidder på. Tilføj derefter din egen broker. Udelad en blok, du ikke har brug for.

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

Genstart tjenesten efter en ændring (`sudo systemctl restart mctomqtt` på Linux). Din repeater dukker derefter op på Analyzeren som en observer, en node, der uploader det, den hører, under din repeaters eget navn. I [README-filen til meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) finder du alle andre indstillinger.
