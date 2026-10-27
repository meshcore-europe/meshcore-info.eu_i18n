---
title: MQTT auf deinem Observer
lead: Lass deinen Repeater über WLAN an den MeshCore Analyzer melden, was er hört. Nachrichten leitet er weiter wie bisher.
description: Mach aus einem ESP32-Repeater mit der DMC-Observer-Firmware einen MeshCore-Observer. Flashe sie, trage WLAN und deinen Flughafencode ein, wähle die Broker und prüfe, ob die Meldungen beim MeshCore Analyzer ankommen.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-26'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
---

Ein Observer ist ein Knoten, der zusätzlich über MQTT meldet, was er hört, und zwar per WLAN. Jeder Observer zeigt auf dem [MeshCore Analyzer](https://meshcore-analyzer.eu/) und auf den [Abdeckungskarten](/map/) ein Stück mehr vom Mesh. Diese Anleitung macht aus einem Repeater (einem Knoten, der Nachrichten weiterleitet) einen Observer. Er leitet weiterhin Nachrichten weiter, und die Meldung geht nur in eine Richtung: Nichts kommt zurück ins Mesh.

{{< callout type="warning" >}}
Diese Anleitung gilt für die **DMC-Observer-Firmware**, den Observer-Build von [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), der auf MeshCore 1.18.0 basiert. Die normale MeshCore-Firmware hat kein MQTT. Alle Befehle unten stammen aus dem Firmware-Quellcode, Build `32dd8ad` vom 19. Oktober 2026.
{{< /callout >}}

## Was du brauchst {#need}

- Ein ESP32-Board mit WLAN, zum Beispiel ein Heltec V3 oder V4, ein LilyGo T3S3 oder ein Xiao S3. Das [Release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev) listet alle Boards auf. nRF52-Boards wie das RAK4631 haben kein WLAN.
- Ein 2.4 GHz WLAN-Netz an dem Ort, an dem das Board steht.
- Ein USB-Datenkabel sowie Chrome, Edge oder Opera auf deinem Computer.
- Den Flughafencode, der deinem Knoten am nächsten liegt, 3 Buchstaben wie `AMS` oder `BRU`. Er sagt den Brokern (den Servern, die deine Meldungen empfangen), in welchem Gebiet dein Observer steht.

Kein WLAN dort, wo dein Repeater steht, aber ein Computer daneben? [Baue stattdessen eine Bridge-Konfiguration](/guides/mctomqtt/).

## Firmware flashen {#flash}

Der [Flasher](/firmware/flasher/) auf dieser Seite enthält nur die normale MeshCore-Firmware. Die Observer-Firmware bekommst du über den Flasher in der [DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Wähle dein Board, dann **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Wähle beim ersten Mal **Full flash**: Das ersetzt alles auf dem Board, auch die Partitionstabelle. Das App-Update lässt den Rest unangetastet und ist für spätere Updates gedacht.
3. Richte deinen Repeater wie gewohnt ein: Name, Funk-Preset und Admin-Passwort, wie in der [Repeater-Anleitung](/repeater-guide/#config) beschrieben.

Diese Firmware ist der **Dev**-Build und aktualisiert sich aus dem Dev-Kanal, wenn du `ota update` eingibst. Der Stable-Kanal liefert noch 1.17.1, bleib für diese Anleitung also auf Dev.

## Einstellungen {#settings}

Öffne die [serielle Konsole](/firmware/console/) auf dieser Seite und verbinde dein Board. Trage dein eigenes WLAN, dein Passwort und deinen Flughafencode ein und füge diese Zeilen dann einzeln ein:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Nach dem Neustart verbindet sich das Board mit deinem WLAN und holt sich die Uhrzeit aus dem Internet. Die Broker brauchen diese Uhrzeit, um zu prüfen, wer dein Observer ist. Ohne Flughafencode wird nichts gemeldet.

Lieber klicken als tippen? Mit `start webconfig` öffnest du eine Einstellungsseite auf dem Board, unter der Adresse, die die Konsole anzeigt. Melde dich mit deinem Admin-Passwort an.

## Broker-Slots {#brokers}

Ein Slot enthält einen Broker. Die Firmware startet mit diesen vorbelegten Slots:

| Slot | Broker | Betrieben von |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Ein Board ohne Zusatzspeicher (PSRAM), etwa das Heltec V3, hat 3 Slots. Es verbindet sich mit 2 davon gleichzeitig, der Analyzer in Slot 3 wird also nie verbunden. Verschiebe ihn in Slot 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Ein Board mit PSRAM, etwa das Heltec V4, hat 6 Slots und verbindet sich mit 5 davon gleichzeitig. Daran musst du nichts ändern.

Dein Knoten meldet sich bei jedem Broker mit seinem eigenen Schlüssel an, du brauchst also kein Konto. `get mqtt.presets` listet die anderen Community-Broker auf, die die Firmware kennt.

### Dein eigener Broker {#own}

Trage deinen eigenen Broker in einen freien Slot ein. Gib seine Adresse, den Port, den Benutzernamen und das Passwort an. Auf einem Board mit PSRAM ist Slot 4 frei:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Auf einem Board ohne PSRAM nimmst du stattdessen Slot 2: Ersetze `mqtt4` durch `mqtt2`. Dein Broker tritt dann an die Stelle von `dutchmeshcore-2`.

Port `8883` verbindet verschlüsselt (TLS), Port `443` verschlüsselt über eine Webverbindung (Websocket), jeder andere Port unverschlüsselt. Du kannst auch die vollständige Adresse angeben, etwa `wss://mqtt.example.org:9002/mqtt`. Dann gilt die Port-Regel nicht.

## Prüfen, ob es läuft {#check}

Gib `get mqtt.status` ein. Jeder Slot zeigt seinen Zustand:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: verbunden.
- `wait`: Dem Slot fehlt eine Einstellung, etwa der Flughafencode.
- `disc`: noch nicht verbunden. Prüfe dein WLAN mit `get wifi.status`.
- `fail`: Der Slot ist 7-mal hintereinander gescheitert, über etwa 20 Minuten, und versucht es jetzt alle 30 Minuten einmal. Prüfe Adresse und Zugangsdaten des Brokers.
- `inactive`: Das Board hat keinen Platz für diesen Slot. Siehe [Broker-Slots](#brokers).

Suche danach den Namen deines Repeaters auf der [Observer-Seite des Analyzers](https://meshcore-analyzer.eu/#observers). Er erscheint dort innerhalb von 5 Minuten, zusammen mit dem, was er gehört hat.
