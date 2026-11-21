---
title: Retranslatora ceļvedis
lead: Augstu novietots retranslators pārsūta ziņas visiem apkārtējiem, pat visā pilsētā vai ielejā. Izvēlies vietu, nodrošini saules enerģiju, iestati ierīci un ievēro likumu.
description: 'Kā Eiropā plānot, darbināt, iestatīt un likumīgi izmantot MeshCore retranslatoru: vietas izvēle, saules sistēmas aprēķins, CLI iestatījumi, 868 MHz jaudas un darba cikla ierobežojumi.'
eyebrow: 868 MHz · līdz 500 mW · bez licences
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'd42ee2ac'
  seeded: '2026-11-21'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '824ab38e', '662ea23c', '70faf508', 'b9991666', '69d7162f', 'bf712994', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'cc266810']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', 'bbea9a0c', '2b9fab3b', 'b13d1947', 'c2bad16f', '636edc86', 'c2d6bcd1', '957ae975', '98874949', '96d1ebad', 'dbd9fa1f', 'aa06d32b', '9958aad3', '73642ab6', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '90338c64', '2b1d995b', '992bed82', '62eb1543', '210f1b66', 'e817b1f7', '63f961dc', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', '50af0550', 'dd7c556b', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '7cf2bc81']
---

Tīkls balstās uz retranslatoriem. Companion ierīces ir radio, no kuriem tu sūti ziņas, un tās ziņas tālāk nepārsūta. Tāpēc bez retranslatoriem tu sasniedz tikai tos, kas ir tiešā darbības rādiusā. Pareizi novietots retranslators paplašina tīklu visiem apkārtējiem. Šis ceļvedis atbilst MeshCore programmaparatūras versijai v1.18.0.

Pirms sāc, parunā ar savu [vietējo grupu](/community/). Tās dalībnieki zina, kur trūkst pārklājuma, [kuru priekšiestatījumu izmanto tavā apkaimē](/guides/settings/) un kā nosaukt retranslatorus. Apskati [pārklājuma kartēs](/map/), kādi retranslatori ir tev tuvumā, un sasveicinies publiskajos vai vietējos [kanālos](/guides/channels/).

## Vai tev tāds vajadzīgs? {#need}

Retranslators pārsūta katru dzirdēto flood ziņu, un visi darbības rādiusā esošie retranslatori dala vienu un to pašu ētera laiku. Ja tīkls tevi jau sasniedz, vēl viens retranslators palielina datplūsmu, nevis pārklājumu. Var pietikt ar companion ierīci, ko novieto augstu, pie bēniņu loga vai uz balkona.

Uzstādi retranslatoru tur, kur trūkst pārklājuma:

- [pārklājuma kartēs](/map/) tev tuvumā nav neviena retranslatora vai ir tikai tādi, kurus tava companion ierīce nedzird;
- tava vietējā grupa saka, ka apkaimei tāds vajadzīgs.

## Izvēlies vietu {#site}

Augstums ir svarīgāks par jaudu. LoRa signāls 868 MHz joslā vislabāk izplatās pa brīvu redzamības līniju. Pakalni, ēkas un blīvi koki atņem daudz vairāk darbības rādiusa, nekā atgūst daži papildu milivati.

- **Izvēlies augstu vietu.** Jumts, masts, augsta ēka vai pakalns aptver daudz lielāku zonu
  nekā palodze. Palīdz pat daži metri virs apkārtējiem jumtiem.
- **Turi antenu brīvā vietā.** Uzstādi to virs jumta malām, tālāk no
  metāla, notekcaurulēm un citām antenām.
- **Pārbaudi redzamību.** Tādi rīki kā [HeyWhatsThat](https://www.heywhatsthat.com/)
  rāda, kas no konkrētās vietas ir redzams. MeshCore lietotne
  [aprēķina, ko tur novietots retranslators var sasniegt](#check-site).
- **Atstāj brīvu telpu.** Radio ceļam vajag brīvu telpu ap tiešo līniju,
  ne tikai pašu līniju. 868 MHz joslā šī telpa ir aptuveni 20 m ap
  5 km ceļa vidu. 20 km ceļam tā ir aptuveni 40 m.
- **Lūdz atļauju.** Saņem īpašnieka piekrišanu jumtam vai mastam un
  vienojies, kā tu piekļūsi retranslatoram apkopei.

### Pārbaudi vietu lietotnē {#check-site}

MeshCore lietotnes 1.33 vai jaunākā versijā šie rīki atrodas izvēlnes sadaļā **Tools**.
Tie darbojas bez pievienota radio.

- **Line of Sight** attēlo zemes profilu starp 2 punktiem un telpu, kas signālam vajadzīga virs tā.
  Kartē ilgi turi nospiestus 2 punktus vai pieskaries retranslatoriem.
- **Antenna Coverage** kartē rāda, ko var sasniegt antena 1 punktā.
  Ilgi turi nospiestu punktu vai pieskaries retranslatoram. Pievieno vēl punktus, lai salīdzinātu vietas.

Datorā rīka izvēlnē izvēlies **Add Point** un ievadi koordinātas.

Abi rīki pēc noklusējuma pieņem, ka antena tavā vietā ir 5 m augstumā, tāpēc rīka iestatījumos norādi plānoto augstumu. Antenna Coverage pēc noklusējuma pieņem, ka uztverošā antena ir 1 m augstumā. Ja radio nav pievienots, Line of Sight pēc noklusējuma izmanto 915 MHz: šī rīka iestatījumos norādi sava [priekšiestatījuma](/guides/settings/) frekvenci.

Rīki rēķina pēc augstuma datiem un tavu radio nepārbauda. Kokus un jaunas ēkas pārbaudi pats, tad aiznes companion ierīci uz šo vietu un paskaties, kurus retranslatorus tā dzird.

![Line of Sight MeshCore lietotnē: zeme starp 2 punktiem un telpa, kas signālam vajadzīga virs tās](/media/guides/line-of-sight.webp)

![Antenna Coverage MeshCore lietotnē: kartē redzama zona, ko var sasniegt antena uz pakalna](/media/guides/antenna-coverage.webp)

## Aparatūra {#hardware}

- **Plate.** Izvēlies nRF52 plati ar mazu enerģijas patēriņu, piemēram, [Heltec T114](/devices/), RAK WisBlock vai SenseCAP Solar Node. ESP32 plates patērē vairāk enerģijas (ierīču lapā tām ir atzīme High), tāpēc tās ir grūti darbināt ar saules enerģiju.
- **Antena.** Izmanto 868 MHz joslai paredzētu antenu un uzstādi to vertikāli. [Antenu ceļvedī](/guides/antenna/) atradīsi informāciju par veidiem, savienotājiem, kabeļiem un stiprināšanu. Antenas pastiprinājums ieskaitās likumā noteiktajā jaudas ierobežojumā; skati sadaļu [Juridiskie ierobežojumi](#legal).
- **Kabelis.** Lieto īsu koaksiālo kabeli vai kabeli ar maziem zudumiem. 868 MHz joslā daži metri plāna kabeļa var atņemt pusi jaudas.
- **Korpuss.** Izvēlies laikapstākļiem izturīgu kārbu (IP65 vai labāku) ar kabeļa blīvslēgu, ventilācijas vai drenāžas caurumu pret kondensātu, gaišā krāsā vai ar saulessargu. Baterijām kaitē karstums, un zem nulles tās nevar uzlādēt.
- **Zibens.** Antena uz jumta ir zibens mērķis. Ievēro vietējos zemējuma noteikumus vai uzstādi antenu tur, kur spēriens nesasniegtu ēkas elektroinstalāciju.

## Enerģija un saules sistēmas aprēķins {#power}

Saules retranslatoram jāiztur ziemas tumšākās nedēļas. Vispirms ieslēdz enerģijas taupīšanu:
pēc `powersaving on` retranslators starp paketēm guļ. Taupīšana darbojas nRF52 platēs un
ESP32 platēs, kuru programmaparatūrā nav tilta. Tad izvēlies baterijas un paneļa izmēru:

1. **Izmēri patēriņu.** Vienu dienu darbini iestatīto retranslatoru caur USB jaudas mērītāju. Nolasi patērēto enerģiju vatstundās (Wh). Šo skaitli ietekmē datplūsma tavā apkaimē, tāpēc, ja vari, mēri uz vietas.
2. **Pieskaiti rezervi.** Plāno baterijas ietilpību vismaz 5 līdz 7 dienām bez noderīgas saules.
3. **Noskaidro ziemas saules daudzumu.** ES bezmaksas [PVGIS rīks](https://re.jrc.ec.europa.eu/pvg_tools/en/) jebkurai vietai parāda, cik enerģijas panelis saražo mēnesī. Izmanto mēnesi, kurā saules ir vismazāk.
4. **Izvēlies paneļa izmēru.** Panelim šajā sliktākajā mēnesī jāsedz katras dienas patēriņš ar rezervi uzlādes zudumiem.

Aprēķina piemērs ar pieņemtiem skaitļiem: retranslatoram, kas patērē 1 Wh dienā, nedēļas rezervei vajag vismaz 7 Wh bateriju, tas ir, aptuveni 2 Ah izmantojamās ietilpības pie 3.7 V. Ja PVGIS rāda, ka 1 W panelis tavā vietā decembrī dod 0.5 Wh dienā, tev vajag vismaz 2 W paneli. Ar 3 līdz 5 W paliek rezerve mākoņiem, sniegam un novecošanai.

## Iestatīšana {#config}

**Ieraksti programmaparatūru.** Atver [tīmekļa flešotāju](https://flasher.meshcore.io) un izvēlies savai platei **Repeater** programmaparatūru. Ierakstīšanas soļi ir sadaļā [Darba sākums](/get-started/#flash).

**Iestati caur USB.** Kamēr retranslators vēl ir pievienots datoram, atver [config.meshcore.io](https://config.meshcore.io) vai flešotāja konsoli. Vari izmantot arī jebkuru seriālo termināli ar ātrumu 115200 baud. Svarīgākās komandas:

| Kas | Komanda |
|---|---|
| Nomaini administratora paroli | `password <new password>` |
| Parole viesiem, kuri var nolasīt tā statusu | `set guest.password <password>` |
| Piešķir nosaukumu | `set name <name>` |
| Radio priekšiestatījums: frekvence, joslas platums, SF, CR (stājas spēkā pēc pārstartēšanas) | `set radio 869.618,62.5,8,8` |
| Darba cikla ierobežojums procentos | `set dutycycle 10` |
| Radio mikroshēmas raidīšanas jauda dBm | `set tx <dBm>` |
| Atrašanās vieta, lai tas būtu redzams kartēs | `set lat <degrees>` un `set lon <degrees>` |
| Kontaktinformācija citiem operatoriem | `set owner.info <text>` |
| Stundas starp flood advert ziņām, kuras dzird viss mesh tīkls | `set flood.advert.interval <hours>` |
| Paziņo par to tūlīt | `advert` |
| Pārstartē | `reboot` |

Noklusējuma administratora parole ir `password`, un ikviens, kurš ar to piesakās, kļūst par administratoru. Nomaini to, pirms retranslators sāk raidīt ēterā.

Viesa parole sākumā ir tukša. Tad ikviens var pieteikties kā viesis bez paroles un nolasīt retranslatora statusu un tā kaimiņus. Katrs pieprasījums rada datplūsmu mesh tīklā. Iestati viesa paroli un iedod to tiem, kam tā vajadzīga.

**Izvēlies nosaukumu.** Nosauc to tā, kā tava vietējā grupa nosauc savus retranslatorus.
Ja grupas nav, ieliec nosaukumā valsti, vietu un īsu vārdu, piemēram,
`DE-63477-MUF1`. Tā citi operatori redz, kur retranslators atrodas. Nosaukums
var būt līdz 31 baitam garš, un advert ziņā, kurā ir arī atrašanās vieta, ietilpst 23.

Iepriekš minētais `set radio` piemērs ir EU/UK (Narrow). Tā vietā izmanto savas apkaimes priekšiestatījuma vērtības: lapā [Ieteicamie iestatījumi](/guides/settings/) tās ir norādītas katrai valstij.

**Iestati pulksteni.** Bez pulksteņa moduļa (RTC) retranslators katrā strāvas pārrāvumā
zaudē laiku un pēc pārstartēšanas rāda 2024. gada maiju. Kamēr retranslators darbojas, tā
pulkstenis arī nobīdās: tas steidzas vai atpaliek. Tāpēc laiku pa laikam iestati
pulksteni: piesakies attālināti no lietotnes un izmanto `clock sync` vai iestati laiku pa
USB. Ar RTC moduli tas tev vajadzīgs reti: modulis saglabā laiku arī strāvas pārrāvumu laikā un nobīdās
daudz mazāk. Programmaparatūra pati atrod DS3231, RV3028, PCF8563 vai RX8130 moduli.

**Plate ar GPS** iestata abus tavā vietā. Pēc `gps on` retranslators ik pēc 30 minūtēm ņem laiku no GPS, un `gps setloc` ieraksta tā atrašanās vietu laukos `lat` un `lon`. GPS patērē enerģiju visu laiku, kamēr tas ir ieslēgts. Ja retranslators darbojas ar saules enerģiju, palaid `gps setloc` vienreiz uz vietas un izslēdz GPS ar `gps off`. Pēc tam pulkstenis atkal jāiestata ar `clock sync`.

**Pārvaldi attālināti.** Kad retranslators ir tīklā, piesakies no MeshCore lietotnes ar administratora paroli. Tur tu nolasi tā statusu un pa radio izmanto tās pašas komandas. Dažas komandas darbojas tikai caur USB, piemēram, `set freq` un rūpnīcas iestatījumu atjaunošanas komanda `erase`.

**Saglabā identitāti.** Pirms dzēšanas caur USB ievadi `get prv.key` un drošā vietā noglabā parādīto privāto atslēgu. Pēc dzēšanas ar `set prv.key <key>` un `reboot` tu atjauno retranslatora veco identitāti. Tāpēc mezgli, kas to pazīst, atrod to ar to pašu prefiksu.

Pilns komandu saraksts ir [MeshCore CLI rokasgrāmatā](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Bezvadu atjaunināšana {#update}

Kad retranslators ir uzstādīts augstu, tu to atjaunini no zemes. Piesakies no MeshCore lietotnes ar administratora paroli, atver tā komandrindu un ievadi `start ota`. Tālākais ir atkarīgs no plates. Citas plates atbild `Error`, un tās tu atjaunini caur USB.

**nRF52 plates**, piemēram, RAK, Heltec T114, Seeed XIAO un SenseCAP Solar:

1. No [tīmekļa flešotāja](https://flasher.meshcore.io) lejupielādē savas plates jaunās programmaparatūras **ZIP** failu.
2. Ievadi `start ota`. Retranslators atbild `OK` un pa Bluetooth ir redzams kā `<board>_OTA`, piemēram, `RAK4631_OTA`.
3. Tālrunī atver lietotni nRF Device Firmware Update, izvēlies ZIP failu un retranslatoru, tad augšupielādē. Tas aizņem dažas minūtes.

Uzstādi [OTAFIX sāknētāju](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
nRF52 platē, pirms to novieto augstumā. Ar standarta sāknētāju neizdevušos
atjauninājumu var salabot tikai ar USB. Ar OTAFIX plate atgriežas
atjaunināšanas režīmā, un tu mēģini vēlreiz ar Bluetooth. `get bootloader.ver` parāda,
kurš sāknētājs platē ir: ar OTAFIX atbildē būs `OTAFIX`.

Pēc atjaunināšanas `ver` parāda programmaparatūras versiju, kas pašlaik darbojas.

**ESP32 plates**, piemēram, Heltec V3 un V4:

1. No tīmekļa flešotāja lejupielādē savas plates **non-merged** `.bin` failu: to, kura nosaukumā nav vārda "merged".
2. Ievadi `start ota`. Retranslators atver WiFi tīklu ar nosaukumu `MeshCore-OTA` un atbild ar savas augšupielādes lapas adresi.
3. WiFi darbības zonā pieslēdz tālruni vai klēpjdatoru šim tīklam, atver adresi un augšupielādē failu.

## Juridiskie ierobežojumi {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
MeshCore Eiropas priekšiestatījumi izmanto apakšjoslu **869.40-869.65 MHz**. ES, Apvienotajā Karalistē, Šveicē un Norvēģijā to bez licences drīkst izmantot maza darbības rādiusa ierīces, ievērojot šos ierobežojumus:

- izstarotā jauda nepārsniedz **500 mW e.r.p.**;
- **darba cikls nepārsniedz 10%**: katra ierīce raida ne vairāk kā 360 sekundes jebkurā stundā. Ierīce drīkst tā vietā izmantot klausīšanos pirms raidīšanas (listen-before-talk) ar adaptīvu frekvences maiņu (adaptive frequency agility), kā noteikts ETSI EN 300 220-2;
- visam signālam, kura platums nepārsniedz 250 kHz, jāpaliek apakšjoslas robežās.

Josla ir koplietojama: tu nedrīksti traucēt licencētiem dienestiem, un citi var traucēt tev.
Radio ierīcei jābūt ar CE marķējumu (Lielbritānijā ar CE vai UKCA).
{{< /callout >}}

Avoti: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845), 1. pielikums, josla h1.7; [Komisijas Lēmums 2006/771/EK](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) un tā grozījumi; [ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), josla O.

### Jauda: e.r.p. un tava antena {#erp}

Ierobežojums attiecas uz *izstaroto* jaudu, ko mēra attiecībā pret vienkāršu dipola antenu (e.r.p.). Antenas pastiprinājums ieskaitās, kabeļa zudumi atskaitās. Ražotāji norāda antenas pastiprinājumu dBi vienībās, un tas ir par 2.15 dB vairāk nekā tas pats pastiprinājums dBd vienībās (attiecībā pret dipolu). Šai summai jābūt 27 dBm (500 mW) vai mazākai:

> raidīšanas jauda (dBm) + antenas pastiprinājums (dBi) − kabeļa zudumi (dB) − 2.15 ≤ 27

- Plate raida 22 dBm 5 dBi antenā caur kabeli ar 1 dB zudumiem: 22 + 5 − 1 − 2.15 = 23.85 dBm, aptuveni 240 mW e.r.p. Tas iekļaujas ierobežojumā.
- Plate ar 30 dBm (1 W) pastiprinātāju raida 3 dBi antenā: 30 + 3 − 2.15 = 30.85 dBm, aptuveni 1.2 W e.r.p. Tas pārsniedz ierobežojumu, tāpēc samazini raidīšanas jaudu.

Ar `set tx` tu iestati LoRa mikroshēmas izejas jaudu dBm vienībās. Pašas SX1262 mikroshēmas maksimums ir 22 dBm, un programmaparatūra ievadīto skaitli nepārbauda. Plates ar papildu pastiprinātāju, piemēram, Heltec V4 vai Station G2, raida daudz lielāku jaudu par iestatīto skaitli. Pirms iestatīšanas apskati ražotāja tabulu un sāc ar mazu vērtību.

### Darba cikls {#duty-cycle}

Retranslators raida visiem apkārtējiem, tāpēc tas iztērē savu ētera laiku ātrāk nekā companion ierīce. MeshCore darba cikla ierobežotāja noklusējuma vērtība ir 50%, kas ir vairāk, nekā šajā joslā atļauts. Katrā retranslatorā iestati 10%:

```text
set dutycycle 10
```

### Frekvences precizitāte {#frequency}

EU/UK (Narrow) kanāls ar 869.618 MHz frekvenci un 62.5 kHz joslas platumu sniedzas līdz 869.649 MHz: mazāk nekā 1 kHz zem apakšjoslas augšējās robežas. Signālam jāpaliek joslā jebkurā temperatūrā. Tam vajag temperatūras kompensētu kvarca rezonatoru (TCXO). Tas ir gandrīz visās pašreizējās platēs. Vecākas plates bez tā, piemēram, Heltec V2, novirzās pārāk tālu, lai uzticami darbotos ar 62.5 kHz.

### Piezīmes par valstīm {#countries}

- **ES dalībvalstīm** šī apakšjosla jādara pieejama ar šiem nosacījumiem (Lēmums 2006/771/EK, 3. pants).
- **Apvienotā Karaliste:** tie paši ierobežojumi, Ofcom dokumentā [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Šveice un Lihtenšteina:** tie paši ierobežojumi, OFCOM dokumentā [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norvēģija:** tie paši ierobežojumi, [noteikumos par vispārējām atļaujām](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Šīs piezīmes nav juridiska konsultācija. Noteikumi mainās. Ja šaubies, jautā savas valsts regulatoram.

## Uzstādīšanas pārbaudes saraksts {#checklist}

Pirms uzstādi retranslatoru augstumā, izskati
[retranslatora pārbaudes sarakstu](/guides/repeater-checklist/). Tajā ir katrs
pārbaudāmais punkts kopā ar komandu, kas to parāda.
