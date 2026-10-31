---
title: Antenneguide
lead: Den rigtige antenne, godt monteret, når længere end mere effekt. Tjek antennen på din companion, og vælg, tilslut og montér så en til en repeater.
description: 'Vælg og montér en MeshCore-antenne til 868 MHz: tjek en companion-pisk, antennetyper og forstærkning, stik, kabeltab pr. meter, filtre, montering og hvordan forstærkning tæller med i den lovlige grænse.'
eyebrow: Companion og repeater · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-10-31'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Højde, en afstemt antenne og et kort kabel giver mere rækkevidde end
ekstra milliwatt. Guiden starter med din companion, den radio, du sender
beskeder fra. Derefter handler den om antennen på en repeater. Det er en
node, der sender beskeder videre fra et tag eller en mast.

## Din companion {#companion}

{{< callout type="warning" >}}
Sæt antennen på, før du tænder radioen. En LoRa-radio, der sender uden
antenne, kan skade sin egen chip.
{{< /callout >}}

Antennen, der fulgte med dit board, klarer opgaven. Sæt den på, hold
noden lodret, og begynd at skrive beskeder. En bedre antenne på en
companion giver ikke meget. En repeater inden for rækkevidde giver meget.

Køb kun en separat whip-antenne, hvis den medfølgende er i stykker eller
mangler. Ikke alle whip-antenner, der sælges til 868 MHz, er afstemt til
den frekvens. [Tjek den med en NanoVNA](#nanovna), en antenneanalysator i
lommeformat, før du stoler på den. Du kan også låne en fra et board, der
virker.

En node tæt på en stærk sender hører mindre, end den burde. Et lille
[SAW-filter (surface acoustic wave)](#filters) mellem radioen og antennen
holder den sender ude af modtageren. Tjek først filterets datablad:

- **Maksimal indgangseffekt.** Filteret sidder også i stien for din egen
  udsendelse. Et board, der sender 22 dBm (160 mW) ind i et filter til
  15 dBm, ødelægger filteret.
- **Pasbånd.** Det skal omfatte frekvensen for dit preset. Et filter til
  868.65 til 869.25 MHz lader ikke EU/UK (Narrow)-kanalen på
  869.618 MHz passere.

## Antennetyper til en repeater {#types}

Alle antenner i meshet står lodret. Vælg typen efter, hvor de noder er,
som du vil nå:

- **Glasfiber-collinear.** Et hvidt rør på en mast med forstærkning hele
  vejen rundt i horisonten. Standardvalget til en repeater, der dækker en
  by.
- **Dipol.** Kortere, med mindre forstærkning og en høj stråle. Den når
  noder under og over dig bedre end en collinear, fx fra en bakke over en
  dal.
- **Yagi.** En bom med tværelementer, rettet mod ét sted. Den når en
  enkelt fjern repeater og ikke meget andet. Montér den med elementerne
  lodret, for dens polarisering følger elementerne.

## Forstærkning og strålen {#gain}

Forstærkning tilføjer ikke effekt. Antennen tager det signal, der ville
gå op og ned, og sender det ud langs horisonten. Det er som en
lommelygte, du fokuserer: det samme batteri, en længere og smallere
stråle. En dipol og en collinear fra samme producent viser det:

| Antenne | Forstærkning | Lodret strålebredde |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 grader |
| Glasfiber-collinear (Sirio SPO 868-915-6) | 5.8 dBi | 23 grader |

{{< gain >}}

Diagrammet skærer gennem masten, set fra siden. Drej det rundt om masten,
så har du hele strålen: en donut for dipolen, en flad skive for
collinearen. En lodret antenne sender ens i alle retninger rundt om sig.
Uden for den tegnede stråle stopper signalet ikke. Det er svagere, men
stadig nok til en node tæt på.

På et tag vil du have en flad stråle. På en bakke højt over noderne går
en stråle på 23 grader hen over hovedet på dem. En dipol dækker dem. En
Yagi tager det et skridt videre: 16.6 dBi i en stråle, der er 23 grader
høj og 25 grader bred (Amphenol Procom 7176870), og intet til siderne.

Forstærkning måles mod en reference. dBi sammenligner med en ideel
antenne, der sender lige meget i alle retninger. dBd sammenligner med en
halvbølgedipol, som selv har 2.15 dBi: selv den enkleste antenne sender
intet lige op eller ned. En længere dipol på 1.25 bølgelængder når
5.2 dBi. En collinear stabler i stedet halvbølgeelementer oven på
hinanden: jo flere den stabler, jo højere forstærkning. Pres det samme
signal ind i halvdelen af rummet, så er det dobbelt så stærkt der: 3 dB.
Ind i en fjerdedel, 4 gange så stærkt: 6 dB. Producenter angiver
forstærkning i dBi. Den lovlige grænse regner i dBd, se
[Inden for den lovlige grænse](#legal).

### Hvilken forstærkning til dit sted {#choose-gain}

- **Bakker, dale eller en tæt by: omkring 3 dBi.** Den høje stråle når
  noder over og under dig, og rundt om de skrænter og bygninger, der er i
  vejen. Det virker også den anden vej: fra en dal går en flad stråle ind
  under en repeater på bakken ovenover. RAKwireless RAKARG12 er sådan en:
  et glasfiberrør på 36 cm.
- **Forstæder eller en by med lave tage: 5 til 6 dBi.** Den almindelige
  glasfiber-collinear.
- **Fladt, åbent land: 8 til 10 dBi.** Den fladeste stråle når længst ud
  langs horisonten. Monteret højt går den hen over noderne tæt på.

Forstærkningen i navnet er det bedste tal over hele antennens bånd.
RAKARG12, der sælges som 3 dBi, har 2.8 dBi ved 865 til 870 MHz. Læs
forstærkningstabellen i databladet ved frekvensen for dit preset.

Over 7 dBi går et board på 22 dBm over den lovlige grænse, medmindre tab
i kabel og filter udligner forskellen. Sænk sendeeffekten, så den passer.

Høj forstærkning hjælper kun, når du ved, hvor noderne er: langs
horisonten rundt om en repeater, eller ved én fjern repeater for en Yagi.
En companion i din hånd peger i alle retninger. Derfor passer den lave
forstærkning, den kom med, bedst til den.

## Hvorfor lodret {#vertical}

Antenner hører hinanden bedst, når de peger samme vej. Tabet vokser med
vinklen mellem dem: 45 grader koster 3 dB, halvdelen af dit signal. Ved
90 grader, en vandret antenne mod en lodret, når der i teorien intet
frem. Meshet står lodret, så det skal din antenne også. Det gælder også
for en companion på et skrivebord: lægger du den ned, hører alle noder
omkring dig mindre.

## Stik {#connectors}

Bestil antennen med det stik, dit board har. Hver adapter er endnu en
samling, du skal tætne, og mere tabt signal.

- **SMA.** Et stik med gevind, omkring 6 mm bredt. Bøsningen på de fleste
  boards har et hul i midten, og antennen har stiften. Et stik af den
  slags taber omkring 0.03 dB ved 868 MHz.
- **RP-SMA.** Samme krop og gevind som SMA, men stiften og hullet har
  byttet plads. Det ligner SMA og passer ikke sammen med det. Tjek, hvilket
  dit board har, før du bestiller.
- **U.FL (IPEX).** En lille bøsning på selve boardet, som du trykker stikket
  på. Et kort pigtail-kabel går fra den til en SMA-bøsning i kabinettet. Den
  er beregnet til 30 tilslutninger. Tilslut den derfor én gang, og lad den
  sidde.
- **N.** Det store stik med gevind på glasfiberantenner og tykt kabel. Det
  taber højst 0.05 dB. En repeater har brug for én adapter eller pigtail
  fra N til boardets SMA.

## Kabeltab {#cable}

Kablet koster signal, før signalet forlader antennen, i begge retninger. 3 dB
er halvdelen af din effekt. Producenternes tal per meter, ved 868 til
900 MHz:

| Kabel | Tab per meter | Tab over 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 meter RG174, det tynde pigtail-kabel, der følger med mange boards,
taber halvdelen af din effekt. Montér boardet ved antennen med et kort
pigtail-kabel, eller træk tykt kabel til den. Læg hver adapter og hvert
filter i stien til summen.

## Filtre {#filters}

Et filter sidder mellem radioen og antennen. Det lader dit bånd passere og
blokerer resten. Så overdøver en stærk sender tæt på ikke modtageren. Du
har brug for et, når en node hører mindre, end den burde, nær andre
sendere. En repeater på en mast med basestationer til mobiltelefoner er
sådan en node. Et filter koster signal i begge retninger: regn dets tab
med som kabel.

| | SAW-filter | Kavitetsfilter |
|---|---|---|
| Størrelse | Få millimeter, på et lille board | En metalblok eller et rør |
| Tab i et godt filter | under 2 dB | under 1 dB |
| Maksimal indgangseffekt i et godt filter | 500 mW | flere watt |

sysmocom cf866.5-kt30 er fx et kavitetsfilter til 863 til 870 MHz. Det
taber højst 1.0 dB og tåler 30 W. Det er lavet til indendørs brug. Sæt
det derfor i en tæt kasse på en mast.

Filtre er meget forskellige. Tjek derfor databladet, før du køber.
Filterets angivne indgangseffekt skal være højere end din sendeeffekt. Dets
pasbånd skal omfatte frekvensen for dit preset.

## Montering {#mounting}

- **Over tagkanten.** Antennen skal have frit udsyn i alle de retninger,
  den dækker. Selv få meter over de omkringliggende tage hjælper.
  [Vælg et sted](/repeater-guide/#site) i repeater-guiden viser, hvordan du
  tjekker udsynet.
- **Væk fra metal.** Tagrender, master, andre antenner og metaltage tæt på
  antennen ændrer dens strålingsmønster og afstemning. Montér den oven på
  masten, ikke ved siden af.
- **Lodret.** Brug et vaterpas, se [Hvorfor lodret](#vertical).
- **Dryppesløjfe.** Lad kablet hænge ned under stikket, før det går op
  eller ind. Så drypper vandet af i stedet for at løbe ind i samlingen.
- **Tætn alle udendørs stik.** Vand i et stik øger tabet og tærer på
  stiften. Tætn stikket mod regn, og tjek tætningen hvert år.
- **Lyn.** En antenne på et tag er et mål. En gasudladningsafleder i
  kablet slår til ved en overspænding og leder den til jord. Følg
  [Hardware](/repeater-guide/#hardware) i repeater-guiden og dine lokale
  regler for jording.

## Inden for den lovlige grænse {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
I Europa bruger MeshCore underbåndet 869.40-869.65 MHz med højst
**500 mW** effektiv udstrålet effekt (e.r.p.). Grænsen regner med det, der
forlader antennen: antennens forstærkning lægges til, tab i kabel og
filter trækkes fra. Forstærkning i dBi tæller 2.15 dB mindre, fordi
grænsen måles mod en dipol.
{{< /callout >}}

En collinear på 5.8 dBi på et board på 22 dBm holder sig inden for
grænsen. Den samme antenne på et board med forstærker gør ikke, før du
sænker sendeeffekten. [Effekt: e.r.p. og din antenne](/repeater-guide/#erp)
i repeater-guiden har udregningen og 2 gennemregnede eksempler.

## Tjek en antenne med en NanoVNA {#nanovna}

En NanoVNA er en vektornetværksanalysator i lommeformat. Den viser, hvilken
frekvens en antenne er afstemt til. Så ved du det, før du monterer den.
NanoVNA-H måler op til 1.5 GHz, og det dækker 868 MHz.

1. Kalibrér den til 800 til 950 MHz med open-, short- og load-delene fra
   dens sæt.
2. Tilslut antennen gennem den adapter, den skal bruge på noden. Hold den
   lodret og væk fra din krop og bordet.
3. Aflæs SWR-kurven (standing wave ratio): den viser, hvor meget signal
   antennen sender tilbage. Dykket skal ligge på frekvensen for dit preset,
   869.618 MHz for EU/UK (Narrow). Et dyk flere hundrede MHz væk betyder,
   at antennen er lavet til et andet bånd.

En kvart bølgelængde ved 868 MHz er 86 mm (bølgelængden er 345 mm). Længden
alene fortæller dig ikke båndet, for producenter folder og belaster
whip-antenner. Det gør NanoVNA'en.

## Kilder {#sources}

- Kabeltab: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  databladet for Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  databladene for Times Microwave LMR-240 og LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antenner: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  databladet for Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Forstærkning som signal presset ind på mindre plads: [RF Cafe, antenna introduction](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Stik: databladene for Rosenberger 32S102 (SMA) og 53S101 (N),
  kataloget for Hirose U.FL.
- Filtre: produktsiden for sysmocom cf866.5-kt30,
  [Citel gasudladningsafledere](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarisationstab: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipolforstærkning efter længde: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Bølgelængde: lysets hastighed fra [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Lovlig grænse: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  bilag 1, bånd h1.7. [Repeater-guiden](/repeater-guide/#legal) oplister
  resten.
