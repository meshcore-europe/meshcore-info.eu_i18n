---
title: Antenen gida
lead: Ondo muntatutako antena egokiarekin urrunago iristen zara potentzia gehiagorekin baino. Egiaztatu companion gailuaren antena, eta gero aukeratu, konektatu eta muntatu errepikagailu baterako antena.
description: 'Aukeratu eta muntatu MeshCore antena bat 868 MHz-erako: companion gailuaren whip antena egiaztatzea, antena motak eta irabazia, konektoreak, kablearen galera metro bakoitzean, iragazkiak, muntaketa eta irabaziak legezko mugan duen eragina.'
eyebrow: Companion eta errepikagailua · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-11-02'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Altuerak, ondo doitutako antenak eta kable laburrak irismen handiagoa ematen dute
edozein miliwatt gehigarrik baino. Gida hau companion gailuarekin hasten da: mezuak
bidaltzeko erabiltzen duzun irratiarekin. Ondoren errepikagailuaren antena azaltzen du.
Errepikagailua teilatu edo masta batetik mezuak aurrera bidaltzen dituen nodoa da.

## Zure companion gailua {#companion}

{{< callout type="warning" >}}
Konektatu antena irratia piztu aurretik. Antenarik gabe transmititzen duen LoRa
irrati batek bere txipa honda dezake.
{{< /callout >}}

Plakarekin batera etorri den antena nahikoa da. Konektatu, eutsi nodoari zutik eta
hasi mezuak bidaltzen. Companion gailuan antena hobea jarrita gutxi irabazten duzu.
Irismenean dagoen errepikagailu batekin asko irabazten duzu.

Erosi aparteko whip antena bat soilik datorrena hautsita badago edo falta bada.
868 MHz-erako saltzen diren whip antena batzuk ez daude maiztasun horretara doituta.
Fidatu aurretik, [egiaztatu NanoVNA batekin](#nanovna), poltsikoko antena-analizatzaile
batekin, edo hartu mailegatuta ondo dabilen plaka baten antena.

Transmisore indartsu baten ondoan dagoen nodoak behar baino gutxiago entzuten du.
Irratiaren eta antenaren arteko [SAW (gainazaleko uhin akustikoen) iragazki](#filters)
txiki batek transmisore hori hargailutik kanpo uzten du. Begiratu lehenik haren
datu-orria:

- **Sarrerako potentzia maximoa.** Zure transmisioa ere iragazkitik pasatzen da.
  22 dBm-n (160 mW) transmititzen duen plaka batek 15 dBm-rako iragazkia hausten du.
- **Pasabanda.** Zure aurrezarpenaren maiztasuna barne hartu behar du.
  868.65 eta 869.25 MHz arteko iragazkiak ez du pasatzen uzten 869.618 MHz-eko
  EU/UK (Narrow) kanala.

## Errepikagailu baterako antena motak {#types}

Sareko antena guztiak zutik daude. Aukeratu mota, iritsi nahi duzun nodoen
kokapenaren arabera:

- **Beira-zuntzezko antena kolineala.** Mastako hodi zuria, horizonte osoan irabazia
  duena. Herri bat estaltzen duen errepikagailurako aukera arrunta da.
- **Dipoloa.** Laburragoa da, irabazi txikiagoa du eta sorta altua. Kolineal batek
  baino hobeto iristen da zure azpitik eta gainetik dauden nodoetara, adibidez haran
  baten gaineko muino batetik.
- **Yagi.** Elementu gurutzatuak dituen besoa, leku bakarrera zuzenduta. Urruneko
  errepikagailu bakar batera iristen da, eta beste gutxitara. Muntatu elementuak
  zutik, polarizazioak elementuen norabideari jarraitzen baitio.

## Irabazia eta sorta {#gain}

Irabaziak ez du potentziarik gehitzen. Gora eta behera joango litzatekeen seinalea
horizontean zehar bidaltzen du. Linterna bat fokatzea bezala da: pila bera, sorta
luzeagoa eta estuagoa. Fabrikatzaile bereko dipolo batek eta kolineal batek
hori erakusten dute:

| Antena | Irabazia | Sorta-zabalera bertikala |
|---|---|---|
| Dipoloa (Sirio SO 868-915-2) | 2.2 dBi | 88 gradu |
| Beira-zuntzezko kolineala (Sirio SPO 868-915-6) | 5.8 dBi | 23 gradu |

{{< gain >}}

Diagramak masta ebakitzen du, albotik ikusita. Biratu mastaren inguruan eta sorta
osoa izango duzu: dipoloarena donut bat da, kolinealarena disko lau bat. Zutik dagoen
antenak berdin igortzen du inguruko norabide guztietara. Marraztutako sortatik kanpo
seinalea ez da gelditzen: ahulagoa da, baina nahikoa da hurbileko nodo batentzat.

Teilatu batean sorta laua nahi duzu. Nodoetatik oso gora dagoen muino batean,
23 graduko sorta haien buruen gainetik pasatzen da, eta dipolo batek estaltzen ditu.
Yagi batekin are nabarmenagoa da: 16.6 dBi, 23 gradu altu eta 25 gradu zabal den sorta
batean (Amphenol Procom 7176870), eta ezer ere ez alboetara.

Irabazia erreferentzia baten aldean neurtzen da. dBi unitateak norabide guztietan
berdin igortzen duen antena ideal batekin alderatzen du. dBd unitateak uhin-erdiko
dipolo batekin alderatzen du, eta dipolo horrek berak 2.15 dBi ditu: antenarik
sinpleenak ere ez du ezer igortzen zuzen gora edo behera. Dipolo luzeago batek,
1.25 uhin-luzerakoak, 5.2 dBi lortzen ditu. Kolineal batek, berriz, uhin-erdiko
elementuak bata bestearen gainean pilatzen ditu: zenbat eta gehiago pilatu, orduan eta
irabazi handiagoa. Estutu seinale bera espazioaren erdian, eta han bi aldiz indartsuagoa
da: 3 dB. Laurden batean, 4 aldiz indartsuagoa: 6 dB. Fabrikatzaileek
irabazia dBi-tan ematen dute. Legezko muga dBd-tan neurtzen da, ikus
[Legezko mugaren barruan](#legal).

### Zein irabazi zure kokapenerako {#choose-gain}

- **Muinoak, haranak edo hiri trinkoa: 3 dBi inguru.** Sorta altua zure gainetik eta
  azpitik dauden nodoetara iristen da, baita bidean dauden maldak eta eraikinak
  inguratuz ere. Alderantziz ere balio du: haran batetik, sorta laua goiko muinoko
  errepikagailuaren azpitik pasatzen da. RAKwireless RAKARG12 antena horietako bat
  da: 36 cm-ko beira-zuntzezko hodia.
- **Hiri-inguruak edo teilatu baxuko herria: 5 eta 6 dBi artean.** Beira-zuntzezko
  kolineal arrunta.
- **Lur laua eta irekia: 8 eta 10 dBi artean.** Sortarik lauena da horizontean zehar
  urrunen iristen dena. Goian muntatuta, hurbileko nodoen gainetik pasatzen da.

Izenean ageri den irabazia antenaren banda osoko baliorik onena da. RAKARG12 antenak,
3 dBi-ko gisa saltzen dutenak, 2.8 dBi ditu 865 eta 870 MHz artean. Begiratu
datu-orriko irabazi-taulan zure aurrezarpenaren maiztasunari dagokion balioa.

7 dBi-tik gora, 22 dBm-ko plaka batek legezko muga gainditzen du, kablearen eta
iragazkiaren galerak aldea konpentsatzen ez badu. Jaitsi transmisio-potentzia
horretara egokitzeko.

Irabazi handiak nodoak non dauden dakizunean bakarrik laguntzen du: errepikagailu
baten inguruko horizontean, edo urruneko errepikagailu bakar batean Yagi batekin.
Eskuan duzun companion gailua norabide guztietara begira dago, beraz berarekin datorren
irabazi txikia da egokiena.

## Zergatik bertikalean {#vertical}

Antenek elkar hobekien entzuten dute norabide berean jarrita daudenean. Galera haien
arteko angeluarekin hazten da: 45 graduk 3 dB kentzen dituzte, zure seinalearen erdia.
90 gradutan, antena etzan bat zutik dagoen baten aurrean, teorian ez da ezer iristen.
Sarea zutik dago, beraz zure antenak ere zutik egon behar du. Hau mahai gaineko
companion gailuari ere badagokio: etzanda jartzen baduzu, inguruko nodo guztiek
gutxiago entzuten dute.

## Konektoreak {#connectors}

Eskatu antena zure plakak duen konektorearekin. Egokitzaile bakoitza zigilatu beharreko
beste juntura bat da, eta seinale gehiago galtzen da.

- **SMA.** 6 mm inguruko zabalera duen konektore hariztatua. Plaka gehienetako
  hartuneak zulo bat du erdian, eta antenak pina du. Mota honetako konektoreak
  0.03 dB inguru galtzen ditu 868 MHz-etan.
- **RP-SMA.** SMAren gorputz eta hari berak ditu, pina eta zuloa trukatuta. SMA
  dirudi, baina ez da harekin konektatzen. Egiaztatu zure plakak zein duen eskatu
  aurretik.
- **U.FL (IPEX).** Plakan bertan dagoen presiozko hartune txiki-txikia. Pigtail kable
  labur bat doa handik kaxako SMA hartune batera. 30 konexio-ziklotarako dago
  egina, beraz konektatu behin eta utzi horrela.
- **N.** Beira-zuntzezko antenetan eta kable lodian dagoen konektore hariztatu handia.
  Gehienez 0.05 dB galtzen ditu. Errepikagailuak egokitzaile edo pigtail bat behar
  du N konektoretik plakaren SMAra.

## Kablearen galera {#cable}

Kableak seinalea kentzen du antenatik atera aurretik, bi norabideetan. 3 dB zure
potentziaren erdia da. Fabrikatzaileen balioak metro bakoitzean, 868 eta 900 MHz artean:

| Kablea | Galera metro bakoitzean | Galera 5 m-tan |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

RG174 kablearen 3 metrok (plaka askorekin datorren pigtail mehea) zure potentziaren
erdia galtzen dute. Muntatu plaka antenaren ondoan pigtail labur batekin, edo eraman
kable lodia antenaraino. Gehitu batuketan bideko egokitzaile eta iragazki guztiak.

## Iragazkiak {#filters}

Iragazkia irratiaren eta antenaren artean jartzen da. Zure banda pasatzen uzten du eta
gainerakoa blokeatzen du, inguruko transmisore indartsu batek hargailua itota utz ez
dezan. Iragazkia behar duzu nodo batek beste transmisore batzuetatik gertu behar baino
gutxiago entzuten duenean. Telefonia mugikorreko oinarrizko estazioak dituen masta bateko
errepikagailua horrelako nodoa da. Iragazkiak seinalea kentzen du bi norabideetan:
kontatu haren galera kablearena bezala.

| | SAW iragazkia | Barrunbe-iragazkia |
|---|---|---|
| Tamaina | Milimetro gutxi batzuk, plaka txiki batean | Metalezko bloke edo hodia |
| Iragazki on baten galera | 2 dB baino gutxiago | 1 dB baino gutxiago |
| Iragazki on baten sarrerako potentzia maximoa | 500 mW | Zenbait watt |

Adibidez, sysmocom cf866.5-kt30 gailua 863 eta 870 MHz arteko barrunbe-iragazkia da. Gehienez
1.0 dB galtzen ditu eta 30 W onartzen ditu. Barruan erabiltzeko egina dago, beraz jarri
mastan kaxa zigilatu batean.

Iragazkiak oso desberdinak dira, beraz begiratu datu-orria erosi aurretik. Sarrerako
potentzia nominalak zure transmisio-potentzia gainditu behar du, eta pasabandak zure
aurrezarpenaren maiztasuna barne hartu behar du.

## Muntaketa {#mounting}

- **Teilatuaren ertzetik gora.** Antenak bista garbia behar du estaltzen duen
  norabide bakoitzean. Inguruko teilatuak baino metro gutxi batzuk gorago jartzeak ere
  laguntzen du. Errepikagailuen gidako [Aukeratu kokapena](/repeater-guide/#site)
  atalak bista nola egiaztatu erakusten du.
- **Metaletik urrun.** Antenaren ondoko kanalek, mastek, beste antenek eta metalezko
  teilatuek haren irradiazio-eredua eta doikuntza aldatzen dituzte. Muntatu mastaren
  goialdean, ez ondoan.
- **Zutik.** Erabili burbuila-maila; ikus [Zergatik bertikalean](#vertical).
- **Tanta-begizta.** Utzi kablea konektorearen azpitik zintzilik gora edo barrura joan
  aurretik. Horrela ura tantaka erortzen da, junturara isuri beharrean.
- **Zigilatu kanpoko konektore guztiak.** Konektoreko urak galera handitzen du eta
  pina herdoiltzen du. Zigilatu euriaren aurka eta egiaztatu zigilua urtero.
- **Tximistak.** Teilatuko antena jomuga da. Kablean jarritako gas-deskargako
  babesgailua gaintentsio batekin aktibatzen da eta lurrera bidaltzen du. Lurreratzeko,
  jarraitu errepikagailuen gidako [Hardwarea](/repeater-guide/#hardware) atalari eta
  zure tokiko arauei.

## Legezko mugaren barruan {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
Europan MeshCore-k 869.40-869.65 MHz azpibanda erabiltzen du, gehienez **500 mW**-eko
potentzia erradiatu eraginkorrarekin (e.r.p.). Mugak antenatik ateratzen dena neurtzen
du: antenaren irabazia gehitu egiten da, kablearen eta iragazkiaren galera kendu.
dBi-tako irabaziak 2.15 dB gutxiago balio du, muga dipolo baten aldean neurtzen baita.
{{< /callout >}}

5.8 dBi-ko kolineala 22 dBm-ko plaka batean mugaren barruan geratzen da. Antena bera
anplifikadoredun plaka batean ez, transmisio-potentzia jaitsi arte. Errepikagailuen
gidako [Potentzia: e.r.p. eta zure antena](/repeater-guide/#erp) atalean daude batuketa
eta 2 adibide landu.

## Egiaztatu antena NanoVNA batekin {#nanovna}

NanoVNA poltsikoko sare-analizatzaile bektoriala da. Antena zein maiztasunetara
doituta dagoen erakusten du, eta horrela muntatu aurretik dakizu. NanoVNA-H gailuak
1.5 GHz-era arte neurtzen du, eta tarte horrek 868 MHz hartzen du barne.

1. Kalibratu 800 eta 950 MHz artean, kitaren open, short eta load piezekin.
2. Konektatu antena nodoan erabiliko duen egokitzailearen bidez. Eutsi zutik, zure
   gorputzetik eta mahaitik urrun.
3. Irakurri SWR (uhin geldikorren erlazioa) kurba: antenak zenbat seinale itzultzen
   duen erakusten du. Beherakadak zure aurrezarpenaren maiztasunean egon behar du:
   869.618 MHz EU/UK (Narrow) aurrezarpenerako. Beherakada ehunka MHz harago badago,
   antena beste banda baterako egina dago.

Uhin-laurden batek 86 mm ditu 868 MHz-etan (uhin-luzera 345 mm da). Luzerak bakarrik ez
dizu esaten zein den banda, fabrikatzaileek whip antenak tolestu eta kargatu egiten
baitituzte. NanoVNA gailuak bai.

## Iturriak {#sources}

- Kablearen galera: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  Huber+Suhner RG316 datu-orria,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  Times Microwave LMR-240 eta LMR-400 datu-orriak,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antenak: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  Sirio SO 868-915-2 datu-orria,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Irabazia, espazio txikiagoan estutako seinale gisa: [RF Cafe, antenen sarrera](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Konektoreak: Rosenberger 32S102 (SMA) eta 53S101 (N) datu-orriak, Hirose U.FL
  katalogoa.
- Iragazkiak: sysmocom cf866.5-kt30 produktu-orria,
  [Citel gas-deskargako babesgailuak](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarizazio-galera: [University of Toronto, Friis efektuak](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipoloaren irabazia luzeraren arabera: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Uhin-luzera: argiaren abiadura, [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c) iturritik.
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Legezko muga: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  1. eranskina, h1.7 banda; [errepikagailuen gidak](/repeater-guide/#legal) gainerakoak
  zerrendatzen ditu.
