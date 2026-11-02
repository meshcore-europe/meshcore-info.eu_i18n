---
title: Sprievodca anténami
lead: Správna a dobre namontovaná anténa dosiahne ďalej než vyšší výkon. Skontroluj anténu na svojom companione, potom pre repeater jednu vyber, pripoj a namontuj.
description: 'Vyber a namontuj anténu pre MeshCore na 868 MHz: kontrola prútovej antény companiona, typy antén a zisk, konektory, útlm kábla na meter, filtre, montáž a započítanie zisku do zákonného limitu.'
eyebrow: Companion a repeater · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-11-02'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Výška, naladená anténa a krátky kábel ti pridajú viac dosahu než akýkoľvek
miliwatt navyše. Tento sprievodca začína companionom, teda rádiom, z ktorého
posielaš správy. Potom prejde na anténu repeatera, teda uzla, ktorý zo strechy
alebo stožiara posúva správy ďalej.

## Tvoj companion {#companion}

{{< callout type="warning" >}}
Anténu pripoj skôr, než rádio zapneš. Rádio LoRa, ktoré vysiela bez antény,
si môže poškodiť vlastný čip.
{{< /callout >}}

Anténa dodaná s doskou stačí. Pripoj ju, drž uzol zvislo a začni
posielať správy. Lepšia anténa na companione prinesie málo, repeater v dosahu
prinesie veľa.

Samostatnú prútovú anténu kúp len vtedy, keď je dodaná anténa pokazená alebo
chýba. Nie každá prútová anténa predávaná na 868 MHz je na túto frekvenciu
naladená. Skôr než jej uveríš, [skontroluj ju pomocou NanoVNA](#nanovna), teda
vreckového analyzátora antén, alebo si požič anténu z funkčnej dosky.

Uzol vedľa silného vysielača počuje menej, než by mal. Malý
[filter SAW (s povrchovou akustickou vlnou)](#filters) medzi rádiom a anténou
tento vysielač k prijímaču nepustí. Najprv si pozri jeho katalógový list:

- **Maximálny vstupný výkon.** Cez filter prechádza aj tvoje vlastné
  vysielanie. Doska, ktorá vysiela 22 dBm (160 mW) do filtra dimenzovaného na
  15 dBm, filter zničí.
- **Priepustné pásmo.** Musí zahŕňať frekvenciu tvojej predvoľby. Filter na
  868.65 až 869.25 MHz neprepustí kanál EU/UK (Narrow) na 869.618 MHz.

## Typy antén pre repeater {#types}

Každá anténa v sieti mesh stojí zvislo. Typ vyber podľa toho, kde sú uzly,
na ktoré chceš dosiahnuť:

- **Sklolaminátová kolineárna anténa.** Biela trubica na stožiari so ziskom
  dookola po celom obzore. Je to štandardná voľba pre repeater, ktorý pokrýva mesto.
- **Dipól.** Je kratší, má menší zisk a vysoký lúč. Na uzly pod tebou a nad
  tebou dosiahne lepšie než kolineárna anténa, napríklad z kopca nad údolím.
- **Yagi.** Ráhno s priečnymi prvkami, namierené na jedno miesto. Dosiahne na
  jeden vzdialený repeater a na máločo iné. Namontuj ju tak, aby prvky stáli
  zvislo, lebo polarizácia sa riadi ich smerom.

## Zisk a lúč {#gain}

Zisk výkon nepridáva. Signál, ktorý by išiel hore a dole, nasmeruje pozdĺž
obzoru. Je to ako baterka, ktorú zaostríš: rovnaká batéria, dlhší a užší lúč.
Ukazujú to dipól a kolineárna anténa od toho istého výrobcu:

| Anténa | Zisk | Vertikálna šírka lúča |
|---|---|---|
| Dipól (Sirio SO 868-915-2) | 2.2 dBi | 88 stupňov |
| Sklolaminátová kolineárna anténa (Sirio SPO 868-915-6) | 5.8 dBi | 23 stupňov |

{{< gain >}}

Diagram je rez stožiarom pri pohľade zboku. Otoč ho okolo stožiara a máš
celý lúč: šišku pri dipóle, plochý disk pri kolineárnej anténe. Zvislá anténa
vysiela rovnako do všetkých smerov okolo seba. Mimo nakresleného lúča signál
nezmizne: je slabší, ale na blízky uzol ešte stačí.

Na streche chceš plochý lúč. Na kopci vysoko nad uzlami prejde 23-stupňový lúč
ponad ich hlavy, dipól ich pokryje. Yagi ide ešte ďalej: 16.6 dBi v lúči
vysokom 23 stupňov a širokom 25 stupňov (Amphenol Procom 7176870) a do strán
nič.

Zisk sa udáva voči referencii. dBi porovnáva s ideálnou anténou, ktorá vysiela
rovnako do všetkých smerov. dBd porovnáva s polvlnným dipólom, ktorý sám má
2.15 dBi: aj najjednoduchšia anténa nevysiela nič priamo nahor ani nadol. Dlhší
dipól s dĺžkou 1.25 vlnovej dĺžky dosiahne 5.2 dBi. Kolineárna anténa namiesto
toho ukladá polvlnné prvky nad seba: čím viac ich má, tým vyšší je zisk. Keď
rovnaký signál stlačíš do polovičného priestoru, je tam dvakrát silnejší: 3 dB.
Do štvrtiny je 4-krát silnejší: 6 dB. Výrobcovia udávajú zisk v dBi,
zákonný limit sa počíta v dBd, pozri [V rámci zákonného limitu](#legal).

### Aký zisk pre tvoje miesto {#choose-gain}

- **Kopce, údolia alebo husté mesto: približne 3 dBi.** Vysoký lúč dosiahne na
  uzly nad tebou a pod tebou a dostane sa okolo svahov a budov v ceste. Platí
  to aj naopak: z údolia prejde plochý lúč popod repeater na kopci nad tebou.
  Takou anténou je RAKwireless RAKARG12: sklolaminátová trubica s dĺžkou 36 cm.
- **Predmestia alebo mesto s nízkymi strechami: 5 až 6 dBi.** Štandardná
  sklolaminátová kolineárna anténa.
- **Rovná, otvorená krajina: 8 až 10 dBi.** Najplochší lúč dosiahne pozdĺž
  obzoru najďalej. Pri montáži vysoko prejde ponad blízke uzly.

Zisk v názve je najlepšia hodnota v celom pásme antény. RAKARG12, predávaná ako
3 dBi, má pri 865 až 870 MHz 2.8 dBi. V katalógovom liste si v tabuľke zisku
pozri hodnotu pri frekvencii tvojej predvoľby.

Nad 7 dBi prekročí doska s 22 dBm zákonný limit, ak rozdiel nevyrovná útlm
kábla a filtra. Vysielací výkon podľa toho zníž.

Vysoký zisk pomôže, len keď vieš, kde sú uzly: pozdĺž obzoru okolo repeatera
alebo pri Yagi na jednom vzdialenom repeateri. Companion v ruke mieri každým
smerom, preto mu najlepšie vyhovuje nízky zisk dodanej antény.

## Prečo zvislo {#vertical}

Antény sa navzájom počujú najlepšie, keď mieria rovnakým smerom. Strata rastie
s uhlom medzi nimi: 45 stupňov stojí 3 dB, teda polovicu signálu. Pri 90
stupňoch, keď je vodorovná anténa oproti zvislej, teoreticky nepríde nič. Antény
v sieti mesh stoja zvislo, takže tvoja tiež. Platí to aj pre companion na stole:
keď ho položíš naplocho, všetky uzly okolo teba počujú menej.

## Konektory {#connectors}

Anténu objednaj s konektorom, aký má tvoja doska. Každý adaptér je ďalší spoj,
ktorý treba utesniť, a ďalšia strata signálu.

- **SMA.** Závitový konektor so šírkou približne 6 mm. Zásuvka na väčšine dosiek
  má v strede otvor, anténa má kolík. Konektor tohto druhu má pri 868 MHz útlm
  približne 0.03 dB.
- **RP-SMA.** Rovnaké telo a závit ako SMA, kolík a otvor sú však vymenené.
  Vyzerá ako SMA, no nedá sa s ním spojiť. Pred objednávkou si over, ktorý z
  nich má tvoja doska.
- **U.FL (IPEX).** Drobná nasúvacia zásuvka priamo na doske. Z nej vedie krátky
  kábel typu pigtail k zásuvke SMA v puzdre. Je dimenzovaná na 30
  pripojovacích cyklov, takže ju pripoj raz a nechaj tak.
- **N.** Veľký závitový konektor na sklolaminátových anténach a hrubom kábli.
  Má útlm najviac 0.05 dB. Repeater potrebuje jeden adaptér alebo pigtail z N na
  SMA dosky.

## Útlm kábla {#cable}

Kábel uberá signál skôr, než opustí anténu, a to v oboch smeroch. 3 dB sú
polovica tvojho výkonu. Hodnoty výrobcov na meter pri 868 až 900 MHz:

| Kábel | Útlm na meter | Útlm na 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

Na 3 metroch RG174, tenkého pigtailu dodávaného k mnohým doskám, stratíš polovicu
výkonu. Dosku namontuj pri anténe a použi krátky pigtail, alebo k anténe veď
hrubý kábel. Do súčtu zarátaj každý adaptér a filter na trase.

## Filtre {#filters}

Filter je medzi rádiom a anténou. Prepustí tvoje pásmo a zvyšok zablokuje, takže
silný vysielač v okolí nezahltí prijímač. Potrebuješ ho, keď uzol v blízkosti
iných vysielačov počuje menej, než by mal. Takým uzlom je repeater na stožiari
so základňovými stanicami mobilných operátorov. Filter uberá signál v oboch
smeroch: jeho útlm počítaj ako pri kábli.

| | Filter SAW | Dutinový filter |
|---|---|---|
| Veľkosť | Niekoľko milimetrov, na malej doske | Kovový blok alebo trubica |
| Útlm dobrého filtra | pod 2 dB | pod 1 dB |
| Maximálny vstupný výkon dobrého filtra | 500 mW | niekoľko wattov |

Napríklad sysmocom cf866.5-kt30 je dutinový filter na 863 až 870 MHz s útlmom
najviac 1.0 dB, ktorý znesie 30 W. Je určený do interiéru, preto ho na stožiari
daj do utesnenej skrinky.

Filtre sa veľmi líšia, preto si pred kúpou pozri katalógový list. Menovitý
vstupný výkon musí byť vyšší než tvoj vysielací výkon a priepustné pásmo musí
zahŕňať frekvenciu tvojej predvoľby.

## Montáž {#mounting}

- **Nad okrajom strechy.** Anténa potrebuje voľný výhľad do každého smeru, ktorý
  pokrýva. Pomôže aj niekoľko metrov nad okolitými strechami. V sprievodcovi
  k repeateru v časti [Vyber miesto](/repeater-guide/#site) nájdeš, ako výhľad
  overiť.
- **Ďalej od kovu.** Odkvapy, stožiare, iné antény a kovové strechy vedľa antény
  menia jej vyžarovací diagram a naladenie. Namontuj ju na vrchol stožiara, nie
  vedľa neho.
- **Zvislo.** Použi vodováhu, pozri [Prečo zvislo](#vertical).
- **Odkvapová slučka.** Kábel nechaj pod konektorom prevesiť, než povedie nahor
  alebo dovnútra. Voda potom odkvapne a nestečie do spoja.
- **Utesni každý vonkajší konektor.** Voda v konektore zvyšuje útlm a spôsobuje
  koróziu kolíka. Utesni ho proti dažďu a každý rok tesnenie skontroluj.
- **Blesk.** Anténa na streche je terčom. Plynový zvodič v kábli pri prepätí
  zareaguje a odvedie ho do zeme. Pri uzemnení sa riaď časťou
  [Hardvér](/repeater-guide/#hardware) v sprievodcovi k repeateru a miestnymi
  predpismi.

## V rámci zákonného limitu {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
V Európe používa MeshCore podpásmo 869.40-869.65 MHz s efektívnym vyžiareným
výkonom (e.r.p.) najviac **500 mW**. Limit sa vzťahuje na to, čo opustí anténu:
zisk antény sa pripočíta, útlm kábla a filtra sa odpočíta. Zisk v dBi sa počíta o
2.15 dB menej, lebo limit sa meria voči dipólu.
{{< /callout >}}

Kolineárna anténa s 5.8 dBi na doske s 22 dBm limit dodrží. Tá istá anténa na
doske so zosilňovačom ho nedodrží, kým neznížiš vysielací výkon. Výpočet a 2
riešené príklady nájdeš v sprievodcovi k repeateru v časti
[Výkon: e.r.p. a tvoja anténa](/repeater-guide/#erp).

## Kontrola antény pomocou NanoVNA {#nanovna}

NanoVNA je vektorový sieťový analyzátor vreckovej veľkosti. Ukáže, na akú
frekvenciu je anténa naladená, takže to vieš ešte pred montážou. NanoVNA-H meria
do 1.5 GHz, čo pokrýva 868 MHz.

1. Kalibruj ho na 800 až 950 MHz pomocou koncoviek open, short a load zo súpravy.
2. Pripoj anténu cez adaptér, ktorý bude používať na uzle. Drž ju zvislo a ďalej
   od tela a stola.
3. Odčítaj krivku SWR (pomer stojatých vĺn): ukazuje, koľko signálu anténa vracia
   späť. Pokles musí byť na frekvencii tvojej predvoľby, pri EU/UK (Narrow) na
   869.618 MHz. Pokles vzdialený stovky MHz znamená, že anténa je určená pre iné
   pásmo.

Štvrťvlna pri 868 MHz má 86 mm (vlnová dĺžka je 345 mm). Samotná dĺžka ti pásmo
neprezradí, lebo výrobcovia prútové antény skladajú a dopĺňajú o predlžovacie
prvky. NanoVNA ti ho prezradí.

## Zdroje {#sources}

- Útlm kábla: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  katalógový list Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  katalógové listy Times Microwave LMR-240 a LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antény: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  katalógový list Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Zisk ako signál stlačený do menšieho priestoru: [RF Cafe, úvod do antén](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Konektory: katalógové listy Rosenberger 32S102 (SMA) a 53S101 (N), katalóg
  Hirose U.FL.
- Filtre: produktová stránka sysmocom cf866.5-kt30,
  [plynové zvodiče Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarizačná strata: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Zisk dipólu podľa dĺžky: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Vlnová dĺžka: rýchlosť svetla z [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Zákonný limit: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Annex 1, pásmo h1.7; ostatné uvádza [sprievodca k repeateru](/repeater-guide/#legal).
