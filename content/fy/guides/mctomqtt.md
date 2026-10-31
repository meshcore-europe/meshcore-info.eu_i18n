---
title: In brêgekonfiguraasje bouwe
lead: 'Stjoer wat dyn repeater heart nei hokker MQTT-broker dan ek: dyn eigen, of de Analyzer. In kompjûter neist de repeater docht it stjoeren.'
description: Draai meshcoretomqtt op in Raspberry Pi of in oare kompjûter en stjoer wat in MeshCore-repeater oer USB heart nei dyn eigen MQTT-broker, de MeshCore Analyzer of beide.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-31'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

In repeater is in node dy't berjochten trochjout. Do wolst syn ferkear op in MQTT-broker
ha: dyn eigen foar in dashboard of in database, of dy fan de
[MeshCore Analyzer](https://meshcore-analyzer.eu/). Of dyn repeater hat sels gjin
WiFi, mar der stiet in Raspberry Pi of in server neist.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), in ark út de mienskip,
is de brêge: it stjoert it ferkear fan dy kompjûter út. Dyn repeater bliuwt
trochjaan, want de brêge lêst allinnich wat de repeater oer USB logt.

## Wat do nedich hast {#need}

- In repeater dy't mei pakketlogging boud is (sjoch hjirûnder).
- In Raspberry Pi Zero, 2, 3 of 4, of in oare kompjûter mei Linux of macOS, mei Python
  3.11 of nijer.
- In USB-datakabel tusken de twa.

De standert repeaterfirmware út de flasher logt gjin pakketten. Bou
de repeaterfirmware sels út de
[MeshCore-boarnekoade](https://github.com/meshcore-dev/MeshCore) en heakje dizze flag
ta oan de build fan dyn board:

```text
-D MESH_PACKET_LOGGING=1
```

## Ynstallearje {#install}

Stek de repeater yn de kompjûter. Draai dêrnei op dy kompjûter it ynstallaasjeskript
fan meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

It skript ynstallearret de brêge as tsjinst dy't mei de kompjûter opstart. It freget
ek nei hokker brokers it stjoere moat. De Analyzer stiet net yn dy list; dy heakest do ta yn
it konfiguraasjebestân hjirûnder. Dyn eigen ynstellingen steane yn
`/etc/mctomqtt/config.d/99-user.toml`; in update oerskriuwt dat bestân nea.

## Brokers {#brokers}

Elke broker krijt in eigen `[[broker]]`-blok, sadat ien repeater ferskate brokers
tagelyk fiede kin. Foar dyn eigen broker brûkst do in brûkersnamme en in wachtwurd, of hielendal gjin oanmelding
(`method = "none"`).
De MeshCore Analyzer wol ynstee in token ha, dat de kaai fan dyn repeater ûndertekenet:

- adres `mqtt.meshcore-analyzer.eu`, poarte `443`, oer in befeilige websocket;
- de audience fan it token is itselde adres.

## Dyn konfiguraasjebestân {#config}

Ferfang de ynhâld fan `/etc/mctomqtt/config.d/99-user.toml` troch dit. Folje
de fleanfjildkoade yn dy't it tichtst by dyn repeater leit (bygelyks `AMS`), en de USB-poarte
dêr't dyn repeater oan sit. Heakje dêrnei dyn eigen broker ta. Lit in blok dat do
net nedich hast fuort.

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

Start de tsjinst nei in feroaring opnij (`sudo systemctl restart mctomqtt` op
Linux). Dyn repeater ferskynt dan op de Analyzer as observer, in node dy't
uploadt wat er heart, ûnder de eigen namme fan dyn repeater. Yn de
[README fan meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) fynst do alle
oare ynstellingen.
