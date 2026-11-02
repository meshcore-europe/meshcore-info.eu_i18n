---
title: Antennen-Guide
lead: Déi richteg Antenn, gutt montéiert, kënnt méi wäit wéi méi Leeschtung. Kontrolléier d'Antenn op dengem Companion. Wiel dann eng fir e Repeater, schléiss se un a montéier se.
description: 'Wiel a montéier eng MeshCore-Antenn fir 868 MHz: Stabantenn vun engem Companion kontrolléieren, Antennentypen a Gain, Stecker, Kabelverloscht pro Meter, Filteren, Montage a wéi de Gain bei der gesetzlecher Limitt zielt.'
eyebrow: Companion a Repeater · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-11-02'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Mat Héicht, enger ofgestëmmter Antenn an engem kuerze Kabel gewënns du méi
Reechwäit wéi mat all zousätzleche Milliwatt. Dëse Guide fänkt mam Companion
un, dem Radio, mat deem s du Noriichte schécks. Duerno geet et ëm d'Antenn op
engem Repeater, engem Knuet, deen Noriichte vun engem Daach oder Mast aus
weiderschéckt.

## Däi Companion {#companion}

{{< callout type="warning" >}}
Schléiss d'Antenn un, ier s du de Radio uschalts. E LoRa-Radio, deen ouni
Antenn sent, kann säin eegene Chip beschiedegen.
{{< /callout >}}

D'Antenn, déi mat dengem Board komm ass, geet duer. Schléiss se un, hal de
Knuet oprecht a fänk un, Noriichten ze schécken. Eng besser Antenn op engem
Companion bréngt wéineg, e Repeater a Reechwäit bréngt vill.

Keef eng separat Stabantenn nëmmen, wann déi matgeliwwert futti ass oder feelt.
Net all Stabantenn, déi fir 868 MHz verkaf gëtt, ass och dorop ofgestëmmt.
[Kontrolléier se mat engem NanoVNA](#nanovna), engem Antennenanalysator fir an
d'Täsch, ier s du hir vertraus, oder léin der eng vun engem Board, dat
funktionéiert.

E Knuet niewent engem staarke Sender héiert manner, wéi e sollt. E klenge
[SAW-Filter (surface acoustic wave)](#filters) tëscht dem Radio an der Antenn
hält dee Sender aus dem Empfänger eraus. Kuck als éischt a säin Dateblat:

- **Maximal Agangsleeschtung.** De Filter läit och um Wee vun denger eegener
  Iwwerdroung. E Board, dat mat 22 dBm (160 mW) an e Filter fir 15 dBm sent,
  mécht de Filter futti.
- **Duerchlassband.** Et muss d'Frequenz vun dengem Preset enthalen. E Filter
  fir 868.65 bis 869.25 MHz léisst den EU/UK (Narrow)-Kanal op 869.618 MHz net
  duerch.

## Antennentypen fir e Repeater {#types}

All Antenn am Mesh steet oprecht. Wiel den Typ no der Plaz, wou d'Kniet sinn,
déi s du erreeche wëlls:

- **Glasfaser-Kollinearantenn.** E wäisse Rouer op engem Mast, mat Gain
  ronderëm um ganzen Horizont. Dat ass d'Standardwiel fir e Repeater, deen eng
  Stad ofdeckt.
- **Dipol.** Méi kuerz, mat manner Gain an engem héije Stral. En erreecht
  Kniet ënner an iwwer dir besser wéi eng Kollinearantenn, zum Beispill vun
  engem Hiwwel iwwer engem Dall.
- **Yagi.** En Träger mat Querelementer, deen op eng Plaz gezielt ass. Si
  erreecht een eenzege Repeater wäit ewech a soss wéineg. Montéier se mat den
  Elementer oprecht, well hir Polarisatioun den Elementer follegt.

## Gain an de Stral {#gain}

Gain bréngt keng zousätzlech Leeschtung. En hëlt d'Signal, dat no uewen an no
ënne géif goen, a schéckt et laanscht den Horizont. Dat ass wéi bei enger
Täschelamp, déi s du fokusséiers: déi selwecht Batterie, e méi laangen a méi
schmuele Stral. En Dipol an eng Kollinearantenn vum selwechte Fabrikant
weisen dat:

| Antenn | Gain | Vertikal Stralbreet |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 Grad |
| Glasfaser-Kollinearantenn (Sirio SPO 868-915-6) | 5.8 dBi | 23 Grad |

{{< gain >}}

D'Diagramm weist e Schnëtt duerch de Mast, vun der Säit gesinn. Dréi et ëm de
Mast an du hues de ganze Stral: en Donut beim Dipol, eng flaach Scheif bei
der Kollinearantenn. Eng oprecht Antenn sent an all Richtung ronderëm sech
d'selwecht. Baussent dem gezeechente Stral hält d'Signal net op. Et ass méi
schwaach, awer nach ëmmer staark genuch fir e Knuet an der Géigend.

Op engem Daach wëlls du e flaache Stral. Op engem Hiwwel héich iwwer de Kniet
geet e Stral vun 23 Grad iwwer hir Käpp ewech, en Dipol deckt se of. Eng Yagi
dreift dat nach méi wäit: 16.6 dBi an engem Stral, deen 23 Grad héich an 25
Grad breet ass (Amphenol Procom 7176870), an op d'Säiten näischt.

Gain bezitt sech op eng Referenz. dBi vergläicht mat enger idealer Antenn, déi
an all Richtung d'selwecht sent. dBd vergläicht mat engem Hallefwellen-Dipol,
deen selwer 2.15 dBi huet: och déi einfachst Antenn sent näischt riicht no uewen
oder no ënnen. E méi laangen Dipol vun 1.25 Wellelängten erreecht 5.2 dBi. Eng
Kollinearantenn stapelt amplaz Hallefwellen-Elementer iwwerteneen: wat se méi
stapelt, wat de Gain méi héich gëtt. Dréck dat selwecht Signal an déi hallef
Plaz, an et ass do duebel esou staark: 3 dB. An e Véierel, 4 Mol esou staark:
6 dB. D'Fabrikanten ginn de Gain an dBi un, d'gesetzlech Limitt zielt an dBd,
kuck [Bannent der gesetzlecher Limitt](#legal).

### Wéi ee Gain fir däi Standuert {#choose-gain}

- **Hiwwelen, Däller oder eng dicht Stad: ongeféier 3 dBi.** Den héije Stral
  erreecht Kniet iwwer an ënner dir, an och ronderëm d'Hänken an d'Gebaier, déi
  am Wee stinn. Dat gëllt och ëmgedréint: aus engem Dall geet e flaache Stral
  ënner engem Repeater um Hiwwel driwwer duerch. D'RAKwireless RAKARG12 ass esou
  eng Antenn: e Glasfaser-Rouer vun 36 cm.
- **Viruerter oder eng Stad mat nidderegen Diech: 5 bis 6 dBi.** Dat ass déi
  üblech Glasfaser-Kollinearantenn.
- **Flaacht, oppent Land: 8 bis 10 dBi.** De flaachste Stral kënnt laanscht den
  Horizont am wäitsten. Héich montéiert geet en iwwer d'Kniet an der Géigend
  ewech.

De Gain am Numm ass de beschte Wäert iwwer dat ganzt Band vun der Antenn.
D'RAKARG12, déi als 3 dBi verkaf gëtt, huet 2.8 dBi op 865 bis 870 MHz. Liess an
der Gain-Tabell vum Dateblat de Wäert bei der Frequenz vun dengem Preset.

Iwwer 7 dBi geet e Board mat 22 dBm iwwer déi gesetzlech Limitt, ausser de
Verloscht vu Kabel a Filter gläicht den Ënnerscheed aus. Setz d'Sendeleeschtung
entspriechend erof.

E héije Gain hëlleft nëmmen, wann s du weess, wou d'Kniet sinn: laanscht den
Horizont ronderëm e Repeater, oder bei engem eenzege Repeater wäit ewech fir eng
Yagi. E Companion an denger Hand weist an all Richtung, dofir passt deen
nidderege Gain, mat deem e komm ass, am beschten.

## Firwat vertikal {#vertical}

Antennen héiere sech am beschten, wa se an déi selwecht Richtung weisen. De
Verloscht wiisst mam Wénkel tëscht hinnen: 45 Grad kaschten 3 dB, d'Halschent
vun dengem Signal. Bei 90 Grad, also enger flaacher Antenn géint eng oprecht,
kënnt theoretesch näischt un. D'Mesh steet oprecht, also steet deng Antenn och
oprecht. Dat gëllt och fir e Companion um Bureau: wann s du e flaach lees, héiert
all Knuet ronderëm dech manner.

## Stecker {#connectors}

Bestell d'Antenn mam Stecker, deen däi Board huet. All Adapter ass eng
Verbindung méi, déi s du ofdichte muss, a méi Signal, dat verluer geet.

- **SMA.** E Schraubstecker, deen ongeféier 6 mm breet ass. D'Buchs op de
  meeschte Boards huet e Lach an der Mëtt, d'Antenn huet de Pin. E Stecker vun
  dëser Aart verléiert ongeféier 0.03 dB bei 868 MHz.
- **RP-SMA.** Dee selwechte Kierper an dat selwecht Gewënn wéi SMA, mee Pin a
  Lach si getosch. E gesäit aus wéi SMA a passt net drop. Kontrolléier, wéi een
  däi Board huet, ier s du bestells.
- **U.FL (IPEX).** Eng winzeg Steckbuchs direkt um Board. E kuerze Pigtail-Kabel
  geet dovun zu enger SMA-Buchs am Gehäis. Si ass fir 30 Steckzyklen ausgeluecht,
  also schléiss se eemol un a looss se dann a Rou.
- **N.** De grousse Schraubstecker op Glasfaser-Antennen an op décke Kabelen. E
  verléiert héchstens 0.05 dB. E Repeater brauch een Adapter oder Pigtail vun N
  op de SMA vum Board.

## Kabelverloscht {#cable}

De Kabel kascht Signal, ier et d'Antenn verléisst, a béid Richtungen. 3 dB sinn
d'Halschent vun denger Leeschtung. D'Wäerter vun de Fabrikante pro Meter, bei
868 bis 900 MHz:

| Kabel | Verloscht pro Meter | Verloscht op 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 Meter RG174, dee dënne Pigtail, deen a ville Boards dobäi ass, verléieren
d'Halschent vun denger Leeschtung. Montéier d'Board mat engem kuerze Pigtail bei
d'Antenn, oder zéi en décke Kabel bis dohin. Rechen all Adapter an all Filter
um Wee an d'Zomm mat.

## Filteren {#filters}

E Filter läit tëscht dem Radio an der Antenn. E léisst däi Band duerch a blockéiert
de Rescht, sou datt e staarke Sender an der Géigend den Empfänger net iwwerdeckt.
Du brauchs een, wann e Knuet bei anere Sender manner héiert, wéi e sollt. E
Repeater op engem Mast mat Basisstatioune vum Handysnetz ass esou e Knuet. E Filter
kascht Signal a béid Richtungen: ziel säi Verloscht wéi dee vum Kabel.

| | SAW-Filter | Cavity-Filter |
|---|---|---|
| Gréisst | E puer Millimeter, op engem klenge Board | E Metallblock oder e Metallrouer |
| Verloscht vun engem gudden | ënner 2 dB | ënner 1 dB |
| Maximal Agangsleeschtung vun engem gudden | 500 mW | e puer Watt |

De sysmocom cf866.5-kt30 zum Beispill ass e Cavity-Filter fir 863 bis 870 MHz, deen
héchstens 1.0 dB verléiert an 30 W aushält. E gouf fir dobanne gemaach, also setz
e op engem Mast an eng dicht Këscht.

Filteren ënnerscheede sech staark, also kuck an d'Dateblat, ier s du ee keefs.
Déi ausgewisen Agangsleeschtung muss iwwer denger Sendeleeschtung leien, an
d'Duerchlassband muss d'Frequenz vun dengem Preset enthalen.

## Montage {#mounting}

- **Iwwer dem Daachrand.** D'Antenn brauch eng fräi Siicht an all Richtung, déi si
  ofdeckt. Schonn e puer Meter iwwer den Diech ronderëm hëllefen. [Wiel eng
  Plaz](/repeater-guide/#site) am Repeater-Guide weist, wéi s du d'Siicht
  kontrolléiers.
- **Ewech vu Metall.** Daachkéiler, Masten, aner Antennen a Metalldiech niewent der
  Antenn veränneren hir Charakteristik an hir Ofstëmmung. Montéier se uewen um Mast,
  net dernieft.
- **Oprecht.** Huel eng Waasserwo, kuck [Firwat vertikal](#vertical).
- **Drëpsschleef.** Looss de Kabel ënner dem Stecker hänken, ier en no uewen oder
  eran geet. Dann dreeft d'Waasser of, amplaz an d'Verbindung ze lafen.
- **Dicht all Stecker dobaussen of.** Waasser an engem Stecker erhéicht de Verloscht
  a léisst de Pin korrodéieren. Dicht e géint de Reen of a kontrolléier d'Dichtung
  all Joer.
- **Blëtz.** Eng Antenn op engem Daach ass en Zil. E Gasentladungsableeder am Kabel
  léist bei enger Iwwerspannung aus a leet se an de Buedem. Folleg
  [Hardware](/repeater-guide/#hardware) am Repeater-Guide an de lokale Reegele fir
  d'Äerdung.

## Bannent der gesetzlecher Limitt {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
An Europa benotzt MeshCore d'Ënnerband 869.40-869.65 MHz, mat héchstens **500 mW**
effektiver Stralungsleeschtung (e.r.p.). D'Limitt zielt dat, wat d'Antenn verléisst:
den Antennegain kënnt dobäi, de Verloscht vu Kabel a Filter geet dervun of. Gain an
dBi zielt 2.15 dB manner, well d'Limitt géint en Dipol gemooss gëtt.
{{< /callout >}}

Eng Kollinearantenn mat 5.8 dBi op engem Board mat 22 dBm bleift bannent der Limitt.
Déi selwecht Antenn op engem Board mat Verstäerker bleift net dobannen, bis s du
d'Sendeleeschtung erofsetz. [Leeschtung: e.r.p. an deng Antenn](/repeater-guide/#erp)
am Repeater-Guide huet d'Rechnung an 2 duerchgerechent Beispiller.

## Eng Antenn mat engem NanoVNA kontrolléieren {#nanovna}

En NanoVNA ass e Vektor-Netzwierkanalysator am Täscheformat. E weist, op wéi eng
Frequenz eng Antenn ofgestëmmt ass, sou datt s du et weess, ier s du se montéiers.
Den NanoVNA-H moosst bis 1.5 GHz, wat 868 MHz ofdeckt.

1. Kalibréier en fir 800 bis 950 MHz mat den Open-, Short- a Load-Stécker aus sengem
   Kit.
2. Schléiss d'Antenn iwwer den Adapter un, deen s du um Knuet benotze wäerts. Hal se
   oprecht a wäit vun dengem Kierper a vum Dësch ewech.
3. Liess d'SWR-Kurv (standing wave ratio): si weist, wéi vill Signal d'Antenn
   zréckschéckt. Den Déifpunkt muss op der Frequenz vun dengem Preset leien, 869.618
   MHz fir EU/UK (Narrow). En Déifpunkt, dee Honnerte vu MHz ewech läit, heescht, datt
   d'Antenn fir en anert Band gemaach ass.

Eng Véierelswell bei 868 MHz ass 86 mm (d'Wellelängt ass 345 mm). D'Längt eleng seet
der net, wéi ee Band et ass, well d'Fabrikante Stabantenne falen a belueden. Den
NanoVNA seet der et.

## Quellen {#sources}

- Kabelverloscht: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  d'Dateblat vum Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  d'Dateblieder vum Times Microwave LMR-240 an LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antennen: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  d'Dateblat vun der Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Gain als Signal, dat a manner Plaz gedréckt gëtt: [RF Cafe, Aféierung an d'Antennen](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Stecker: d'Dateblieder vum Rosenberger 32S102 (SMA) a 53S101 (N), de
  Katalog vum Hirose U.FL.
- Filteren: d'Produktsäit vum sysmocom cf866.5-kt30,
  [Citel Gasentladungsableeder](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarisatiounsverloscht: [University of Toronto, Friis-Effekter](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipol-Gain no Längt: [Wikipedia, Dipolantenn](https://en.wikipedia.org/wiki/Dipole_antenna).
- Wellelängt: Liichtgeschwindegkeet vum [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Gesetzlech Limitt: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Annex 1, Band h1.7; de [Repeater-Guide](/repeater-guide/#legal) lëscht de Rescht op.
