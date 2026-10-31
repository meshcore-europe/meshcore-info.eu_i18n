---
title: Antennguide
lead: Rätt antenn, väl monterad, når längre än mer effekt. Kontrollera antennen på din companion, och välj, anslut och montera sedan en antenn till en repeater.
description: 'Välj och montera en MeshCore-antenn för 868 MHz: kontrollera en companions spröt, antenntyper och förstärkning, kontakter, kabelförlust per meter, filter, montering och hur förstärkningen räknas mot den lagliga gränsen.'
eyebrow: Companion och repeater · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-10-31'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Höjd, en avstämd antenn och en kort kabel ger mer räckvidd än några extra
milliwatt. Den här guiden börjar med din companion, radion du skickar
meddelanden från. Sedan handlar den om antennen på en repeater, en nod som
skickar meddelanden vidare från ett tak eller en mast.

## Din companion {#companion}

{{< callout type="warning" >}}
Sätt fast antennen innan du slår på radion. En LoRa-radio som
sänder utan antenn kan skada sitt eget chip.
{{< /callout >}}

Antennen som följde med ditt kort räcker. Sätt fast den, håll
noden upprätt och börja skicka meddelanden. En bättre
antenn på en companion ger lite; en repeater inom räckhåll ger mycket.

Köp en separat spröantenn bara om den medföljande är trasig eller saknas. Inte
alla spröantenner som säljs för 868 MHz är avstämda för den frekvensen. [Kontrollera den med en
NanoVNA](#nanovna), en antennanalysator i fickformat, innan du litar på den, eller låna en från ett kort som
fungerar.

En nod nära en stark sändare hör sämre än den borde. Ett litet
[SAW-filter (surface acoustic wave)](#filters) mellan radion och
antennen håller den sändaren borta från mottagaren. Läs först filtrets
datablad:

- **Maximal ineffekt.** Filtret sitter också i signalvägen för din egen
  sändning. Ett kort som sänder 22 dBm (160 mW) in i ett filter klassat för 15 dBm
  förstör filtret.
- **Passband.** Det måste omfatta frekvensen för din preset. Ett filter för
  868.65 till 869.25 MHz släpper inte igenom EU/UK (Narrow)-kanalen på
  869.618 MHz.

## Antenntyper för en repeater {#types}

Alla antenner i meshen står upprätt. Välj typ efter var noderna du vill nå
finns:

- **Glasfiberkollinear.** Ett vitt rör på en mast, med förstärkning runt
  hela horisonten. Standardvalet för en repeater som täcker en ort.
- **Dipol.** Kortare, med lägre förstärkning och en hög lob. Den når noder
  under och över dig bättre än en kollinear, till exempel från en kulle
  ovanför en dal.
- **Yagi.** En bom med tvärelement, riktad mot en plats. Den når en enda
  avlägsen repeater och lite annat. Montera den med elementen upprätt,
  eftersom polarisationen följer elementen.

## Förstärkning och stråle {#gain}

Förstärkning tillför ingen effekt. Den tar signalen som skulle gå uppåt och nedåt
och skickar den längs horisonten. Som en ficklampa du fokuserar: samma batteri,
en längre och smalare stråle. En dipol och en kollinear från samma tillverkare
visar det:

| Antenn | Förstärkning | Vertikal strålbredd |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 grader |
| Glasfiberkollinear (Sirio SPO 868-915-6) | 5.8 dBi | 23 grader |

{{< gain >}}

Diagrammet skär genom masten, sett från sidan. Vrid det runt
masten så har du hela strålen: en munk för dipolen, en platt skiva
för kollinearen. En upprätt antenn sänder likadant åt alla håll runt
sig. Utanför den ritade strålen tar signalen inte slut. Den är svagare, men räcker
fortfarande för en nod i närheten.

På ett tak vill du ha en platt stråle. På en kulle högt ovanför noderna
går en stråle på 23 grader över deras huvuden. En dipol täcker dem. En Yagi
går ännu längre: 16.6 dBi i en stråle som är 23 grader hög
och 25 grader bred (Amphenol Procom
7176870), och ingenting åt sidorna.

Förstärkning räknas mot en referens. dBi jämför med en ideal antenn som
sänder lika mycket åt alla håll. dBd jämför med en halvvågsdipol,
som själv har 2.15 dBi: även den enklaste antennen sänder ingenting rakt
upp eller ner. En längre dipol, 1.25 våglängder, når 5.2 dBi. En kollinear
staplar i stället halvvågselement ovanpå varandra: ju fler den staplar, desto
högre förstärkning. Pressa ihop samma signal till halva utrymmet så är den
dubbelt så stark där: 3 dB. Till en fjärdedel, 4 gånger så stark: 6 dB.
Tillverkare anger förstärkning i dBi. Den lagliga gränsen räknas i dBd, se
[Inom den lagliga gränsen](#legal).

### Vilken förstärkning passar din plats {#choose-gain}

- **Kullar, dalar eller en tät stad: cirka 3 dBi.** Den höga strålen når
  noder över och under dig, och runt sluttningar och byggnader i vägen.
  Det gäller åt andra hållet också: från en dal går en platt stråle under en
  repeater på kullen ovanför. RAKwireless RAKARG12 är en sådan: ett
  glasfiberrör på 36 cm.
- **Förorter eller en ort med låga tak: 5 till 6 dBi.** Den vanliga
  glasfiberkollinearen.
- **Platt, öppet land: 8 till 10 dBi.** Den plattaste strålen når längst
  längs horisonten. Monterad högt går den över noderna i närheten.

Förstärkningen i namnet är det bästa värdet över antennens hela band.
RAKARG12 säljs som 3 dBi men har 2.8 dBi vid 865 till 870 MHz. Läs
förstärkningstabellen i databladet vid din presets frekvens.

Över 7 dBi hamnar ett kort på 22 dBm över den lagliga gränsen, om inte
förluster i kabel och filter tar upp skillnaden. Sänk sändeffekten så att det
stämmer.

Hög förstärkning hjälper bara när du vet var noderna finns: längs horisonten
runt en repeater, eller mot en avlägsen repeater för en Yagi. En companion i
din hand pekar åt alla håll, så den låga förstärkningen den kom med passar den
bäst.

## Varför vertikalt {#vertical}

Antenner hör varandra bäst när de pekar åt samma håll. Förlusten ökar med
vinkeln mellan dem: 45 grader kostar 3 dB, halva din signal. Vid 90 grader,
en liggande antenn mot en upprätt, kommer i teorin ingenting fram. Meshen
står upprätt, så din antenn ska också göra det. Det gäller även en
companion på ett skrivbord: lägger du den platt hör alla noder runt dig
sämre.

## Kontakter {#connectors}

Beställ antennen med den kontakt
som ditt kort har. Varje adapter är ännu en skarv att täta och mer signal
som går förlorad.

- **SMA.** En gängad kontakt som är cirka 6 mm bred. Uttaget på de flesta kort
  har ett hål i mitten; antennen har stiftet. En kontakt av det här
  slaget förlorar cirka 0.03 dB vid 868 MHz.
- **RP-SMA.** Samma hus och gänga som SMA, med stiftet och hålet
  ombytta. Den ser ut som SMA men passar inte ihop med den. Kontrollera vilken
  ditt kort har innan du beställer.
- **U.FL (IPEX).** Ett pyttelitet tryckuttag direkt på kortet. En kort
  pigtail-kabel går från det till ett SMA-uttag i höljet. Det är klassat för
  30 anslutningscykler, så anslut det en gång och låt det sitta.
- **N.** Den stora gängade kontakten på glasfiberantenner och grov
  kabel. Den förlorar högst 0.05 dB. En repeater behöver en
  adapter eller pigtail från N till kortets SMA.

## Kabelförlust {#cable}

Kabeln kostar signal innan signalen lämnar antennen, åt båda hållen. 3 dB
är halva din effekt. Tillverkarnas värden per meter, vid 868 till 900 MHz:

| Kabel | Förlust per meter | Förlust över 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 meter RG174, den tunna pigtail-kabeln som följer med många kort, förlorar
halva din effekt. Montera kortet vid antennen med en kort pigtail, eller
dra grov kabel till den. Räkna in varje adapter och filter längs vägen i summan.

## Filter {#filters}

Ett filter sitter mellan radion och antennen. Det släpper igenom ditt band
och blockerar resten, så att en stark sändare i närheten inte dränker
mottagaren. Du behöver ett när en nod hör sämre än den borde nära andra
sändare. En repeater på en mast med basstationer för mobiltelefoni är en
sådan nod. Ett filter kostar signal åt båda hållen: räkna in dess förlust
som för kabel.

| | SAW-filter | Kavitetsfilter |
|---|---|---|
| Storlek | Några millimeter, på ett litet kort | Ett metallblock eller ett rör |
| Förlust i ett bra filter | under 2 dB | under 1 dB |
| Maximal ineffekt i ett bra filter | 500 mW | flera watt |

sysmocom cf866.5-kt30 är till exempel ett kavitetsfilter för 863 till
870 MHz som förlorar högst 1.0 dB och tål 30 W. Det är gjort för inomhusbruk,
så sätt det i en tät låda på masten.

Filter skiljer sig mycket åt, så läs databladet innan du köper. Den klassade
ineffekten måste vara högre än din sändeffekt. Passbandet måste omfatta
frekvensen för din preset.

## Montering {#mounting}

- **Ovanför takkanten.** Antennen behöver fri sikt åt alla håll den ska
  täcka. Redan några meter över de omgivande taken hjälper. [Välj en
  plats](/repeater-guide/#site) i repeaterguiden visar hur du kontrollerar
  sikten.
- **På avstånd från metall.** Hängrännor, master, andra antenner och plåttak
  intill antennen ändrar dess strålningsdiagram och avstämning. Montera den
  överst på masten, inte bredvid.
- **Upprätt.** Använd ett vattenpass, se [Varför vertikalt](#vertical).
- **Droppslinga.** Låt kabeln hänga under kontakten innan den går upp eller
  in. Då droppar vattnet av i stället för att rinna in i skarven.
- **Täta varje kontakt utomhus.** Vatten i en kontakt ökar förlusten och
  får stiftet att korrodera. Täta den mot regn och kontrollera tätningen
  varje år.
- **Blixtnedslag.** En antenn på ett tak är ett mål. En gasurladdningsavledare
  i kabeln löser ut vid en spänningstopp och leder den till jord. Följ
  [Hårdvara](/repeater-guide/#hardware) i repeaterguiden och dina lokala
  regler för jordning.

## Inom den lagliga gränsen {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
I Europa använder MeshCore delbandet 869.40-869.65 MHz, med högst
**500 mW** effektiv utstrålad effekt (e.r.p.). Gränsen gäller det som lämnar antennen:
antennens förstärkning läggs till, förlust i kabel och filter dras av. Förstärkning i dBi räknas
2.15 dB lägre, eftersom gränsen mäts mot en dipol.
{{< /callout >}}

En kollinear på 5.8 dBi på ett kort med 22 dBm håller sig inom gränsen. Samma
antenn på ett kort med förstärkare gör det inte, förrän du sänker sändeffekten.
[Effekt: e.r.p. och din antenn](/repeater-guide/#erp) i
repeaterguiden har uträkningen och 2 räknade exempel.

## Kontrollera en antenn med en NanoVNA {#nanovna}

En NanoVNA är en vektornätverksanalysator i fickformat. Den visar vilken
frekvens en antenn är avstämd för, så att du vet det innan du monterar den.
NanoVNA-H mäter upp till 1.5 GHz, vilket omfattar 868 MHz.

1. Kalibrera den för 800 till 950 MHz med open-, short- och load-delarna
   från satsen som följer med.
2. Anslut antennen via den adapter den ska använda på noden. Håll den
   upprätt och på avstånd från kroppen och bordet.
3. Läs av SWR-kurvan (ståendevågförhållande): den visar hur mycket signal
   antennen skickar tillbaka. Dippen måste ligga på din presets frekvens,
   869.618 MHz för EU/UK (Narrow). En dipp hundratals MHz bort betyder att
   antennen är gjord för ett annat band.

En kvartsvåg vid 868 MHz är 86 mm (våglängden är 345 mm). Längden ensam
avslöjar inte bandet, eftersom tillverkare viker och belastar spröantenner.
Det gör NanoVNA:n.

## Källor {#sources}

- Kabelförlust: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  databladet för Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  databladen för Times Microwave LMR-240 och LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antenner: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  databladet för Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Förstärkning som signal hoppressad på mindre utrymme: [RF Cafe, introduktion till antenner](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Kontakter: databladen för Rosenberger 32S102 (SMA) och 53S101 (N),
  Hiroses U.FL-katalog.
- Filter: produktsidan för sysmocom cf866.5-kt30,
  [Citel gasurladdningsavledare](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarisationsförlust: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipolens förstärkning efter längd: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Våglängd: ljusets hastighet från [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Laglig gräns: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Annex 1, band h1.7. [Repeaterguiden](/repeater-guide/#legal) listar
  resten.
