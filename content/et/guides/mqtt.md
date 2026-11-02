---
title: MQTT sinu vaatlejal
lead: Lase oma kordajal Wi-Fi kaudu MeshCore Analyzerile teatada, mida ta kuuleb. Sõnumeid edastab ta edasi nagu varem.
description: Tee ESP32 kordajast DMC observer firmware abil MeshCore'i vaatleja. Paigalda püsivara, seadista Wi-Fi ja lennujaama kood, vali brokerid ja kontrolli, kas MeshCore Analyzer teateid saab.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-11-02'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Vaatleja on sõlm, mis annab MQTT kaudu teada ka sellest, mida ta kuuleb. Teated liiguvad Wi-Fi kaudu. Iga vaatlejaga on
[MeshCore Analyzeris](https://meshcore-analyzer.eu/) ja
[levikaartidel](/map/) näha veidi rohkem võrku. Selle juhendiga teed vaatleja kordajast (sõlmest,
mis saadab sõnumeid edasi). Kordaja jätkab edastamist ja teated liiguvad ainult
ühes suunas: võrku ei tule midagi tagasi.

{{< callout type="warning" >}}
See juhend on mõeldud **DMC observer firmware** jaoks. See on
[Dutch-MeshCore'i](https://github.com/Dutch-MeshCore/MeshCore) vaatlejaversioon,
mis põhineb MeshCore 1.18.0-l. Tavalisel MeshCore'il MQTT-d ei ole. Kõik allpool
toodud käsud on loetud püsivara lähtekoodist, 19. oktoobri 2026. aasta versioonist
`32dd8ad`.
{{< /callout >}}

## Mida vajad {#need}

- ESP32-plaati, millel on Wi-Fi, näiteks Heltec V3 või V4, LilyGo T3S3 või
  Xiao S3. Kõik plaadid leiad [väljalaskelehelt](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev).
  nRF52-plaatidel, näiteks RAK4631-l, Wi-Fi puudub.
- 2.4 GHz Wi-Fi-võrku kohas, kus plaat asub.
- USB-andmekaablit ning arvutis Chrome'i, Edge'i või Operat.
- Sõlmele lähima lennujaama koodi: 3 tähte, näiteks `AMS` või `BRU`.
  Selle järgi teavad brokerid (serverid, mis sinu teated vastu võtavad),
  millises piirkonnas sinu vaatleja asub.

Kordaja juures pole Wi-Fi-t, aga selle kõrval on arvuti?
[Koosta hoopis sillaseadistus](/guides/mctomqtt/).

## Paigalda püsivara {#flash}

Selle saidi [paigaldustööriist](/firmware/flasher/) sisaldab ainult tavalist
MeshCore'i. Vaatleja püsivara saad
[DutchMeshCore Toolboxi](https://toolbox.dutchmeshcore.nl/) paigaldustööriistast:

1. Vali oma plaat ja seejärel **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Esimesel korral vali **Full flash**: see asendab plaadil kõik, ka
   partitsioonitabeli. Rakenduse uuendus jätab olemasoleva alles ja on mõeldud
   hilisemateks uuendusteks.
3. Seadista kordaja nagu tavaliselt: nimi, raadio eelseadistus ja
   administraatori parool, nagu on kirjas [kordaja juhendis](/repeater-guide/#config).

See püsivara on **dev**-versioon. Kui sisestad `ota update`, uuendab see end
dev-kanalist. Stabiilses kanalis on endiselt 1.17.1, seega jää selle juhendi
jaoks dev-kanalile.

## Seaded {#settings}

Ava selle saidi [jadakonsool](/firmware/console/) ja ühenda plaat. Kirjuta
käskudesse oma Wi-Fi-võrk, parool ja lennujaama kood. Seejärel kleebi read
ükshaaval konsooli:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Pärast taaskäivitust liitub plaat sinu Wi-Fi-võrguga ja seab kella interneti
järgi. Seda kella on brokeritel vaja, et kontrollida, kes sinu vaatleja on.
Ilma lennujaama koodita ei lähe ükski teade teele.

Eelistad klõpsimist trükkimisele? Käsk `start webconfig` avab plaadil
seadete lehe aadressil, mille konsool sulle näitab. Logi sisse oma
administraatori parooliga.

## Brokeri pesad {#brokers}

Ühes pesas on üks broker. Püsivaras on algselt täidetud need pesad:

| Pesa | Broker | Haldaja |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Ilma lisamäluta (PSRAM) plaadil, näiteks Heltec V3-l, on 3 pesa. Selline plaat
ühendub korraga 2 pesaga, seega ei saa pesas 3 olev Analyzer kunagi ühendust.
Tõsta see pessa 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

PSRAM-iga plaadil, näiteks Heltec V4-l, on 6 pesa ja see ühendub korraga 5-ga.
Sellisel plaadil pole muudatust vaja.

Sinu sõlm logib igasse brokerisse sisse oma võtmega, seega kontot sul vaja ei
ole. Käsk `get mqtt.presets` näitab teisi kogukonna brokereid, mida püsivara
tunneb.

### Oma broker {#own}

Pane oma broker vabasse pessa. Sisesta selle aadress, port, kasutajanimi ja
parool. PSRAM-iga plaadil on pesa 4 vaba:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Ilma PSRAM-ita plaadil kasuta hoopis pesa 2: asenda `mqtt4` kujuga `mqtt2`.
Sinu broker tuleb siis `dutchmeshcore-2` asemele.

Port `8883` loob krüpteeritud ühenduse (TLS), port `443` krüpteeritud ühenduse
veebiühenduse kaudu (websocket) ja iga muu port krüpteerimata ühenduse. Võid
sisestada ka täieliku aadressi, näiteks `wss://mqtt.example.org:9002/mqtt`;
siis pordireegel ei kehti.

## Kontrolli, kas see töötab {#check}

Sisesta `get mqtt.status`. Iga pesa juures on näha selle olek:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: ühendatud.
- `wait`: pesal puudub mõni seade, näiteks lennujaama kood.
- `disc`: veel ühendamata. Kontrolli Wi-Fi-t käsuga `get wifi.status`.
- `fail`: pesa andis umbes 20 minuti jooksul 7 korda järjest tõrke ja proovib
  nüüd kord 30 minuti tagant. Kontrolli brokeri aadressi ja sisselogimisandmeid.
- `inactive`: plaadil pole selle pesa jaoks ruumi. Vaata jaotist
  [Brokeri pesad](#brokers).

Seejärel otsi oma kordaja nime
[Analyzeri vaatlejate lehelt](https://meshcore-analyzer.eu/#observers).
See ilmub sinna 5 minuti jooksul koos sellega, mida kordaja kuulis.
