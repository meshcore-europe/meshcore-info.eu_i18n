---
title: Lag en bridge-konfigurasjon
lead: 'Send det repeateren din hører til en hvilken som helst MQTT-broker: din egen, eller Analyzer. En datamaskin ved siden av repeateren gjør sendingen.'
description: Kjør meshcoretomqtt på en Raspberry Pi eller en annen datamaskin for å sende det en MeshCore-repeater hører over USB til din egen MQTT-broker, MeshCore Analyzer, eller begge.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-26'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
---

En repeater er en node som sender meldinger videre. Du vil ha trafikken dens
på en MQTT-broker: din egen for et dashbord eller en database, eller den til
[MeshCore Analyzer](https://meshcore-analyzer.eu/). Eller repeateren din har
ikke egen Wi-Fi, men en Raspberry Pi eller en server står ved siden av den.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), et verktøy fra
fellesskapet, er bridgen: den sender trafikken fra den datamaskinen.
Repeateren din fortsetter å repetere, fordi bridgen bare leser det den logger
over USB.

## Dette trenger du {#need}

- En repeater bygget med pakkelogging (se under).
- En Raspberry Pi Zero, 2, 3 eller 4, eller en hvilken som helst Linux- eller
  macOS-maskin, med Python 3.11 eller nyere.
- En USB-datakabel mellom de to.

Standard repeater-firmware fra flasheren logger ikke pakker. Bygg
repeater-firmwaren selv fra
[MeshCore-kildekoden](https://github.com/meshcore-dev/MeshCore) med dette
flagget lagt til i bygget for kortet ditt:

```text
-D MESH_PACKET_LOGGING=1
```

## Installer {#install}

Koble repeateren til datamaskinen, og kjør så installasjonsskriptet til
meshcoretomqtt på den maskinen:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skriptet installerer bridgen som en tjeneste som starter sammen med
datamaskinen, og spør hvilke brokere den skal sende til. Analyzer står ikke
på den listen; den legger du til i konfigurasjonsfilen under. Dine egne
innstillinger ligger i `/etc/mctomqtt/config.d/99-user.toml`; en oppdatering
overskriver aldri den filen.

## Brokere {#brokers}

Hver broker får sin egen `[[broker]]`-blokk, så én repeater kan mate flere
samtidig. Din egen broker tar et brukernavn og et passord, eller ingen
innlogging i det hele tatt (`method = "none"`).
MeshCore Analyzer tar i stedet et token, som nøkkelen til repeateren din
signerer:

- adresse `mqtt.meshcore-analyzer.eu`, port `443`, over en sikker websocket;
- tokenets audience er den samme adressen.

## Konfigurasjonsfilen din {#config}

Erstatt innholdet i `/etc/mctomqtt/config.d/99-user.toml` med dette. Fyll inn
flyplasskoden nærmest repeateren din (`AMS`, for eksempel) og USB-porten
repeateren står på. Legg så til din egen broker. La en blokk du ikke trenger
stå utenfor.

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

Start tjenesten på nytt etter en endring (`sudo systemctl restart mctomqtt`
på Linux). Repeateren din vises da på Analyzer som en observer, en node som
laster opp det den hører, under repeaterens eget navn. I
[README for meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) finner
du alle andre innstillinger.
