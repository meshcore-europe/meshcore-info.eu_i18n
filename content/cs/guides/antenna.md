---
title: Průvodce anténami
lead: Správná anténa, dobře namontovaná, dosáhne dál než vyšší výkon. Zkontroluj anténu na svém companionu, pak vyber, připoj a namontuj anténu pro repeater.
description: 'Vyber a namontuj anténu pro MeshCore na 868 MHz: kontrola prutové antény companionu, typy antén a zisk, konektory, útlum kabelu na metr, filtry, montáž a jak se zisk započítává do zákonného limitu.'
eyebrow: Companion a repeater · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-10-31'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Výška, naladěná anténa a krátký kabel přinesou větší dosah než jakýkoli miliwatt navíc.
Tento průvodce začíná u companionu, rádia, ze kterého posíláš zprávy.
Pak se věnuje anténě na repeateru. To je uzel, který předává zprávy dál
ze střechy nebo stožáru.

## Tvůj companion {#companion}

{{< callout type="warning" >}}
Než rádio zapneš, připoj anténu. LoRa rádio, které vysílá bez antény,
si může poškodit vlastní čip.
{{< /callout >}}

Anténa dodaná s deskou svou práci odvede. Připoj ji, drž uzel
svisle a začni posílat zprávy. Lepší anténa na companionu přinese málo,
repeater v dosahu přinese hodně.

Samostatný prut kupuj, jen když je ten dodaný rozbitý nebo chybí. Ne
každý prut prodávaný pro 868 MHz je na tuto frekvenci naladěný. Než se na
něj spolehneš, [změř ho NanoVNA](#nanovna), kapesním analyzátorem antén,
nebo si půjč prut z desky, která funguje.

Uzel vedle silného vysílače slyší méně, než by měl. Malý
[SAW filtr (filtr s povrchovou akustickou vlnou)](#filters) mezi rádiem
a anténou nepustí signál toho vysílače do přijímače. Nejdřív zkontroluj jeho
datasheet:

- **Maximální vstupní výkon.** Filtr stojí i v cestě tvého vlastního
  vysílání. Deska, která vysílá 22 dBm (160 mW) do filtru dimenzovaného
  na 15 dBm, filtr zničí.
- **Propustné pásmo.** Musí zahrnovat frekvenci tvého presetu. Filtr pro
  868.65 až 869.25 MHz nepropustí kanál EU/UK (Narrow) na 869.618 MHz.

## Typy antén pro repeater {#types}

Všechny antény v mesh síti stojí svisle. Typ vyber podle toho, kde jsou uzly,
na které chceš dosáhnout:

- **Sklolaminátová kolineární anténa.** Bílá trubka na stožáru se ziskem
  dokola po celém horizontu. Standardní volba pro repeater, který pokrývá město.
- **Dipól.** Je kratší, má menší zisk a vysoký svazek. Na uzly pod tebou
  a nad tebou dosáhne lépe než kolineární anténa, třeba z kopce nad údolím.
- **Yagi.** Ráhno s příčnými prvky, namířené na jedno místo. Dosáhne na
  jeden vzdálený repeater a skoro na nic jiného. Namontuj ji s prvky svisle,
  protože její polarizace se řídí prvky.

## Zisk a svazek {#gain}

Zisk nepřidává výkon. Bere signál, který by šel nahoru a dolů,
a posílá ho podél horizontu. Je to jako baterka, kterou zaostříš: stejná
baterie, delší a užší paprsek. Ukazují to dipól a kolineární anténa od
stejného výrobce:

| Anténa | Zisk | Vertikální šířka svazku |
|---|---|---|
| Dipól (Sirio SO 868-915-2) | 2.2 dBi | 88 stupňů |
| Sklolaminátová kolineární anténa (Sirio SPO 868-915-6) | 5.8 dBi | 23 stupňů |

{{< gain >}}

Diagram je řez stožárem při pohledu ze strany. Otoč ho kolem stožáru
a máš celý svazek: u dipólu koblihu, u kolineární antény plochý disk.
Svislá anténa vysílá stejně do všech směrů kolem sebe. Mimo nakreslený
svazek signál nekončí. Je slabší, ale na blízký uzel pořád stačí.

Na střeše chceš plochý svazek. Na kopci vysoko nad uzly jim svazek
o 23 stupních přejde nad hlavami. Dipól je pokryje. Yagi jde ještě dál:
16.6 dBi ve svazku 23 stupňů vysokém
a 25 stupňů širokém (Amphenol Procom
7176870), a do stran nic.

Zisk se udává vůči referenci. dBi porovnává s ideální anténou, která
vysílá stejně do všech směrů. dBd porovnává s půlvlnným dipólem, který
sám má 2.15 dBi: ani ta nejjednodušší anténa nevysílá nic přímo nahoru
nebo dolů. Delší dipól, 1.25 vlnové délky, dosáhne 5.2 dBi. Kolineární
anténa místo toho skládá půlvlnné prvky nad sebe. Čím víc jich složí,
tím vyšší je zisk. Stlač stejný signál do poloviny prostoru a je tam
dvakrát silnější: 3 dB. Do čtvrtiny a je 4krát silnější: 6 dB.
Výrobci uvádějí zisk v dBi. Zákonný limit počítá v dBd, viz
[V rámci zákonného limitu](#legal).

### Jaký zisk pro tvé místo {#choose-gain}

- **Kopce, údolí nebo hustě zastavěné město: kolem 3 dBi.** Vysoký svazek
  dosáhne na uzly nad tebou i pod tebou a obejde svahy a budovy v cestě.
  Funguje to i opačně: z údolí projde plochý svazek pod repeaterem na
  kopci nad tebou. Příkladem je RAKwireless RAKARG12: sklolaminátová trubka
  dlouhá 36 cm.
- **Předměstí nebo město s nízkými střechami: 5 až 6 dBi.** Standardní
  sklolaminátová kolineární anténa.
- **Rovná, otevřená krajina: 8 až 10 dBi.** Nejplošší svazek dosáhne
  nejdál podél horizontu. Když je anténa vysoko, přejde svazek nad blízkými
  uzly.

Zisk v názvu je nejlepší hodnota v celém pásmu antény. RAKARG12,
prodávaná jako 3 dBi, má na 865 až 870 MHz 2.8 dBi. V datasheetu si
přečti tabulku zisku na frekvenci tvého presetu.

Nad 7 dBi překročí deska s 22 dBm zákonný limit, pokud rozdíl nevyrovnají
ztráty v kabelu a filtru. Podle toho sniž vysílací výkon.

Vysoký zisk pomůže, jen když víš, kde uzly jsou: podél horizontu kolem
repeateru, nebo u Yagi na jednom vzdáleném repeateru. Companion v ruce
míří všemi směry, a tak se mu nejlépe hodí nízký zisk antény, kterou
má z výroby.

## Proč svisle {#vertical}

Antény se slyší nejlépe, když míří stejným směrem. Ztráta roste s úhlem
mezi nimi: 45 stupňů stojí 3 dB, polovinu tvého signálu. Při 90 stupních,
tedy vodorovná anténa proti svislé, teoreticky nedorazí nic. Mesh síť stojí
svisle, takže i tvoje anténa. Platí to i pro companion na stole: když ho
položíš naplocho, všechny uzly kolem tebe slyší hůř.

## Konektory {#connectors}

Anténu objednej s konektorem,
který má tvoje deska. Každý adaptér je další spoj, který musíš utěsnit,
a další ztracený signál.

- **SMA.** Konektor se závitem, široký asi 6 mm. Zásuvka na většině desek
  má uprostřed otvor, anténa má kolík. Konektor tohoto druhu ztrácí asi
  0.03 dB na 868 MHz.
- **RP-SMA.** Stejné tělo a závit jako SMA, kolík a otvor jsou prohozené.
  Vypadá jako SMA, ale nedá se s ním spojit. Než objednáš, zkontroluj, který
  z nich tvoje deska má.
- **U.FL (IPEX).** Drobná nasouvací zásuvka přímo na desce. Krátký kabel
  (pigtail) z ní vede k zásuvce SMA v krabičce. Je dimenzovaná na 30
  připojení, takže ji připoj jednou a nech ji být.
- **N.** Velký konektor se závitem na sklolaminátových anténách a silném
  kabelu. Ztrácí nejvýš 0.05 dB. Repeater potřebuje jeden
  adaptér nebo pigtail z N na SMA desky.

## Ztráty v kabelu {#cable}

Kabel ubírá signál dřív, než opustí anténu, a to v obou směrech. 3 dB
je polovina tvého výkonu. Údaje výrobců na metr, na 868 až 900 MHz:

| Kabel | Ztráta na metr | Ztráta na 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metry RG174, tenkého pigtailu dodávaného s mnoha deskami, ztratí polovinu
tvého výkonu. Namontuj desku k anténě s krátkým pigtailem, nebo k ní
veď silný kabel. Do součtu přidej každý adaptér a filtr v cestě.

## Filtry {#filters}

Filtr je mezi rádiem a anténou. Propustí tvé pásmo a zbytek zablokuje.
Silný vysílač poblíž tak nezahltí přijímač. Potřebuješ ho, když uzel
poblíž jiných vysílačů slyší méně, než by měl. Takový uzel je třeba
repeater na stožáru se základnovými stanicemi mobilních sítí. Filtr ubírá
signál v obou směrech: jeho ztrátu počítej jako u kabelu.

| | SAW filtr | Dutinový filtr |
|---|---|---|
| Velikost | Pár milimetrů, na malé desce | Kovový blok nebo trubka |
| Ztráta dobrého filtru | pod 2 dB | pod 1 dB |
| Maximální vstupní výkon dobrého filtru | 500 mW | několik wattů |

Třeba sysmocom cf866.5-kt30 je dutinový filtr pro 863 až 870 MHz.
Ztrácí nejvýš 1.0 dB a snese 30 W. Je určený do vnitřních prostor, takže
ho na stožáru dej do utěsněné krabičky.

Filtry se hodně liší, proto si před nákupem zkontroluj datasheet. Jeho
jmenovitý vstupní výkon musí být vyšší než tvůj vysílací výkon. Jeho
propustné pásmo musí zahrnovat frekvenci tvého presetu.

## Montáž {#mounting}

- **Nad okrajem střechy.** Anténa potřebuje volný výhled do všech směrů,
  které pokrývá. Pomůže i pár metrů nad okolními střechami. Jak výhled
  ověřit, popisuje [Výběr místa](/repeater-guide/#site) v průvodci repeaterem.
- **Dál od kovu.** Okapy, stožáry, jiné antény a plechové střechy vedle
  antény mění její vyzařovací diagram a naladění. Namontuj ji na vrchol
  stožáru, ne vedle něj.
- **Svisle.** Použij vodováhu, viz [Proč svisle](#vertical).
- **Odkapová smyčka.** Nech kabel pod konektorem prověsit, než povede
  nahoru nebo dovnitř. Voda pak odkape a nesteče do spoje.
- **Utěsni každý venkovní konektor.** Voda v konektoru zvyšuje útlum
  a kolík koroduje. Utěsni ho proti dešti a těsnění každý rok
  zkontroluj.
- **Blesk.** Anténa na střeše je terč. Plynová bleskojistka v kabelu při
  přepětí sepne a svede ho do země. Při uzemnění se řiď částí
  [Hardware](/repeater-guide/#hardware) v průvodci repeaterem a místními
  předpisy.

## V rámci zákonného limitu {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
V Evropě používá MeshCore podpásmo 869.40-869.65 MHz s nejvýš
**500 mW** efektivního vyzářeného výkonu (e.r.p.). Limit počítá to, co opustí anténu:
zisk antény se přičítá, ztráty v kabelu a filtru se odečítají. Zisk v dBi se počítá
o 2.15 dB méně, protože limit se měří vůči dipólu.
{{< /callout >}}

Sklolaminátová kolineární anténa s 5.8 dBi na desce s 22 dBm zůstane v limitu. Stejná
anténa na desce se zesilovačem v limitu nezůstane, dokud nesnížíš vysílací
výkon. Část [Výkon: e.r.p. a tvoje anténa](/repeater-guide/#erp) v průvodci
repeaterem ukazuje výpočet a 2 řešené příklady.

## Kontrola antény s NanoVNA {#nanovna}

NanoVNA je vektorový analyzátor obvodů do kapsy. Ukáže, na jakou
frekvenci je anténa naladěná, takže to víš dřív, než ji namontuješ.
NanoVNA-H měří až do 1.5 GHz, což pokrývá 868 MHz.

1. Zkalibruj ho pro 800 až 950 MHz pomocí dílů open, short a load
   z jeho sady.
2. Připoj anténu přes adaptér, který bude používat na uzlu. Drž ji
   svisle a dál od těla a od stolu.
3. Přečti křivku SWR (poměr stojatých vln): ukazuje, kolik signálu
   anténa vrací zpět. Minimum musí ležet na frekvenci tvého presetu,
   pro EU/UK (Narrow) na 869.618 MHz. Minimum o stovky MHz jinde
   znamená, že anténa je vyrobená pro jiné pásmo.

Čtvrtvlna na 868 MHz měří 86 mm (vlnová délka je 345 mm). Samotná délka
ti pásmo neprozradí, protože výrobci pruty skládají a prodlužují cívkou.
NanoVNA ti ho prozradí.

## Zdroje {#sources}

- Útlum kabelu: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  datasheet Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  datasheety Times Microwave LMR-240 a LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antény: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  datasheet Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Zisk jako signál stlačený do menšího prostoru: [RF Cafe, úvod do antén](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Konektory: datasheety Rosenberger 32S102 (SMA) a 53S101 (N), katalog
  Hirose U.FL.
- Filtry: produktová stránka sysmocom cf866.5-kt30,
  [plynové bleskojistky Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarizační ztráta: [University of Toronto, Friisovy jevy](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Zisk dipólu podle délky: [Wikipedie, Dipólová anténa](https://en.wikipedia.org/wiki/Dipole_antenna).
- Vlnová délka: rychlost světla podle [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Zákonný limit: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  příloha 1, pásmo h1.7. Zbytek uvádí [průvodce repeaterem](/repeater-guide/#legal).
