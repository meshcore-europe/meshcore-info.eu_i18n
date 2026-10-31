---
title: Bridge-Konfiguration erstellen
lead: 'Schick, was dein Repeater hört, an einen beliebigen MQTT-Broker: deinen eigenen oder den des Analyzers. Ein Computer neben dem Repeater übernimmt das Senden.'
description: Mit meshcoretomqtt auf einem Raspberry Pi oder einem anderen Computer schickst du, was ein MeshCore-Repeater über USB hört, an deinen eigenen MQTT-Broker, an den MeshCore Analyzer oder an beide.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-31'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Ein Repeater ist ein Knoten, der Nachrichten weiterleitet. Du willst seinen Verkehr
auf einem MQTT-Broker haben: auf deinem eigenen für ein Dashboard oder eine
Datenbank oder auf dem des [MeshCore Analyzer](https://meshcore-analyzer.eu/).
Oder dein Repeater hat kein eigenes WiFi, aber neben ihm steht ein Raspberry Pi
oder ein Server. [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) ist
ein Tool aus der Community und die Bridge: Es schickt den Verkehr von diesem
Computer aus. Dein Repeater leitet weiter wie bisher, denn die Bridge liest nur,
was er über USB protokolliert.

## Was du brauchst {#need}

- Einen Repeater, der mit Paketprotokollierung gebaut ist (siehe unten).
- Einen Raspberry Pi Zero, 2, 3 oder 4 oder einen beliebigen Linux- oder
  macOS-Computer mit Python 3.11 oder neuer.
- Ein USB-Datenkabel zwischen beiden.

Die Standard-Firmware für Repeater aus dem Flasher protokolliert keine Pakete.
Du baust die Repeater-Firmware selbst aus dem
[MeshCore-Quellcode](https://github.com/meshcore-dev/MeshCore). Dabei ergänzt du
im Build für dein Board dieses Flag:

```text
-D MESH_PACKET_LOGGING=1
```

## Installieren {#install}

Schließ den Repeater an den Computer an. Führ dann auf diesem Computer das
Installationsskript von meshcoretomqtt aus:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Das Skript installiert die Bridge als Dienst, der mit dem Computer startet. Es
fragt dich, an welche Broker die Bridge senden soll. Der Analyzer steht nicht in
dieser Liste. Du trägst ihn unten in der Konfigurationsdatei ein. Deine eigenen
Einstellungen stehen in `/etc/mctomqtt/config.d/99-user.toml`. Ein Update
überschreibt diese Datei nie.

## Broker {#brokers}

Jeder Broker bekommt einen eigenen `[[broker]]`-Block. So kann ein Repeater
mehrere Broker gleichzeitig beliefern. Dein eigener Broker braucht einen
Benutzernamen und ein Passwort oder gar keine Anmeldung (`method = "none"`).
Der MeshCore Analyzer braucht stattdessen ein Token, das der Schlüssel deines
Repeaters signiert:

- Adresse `mqtt.meshcore-analyzer.eu`, Port `443`, über einen sicheren Websocket;
- die Audience des Tokens ist dieselbe Adresse.

## Deine Konfigurationsdatei {#config}

Ersetz den Inhalt von `/etc/mctomqtt/config.d/99-user.toml` durch Folgendes. Trag
den Flughafencode ein, der deinem Repeater am nächsten liegt (zum Beispiel
`AMS`), und den USB-Port, an dem dein Repeater hängt. Ergänz dann deinen eigenen
Broker. Einen Block, den du nicht brauchst, lässt du weg.

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

Starte den Dienst nach jeder Änderung neu (`sudo systemctl restart mctomqtt`
unter Linux). Dein Repeater erscheint dann im Analyzer als Observer, also als
Knoten, der hochlädt, was er hört. Er trägt dort den eigenen Namen deines
Repeaters. Alle weiteren Einstellungen findest du in der
[README von meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt).
