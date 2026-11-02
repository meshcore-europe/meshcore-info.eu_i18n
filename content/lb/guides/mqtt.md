---
title: MQTT op dengem Observer
lead: Looss däi Repeater iwwer Wi-Fi un de MeshCore Analyzer mellen, wat en héiert. Hie gëtt d'Noriichte weider wéi virdrun.
description: Maach aus engem ESP32-Repeater e MeshCore-Observer mat der DMC-Observer-Firmware. Flash se, stell Wi-Fi an däi Fluchhafcode an, wiel d'Brokeren a kontrolléier, ob en un de MeshCore Analyzer mellt.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-11-02'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

En Observer ass e Knuet, deen och mellt, wat en héiert, an dat iwwer MQTT, via
Wi-Fi. All Observer weist e bësse méi vum Mesh um
[MeshCore Analyzer](https://meshcore-analyzer.eu/) an op den
[Ofdeckungskaarten](/map/). Mat dësem Guide méchs du aus engem Repeater (e
Knuet, deen Noriichte weidergëtt) en Observer. Hie bleift weider e Repeater, an
de Rapport geet nëmmen an eng Richtung: näischt kënnt zréck op de Mesh.

{{< callout type="warning" >}}
Dëse Guide ass fir d'**DMC observer firmware**, d'Observer-Versioun vu
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), op Basis vu
MeshCore 1.18.0. D'Standard-MeshCore huet kee MQTT. All Kommando hei drënner ass
aus dem Quellcode vun der Firmware erausgelies, Build `32dd8ad` vum 19. Oktober 2026.
{{< /callout >}}

## Wat s du brauchs {#need}

- En ESP32-Board mat Wi-Fi, wéi en Heltec V3 oder V4, e LilyGo T3S3 oder e
  Xiao S3. An der [Release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  stinn all Boards. nRF52-Boards wéi de RAK4631 hu kee Wi-Fi.
- E Wi-Fi-Netz op 2.4 GHz do, wou de Board steet.
- En USB-Datekabel, a Chrome, Edge oder Opera op dengem Computer.
- De Code vum Fluchhafen, deen am nootste bei dengem Knuet läit, 3 Buschtawe wéi `AMS` oder `BRU`.
  Domat wëssen d'Brokeren (d'Serveren, déi deng Rapporte kréien), a wéi
  enger Regioun däin Observer steet.

Kee Wi-Fi do, wou däi Repeater steet, mee e Computer dernieft?
[Bau dann amplaz eng Bridge-Config](/guides/mctomqtt/).

## D'Firmware flashen {#flash}

De [Flasher](/firmware/flasher/) op dësem Site huet nëmmen d'Standard-MeshCore.
D'Observer-Firmware kriss du iwwer de Flasher an der
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Wiel däi Board an duerno **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Wiel déi éischte Kéier **Full flash**: dat ersetzt alles um Board, och
   d'Partitiounstabell. Den App-Update behält, wat do ass, an ass fir spéider Updates.
3. Riicht däi Repeater wéi gewinnt an: Numm, Radio-Preset an Admin-Passwuert, wéi
   am [Repeater-Guide](/repeater-guide/#config).

Dës Firmware ass de **dev**-Build an aktualiséiert sech vum dev-Kanal, wann s du
`ota update` tipps. De stabile Kanal huet nach ëmmer 1.17.1, also bleif fir dëse
Guide op dev.

## Astellungen {#settings}

Maach d'[seriell Konsol](/firmware/console/) op dësem Site op a verbann däi Board.
Gëff däin eegent Wi-Fi-Netz, däi Passwuert an de Code vum Fluchhafen an, a fëg dës
Zeilen eng no der anerer an:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Nom Reboot verbënnt sech de Board mat dengem Wi-Fi a stellt seng Auer iwwer den Internet. D'Brokere
brauchen déi Auer, fir ze préiwen, wien däin Observer ass. Ouni Fluchhafecode gëtt
näischt gemellt.

Léiwer klicke wéi tippen? `start webconfig` mécht eng Astellungssäit um Board
op, op der Adress, déi d'Konsol weist. Mell dech mat dengem Admin-Passwuert un.

## Broker-Slots {#brokers}

An engem Slot ass ee Broker. An der Firmware sinn dës Slots am Ufank ausgefëllt:

| Slot | Broker | Bedriwwe vun |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

E Board ouni extra Späicher (PSRAM), wéi den Heltec V3, huet 3 Slots. Hie
verbënnt sech gläichzäiteg mat 2 dovun, dofir kritt den Analyzer am Slot 3 ni eng Verbindung.
Réck en an de Slot 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

E Board mat PSRAM, wéi den Heltec V4, huet 6 Slots a verbënnt sech gläichzäiteg mat
5. Do muss du näischt änneren.

Däi Knuet mellt sech bei all Broker mat sengem eegene Schlëssel un, also brauchs du
kee Kont. `get mqtt.presets` lëscht déi aner Community-Brokeren op, déi d'Firmware kennt.

### Däin eegene Broker {#own}

Setz däin eegene Broker an e fräie Slot. Gëff seng Adress, säi Port, säi
Benotzernumm a säi Passwuert an. Op engem Board mat PSRAM ass de Slot 4 fräi:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Op engem Board ouni PSRAM huel amplaz de Slot 2: ersetz `mqtt4` duerch `mqtt2`.
Däi Broker hëlt dann d'Plaz vun `dutchmeshcore-2`.

Port `8883` verbënnt verschlësselt (TLS), Port `443` verschlësselt iwwer eng
Webverbindung (websocket), an all anere Port onverschlësselt. Du kanns och déi ganz
Adress uginn, wéi `wss://mqtt.example.org:9002/mqtt`; da gëllt d'Port-Regel net.

## Kontrolléieren, ob et funktionéiert {#check}

Tipp `get mqtt.status`. All Slot weist säin Zoustand:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: verbonnen.
- `wait`: dem Slot feelt eng Astellung, wéi de Fluchhafecode.
- `disc`: nach net verbonnen. Kontrolléier däi Wi-Fi mat `get wifi.status`.
- `fail`: de Slot ass 7 Mol hannereneen ausgefall, bannent ongeféier 20 Minutten, a
  probéiert elo eemol all 30 Minutten. Kontrolléier d'Adress an de Login vum Broker.
- `inactive`: de Board huet keng Plaz fir dëse Slot. Kuck
  [Broker-Slots](#brokers).

Sich duerno den Numm vun dengem Repeater op der
[Observer-Säit vum Analyzer](https://meshcore-analyzer.eu/#observers).
En daucht bannent 5 Minutten do op, mat deem, wat en héieren huet.
