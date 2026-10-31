---
title: MQTT op dyn observer
lead: Lit dyn repeater fia Wi-Fi oan de MeshCore Analyzer trochjaan wat er heart. Hy stjoert berjochten gewoan troch lykas earder.
description: Meitsje fan in ESP32-repeater in MeshCore-observer mei de DMC-observerfirmware. Flash him, stel Wi-Fi en dyn fleanfjildkoade yn, kies de brokers en kontrolearje oft er oan de MeshCore Analyzer rapportearret.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-31'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

In observer is in node dy't fia Wi-Fi ek oer MQTT trochjout wat er heart.
Elke observer lit op de [MeshCore Analyzer](https://meshcore-analyzer.eu/)
en op de [dekkingskaarten](/map/) wat mear fan it mesh sjen. Mei dizze
hantlieding meitsjest do fan in repeater (in node dy't berjochten trochstjoert)
in observer. Hy bliuwt trochstjoeren, en it rapport giet ien kant út: der
komt neat werom op it mesh.

{{< callout type="warning" >}}
Dizze hantlieding is foar de **DMC-observerfirmware**, de observerbou fan
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), basearre op
MeshCore 1.18.0. Standert MeshCore hat gjin MQTT. Elk kommando hjirûnder
komt út de boarnekoade fan de firmware, bou `32dd8ad` fan 19 oktober 2026.
{{< /callout >}}

## Wat do nedich hast {#need}

- In ESP32-board mei Wi-Fi, lykas in Heltec V3 of V4, in LilyGo T3S3 of in
  Xiao S3. Yn de [release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  stiet elk board. nRF52-boards lykas de RAK4631 hawwe gjin Wi-Fi.
- In Wi-Fi-netwurk fan 2.4 GHz op it plak dêr't it board stiet.
- In USB-datakabel, en Chrome, Edge of Opera op dyn kompjûter.
- De fleanfjildkoade it tichtst by dyn node, 3 letters lykas `AMS` of `BRU`.
  Dêrmei witte de brokers (de servers dy't dyn rapporten ûntfange) yn hokker
  gebiet dyn observer stiet.

Hast gjin Wi-Fi by dyn repeater, mar wol in kompjûter dêrnêst?
[Meitsje dan in bridge-konfiguraasje](/guides/mctomqtt/).

## De firmware flashe {#flash}

De [flasher](/firmware/flasher/) op dizze side hat allinnich standert MeshCore.
De observerfirmware hellest do út de flasher yn de
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Kies dyn board en dan **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Kies de earste kear **Full flash**: dat ferfangt alles op it board, ek de
   partysjetabel. De app-update hâldt wat der stiet en is foar lettere updates.
3. Stel dyn repeater yn lykas altyd: namme, radiopreset en adminwachtwurd, as
   yn de [repeaterhantlieding](/repeater-guide/#config).

Dizze firmware is de **dev**-bou. Hy fernijt himsels út it dev-kanaal as
do `ota update` typest. It stabile kanaal hat noch 1.17.1, dus bliuw foar
dizze hantlieding op dev.

## Ynstellingen {#settings}

Iepenje de [seriële konsole](/firmware/console/) op dizze side en ferbyn dyn
board. Folje dyn eigen Wi-Fi-netwurk, wachtwurd en fleanfjildkoade yn. Plak
dêrnei dizze rigels ien foar ien:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Nei de herstart ferbynt it board mei dyn Wi-Fi en set it syn klok gelyk fia it
ynternet. De brokers hawwe dy klok nedich om te kontrolearjen wa't dyn observer
is. Sûnder fleanfjildkoade wurdt der neat rapportearre.

Klikst leaver as datst typest? Mei `start webconfig` iepenest in
ynstellingsside op it board, op it adres dat de konsole sjen lit. Meld dy oan
mei dyn adminwachtwurd.

## Brokerslots {#brokers}

Yn in slot stiet ien broker. Standert hat de firmware dizze slots ynfolle:

| Slot | Broker | Beheard troch |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

In board sûnder ekstra ûnthâld (PSRAM), lykas de Heltec V3, hat 3 slots. It
makket mei 2 dêrfan tagelyk ferbining, dus de Analyzer yn slot 3 kriget nea ferbining.
Ferpleats him nei slot 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

In board mei PSRAM, lykas de Heltec V4, hat 6 slots en ferbynt mei 5 tagelyk.
Dêr hoechst neat te feroarjen.

Dyn node meldt him by elke broker oan mei in eigen kaai, dus do hast gjin
akkount nedich. Mei `get mqtt.presets` sjochst de oare mienskipsbrokers dy't de
firmware ken.

### Dyn eigen broker {#own}

Set dyn eigen broker yn in frij slot. Folje it adres, de poarte, de
brûkersnamme en it wachtwurd yn. Op in board mei PSRAM is slot 4 frij:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Brûk op in board sûnder PSRAM ynstee slot 2: ferfang `mqtt4` troch `mqtt2`.
Dyn broker komt dan op it plak fan `dutchmeshcore-2`.

Poarte `8883` ferbynt fersifere (TLS), poarte `443` fersifere oer in
webferbining (websocket), en elke oare poarte sûnder fersifering. Do kinst ek it
folsleine adres opjaan, lykas `wss://mqtt.example.org:9002/mqtt`. Dan jildt de
poarteregel net.

## Kontrolearje oft it wurket {#check}

Typ `get mqtt.status`. Elk slot lit syn status sjen:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: ferbûn.
- `wait`: it slot mist in ynstelling, lykas de fleanfjildkoade.
- `disc`: noch net ferbûn. Kontrolearje dyn Wi-Fi mei `get wifi.status`.
- `fail`: it slot is 7 kear efterinoar mislearre, oer sa'n 20 minuten, en
  besiket it no ien kear yn de 30 minuten. Kontrolearje it adres en de
  oanmelding fan de broker.
- `inactive`: it board hat gjin romte foar dit slot. Sjoch
  [Brokerslots](#brokers).

Sykje dêrnei de namme fan dyn repeater op de
[observersside fan de Analyzer](https://meshcore-analyzer.eu/#observers).
Binnen 5 minuten stiet er der, mei wat er heard hat.
