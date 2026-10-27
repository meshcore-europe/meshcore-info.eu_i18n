---
title: Eine Bridge-Konfiguration erstellen
lead: 'Schick, was dein Repeater hört, an einen beliebigen MQTT-Broker: deinen eigenen oder den Analyzer. Ein Computer neben dem Repeater übernimmt das Senden.'
description: Lass meshcoretomqtt auf einem Raspberry Pi oder einem anderen Computer laufen, um alles, was ein MeshCore-Repeater hört, über USB an deinen eigenen MQTT-Broker, den MeshCore Analyzer oder beide zu senden.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-26'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
---

Ein Repeater ist ein Knoten, der Nachrichten weiterleitet. Du willst seinen
Verkehr auf einem MQTT-Broker haben: auf deinem eigenen für ein Dashboard oder
eine Datenbank, oder auf dem des
[MeshCore Analyzer](https://meshcore-analyzer.eu/). Oder dein Repeater hat kein
eigenes WLAN, aber daneben steht ein Raspberry Pi oder ein Server.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), ein Tool aus der
Community, ist die Bridge: Es sendet den Verkehr von diesem Computer aus. Dein
Repeater arbeitet dabei normal weiter, denn die Bridge liest nur mit, was er
über USB protokolliert.

## Was du brauchst {#need}

- Einen Repeater mit eingebautem Paket-Logging (siehe unten).
- Einen Raspberry Pi Zero, 2, 3 oder 4 oder einen beliebigen Linux- oder
  macOS-Computer mit Python 3.11 oder neuer.
- Ein USB-Datenkabel zwischen beiden.

Die Standard-Repeater-Firmware aus dem Flasher protokolliert keine Pakete. Baue
die Repeater-Firmware selbst aus dem
[MeshCore-Quellcode](https://github.com/meshcore-dev/MeshCore) und füge dem
Build für dein Board dieses Flag hinzu:

```text
-D MESH_PACKET_LOGGING=1
```

## Installieren {#install}

Schließ den Repeater an den Computer an und starte dann auf diesem Computer das
Installationsskript von meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Das Skript richtet die Bridge als Dienst ein, der mit dem Computer startet, und
fragt dich, an welche Broker du senden willst. Der Analyzer steht nicht in dieser
Liste; den trägst du unten in der Konfigurationsdatei ein. Deine eigenen
Einstellungen liegen in `/etc/mctomqtt/config.d/99-user.toml`; ein Update
überschreibt diese Datei nie.

## Broker {#brokers}

Jeder Broker bekommt seinen eigenen `[[broker]]`-Block, sodass ein Repeater
mehrere gleichzeitig beliefern kann. Dein eigener Broker nimmt einen
Benutzernamen und ein Passwort oder gar keine Anmeldung (`method = "none"`).
Der MeshCore Analyzer nimmt stattdessen ein Token, das der Schlüssel deines
Repeaters signiert:

- Adresse `mqtt.meshcore-analyzer.eu`, Port `443`, über einen sicheren
  Websocket;
- die Audience des Tokens ist dieselbe Adresse.

## Deine Konfigurationsdatei {#config}

Ersetze den Inhalt von `/etc/mctomqtt/config.d/99-user.toml` durch Folgendes.
Trag den Flughafencode ein, der deinem Repeater am nächsten liegt (zum Beispiel
`AMS`), und den USB-Port, an dem dein Repeater hängt. Füge dann deinen eigenen
Broker hinzu. Einen Block, den du nicht brauchst, lässt du weg.

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

Starte den Dienst nach einer Änderung neu (unter Linux mit
`sudo systemctl restart mctomqtt`). Dein Repeater erscheint dann im Analyzer als
Observer, also als Knoten, der hochlädt, was er hört, unter dem Namen deines
Repeaters. Alle weiteren Einstellungen findest du in der
[README von meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt).
