---
title: MQTT op je observer
lead: Laat je repeater over wifi aan de MeshCore Analyzer melden wat hij hoort. Hij blijft berichten doorgeven zoals voorheen.
description: Maak van een ESP32-repeater een MeshCore-observer met de DMC observer-firmware. Flash hem, stel wifi en je luchthavencode in, kies de brokers en controleer of hij rapporteert aan de MeshCore Analyzer.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-26'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
---

Een observer is een node die daarnaast via wifi over MQTT meldt wat hij
hoort. Elke observer laat iets meer van de mesh zien op de
[MeshCore Analyzer](https://meshcore-analyzer.eu/) en op de
[dekkingskaarten](/map/). Met deze handleiding maak je er een van een
repeater (een node die berichten doorgeeft). Hij blijft repeaten, en de
melding gaat één kant op: er komt niets terug op de mesh.

{{< callout type="warning" >}}
Deze handleiding is voor de **DMC observer-firmware**, de observer-build van
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), gebaseerd op
MeshCore 1.18.0. Standaard MeshCore heeft geen MQTT. Elk commando hieronder
komt uit de broncode van de firmware bij build `32dd8ad` van 19 oktober 2026.
{{< /callout >}}

## Wat je nodig hebt {#need}

- Een ESP32-board met wifi, zoals een Heltec V3 of V4, een LilyGo T3S3 of een
  Xiao S3. De [release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  noemt elk board. nRF52-boards zoals de RAK4631 hebben geen wifi.
- Een 2.4 GHz wifi-netwerk op de plek waar het board staat.
- Een USB-datakabel, en Chrome, Edge of Opera op je computer.
- De luchthavencode het dichtst bij je node, 3 letters zoals `AMS` of `BRU`.
  Die vertelt de brokers (de servers die je meldingen ontvangen) in welk
  gebied je observer staat.

Geen wifi waar je repeater staat, maar wel een computer ernaast?
[Maak dan een bridge-config](/guides/mctomqtt/).

## De firmware flashen {#flash}

De [flasher](/firmware/flasher/) op deze site bevat alleen standaard MeshCore.
De observer-firmware haal je uit de flasher in de
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Kies je bord en daarna **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Kies de eerste keer **Full flash**: dat vervangt alles op het bord,
   inclusief de partitietabel. De app-update laat staan wat er is en is
   bedoeld voor latere updates.
3. Stel je repeater in zoals gewoonlijk: naam, radiopreset en
   beheerderswachtwoord, zoals in de
   [repeater-handleiding](/repeater-guide/#config).

Deze firmware is de **dev**-build en werkt zichzelf bij vanuit het dev-kanaal
als je `ota update` typt. Het stabiele kanaal bevat nog 1.17.1, dus blijf
voor deze handleiding op dev.

## Instellingen {#settings}

Open de [seriële console](/firmware/console/) op deze site en verbind je
bord. Vul je eigen wifinetwerk, wachtwoord en luchthavencode in en plak
daarna deze regels één voor één:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Na de herstart verbindt het bord met je wifi en haalt het de tijd van
internet. De brokers hebben die tijd nodig om te controleren wie je observer
is. Zonder luchthavencode wordt er niets gemeld.

Liever klikken dan typen? Met `start webconfig` open je een instellingenpagina
op het bord, op het adres dat de console toont. Log in met je
beheerderswachtwoord.

## Brokerslots {#brokers}

In een slot staat één broker. De firmware begint met deze slots ingevuld:

| Slot | Broker | Beheerd door |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Een bord zonder extra geheugen (PSRAM), zoals de Heltec V3, heeft 3 slots.
Het verbindt met 2 ervan tegelijk, dus de Analyzer in slot 3 verbindt nooit.
Verplaats hem naar slot 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Een bord met PSRAM, zoals de Heltec V4, heeft 6 slots en verbindt met 5
tegelijk. Daar hoef je niets aan te veranderen.

Je node logt bij elke broker in met zijn eigen sleutel, dus je hebt geen
account nodig. Met `get mqtt.presets` zie je welke andere communitybrokers
de firmware kent.

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

Op een bord zonder PSRAM gebruik je slot 2: vervang `mqtt4` door `mqtt2`.
Je broker neemt dan de plaats in van `dutchmeshcore-2`.

Poort `8883` verbindt versleuteld (TLS), poort `443` versleuteld over een
webverbinding (websocket), en elke andere poort onversleuteld. Je kunt ook
het volledige adres opgeven, zoals `wss://mqtt.example.org:9002/mqtt`; dan
geldt de poortregel niet.

## Controleren of het werkt {#check}

Typ `get mqtt.status`. Elk slot toont zijn status:

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
  [Brokerslots](#brokers).

Zoek daarna de naam van je repeater op de
[observerpagina van de Analyzer](https://meshcore-analyzer.eu/#observers).
Hij verschijnt binnen 5 minuten, met wat hij heeft gehoord.
