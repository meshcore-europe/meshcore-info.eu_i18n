---
title: MQTT tavā novērotājā
lead: Ļauj savam retranslatoram, izmantojot Wi-Fi, ziņot MeshCore Analyzer par visu, ko tas dzird. Ziņojumus tas pārsūta tāpat kā līdz šim.
description: Pārvērt ESP32 retranslatoru par MeshCore novērotāju ar DMC novērotāja programmaparatūru. Ieraksti to platē, iestati Wi-Fi un lidostas kodu, izvēlies brokerus un pārbaudi, vai dati nonāk MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-11-02'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Novērotājs ir mezgls, kas par dzirdēto ziņo arī pa MQTT, izmantojot Wi-Fi. Ar katru novērotāju
[MeshCore Analyzer](https://meshcore-analyzer.eu/) un
[pārklājuma kartēs](/map/) redzama nedaudz lielāka mesh tīkla daļa. Šajā pamācībā tu pārvērt retranslatoru (mezglu, kas pārsūta ziņojumus) par novērotāju. Tas turpina pārsūtīt ziņojumus,
un dati plūst vienā virzienā: mesh tīklā nekas neatgriežas.

{{< callout type="warning" >}}
Šī pamācība attiecas uz **DMC novērotāja programmaparatūru**, proti,
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) novērotāja būvējumu,
kura pamatā ir MeshCore 1.18.0. Standarta MeshCore nav MQTT. Visas komandas tālāk
ir ņemtas no programmaparatūras pirmkoda, 2026. gada 19. oktobra būvējuma `32dd8ad`.
{{< /callout >}}

## Kas tev vajadzīgs {#need}

- ESP32 plate ar Wi-Fi, piemēram, Heltec V3 vai V4, LilyGo T3S3 vai
  Xiao S3. Visas plates ir uzskaitītas [laidienā](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev).
  nRF52 platēm, piemēram, RAK4631, nav Wi-Fi.
- 2.4 GHz Wi-Fi tīkls vietā, kur atrodas plate.
- USB datu kabelis un Chrome, Edge vai Opera tavā datorā.
- Tavam mezglam tuvākās lidostas kods no 3 burtiem, piemēram, `AMS` vai `BRU`.
  Tas norāda brokeriem (serveriem, kas saņem tavus datus), kurā apgabalā
  atrodas tavs novērotājs.

Vietā, kur stāv retranslators, nav Wi-Fi, bet blakus ir dators?
Tādā gadījumā [izveido tilta konfigurāciju](/guides/mctomqtt/).

## Ieraksti programmaparatūru {#flash}

Šīs vietnes [ierakstīšanas rīkā](/firmware/flasher/) ir tikai standarta MeshCore.
Novērotāja programmaparatūru tu atradīsi ierakstīšanas rīkā, kas ir
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/) daļa:

1. Izvēlies savu plati un pēc tam **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Pirmajā reizē izvēlies **Full flash**: tas aizstāj visu, kas ir platē,
   arī nodalījumu tabulu. Lietotnes atjauninājums saglabā to, kas platē jau ir,
   un ir paredzēts vēlākiem atjauninājumiem.
3. Iestati retranslatoru kā parasti: nosaukumu, radio iestatījumu komplektu un
   administratora paroli, kā aprakstīts [retranslatora pamācībā](/repeater-guide/#config).

Šī programmaparatūra ir **dev** būvējums, un, kad ievadi `ota update`, tā
atjauninās no dev kanāla. Stabilajā kanālā joprojām ir 1.17.1, tāpēc, sekojot šai
pamācībai, paliec dev kanālā.

## Iestatījumi {#settings}

Atver šīs vietnes [seriālo konsoli](/firmware/console/) un pievieno plati.
Ieraksti sava Wi-Fi tīkla nosaukumu, paroli un lidostas kodu, pēc tam ielīmē
šīs rindas pa vienai:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Pēc pārstartēšanas plate pievienojas tavam Wi-Fi tīklam un iestata pulksteni no
interneta. Brokeriem šis pulkstenis vajadzīgs, lai pārbaudītu tava novērotāja
identitāti. Bez lidostas koda plate neko nenosūta.

Labāk klikšķināt, nevis rakstīt? Komanda `start webconfig` atver platē iestatījumu lapu
adresē, ko parāda konsole. Piesakies ar savu administratora paroli.

## Brokeru sloti {#brokers}

Katrā slotā ir viens brokeris. Programmaparatūrā sākotnēji ir aizpildīti šādi sloti:

| Slots | Brokeris | Uztur |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Platei bez papildu atmiņas (PSRAM), piemēram, Heltec V3, ir 3 sloti. Vienlaikus
tā savienojas ar 2 no tiem, tāpēc Analyzer 3. slotā nekad neizveido savienojumu.
Pārvieto to uz 1. slotu:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Platei ar PSRAM, piemēram, Heltec V4, ir 6 sloti, un vienlaikus tā savienojas
ar 5. Šai platei nekas nav jāmaina.

Tavs mezgls katrā brokerī piesakās ar savu atslēgu, tāpēc konts tev nav vajadzīgs.
Komanda `get mqtt.presets` parāda pārējos kopienas brokerus, ko programmaparatūra zina.

### Tavs brokeris {#own}

Ieliec savu brokeri brīvā slotā. Ieraksti tā adresi, portu, lietotājvārdu un
paroli. Platē ar PSRAM brīvs ir 4. slots:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Platē bez PSRAM izmanto 2. slotu: aizstāj `mqtt4` ar `mqtt2`.
Tad tavs brokeris aizņem `dutchmeshcore-2` vietu.

Ar portu `8883` savienojums ir šifrēts (TLS), ar portu `443` tas ir šifrēts pa
tīmekļa savienojumu (websocket), bet ar jebkuru citu portu tas nav šifrēts.
Tu vari norādīt arī pilnu adresi, piemēram, `wss://mqtt.example.org:9002/mqtt`;
tad noteikums par portiem nav spēkā.

## Pārbaudi, vai viss darbojas {#check}

Ievadi `get mqtt.status`. Katram slotam redzams tā stāvoklis:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: savienojums ir izveidots.
- `wait`: slotam trūkst iestatījuma, piemēram, lidostas koda.
- `disc`: savienojuma vēl nav. Pārbaudi Wi-Fi ar `get wifi.status`.
- `fail`: slotam 7 reizes pēc kārtas neizdevās savienoties, aptuveni 20 minūšu laikā, un tagad
  tas mēģina vienu reizi 30 minūtēs. Pārbaudi brokera adresi un pieteikšanās datus.
- `inactive`: platē šim slotam nav vietas. Skati sadaļu
  [Brokeru sloti](#brokers).

Pēc tam meklē sava retranslatora nosaukumu
[Analyzer novērotāju lapā](https://meshcore-analyzer.eu/#observers).
5 minūšu laikā tas tur parādās kopā ar dzirdēto.
