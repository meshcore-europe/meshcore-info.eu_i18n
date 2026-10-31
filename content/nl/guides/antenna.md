---
title: Antennegids
lead: Een goede antenne, goed gemonteerd, reikt verder dan meer vermogen. Controleer eerst de antenne op je companion. Kies daarna een antenne voor een repeater, sluit hem aan en monteer hem.
description: 'Kies en monteer een MeshCore-antenne voor 868 MHz: een companion-sprietantenne controleren, antennetypes en versterking, connectoren, kabelverlies per meter, filters, montage en hoe versterking meetelt voor de wettelijke grens.'
eyebrow: Companion en repeater · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-10-31'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Hoogte, een afgestemde antenne en een korte kabel leveren meer bereik op
dan elke extra milliwatt. Deze gids begint bij de companion: de radio
waarmee je berichten stuurt. Daarna gaat het over de antenne op een
repeater. Dat is een node die berichten vanaf een dak of mast doorgeeft.

## Je companion {#companion}

{{< callout type="warning" >}}
Sluit de antenne aan voordat je de radio aanzet. Een LoRa-radio die
zonder antenne zendt, kan zijn eigen chip beschadigen.
{{< /callout >}}

De antenne die bij je board zat, doet zijn werk. Sluit hem aan, houd de
node rechtop en begin met berichten sturen. Een betere antenne op een
companion levert weinig op. Een repeater binnen bereik levert veel op.

Koop alleen een losse sprietantenne als de meegeleverde kapot is of
ontbreekt. Niet elke sprietantenne die voor 868 MHz wordt verkocht, is
daar ook op afgestemd. [Controleer hem met een NanoVNA](#nanovna), een
antenne-analyzer op zakformaat, voordat je erop vertrouwt. Of leen er een
van een board dat werkt.

Een node naast een sterke zender ontvangt minder dan hij zou moeten. Een
klein [SAW-filter (surface acoustic wave)](#filters) tussen de radio en de
antenne houdt die zender uit de ontvanger. Lees eerst de datasheet:

- **Maximaal ingangsvermogen.** Het filter zit ook in het pad van je eigen
  uitzending. Zendt een board 22 dBm (160 mW) in een filter dat tot 15 dBm
  aankan, dan gaat het filter kapot.
- **Doorlaatband.** Die moet de frequentie van je preset bevatten. Een
  filter voor 868.65 tot 869.25 MHz laat het EU/UK (Narrow)-kanaal op
  869.618 MHz niet door.

## Antennetypes voor een repeater {#types}

Elke antenne op de mesh staat rechtop. Kies het type op basis van waar de
nodes staan die je wilt bereiken:

- **Glasvezel-collineair.** Een witte buis op een mast, met versterking
  rondom langs de horizon. De standaardkeuze voor een repeater die een
  stad of dorp bedient.
- **Dipool.** Korter, met minder versterking en een hoge bundel. Hij
  bereikt nodes onder en boven je beter dan een collineaire antenne,
  bijvoorbeeld vanaf een heuvel boven een dal.
- **Yagi.** Een boom met dwarselementen, gericht op één plek. Hij bereikt
  één verre repeater en weinig anders. Monteer hem met de elementen
  rechtop, want zijn polarisatie volgt de elementen.

## Versterking en de bundel {#gain}

Versterking voegt geen vermogen toe. De antenne neemt het signaal dat
omhoog en omlaag zou gaan, en stuurt het langs de horizon. Vergelijk het
met een zaklamp die je scherpstelt: dezelfde batterij, een langere en
smallere bundel. Een dipool en een collineaire antenne van dezelfde
fabrikant laten dat zien:

| Antenne | Versterking | Verticale bundelbreedte |
|---|---|---|
| Dipool (Sirio SO 868-915-2) | 2.2 dBi | 88 graden |
| Glasvezel-collineair (Sirio SPO 868-915-6) | 5.8 dBi | 23 graden |

{{< gain >}}

Het diagram is een doorsnede door de mast, van opzij gezien. Draai het
rond de mast en je hebt de hele bundel: een donut bij de dipool, een
platte schijf bij de collineaire antenne. Een rechtopstaande antenne
zendt in elke richting rondom even sterk. Buiten de getekende bundel houdt
het signaal niet op. Het is daar zwakker, maar nog genoeg voor een node
dichtbij.

Op een dak wil je een platte bundel. Op een heuvel hoog boven de nodes
gaat een bundel van 23 graden over hun hoofden heen. Een dipool bereikt
ze wel. Een Yagi gaat nog verder: 16.6 dBi in een bundel van 23 graden
hoog en 25 graden breed (Amphenol Procom 7176870), en niets opzij.

Versterking meet je ten opzichte van een referentie. dBi vergelijkt met
een ideale antenne die in elke richting even sterk zendt. dBd vergelijkt
met een halvegolfdipool, die zelf 2.15 dBi heeft. Zelfs de eenvoudigste
antenne zendt namelijk niets recht omhoog of omlaag. Een langere dipool,
van 1.25 golflengte, haalt 5.2 dBi. Een collineaire antenne stapelt in
plaats daarvan halvegolfelementen boven elkaar. Hoe meer elementen, hoe
hoger de versterking. Pers je hetzelfde signaal in de helft van de ruimte,
dan is het daar twee keer zo sterk: 3 dB. In een kwart is het 4 keer zo
sterk: 6 dB. Fabrikanten geven versterking op in dBi. De wettelijke grens
rekent in dBd, zie [Binnen de wettelijke grens](#legal).

### Welke versterking past bij je locatie {#choose-gain}

- **Heuvels, dalen of een dichtbebouwde stad: rond 3 dBi.** De hoge
  bundel bereikt nodes boven en onder je, en rond hellingen en gebouwen
  die in de weg staan. Het werkt ook andersom: vanuit een dal gaat een
  platte bundel onder een repeater op de heuvel erboven door. De
  RAKwireless RAKARG12 is zo'n antenne: een glasvezelbuis van 36 cm.
- **Buitenwijken of een dorp met lage daken: 5 tot 6 dBi.** De standaard
  glasvezel-collineaire antenne.
- **Vlak, open land: 8 tot 10 dBi.** De platste bundel reikt het verst
  langs de horizon. Hoog gemonteerd gaat hij over de nodes dichtbij heen.

De versterking in de naam is het beste cijfer over de hele band van de
antenne. De RAKARG12, verkocht als 3 dBi, heeft 2.8 dBi op 865 tot
870 MHz. Kijk in de versterkingstabel van de datasheet bij de frequentie
van je preset.

Boven 7 dBi gaat een board van 22 dBm over de wettelijke grens, tenzij
kabel- en filterverlies het verschil goedmaken. Verlaag het zendvermogen
dan zoveel als nodig is.

Hoge versterking helpt alleen als je weet waar de nodes staan: langs de
horizon rond een repeater, of bij een Yagi op één verre repeater. Een
companion in je hand wijst alle kanten op. De lage versterking waarmee hij
geleverd werd, past daar het best bij.

## Waarom verticaal {#vertical}

Antennes horen elkaar het best als ze dezelfde kant op wijzen. Het
verlies groeit met de hoek ertussen: 45 graden kost 3 dB, de helft van je
signaal. Bij 90 graden, een liggende antenne tegenover een staande, komt
er in theorie niets aan. De mesh staat rechtop, dus jouw antenne ook. Dat
geldt ook voor een companion op je bureau: leg je hem plat, dan hoort
elke node om je heen minder.

## Connectoren {#connectors}

Bestel de antenne met de connector die je board heeft. Elke adapter is
weer een verbinding die je moet afdichten, en kost signaal.

- **SMA.** Een schroefconnector van ongeveer 6 mm breed. De bus op de
  meeste boards heeft een gat in het midden. De antenne heeft de pin. Zo'n
  connector verliest ongeveer 0.03 dB op 868 MHz.
- **RP-SMA.** Dezelfde behuizing en schroefdraad als SMA, maar pin en gat
  zijn omgewisseld. Hij lijkt op SMA, maar past er niet op. Kijk welke je
  board heeft voordat je bestelt.
- **U.FL (IPEX).** Een piepkleine klikconnector op het board zelf. Een
  korte pigtailkabel loopt ervan naar een SMA-bus in de behuizing. Hij is
  ontworpen voor 30 keer aansluiten. Sluit hem dus één keer aan en laat
  hem zitten.
- **N.** De grote schroefconnector op glasvezelantennes en dikke kabel.
  Hij verliest hooguit 0.05 dB. Een repeater heeft één adapter of pigtail
  nodig van N naar de SMA van het board.

## Kabelverlies {#cable}

Kabel kost signaal voordat het de antenne verlaat, in beide richtingen.
3 dB is de helft van je vermogen. Dit zijn de cijfers van de fabrikanten
per meter, op 868 tot 900 MHz:

| Kabel | Verlies per meter | Verlies over 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 meter RG174, de dunne pigtail die bij veel boards zit, kost de helft van
je vermogen. Monteer het board bij de antenne met een korte pigtail, of
trek er dikke kabel naartoe. Tel elke adapter en elk filter in het pad
mee in de som.

## Filters {#filters}

Een filter zit tussen de radio en de antenne. Het laat je band door en
blokkeert de rest. Zo overstemt een sterke zender in de buurt de
ontvanger niet. Je hebt er een nodig als een node minder hoort dan hij
zou moeten in de buurt van andere zenders. Een repeater op een mast met
basisstations voor mobiele telefonie is zo'n node. Een filter kost signaal
in beide richtingen: tel het verlies mee zoals bij kabel.

| | SAW-filter | Caviteitsfilter |
|---|---|---|
| Afmeting | Een paar millimeter, op een klein board | Een metalen blok of buis |
| Verlies van een goed exemplaar | onder 2 dB | onder 1 dB |
| Maximaal ingangsvermogen van een goed exemplaar | 500 mW | enkele watts |

De sysmocom cf866.5-kt30 is bijvoorbeeld een caviteitsfilter voor 863 tot
870 MHz. Hij verliest hooguit 1.0 dB en kan 30 W aan. Hij is gemaakt voor
binnen, dus zet hem op een mast in een afgesloten kast.

Filters verschillen sterk, dus lees de datasheet voordat je koopt. Het
toegestane ingangsvermogen moet hoger zijn dan je zendvermogen. De
doorlaatband moet de frequentie van je preset bevatten.

## Montage {#mounting}

- **Boven de dakrand.** De antenne heeft vrij zicht nodig in elke richting
  die hij bedient. Zelfs een paar meter boven de omliggende daken helpt al.
  In de repeatergids lees je bij [Kies een locatie](/repeater-guide/#site)
  hoe je het zicht controleert.
- **Uit de buurt van metaal.** Dakgoten, masten, andere antennes en
  metalen daken naast de antenne veranderen het stralingspatroon en de
  afstemming. Monteer hem boven op de mast, niet ernaast.
- **Rechtop.** Gebruik een waterpas, zie [Waarom verticaal](#vertical).
- **Druiplus.** Laat de kabel onder de connector doorhangen voordat hij
  omhoog of naar binnen gaat. Water druipt dan af en loopt niet de
  verbinding in.
- **Dicht elke connector buiten af.** Water in een connector verhoogt het
  verlies en laat de pin corroderen. Dicht hem af tegen regen en controleer
  de afdichting elk jaar.
- **Bliksem.** Een antenne op een dak is een doelwit. Een gasontladingsbuis
  in de kabel slaat door bij een piekspanning en leidt die naar aarde.
  Volg [Hardware](/repeater-guide/#hardware) in de repeatergids en de
  plaatselijke regels voor aarding.

## Binnen de wettelijke grens {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
In Europa gebruikt MeshCore de subband 869.40-869.65 MHz, met hooguit
**500 mW** effectief uitgestraald vermogen (e.r.p.). De grens telt wat de
antenne verlaat: antenneversterking telt op, kabel- en filterverlies gaan
eraf. Versterking in dBi telt 2.15 dB minder, omdat de grens ten opzichte
van een dipool wordt gemeten.
{{< /callout >}}

Een collineaire antenne van 5.8 dBi op een board van 22 dBm blijft binnen
de grens. Dezelfde antenne op een board met een versterker niet, tot je
het zendvermogen verlaagt. In de repeatergids vind je bij
[Vermogen: e.r.p. en je antenne](/repeater-guide/#erp) de som en 2
uitgewerkte voorbeelden.

## Een antenne controleren met een NanoVNA {#nanovna}

Een NanoVNA is een vector network analyzer op zakformaat. Je ziet ermee
op welke frequentie een antenne is afgestemd. Zo weet je dat voordat je
hem monteert. De NanoVNA-H meet tot 1.5 GHz, dus 868 MHz valt erbinnen.

1. Kalibreer hem voor 800 tot 950 MHz met de open-, short- en
   load-stukjes uit de set.
2. Sluit de antenne aan via de adapter die hij op de node gaat gebruiken.
   Houd hem rechtop en uit de buurt van je lichaam en de tafel.
3. Lees de SWR-curve (staandegolfverhouding) af: die laat zien hoeveel
   signaal de antenne terugstuurt. De dip moet op de frequentie van je
   preset liggen, 869.618 MHz voor EU/UK (Narrow). Ligt de dip honderden
   MHz verderop, dan is de antenne voor een andere band gemaakt.

Een kwart golflengte op 868 MHz is 86 mm (de golflengte is 345 mm). De
lengte alleen vertelt je de band niet, want fabrikanten vouwen en
verlengen sprietantennes elektrisch. De NanoVNA vertelt het je wel.

## Bronnen {#sources}

- Kabelverlies: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  de datasheet van Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  de datasheets van Times Microwave LMR-240 en LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antennes: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  de datasheet van de Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Versterking als signaal in minder ruimte geperst: [RF Cafe, antenna introduction](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Connectoren: de datasheets van Rosenberger 32S102 (SMA) en 53S101 (N),
  de catalogus van Hirose U.FL.
- Filters: de productpagina van de sysmocom cf866.5-kt30,
  [Citel-gasontladingsbuizen](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarisatieverlies: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Versterking van een dipool per lengte: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Golflengte: lichtsnelheid volgens [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Wettelijke grens: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Annex 1, band h1.7. De [repeatergids](/repeater-guide/#legal) noemt de
  rest.
