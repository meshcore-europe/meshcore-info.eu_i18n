---
title: MQTT auf deinem Observer
lead: Dein Repeater meldet über WLAN an den MeshCore Analyzer, was er hört. Nachrichten leitet er weiter wie bisher.
description: Mach aus einem ESP32-Repeater einen MeshCore-Observer mit der DMC-Observer-Firmware. Du flashst sie, stellst WLAN und deinen Flughafencode ein, wählst die Broker und prüfst, ob sie an den MeshCore Analyzer meldet.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-31'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Ein Observer ist ein Knoten, der zusätzlich per MQTT über WLAN meldet, was er
hört. Jeder Observer zeigt etwas mehr vom Mesh im
[MeshCore Analyzer](https://meshcore-analyzer.eu/) und auf den
[Abdeckungskarten](/map/). In dieser Anleitung machst du aus einem Repeater
(einem Knoten, der Nachrichten weiterleitet) einen Observer. Er leitet
weiterhin weiter, und die Meldung geht nur in eine Richtung: Nichts kommt
zurück ins Mesh.

{{< callout type="warning" >}}
Diese Anleitung gilt für die **DMC-Observer-Firmware**, den Observer-Build von
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) auf Basis von
MeshCore 1.18.0. Das Standard-MeshCore hat kein MQTT. Alle Befehle unten
stammen aus dem Quellcode der Firmware, Build `32dd8ad` vom 19. Oktober 2026.
{{< /callout >}}

## Was du brauchst {#need}

- Ein ESP32-Board mit WLAN, zum Beispiel ein Heltec V3 oder V4, ein LilyGo T3S3
  oder ein Xiao S3. Das [Release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  nennt alle Boards. nRF52-Boards wie das RAK4631 haben kein WLAN.
- Ein 2.4-GHz-WLAN dort, wo das Board steht.
- Ein USB-Datenkabel und Chrome, Edge oder Opera auf deinem Computer.
- Den Flughafencode, der deinem Knoten am nächsten liegt: 3 Buchstaben wie
  `AMS` oder `BRU`. Er sagt den Brokern (den Servern, die deine Meldungen
  empfangen), in welchem Gebiet dein Observer steht.

Am Standort deines Repeaters gibt es kein WLAN, aber einen Computer daneben?
[Erstelle stattdessen eine Bridge-Konfiguration](/guides/mctomqtt/).

## Firmware flashen {#flash}

Der [Flasher](/firmware/flasher/) auf dieser Seite enthält nur das
Standard-MeshCore. Die Observer-Firmware bekommst du über den Flasher in der
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Wähle dein Board und dann **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Wähle beim ersten Mal **Full flash**: Damit ersetzt du alles auf dem Board,
   auch die Partitionstabelle. Das App-Update behält den vorhandenen Inhalt
   und ist für spätere Updates gedacht.
3. Richte deinen Repeater wie gewohnt ein: Name, Funk-Preset und
   Admin-Passwort, wie in der [Repeater-Anleitung](/repeater-guide/#config).

Diese Firmware ist der **dev**-Build. Wenn du `ota update` eingibst, holt sie
das Update aus dem dev-Kanal. Im stable-Kanal liegt noch 1.17.1, also bleib
für diese Anleitung bei dev.

## Einstellungen {#settings}

Öffne die [serielle Konsole](/firmware/console/) auf dieser Seite und verbinde
dein Board. Trag dein eigenes WLAN, dein Passwort und deinen Flughafencode ein.
Füge dann diese Zeilen einzeln ein:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Nach dem Neustart verbindet sich das Board mit deinem WLAN und stellt seine Uhr
über das Internet. Die Broker brauchen diese Uhrzeit, um deinen Observer zu
identifizieren. Ohne Flughafencode meldet das Board nichts.

Klickst du lieber, statt zu tippen? Mit `start webconfig` öffnest du eine
Einstellungsseite auf dem Board, unter der Adresse, die die Konsole anzeigt.
Melde dich mit deinem Admin-Passwort an.

## Broker-Slots {#brokers}

Ein Slot enthält einen Broker. Ab Werk sind diese Slots in der Firmware belegt:

| Slot | Broker | Betrieben von |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Ein Board ohne Zusatzspeicher (PSRAM), etwa das Heltec V3, hat 3 Slots. Es
verbindet sich mit 2 davon gleichzeitig, also verbindet sich der Analyzer in
Slot 3 nie. Verschieb ihn in Slot 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Ein Board mit PSRAM, etwa das Heltec V4, hat 6 Slots und verbindet sich mit 5
gleichzeitig. Dort musst du nichts ändern.

Dein Knoten meldet sich bei jedem Broker mit seinem eigenen Schlüssel an, du
brauchst also kein Konto. Mit `get mqtt.presets` siehst du die anderen
Community-Broker, die die Firmware kennt.

### Dein eigener Broker {#own}

Trag deinen eigenen Broker in einen freien Slot ein. Gib Adresse, Port,
Benutzername und Passwort an. Auf einem Board mit PSRAM ist Slot 4 frei:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Auf einem Board ohne PSRAM nimmst du stattdessen Slot 2: Ersetze `mqtt4` durch
`mqtt2`. Dein Broker tritt dann an die Stelle von `dutchmeshcore-2`.

Über Port `8883` läuft die Verbindung verschlüsselt (TLS), über Port `443`
verschlüsselt per Webverbindung (Websocket) und über jeden anderen Port
unverschlüsselt. Du kannst auch die vollständige Adresse angeben, etwa
`wss://mqtt.example.org:9002/mqtt`. Dann gilt die Port-Regel nicht.

## Prüfen, ob es läuft {#check}

Gib `get mqtt.status` ein. Zu jedem Slot siehst du den Zustand:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: verbunden.
- `wait`: Dem Slot fehlt eine Einstellung, etwa der Flughafencode.
- `disc`: noch nicht verbunden. Prüf dein WLAN mit `get wifi.status`.
- `fail`: Der Slot ist 7-mal hintereinander gescheitert, über etwa 20 Minuten,
  und versucht es jetzt einmal alle 30 Minuten. Prüf Adresse und Zugangsdaten
  des Brokers.
- `inactive`: Das Board hat keinen Platz für diesen Slot. Siehe
  [Broker-Slots](#brokers).

Such dann den Namen deines Repeaters auf der
[Observer-Seite des Analyzers](https://meshcore-analyzer.eu/#observers).
Er erscheint innerhalb von 5 Minuten, mit dem, was er gehört hat.
