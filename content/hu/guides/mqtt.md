---
title: MQTT a megfigyelődön
lead: Az átjátszód Wi-Fi-n jelentheti a MeshCore Analyzernek, amit hall. Közben továbbra is továbbítja az üzeneteket, mint eddig.
description: Így lesz egy ESP32 átjátszóból MeshCore megfigyelő a DMC observer firmware-rel. Flasheld fel, add meg a Wi-Fi-t és a repülőtérkódot, válaszd ki a brókereket, és ellenőrizd, hogy jelent a MeshCore Analyzernek.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-26'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
---

A megfigyelő olyan csomópont, amely MQTT-n, Wi-Fi-n keresztül azt is
jelenti, amit hall. Minden megfigyelő egy kicsit többet mutat a mesh-ből a
[MeshCore Analyzeren](https://meshcore-analyzer.eu/) és a
[lefedettségi térképeken](/map/). Ebben az útmutatóban egy átjátszót (egy
üzeneteket továbbító csomópontot) alakítasz megfigyelővé. Továbbra is
átjátszik, a jelentés pedig csak egy irányba megy: a mesh-be semmi nem kerül
vissza.

{{< callout type="warning" >}}
Ez az útmutató a **DMC observer firmware-hez** készült, ami a
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) megfigyelő
változata, a MeshCore 1.18.0 alapján. Az eredeti MeshCore-ban nincs MQTT. Az
alábbi parancsok mindegyike a firmware forráskódjából származik, a 2026.
október 19-i `32dd8ad` buildből.
{{< /callout >}}

## Amire szükséged van {#need}

- Egy Wi-Fi-s ESP32 lap, például Heltec V3 vagy V4, LilyGo T3S3 vagy
  Xiao S3. A [kiadás](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  felsorolja az összes lapot. Az nRF52 lapokban, például a RAK4631-ben, nincs Wi-Fi.
- Egy 2.4 GHz-es Wi-Fi hálózat ott, ahol a lap áll.
- Egy USB adatkábel, valamint Chrome, Edge vagy Opera a számítógépeden.
- A csomópontodhoz legközelebbi repülőtér kódja, 3 betű, például `AMS` vagy `BRU`.
  Ez mondja meg a brokereknek (a jelentéseidet fogadó szervereknek), melyik
  területen van a megfigyelőd.

Nincs Wi-Fi ott, ahol az átjátszód áll, de van mellette számítógép?
Akkor inkább [építs egy híd konfigurációt](/guides/mctomqtt/).

## A firmware felflashelése {#flash}

Az oldal [flashere](/firmware/flasher/) csak az eredeti MeshCore-t
tartalmazza. A megfigyelő firmware-t a
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/) flasheréből
kapod:

1. Válaszd ki a kártyádat, majd a **DutchMeshCore MQTT** opciót (Repeater +
   Observer + MQTT).
2. Első alkalommal a **Full flash** opciót válaszd: ez mindent felülír a
   kártyán, a partíciós táblát is. Az app update megtartja, ami a kártyán
   van, és a későbbi frissítésekre való.
3. Állítsd be az átjátszódat a megszokott módon: név, rádiós előbeállítás és
   admin jelszó, ahogy az [átjátszó útmutatóban](/repeater-guide/#config) is
   áll.

Ez a firmware a **dev** build, és a dev csatornáról frissíti magát, amikor
beírod az `ota update` parancsot. A stabil csatornán még az 1.17.1 van, ezért
ehhez az útmutatóhoz maradj a dev csatornán.

## Beállítások {#settings}

Nyisd meg az oldal [soros konzolját](/firmware/console/), és csatlakoztasd a
kártyádat. Írd be a saját Wi-Fi hálózatodat, jelszavadat és repülőtérkódodat,
majd illeszd be ezeket a sorokat egyenként:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Az újraindítás után a kártya csatlakozik a Wi-Fi-dre, és az internetről
állítja be az óráját. A brókereknek ez az óra kell ahhoz, hogy ellenőrizzék,
ki a megfigyelőd. Repülőtérkód nélkül semmi nem kerül jelentésre.

Inkább kattintanál, mint gépelnél? A `start webconfig` parancs beállítási
oldalt nyit a kártyán, a konzolban megjelenő címen. Az admin jelszavaddal
jelentkezz be.

## Brókerhelyek {#brokers}

Egy hely egy brókert tárol. A firmware ezekkel az előre kitöltött helyekkel
indul:

| Hely | Bróker | Üzemelteti |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Egy extra memória (PSRAM) nélküli kártyának, például a Heltec V3-nak, 3 helye
van. Egyszerre 2-hez csatlakozik, ezért a 3. helyen lévő Analyzer soha nem
kapcsolódik. Tedd át az 1. helyre:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Egy PSRAM-os kártyának, például a Heltec V4-nek, 6 helye van, és egyszerre
5-höz csatlakozik. Ezen nem kell változtatni.

A csomópontod a saját kulcsával jelentkezik be minden brókerre, így nem kell
fiók. A `get mqtt.presets` parancs kilistázza a firmware által ismert többi
közösségi brókert.

### Saját bróker {#own}

A saját brókeredet egy szabad helyre tedd. Add meg a címét, portját,
felhasználónevét és jelszavát. PSRAM-os kártyán a 4. hely szabad:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

PSRAM nélküli kártyán a 2. helyet használd: írj `mqtt4` helyett `mqtt2`-t. A
brókered ekkor a `dutchmeshcore-2` helyére kerül.

A `8883` port titkosítva (TLS) csatlakozik, a `443` port titkosítva webes
kapcsolaton (websocket), minden más port titkosítás nélkül. Megadhatod a
teljes címet is, például `wss://mqtt.example.org:9002/mqtt`; ekkor a
portszabály nem érvényes.

## Működés ellenőrzése {#check}

Írd be a `get mqtt.status` parancsot. Minden hely mutatja az állapotát:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: csatlakozva.
- `wait`: a helyről hiányzik egy beállítás, például a repülőtérkód.
- `disc`: még nincs csatlakozva. Ellenőrizd a Wi-Fi-t a `get wifi.status`
  paranccsal.
- `fail`: a hely 7-szer hibázott egymás után, körülbelül 20 perc alatt, és
  most 30 percenként próbálkozik. Ellenőrizd a bróker címét és a belépési
  adatokat.
- `inactive`: a kártyán nincs hely ennek a brókernek. Lásd:
  [Brókerhelyek](#brokers).

Ezután keresd meg az átjátszód nevét az
[Analyzer megfigyelők oldalán](https://meshcore-analyzer.eu/#observers).
5 percen belül megjelenik, azzal együtt, amit hallott.
