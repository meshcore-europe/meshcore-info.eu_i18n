---
title: Antenneguide
lead: Riktig antenne, godt montert, når lenger enn mer effekt. Sjekk antennen på companion-enheten din, og velg, koble til og monter deretter en antenne til en repeater.
description: 'Velg og monter en MeshCore-antenne for 868 MHz: sjekk en companion-pisk, antennetyper og forsterkning, kontakter, kabeltap per meter, filtre, montering og hvordan forsterkningen teller mot den lovlige grensen.'
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

Høyde, en avstemt antenne og en kort kabel gir mer rekkevidde enn noen
ekstra milliwatt. Guiden begynner med companion-enheten, radioen du sender
meldinger fra. Deretter tar den for seg antennen på en repeater, en node
som sender meldinger videre fra et tak eller en mast.

## Companion-enheten din {#companion}

{{< callout type="warning" >}}
Skru fast antennen før du slår på radioen. En LoRa-radio som sender uten
antenne, kan skade sin egen brikke.
{{< /callout >}}

Antennen som fulgte med kortet ditt, gjør jobben. Skru den fast, hold noden
loddrett og begynn å sende meldinger. En bedre antenne på en companion-enhet
gir lite. En repeater innen rekkevidde gir mye.

Kjøp en egen piskantenne bare når den medfølgende er ødelagt eller mangler.
Ikke alle piskantenner som selges for 868 MHz, er avstemt for den
frekvensen. [Sjekk den med en NanoVNA](#nanovna), en antenneanalysator i
lommeformat, før du stoler på den. Du kan også låne en fra et kort som
fungerer.

En node ved siden av en sterk sender hører mindre enn den burde. Et lite
[SAW-filter (surface acoustic wave)](#filters) mellom radioen og antennen
holder den senderen ute av mottakeren. Sjekk databladet til filteret
først:

- **Maksimal inngangseffekt.** Filteret sitter også i signalveien for din
  egen sending. Et kort som sender 22 dBm (160 mW) inn i et filter beregnet for
  15 dBm, ødelegger filteret.
- **Passbånd.** Det må omfatte frekvensen til forhåndsinnstillingen din. Et
  filter for 868.65 til 869.25 MHz slipper ikke gjennom EU/UK (Narrow)-kanalen
  på 869.618 MHz.

## Antennetyper for en repeater {#types}

Alle antennene i meshet står loddrett. Velg type ut fra hvor nodene du vil
nå, befinner seg:

- **Kollineær antenne i glassfiber.** Et hvitt rør på en mast, med
  forsterkning hele veien rundt horisonten. Standardvalget for en repeater
  som dekker en by.
- **Dipol.** Kortere, med mindre forsterkning og en høy stråle. Den når
  noder under og over deg bedre enn en kollineær antenne, for eksempel fra
  en ås over en dal.
- **Yagi.** En bom med tverrelementer, rettet mot ett sted. Den når én
  fjern repeater og lite annet. Monter den med elementene loddrett, fordi
  polarisasjonen følger elementene.

## Forsterkning og strålen {#gain}

Forsterkning gir ikke mer effekt. Antennen tar signalet som ville gått opp
og ned, og sender det langs horisonten. Det er som en lommelykt du
fokuserer: samme batteri, men en lengre og smalere stråle. En dipol og en
kollineær antenne fra samme produsent viser dette:

| Antenne | Forsterkning | Vertikal strålebredde |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 grader |
| Kollineær antenne i glassfiber (Sirio SPO 868-915-6) | 5.8 dBi | 23 grader |

{{< gain >}}

Diagrammet er et snitt gjennom masten, sett fra siden. Drei det rundt
masten, så får du hele strålen: en smultring for dipolen og en flat skive
for den kollineære antennen. En loddrett antenne sender likt i alle
retninger rundt seg. Utenfor den tegnede strålen stopper ikke signalet. Det
er svakere, men fortsatt nok for en node i nærheten.

På et tak vil du ha en flat stråle. På en ås høyt over nodene går en stråle
på 23 grader over hodene deres. En dipol dekker dem. En Yagi tar dette
lenger: 16.6 dBi i en stråle som er 23 grader høy og 25 grader bred
(Amphenol Procom 7176870), og ingenting til sidene.

Forsterkning måles mot en referanse. dBi sammenligner med en ideell antenne
som sender likt i alle retninger. dBd sammenligner med en halvbølgedipol,
som selv har 2.15 dBi: selv den enkleste antennen sender ingenting rett opp
eller ned. En lengre dipol, på 1.25 bølgelengder, når 5.2 dBi. En kollineær
antenne stabler i stedet halvbølgeelementer oppå hverandre: jo flere den
stabler, desto høyere forsterkning. Klemmer du det samme signalet inn i
halve rommet, blir det dobbelt så sterkt der: 3 dB. Inn i en fjerdedel blir
det 4 ganger så sterkt: 6 dB. Produsentene oppgir forsterkning i dBi. Den
lovlige grensen regnes i dBd, se [Innenfor den lovlige grensen](#legal).

### Hvilken forsterkning passer for stedet ditt {#choose-gain}

- **Åser, daler eller tett by: rundt 3 dBi.** Den høye strålen når noder
  over og under deg, og rundt skråninger og bygninger som står i veien. Det
  gjelder også motsatt vei: fra en dal går en flat stråle under en repeater
  på åsen over. RAKwireless RAKARG12 er en slik antenne: et glassfiberrør på
  36 cm.
- **Forsteder eller en by med lave tak: 5 til 6 dBi.** Den vanlige
  kollineære antennen i glassfiber.
- **Flatt, åpent landskap: 8 til 10 dBi.** Den flateste strålen når lengst
  langs horisonten. Montert høyt går den over nodene i nærheten.

Forsterkningen i navnet er det beste tallet over hele antennens bånd.
RAKARG12, som selges som 3 dBi, har 2.8 dBi ved 865 til 870 MHz. Les
forsterkningstabellen i databladet ved frekvensen til forhåndsinnstillingen
din.

Over 7 dBi går et kort på 22 dBm over den lovlige grensen, med mindre tap i
kabel og filter utligner forskjellen. Senk sendeeffekten tilsvarende.

Høy forsterkning hjelper bare når du vet hvor nodene er: langs horisonten
rundt en repeater, eller ved én fjern repeater for en Yagi. En
companion-enhet i hånden peker i alle retninger. Derfor passer den lave
forsterkningen den kom med, best.

## Hvorfor loddrett {#vertical}

Antenner hører hverandre best når de peker samme vei. Tapet øker med
vinkelen mellom dem: 45 grader koster 3 dB, halve signalet ditt. Ved 90
grader, en liggende antenne mot en stående, kommer det i teorien ingenting
fram. Meshet står loddrett, så det gjør antennen din også. Dette gjelder
også en companion-enhet på et skrivebord: Legger du den flat, hører alle
nodene rundt deg mindre.

## Kontakter {#connectors}

Bestill antennen med samme kontakt som kortet ditt har. Hver adapter er ett
skjøtepunkt til som må tettes, og mer tapt signal.

- **SMA.** En gjenget kontakt på rundt 6 mm i bredden. Kontakten på de
  fleste kort har et hull i midten. Antennen har pinnen. En kontakt av denne
  typen taper rundt 0.03 dB ved 868 MHz.
- **RP-SMA.** Samme hus og gjenger som SMA, men med pinne og hull byttet om.
  Den ser ut som SMA, men passer ikke sammen med den. Sjekk hvilken kortet
  ditt har før du bestiller.
- **U.FL (IPEX).** En bitteliten trykkontakt direkte på kortet. En kort
  pigtail-kabel går fra den til en SMA-kontakt i kabinettet. Den tåler 30
  tilkoblinger, så koble den til én gang og la den være.
- **N.** Den store gjengede kontakten på glassfiberantenner og tykk kabel.
  Den taper høyst 0.05 dB. En repeater trenger én adapter eller pigtail fra
  N til kortets SMA.

## Kabeltap {#cable}

Kabelen koster signal før det forlater antennen, i begge retninger. 3 dB er
halve effekten din. Produsentenes tall per meter ved 868 til 900 MHz:

| Kabel | Tap per meter | Tap over 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 meter RG174, den tynne pigtail-kabelen som følger med mange kort, taper
halve effekten din. Monter kortet ved antennen med en kort pigtail, eller
trekk tykk kabel fram til den. Ta med hver adapter og hvert filter i
signalveien i regnestykket.

## Filtre {#filters}

Et filter sitter mellom radioen og antennen. Det slipper gjennom båndet ditt
og blokkerer resten. Da overdøver ikke en sterk sender i nærheten
mottakeren. Du trenger et filter når en node hører mindre enn den burde nær
andre sendere. En repeater på en mast med basestasjoner for mobiltelefoni er
en slik node. Et filter koster signal i begge retninger: Regn med tapet på
samme måte som for kabel.

| | SAW-filter | Hulromsfilter |
|---|---|---|
| Størrelse | Noen få millimeter, på et lite kort | En metallblokk eller et rør |
| Tap i et godt filter | under 2 dB | under 1 dB |
| Maksimal inngangseffekt i et godt filter | 500 mW | flere watt |

sysmocom cf866.5-kt30 er for eksempel et hulromsfilter for 863 til 870 MHz
som taper høyst 1.0 dB og tåler 30 W. Det er laget for innendørs bruk, så
sett det i en tett boks hvis det skal på en mast.

Filtre er svært ulike, så sjekk databladet før du kjøper. Den oppgitte
inngangseffekten må være høyere enn sendeeffekten din, og passbåndet må
omfatte frekvensen til forhåndsinnstillingen din.

## Montering {#mounting}

- **Over takkanten.** Antennen trenger fri sikt i alle retninger den skal
  dekke. Selv noen få meter over takene rundt hjelper. [Velg et
  sted](/repeater-guide/#site) i repeaterguiden viser hvordan du sjekker
  sikten.
- **Unna metall.** Takrenner, master, andre antenner og metalltak ved siden
  av antennen endrer strålingsmønsteret og avstemmingen. Monter den på
  toppen av masten, ikke ved siden av.
- **Loddrett.** Bruk et vater, se [Hvorfor loddrett](#vertical).
- **Dryppsløyfe.** La kabelen henge ned under kontakten før den går opp
  eller inn. Da drypper vannet av i stedet for å renne inn i skjøten.
- **Tett alle utendørs kontakter.** Vann i en kontakt øker tapet og får
  pinnen til å korrodere. Tett den mot regn og sjekk tetningen hvert år.
- **Lyn.** En antenne på et tak er et mål. En gassutladningsavleder i
  kabelen løser ut ved et spenningsstøt og leder det til jord. Følg
  [Maskinvare](/repeater-guide/#hardware) i repeaterguiden og de lokale
  reglene for jording.

## Innenfor den lovlige grensen {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
I Europa bruker MeshCore delbåndet 869.40-869.65 MHz, med høyst **500 mW**
effektiv utstrålt effekt (e.r.p.). Grensen gjelder det som forlater
antennen: Antenneforsterkning legges til, tap i kabel og filter trekkes fra.
Forsterkning i dBi teller 2.15 dB mindre, fordi grensen måles mot en dipol.
{{< /callout >}}

En kollineær antenne på 5.8 dBi på et kort med 22 dBm holder seg innenfor
grensen. Den samme antennen på et kort med forsterker gjør det ikke, før du
senker sendeeffekten. [Effekt: e.r.p. og antennen din](/repeater-guide/#erp)
i repeaterguiden viser regnestykket og 2 gjennomregnede eksempler.

## Sjekk en antenne med en NanoVNA {#nanovna}

En NanoVNA er en vektornettverksanalysator i lommeformat. Den viser hvilken
frekvens en antenne er avstemt for, så du vet det før du monterer den.
NanoVNA-H måler opptil 1.5 GHz, noe som dekker 868 MHz.

1. Kalibrer den for 800 til 950 MHz med open-, short- og load-delene fra
   settet.
2. Koble til antennen gjennom adapteren den skal bruke på noden. Hold den
   loddrett og unna kroppen din og bordet.
3. Les av SWR-kurven (ståbølgeforhold): Den viser hvor mye signal antennen
   sender tilbake. Bunnpunktet må ligge på frekvensen til
   forhåndsinnstillingen din, 869.618 MHz for EU/UK (Narrow). Et bunnpunkt
   flere hundre MHz unna betyr at antennen er laget for et annet bånd.

En kvartbølge ved 868 MHz er 86 mm (bølgelengden er 345 mm). Lengden alene
forteller deg ikke båndet, fordi produsentene bretter og belaster
piskantenner. Det gjør NanoVNA-en.

## Kilder {#sources}

- Kabeltap: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  databladet for Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  databladene for Times Microwave LMR-240 og LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antenner: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  databladet for Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Forsterkning som signal klemt inn i mindre rom: [RF Cafe, introduksjon til antenner](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Kontakter: databladene for Rosenberger 32S102 (SMA) og 53S101 (N),
  Hirose U.FL-katalogen.
- Filtre: produktsiden for sysmocom cf866.5-kt30,
  [Citel gassutladningsavledere](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarisasjonstap: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipolforsterkning etter lengde: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Bølgelengde: lyshastigheten fra [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Lovlig grense: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  vedlegg 1, bånd h1.7. [Repeaterguiden](/repeater-guide/#legal) viser
  resten.
