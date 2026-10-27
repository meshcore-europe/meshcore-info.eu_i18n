---
title: Antenneguide
lead: Antennen er halve noden din. Den rette antennen, godt montert, rekker lenger enn mer effekt. Sjekk antennen på companionen din, og velg, koble til og monter deretter en for en repeater.
description: 'Velg og monter en MeshCore-antenne for 868 MHz: sjekk pisken på en companion, antennetyper og gain, kontakter, kabeltap per meter, filtre, montering og hvordan gain teller mot den lovlige grensen.'
eyebrow: Companion og repeater · 868 MHz
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '45010ad0'
  seeded: '2026-10-26'
  fields: {title: '3a76cb0e', lead: '98430ade', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', '94c5bae4', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
---

Høyde, en avstemt antenne og en kort kabel gir mer rekkevidde enn noen ekstra milliwatt. Denne guiden begynner med companionen, radioen du sender meldinger fra. Deretter tar den for seg antennen på en repeater, en node som sender meldinger videre fra et tak eller en mast.

## Din companion {#companion}

{{< callout type="warning" >}}
Sett på antennen før du slår på radioen. En LoRa-radio som
sender uten antenne kan skade sin egen brikke.
{{< /callout >}}

Antennen som fulgte med kortet ditt gjør jobben. Sett den på, hold
noden loddrett, og begynn å sende meldinger. En bedre
antenne på en companion gir lite; en repeater innen rekkevidde gir mye.

Kjøp en egen pisk bare når den medfølgende er ødelagt eller mangler. Ikke
alle pisker som selges for 868 MHz er avstemt for det. [Sjekk den med en
NanoVNA](#nanovna), en antenneanalysator i lommeformat, før du stoler på den, eller lån en fra et kort som
virker.

En node ved siden av en sterk sender hører mindre enn den burde. Et lite
[SAW-filter (surface acoustic wave)](#filters) mellom radioen og
antennen holder den senderen ute av mottakeren. Sjekk databladet
først:

- **Maksimal inngangseffekt.** Filteret sitter også i stien til din egen
  sending. Et kort som sender 22 dBm (160 mW) inn i et filter laget for 15 dBm
  ødelegger filteret.
- **Passbånd.** Det må omfatte frekvensen til presetet ditt. Et filter for
  868.65 til 869.25 MHz slipper ikke gjennom kanalen EU/UK (Narrow) på
  869.618 MHz.

## Antennetyper for en repeater {#types}

Alle antenner i meshen står loddrett. Velg type etter hvor nodene du vil nå befinner seg:

- **Kollineær glassfiberantenne.** Et hvitt rør på en mast, med gain rundt hele horisonten. Standardvalget for en repeater som dekker en by.
- **Dipol.** Kortere, med mindre gain og en høy stråle. Den når noder under og over deg bedre enn en kollineær. Det betyr noe på en ås over en dal.
- **Yagi.** En bom med tverrelementer, rettet mot ett sted. Den når én fjern repeater og lite annet. Monter den med elementene loddrett, fordi polarisasjonen følger elementene.

## Gain og strålen {#gain}

Gain gir ikke mer effekt. Den tar signalet som ellers ville gått opp og ned
og sender det langs horisonten. Som en lommelykt du fokuserer: samme batteri,
en lengre og smalere stråle. En dipol og en kollineær fra samme produsent
viser det:

| Antenne | Gain | Vertikal strålebredde |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 grader |
| Kollineær glassfiberantenne (Sirio SPO 868-915-6) | 5.8 dBi | 23 grader |

{{< gain >}}

Diagrammet skjærer gjennom masten, sett fra siden. Drei det rundt
masten, og du har hele strålen: en smultring for dipolen, en flat skive
for den kollineære. En loddrett antenne sender likt i alle retninger rundt
seg. Utenfor den tegnede strålen stopper ikke signalet; det er svakere, men fortsatt
nok for en node i nærheten.

På et tak er en flat stråle det du vil ha. På en ås høyt over nodene
går en stråle på 23 grader over hodet på dem; en dipol dekker dem. En Yagi
tar dette lenger: 16.6 dBi i en stråle som er 23 grader høy
og 25 grader bred (Amphenol Procom
7176870), og ingenting til sidene.

Gain måles mot en referanse. dBi sammenligner med en ideell antenne som
sender likt i alle retninger. dBd sammenligner med en halvbølgedipol,
som selv har 2.15 dBi: selv den enkleste antennen sender ingenting rett
opp eller ned. En lengre dipol, 1.25 bølgelengder, når 5.2 dBi. En kollineær
stabler i stedet halvbølgeelementer over hverandre: jo flere den stabler, desto
høyere gain. Press det samme signalet inn i halve rommet, og det er
dobbelt så sterkt der: 3 dB. Inn i en fjerdedel, 4 ganger så sterkt: 6 dB.
Produsenter oppgir gain i dBi; den lovlige grensen regnes i dBd, se
[Innenfor den lovlige grensen](#legal).

### Hvilken gain for stedet ditt {#choose-gain}

- **Åser, daler eller en tett by: rundt 3 dBi.** Den høye strålen når
  noder over og under deg, og rundt skråningene og bygningene i veien.
  Det virker også omvendt: fra en dal går en flat stråle under en
  repeater på åsen over. RAKwireless RAKARG12 er en slik: et
  glassfiberrør på 36 cm.
- **Forsteder eller en småby med lave tak: 5 til 6 dBi.** Den vanlige
  kollineære glassfiberantennen.
- **Flatt, åpent land: 8 til 10 dBi.** Den flateste strålen når lengst
  langs horisonten. Montert høyt går den over nodene i nærheten.

Gainen i navnet er den beste verdien over antennens hele bånd.
RAKARG12, solgt som 3 dBi, har 2.8 dBi ved 865 til 870 MHz. Les gaintabellen
i databladet ved frekvensen til presetet ditt.

Over 7 dBi går et kort på 22 dBm over den lovlige grensen, med mindre tap i kabel og filter
utligner forskjellen. Senk sendeeffekten tilsvarende.

Høy gain hjelper bare når du vet hvor nodene er: langs horisonten
rundt en repeater, eller ved én fjern repeater for en Yagi. En companion i hånden
din peker i alle retninger, så den lave gainen den kom med passer den best.

## Hvorfor loddrett {#vertical}

Antenner hører hverandre best når de peker samme vei. Tapet øker med vinkelen mellom dem: 45 grader koster 3 dB, halve signalet ditt. Ved 90 grader, en liggende antenne mot en loddrett, kommer i teorien ingenting fram. Meshen står loddrett, så det gjør antennen din også. Dette gjelder også en companion på et skrivebord: legg den flatt, og alle noder rundt deg hører mindre.

## Kontakter {#connectors}

Bestill antennen med den kontakten
kortet ditt har. Hver adapter er enda en skjøt å tette og mer signal
som går tapt.

- **SMA.** En gjenget kontakt rundt 6 mm bred. Kontakten på de fleste kort
  har et hull i midten; antennen har pinnen. En kontakt av denne
  typen taper rundt 0.03 dB ved 868 MHz.
- **RP-SMA.** Samme hus og gjenger som SMA, med pinnen og hullet
  byttet om. Den ser ut som SMA og passer ikke sammen med den. Sjekk hvilken
  kortet ditt har før du bestiller.
- **U.FL (IPEX).** En liten trykk-på-kontakt på selve kortet. En kort
  pigtail-kabel går fra den til en SMA-kontakt i kabinettet. Den tåler
  30 tilkoblinger, så koble den til én gang og la den sitte.
- **N.** Den store gjengede kontakten på glassfiberantenner og tykk
  kabel. Den taper høyst 0.05 dB. En repeater trenger én
  adapter eller pigtail fra N til kortets SMA.

## Kabeltap {#cable}

Kabelen koster signal før det forlater antennen, i begge retninger. 3 dB
er halve effekten din. Produsentenes tall per meter, ved 868 til 900 MHz:

| Kabel | Tap per meter | Tap over 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 meter RG174, den tynne pigtail-kabelen som følger med mange kort, taper halve
effekten din. Monter kortet ved antennen med en kort pigtail, eller
legg tykk kabel fram til den. Legg til hver adapter og hvert filter i stien til summen.

## Filtre {#filters}

Et filter sitter mellom radioen og antennen. Det slipper gjennom båndet ditt og
stopper resten, så en sterk sender i nærheten ikke overdøver
mottakeren. Du trenger et når en node hører mindre enn den burde nær andre
sendere. En repeater på en mast med basestasjoner for mobiltelefon er en slik
node. Et filter koster signal i begge retninger: regn tapet som
kabel.

| | SAW-filter | Kavitetsfilter |
|---|---|---|
| Størrelse | Noen få millimeter, på et lite kort | En metallblokk eller et rør |
| Tap i et godt filter | under 2 dB | under 1 dB |
| Maksimal inngangseffekt i et godt filter | 500 mW | flere watt |

sysmocom cf866.5-kt30, for eksempel, er et kavitetsfilter for 863 til
870 MHz som taper høyst 1.0 dB og tåler 30 W. Det er laget for innendørs bruk,
så sett det i en tett boks på en mast.

Filtre varierer mye, så sjekk databladet før du kjøper. Den oppgitte
inngangseffekten må være høyere enn sendeeffekten din, og passbåndet må omfatte
frekvensen til presetet ditt.

## Montering {#mounting}

- **Over takkanten.** Antennen trenger fri sikt i alle retninger den dekker. Selv noen få meter over takene rundt hjelper. [Velg et sted](/repeater-guide/#site) i repeaterguiden viser hvordan du sjekker sikten.
- **Unna metall.** Takrenner, master, andre antenner og metalltak rett ved antennen endrer strålemønsteret og avstemmingen. Monter den på toppen av masten, ikke ved siden av.
- **Loddrett.** Bruk et vater, se [Hvorfor loddrett](#vertical).
- **Dryppsløyfe.** La kabelen henge ned under kontakten før den går opp eller inn. Da drypper vannet av i stedet for å renne inn i skjøten.
- **Tett alle utendørskontakter.** Vann i en kontakt øker tapet og får pinnen til å ruste. Tett den mot regn og sjekk tettingen hvert år.
- **Lyn.** En antenne på et tak er et mål. En gassavleder i kabelen utløses ved et overspenningsstøt og leder det til jord. Følg [Maskinvare](/repeater-guide/#hardware) i repeaterguiden og de lokale reglene dine for jording.

## Innenfor den lovlige grensen {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
I Europa bruker MeshCore delbåndet 869.40-869.65 MHz, med høyst
**500 mW** effektiv utstrålt effekt (e.r.p.). Grensen regner det som forlater antennen:
antennegain legges til, tap i kabel og filter trekkes fra. Gain i dBi regnes
2.15 dB lavere, fordi grensen måles mot en dipol.
{{< /callout >}}

En kollineær på 5.8 dBi på et kort på 22 dBm holder seg innenfor grensen. Den samme
antennen på et kort med forsterker gjør det ikke, før du senker sendeeffekten.
[Effekt: e.r.p. og antennen din](/repeater-guide/#erp) i
repeaterguiden har regnestykket og 2 gjennomregnede eksempler.

## Sjekk en antenne med en NanoVNA {#nanovna}

En NanoVNA er en vektornettverksanalysator i lommeformat. Den viser hvilken
frekvens en antenne er avstemt for, så du vet det før du monterer den.
NanoVNA-H måler opp til 1.5 GHz, som dekker 868 MHz.

1. Kalibrer den for 800 til 950 MHz med open-, short- og load-delene
   fra settet.
2. Koble til antennen gjennom adapteren den skal bruke på noden. Hold den
   loddrett og unna kroppen din og bordet.
3. Les SWR-kurven (ståbølgeforhold): den viser hvor mye signal
   antennen sender tilbake. Dippen må ligge på frekvensen til presetet ditt, 869.618
   MHz for EU/UK (Narrow). En dipp hundrevis av MHz unna betyr at antennen er
   laget for et annet bånd.

En kvartbølge ved 868 MHz er 86 mm (bølgelengden er 345 mm). Lengden
alene sier deg ikke båndet, fordi produsenter folder og belaster pisker;
det gjør NanoVNA-en.

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
- Gain som signal presset inn i mindre rom: [RF Cafe, antenna introduction](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Kontakter: databladene for Rosenberger 32S102 (SMA) og 53S101 (N), Hirose U.FL-katalogen.
- Filtre: produktsiden for sysmocom cf866.5-kt30,
  [Citel gassavledere](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarisasjonstap: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipolgain etter lengde: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Bølgelengde: lyshastigheten fra [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Lovlig grense: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Annex 1, bånd h1.7. [Repeaterguiden](/repeater-guide/#legal) lister opp resten.
