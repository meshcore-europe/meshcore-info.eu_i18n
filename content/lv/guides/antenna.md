---
title: Antenu ceļvedis
lead: Pareizā antena, labi uzstādīta, sniedzas tālāk nekā lielāka jauda. Pārbaudi sava kompanjona antenu, pēc tam izvēlies, pievieno un uzstādi antenu retranslatoram.
description: 'Izvēlies un uzstādi MeshCore antenu 868 MHz joslai: kompanjona stieņa antenas pārbaude, antenu veidi un pastiprinājums, savienotāji, kabeļa zudumi uz metru, filtri, uzstādīšana un pastiprinājuma ietekme uz likumīgo robežu.'
eyebrow: Kompanjons un retranslators · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-11-02'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Augstums, noskaņota antena un īss kabelis palielina sniedzamību vairāk nekā jebkurš papildu
milivats. Šis ceļvedis sākas ar kompanjonu, radio, no kura tu sūti ziņas.
Pēc tam tas aplūko retranslatora antenu. Retranslators ir mezgls, kas no jumta vai masta
pārsūta ziņas tālāk.

## Tavs kompanjons {#companion}

{{< callout type="warning" >}}
Pievieno antenu, pirms ieslēdz radio. LoRa radio, kas raida bez antenas,
var sabojāt pats savu mikroshēmu.
{{< /callout >}}

Ar antenu, kas nāca komplektā ar tavu plati, pietiek. Pievieno to, turi mezglu
vertikāli un sāc sūtīt ziņas. Labāka antena kompanjonam dod maz, bet retranslators
sasniedzamā attālumā dod daudz.

Atsevišķu stieņa antenu pērc tikai tad, ja komplektā iekļautā ir bojāta vai tās nav. Ne
katra stieņa antena, ko pārdod 868 MHz joslai, ir tai noskaņota. Pirms tai uzticies,
[pārbaudi to ar NanoVNA](#nanovna), kabatas antenu analizatoru, vai aizņemies antenu no
plates, kas darbojas.

Mezgls spēcīga raidītāja tuvumā dzird sliktāk, nekā vajadzētu. Neliels
[SAW (virsmas akustisko viļņu) filtrs](#filters) starp radio un antenu neļauj šim raidītājam
iekļūt uztvērējā. Vispirms pārbaudi filtra datu lapu:

- **Maksimālā ieejas jauda.** Filtrs atrodas arī tava paša raidījuma ceļā. Plate, kas raida
  ar 22 dBm (160 mW), sabojā filtru, kura nominālā jauda ir 15 dBm.
- **Caurlaides josla.** Tajā jāietilpst tava priekšiestatījuma frekvencei. Filtrs joslai
  no 868.65 līdz 869.25 MHz nelaiž cauri EU/UK (Narrow) kanālu uz 869.618 MHz.

## Retranslatora antenu veidi {#types}

Visas antenas tīklā stāv vertikāli. Izvēlies veidu pēc tā, kur atrodas mezgli, kurus gribi
sasniegt:

- **Stiklšķiedras kolineārā antena.** Balta caurule mastā, ar pastiprinājumu visapkārt gar
  apvārsni. Tā ir standarta izvēle retranslatoram, kas apkalpo pilsētu.
- **Dipols.** Īsāks, ar mazāku pastiprinājumu un augstu staru. Tas labāk nekā kolineārā
  antena sasniedz mezglus zem tevis un virs tevis, piemēram, no kalna virs ielejas.
- **Yagi.** Sija ar šķērselementiem, kas vērsta uz vienu vietu. Tā sasniedz vienu tālu
  retranslatoru un maz ko citu. Uzstādi to ar elementiem vertikāli, jo polarizācija sakrīt
  ar elementu virzienu.

## Pastiprinājums un stars {#gain}

Pastiprinājums nepievieno jaudu. Antena paņem signālu, kas ietu uz augšu un uz leju, un
sūta to gar apvārsni. Tas ir kā kabatas lukturis, kuru fokusē: tā pati baterija, garāks un
šaurāks stars. To parāda viena ražotāja dipols un kolineārā antena:

| Antena | Pastiprinājums | Vertikālais stara platums |
|---|---|---|
| Dipols (Sirio SO 868-915-2) | 2.2 dBi | 88 grādi |
| Stiklšķiedras kolineārā antena (Sirio SPO 868-915-6) | 5.8 dBi | 23 grādi |

{{< gain >}}

Diagramma rāda griezumu caur mastu, skatu no sāniem. Pagriez to ap mastu, un redzēsi visu
staru: virtuli dipolam, plakanu disku kolineārajai antenai. Vertikāla antena raida vienādi
visos virzienos ap sevi. Ārpus uzzīmētā stara signāls nepazūd. Tas ir vājāks, bet joprojām
pietiekams tuvam mezglam.

Uz jumta tev vajag plakanu staru. Kalnā augstu virs mezgliem 23 grādu stars aiziet tiem pāri
galvām, bet dipols tos aptver. Yagi antenai tas ir vēl izteiktāk: 16.6 dBi starā, kas ir
23 grādus augsts un 25 grādus plats (Amphenol Procom 7176870), un uz sāniem nekā.

Pastiprinājumu mēra attiecībā pret atskaites antenu. dBi salīdzina ar ideālu antenu, kas
raida vienādi visos virzienos. dBd salīdzina ar pusviļņa dipolu, kuram pašam ir 2.15 dBi:
pat vienkāršākā antena neko neraida taisni uz augšu vai uz leju. Garāks dipols, 1.25 viļņa
garumā, sasniedz 5.2 dBi. Kolineārajai antenai turpretī pusviļņa elementi ir cits virs
cita: jo vairāk elementu, jo lielāks pastiprinājums. Saspied to pašu signālu uz pusi mazākā
telpā, un tur tas ir divreiz stiprāks: 3 dB. Ceturtdaļā telpas tas ir 4 reizes stiprāks:
6 dB. Ražotāji pastiprinājumu norāda dBi, bet likumīgo robežu rēķina dBd, skat.
[Likumīgās robežās](#legal).

### Kāds pastiprinājums der tavai vietai {#choose-gain}

- **Pakalni, ielejas vai blīva pilsēta: apmēram 3 dBi.** Augstais stars sasniedz mezglus virs
  tevis un zem tevis, kā arī tiek apkārt nogāzēm un ēkām ceļā. Tas darbojas arī otrādi: no
  ielejas plakans stars aiziet zem retranslatora kalnā virs tevis. Viens piemērs ir
  RAKwireless RAKARG12, 36 cm gara stiklšķiedras caurule.
- **Priekšpilsētas vai pilsēta ar zemiem jumtiem: 5 līdz 6 dBi.** Standarta stiklšķiedras
  kolineārā antena.
- **Līdzena, atklāta vieta: 8 līdz 10 dBi.** Visplakanākais stars sniedzas vistālāk gar
  apvārsni. Augstu uzstādīts, tas aiziet pāri tuvajiem mezgliem.

Nosaukumā minētais pastiprinājums ir labākais rādītājs visā antenas joslā. RAKARG12, ko
pārdod kā 3 dBi antenu, joslā no 865 līdz 870 MHz pastiprinājums ir 2.8 dBi. Datu lapas
pastiprinājuma tabulā skaties vērtību sava priekšiestatījuma frekvencē.

Virs 7 dBi plate ar 22 dBm pārsniedz likumīgo robežu, ja vien kabeļa un filtra zudumi
nekompensē starpību. Attiecīgi samazini raidīšanas jaudu.

Liels pastiprinājums palīdz tikai tad, ja zini, kur atrodas mezgli: gar apvārsni ap
retranslatoru vai, Yagi antenas gadījumā, pie viena tāla retranslatora. Kompanjons tavā rokā
ir vērsts uz visām pusēm, tāpēc tam vislabāk der mazais pastiprinājums, ar kādu to piegādā.

## Kāpēc vertikāli {#vertical}

Antenas cita citu dzird vislabāk, kad tās ir vērstas vienā virzienā. Zudumi aug līdz ar leņķi
starp tām: pie 45 grādiem tu zaudē 3 dB, pusi sava signāla. Pie 90 grādiem (guļus antena pret
vertikālu) teorētiski nekas nepienāk. Tīklā antenas stāv vertikāli, tāpēc arī tavai jāstāv
vertikāli. Tas attiecas arī uz kompanjonu uz galda: noguldi to, un visi mezgli ap tevi dzirdēs
sliktāk.

## Savienotāji {#connectors}

Pasūti antenu ar tādu savienotāju, kāds ir tavai platei. Katrs pārejas adapteris ir vēl viens
savienojums, kas jāhermetizē, un papildu signāla zudumi.

- **SMA.** Vītņots savienotājs, apmēram 6 mm plats. Vairumam plašu ligzdai centrā ir caurums,
  bet antenai ir tapa. Šāda savienotāja zudumi 868 MHz frekvencē ir apmēram 0.03 dB.
- **RP-SMA.** Tāds pats korpuss un vītne kā SMA, bet tapa un caurums ir samainīti vietām. Tas
  izskatās pēc SMA, bet ar to nesavienojas. Pirms pasūti, pārbaudi, kurš no tiem ir tavai
  platei.
- **U.FL (IPEX).** Sīka uzspiežama ligzda pašā platē. No tās īss pigtail kabelis iet līdz SMA
  ligzdai korpusā. Tās nominālais resurss ir 30 savienošanas cikli, tāpēc pievieno to vienreiz
  un vairs neaiztiec.
- **N.** Lielais vītņotais savienotājs uz stiklšķiedras antenām un bieziem kabeļiem. Tā zudumi
  nepārsniedz 0.05 dB. Retranslatoram vajag vienu adapteri vai pigtail kabeli no N uz plates
  SMA.

## Kabeļa zudumi {#cable}

Kabelī signāls zūd, vēl pirms tas atstāj antenu, un tas notiek abos virzienos. 3 dB ir puse
tavas jaudas. Ražotāju dati uz metru 868 līdz 900 MHz joslā:

| Kabelis | Zudumi uz metru | Zudumi 5 m garumā |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metros RG174, plānā pigtail kabeļa, ko pievieno daudzām platēm, tu zaudē pusi jaudas.
Uzstādi plati pie antenas ar īsu pigtail kabeli vai izvelc līdz antenai biezu kabeli. Summai
pieskaiti katru adapteri un filtru signāla ceļā.

## Filtri {#filters}

Filtrs atrodas starp radio un antenu. Tas laiž cauri tavu joslu un bloķē pārējo, tāpēc spēcīgs
raidītājs tuvumā nepārslogo uztvērēju. Filtrs tev vajadzīgs, ja mezgls citu raidītāju tuvumā
dzird sliktāk, nekā vajadzētu. Retranslators mastā kopā ar mobilo sakaru bāzes stacijām ir
šāds mezgls. Filtrā signāls zūd abos virzienos: rēķini tā zudumus tāpat kā kabelim.

| | SAW filtrs | Dobumrezonatora filtrs |
|---|---|---|
| Izmērs | Daži milimetri, uz nelielas plates | Metāla bloks vai caurule |
| Laba filtra zudumi | mazāk par 2 dB | mazāk par 1 dB |
| Laba filtra maksimālā ieejas jauda | 500 mW | vairāki vati |

Piemēram, sysmocom cf866.5-kt30 ir dobumrezonatora filtrs joslai no 863 līdz 870 MHz. Tā
zudumi nepārsniedz 1.0 dB, un tas iztur 30 W. Tas ir paredzēts lietošanai telpās, tāpēc mastā
ievieto to hermētiskā kastē.

Filtri ļoti atšķiras, tāpēc pirms pirkšanas pārbaudi datu lapu. Filtra nominālajai ieejas
jaudai jābūt lielākai par tavu raidīšanas jaudu, un tā caurlaides joslā jāietilpst tava
priekšiestatījuma frekvencei.

## Uzstādīšana {#mounting}

- **Virs jumta malas.** Antenai vajag brīvu redzamību visos virzienos, kurus tā apkalpo. Palīdz
  pat daži metri virs apkārtējiem jumtiem. Retranslatoru ceļveža sadaļa
  [Izvēlies vietu](/repeater-guide/#site) rāda, kā pārbaudīt redzamību.
- **Tālāk no metāla.** Notekas, masti, citas antenas un metāla jumti antenas tuvumā maina tās
  starojuma diagrammu un noskaņojumu. Uzstādi to masta galā, nevis tam blakus.
- **Vertikāli.** Izmanto līmeņrādi, skat. [Kāpēc vertikāli](#vertical).
- **Pilienu cilpa.** Ļauj kabelim nokarāties zem savienotāja, pirms tas iet uz augšu vai iekšā.
  Tad ūdens nopil, nevis ietek savienojumā.
- **Hermetizē katru āra savienotāju.** Ūdens savienotājā palielina zudumus un izraisa tapas
  koroziju. Hermetizē to pret lietu un katru gadu pārbaudi blīvējumu.
- **Zibens.** Antena uz jumta ir mērķis. Gāzizlādes novadītājs kabelī pārsprieguma brīdī
  nostrādā un novada to uz zemi. Zemēšanā ievēro retranslatoru ceļveža sadaļu
  [Aparatūra](/repeater-guide/#hardware) un vietējos noteikumus.

## Likumīgās robežās {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
Eiropā MeshCore izmanto apakšjoslu 869.40-869.65 MHz, un efektīvā izstarotā jauda (e.r.p.)
ir ne vairāk kā **500 mW**. Robeža attiecas uz to, kas atstāj antenu: antenas pastiprinājumu
pieskaita, kabeļa un filtra zudumus atņem. Pastiprinājums dBi skaitās par 2.15 dB mazāks, jo
robežu mēra attiecībā pret dipolu.
{{< /callout >}}

5.8 dBi kolineārā antena uz plates ar 22 dBm paliek robežās. Tā pati antena uz plates ar
pastiprinātāju robežu pārsniedz, kamēr tu nesamazini raidīšanas jaudu. Retranslatoru ceļveža
sadaļā [Jauda: e.r.p. un tava antena](/repeater-guide/#erp) ir aprēķins un 2 izrēķināti piemēri.

## Pārbaudi antenu ar NanoVNA {#nanovna}

NanoVNA ir kabatas izmēra vektoru tīkla analizators. Tas parāda, kurai frekvencei antena ir
noskaņota, tāpēc tu to zini pirms uzstādīšanas. NanoVNA-H mēra līdz 1.5 GHz, un šajā diapazonā
ietilpst 868 MHz.

1. Kalibrē to diapazonam no 800 līdz 950 MHz ar atvērtās ķēdes, īsslēguma un slodzes uzgaļiem
   no tā komplekta.
2. Pievieno antenu ar adapteri, kuru tā izmantos mezglā. Turi to vertikāli, tālāk no sava
   ķermeņa un galda.
3. Nolasi SWR (stāvviļņu koeficienta) līkni: tā parāda, cik daudz signāla antena atdod atpakaļ.
   Iedobumam jāatrodas tava priekšiestatījuma frekvencē, EU/UK (Narrow) gadījumā 869.618 MHz.
   Iedobums simtiem MHz attālumā nozīmē, ka antena ir paredzēta citai joslai.

Ceturtdaļvilnis pie 868 MHz ir 86 mm (viļņa garums ir 345 mm). Garums vien joslu nepasaka, jo
ražotāji stieņa antenas loka un pievieno tām slodzi. To pasaka NanoVNA.

## Avoti {#sources}

- Kabeļa zudumi: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  Huber+Suhner RG316 datu lapa,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  Times Microwave LMR-240 un LMR-400 datu lapas,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antenas: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  Sirio SO 868-915-2 datu lapa,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Pastiprinājums kā signāls, kas saspiests mazākā telpā: [RF Cafe, ievads antenās](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Savienotāji: Rosenberger 32S102 (SMA) un 53S101 (N) datu lapas, Hirose U.FL katalogs.
- Filtri: sysmocom cf866.5-kt30 produkta lapa,
  [Citel gāzizlādes novadītāji](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarizācijas zudumi: [University of Toronto, Friis efekti](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipola pastiprinājums atkarībā no garuma: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Viļņa garums: gaismas ātrums no [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Likumīgā robeža: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  1. pielikums, josla h1.7; pārējie avoti ir uzskaitīti [retranslatoru ceļvedī](/repeater-guide/#legal).
