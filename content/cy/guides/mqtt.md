---
title: MQTT ar dy arsyllwr
lead: Gad i dy ailadroddydd adrodd yr hyn mae'n ei glywed i'r MeshCore Analyzer dros Wi-Fi. Mae'n dal i basio negeseuon ymlaen fel o'r blaen.
description: Tro ailadroddydd ESP32 yn arsyllwr MeshCore gyda chadarnwedd arsyllwr DMC. Fflachia'r gadarnwedd, gosoda Wi-Fi a dy god maes awyr, dewisa'r broceriaid a gwiria fod y nod yn adrodd i'r MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-11-02'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Nod sydd hefyd yn adrodd yr hyn mae'n ei glywed dros MQTT, drwy Wi-Fi, yw arsyllwr. Mae pob arsyllwr yn dangos ychydig mwy o'r rhwyll ar y
[MeshCore Analyzer](https://meshcore-analyzer.eu/) ac ar y
[mapiau darpariaeth](/map/). Gyda'r canllaw hwn, rwyt ti'n troi ailadroddydd (nod sy'n pasio negeseuon ymlaen) yn arsyllwr. Mae'n dal i ailadrodd, ac mae'r adroddiad yn mynd un ffordd: does dim byd yn dod yn ôl i'r rhwyll.

{{< callout type="warning" >}}
Mae'r canllaw hwn ar gyfer **cadarnwedd arsyllwr DMC**, sef fersiwn arsyllwr
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), wedi'i seilio ar
MeshCore 1.18.0. Does gan MeshCore safonol ddim MQTT. Daw pob gorchymyn isod o god ffynhonnell y gadarnwedd, yn adeiliad `32dd8ad` o 19 Hydref 2026.
{{< /callout >}}

## Beth sydd ei angen arnat ti {#need}

- Bwrdd ESP32 gyda Wi-Fi, fel Heltec V3 neu V4, LilyGo T3S3 neu Xiao S3. Mae'r [rhyddhad](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  yn rhestru pob bwrdd. Does gan fyrddau nRF52 fel y RAK4631 ddim Wi-Fi.
- Rhwydwaith Wi-Fi 2.4 GHz lle mae'r bwrdd.
- Cebl data USB, a Chrome, Edge neu Opera ar dy gyfrifiadur.
- Cod y maes awyr agosaf at dy nod, 3 llythyren fel `AMS` neu `BRU`.
  Mae'n dweud wrth y broceriaid (y gweinyddion sy'n derbyn dy adroddiadau) ym mha ardal mae dy arsyllwr.

Dim Wi-Fi lle mae dy ailadroddydd, ond cyfrifiadur wrth ei ymyl?
[Crea ffurfweddiad pont](/guides/mctomqtt/) yn lle hynny.

## Fflachia'r gadarnwedd {#flash}

Dim ond MeshCore safonol sydd ar y [fflachiwr](/firmware/flasher/) ar y wefan hon.
Daw cadarnwedd yr arsyllwr o'r fflachiwr yn y
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Dewisa dy fwrdd, yna **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Dewisa **Full flash** y tro cyntaf: mae'n disodli popeth ar y bwrdd, gan gynnwys y tabl rhaniadau. Mae diweddariad yr ap yn cadw'r hyn sydd yno, ac mae ar gyfer diweddariadau yn nes ymlaen.
3. Gosoda dy ailadroddydd fel arfer: enw, rhagosodiad radio a chyfrinair gweinyddwr, fel yn y [canllaw ailadroddydd](/repeater-guide/#config).

Y fersiwn **dev** yw'r gadarnwedd hon, ac mae'n ei diweddaru ei hun o'r sianel dev pan fyddi di'n teipio `ota update`. Mae'r sianel sefydlog yn dal i gynnig 1.17.1, felly arhosa ar dev ar gyfer y canllaw hwn.

## Gosodiadau {#settings}

Agora'r [consol cyfresol](/firmware/console/) ar y wefan hon a chysyllta dy fwrdd. Noda dy rwydwaith Wi-Fi, dy gyfrinair a dy god maes awyr dy hun, yna gluda'r llinellau hyn fesul un:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Ar ôl yr ailgychwyn, mae'r bwrdd yn ymuno â dy Wi-Fi ac yn gosod ei gloc o'r rhyngrwyd. Mae ar y broceriaid angen y cloc hwnnw i wirio pwy yw dy arsyllwr. Heb god maes awyr, does dim byd yn cael ei adrodd.

Gwell gen ti glicio na theipio? Mae `start webconfig` yn agor tudalen osodiadau ar y bwrdd, yn y cyfeiriad mae'r consol yn ei ddangos. Mewngofnoda gyda dy gyfrinair gweinyddwr.

## Slotiau broceriaid {#brokers}

Mae slot yn dal un brocer. Mae'r gadarnwedd yn dechrau gyda'r slotiau hyn wedi'u llenwi:

| Slot | Brocer | Pwy sy'n ei redeg |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Mae gan fwrdd heb gof ychwanegol (PSRAM), fel y Heltec V3, 3 slot. Mae'n cysylltu â 2 ohonyn nhw ar yr un pryd, felly dydy'r Analyzer yn slot 3 byth yn cysylltu. Symuda fe i slot 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Mae gan fwrdd gyda PSRAM, fel y Heltec V4, 6 slot, ac mae'n cysylltu â 5 ar yr un pryd. Does dim angen newid dim arno.

Mae dy nod yn mewngofnodi i bob brocer gyda'i allwedd ei hun, felly does dim angen cyfrif arnat ti. Mae `get mqtt.presets` yn rhestru'r broceriaid cymunedol eraill mae'r gadarnwedd yn eu hadnabod.

### Dy frocer dy hun {#own}

Rho dy frocer dy hun mewn slot rhydd. Noda ei gyfeiriad, ei borth, ei enw defnyddiwr a'i gyfrinair. Ar fwrdd gyda PSRAM, mae slot 4 yn rhydd:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Ar fwrdd heb PSRAM, defnyddia slot 2 yn lle hynny: rho `mqtt2` yn lle `mqtt4`.
Mae dy frocer wedyn yn cymryd lle `dutchmeshcore-2`.

Mae porth `8883` yn cysylltu gydag amgryptio (TLS), porth `443` gydag amgryptio dros gysylltiad gwe (websocket), ac unrhyw borth arall heb amgryptio. Gelli di hefyd roi'r cyfeiriad llawn, fel `wss://mqtt.example.org:9002/mqtt`; wedyn dydy rheol y porth ddim yn berthnasol.

## Gwiria ei fod yn gweithio {#check}

Teipia `get mqtt.status`. Mae pob slot yn dangos ei gyflwr:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: wedi cysylltu.
- `wait`: mae gosodiad ar goll o'r slot, fel y cod maes awyr.
- `disc`: heb gysylltu eto. Gwiria dy Wi-Fi gyda `get wifi.status`.
- `fail`: methodd y slot 7 gwaith yn olynol, dros tua 20 munud, ac mae bellach yn ceisio unwaith bob 30 munud. Gwiria gyfeiriad a manylion mewngofnodi'r brocer.
- `inactive`: does gan y bwrdd ddim lle i'r slot hwn. Edrycha ar
  [Slotiau broceriaid](#brokers).

Yna chwilia am enw dy ailadroddydd ar
[dudalen arsyllwyr yr Analyzer](https://meshcore-analyzer.eu/#observers).
Mae'n ymddangos o fewn 5 munud, gyda'r hyn a glywodd.
