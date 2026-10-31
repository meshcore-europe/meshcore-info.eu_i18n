---
title: MQTT op je observer
lead: Laat je repeater via wifi aan de MeshCore Analyzer melden wat hij hoort. Hij blijft berichten doorgeven zoals voorheen.
description: Maak van een ESP32-repeater een MeshCore-observer met de DMC observer-firmware. Flash de firmware, stel wifi en je luchthavencode in, kies de brokers en controleer of hij meldt aan de MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-31'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Een observer is een node die ook meldt wat hij hoort, via MQTT over wifi.
Elke observer laat iets meer van de mesh zien op de
[MeshCore Analyzer](https://meshcore-analyzer.eu/) en op de
[dekkingskaarten](/map/). Met deze handleiding maak je van een repeater (een
node die berichten doorgeeft) een observer. Hij blijft doorgeven, en de
melding gaat één kant op: er komt niets terug op de mesh.

{{< callout type="warning" >}}
Deze handleiding gaat over de **DMC observer-firmware**, de observer-build van
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), gebaseerd op
MeshCore 1.18.0. Standaard MeshCore heeft geen MQTT. Alle commando's hieronder
komen uit de broncode van de firmware, build `32dd8ad` van 19 oktober 2026.
{{< /callout >}}

## Wat je nodig hebt {#need}

- Een ESP32-bord met wifi, zoals een Heltec V3 of V4, een LilyGo T3S3 of een
  Xiao S3. In de [release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  staan alle borden. nRF52-borden zoals de RAK4631 hebben geen wifi.
- Een 2.4 GHz-wifinetwerk op de plek van het bord.
- Een USB-datakabel, en Chrome, Edge of Opera op je computer.
- De luchthavencode het dichtst bij je node, 3 letters zoals `AMS` of `BRU`.
  Daarmee weten de brokers (de servers die je meldingen ontvangen) in welk
  gebied je observer staat.

Geen wifi bij je repeater, maar wel een computer ernaast?
[Stel dan een bridge-configuratie samen](/guides/mctomqtt/).

## De firmware flashen {#flash}

De [flasher](/firmware/flasher/) op deze site heeft alleen standaard MeshCore.
De observer-firmware haal je uit de flasher in de
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Kies je bord en daarna **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Kies de eerste keer **Full flash**: die vervangt alles op het bord, ook de
   partitietabel. De app-update laat staan wat er al is en gebruik je voor
   latere updates.
3. Stel je repeater in zoals gewoonlijk: naam, radiopreset en
   beheerderswachtwoord, zoals in de [repeater-handleiding](/repeater-guide/#config).

Deze firmware is de **dev**-build. Als je `ota update` typt, werkt hij
zichzelf bij vanuit het dev-kanaal. Op het stabiele kanaal staat nog 1.17.1,
dus blijf voor deze handleiding op dev.

## Instellingen {#settings}

Open de [seriële console](/firmware/console/) op deze site en verbind je bord.
Vul je eigen wifinetwerk, wachtwoord en luchthavencode in. Plak deze regels
daarna één voor één:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Na de herstart maakt het bord verbinding met je wifi en haalt het de tijd van
internet. Met die klok controleren de brokers wie je observer is. Zonder
luchthavencode wordt er niets gemeld.

Klik je liever dan dat je typt? Met `start webconfig` open je een
instellingenpagina op het bord, op het adres dat de console toont. Log in met
je beheerderswachtwoord.

## Broker-slots {#brokers}

In een slot staat één broker. Bij de start zijn deze slots al ingevuld:

| Slot | Broker | Beheerd door |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Een bord zonder extra geheugen (PSRAM), zoals de Heltec V3, heeft 3 slots. Het
verbindt met 2 tegelijk, dus de Analyzer in slot 3 krijgt nooit verbinding.
Zet hem in slot 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Een bord met PSRAM, zoals de Heltec V4, heeft 6 slots en verbindt met 5
tegelijk. Daar hoef je niets te veranderen.

Je node logt bij elke broker in met een eigen sleutel, dus je hebt geen
account nodig. Met `get mqtt.presets` zie je de andere communitybrokers die de
firmware kent.

### Je eigen broker {#own}

Zet je eigen broker in een vrij slot. Vul het adres, de poort, de
gebruikersnaam en het wachtwoord in. Op een bord met PSRAM is slot 4 vrij:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Gebruik op een bord zonder PSRAM slot 2: vervang `mqtt4` door `mqtt2`. Je
broker neemt dan de plaats in van `dutchmeshcore-2`.

Via poort `8883` verbind je versleuteld (TLS), via poort `443` versleuteld
over een webverbinding (websocket) en via elke andere poort onversleuteld. Je
kunt ook het volledige adres opgeven, zoals `wss://mqtt.example.org:9002/mqtt`.
De regel voor de poort geldt dan niet.

## Controleren of het werkt {#check}

Typ `get mqtt.status`. Je ziet dan de status van elk slot:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: verbonden.
- `wait`: het slot mist een instelling, zoals de luchthavencode.
- `disc`: nog niet verbonden. Controleer je wifi met `get wifi.status`.
- `fail`: het slot is 7 keer achter elkaar mislukt, in ongeveer 20 minuten,
  en probeert het nu eens per 30 minuten. Controleer het adres en de
  inloggegevens van de broker.
- `inactive`: het bord heeft geen ruimte voor dit slot. Zie
  [Broker-slots](#brokers).

Zoek daarna de naam van je repeater op de
[observerpagina van de Analyzer](https://meshcore-analyzer.eu/#observers).
Binnen 5 minuten verschijnt hij daar, met wat hij heeft gehoord.
