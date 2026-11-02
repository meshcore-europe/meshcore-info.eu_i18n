---
title: Eng Bréck-Konfiguratioun opsetzen
lead: 'Schéck dat, wat däi Repeater héiert, op all MQTT-Broker: däin eegenen oder deen vum Analyzer. E Computer nieft dem Repeater iwwerhëlt d''Schécken.'
description: Mat meshcoretomqtt op engem Raspberry Pi oder engem anere Computer schécks du dat, wat e MeshCore-Repeater héiert, iwwer USB op däin eegene MQTT-Broker, op de MeshCore Analyzer oder op béid.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

E Repeater ass en Node, deen Noriichte weiderleet. Du wëlls säin Traffic op
engem MQTT-Broker hunn: op dengem eegene fir en Dashboard oder eng Datebank, oder
op deem vum [MeshCore Analyzer](https://meshcore-analyzer.eu/). Oder däi Repeater
huet selwer kee Wi-Fi, mee e Raspberry Pi oder e Server steet dernieft.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), e Community-Tool,
ass d'Bréck: et schéckt den Traffic vun deem Computer aus. Däi Repeater leet
Noriichte weider wéi virdrun, well d'Bréck nëmmen dat liest, wat hien iwwer USB
protokolléiert.

## Wat s du brauchs {#need}

- E Repeater, dee mat Packet-Logging gebaut ass (kuck hei ënnen).
- E Raspberry Pi Zero, 2, 3 oder 4, oder all anere Linux- oder macOS-Computer,
  mat Python 3.11 oder méi nei.
- En USB-Datekabel tëscht deenen zwee.

D'Standard-Repeater-Firmware aus dem Flasher protokolléiert keng Paketen. Bau d'Repeater-Firmware
selwer aus dem [MeshCore-Quellcode](https://github.com/meshcore-dev/MeshCore)
a setz dëse Flag an de Build vun dengem Board:

```text
-D MESH_PACKET_LOGGING=1
```

## Installéieren {#install}

Schléiss de Repeater un de Computer un. Start dann op deem Computer den
Installatiounsskript vu meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

De Skript installéiert d'Bréck als Service, deen zesumme mam Computer start. Hie
freet dech och, op wéi eng Brokere si schécke soll. Den Analyzer steet net an där
Lëscht: du füügs en an der Konfiguratiounsdatei hei ënnen derbäi. Deng eegen
Astellunge stinn an `/etc/mctomqtt/config.d/99-user.toml`. En Update iwwerschreift
dës Datei ni.

## Brokeren {#brokers}

All Broker kritt säin eegene `[[broker]]`-Block, sou kann ee Repeater der e puer
gläichzäiteg beliwweren. Bei dengem eegene Broker gëss du e Benotzernumm an e
Passwuert un, oder du kënns ganz ouni Umeldung aus (`method = "none"`).
De MeshCore Analyzer verlaangt amplaz en Token, deen de Schlëssel vun dengem
Repeater signéiert:

- Adress `mqtt.meshcore-analyzer.eu`, Port `443`, iwwer e séchere Websocket;
- d'Audience vum Token ass déi selwecht Adress.

## Deng Konfiguratiounsdatei {#config}

Ersetz den Inhalt vun `/etc/mctomqtt/config.d/99-user.toml` duerch dësen Text.
Dro de Code vum Fluchhafen an, deen am nootsten un dengem Repeater läit
(zum Beispill `AMS`), an den USB-Port, un deem däi Repeater hänkt. Füüg dann däin
eegene Broker derbäi. Looss e Block ewech, wann s du en net brauchs.

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

Start de Service no enger Ännerung nei (`sudo systemctl restart mctomqtt` op
Linux). Däi Repeater erschéngt dann um Analyzer ënner sengem eegenen Numm als
Observer, en Node, deen eroplued, wat en héiert. All aner Astellunge fënns du am
[meshcoretomqtt README](https://github.com/Cisien/meshcoretomqtt).
