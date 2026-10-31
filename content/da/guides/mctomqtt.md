---
title: Byg en bro-konfiguration
lead: 'Send det, din repeater hører, til en vilkårlig MQTT-broker: din egen eller Analyzer. En computer ved siden af repeateren står for afsendelsen.'
description: Kør meshcoretomqtt på en Raspberry Pi eller en anden computer, og send det, en MeshCore-repeater hører over USB, til din egen MQTT-broker, til MeshCore Analyzer eller til begge.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-31'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

En repeater er en node, der sender beskeder videre. Du vil have dens trafik på en MQTT-broker:
din egen til et dashboard eller en database, eller brokeren hos
[MeshCore Analyzer](https://meshcore-analyzer.eu/). Eller din repeater har ikke
selv Wi-Fi, men der står en Raspberry Pi eller en server ved siden af den.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), et værktøj fra fællesskabet,
er broen: Det sender trafikken fra den computer. Din repeater bliver ved med
at videresende. Broen læser nemlig kun det, repeateren logger over USB.

## Det skal du bruge {#need}

- En repeater bygget med pakkelogning (se nedenfor).
- En Raspberry Pi Zero, 2, 3 eller 4 eller en anden Linux- eller macOS-computer med Python
  3.11 eller nyere.
- Et USB-datakabel mellem de to.

Standard-firmwaren til repeatere fra flasheren logger ikke pakker. Byg selv
repeater-firmwaren ud fra
[MeshCores kildekode](https://github.com/meshcore-dev/MeshCore), og tilføj dette flag
til buildet for dit board:

```text
-D MESH_PACKET_LOGGING=1
```

## Installation {#install}

Slut repeateren til computeren. Kør derefter installationsscriptet til
meshcoretomqtt på den computer:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Scriptet installerer broen som en tjeneste, der starter sammen med computeren. Det spørger også,
hvilke brokere broen skal sende til. Analyzer er ikke på den liste. Den tilføjer du i
konfigurationsfilen nedenfor. Dine egne indstillinger ligger i
`/etc/mctomqtt/config.d/99-user.toml`. En opdatering overskriver aldrig den fil.

## Brokere {#brokers}

Hver broker får sin egen `[[broker]]`-blok. Så kan én repeater sende til flere
på samme tid. Din egen broker bruger et brugernavn og en adgangskode eller slet ikke noget login
(`method = "none"`).
MeshCore Analyzer bruger i stedet et token, som din repeaters nøgle signerer:

- adresse `mqtt.meshcore-analyzer.eu`, port `443`, over en sikker websocket;
- tokenets audience er den samme adresse.

## Din konfigurationsfil {#config}

Erstat indholdet af `/etc/mctomqtt/config.d/99-user.toml` med dette. Udfyld
koden for den lufthavn, der ligger nærmest din repeater (f.eks. `AMS`), og den USB-port,
din repeater sidder i. Tilføj derefter din egen broker. Udelad de blokke, du
ikke har brug for.

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

Genstart tjenesten, når du har ændret noget (`sudo systemctl restart mctomqtt` på
Linux). Derefter dukker din repeater op i Analyzer som observer, altså en node, der
uploader det, den hører. Den vises under din repeaters eget navn. Alle andre indstillinger
finder du i [meshcoretomqtt-README'en](https://github.com/Cisien/meshcoretomqtt).
