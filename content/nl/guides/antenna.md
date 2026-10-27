---
title: Antennegids
lead: De antenne is de helft van je node. De juiste antenne, goed gemonteerd, reikt verder dan meer vermogen. Controleer de antenne op je companion, en kies, sluit aan en monteer er daarna een voor een repeater.
description: 'Kies en monteer een MeshCore-antenne voor 868 MHz: controleer een companion-sprietantenne, antennetypes en gain, connectors, kabelverlies per meter, filters, montage en hoe gain meetelt voor de wettelijke limiet.'
eyebrow: Companion en repeater · 868 MHz
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '45010ad0'
  seeded: '2026-10-26'
  fields: {title: '3a76cb0e', lead: '98430ade', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', '94c5bae4', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
---

Hoogte, een afgestemde antenne en een korte kabel leveren meer bereik op
dan elke extra milliwatt. Deze gids begint bij de companion, de radio
waarmee je berichten stuurt. Daarna komt de antenne op een repeater aan
bod, een node die berichten doorgeeft vanaf een dak of mast.

## Je companion {#companion}

{{< callout type="warning" >}}
Bevestig de antenne voordat je de radio aanzet. Een LoRa-radio die
zendt zonder antenne kan zijn eigen chip beschadigen.
{{< /callout >}}

De antenne die bij je board zat, voldoet. Bevestig hem, houd de node
rechtop en begin met berichten sturen. Een betere antenne op een
companion levert weinig op; een repeater binnen bereik levert veel op.

Koop alleen een losse sprietantenne als de meegeleverde kapot is of
ontbreekt. Niet elke sprietantenne die voor 868 MHz wordt verkocht, is
daarop afgestemd. [Controleer hem met een NanoVNA](#nanovna), een
antenne-analyser voor in je zak, voordat je erop vertrouwt, of leen er
een van een board dat werkt.

Een node naast een sterke zender hoort minder dan zou moeten. Een klein
[SAW-filter (surface acoustic wave)](#filters) tussen de radio en de
antenne houdt die zender buiten de ontvanger. Controleer eerst het
datasheet:

- **Maximaal ingangsvermogen.** Het filter zit ook in het pad van je
  eigen zending. Een board dat 22 dBm (160 mW) in een filter stuurt dat
  voor 15 dBm is gespecificeerd, maakt het filter kapot.
- **Doorlaatband.** Die moet de frequentie van je preset bevatten. Een
  filter voor 868.65 tot 869.25 MHz laat het EU/UK (Narrow)-kanaal op
  869.618 MHz niet door.

## Antennetypes voor een repeater {#types}

Elke antenne in de mesh staat rechtop. Kies het type op basis van waar de
nodes staan die je wilt bereiken:

- **Glasvezel-collineair.** Een witte buis op een mast, met gain rondom
  langs de horizon. De standaardkeuze voor een repeater die een stad
  bedient.
- **Dipool.** Korter, met minder gain en een hoge bundel. Hij bereikt
  nodes onder en boven je beter dan een collineair. Dat telt op een heuvel
  boven een dal.
- **Yagi.** Een draagarm met dwarselementen, gericht op één plek. Hij
  bereikt één verre repeater en verder weinig. Monteer hem met de elementen
  rechtop, want de polarisatie volgt de elementen.

## Gain en de bundel {#gain}

Gain voegt geen vermogen toe. Het neemt het signaal dat omhoog en omlaag
zou gaan en stuurt het langs de horizon. Zoals een zaklamp die je
focust: dezelfde batterij, een langere en smallere bundel. Een dipool en
een collineair van dezelfde fabrikant laten het zien:

| Antenne | Gain | Verticale bundelbreedte |
|---|---|---|
| Dipool (Sirio SO 868-915-2) | 2.2 dBi | 88 graden |
| Glasvezel-collineair (Sirio SPO 868-915-6) | 5.8 dBi | 23 graden |

{{< gain >}}

Het diagram snijdt door de mast, van opzij gezien. Draai het rond de mast
en je hebt de hele bundel: een donut voor de dipool, een platte schijf
voor de collineair. Een rechtopstaande antenne zendt in elke richting om
zich heen hetzelfde. Buiten de getekende bundel stopt het signaal niet; het
is zwakker, nog genoeg voor een node dichtbij.

Op een dak wil je een platte bundel. Op een heuvel hoog boven de nodes
gaat een bundel van 23 graden over hun hoofden heen; een dipool dekt ze
wel. Een Yagi gaat hierin verder: 16.6 dBi in een bundel van 23 graden
hoog en 25 graden breed (Amphenol Procom 7176870), en niets naar de
zijkanten.

Gain telt ten opzichte van een referentie. dBi vergelijkt met een ideale
antenne die in elke richting even sterk zendt. dBd vergelijkt met een
halvegolfdipool, die zelf 2.15 dBi heeft: zelfs de simpelste antenne
zendt niets recht omhoog of omlaag. Een langere dipool, 1.25 golflengte,
haalt 5.2 dBi. Een collineair stapelt in plaats daarvan halvegolfelementen
boven elkaar: hoe meer hij stapelt, hoe hoger de gain. Pers hetzelfde
signaal in de helft van de ruimte en het is daar twee keer zo sterk: 3 dB.
In een kwart, 4 keer zo sterk: 6 dB. Fabrikanten geven gain op in dBi; de
wettelijke limiet rekent in dBd, zie
[Binnen de wettelijke limiet](#legal).

### Welke gain voor jouw locatie {#choose-gain}

- **Heuvels, dalen of een dichtbebouwde stad: ongeveer 3 dBi.** De hoge
  bundel bereikt nodes boven en onder je, en om de hellingen en gebouwen
  heen die in de weg staan. Het werkt ook andersom: vanuit een dal gaat
  een platte bundel onder een repeater op de heuvel erboven door. De
  RAKwireless RAKARG12 is er zo een: een glasvezelbuis van 36 cm.
- **Buitenwijken of een stad met lage daken: 5 tot 6 dBi.** De
  standaard glasvezel-collineair.
- **Vlak, open land: 8 tot 10 dBi.** De platste bundel reikt het verst
  langs de horizon. Hoog gemonteerd gaat hij over de nodes dichtbij heen.

De gain in de naam is het beste cijfer over de hele band van de antenne.
De RAKARG12, verkocht als 3 dBi, heeft 2.8 dBi op 865 tot 870 MHz. Lees de
gaintabel in het datasheet af op de frequentie van je preset.

Boven 7 dBi gaat een board van 22 dBm over de wettelijke limiet, tenzij
kabel- en filterverlies het verschil goedmaken. Verlaag het zendvermogen
tot het klopt.

Hoge gain helpt alleen als je weet waar de nodes staan: langs de horizon
rond een repeater, of bij één verre repeater voor een Yagi. Een companion
in je hand wijst alle kanten op, dus de lage gain waarmee hij geleverd is,
past daar het best bij.

## Waarom verticaal {#vertical}

Antennes horen elkaar het best als ze dezelfde kant op wijzen. Het verlies
groeit met de hoek ertussen: 45 graden kost 3 dB, de helft van je signaal.
Bij 90 graden, een platte antenne tegenover een rechtopstaande, komt er in
theorie niets aan. De mesh staat rechtop, dus jouw antenne ook. Dat geldt
ook voor een companion op een bureau: leg hem plat en elke node om je heen
hoort minder.

## Connectors {#connectors}

Bestel de antenne met de connector die je board heeft. Elke adapter is
een extra verbinding om af te dichten en meer signaalverlies.

- **SMA.** Een schroefconnector van ongeveer 6 mm breed. De bus op de
  meeste boards heeft een gat in het midden; de antenne heeft de pin. Zo'n
  connector verliest ongeveer 0.03 dB op 868 MHz.
- **RP-SMA.** Dezelfde behuizing en schroefdraad als SMA, met de pin en
  het gat omgewisseld. Het lijkt op SMA en past er niet op. Controleer
  welke je board heeft voordat je bestelt.
- **U.FL (IPEX).** Een piepklein drukbusje op het board zelf. Een korte
  pigtailkabel loopt ervan naar een SMA-bus in de behuizing. Het is
  berekend op 30 keer koppelen, dus sluit het één keer aan en laat het
  zitten.
- **N.** De grote schroefconnector op glasvezelantennes en dikke kabel.
  Hij verliest hoogstens 0.05 dB. Een repeater heeft één adapter of
  pigtail nodig van N naar de SMA van het board.

## Kabelverlies {#cable}

Kabel kost signaal voordat het de antenne verlaat, in beide richtingen.
3 dB is de helft van je vermogen. De cijfers van de fabrikanten per meter,
op 868 tot 900 MHz:

| Kabel | Verlies per meter | Verlies over 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 meter RG174, de dunne pigtail die bij veel boards zit, verliest de helft
van je vermogen. Monteer het board bij de antenne met een korte pigtail,
of trek dikke kabel ernaartoe. Tel elke adapter en elk filter in het pad
bij de som op.

## Filters {#filters}

Een filter zit tussen de radio en de antenne. Het laat jouw band door en
blokkeert de rest, zodat een sterke zender in de buurt de ontvanger niet
overspoelt. Je hebt er een nodig als een node bij andere zenders minder
hoort dan hij zou moeten. Een repeater op een mast met basisstations voor
mobiele telefonie is zo'n node. Een filter kost signaal in beide
richtingen: tel het verlies mee zoals bij kabel.

| | SAW-filter | Cavityfilter |
|---|---|---|
| Grootte | Een paar millimeter, op een klein printje | Een metalen blok of buis |
| Verlies van een goede | onder 2 dB | onder 1 dB |
| Maximaal ingangsvermogen van een goede | 500 mW | meerdere watt |

De sysmocom cf866.5-kt30 is bijvoorbeeld een cavityfilter voor 863 tot
870 MHz dat hoogstens 1.0 dB verliest en 30 W aankan. Het is gemaakt voor
binnen, dus zet het in een afgedichte kast op een mast.

Filters verschillen sterk, dus lees het datasheet voordat je koopt. Het
opgegeven ingangsvermogen moet hoger zijn dan je zendvermogen, en de
frequentie van je preset moet in de doorlaatband vallen.

## Montage {#mounting}

- **Boven de dakrand.** De antenne heeft vrij zicht nodig in elke richting
  die hij bedient. Zelfs een paar meter boven de omliggende daken helpt.
  [Kies een locatie](/repeater-guide/#site) in de repeatergids laat zien
  hoe je het zicht controleert.
- **Weg van metaal.** Dakgoten, masten, andere antennes en metalen daken
  naast de antenne veranderen zijn patroon en afstemming. Monteer hem
  bovenop de mast, niet ernaast.
- **Rechtop.** Gebruik een waterpas; zie [Waarom verticaal](#vertical).
- **Druiplus.** Laat de kabel onder de connector hangen voordat hij omhoog
  of naar binnen gaat. Water druipt er dan af in plaats van de verbinding
  in te lopen.
- **Dicht elke buitenconnector af.** Water in een connector verhoogt het
  verlies en laat de pin corroderen. Dicht hem af tegen regen en
  controleer de afdichting elk jaar.
- **Bliksem.** Een antenne op een dak is een doelwit. Een gasontladingsbeveiliging
  in de kabel schakelt bij een piek en voert die af naar de aarde. Volg
  [Hardware](/repeater-guide/#hardware) in de repeatergids en je lokale
  regels voor aarding.

## Binnen de wettelijke limiet {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
In Europa gebruikt MeshCore de subband 869.40-869.65 MHz, met hoogstens
**500 mW** effectief uitgestraald vermogen (e.r.p.). De limiet rekent met
wat de antenne verlaat: antennegain telt erbij, kabel- en filterverlies
gaat eraf. Gain in dBi telt 2.15 dB minder, omdat de limiet wordt gemeten
ten opzichte van een dipool.
{{< /callout >}}

Een collineair van 5.8 dBi op een board van 22 dBm blijft binnen de
limiet. Dezelfde antenne op een board met een versterker niet, totdat je
het zendvermogen verlaagt. [Vermogen: e.r.p. en je antenne](/repeater-guide/#erp)
in de repeatergids heeft de som en 2 uitgewerkte voorbeelden.

## Controleer een antenne met een NanoVNA {#nanovna}

Een NanoVNA is een vectornetwerkanalyser voor in je zak. Hij laat zien op
welke frequentie een antenne is afgestemd, zodat je het weet voordat je
hem monteert. De NanoVNA-H meet tot 1.5 GHz, en dat dekt 868 MHz.

1. Kalibreer hem voor 800 tot 950 MHz met de open-, short- en
   load-stukjes uit zijn set.
2. Sluit de antenne aan via de adapter die hij op de node gaat gebruiken.
   Houd hem rechtop en weg van je lichaam en de tafel.
3. Lees de SWR-curve (staandegolfverhouding) af: die laat zien hoeveel
   signaal de antenne terugstuurt. De dip moet op de frequentie van je
   preset zitten, 869.618 MHz voor EU/UK (Narrow). Een dip honderden MHz
   verderop betekent dat de antenne voor een andere band is gemaakt.

Een kwartgolf op 868 MHz is 86 mm (de golflengte is 345 mm). Lengte alleen
zegt niets over de band, omdat fabrikanten sprietantennes vouwen en
belasten; de NanoVNA wel.

## Bronnen {#sources}

- Kabelverlies: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  het Huber+Suhner RG316-datasheet,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  de Times Microwave LMR-240- en LMR-400-datasheets,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antennes: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  het Sirio SO 868-915-2-datasheet,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Gain als signaal dat in minder ruimte wordt geperst: [RF Cafe, antenna introduction](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Connectors: de Rosenberger 32S102- (SMA) en 53S101-datasheets (N), de
  Hirose U.FL-catalogus.
- Filters: de productpagina van de sysmocom cf866.5-kt30,
  [Citel gasontladingsbeveiligingen](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarisatieverlies: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipoolgain per lengte: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Golflengte: lichtsnelheid van [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Wettelijke limiet: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Annex 1, band h1.7; de [repeatergids](/repeater-guide/#legal) noemt de
  rest.
