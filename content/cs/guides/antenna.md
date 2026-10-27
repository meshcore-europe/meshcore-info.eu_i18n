---
title: Průvodce anténami
lead: Anténa je polovina tvého uzlu. Správná anténa, dobře namontovaná, dosáhne dál než větší výkon. Zkontroluj anténu na svém companionu, pak vyber, připoj a namontuj anténu pro repeater.
description: 'Vyber a namontuj anténu pro MeshCore na 868 MHz: kontrola prutové antény companionu, typy antén a zisk, konektory, útlum kabelu na metr, filtry, montáž a jak se zisk počítá do zákonného limitu.'
eyebrow: Companion a repeater · 868 MHz
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '45010ad0'
  seeded: '2026-10-26'
  fields: {title: '3a76cb0e', lead: '98430ade', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', '94c5bae4', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
---

Výška, naladěná anténa a krátký kabel přinesou větší dosah než jakýkoli
miliwatt navíc. Tento průvodce začíná u companionu, rádia, ze kterého
píšeš zprávy. Pak se věnuje anténě na repeateru, uzlu, který předává
zprávy dál ze střechy nebo stožáru.

## Tvůj companion {#companion}

{{< callout type="warning" >}}
Připoj anténu dřív, než rádio zapneš. LoRa rádio, které vysílá bez
antény, si může poškodit vlastní čip.
{{< /callout >}}

Anténa dodaná s tvou deskou svou práci zvládne. Připoj ji, drž uzel
svisle a začni psát zprávy. Lepší anténa na companionu přinese málo;
repeater v dosahu přinese hodně.

Samostatný prut kupuj jen tehdy, když je dodaný rozbitý nebo chybí. Ne
každý prut prodávaný pro 868 MHz je na toto pásmo naladěný. [Ověř ho
pomocí NanoVNA](#nanovna), kapesního analyzátoru antén, než mu budeš
věřit, nebo si půjč prut z desky, která funguje.

Uzel vedle silného vysílače slyší méně, než by měl. Malý
[SAW filtr (surface acoustic wave)](#filters) mezi rádiem a anténou
udrží ten vysílač mimo přijímač. Nejdřív zkontroluj jeho datasheet:

- **Maximální vstupní výkon.** Filtr stojí také v cestě tvého vlastního
  vysílání. Deska vysílající 22 dBm (160 mW) do filtru dimenzovaného na 15 dBm
  filtr zničí.
- **Propustné pásmo.** Musí zahrnovat frekvenci tvého presetu. Filtr pro
  868.65 až 869.25 MHz nepropustí kanál EU/UK (Narrow) na
  869.618 MHz.

## Typy antén pro repeater {#types}

Každá anténa v meshi stojí svisle. Typ vyber podle toho, kde jsou uzly,
na které chceš dosáhnout:

- **Skleněný kolineár.** Bílá trubka na stožáru se ziskem do všech stran
  po horizontu. Standardní volba pro repeater, který obsluhuje město.
- **Dipól.** Kratší, s menším ziskem a vysokým vyzařovacím svazkem. Uzly
  pod tebou a nad tebou pokryje lépe než kolineár. Na to dojde na kopci
  nad údolím.
- **Yagi.** Nosník s příčnými prvky, namířený na jedno místo. Dosáhne na
  jeden vzdálený repeater a skoro na nic jiného. Montuj ji s prvky svisle,
  protože její polarizace sleduje prvky.

## Zisk a vyzařovací svazek {#gain}

Zisk nepřidává výkon. Vezme signál, který by šel nahoru a dolů, a pošle
ho podél horizontu. Jako baterka, kterou zaostříš: stejná baterie, delší
a užší paprsek. Dipól a kolineár od stejného výrobce to ukazují:

| Anténa | Zisk | Vertikální šířka svazku |
|---|---|---|
| Dipól (Sirio SO 868-915-2) | 2.2 dBi | 88 stupňů |
| Skleněný kolineár (Sirio SPO 868-915-6) | 5.8 dBi | 23 stupňů |

{{< gain >}}

Diagram je řez stožárem, viděný ze strany. Otoč ho kolem stožáru a máš
celý svazek: u dipólu prstenec, u kolineáru plochý disk. Svislá anténa
vysílá stejně do všech směrů kolem sebe. Mimo nakreslený svazek signál
nekončí; je slabší, pořád stačí pro uzel nablízku.

Na střeše chceš plochý svazek. Na kopci vysoko nad uzly jde svazek o
23 stupních přes jejich hlavy; dipól je pokryje. Yagi jde ještě dál:
16.6 dBi ve svazku 23 stupňů vysokém a 25 stupňů širokém (Amphenol Procom
7176870), a do stran nic.

Zisk se počítá vůči referenci. dBi porovnává s ideální anténou, která
vysílá stejně do všech směrů. dBd porovnává s půlvlnným dipólem, který
sám má 2.15 dBi: ani nejjednodušší anténa nevysílá přímo nahoru ani dolů.
Delší dipól, 1.25 vlnové délky, dosáhne 5.2 dBi. Kolineár místo toho
skládá půlvlnné prvky nad sebe: čím víc jich skládá, tím vyšší zisk.
Stlač stejný signál do poloviny prostoru a bude tam dvakrát silnější:
3 dB. Do čtvrtiny, 4krát silnější: 6 dB. Výrobci uvádějí zisk v dBi;
zákonný limit počítá v dBd, viz [V rámci zákonného limitu](#legal).

### Jaký zisk pro tvoje stanoviště {#choose-gain}

- **Kopce, údolí nebo hustá zástavba: kolem 3 dBi.** Vysoký svazek dosáhne
  na uzly nad tebou a pod tebou a kolem svahů a budov, které stojí v cestě.
  Funguje to i obráceně: z údolí projde plochý svazek pod repeaterem na
  kopci nad tebou. Jednou takovou je RAKwireless RAKARG12: skleněná
  trubka o délce 36 cm.
- **Předměstí nebo město s nízkými střechami: 5 až 6 dBi.** Standardní
  skleněný kolineár.
- **Rovná, otevřená krajina: 8 až 10 dBi.** Nejplošší svazek dosáhne
  nejdál podél horizontu. Namontovaný vysoko jde přes uzly nablízku.

Zisk v názvu je nejlepší hodnota z celého pásma antény. RAKARG12,
prodávaná jako 3 dBi, má 2.8 dBi na 865 až 870 MHz. Přečti si tabulku
zisku v datasheetu na frekvenci tvého presetu.

Nad 7 dBi jde deska s 22 dBm přes zákonný limit, pokud rozdíl nevyrovná
útlum kabelu a filtru. Sniž vysílací výkon, aby to odpovídalo.

Vysoký zisk pomáhá jen tehdy, když víš, kde uzly jsou: podél horizontu
kolem repeateru, nebo u jednoho vzdáleného repeateru pro Yagi. Companion
v tvé ruce míří na všechny strany, takže mu nejlépe sedí nízký zisk, se
kterým přišel.

## Proč svisle {#vertical}

Antény se slyší nejlépe, když míří stejným směrem. Ztráta roste s úhlem
mezi nimi: 45 stupňů stojí 3 dB, polovinu tvého signálu. Při 90 stupních,
tedy ležící anténa proti svislé, teoreticky nedorazí nic. Mesh stojí
svisle, takže i tvoje anténa. Platí to i pro companion na stole: polož ho
naplocho a každý uzel kolem tebe slyší méně.

## Konektory {#connectors}

Objednej anténu s konektorem, který má tvoje deska. Každá redukce je další
spoj k utěsnění a další ztráta signálu.

- **SMA.** Závitový konektor široký asi 6 mm. Zásuvka na většině desek má
  uprostřed otvor; anténa má kolík. Konektor tohoto druhu ztrácí asi
  0.03 dB na 868 MHz.
- **RP-SMA.** Stejné tělo a závit jako SMA, s prohozeným kolíkem a
  otvorem. Vypadá jako SMA a nejde s ním spojit. Než objednáš, zkontroluj,
  který z nich tvoje deska má.
- **U.FL (IPEX).** Drobná nasouvací zásuvka přímo na desce. Krátký pigtail
  kabel z ní vede k zásuvce SMA v krabičce. Je dimenzovaná na 30 cyklů
  spojení, takže ji připoj jednou a nech být.
- **N.** Velký závitový konektor na skleněných anténách a tlustém kabelu.
  Ztrácí nejvýš 0.05 dB. Repeater potřebuje jednu redukci nebo pigtail
  z N na SMA desky.

## Útlum kabelu {#cable}

Kabel stojí signál dřív, než opustí anténu, a to v obou směrech. 3 dB
je polovina tvého výkonu. Údaje výrobců na metr, na 868 až 900 MHz:

| Kabel | Útlum na metr | Útlum na 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metry RG174, tenkého pigtailu dodávaného s mnoha deskami, ztratí
polovinu tvého výkonu. Namontuj desku k anténě s krátkým pigtailem, nebo
k ní veď tlustý kabel. K součtu přičti každou redukci a filtr v cestě.

## Filtry {#filters}

Filtr sedí mezi rádiem a anténou. Propustí tvoje pásmo a zbytek
blokuje, takže silný vysílač nablízku nezahltí přijímač. Potřebuješ ho,
když uzel slyší méně, než by měl, poblíž jiných vysílačů. Repeater na
stožáru se základnovými stanicemi mobilních operátorů je takový uzel.
Filtr stojí signál v obou směrech: jeho útlum počítej jako kabel.

| | SAW filtr | Dutinový filtr |
|---|---|---|
| Velikost | Několik milimetrů, na malé desce | Kovový blok nebo trubka |
| Útlum dobrého kusu | pod 2 dB | pod 1 dB |
| Maximální vstupní výkon dobrého kusu | 500 mW | několik wattů |

Například sysmocom cf866.5-kt30 je dutinový filtr pro 863 až 870 MHz,
který ztrácí nejvýš 1.0 dB a snese 30 W. Je vyrobený pro interiér, takže
ho na stožáru dej do utěsněné krabičky.

Filtry se hodně liší, takže si před nákupem přečti datasheet. Jeho
jmenovitý vstupní výkon musí převyšovat tvůj vysílací výkon a jeho
propustné pásmo musí zahrnovat frekvenci tvého presetu.

## Montáž {#mounting}

- **Nad hranu střechy.** Anténa potřebuje volný výhled do každého směru,
  který obsluhuje. Pomůže i několik metrů nad okolními střechami.
  Jak výhled ověřit, ukazuje [Výběr stanoviště](/repeater-guide/#site) v
  průvodci repeaterem.
- **Dál od kovu.** Okapy, stožáry, jiné antény a plechové střechy vedle
  antény mění její vyzařovací charakteristiku i ladění. Montuj ji na vršek
  stožáru, ne vedle něj.
- **Svisle.** Použij vodováhu; viz [Proč svisle](#vertical).
- **Odkapávací smyčka.** Nech kabel pod konektorem prověsit, než půjde
  nahoru nebo dovnitř. Voda pak odkape, místo aby stékala do spoje.
- **Utěsni každý venkovní konektor.** Voda v konektoru zvyšuje útlum a
  koroduje kolík. Utěsni ho proti dešti a těsnění každý rok zkontroluj.
- **Blesk.** Anténa na střeše je terč. Plynová bleskojistka v kabelu při
  přepětí sepne a svede ho do země. Řiď se částí
  [Hardware](/repeater-guide/#hardware) v průvodci repeaterem a místními
  pravidly pro uzemnění.

## V rámci zákonného limitu {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
V Evropě používá MeshCore dílčí pásmo 869.40-869.65 MHz s nejvýše
**500 mW** efektivního vyzářeného výkonu (e.r.p.). Limit počítá to, co opouští anténu:
zisk antény se přičítá, útlum kabelu a filtru se odečítá. Zisk v dBi se
počítá o 2.15 dB méně, protože limit se měří vůči dipólu.
{{< /callout >}}

Kolineár s 5.8 dBi na desce s 22 dBm zůstává v limitu. Stejná anténa na
desce se zesilovačem ne, dokud nesnížíš vysílací výkon. Část
[Výkon: e.r.p. a tvoje anténa](/repeater-guide/#erp) v průvodci
repeaterem obsahuje součet a 2 řešené příklady.

## Ověř anténu pomocí NanoVNA {#nanovna}

NanoVNA je kapesní vektorový analyzátor. Ukáže, na jakou frekvenci je
anténa naladěná, takže to víš dřív, než ji namontuješ. NanoVNA-H měří
do 1.5 GHz, což 868 MHz pokrývá.

1. Zkalibruj ho pro 800 až 950 MHz pomocí dílů open, short a load z jeho
   sady.
2. Připoj anténu přes redukci, kterou bude používat na uzlu. Drž ji
   svisle a dál od těla i stolu.
3. Přečti křivku SWR (poměr stojatých vln): ukazuje, kolik signálu anténa
   posílá zpět. Propad musí ležet na frekvenci tvého presetu, 869.618
   MHz pro EU/UK (Narrow). Propad stovky MHz vedle znamená, že anténa je
   vyrobená pro jiné pásmo.

Čtvrt vlny na 868 MHz je 86 mm (vlnová délka je 345 mm). Samotná délka
ti pásmo neprozradí, protože výrobci pruty skládají a zatěžují; NanoVNA
ano.

## Zdroje {#sources}

- Útlum kabelu: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  katalogový list Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  katalogové listy Times Microwave LMR-240 a LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antény: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  katalogový list Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Zisk jako signál stlačený do menšího prostoru: [RF Cafe, úvod do antén](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Konektory: katalogové listy Rosenberger 32S102 (SMA) a 53S101 (N),
  katalog Hirose U.FL.
- Filtry: produktová stránka sysmocom cf866.5-kt30,
  [plynové bleskojistky Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarizační ztráta: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Zisk dipólu podle délky: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Vlnová délka: rychlost světla podle [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Zákonný limit: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  příloha 1, pásmo h1.7; zbytek uvádí [průvodce repeaterem](/repeater-guide/#legal).
