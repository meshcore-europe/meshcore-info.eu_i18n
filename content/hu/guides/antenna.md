---
title: Antennakalauz
lead: Az antenna a csomópontod fele. A megfelelő antenna, jól felszerelve, messzebbre ér, mint a nagyobb teljesítmény. Ellenőrizd a companion antennáját, aztán válassz, csatlakoztass és szerelj fel egyet az átjátszóhoz.
description: 'MeshCore antenna kiválasztása és felszerelése 868 MHz-re: a companion botantennájának ellenőrzése, antennatípusok és nyereség, csatlakozók, kábelveszteség méterenként, szűrők, szerelés, és hogyan számít a nyereség a jogi határértékbe.'
eyebrow: Companion és átjátszó · 868 MHz
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '45010ad0'
  seeded: '2026-10-26'
  fields: {title: '3a76cb0e', lead: '98430ade', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', '94c5bae4', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
---

A magasság, a hangolt antenna és a rövid kábel több hatótávot hoz, mint
bármennyi plusz milliwatt. Ez a kalauz a companionnel kezd, azzal a
rádióval, amelyről üzenetet küldesz. Utána az átjátszó antennájával
foglalkozik. Az átjátszó olyan csomópont, amely tetőről vagy árbocról
továbbítja az üzeneteket.

## A companionöd {#companion}

{{< callout type="warning" >}}
Csatlakoztasd az antennát, mielőtt bekapcsolod a rádiót. Az antenna nélkül
adó LoRa rádió tönkreteheti a saját chipjét.
{{< /callout >}}

A kártyához kapott antenna megteszi. Csatlakoztasd, tartsd a csomópontot
függőlegesen, és kezdj üzenni. A jobb antenna a companionön keveset hoz;
egy elérhető átjátszó sokat.

Külön pálcaantennát csak akkor vegyél, ha a mellékelt törött vagy hiányzik.
Nem minden 868 MHz-re árult pálcaantenna van rá hangolva. [Ellenőrizd
NanoVNA-val](#nanovna), egy zsebméretű antennaelemzővel, mielőtt megbízol
benne, vagy kérj kölcsön egyet egy működő kártyáról.

Egy erős adó melletti csomópont kevesebbet hall, mint kellene. Egy kis
[SAW (felületi akusztikus hullámú) szűrő](#filters) a rádió és az antenna
között távol tartja azt az adót a vevőtől. Előbb nézd meg az adatlapját:

- **Maximális bemeneti teljesítmény.** A szűrő a saját adásod útjában is
  áll. Egy 22 dBm-mel (160 mW) adó kártya egy 15 dBm-re méretezett szűrőbe
  tönkreteszi a szűrőt.
- **Áteresztő sáv.** Tartalmaznia kell a presetted frekvenciáját. Egy
  868.65 és 869.25 MHz közötti szűrő nem engedi át az EU/UK (Narrow)
  csatornát a 869.618 MHz-en.

## Antennatípusok átjátszóhoz {#types}

A mesh minden antennája függőlegesen áll. A típust aszerint válaszd, hol
vannak az elérni kívánt csomópontok:

- **Üvegszálas kollineáris.** Fehér cső az árbocon, nyereséggel a horizont
  minden irányába. Ez a szokásos választás egy várost kiszolgáló
  átjátszóhoz.
- **Dipól.** Rövidebb, kisebb nyereséggel és magas nyalábbal. Az alattad
  és feletted lévő csomópontokat jobban eléri, mint a kollineáris. Ez
  számít egy völgy feletti dombon.
- **Yagi.** Egy rúd keresztelemekkel, egyetlen helyre irányítva. Egyetlen
  távoli átjátszót ér el, és szinte semmi mást. Függőleges elemekkel
  szereld fel, mert a polarizációja az elemeket követi.

## Nyereség és a nyaláb {#gain}

A nyereség nem ad teljesítményt. A fel és le menő jelet fogja, és a
horizont mentén küldi tovább. Mint egy fókuszált zseblámpa: ugyanaz az
elem, hosszabb és keskenyebb nyaláb. Egy gyártó dipólja és kollineárisa
mutatja ezt:

| Antenna | Nyereség | Függőleges nyalábszélesség |
|---|---|---|
| Dipól (Sirio SO 868-915-2) | 2.2 dBi | 88 fok |
| Üvegszálas kollineáris (Sirio SPO 868-915-6) | 5.8 dBi | 23 fok |

{{< gain >}}

Az ábra az árbocot metszi, oldalról nézve. Forgasd körbe az árboc körül,
és megkapod a teljes nyalábot: fánk a dipólnál, lapos korong a
kollineárisnál. A függőleges antenna minden irányba ugyanúgy sugároz maga
körül. A rajzolt nyalábon kívül a jel nem áll meg; gyengébb, de egy közeli
csomópontnak még elég.

Tetőn lapos nyalábot akarsz. A csomópontok fölött magas dombon a 23 fokos
nyaláb a fejük felett megy el; a dipól lefedi őket. A Yagi ezt tovább
viszi: 16.6 dBi egy 23 fok magas és 25 fok széles nyalábban (Amphenol
Procom 7176870), és semmi oldalra.

A nyereség egy viszonyítási alaphoz képest számít. A dBi egy ideális,
minden irányba egyformán sugárzó antennához hasonlít. A dBd egy
félhullámú dipólhoz hasonlít, amelynek önmagában 2.15 dBi a nyeresége: még
a legegyszerűbb antenna sem sugároz egyenesen fel vagy le. Egy hosszabb,
1.25 hullámhosszú dipól 5.2 dBi-t ér el. A kollineáris ehelyett félhullámú
elemeket rak egymás fölé: minél többet rak, annál nagyobb a nyereség.
Szorítsd ugyanazt a jelet fele akkora térbe, és ott kétszer olyan erős:
3 dB. Negyedakkora térbe, 4-szer olyan erős: 6 dB. A gyártók dBi-ben adják
meg a nyereséget; a törvényi határ dBd-ben számol, lásd [A törvényi
határon belül](#legal).

### Melyik nyereség illik a helyedhez {#choose-gain}

- **Dombok, völgyek vagy sűrű város: körülbelül 3 dBi.** A magas nyaláb
  eléri az alattad és feletted lévő csomópontokat, és körbemegy az útban
  álló lejtőkön és épületeken. Fordítva is működik: egy völgyből a lapos
  nyaláb elmegy a fenti domb átjátszója alatt. A RAKwireless RAKARG12 ilyen:
  egy 36 cm-es üvegszálas cső.
- **Elővárosok vagy alacsony tetős kisváros: 5 és 6 dBi között.** A szokásos
  üvegszálas kollineáris.
- **Sík, nyílt terep: 8 és 10 dBi között.** A leglaposabb nyaláb ér el
  legmesszebbre a horizont mentén. Magasra szerelve elmegy a közeli
  csomópontok felett.

A névben szereplő nyereség az antenna teljes sávján mért legjobb érték. A
3 dBi-vel eladott RAKARG12 865 és 870 MHz között 2.8 dBi-t ad. Olvasd el
az adatlap nyereségtáblázatát a preseted frekvenciáján.

7 dBi felett egy 22 dBm-es board túllépi a törvényi határt, hacsak a kábel
és a szűrő vesztesége nem pótolja a különbséget. Csökkentsd ehhez az adási
teljesítményt.

A nagy nyereség csak akkor segít, ha tudod, hol vannak a csomópontok: a
horizont mentén egy átjátszó körül, vagy egyetlen távoli átjátszónál egy
Yaginál. A kezedben tartott companion minden irányba mutat, így a vele
kapott kis nyereség illik hozzá a legjobban.

## Miért függőlegesen {#vertical}

Az antennák akkor hallják egymást a legjobban, ha ugyanabba az irányba
mutatnak. A veszteség a köztük lévő szöggel nő: 45 fok 3 dB-be kerül, a
jeled felébe. 90 foknál, egy fekvő antenna egy állóval szemben, elméletben
semmi nem érkezik meg. A mesh függőlegesen áll, tehát a te antennád is.
Ez az asztalon fekvő companionre is igaz: ha lefekteted, minden
csomópont körülötted kevesebbet hall.

## Csatlakozók {#connectors}

Olyan csatlakozóval rendeld az antennát, amilyen a boardodon van. Minden
adapter eggyel több tömítendő illesztés és több elveszett jel.

- **SMA.** Egy körülbelül 6 mm széles menetes csatlakozó. A legtöbb board
  aljzatában középen lyuk van; a tű az antennán van. Egy ilyen csatlakozó
  868 MHz-en körülbelül 0.03 dB-t veszít.
- **RP-SMA.** Ugyanaz a test és menet, mint az SMA-nál, de a tű és a lyuk
  fel van cserélve. Úgy néz ki, mint az SMA, és nem illik hozzá. Rendelés
  előtt nézd meg, melyik van a boardodon.
- **U.FL (IPEX).** Apró, rápattintható aljzat magán a boardon. Rövid
  pigtail kábel megy róla a ház SMA-aljzatához. 30 csatlakoztatásra
  méretezték, ezért egyszer kösd be, és hagyd úgy.
- **N.** A nagy menetes csatlakozó az üvegszálas antennákon és a vastag
  kábelen. Legfeljebb 0.05 dB-t veszít. Az átjátszóhoz kell egy adapter
  vagy pigtail N-ről a board SMA-jára.

## Kábelveszteség {#cable}

A kábel még az antenna előtt jelet emészt fel, mindkét irányban. 3 dB a
teljesítményed fele. A gyártók méterenkénti értékei 868 és 900 MHz
között:

| Kábel | Veszteség méterenként | Veszteség 5 m-en |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 méter RG174, a sok boardhoz adott vékony pigtail, a teljesítményed felét
elveszíti. Szereld a boardot az antennához egy rövid pigtaillel, vagy
vezess hozzá vastag kábelt. Az útvonalon lévő minden adaptert és szűrőt
add hozzá az összeghez.

## Szűrők {#filters}

A szűrő a rádió és az antenna között ül. Átengedi a sávodat, és
kiszűri a többit, így egy közeli erős adó nem telíti a vevőt. Akkor kell,
ha egy csomópont más adók közelében kevesebbet hall, mint kellene. Egy
mobil bázisállomásokkal közös árbocon álló átjátszó ilyen csomópont. A
szűrő mindkét irányban jelet veszít: a veszteségét úgy számold, mint a
kábelét.

| | SAW-szűrő | Üregrezonátoros szűrő |
|---|---|---|
| Méret | Néhány milliméter, egy kis panelen | Fémtömb vagy -cső |
| Egy jó darab vesztesége | 2 dB alatt | 1 dB alatt |
| Egy jó darab legnagyobb bemeneti teljesítménye | 500 mW | több watt |

A sysmocom cf866.5-kt30 például üregrezonátoros szűrő 863 és 870 MHz
közé, legfeljebb 1.0 dB-t veszít, és 30 W-ot bír. Beltérre készült, ezért
az árbocon tömített dobozba tedd.

A szűrők nagyon különböznek, ezért vásárlás előtt nézd meg az adatlapot.
A névleges bemeneti teljesítménye haladja meg az adási teljesítményedet,
és az áteresztő sávja tartalmazza a preseted frekvenciáját.

## Szerelés {#mounting}

- **A tetőél fölé.** Az antennának szabad kilátás kell minden irányba,
  amelyet kiszolgál. Már néhány méter a környező tetők felett is segít.
  Az átjátszókalauz [Helyszín választása](/repeater-guide/#site) része
  mutatja, hogyan ellenőrizd a kilátást.
- **Fémtől távol.** Az antenna melletti ereszcsatornák, árbocok, más
  antennák és fémtetők megváltoztatják a sugárzási képét és a hangolását.
  Az árboc tetejére szereld, ne mellé.
- **Függőlegesen.** Használj vízmértéket, lásd [Miért
  függőlegesen](#vertical).
- **Csepegtetőhurok.** Hagyd, hogy a kábel a csatlakozó alá lógjon, mielőtt
  felfelé vagy befelé megy. A víz így lecsepeg, ahelyett hogy a kötésbe
  folyna.
- **Tömíts minden kültéri csatlakozót.** A csatlakozóba jutó víz növeli a
  veszteséget és korrodálja a tűt. Tömítsd eső ellen, és évente ellenőrizd
  a tömítést.
- **Villám.** A tetőn lévő antenna célpont. A kábelbe iktatott
  gázkisüléses túlfeszültség-levezető túlfeszültségnél begyújt, és a
  földbe vezeti azt. Kövesd az átjátszókalauz [Hardver](/repeater-guide/#hardware)
  részét és a helyi földelési szabályokat.

## A törvényi határon belül {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
Európában a MeshCore a 869.40-869.65 MHz alsávot használja, legfeljebb
**500 mW** effektív kisugárzott teljesítménnyel (e.r.p.). A határ azt
számolja, ami az antennát elhagyja: az antenna nyeresége hozzáad, a kábel
és a szűrő vesztesége levon. A dBi-ben megadott nyereség 2.15 dB-lel
kevesebbet számít, mert a határt dipólhoz képest mérik.
{{< /callout >}}

Egy 5.8 dBi-s kollineáris egy 22 dBm-es boardon a határon belül marad.
Ugyanez az antenna egy erősítős boardon nem, amíg nem csökkented az adási
teljesítményt. Az átjátszókalauz [Teljesítmény: e.r.p. és az
antennád](/repeater-guide/#erp) része adja az összeget és 2 kidolgozott
példát.

## Antenna ellenőrzése NanoVNA-val {#nanovna}

A NanoVNA egy zsebméretű vektoros hálózatelemző. Megmutatja, melyik
frekvenciára van hangolva az antenna, így még a felszerelés előtt tudod.
A NanoVNA-H 1.5 GHz-ig mér, ami lefedi a 868 MHz-et.

1. Kalibráld 800 és 950 MHz közé a készletében lévő nyitott, rövidzár és
   lezáró darabokkal.
2. Csatlakoztasd az antennát azon az adapteren át, amelyet a csomóponton
   használ majd. Tartsd függőlegesen, távol a testedtől és az asztaltól.
3. Olvasd le az SWR (állóhullámarány) görbét: ez mutatja, mennyi jelet küld
   vissza az antenna. A völgynek a preseted frekvenciáján kell ülnie, EU/UK
   (Narrow) esetén 869.618 MHz-en. Egy több száz MHz-cel arrébb lévő völgy
   azt jelenti, hogy az antenna más sávra készült.

Egy negyedhullám 868 MHz-en 86 mm (a hullámhossz 345 mm). A hossz
önmagában nem árulja el a sávot, mert a gyártók hajtogatják és terhelik a
pálcaantennákat; a NanoVNA igen.

## Források {#sources}

- Kábelveszteség: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  a Huber+Suhner RG316 adatlap,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  a Times Microwave LMR-240 és LMR-400 adatlapok,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antennák: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  a Sirio SO 868-915-2 adatlap,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Nyereség mint kisebb térbe préselt jel: [RF Cafe, bevezetés az antennákba](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Csatlakozók: a Rosenberger 32S102 (SMA) és 53S101 (N) adatlapok, a
  Hirose U.FL katalógus.
- Szűrők: a sysmocom cf866.5-kt30 termékoldal,
  [Citel gázkisüléses túlfeszültség-levezetők](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarizációs veszteség: [University of Toronto, Friis-hatások](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipólnyereség hossz szerint: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Hullámhossz: a fénysebesség a [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c) oldaláról.
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Jogi határérték: [CEPT ERC 70-03 ajánlás](https://docdb.cept.org/document/845),
  1. melléklet, h1.7 sáv; a többit az [átjátszókalauz](/repeater-guide/#legal)
  sorolja fel.
