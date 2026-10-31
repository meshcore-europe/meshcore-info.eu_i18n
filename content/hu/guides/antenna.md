---
title: Antennaútmutató
lead: A jó antenna, jól felszerelve, messzebbre ér, mint a nagyobb teljesítmény. Ellenőrizd a companion antennáját, aztán válassz, csatlakoztass és szerelj fel egyet egy átjátszóhoz.
description: 'MeshCore-antenna kiválasztása és felszerelése 868 MHz-re: a companion botantennájának ellenőrzése, antennatípusok és nyereség, csatlakozók, kábelveszteség méterenként, szűrők, szerelés, és hogyan számít bele a nyereség a jogi határértékbe.'
eyebrow: Companion és átjátszó · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-10-31'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

A magasság, a hangolt antenna és a rövid kábel több hatótávot ad,
mint bármennyi extra milliwatt. Ez az útmutató a companionnel kezdődik.
Ez az a rádió, amelyről üzenetet küldesz. Utána az átjátszó antennájáról
lesz szó. Az átjátszó olyan csomópont, amely tetőről vagy árbocról
továbbadja az üzeneteket.

## A companionöd {#companion}

{{< callout type="warning" >}}
Mielőtt bekapcsolod a rádiót, csatlakoztasd az antennát. Ha egy LoRa
rádió antenna nélkül ad, tönkreteheti a saját chipjét.
{{< /callout >}}

A paneledhez kapott antenna megfelel. Csatlakoztasd, tartsd függőlegesen a
csomópontot, és kezdj el üzenni. Egy jobb antenna a companionön keveset javít.
Egy elérhető közelségben lévő átjátszó sokat javít.

Külön botantennát csak akkor vegyél, ha a gyári eltört vagy hiányzik. Nem
minden 868 MHz-re árult botantenna van erre hangolva. Mielőtt megbízol
benne, [ellenőrizd NanoVNA-val](#nanovna), amely egy zsebméretű
antennaanalizátor. Vagy kölcsönözz egyet egy működő panelről.

Egy erős adó mellett a csomópont kevesebbet hall, mint kellene. Egy kis
[SAW (felületi akusztikus hullám) szűrő](#filters) a rádió és az antenna
között távol tartja ezt az adót a vevőtől. Előbb nézd meg az adatlapját:

- **Maximális bemenő teljesítmény.** A szűrő a saját adásod útvonalában
  is ott van. Ha egy panel 22 dBm-mel (160 mW) ad egy 15 dBm-re méretezett
  szűrőbe, a szűrő tönkremegy.
- **Áteresztő sáv.** Tartalmaznia kell a preseted frekvenciáját. Egy
  868.65–869.25 MHz-es szűrő nem engedi át a 869.618 MHz-es EU/UK (Narrow)
  csatornát.

## Antennatípusok átjátszóhoz {#types}

A mesh minden antennája függőlegesen áll. A típust aszerint válaszd, hol
vannak az elérni kívánt csomópontok:

- **Üvegszálas kollineáris antenna.** Fehér cső egy árbocon, a nyeresége
  körben a horizont mentén van. Ez a szokásos választás egy várost
  kiszolgáló átjátszóhoz.
- **Dipól.** Rövidebb, kisebb a nyeresége, és magas a nyalábja. A
  kollineárisnál jobban eléri az alattad és feletted lévő csomópontokat,
  például egy völgy feletti dombról.
- **Yagi.** Egy tartórúd keresztirányú elemekkel, egy helyre irányítva.
  Egyetlen távoli átjátszót ér el, mást alig. Az elemekkel függőlegesen
  szereld fel, mert a polarizációja az elemeket követi.

## Nyereség és nyaláb {#gain}

A nyereség nem növeli a teljesítményt. A jelet, amely felfelé és lefelé
menne, a horizont mentén küldi el. Olyan, mint egy fókuszált zseblámpa: ugyanaz
az elem, hosszabb és keskenyebb fénycsóva. Ezt jól mutatja ugyanannak a
gyártónak egy dipólja és egy kollineárisa:

| Antenna | Nyereség | Függőleges nyalábszélesség |
|---|---|---|
| Dipól (Sirio SO 868-915-2) | 2.2 dBi | 88 fok |
| Üvegszálas kollineáris (Sirio SPO 868-915-6) | 5.8 dBi | 23 fok |

{{< gain >}}

Az ábra az árbocon átmenő metszet, oldalról nézve. Forgasd körbe az árboc körül,
és megkapod a teljes nyalábot: a dipólnál fánkot, a kollineárisnál lapos
korongot. A függőleges antenna minden irányba egyformán sugároz maga körül.
A rajzolt nyalábon kívül a jel nem szűnik meg. Gyengébb, de egy közeli
csomópontnak még elég.

Tetőn a lapos nyaláb a jó. A csomópontok fölé magasodó dombon egy 23 fokos
nyaláb elhalad a fejük fölött. Egy dipól lefedi őket. A Yagi még tovább
megy: 16.6 dBi egy 23 fok magas és 25 fok széles nyalábban (Amphenol
Procom 7176870), oldalra pedig semmi.

A nyereséget egy referenciához mérik. A dBi egy ideális antennához
viszonyít, amely minden irányba egyformán sugároz. A dBd egy félhullámú
dipólhoz viszonyít, amelynek magának 2.15 dBi a nyeresége. Még a
legegyszerűbb antenna sem sugároz semmit egyenesen fel vagy le. Egy
hosszabb, 1.25 hullámhosszú dipól 5.2 dBi-t ér el. A kollineáris antenna
ehelyett félhullámú elemeket rak egymás fölé. Minél többet rak egymásra,
annál nagyobb a nyereség. Ha ugyanazt a jelet fele akkora térbe sűríted,
ott kétszer olyan erős: 3 dB. Negyedakkorába sűrítve 4-szer olyan erős:
6 dB. A gyártók dBi-ben adják meg a nyereséget, a jogi határérték viszont
dBd-ben számol, lásd [A jogi határértéken belül](#legal).

### Milyen nyereség kell a helyszínedhez {#choose-gain}

- **Dombok, völgyek vagy sűrű város: kb. 3 dBi.** A magas nyaláb eléri az
  alattad és feletted lévő csomópontokat. Az útban álló lejtőket és
  épületeket is megkerüli. Fordítva is igaz: völgyből a lapos nyaláb
  elhalad a fenti dombon álló átjátszó alatt. Ilyen például a RAKwireless
  RAKARG12, egy 36 cm-es üvegszálas cső.
- **Kertváros vagy alacsony tetős város: 5–6 dBi.** A szokásos üvegszálas
  kollineáris.
- **Sík, nyílt terep: 8–10 dBi.** A leglaposabb nyaláb ér a legmesszebbre
  a horizont mentén. Magasra szerelve elhalad a közeli csomópontok fölött.

A névben szereplő nyereség az antenna teljes sávjának legjobb értéke. A
3 dBi-sként árult RAKARG12 nyeresége 865–870 MHz-en 2.8 dBi. Az
adatlap nyereségtáblázatában a preseted frekvenciáját nézd.

7 dBi felett egy 22 dBm-es panel túllépi a jogi határértéket, hacsak a
kábel- és szűrőveszteség ki nem egyenlíti a különbséget. Ennek megfelelően
csökkentsd az adóteljesítményt.

A nagy nyereség csak akkor segít, ha tudod, hol vannak a csomópontok: egy
átjátszó körül a horizont mentén, vagy Yagi esetén egy távoli átjátszónál.
A kezedben tartott companion mindenfelé mutat. Ezért a gyári, kis
nyereségű antenna illik hozzá a legjobban.

## Miért függőleges {#vertical}

Az antennák akkor hallják egymást a legjobban, ha egy irányba állnak. A
veszteség a köztük lévő szöggel nő: 45 fok 3 dB-be kerül, ez a jeled fele.
90 foknál, vagyis egy fekvő antenna egy állóval szemben, elméletben semmi
sem érkezik meg. A mesh függőlegesen áll, ezért a te antennád is. Ez az
asztalon lévő companionre is igaz: ha lefekteted, minden körülötted lévő
csomópont kevesebbet hall.

## Csatlakozók {#connectors}

Az antennát a paneleden lévő csatlakozóval rendeld. Minden adapter egy
újabb tömítendő illesztés, és újabb jelveszteség.

- **SMA.** Kb. 6 mm széles menetes csatlakozó. A legtöbb panelen az
  aljzat közepén lyuk van, az antennán tüske. Egy ilyen csatlakozó
  868 MHz-en kb. 0.03 dB-t veszít.
- **RP-SMA.** Ugyanaz a ház és menet, mint az SMA-nál, de a tüske és a
  lyuk fel van cserélve. Úgy néz ki, mint az SMA, mégsem illeszkedik
  hozzá. Rendelés előtt nézd meg, melyik van a paneleden.
- **U.FL (IPEX).** Apró, rádugós aljzat magán a panelen. Egy rövid
  pigtail kábel vezet belőle a ház SMA-aljzatához. 30 csatlakoztatásra
  méretezték, ezért egyszer dugd be, és hagyd úgy.
- **N.** Nagy menetes csatlakozó az üvegszálas antennákon és a vastag
  kábeleken. Legfeljebb 0.05 dB-t veszít. Egy átjátszóhoz kell egy adapter
  vagy pigtail N-ről a panel SMA-jára.

## Kábelveszteség {#cable}

A kábel már azelőtt jelet emészt fel, hogy a jel elhagyná az antennát,
mindkét irányban. 3 dB a teljesítményed fele. A gyártók méterenkénti
adatai 868–900 MHz-en:

| Kábel | Veszteség méterenként | Veszteség 5 m-en |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 méter RG174, a sok panelhez adott vékony pigtail, elviszi a teljesítményed
felét. A panelt rövid pigtaillel szereld az antenna mellé, vagy vezess
hozzá vastag kábelt. Az összeghez add hozzá az útvonal minden adapterét és
szűrőjét.

## Szűrők {#filters}

A szűrő a rádió és az antenna között van. Átengedi a sávodat, a többit
blokkolja, így egy közeli erős adó nem nyomja el a vevőt. Akkor kell, ha
egy csomópont más adók közelében kevesebbet hall, mint kellene. Ilyen egy
árbocon álló átjátszó, ahol mobiltelefon-bázisállomások is vannak. A szűrő
mindkét irányban jelet emészt fel: a veszteségét úgy számold, mint a
kábelét.

| | SAW-szűrő | Üregrezonátoros szűrő |
|---|---|---|
| Méret | Néhány milliméter, egy kis panelen | Fémtömb vagy -cső |
| Egy jó szűrő vesztesége | 2 dB alatt | 1 dB alatt |
| Egy jó szűrő maximális bemenő teljesítménye | 500 mW | több watt |

A sysmocom cf866.5-kt30 például egy 863–870 MHz-es üregrezonátoros szűrő,
legfeljebb 1.0 dB-t veszít, és 30 W-ot bír. Beltérre készült, ezért
árbocon tedd egy tömített dobozba.

A szűrők nagyon különböznek, ezért vásárlás előtt nézd meg az adatlapot.
A névleges bemenő teljesítményének meg kell haladnia az adóteljesítményedet,
az áteresztő sávjának pedig tartalmaznia kell a preseted frekvenciáját.

## Felszerelés {#mounting}

- **A tetőperem fölé.** Az antennának szabad rálátás kell minden irányba,
  amelyet kiszolgál. Már néhány méter a környező tetők fölött is segít. Az
  átjátszó-útmutató [Helyszín kiválasztása](/repeater-guide/#site) része
  megmutatja, hogyan ellenőrizd a rálátást.
- **Fémtől távol.** Az antenna melletti ereszcsatornák, árbocok, más
  antennák és fémtetők megváltoztatják a sugárzási képét és a hangolását.
  Az árboc tetejére szereld, ne mellé.
- **Függőlegesen.** Használj vízmértéket, lásd [Miért
  függőleges](#vertical).
- **Csepphurok.** Hagyd, hogy a kábel a csatlakozó alá lógjon, mielőtt
  felfelé vagy befelé megy. Így a víz lecsöpög, és nem folyik az
  illesztésbe.
- **Tömíts minden kültéri csatlakozót.** A csatlakozóba jutó víz növeli a
  veszteséget, és korrodálja a tüskét. Tömítsd eső ellen, és évente
  ellenőrizd a tömítést.
- **Villám.** A tetőn álló antenna célpont. A kábelbe tett gázkisüléses
  túlfeszültség-levezető túlfeszültségnél működésbe lép, és a földbe
  vezeti. A földeléshez kövesd az átjátszó-útmutató
  [Hardver](/repeater-guide/#hardware) részét és a helyi előírásokat.

## A jogi határértéken belül {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
Európában a MeshCore a 869.40-869.65 MHz-es alsávot használja, legfeljebb
**500 mW** effektív kisugárzott teljesítménnyel (e.r.p.). A határérték azt
számolja, ami elhagyja az antennát: az antenna nyeresége hozzáadódik, a
kábel- és szűrőveszteség levonódik. A dBi-ben megadott nyereség 2.15 dB-lel
kevesebbet számít, mert a határértéket egy dipólhoz mérik.
{{< /callout >}}

Egy 5.8 dBi-s kollineáris egy 22 dBm-es panelen a határértéken belül
marad. Ugyanez az antenna egy erősítős panelen túllépi, amíg nem csökkented
az adóteljesítményt. Az átjátszó-útmutató [Teljesítmény: e.r.p. és az
antennád](/repeater-guide/#erp) része tartalmazza a számítást és 2
kidolgozott példát.

## Antenna ellenőrzése NanoVNA-val {#nanovna}

A NanoVNA egy zsebméretű vektoros hálózatanalizátor. Megmutatja, melyik
frekvenciára van hangolva egy antenna, így még felszerelés előtt tudod. A
NanoVNA-H 1.5 GHz-ig mér, ez lefedi a 868 MHz-et.

1. Kalibráld 800–950 MHz-re a készlet open, short és load elemeivel.
2. Csatlakoztasd az antennát azon az adapteren keresztül, amelyet a
   csomóponton is használni fog. Tartsd függőlegesen, a testedtől és az
   asztaltól távol.
3. Olvasd le az SWR (állóhullám-arány) görbét: megmutatja, mennyi jelet
   ver vissza az antenna. A mélypontnak a preseted frekvenciájára kell
   esnie, EU/UK (Narrow) esetén 869.618 MHz-re. Ha a mélypont több száz
   MHz-re van, az antenna másik sávra készült.

868 MHz-en a negyedhullám 86 mm (a hullámhossz 345 mm). A hosszból
önmagában nem derül ki a sáv, mert a gyártók hajtogatják és terhelik a
botantennákat. A NanoVNA viszont megmutatja.

## Források {#sources}

- Kábelveszteség: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  a Huber+Suhner RG316 adatlapja,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  a Times Microwave LMR-240 és LMR-400 adatlapjai,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antennák: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  a Sirio SO 868-915-2 adatlapja,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- A nyereség mint kisebb térbe sűrített jel: [RF Cafe, bevezetés az antennákhoz](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Csatlakozók: a Rosenberger 32S102 (SMA) és 53S101 (N) adatlapjai, a
  Hirose U.FL katalógus.
- Szűrők: a sysmocom cf866.5-kt30 termékoldala,
  [Citel gázkisüléses túlfeszültség-levezetők](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarizációs veszteség: [University of Toronto, Friis-hatások](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- A dipól nyeresége hossz szerint: [Wikipedia, Dipólantenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Hullámhossz: a fénysebesség a [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c) adata szerint.
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Jogi határérték: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  1. melléklet, h1.7 sáv; a többit az [átjátszó-útmutató](/repeater-guide/#legal)
  sorolja fel.
