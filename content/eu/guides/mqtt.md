---
title: MQTT zure behatzailean
lead: Zure errepikagailuak entzuten duena Wi-Fi bidez bidal diezaioke MeshCore Analyzer-i. Mezuak lehen bezala birbidaltzen jarraituko du.
description: Bihurtu ESP32 errepikagailu bat MeshCore behatzaile DMC observer firmwarearekin. Instalatu firmwarea, ezarri Wi-Fi sarea eta aireportu-kodea, aukeratu brokerrak eta egiaztatu datuak MeshCore Analyzer-era iristen direla.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-11-02'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Behatzailea (observer) entzuten duena MQTT bidez ere jakinarazten duen nodoa da, Wi-Fi erabilita.
Behatzaile bakoitzak mesh sarearen zati handixeagoa erakusten du
[MeshCore Analyzer](https://meshcore-analyzer.eu/) tresnan eta
[estaldura-mapetan](/map/). Gida honekin errepikagailu bat (mezuak birbidaltzen dituen nodoa)
behatzaile bihurtuko duzu. Errepikagailuak birbidaltzen jarraituko du, eta txostenak noranzko bakarrean doaz:
ez da ezer itzultzen mesh sarera.

{{< callout type="warning" >}}
Gida hau **DMC observer firmwarerako** da, hau da,
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) proiektuaren behatzaile-bertsiorako,
MeshCore 1.18.0 oinarri duena. MeshCore estandarrak ez du MQTT-rik. Beheko komando guztiak
firmwarearen iturburu-kodetik hartu ditugu, 2026ko urriaren 19ko `32dd8ad` konpilaziotik.
{{< /callout >}}

## Zer behar duzun {#need}

- Wi-Fi duen ESP32 plaka bat, adibidez Heltec V3 edo V4, LilyGo T3S3 edo
  Xiao S3. Plaka guztien zerrenda [argitalpenean](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  dago. nRF52 plakek, RAK4631 kasu, ez dute Wi-Firik.
- 2.4 GHz-eko Wi-Fi sare bat plaka dagoen tokian.
- Datuetarako USB kable bat, eta Chrome, Edge edo Opera zure ordenagailuan.
- Zure nodotik hurbilen dagoen aireportuaren kodea, 3 letrakoa, adibidez `AMS` edo `BRU`.
  Kode horrekin brokerrek (zure txostenak jasotzen dituzten zerbitzariek) badakite
  zure behatzailea zein eremutan dagoen.

Zure errepikagailua dagoen tokian Wi-Firik ez, baina ordenagailu bat ondoan?
Kasu horretan, [sortu zubi-konfigurazio bat](/guides/mctomqtt/).

## Instalatu firmwarea {#flash}

Webgune honetako [flasherrak](/firmware/flasher/) MeshCore estandarra baino ez dakar.
Behatzaile-firmwarea
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/) tresnako flasherrean dago:

1. Aukeratu zure plaka, eta ondoren **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Lehen aldian, aukeratu **Full flash**: plakan dagoen guztia ordezkatzen du,
   partizio-taula barne. Aplikazioaren eguneratzeak dagoena gordetzen du,
   eta geroko eguneratzeetarako da.
3. Konfiguratu errepikagailua ohi bezala: izena, irrati-aurrezarpena eta administratzaile-pasahitza,
   [errepikagailuaren gidan](/repeater-guide/#config) azaltzen den moduan.

Firmware hau **dev** konpilazioa da, eta `ota update` idazten duzunean dev kanaletik
eguneratzen da. Kanal egonkorrak 1.17.1 dakar oraindik, beraz, gida honetarako jarraitu dev kanalean.

## Ezarpenak {#settings}

Ireki webgune honetako [serieko kontsola](/firmware/console/) eta konektatu zure plaka.
Idatzi zure Wi-Fi sarea, pasahitza eta aireportu-kodea, eta itsatsi lerro hauek banan-banan:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Berrabiarazi ondoren, plaka zure Wi-Fi sarera konektatzen da eta erlojua internetetik doitzen du.
Brokerrek erloju hori behar dute zure behatzailea nor den egiaztatzeko. Aireportu-koderik gabe,
ez da ezer jakinarazten.

Idatzi beharrean klik egitea nahiago duzu? `start webconfig` komandoak ezarpen-orri bat irekitzen du plakan,
kontsolak erakusten duen helbidean. Hasi saioa zure administratzaile-pasahitzarekin.

## Broker-zirrikituak {#brokers}

Zirrikitu batek broker bat gordetzen du. Firmwarea zirrikitu hauek beteta dituela dator:

| Zirrikitua | Brokerra | Nork kudeatzen du |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Memoria gehigarririk (PSRAM) gabeko plakak, Heltec V3 kasu, 3 zirrikitu ditu. Horietako 2ra
konektatzen da aldi berean, beraz, 3. zirrikituko Analyzer ez da inoiz konektatzen.
Eraman 1. zirrikitura:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

PSRAM duen plakak, Heltec V4 kasu, 6 zirrikitu ditu eta 5era konektatzen da aldi berean.
Plaka horretan ez duzu ezer aldatu behar.

Zure nodoak bere gakoarekin hasten du saioa broker bakoitzean, beraz, ez duzu konturik behar.
`get mqtt.presets` komandoak firmwareak ezagutzen dituen gainerako komunitate-brokerrak zerrendatzen ditu.

### Zure broker propioa {#own}

Jarri zure broker propioa zirrikitu libre batean. Idatzi haren helbidea, ataka, erabiltzaile-izena eta
pasahitza. PSRAM duen plakan, 4. zirrikitua libre dago:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

PSRAM gabeko plakan, erabili 2. zirrikitua: `mqtt4` ordez, idatzi `mqtt2`.
Orduan zure brokerrak `dutchmeshcore-2` brokerraren lekua hartzen du.

`8883` atakak zifratuta konektatzen du (TLS), `443` atakak zifratuta web-konexio baten bidez (websocket),
eta beste edozein atakak zifratu gabe. Helbide osoa ere eman dezakezu, adibidez
`wss://mqtt.example.org:9002/mqtt`; kasu horretan, ataken arauak ez du balio.

## Egiaztatu funtzionatzen duela {#check}

Idatzi `get mqtt.status`. Zirrikitu bakoitzak bere egoera erakusten du:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: konektatuta.
- `wait`: zirrikituari ezarpen bat falta zaio, adibidez aireportu-kodea.
- `disc`: oraindik ez dago konektatuta. Egiaztatu zure Wi-Fi sarea `get wifi.status` komandoarekin.
- `fail`: zirrikituak 7 aldiz jarraian huts egin du, 20 minutu inguruan, eta orain
  30 minutuan behin saiatzen da. Egiaztatu brokerraren helbidea eta saio-hasierako datuak.
- `inactive`: plakak ez du lekurik zirrikitu honetarako. Ikus
  [Broker-zirrikituak](#brokers).

Ondoren, bilatu zure errepikagailuaren izena
[Analyzer-eko behatzaileen orrian](https://meshcore-analyzer.eu/#observers).
5 minutuko epean agertuko da, entzun duenarekin batera.
