---
title: Antennguide
lead: Antennen är halva din nod. Rätt antenn, väl monterad, når längre än mer effekt. Kontrollera antennen på din companion, välj sedan en antenn för en repeater, anslut den och montera den.
description: 'Välj och montera en MeshCore-antenn för 868 MHz: kontrollera en companion-pinnantenn, antenntyper och förstärkning, kontakter, kabelförlust per meter, filter, montering och hur förstärkning räknas mot den lagliga gränsen.'
eyebrow: Companion och repeater · 868 MHz
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '45010ad0'
  seeded: '2026-10-26'
  fields: {title: '3a76cb0e', lead: '98430ade', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', '94c5bae4', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
---

Höjd, en avstämd antenn och en kort kabel ger mer räckvidd än varje extra
milliwatt. Den här guiden börjar med din companion, radion du skickar
meddelanden från. Sedan tar den upp antennen på en repeater, en nod som
skickar meddelanden vidare från ett tak eller en mast.

## Din companion {#companion}

{{< callout type="warning" >}}
Sätt fast antennen innan du slår på radion. En LoRa-radio som sänder
utan antenn kan skada sitt eget chip.
{{< /callout >}}

Antennen som följde med ditt kort duger. Sätt fast den, håll noden
upprätt och börja skicka meddelanden. En bättre antenn på en companion
ger lite; en repeater inom räckhåll ger mycket.

Köp en separat pinnantenn bara när den medföljande är trasig eller saknas.
Alla pinnantenner som säljs för 868 MHz är inte avstämda för det.
[Kontrollera den med en NanoVNA](#nanovna), en antennanalysator i
fickformat, innan du litar på den, eller låna en från ett kort som fungerar.

En nod bredvid en stark sändare hör mindre än den borde. Ett litet
[SAW-filter (surface acoustic wave)](#filters) mellan radion och antennen
håller den sändaren borta från mottagaren. Läs databladet först:

- **Maximal ineffekt.** Filtret sitter också i vägen för din egen
  sändning. Ett kort som sänder 22 dBm (160 mW) in i ett filter märkt
  för 15 dBm förstör filtret.
- **Passband.** Det måste omfatta frekvensen för ditt preset. Ett filter
  för 868.65 till 869.25 MHz släpper inte igenom kanalen EU/UK (Narrow)
  på 869.618 MHz.

## Antenntyper för en repeater {#types}

Varje antenn i meshen står upprätt. Välj typ efter var de noder finns
som du vill nå:

- **Glasfiberkollineär.** Ett vitt rör på en mast, med förstärkning runt
  hela horisonten. Standardvalet för en repeater som täcker en stad.
- **Dipol.** Kortare, med mindre förstärkning och en hög lob. Den når
  noder under och ovanför dig bättre än en kollineär. Det spelar roll på
  en kulle ovanför en dal.
- **Yagi.** En bom med tvärgående element, riktad mot en plats. Den når
  en enda avlägsen repeater och lite annat. Montera den med elementen
  upprätt, eftersom polarisationen följer elementen.

## Förstärkning och loben {#gain}

Förstärkning lägger inte till effekt. Den tar signalen som skulle gå
uppåt och nedåt och skickar den längs horisonten. Som en ficklampa du
fokuserar: samma batteri, en längre och smalare stråle. En dipol och en
kollineär från samma tillverkare visar det:

| Antenn | Förstärkning | Vertikal lobbredd |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 grader |
| Glasfiberkollineär (Sirio SPO 868-915-6) | 5.8 dBi | 23 grader |

{{< gain >}}

Diagrammet skär genom masten, sett från sidan. Vrid det runt masten så
har du hela loben: en munk för dipolen, en platt skiva för den
kollineära. En upprätt antenn sänder likadant åt alla håll runt sig.
Utanför den ritade loben upphör inte signalen; den är svagare, men räcker
ändå för en nod i närheten.

På ett tak är en platt lob det du vill ha. På en kulle högt ovanför
noderna går en lob på 23 grader över huvudet på dem; en dipol täcker dem.
En Yagi driver det längre: 16.6 dBi i en lob som är 23 grader hög och
25 grader bred (Amphenol Procom 7176870), och ingenting åt sidorna.

Förstärkning räknas mot en referens. dBi jämför med en ideal antenn som
sänder lika mycket åt alla håll. dBd jämför med en halvvågsdipol, som
själv har 2.15 dBi: även den enklaste antennen sänder ingenting rakt
uppåt eller nedåt. En längre dipol, 1.25 våglängder, når 5.2 dBi. En
kollineär staplar i stället halvvågselement ovanpå varandra: ju fler den
staplar, desto högre förstärkning. Tryck ihop samma signal i halva
utrymmet så är den dubbelt så stark där: 3 dB. I en fjärdedel, 4 gånger
så stark: 6 dB. Tillverkare anger förstärkning i dBi; den lagliga gränsen
räknar i dBd, se [Inom den lagliga gränsen](#legal).

### Vilken förstärkning för din plats {#choose-gain}

- **Kullar, dalar eller en tät stad: omkring 3 dBi.** Den höga loben når
  noder ovanför och under dig, och runt sluttningarna och byggnaderna i
  vägen. Det gäller också åt andra hållet: från en dal går en platt lob
  under en repeater på kullen ovanför. RAKwireless RAKARG12 är en sådan:
  ett glasfiberrör på 36 cm.
- **Förorter eller en stad med låga tak: 5 till 6 dBi.** Den vanliga
  glasfiberkollineära.
- **Platt, öppet landskap: 8 till 10 dBi.** Den plattaste loben når längst
  längs horisonten. Högt monterad går den över noderna i närheten.

Förstärkningen i namnet är den bästa siffran över antennens hela band.
RAKARG12, som säljs som 3 dBi, har 2.8 dBi vid 865 till 870 MHz. Läs
förstärkningstabellen i databladet vid frekvensen för ditt preset.

Över 7 dBi går ett kort på 22 dBm över den lagliga gränsen, om inte
kabel- och filterförlust täcker skillnaden. Sänk sändeffekten så att det
stämmer.

Hög förstärkning hjälper bara när du vet var noderna finns: längs
horisonten runt en repeater, eller vid en enda avlägsen repeater för en
Yagi. En companion i din hand pekar åt alla håll, så den låga
förstärkningen den kom med passar den bäst.

## Varför vertikalt {#vertical}

Antenner hör varandra bäst när de pekar åt samma håll. Förlusten växer
med vinkeln mellan dem: 45 grader kostar 3 dB, halva din signal. Vid
90 grader, en liggande antenn mot en upprätt, kommer i teorin ingenting
fram. Meshen står upprätt, så det gör din antenn också. Det gäller även
en companion på ett skrivbord: lägg den platt så hör varje nod runt dig
mindre.

## Kontakter {#connectors}

Beställ antennen med den kontakt ditt kort har. Varje adapter är en skarv
till att täta och mer signal som går förlorad.

- **SMA.** En gängad kontakt omkring 6 mm bred. Uttaget på de flesta kort
  har ett hål i mitten; antennen har stiftet. En kontakt av det här
  slaget förlorar omkring 0.03 dB vid 868 MHz.
- **RP-SMA.** Samma kropp och gänga som SMA, med stiftet och hålet
  omkastade. Den ser ut som SMA och passar inte ihop med den. Kontrollera
  vilken ditt kort har innan du beställer.
- **U.FL (IPEX).** Ett pyttelitet uttag att trycka fast på själva kortet.
  En kort pigtail-kabel går från det till ett SMA-uttag i lådan. Det är
  märkt för 30 anslutningar, så anslut det en gång och låt det sitta.
- **N.** Den stora gängade kontakten på glasfiberantenner och tjock kabel.
  Den förlorar högst 0.05 dB. En repeater behöver en adapter eller pigtail
  från N till kortets SMA.

## Kabelförlust {#cable}

Kabel kostar signal innan den lämnar antennen, i båda riktningarna. 3 dB
är halva din effekt. Tillverkarnas siffror per meter, vid 868 till 900 MHz:

| Kabel | Förlust per meter | Förlust över 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 meter RG174, den tunna pigtail som följer med många kort, förlorar halva
din effekt. Montera kortet vid antennen med en kort pigtail, eller dra
tjock kabel dit. Lägg till varje adapter och filter i vägen till summan.

## Filter {#filters}

Ett filter sitter mellan radion och antennen. Det släpper igenom ditt band
och spärrar resten, så att en stark sändare i närheten inte dränker
mottagaren. Du behöver ett när en nod hör mindre än den borde nära andra
sändare. En repeater på en mast med basstationer för mobiltelefoni är en
sådan nod. Ett filter kostar signal i båda riktningarna: räkna dess
förlust som kabel.

| | SAW-filter | Kavitetsfilter |
|---|---|---|
| Storlek | Några millimeter, på ett litet kort | Ett metallblock eller rör |
| Förlust hos ett bra | under 2 dB | under 1 dB |
| Maximal ineffekt hos ett bra | 500 mW | flera watt |

sysmocom cf866.5-kt30 är till exempel ett kavitetsfilter för 863 till
870 MHz som förlorar högst 1.0 dB och tål 30 W. Det är gjort för inomhus,
så sätt det i en tät låda på en mast.

Filter skiljer sig mycket åt, så läs databladet innan du köper. Dess
märkta ineffekt måste överstiga din sändeffekt, och dess passband måste
omfatta frekvensen för ditt preset.

## Montering {#mounting}

- **Ovanför takkanten.** Antennen behöver fri sikt i varje riktning den
  täcker. Även några meter ovanför taken runt omkring hjälper.
  [Välj en plats](/repeater-guide/#site) i repeaterguiden visar hur du
  kontrollerar sikten.
- **Bort från metall.** Hängrännor, master, andra antenner och plåttak
  intill antennen ändrar dess diagram och avstämning. Montera den högst
  upp på masten, inte bredvid den.
- **Upprätt.** Använd ett vattenpass; se [Varför vertikalt](#vertical).
- **Droppslinga.** Låt kabeln hänga nedanför kontakten innan den går upp
  eller in. Då droppar vattnet av i stället för att rinna in i skarven.
- **Täta varje utomhuskontakt.** Vatten i en kontakt ökar förlusten och
  korroderar stiftet. Täta den mot regn och kontrollera tätningen varje år.
- **Åska.** En antenn på ett tak är ett mål. Ett gasurladdningsskydd i
  kabeln löser ut vid en spänningstopp och leder den till jord. Följ
  [Hårdvara](/repeater-guide/#hardware) i repeaterguiden och dina lokala
  regler för jordning.

## Inom den lagliga gränsen {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
I Europa använder MeshCore delbandet 869.40-869.65 MHz, med högst
**500 mW** effektivt utstrålad effekt (e.r.p.). Gränsen räknar det som
lämnar antennen: antennförstärkning läggs till, kabel- och filterförlust
dras av. Förstärkning i dBi räknas 2.15 dB lägre, eftersom gränsen mäts
mot en dipol.
{{< /callout >}}

En kollineär på 5.8 dBi på ett kort med 22 dBm håller sig inom gränsen.
Samma antenn på ett kort med förstärkare gör det inte, förrän du sänker
sändeffekten. [Effekt: e.r.p. och din antenn](/repeater-guide/#erp) i
repeaterguiden har uträkningen och 2 genomräknade exempel.

## Kontrollera en antenn med en NanoVNA {#nanovna}

En NanoVNA är en vektornätverksanalysator i fickformat. Den visar vid
vilken frekvens en antenn är avstämd, så du vet det innan du monterar den.
NanoVNA-H mäter upp till 1.5 GHz, vilket täcker 868 MHz.

1. Kalibrera den för 800 till 950 MHz med delarna open, short och load
   från dess sats.
2. Anslut antennen genom den adapter den ska använda på noden. Håll den
   upprätt och bort från din kropp och bordet.
3. Läs SWR-kurvan (ståendevågförhållande): den visar hur mycket signal
   antennen skickar tillbaka. Dippen måste ligga på frekvensen för ditt
   preset, 869.618 MHz för EU/UK (Narrow). En dipp hundratals MHz bort
   betyder att antennen är gjord för ett annat band.

En kvartsvåg vid 868 MHz är 86 mm (våglängden är 345 mm). Längden ensam
säger dig inte bandet, eftersom tillverkare viker och belastar pinnantenner;
det gör NanoVNA.

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
- Förstärkning som signal hoptryckt i mindre utrymme: [RF Cafe, antenna introduction](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Kontakter: databladen för Rosenberger 32S102 (SMA) och 53S101 (N),
  Hirose U.FL-katalogen.
- Filter: produktsidan för sysmocom cf866.5-kt30,
  [Citel gasurladdningsskydd](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarisationsförlust: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipolförstärkning efter längd: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Våglängd: ljusets hastighet från [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Laglig gräns: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Annex 1, band h1.7; [repeaterguiden](/repeater-guide/#legal) listar
  resten.
