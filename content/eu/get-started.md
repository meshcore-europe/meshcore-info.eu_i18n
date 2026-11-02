---
title: Lehen urratsak
lead: Plaka berri batetik mesh sareko zure lehen mezura. LoRa plaka bat, Chrome edo Edge duen ordenagailu bat eta aplikaziorako telefono edo ordenagailu eramangarri bat behar dituzu.
description: Flasheatu MeshCore nabigatzailetik, parekatu aplikazioa, aukeratu zure eremuak erabiltzen duen irrati-aurrezarpena, bidali zure lehen mezua eta sartu zure tokiko kanalean.
eyebrow: 6 urrats · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-11-02'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Urrats hauek MeshCore firmwarearen v1.18.0 bertsioan eta 2026ko urriko tresna ofizialetan oinarrituta daude. Aplikazioko menuen izenak apur bat alda daitezke bertsio batetik bestera.

## 1. Aukeratu gailu bat {#device}

[Gailuen orrian](/devices/) companion aukera duen edozein plakak balio du. Zure lehen nodorako, aukeratu *companion* bat: mezuak bidaltzeko erabiltzen duzun irratia. Parekatu telefonoarekin edo ordenagailu eramangarriarekin, Bluetooth edo USB bidez. Bestela, aukeratu pantaila eta teklatu propioak dituen bat, bere kabuz dabilena.

Hartu 868 MHz-ko bertsioa. Berarekin datorren antenak balio du; [antena-gidan](/guides/antenna/) ikusiko duzu nola egiaztatu antena bat.

{{< callout type="warning" >}}
Konektatu antena irratia piztu aurretik. Antenarik gabe transmititzen duen LoRa irrati batek bere txipa honda dezake.
{{< /callout >}}

## 2. Flasheatu firmwarea {#flash}

1. Konektatu gailua ordenagailura USB datu-kable batekin.
2. Ireki web flasherra [flasher.meshcore.io](https://flasher.meshcore.io) helbidean, Chrome edo Edge nabigatzailean. Flasherrak Web Serial erabiltzen du, eta beste nabigatzaileek ez dute hori.
3. Aukeratu zure gailua, eta gero **Companion** firmwarea **Bluetooth**-erako (edo USB-rako, ordenagailuarekin kablez bakarrik erabiliko baduzu).
4. Flasheatu. Plaka batzuek lehenik eguneratze-moduan sartu behar dute; flasherrak azaltzen dizu nola.

Erabili *erase* hutsetik hasteko bakarrik: ezabatzean, gailuaren identitatea eta zure kontaktuak galtzen dira. Geroko eguneratzeetan, flasheatu ezabatu gabe. Ezabatzean identitatea ez galtzeko, esportatu lehenik zure companion-aren gako pribatua aplikaziotik, eta inportatu gero.

## 3. Instalatu aplikazioa {#app}

MeshCore aplikazio ofiziala Android, iOS, Windows eta macOS sistemetarako dago; [meshcore.io](https://meshcore.io) webgunean bertsio guztien estekak aurkituko dituzu. Web aplikazio bat ere badago [app.meshcore.nz](https://app.meshcore.nz) helbidean, ordenagailuko Chrome edo Edge nabigatzailean dabilena.

## 4. Parekatu zure nodoa {#pair}

Piztu nodoa, ireki aplikazioa eta konektatu nodora Bluetooth bidez. PIN bat eskatzen dizunean:

- pantaila **duen** nodo batek PIN bat erakusten du; idatzi hori;
- pantailarik **ez duen** nodo batek `123456` erabiltzen du.

Parekatzeak huts egiten badu, kendu gailua telefonoaren Bluetooth ezarpenetatik eta saiatu berriro. Gero, jarri izen bat zure nodoari. Besteek izen hori ikusten dute, beraz ez erabili zure izen osoa edo helbidea, nahi ez baduzu.

## 5. Aukeratu zure eremuko irrati-aurrezarpena {#preset}

Eremu bateko irrati guztiek maiztasun eta ezarpen berberak erabiltzen dituzte; bestela, ez dute elkar entzuten. Aplikazioko irrati-ezarpenetan, aukeratu zure eremuak erabiltzen duen aurrezarpena. Beheko eremuetatik kanpo, Europak **EU/UK (Narrow)** erabiltzen du. Herbehereek, Txekiak, Hungariak, Eslovakiak, Portugalek eta Suitzak berea dute, eta Herbehereetako Limburgek aldaera bat du:

{{< presets >}}

Zure gailuak ez du zure eremuko aurrezarpena eskaintzen? Sartu eskuz taulako 4 balioak aplikazioko irrati-ezarpenetan: maiztasuna, banda-zabalera, spreading factor eta coding rate. Beste balio batzuk dituen nodo batek ez du mesh sarea entzuten.

Ez zaude ziur? Zure [tokiko taldeak](/community/) badaki zein aurrezarpen erabiltzen den zure eremuan. Aplikazioak MeshCore proiektutik deskargatzen du zerrenda hau, beraz aurrezarpen berri batek ez du aplikazioaren eguneratzerik behar.

## 6. Esan kaixo {#hello}

1. **Iragarri zure burua.** Bidali *advert* bat aplikaziotik. "Flood" motako advert bat errepikagailuetatik (mezuak aurrera pasatzen dituzten nodoetatik) igarotzen da, eta horrela mesh sareko edonork gehi zaitzake.
   Companion-ek ez dute inoiz beren burua automatikoki iragartzen.
2. **Bilatu besteak.** Jendea zure kontaktuetan agertzen da, haien advert-ak zuregana iristen direnean. Lehenespenez, errepikagailuek flood advert bat bidaltzen dute 47 orduz behin, beraz zure zerrenda betetzeak 2 egun har ditzake.
3. **Bidali mezu bat.** Ireki kontaktu bat eta idatzi. Lehen mezua sare osoan hedatzen da (flood); hartzaileak mezuak egindako bidea jakinarazten du, eta hurrengo mezuek bide horri jarraitzen diote.
4. **Sartu kanaletan.** **Public** kanala prest dago; bertan idazten duzun guztia mesh sareko guztiengana iristen da. Gehitu zure eskualdeko *hashtag kanala* (`#` karakterez hasten den izena) haren izena idatzita. Zure [tokiko taldeak](/community/) esango dizu zein kanal dauden aktibo.

## Zerbait ondo ez dabilenean {#troubleshooting}

**Aplikazioak ez du nire gailua aurkitzen Bluetooth bidez.**
Seguruenik USB companion-a flasheatu duzu. Flasheatu berriro eta aukeratu Bluetooth bertsioa. Heltec V3-n, Bluetooth antena txiki integratuak irismen laburra du; eduki telefonoa gertu.

**Parekatzeak huts egiten du behin eta berriro.**
Kendu gailua telefonoaren Bluetooth ezarpenetatik, berrabiarazi Bluetooth eta parekatu berriro pantailako PINarekin edo `123456` erabilita.

**Inor ez da agertzen nire kontaktuetan.**
Egiaztatu zure aurrezarpena zure eremukoa dela. Bidali flood advert bat. Errepikagailurik irismenean ez badago, gertuko irratiak bakarrik entzungo dituzu; [maparen orrian](/map/) ikusiko duzu non dauden errepikagailuak.

**Kontaktu baten "last seen" duela egun batzuetakoa da, nahiz eta aktibo egon.**
Bi nodoetako batek ordu okerra du. Companion batek telefonotik hartzen du ordua; errepikagailuen eta room server-en (talde baterako mezuak gordetzen dituzten nodoen) ordua jabeak ezarri behar du.

**Mezu zuzen bat ez da inoiz iristen.**
Bi aldeek izan behar dute bestea kontaktu gisa. Nodo batek ezagutzen ez duen norbaiten mezua baztertu egiten du, igorleari ezer esan gabe. Bidali flood advert bat eta eskatu besteari hark ere bat bidaltzeko. Egiaztatu aplikazioan kontaktu berriak automatikoki gehitzen dituela; bere jauzi-mugaren barruko nodoak bakarrik gehitzen ditu.

**Kontaktu zaharrak badabiltza, berriak ez dira inoiz konektatzen.**
Lehen mezua sarean hedatzen da (flood), eta errepikagailu batek mezuaren eskualdea duenean bakarrik pasatzen du aurrera. Hurrengo mezuek ikasitako bide bati jarraitzen diote, eta eskualde-egiaztapen batek ere ez ditu geldiarazten. Galdetu zure [tokiko taldeari](/community/) zure inguruko errepikagailuek zein eskualde dituzten, eta begiratu [zure eremuko ezarpenak](/guides/settings/#traffic).

**Aplikazioa ez da jada konektatzen zure companion-era.**
Plaka batzuek erabiltzaile-botoi bat dute, hala nola RAK plaka batzuek eta Heltec T114-k. Eduki sakatuta plaka abiatu ondorengo lehen 8 segundoetan. Companion-ak erreskate-kontsola bat irekitzen du USB bidez. [flasher.meshcore.io](https://flasher.meshcore.io) webguneko kontsolan, `set pin <pin>` komandoak Bluetooth PIN berria ezartzen du eta `erase` komandoak gailua garbitzen du.

**Flasherrak ezin du serieko ataka ireki Linuxen.**
Zure erabiltzaileak atakarako sarbidea behar du, adibidez `sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, edo `dialout` taldeko kide izan behar du.

**Beste zerbait.** [MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md) dokumentuak arazo askoz gehiago lantzen ditu.
