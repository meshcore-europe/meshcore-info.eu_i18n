---
title: Sett opp en bro
lead: 'Send det repeateren din hører, til en hvilken som helst MQTT-broker: din egen eller Analyzer. En datamaskin ved siden av repeateren står for sendingen.'
description: Kjør meshcoretomqtt på en Raspberry Pi eller en annen datamaskin. Da sender du det en MeshCore-repeater hører over USB, til din egen MQTT-broker, til MeshCore Analyzer eller til begge.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-31'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

En repeater er en node som sender meldinger videre. Du vil ha trafikken fra den på en MQTT-broker. Det kan være din egen, for et dashbord eller en database, eller brokeren til [MeshCore Analyzer](https://meshcore-analyzer.eu/). Eller repeateren din har ikke egen Wi-Fi, men det står en Raspberry Pi eller en server ved siden av den. [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) er et verktøy fra fellesskapet, og det er broen: Det sender trafikken fra den maskinen. Repeateren din fortsetter å videresende, for broen leser bare det repeateren logger over USB.

## Dette trenger du {#need}

- En repeater som er bygget med pakkelogging (se under).
- En Raspberry Pi Zero, 2, 3 eller 4, eller en hvilken som helst Linux- eller macOS-maskin, med Python 3.11 eller nyere.
- En USB-datakabel mellom de to.

Standardfirmwaren for repeatere fra flasheren logger ikke pakker. Du må bygge repeater-firmwaren selv fra [MeshCore-kildekoden](https://github.com/meshcore-dev/MeshCore). Legg da til dette flagget i byggeoppsettet for kortet ditt:

```text
-D MESH_PACKET_LOGGING=1
```

## Installasjon {#install}

Koble repeateren til datamaskinen. Kjør så installasjonsskriptet til meshcoretomqtt på den maskinen:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skriptet installerer broen som en tjeneste som starter sammen med maskinen. Det spør også hvilke brokere du vil sende til. Analyzer står ikke på den listen. Den legger du til i konfigurasjonsfilen under. Dine egne innstillinger ligger i `/etc/mctomqtt/config.d/99-user.toml`. En oppdatering overskriver aldri den filen.

## Brokere {#brokers}

Hver broker får sin egen `[[broker]]`-blokk. Slik kan én repeater sende til flere samtidig. Til din egen broker bruker du brukernavn og passord, eller ingen innlogging i det hele tatt (`method = "none"`).
MeshCore Analyzer bruker i stedet et token, som nøkkelen til repeateren din signerer:

- adresse `mqtt.meshcore-analyzer.eu`, port `443`, over en sikker websocket;
- audience for tokenet er den samme adressen.

## Konfigurasjonsfilen din {#config}

Erstatt innholdet i `/etc/mctomqtt/config.d/99-user.toml` med dette. Fyll inn flyplasskoden som ligger nærmest repeateren din (for eksempel `AMS`). Fyll også inn USB-porten repeateren din sitter i. Legg så til din egen broker. Ta bort blokker du ikke trenger.

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

Start tjenesten på nytt etter en endring (`sudo systemctl restart mctomqtt` på Linux). Da dukker repeateren din opp i Analyzer som en observer, altså en node som laster opp det den hører. Den vises under repeaterens eget navn. I [README-filen til meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) finner du alle andre innstillinger.
