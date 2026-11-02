---
title: Errepikagailuen gida
lead: Toki altuan jarritako errepikagailuak inguruko guztien mezuak birbidaltzen ditu, herri edo haran oso batean. Aukeratu kokapena, elikatu eguzkiaren bidez, konfiguratu eta bete legea.
description: 'Planifikatu, elikatu, konfiguratu eta legearen barruan erabili MeshCore errepikagailu bat Europan: kokapena, eguzki-sistemaren neurria, CLI ezarpenak, 868 MHz bandako potentzia eta duty cycle mugak.'
eyebrow: 868 MHz · gehienez 500 mW · lizentziarik gabe
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-11-02'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Errepikagailuek eusten diote mesh sareari. Companion gailuek, mezuak bidaltzeko erabiltzen dituzun irratiek, ez dituzte mezuak birbidaltzen. Beraz, errepikagailurik gabe, zuzeneko irismenean dagoen jendearengana bakarrik iristen zara. Toki egokian jarritako errepikagailuak inguruko guztientzat zabaltzen du sarea. Gida honek MeshCore firmwarearen v1.18.0 bertsioa hartzen du oinarritzat.

Hasi aurretik, hitz egin [tokiko taldearekin](/community/). Taldeak badaki non falta den estaldura, [zure inguruan zein preset erabiltzen den](/guides/settings/) eta nola izendatu errepikagailuak. Begiratu [estaldura-mapetan](/map/) zein errepikagailu dituzun gertu, eta agurtu jendea [kanal](/guides/channels/) publikoetan edo tokikoetan.

## Behar duzu errepikagailurik? {#need}

Errepikagailu batek entzuten duen flood mezu oro birbidaltzen du, eta irismenean dauden errepikagailu guztiek aire-denbora bera partekatzen dute. Sarea dagoeneko zuregana iristen bada, errepikagailu berri batek trafikoa gehitzen du, ez estaldura. Agian nahikoa duzu companion gailu bat toki altuan jartzea, ganbarako leihoan edo balkoian.

Jarri errepikagailua estaldura falta den tokian:

- [estaldura-mapek](/map/) ez dute errepikagailurik erakusten zure inguruan, edo zure companion gailuak entzuten ez dituenak bakarrik erakusten dituzte;
- tokiko taldeak dio inguruak errepikagailu bat behar duela.

## Aukeratu kokapena {#site}

Altuerak potentziak baino gehiago balio du. 868 MHz bandan, LoRa seinalea ikusmen-lerro garbian hedatzen da ondoen. Muinoek, eraikinek eta zuhaitz trinkoek irismen asko kentzen dute, milliwatt gehigarri batzuek berreskuratzen dutena baino askoz gehiago.

- **Jarri goian.** Teilatu batek, masta batek, eraikin altu batek edo muino batek leiho-ertz batek baino askoz eremu handiagoa estaltzen du. Inguruko teilatuen gainetik metro batzuk igotzeak ere laguntzen du.
- **Utzi antena oztoporik gabe.** Muntatu teilatu-ertzen gainetik, metaletatik, euri-kanaletatik eta beste antenetatik urrun.
- **Egiaztatu ikuspegia.** [HeyWhatsThat](https://www.heywhatsthat.com/) bezalako tresnek erakusten dute toki batetik zer ikusten den. Toki bat ikusten baduzu, han dagoen errepikagailua irismenean duzu.
- **Utzi tartea.** Irrati-bideak leku librea behar du lerro zuzenaren inguruan ere, ez lerroan bakarrik. Distantzia luzeetan, bidearen erdialdeak metro batzuetako tartea izan behar du oztopoen gainetik.
- **Eskatu baimena.** Lortu teilatuaren edo mastaren jabearen baimena, eta adostu nola iritsiko zaren errepikagailura mantentze-lanak egiteko.

## Hardwarea {#hardware}

- **Plaka.** Aukeratu kontsumo txikiko nRF52 plaka bat, hala nola [Heltec T114](/devices/), RAK WisBlock edo SenseCAP Solar Node. ESP32 plakek potentzia gehiago kontsumitzen dute (gailuen orrian High marka dute), eta horregatik zaila da eguzki-energiarekin elikatzea.
- **Antena.** Erabili 868 MHz bandarako egindako antena bat, bertikalean muntatuta. [Antenen gidak](/guides/antenna/) motak, konektoreak, kablea eta muntaketa azaltzen ditu. Antenaren irabazia legezko potentzia-mugan zenbatzen da: ikus [Legezko mugak](#legal).
- **Kablea.** Erabili kable koaxial laburra edo galera txikiko kablea. 868 MHz bandan, kable meheko metro batzuetan zure potentziaren erdia gal dezakezu.
- **Kaxa.** Eguraldiari eusten dion kaxa bat (IP65 edo hobea), kable-prentsa batekin, kondentsazioaren aurkako aireztapen- edo drainatze-zulo batekin, eta kolore argikoa edo eguzki-babesarekin. Beroak kalte egiten die bateriei, eta ezin dira kargatu izozte-puntutik behera.
- **Tximistak.** Teilatuko antena jomuga bat da. Bete lur-konexioari buruzko tokiko arauak, edo muntatu tximista bat eraikinaren kableatura iritsiko ez den tokian.

## Potentzia eta eguzki-sistemaren neurria {#power}

Eguzki-errepikagailuak neguko aste ilunenei eutsi behar die. Kalkulatu sistemaren neurria aste horietarako:

1. **Neurtu kontsumoa.** Eduki konfiguratutako errepikagailua martxan egun batez, USB potentzia-neurgailu baten bidez. Irakurri kontsumitutako energia watt-ordutan (Wh). Zure inguruko trafikoak zenbakia aldatzen du. Beraz, neurtu tokian bertan, ahal baduzu.
2. **Gehitu erreserba.** Kalkulatu bateriaren edukiera gutxienez 5 eta 7 egun artean irauteko, eguzki baliagarririk gabe.
3. **Aurkitu zure neguko eguzkia.** EBren doako [PVGIS tresnak](https://re.jrc.ec.europa.eu/pvg_tools/en/) erakusten du, edozein kokapenetan, panel batek hilean zenbat energia sortzen duen. Erabili eguzki gutxien duen hilabetea.
4. **Kalkulatu panelaren neurria.** Hilabete txar horretan, panelak egun bakoitzeko kontsumoa ordeztu behar du, karga-galeretarako tartea utzita.

Adibide bat, zenbaki hipotetikoekin: egunean 1 Wh kontsumitzen duen errepikagailuak gutxienez 7 Wh-ko bateria behar du astebeteko erreserbarako, gutxi gorabehera 2 Ah-ko edukiera erabilgarria 3.7 V-tan. PVGISen arabera 1 W-ko panelak egunean 0.5 Wh ematen baditu abenduan zure kokapenean, gutxienez 2 W-ko panela behar duzu. 3 eta 5 W arteko panelak tartea uzten du hodeietarako, elurrerako eta zahartzerako.

## Konfiguratu {#config}

**Instalatu firmwarea.** Erabili [web flasher](https://flasher.meshcore.io) tresna eta aukeratu zure plakarako **Repeater** firmwarea. Urratsak [Hasi hemen](/get-started/#flash) orrian dituzu.

**Konfiguratu USB bidez.** Errepikagailua oraindik ordenagailura konektatuta duzula, ireki [config.meshcore.io](https://config.meshcore.io) edo flasherraren kontsola. Serieko edozein terminal ere erabil dezakezu, 115200 baud-etan. Komando garrantzitsuenak:

| Zer | Komandoa |
|---|---|
| Aldatu administratzailearen pasahitza | `password <new password>` |
| Jarri izena | `set name <name>` |
| Irrati-preseta: maiztasuna, banda-zabalera, SF, CR (berrabiarazi aplikatzeko) | `set radio 869.618,62.5,8,8` |
| Duty cycle muga, ehunekotan | `set dutycycle 10` |
| Irrati-txiparen igorpen-potentzia, dBm-tan | `set tx <dBm>` |
| Kokapena, mapetan ager dadin | `set lat <degrees>` eta `set lon <degrees>` |
| Beste operadoreentzako harremanetarako datuak | `set owner.info <text>` |
| Flood iragarkien arteko orduak (sare osoak entzuten dituen iragarkiak) | `set flood.advert.interval <hours>` |
| Iragarri orain | `advert` |
| Berrabiarazi | `reboot` |

Administratzailearen pasahitz lehenetsia `password` da, eta harekin saioa hasten duen edonor administratzaile bihurtzen da. Aldatu pasahitza errepikagailua emititzen hasi aurretik.

Goiko `set radio` adibidea EU/UK (Narrow) presetarena da. Erabili horren ordez zure inguruko presetaren balioak: [Gomendatutako ezarpenak](/guides/settings/) orrian herrialdez herrialde daude zerrendatuta.

**Doitu erlojua.** Erloju-modulurik (RTC) gabe, errepikagailuak ordua galtzen du argindarra joaten den bakoitzean, eta 2024ko maiatzean hasten da berriro. Martxan dagoen bitartean, erlojua desbideratu ere egiten da: gero eta aurrerago edo atzerago doa. Beraz, doitu erlojua noizean behin: hasi saioa urrunetik, aplikazioan, eta erabili `clock sync`, edo jarri ordua USB bidez. RTC modulu batekin gutxitan egin behar duzu: moduluak ordua gordetzen du argindarra joaten denean, eta askoz gutxiago desbideratzen da.

**Kudeatu urrunetik.** Errepikagailua sarean dagoenean, hasi saioa MeshCore aplikaziotik administratzailearen pasahitzarekin. Han irakurtzen duzu haren egoera, eta komando berak erabiltzen dituzu irrati bidez. Komando batzuek USB bidez bakarrik funtzionatzen dute, hala nola `set freq` eta fabrika-berrezarpena egiten duen `erase`.

**Gorde identitatea.** Ezabatu aurretik, idatzi `get prv.key` USB bidez eta gorde erakusten duen gako pribatua toki seguruan. Ezabatu ondoren, `set prv.key <key>` eta `reboot` erabiliz, errepikagailuak bere identitate zaharra berreskuratzen du. Horrela, ezagutzen duten nodoek aurrizki berarekin aurkitzen dute.

Komando-zerrenda osoa [MeshCore CLI erreferentzian](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md) dago.

## Eguneratu airez {#update}

Errepikagailua goian dagoenean, lurretik eguneratzen duzu. Hasi saioa MeshCore aplikaziotik administratzailearen pasahitzarekin, ireki haren komando-lerroa eta idatzi `start ota`. Hurrengo urratsak plakaren araberakoak dira. Beste plakek `Error` erantzuten dute, eta horiek USB bidez eguneratzen dituzu.

**nRF52 plakak**, hala nola RAK, Heltec T114, Seeed XIAO eta SenseCAP Solar:

1. Deskargatu zure plakarako firmware berriaren **ZIP** fitxategia [web flasher](https://flasher.meshcore.io) tresnatik.
2. Idatzi `start ota`. Errepikagailuak `OK` erantzuten du eta Bluetooth bidez `<board>_OTA` izenarekin agertzen da, adibidez `RAK4631_OTA`.
3. Ireki nRF Device Firmware Update aplikazioa telefonoan, aukeratu ZIP fitxategia eta errepikagailua, eta igo fitxategia. Minutu batzuk irauten du.

Instalatu [OTAFIX abiarazlea](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX) nRF52 plakan, goian jarri aurretik. Jatorrizko abiarazlearekin, huts egindako eguneratzea USB bidez bakarrik konpon dezakezu. OTAFIXekin, plaka eguneratze-modura itzultzen da, eta berriro saia zaitezke Bluetooth bidez.

**ESP32 plakak**, hala nola Heltec V3 eta V4:

1. Deskargatu zure plakarako **non-merged** `.bin` fitxategia web flasher tresnatik: izenean "merged" ez daraman fitxategia.
2. Idatzi `start ota`. Errepikagailuak `MeshCore-OTA` izeneko WiFi sare bat irekitzen du eta bere igoera-orriaren helbidearekin erantzuten du.
3. WiFi irismenaren barruan, konektatu telefonoa edo ordenagailu eramangarria sare horretara, ireki helbidea eta igo fitxategia.

## Legezko mugak {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
MeshCoreren Europako presetak **869.40-869.65 MHz** azpibandan daude. EBn, Erresuma Batuan, Suitzan eta Norvegian, irismen laburreko gailuek lizentziarik gabe erabil dezakete azpibanda hori, muga hauen barruan:

- gehienez **500 mW e.r.p.** potentzia erradiatua;
- gehienez **%10eko duty cycle**: gailu bakoitzak ordu bakoitzean gehienez 360 segundoz igor dezake. Bestela, gailuak listen-before-talk erabil dezake maiztasun-egokitzapenarekin (adaptive frequency agility), ETSI EN 300 220-2 arauak definitzen duen moduan;
- seinale osoak, gehienez 250 kHz-eko zabalerakoak, azpibandaren barruan egon behar du.

Banda partekatua da: ezin dituzu lizentziadun zerbitzuak oztopatu, eta besteek oztopa zaitzakete.
Irratiak CE marka izan behar du (Britainia Handian, CE edo UKCA).
{{< /callout >}}

Iturriak: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845), 1. eranskina, h1.7 banda; [Batzordearen 2006/771/EE Erabakia](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) eta haren aldaketak; [ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), O banda.

### Potentzia: e.r.p. eta zure antena {#erp}

Muga potentzia *erradiatuari* aplikatzen zaio, dipolo antena sinple batekin alderatuta neurtuta (e.r.p.). Antenaren irabazia gehitu egiten da, eta kablearen galera kendu. Fabrikatzaileek antenaren irabazia dBi-tan ematen dute, eta hori irabazi bera dBd-tan (dipoloarekiko) baino 2.15 dB gehiago da. Mantendu batura hau 27 dBm-tan (500 mW) edo azpitik:

> igorpen-potentzia (dBm) + antenaren irabazia (dBi) − kablearen galera (dB) − 2.15 ≤ 27

- 22 dBm igortzen dituen plaka bat, 5 dBi-ko antenarekin eta 1 dB galtzen duen kablearekin: 22 + 5 − 1 − 2.15 = 23.85 dBm, gutxi gorabehera 240 mW e.r.p. Mugaren barruan dago.
- 30 dBm-ko (1 W) anplifikadorea duen plaka bat, 3 dBi-ko antenarekin: 30 + 3 − 2.15 = 30.85 dBm, gutxi gorabehera 1.2 W e.r.p. Muga gainditzen du: jaitsi igorpen-potentzia.

`set tx` komandoak LoRa txiparen irteera ezartzen du, dBm-tan. SX1262 txipak berak gehienez 22 dBm ematen ditu, eta firmwareak ez du egiaztatzen sartzen duzun zenbakia. Anplifikadore gehigarria duten plakek, hala nola Heltec V4 edo Station G2, ezartzen duzun zenbakia baino askoz gehiago igortzen dute. Begiratu fabrikatzailearen taula ezarri aurretik, eta hasi balio txiki batekin.

### Duty cycle {#duty-cycle}

Errepikagailuak inguruko guztientzat igortzen du, eta horregatik companion gailu batek baino azkarrago agortzen du bere aire-denbora. MeshCoreren duty cycle mugatzaileak %50 du lehenetsita, eta hori banda honek baimentzen duena baino gehiago da. Ezarri %10 errepikagailu guztietan:

```text
set dutycycle 10
```

### Maiztasunaren zehaztasuna {#frequency}

EU/UK (Narrow) kanala (869.618 MHz, 62.5 kHz-eko banda-zabalera) 869.649 MHz-eraino iristen da: azpibandaren goiko mugatik 1 kHz baino gutxiagora. Seinaleak bandaren barruan egon behar du tenperatura guztietan. Horretarako, tenperatura-konpentsazioa duen kristal bat (TCXO) behar da. Egungo plaka ia guztiek badute. TCXOrik gabeko plaka zaharrak, hala nola Heltec V2, gehiegi desbideratzen dira 62.5 kHz-etan fidagarri funtzionatzeko.

### Herrialdeen oharrak {#countries}

- **EBko estatu kideek** azpibanda hau baldintza hauetan eskuragarri jarri behar dute (2006/771/EE Erabakia, 3. artikulua).
- **Erresuma Batua:** muga berak, Ofcomen [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices) dokumentuan.
- **Suitza eta Liechtenstein:** muga berak, OFCOMen [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09) dokumentuan.
- **Norvegia:** muga berak, [baimen orokorrei buruzko araudian](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Ohar hauek ez dira lege-aholkularitza. Arauak aldatu egiten dira. Zalantzarik baduzu, galdetu zure herrialdeko erregulatzaileari.

## Instalazioaren egiaztapen-zerrenda {#checklist}

- [ ] Kokapenaren jabeak baimena eman du, eta errepikagailura irits zaitezke mantentze-lanetarako.
- [ ] Plakak **Repeater** firmwarea du, eta lehen aldiz piztu aurretik konektatu zenuen antena.
- [ ] Administratzailearen pasahitza aldatu duzu.
- [ ] Irratia [zure inguruko presetarekin](/guides/settings/) bat dator (`get radio`).
- [ ] `set dutycycle 10` ezarrita dago.
- [ ] Igorpen-potentzia gehi antenaren irabazia 500 mW e.r.p. mugaren barruan dago.
- [ ] Izena, kokapena eta `owner.info` ezarrita daude, besteek jakin dezaten nork kudeatzen duen.
- [ ] Erlojua doituta dago (`clock`).
- [ ] Kaxa ondo itxita dago, drainatze- edo aireztapen-zuloarekin, eta kableak tanta-begizta du.
- [ ] Bateriaren eta panelaren neurria neguko hilabete txarrenerako kalkulatuta dago.
- [ ] Urrunetik probatu duzu aplikazioarekin, kokapenetik joan aurretik.
- [ ] Tokiko taldeak badaki errepikagailua martxan dagoela.
