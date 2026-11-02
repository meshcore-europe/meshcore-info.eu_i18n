---
title: MQTT fuq l-observer tiegħek
lead: Ħalli r-repeater tiegħek jirrapporta dak li jisma' lill-MeshCore Analyzer permezz tal-Wi-Fi. Ir-repeater ikompli jgħaddi l-messaġġi bħal qabel.
description: Ibdel repeater ESP32 f'observer ta' MeshCore bil-firmware DMC observer. Agħmel il-flash, issettja l-Wi-Fi u l-kodiċi tal-ajruport, agħżel il-brokers u ċċekkja li r-rapporti jaslu għand il-MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-11-02'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Observer huwa node li jirrapporta wkoll dak li jisma' fuq MQTT, permezz tal-Wi-Fi. Kull observer juri ftit iktar mill-mesh fuq il-[MeshCore Analyzer](https://meshcore-analyzer.eu/) u fuq il-[mapep tal-kopertura](/map/). B'din il-gwida tibdel repeater (node li jgħaddi l-messaġġi) f'observer. Ir-repeater ikompli jgħaddi l-messaġġi, u r-rapport imur f'direzzjoni waħda: xejn ma jerġa' lura fuq il-mesh.

{{< callout type="warning" >}}
Din il-gwida hija għall-**firmware DMC observer**, il-build observer ta' [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), ibbażat fuq MeshCore 1.18.0. MeshCore standard m'għandux MQTT. Qrajna kull kmand hawn taħt mis-sors tal-firmware, fil-build `32dd8ad` tad-19 ta' Ottubru 2026.
{{< /callout >}}

## X'għandek bżonn {#need}

- Bord ESP32 bil-Wi-Fi, bħal Heltec V3 jew V4, LilyGo T3S3 jew Xiao S3. Il-[release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev) telenka kull bord. Bordijiet nRF52 bħar-RAK4631 m'għandhomx Wi-Fi.
- Netwerk Wi-Fi ta' 2.4 GHz fejn ikun il-bord.
- Kejbil USB tad-data, u Chrome, Edge jew Opera fuq il-kompjuter tiegħek.
- Il-kodiċi tal-eqreb ajruport lejn in-node tiegħek, 3 ittri bħal `AMS` jew `BRU`. Bih il-brokers (is-servers li jirċievu r-rapporti tiegħek) ikunu jafu f'liema żona jinsab l-observer tiegħek.

M'hemmx Wi-Fi fejn hemm ir-repeater tiegħek, imma għandek kompjuter ħdejh? [Ibni konfigurazzjoni ta' bridge](/guides/mctomqtt/) minflok.

## Agħmel il-flash tal-firmware {#flash}

Il-[flasher](/firmware/flasher/) fuq dan is-sit fih MeshCore standard biss. Il-firmware observer issibu fil-flasher tad-[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Agħżel il-bord tiegħek, imbagħad **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Agħżel **Full flash** l-ewwel darba: dan jibdel kollox fuq il-bord, inkluża t-tabella tal-partizzjonijiet. L-app update iżomm dak li hemm u huwa għall-aġġornamenti ta' wara.
3. Ikkonfigura r-repeater tiegħek bħas-soltu: l-isem, il-preset tar-radju u l-password tal-admin, kif tgħid il-[gwida tar-repeater](/repeater-guide/#config).

Dan il-firmware huwa l-build **dev** u jaġġorna lilu nnifsu mill-kanal dev meta tikteb `ota update`. Il-kanal stable għadu fuq 1.17.1, għalhekk ibqa' fuq dev għal din il-gwida.

## Is-settings {#settings}

Iftaħ il-[console serjali](/firmware/console/) fuq dan is-sit u qabbad il-bord tiegħek. Daħħal in-netwerk Wi-Fi, il-password u l-kodiċi tal-ajruport tiegħek, imbagħad waħħal dawn il-linji waħda waħda:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Wara r-reboot, il-bord jikkonnettja mal-Wi-Fi tiegħek u jirregola l-arloġġ tiegħu mill-internet. Il-brokers għandhom bżonn dak l-arloġġ biex jivverifikaw min hu l-observer tiegħek. Mingħajr kodiċi tal-ajruport, ma jintbagħat ebda rapport.

Tippreferi tikklikkja milli tikteb? `start webconfig` jiftaħ paġna tas-settings fuq il-bord, fl-indirizz li turi l-console. Idħol bil-password tal-admin tiegħek.

## Is-slots tal-brokers {#brokers}

Kull slot iżomm broker wieħed. Il-firmware jibda b'dawn is-slots diġà mimlija:

| Slot | Broker | Min imexxih |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Bord mingħajr memorja żejda (PSRAM), bħall-Heltec V3, għandu 3 slots. Jikkonnettja ma' 2 minnhom fl-istess ħin, għalhekk l-Analyzer fis-slot 3 qatt ma jikkonnettja. Ċaqilqu għas-slot 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Bord bil-PSRAM, bħall-Heltec V4, għandu 6 slots u jikkonnettja ma' 5 fl-istess ħin. Ma jeħtieġ ebda bidla.

In-node tiegħek jidħol f'kull broker biċ-ċavetta tiegħu, għalhekk ma għandekx bżonn kont. `get mqtt.presets` jelenka l-brokers l-oħra tal-komunità li l-firmware jaf bihom.

### Il-broker tiegħek {#own}

Poġġi l-broker tiegħek f'slot vojt. Daħħal l-indirizz, il-port, l-username u l-password tiegħu. Fuq bord bil-PSRAM, is-slot 4 huwa vojt:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Fuq bord mingħajr PSRAM, uża s-slot 2 minflok: ibdel `mqtt4` b'`mqtt2`. Il-broker tiegħek imbagħad jieħu post `dutchmeshcore-2`.

Il-port `8883` jikkonnettja b'mod ikkriptat (TLS), il-port `443` b'mod ikkriptat fuq konnessjoni web (websocket), u kull port ieħor mingħajr kriptaġġ. Tista' tagħti wkoll l-indirizz sħiħ, bħal `wss://mqtt.example.org:9002/mqtt`; f'dak il-każ ir-regola tal-port ma tapplikax.

## Iċċekkja li jaħdem {#check}

Ikteb `get mqtt.status`. Kull slot juri l-istat tiegħu:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: ikkonnettjat.
- `wait`: lis-slot jonqsu setting, bħall-kodiċi tal-ajruport.
- `disc`: għadu mhux ikkonnettjat. Iċċekkja l-Wi-Fi tiegħek b'`get wifi.status`.
- `fail`: is-slot falla 7 darbi wara xulxin, f'madwar 20 minuta, u issa jipprova darba kull 30 minuta. Iċċekkja l-indirizz u d-dettalji tal-login tal-broker.
- `inactive`: il-bord m'għandux spazju għal dan is-slot. Ara [Is-slots tal-brokers](#brokers).

Imbagħad fittex l-isem tar-repeater tiegħek fuq il-[paġna tal-observers tal-Analyzer](https://meshcore-analyzer.eu/#observers). Jidher fi żmien 5 minuti, flimkien ma' dak li sema'.
