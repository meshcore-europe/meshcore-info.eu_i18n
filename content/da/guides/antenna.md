---
title: Antenneguide
lead: Antennen er halvdelen af din node. Den rigtige antenne, monteret godt, rækker længere end mere sendeeffekt. Tjek antennen på din companion, og vælg, tilslut og montér derefter en til en repeater.
description: 'Vælg og montér en MeshCore-antenne til 868 MHz: tjek en companion-pisk, antennetyper og gain, stik, kabeltab per meter, filtre, montering og hvordan gain tæller med i den lovlige grænse.'
eyebrow: Companion og repeater · 868 MHz
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '45010ad0'
  seeded: '2026-10-26'
  fields: {title: '3a76cb0e', lead: '98430ade', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', '94c5bae4', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
---

Højde, en afstemt antenne og et kort kabel giver mere rækkevidde end hver
eneste ekstra milliwatt. Denne guide begynder med companion, den radio du
sender beskeder fra. Derefter handler den om antennen på en repeater, en
node der sender beskeder videre fra et tag eller en mast.

## Din companion {#companion}

{{< callout type="warning" >}}
Sæt antennen på, før du tænder radioen. En LoRa-radio, der
sender uden antenne, kan beskadige sin egen chip.
{{< /callout >}}

Antennen, der fulgte med dit board, gør arbejdet. Sæt den på, hold
noden lodret, og begynd at sende beskeder. En bedre
antenne på en companion vinder lidt; en repeater inden for rækkevidde vinder meget.

Køb kun en separat pisk-antenne, når den medfølgende er i stykker eller mangler. Ikke
alle pisk-antenner, der sælges til 868 MHz, er afstemt til det. [Tjek den med en
NanoVNA](#nanovna), en antenneanalysator i lommeformat, før du stoler på den, eller lån en fra et board, der
virker.

En node ved siden af en stærk sender hører mindre, end den burde. Et lille
[SAW-filter (surface acoustic wave)](#filters) mellem radioen og
antennen holder den sender ude af modtageren. Tjek dets datablad
først:

- **Maksimal indgangseffekt.** Filteret sidder også i stien for din egen
  sending. Et board, der sender 22 dBm (160 mW) ind i et filter godkendt til 15 dBm,
  ødelægger filteret.
- **Pasbånd.** Det skal omfatte din presets frekvens. Et filter til
  868.65 til 869.25 MHz lader ikke EU/UK (Narrow)-kanalen på
  869.618 MHz passere.

## Antennetyper til en repeater {#types}

Alle antenner i meshet står lodret. Vælg typen efter, hvor de noder er,
som du vil nå:

- **Glasfiber-kollineær.** Et hvidt rør på en mast med gain hele vejen
  rundt langs horisonten. Standardvalget til en repeater, der dækker en by.
- **Dipol.** Kortere, med mindre gain og en høj stråle. Den når noder under
  og over dig bedre end en kollineær. Det betyder noget på en bakke over
  en dal.
- **Yagi.** En bom med tværelementer, rettet mod ét sted. Den når en enkelt
  fjern repeater og ikke meget andet. Montér den med elementerne lodret,
  fordi dens polarisering følger elementerne.

## Gain og strålen {#gain}

Gain tilføjer ikke effekt. Det tager det signal, der ville gå op og ned,
og sender det langs horisonten. Som en lommelygte, du fokuserer: samme batteri,
en længere og smallere stråle. En dipol og en kollineær fra samme producent
viser det:

| Antenne | Gain | Lodret strålebredde |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 grader |
| Glasfiber-kollineær (Sirio SPO 868-915-6) | 5.8 dBi | 23 grader |

{{< gain >}}

Diagrammet skærer gennem masten, set fra siden. Drej det rundt om
masten, og du har hele strålen: en ring for dipolen, en flad skive
for den kollineære. En lodret antenne sender ens i alle retninger omkring
sig. Uden for den tegnede stråle stopper signalet ikke; det er svagere, stadig
nok til en node tæt på.

På et tag er en flad stråle det, du vil have. På en bakke højt over noderne
går en stråle på 23 grader hen over hovedet på dem; en dipol dækker dem. En Yagi
går længere: 16.6 dBi i en stråle, der er 23 grader høj
og 25 grader bred (Amphenol Procom
7176870), og intet til siderne.

Gain tæller i forhold til en reference. dBi sammenligner med en ideel antenne, der
sender lige meget i alle retninger. dBd sammenligner med en halvbølge-dipol,
som selv har 2.15 dBi: selv den enkleste antenne sender intet lige
op eller ned. En længere dipol, 1.25 bølgelængder, når 5.2 dBi. En kollineær
stabler i stedet halvbølge-elementer oven på hinanden: jo flere den stabler, jo
højere gain. Pres det samme signal ind på halvt så meget plads, og det er
dobbelt så stærkt der: 3 dB. Ind på en fjerdedel, 4 gange så stærkt: 6 dB.
Producenter angiver gain i dBi; den lovlige grænse regner i dBd, se
[Inden for den lovlige grænse](#legal).

### Hvilken gain til dit sted {#choose-gain}

- **Bakker, dale eller en tæt by: omkring 3 dBi.** Den høje stråle når
  noder over og under dig, og rundt om de skråninger og bygninger, der er i vejen.
  Det virker også den anden vej: fra en dal passerer en flad stråle under en
  repeater på bakken ovenfor. RAKwireless RAKARG12 er en af dem: et
  glasfiberrør på 36 cm.
- **Forstæder eller en by med lave tage: 5 til 6 dBi.** Standard
  glasfiber-kollineær.
- **Fladt, åbent land: 8 til 10 dBi.** Den fladeste stråle når længst
  langs horisonten. Monteret højt går den hen over noderne tæt på.

Gainet i navnet er det bedste tal over hele antennens bånd.
RAKARG12, solgt som 3 dBi, har 2.8 dBi ved 865 til 870 MHz. Læs gain-tabellen
i databladet ved din presets frekvens.

Over 7 dBi går et board på 22 dBm over den lovlige grænse, medmindre tab i kabel og filter
udligner forskellen. Sænk sendeeffekten, så det passer.

Høj gain hjælper kun, når du ved, hvor noderne er: langs horisonten
rundt om en repeater, eller ved én fjern repeater for en Yagi. En companion i din
hånd peger i alle retninger, så den lave gain, den kom med, passer bedst til den.

## Hvorfor lodret {#vertical}

Antenner hører hinanden bedst, når de peger samme vej. Tabet vokser med
vinklen mellem dem: 45 grader koster 3 dB, halvdelen af dit signal. Ved
90 grader, en liggende antenne mod en lodret, når der i teorien intet frem.
Meshet står lodret, så det gør din antenne også. Det gælder også en
companion på et skrivebord: læg den ned, og alle noder omkring dig hører
mindre.

## Konnektorer {#connectors}

Bestil antennen med den konnektor,
dit board har. Hver adapter er en samling mere, der skal tætnes, og mere signal,
der går tabt.

- **SMA.** En konnektor med gevind, omkring 6 mm bred. Stikket på de fleste boards
  har et hul i midten; antennen har pinden. En konnektor af denne
  slags taber omkring 0.03 dB ved 868 MHz.
- **RP-SMA.** Samme hus og gevind som SMA, med pinden og hullet
  byttet om. Den ligner SMA og passer ikke sammen med den. Tjek, hvilken en
  dit board har, før du bestiller.
- **U.FL (IPEX).** Et lille tryk-på-stik på selve boardet. Et kort
  pigtail-kabel går fra det til et SMA-stik i kabinettet. Det er godkendt til
  30 til- og frakoblinger, så tilslut det én gang, og lad det sidde.
- **N.** Den store konnektor med gevind på glasfiberantenner og tykt
  kabel. Den taber højst 0.05 dB. En repeater skal have én
  adapter eller pigtail fra N til boardets SMA.

## Kabeltab {#cable}

Kablet koster signal, før det forlader antennen, i begge retninger. 3 dB
er halvdelen af din effekt. Producenternes tal per meter, ved 868 til 900 MHz:

| Kabel | Tab per meter | Tab over 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 meter RG174, det tynde pigtail-kabel der følger med mange boards, taber halvdelen
af din effekt. Montér boardet ved antennen med et kort pigtail-kabel, eller
træk tykt kabel hen til det. Læg hver adapter og hvert filter i stien til summen.

## Filtre {#filters}

Et filter sidder mellem radioen og antennen. Det lader dit bånd passere og
blokerer resten, så en stærk sender i nærheden ikke overdøver
modtageren. Du har brug for et, når en node hører mindre, end den burde, nær andre
sendere. En repeater på en mast med basestationer til mobiltelefoner er sådan
en node. Et filter koster signal i begge retninger: regn dets tab med ligesom
kabel.

| | SAW-filter | Kavitetsfilter |
|---|---|---|
| Størrelse | Få millimeter, på et lille board | En metalblok eller et metalrør |
| Tab ved et godt filter | under 2 dB | under 1 dB |
| Maksimal indgangseffekt ved et godt filter | 500 mW | flere watt |

sysmocom cf866.5-kt30 er for eksempel et kavitetsfilter til 863 til
870 MHz, der højst taber 1.0 dB og tåler 30 W. Det er lavet til indendørs brug,
så sæt det i en tæt boks på en mast.

Filtre er meget forskellige, så tjek databladet, før du køber. Dets godkendte
indgangseffekt skal være højere end din sendeeffekt, og dets pasbånd skal omfatte
din presets frekvens.

## Montering {#mounting}

- **Over tagkanten.** Antennen skal have frit udsyn i alle de retninger,
  den dækker. Selv nogle få meter over de omkringliggende tage hjælper.
  [Vælg et sted](/repeater-guide/#site) i repeater-guiden viser, hvordan du
  tjekker udsynet.
- **Væk fra metal.** Tagrender, master, andre antenner og metaltage ved
  siden af antennen ændrer dens strålingsmønster og afstemning. Montér den
  øverst på masten, ikke ved siden af.
- **Lodret.** Brug et vaterpas; se [Hvorfor lodret](#vertical).
- **Drypsløjfe.** Lad kablet hænge under stikket, før det går op eller ind.
  Så drypper vandet af i stedet for at løbe ind i samlingen.
- **Tætn alle udendørs stik.** Vand i et stik øger tabet og tærer stiften.
  Tætn det mod regn, og tjek tætningen hvert år.
- **Lyn.** En antenne på et tag er et mål. En gasafleder i kablet udløses
  ved en overspænding og leder den til jord. Følg
  [Hardware](/repeater-guide/#hardware) i repeater-guiden og dine lokale
  regler for jording.

## Inden for den lovlige grænse {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
I Europa bruger MeshCore delbåndet 869.40-869.65 MHz med højst
**500 mW** effektiv udstrålet effekt (e.r.p.). Grænsen tæller det, der forlader antennen:
antennegain lægges til, tab i kabel og filter trækkes fra. Gain i dBi tæller
2.15 dB mindre, fordi grænsen måles i forhold til en dipol.
{{< /callout >}}

En kollineær på 5.8 dBi på et board på 22 dBm holder sig inden for grænsen. Den samme
antenne på et board med forstærker gør det ikke, før du sænker
sendeeffekten. [Effekt: e.r.p. og din antenne](/repeater-guide/#erp) i
repeater-guiden har regnestykket og 2 gennemregnede eksempler.

## Tjek en antenne med en NanoVNA {#nanovna}

En NanoVNA er en vektornetværksanalysator i lommeformat. Den viser, ved hvilken
frekvens en antenne er afstemt, så du ved det, før du monterer den.
NanoVNA-H måler op til 1.5 GHz, hvilket dækker 868 MHz.

1. Kalibrér den til 800 til 950 MHz med open-, short- og load-stykkerne
   fra dens sæt.
2. Tilslut antennen gennem den adapter, den skal bruge på noden. Hold den
   lodret og væk fra din krop og bordet.
3. Læs SWR-kurven (standing wave ratio): den viser, hvor meget signal
   antennen sender tilbage. Dykket skal ligge på din presets frekvens, 869.618
   MHz for EU/UK (Narrow). Et dyk hundredvis af MHz væk betyder, at antennen er
   lavet til et andet bånd.

En kvart bølgelængde ved 868 MHz er 86 mm (bølgelængden er 345 mm). Længden
alene fortæller dig ikke båndet, fordi producenter folder og belaster pisk-antenner;
det gør NanoVNA'en.

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
- Gain som signal presset ind på mindre rum: [RF Cafe, antenna introduction](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Stik: databladene for Rosenberger 32S102 (SMA) og 53S101 (N), Hirose
  U.FL-kataloget.
- Filtre: produktsiden for sysmocom cf866.5-kt30,
  [Citel gasafledere](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polariseringstab: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipolgain efter længde: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Bølgelængde: lysets hastighed fra [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Lovlig grænse: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Annex 1, bånd h1.7; [repeater-guiden](/repeater-guide/#legal) har
  resten.
