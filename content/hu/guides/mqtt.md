---
title: MQTT az observereden
lead: A repeatered Wi-Fin keresztül jelenti a MeshCore Analyzernek, amit hall. Közben ugyanúgy továbbítja az üzeneteket, mint eddig.
description: A DMC observer firmware-rel egy ESP32-es átjátszóból MeshCore observert csinálsz. Flasheld, add meg a Wi-Fit és a reptérkódodat, válaszd ki a brokereket, és ellenőrizd, hogy jelent-e a MeshCore Analyzernek.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-31'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Az observer olyan csomópont, amely azt is jelenti MQTT-n, amit hall, Wi-Fin
keresztül. Minden observer egy kicsit többet mutat meg a mesh-ből a
[MeshCore Analyzeren](https://meshcore-analyzer.eu/) és a
[lefedettségi térképeken](/map/). Ebben az útmutatóban egy átjátszóból
(egy csomópontból, amely továbbadja az üzeneteket) observert csinálsz.
Az átjátszó továbbra is továbbít, a jelentés pedig egyirányú: semmi sem
jut vissza a mesh-re.

{{< callout type="warning" >}}
Ez az útmutató a **DMC observer firmware**-hez készült. Ez a
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) observer
változata, és a MeshCore 1.18.0-ra épül. A gyári MeshCore-ban nincs MQTT.
Az alábbi parancsokat a firmware forráskódjából vettük, a 2026. október 19-i
`32dd8ad` buildből.
{{< /callout >}}

## Amire szükséged lesz {#need}

- Egy Wi-Fis ESP32 lap, például Heltec V3 vagy V4, LilyGo T3S3 vagy
  Xiao S3. A [kiadás](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  felsorolja az összes lapot. Az nRF52 lapokon, például a RAK4631-en, nincs Wi-Fi.
- Egy 2.4 GHz-es Wi-Fi hálózat ott, ahol a lap áll.
- Egy USB adatkábel, és Chrome, Edge vagy Opera a számítógépeden.
- A csomópontodhoz legközelebbi repülőtér kódja, 3 betű, például `AMS` vagy `BRU`.
  Ebből tudják a brokerek (a szerverek, amelyek fogadják a jelentéseidet),
  melyik területen van az observered.

Nincs Wi-Fi ott, ahol az átjátszód áll, de van mellette egy számítógép?
Akkor inkább [készíts egy bridge konfigurációt](/guides/mctomqtt/).

## A firmware flashelése {#flash}

Az oldalunkon lévő [flasher](/firmware/flasher/) csak a gyári MeshCore-t
tudja feltenni. Az observer firmware-t a
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/) flasherével
teszed fel:

1. Válaszd ki a lapodat, majd a **DutchMeshCore MQTT** (Repeater + Observer + MQTT) lehetőséget.
2. Először a **Full flash** opciót válaszd: ez mindent lecserél a lapon, a
   partíciós táblát is. Az app update megtartja, ami már fent van, ezt a
   későbbi frissítésekhez használd.
3. Állítsd be az átjátszódat a szokásos módon: nevet, rádiós presetet és
   admin jelszót, ahogy az [átjátszó-útmutatóban](/repeater-guide/#config) olvasod.

Ez a firmware a **dev** build. Ha begépeled az `ota update` parancsot, a dev
csatornáról frissíti magát. A stable csatornán még az 1.17.1 van, ezért ehhez
az útmutatóhoz maradj a dev csatornán.

## Beállítások {#settings}

Nyisd meg az oldalunkon a [soros konzolt](/firmware/console/), és csatlakoztasd
a lapodat. Írd be a saját Wi-Fi-hálózatodat, jelszavadat és reptérkódodat,
aztán egyenként másold be ezeket a sorokat:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Újraindítás után a lap csatlakozik a Wi-Fidhez, és az internetről beállítja
az óráját. A brokereknek erre az órára van szükségük, hogy ellenőrizzék, ki
az observered. Reptérkód nélkül semmit sem jelent.

Inkább kattintanál, mint gépelnél? A `start webconfig` paranccsal megnyitsz
egy beállítóoldalt a lapon, azon a címen, amelyet a konzol kiír. Az admin
jelszavaddal lépj be.

## Broker-helyek {#brokers}

Egy hely egy brokert tárol. A firmware ezekkel a kitöltött helyekkel indul:

| Hely | Broker | Üzemelteti |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Az extra memória (PSRAM) nélküli lapokon, például a Heltec V3-on, 3 hely van.
Ezek közül egyszerre 2-höz kapcsolódik a lap, így a 3. helyen lévő Analyzerhez
sosem. Tedd át az 1. helyre:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

A PSRAM-mal rendelkező lapokon, például a Heltec V4-en, 6 hely van, és a lap
egyszerre 5-höz kapcsolódik. Itt nem kell semmit módosítanod.

A csomópontod a saját kulcsával lép be minden brokerhez, ezért nem kell fiók.
A `get mqtt.presets` kilistázza a többi közösségi brokert, amelyet a firmware ismer.

### Saját broker {#own}

A saját brokeredet egy szabad helyre teheted. Add meg a címét, portját,
felhasználónevét és jelszavát. PSRAM-os lapon a 4. hely szabad:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

PSRAM nélküli lapon inkább a 2. helyet használd: az `mqtt4` helyére írj
`mqtt2`-t. A brokered így a `dutchmeshcore-2` helyére kerül.

A `8883`-as port titkosítva (TLS) kapcsolódik, a `443`-as titkosítva, webes
kapcsolaton (websocketen) át, minden más port titkosítás nélkül. A teljes
címet is megadhatod, például `wss://mqtt.example.org:9002/mqtt`. Ekkor a
portszabály nem érvényes.

## Ellenőrzés {#check}

Írd be: `get mqtt.status`. Minden hely kiírja az állapotát:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: kapcsolódva.
- `wait`: a helyről hiányzik egy beállítás, például a reptérkód.
- `disc`: még nincs kapcsolat. A Wi-Fit a `get wifi.status` paranccsal ellenőrizd.
- `fail`: a hely 7-szer egymás után hibázott, nagyjából 20 perc alatt, és
  most 30 percenként egyszer próbálkozik. Ellenőrizd a broker címét és a
  belépési adatokat.
- `inactive`: a lapon nincs hely ehhez a helyhez. Lásd:
  [Broker-helyek](#brokers).

Aztán keresd meg az átjátszód nevét az
[Analyzer observers oldalán](https://meshcore-analyzer.eu/#observers).
5 percen belül megjelenik, azzal együtt, amit hallott.
