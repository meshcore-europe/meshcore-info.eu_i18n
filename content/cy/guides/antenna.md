---
title: Canllaw antena
lead: Mae'r antena iawn, wedi'i osod yn dda, yn cyrraedd ymhellach na mwy o bŵer. Gwiria'r antena ar dy gydymaith, yna dewisa, cysyllta a gosod un ar gyfer ailadroddydd.
description: 'Dewis a gosod antena MeshCore ar gyfer 868 MHz: gwirio chwip cydymaith, mathau o antena a chynnydd, cysylltwyr, colled cebl y metr, hidlyddion, gosod a sut mae cynnydd yn cyfrif tuag at y terfyn cyfreithiol.'
eyebrow: Cydymaith ac ailadroddydd · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-11-02'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Mae uchder, antena wedi'i diwnio a chebl byr yn rhoi mwy o gyrhaeddiad nag
unrhyw filiwat ychwanegol. Mae'r canllaw hwn yn dechrau gyda'r cydymaith, y
radio rwyt ti'n anfon negeseuon ohono. Yna mae'n trafod yr antena ar
ailadroddydd, nod sy'n pasio negeseuon ymlaen o do neu fast.

## Dy gydymaith {#companion}

{{< callout type="warning" >}}
Cysyllta'r antena cyn i ti droi'r radio ymlaen. Gall radio LoRa sy'n
trosglwyddo heb antena niweidio'i sglodyn ei hun.
{{< /callout >}}

Mae'r antena a ddaeth gyda dy fwrdd yn gwneud y gwaith. Cysyllta fe, dal y
nod ar ei sefyll, a dechreua anfon negeseuon. Ychydig a enilli di o antena
gwell ar gydymaith; llawer a enilli di o ailadroddydd o fewn cyrraedd.

Paid â phrynu chwip ar wahân oni bai bod yr un a ddaeth gyda'r bwrdd wedi
torri neu ar goll. Dydy pob chwip sydd ar werth ar gyfer 868 MHz ddim wedi'i
diwnio i'r amledd hwnnw. [Gwiria fe gyda NanoVNA](#nanovna), dadansoddwr antena
poced, cyn i ti ymddiried ynddo, neu benthyca un oddi ar fwrdd sy'n gweithio.

Mae nod wrth ymyl trosglwyddydd cryf yn clywed llai nag y dylai. Mae
[hidlydd SAW (tonnau acwstig arwyneb)](#filters) bach rhwng y radio a'r antena
yn cadw'r trosglwyddydd hwnnw allan o'r derbynnydd. Gwiria ei daflen ddata yn
gyntaf:

- **Uchafswm pŵer mewnbwn.** Mae'r hidlydd hefyd ar lwybr dy drosglwyddiad dy
  hun. Mae bwrdd sy'n trosglwyddo 22 dBm (160 mW) i hidlydd wedi'i raddio ar
  gyfer 15 dBm yn torri'r hidlydd.
- **Band pasio.** Rhaid iddo gynnwys amledd dy ragosodiad. Dydy hidlydd ar
  gyfer 868.65 i 869.25 MHz ddim yn gadael sianel EU/UK (Narrow) ar
  869.618 MHz drwodd.

## Mathau o antena ar gyfer ailadroddydd {#types}

Mae pob antena ar y rhwydwaith mesh yn sefyll yn syth i fyny. Dewisa'r math yn
ôl lle mae'r nodau rwyt ti am eu cyrraedd:

- **Colinear gwydr ffibr.** Tiwb gwyn ar fast, gyda chynnydd yr holl ffordd
  o amgylch y gorwel. Dyma'r dewis arferol i ailadroddydd sy'n gwasanaethu
  tref.
- **Deupol.** Mae'n fyrrach, gyda llai o gynnydd a phaladr tal. Mae'n cyrraedd
  nodau oddi tanat ac uwch dy ben yn well na cholinear, er enghraifft o fryn
  uwchben dyffryn.
- **Yagi.** Bŵm ag elfennau croes, wedi'i anelu at un lle. Mae'n cyrraedd un
  ailadroddydd pell a fawr ddim arall. Gosoda fe gyda'r elfennau'n syth i fyny,
  oherwydd bod ei bolareiddiad yn dilyn yr elfennau.

## Cynnydd a'r paladr {#gain}

Dydy cynnydd ddim yn ychwanegu pŵer. Mae'n cymryd y signal a fyddai'n mynd i
fyny ac i lawr ac yn ei anfon ar hyd y gorwel. Mae fel tortsh rwyt ti'n ei
ffocysu: yr un batri, paladr hirach a chulach. Mae deupol a cholinear gan yr
un gwneuthurwr yn dangos hyn:

| Antena | Cynnydd | Lled fertigol y paladr |
|---|---|---|
| Deupol (Sirio SO 868-915-2) | 2.2 dBi | 88 gradd |
| Colinear gwydr ffibr (Sirio SPO 868-915-6) | 5.8 dBi | 23 gradd |

{{< gain >}}

Mae'r diagram yn dangos toriad trwy'r mast, o'r ochr. Tro fe o amgylch y
mast ac mae gen ti'r paladr cyfan: toesen i'r deupol, disg fflat i'r colinear.
Mae antena syth yn anfon yr un fath i bob cyfeiriad o'i gwmpas. Y tu allan i'r
paladr yn y llun dydy'r signal ddim yn stopio; mae'n wannach, ond yn dal yn
ddigon i nod gerllaw.

Ar do, paladr fflat rwyt ti ei eisiau. Ar fryn ymhell uwchben y nodau,
mae paladr 23 gradd yn pasio dros eu pennau; mae deupol yn eu cyrraedd. Mae
Yagi yn mynd â hyn ymhellach: 16.6 dBi mewn paladr 23 gradd o uchder a 25 gradd
o led (Amphenol Procom 7176870), a dim i'r ochrau.

Rwyt ti'n cyfrif cynnydd yn erbyn cyfeirnod. Mae dBi yn cymharu ag antena delfrydol
sy'n anfon yn gyfartal i bob cyfeiriad. Mae dBd yn cymharu â deupol hanner ton,
sydd â 2.15 dBi ei hun: dydy hyd yn oed yr antena symlaf ddim yn anfon dim yn
syth i fyny nac i lawr. Mae deupol hirach, 1.25 tonfedd, yn cyrraedd 5.2 dBi.
Yn lle hynny, mae colinear yn pentyrru elfennau hanner ton uwchben ei gilydd:
po fwyaf mae'n eu pentyrru, uchaf yw'r cynnydd. Gwasga'r un signal i hanner
y gofod ac mae'n ddwywaith mor gryf yno: 3 dB. I chwarter, ac mae'n 4 gwaith
mor gryf: 6 dB. Mae gwneuthurwyr yn nodi cynnydd mewn dBi; mae'r terfyn
cyfreithiol yn cyfrif mewn dBd, gwela [O fewn y terfyn cyfreithiol](#legal).

### Pa gynnydd i dy safle di {#choose-gain}

- **Bryniau, dyffrynnoedd neu ddinas ddwys: tua 3 dBi.** Mae'r paladr tal yn
  cyrraedd nodau uwch dy ben ac oddi tanat, ac o amgylch y llethrau a'r adeiladau
  sydd yn y ffordd. Mae hefyd yn gweithio'r ffordd arall: o ddyffryn, mae paladr
  fflat yn pasio o dan ailadroddydd ar y bryn uwchben. Un enghraifft yw'r
  RAKwireless RAKARG12: tiwb gwydr ffibr 36 cm.
- **Maestrefi neu dref â thoeau isel: 5 i 6 dBi.** Y colinear gwydr ffibr arferol.
- **Tir gwastad, agored: 8 i 10 dBi.** Y paladr mwyaf fflat sy'n cyrraedd
  bellaf ar hyd y gorwel. Wedi'i osod yn uchel, mae'n pasio dros y nodau gerllaw.

Y cynnydd yn yr enw yw'r ffigur gorau ar draws band cyfan yr antena. Mae gan y
RAKARG12, sydd ar werth fel 3 dBi, 2.8 dBi ar 865 i 870 MHz. Darllena'r tabl
cynnydd yn y daflen ddata ar amledd dy ragosodiad.

Uwchben 7 dBi mae bwrdd 22 dBm yn mynd dros y terfyn cyfreithiol, oni bai bod
colled cebl a hidlydd yn gwneud iawn am y gwahaniaeth. Gostynga'r pŵer trosglwyddo
i gyd-fynd â hynny.

Dim ond pan wyt ti'n gwybod ble mae'r nodau y mae cynnydd uchel yn helpu: ar hyd y
gorwel o amgylch ailadroddydd, neu at un ailadroddydd pell gyda Yagi. Mae
cydymaith yn dy law yn pwyntio i bob cyfeiriad, felly y cynnydd isel a ddaeth
gydag ef sydd orau iddo.

## Pam yn fertigol {#vertical}

Mae antenâu yn clywed ei gilydd orau pan fyddan nhw'n pwyntio'r un ffordd. Mae'r
golled yn tyfu gyda'r ongl rhyngddyn nhw: mae 45 gradd yn costio 3 dB, hanner dy
signal. Ar 90 gradd, antena fflat yn erbyn un syth, does dim yn cyrraedd mewn
theori. Mae'r rhwydwaith mesh yn sefyll yn syth, felly mae dy antena di'n sefyll
yn syth hefyd. Mae hyn hefyd yn wir am gydymaith ar ddesg: gosoda fe'n fflat ac
mae pob nod o dy gwmpas yn clywed llai.

## Cysylltwyr {#connectors}

Archeba'r antena gyda'r cysylltydd sydd ar dy fwrdd. Mae pob addasydd yn un uniad
arall i'w selio ac yn golygu colli mwy o signal.

- **SMA.** Cysylltydd ag edau, tua 6 mm o led. Mae gan y soced ar y rhan fwyaf o
  fyrddau dwll yn y canol; mae'r pin ar yr antena. Mae cysylltydd o'r math hwn yn
  colli tua 0.03 dB ar 868 MHz.
- **RP-SMA.** Yr un corff ac edau ag SMA, gyda'r pin a'r twll wedi'u cyfnewid.
  Mae'n edrych fel SMA, ond dydy'r ddau ddim yn cysylltu. Gwiria pa un sydd ar dy
  fwrdd cyn i ti archebu.
- **U.FL (IPEX).** Soced gwthio bach iawn ar y bwrdd ei hun. Mae cebl pigtail byr
  yn rhedeg ohono i soced SMA yn y cas. Mae wedi'i raddio ar gyfer 30 cylch
  cysylltu, felly cysyllta fe unwaith a gad lonydd iddo.
- **N.** Y cysylltydd mawr ag edau ar antenâu gwydr ffibr a chebl trwchus. Mae'n
  colli 0.05 dB ar y mwyaf. Mae angen un addasydd neu bigtail o N i SMA y bwrdd ar
  ailadroddydd.

## Colled cebl {#cable}

Mae cebl yn costio signal cyn iddo adael yr antena, i'r ddau gyfeiriad. Mae 3 dB
yn hanner dy bŵer. Ffigurau'r gwneuthurwyr y metr, ar 868 i 900 MHz:

| Cebl | Colled y metr | Colled dros 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

Mae 3 metr o RG174, y pigtail tenau a ddaw gyda llawer o fyrddau, yn colli hanner
dy bŵer. Gosoda'r bwrdd wrth yr antena gyda phigtail byr, neu rheda gebl trwchus
ato. Ychwanega bob addasydd a hidlydd ar y llwybr at y swm.

## Hidlyddion {#filters}

Mae hidlydd yn mynd rhwng y radio a'r antena. Mae'n gadael dy fand drwodd ac yn
rhwystro'r gweddill, felly dydy trosglwyddydd cryf gerllaw ddim yn boddi'r derbynnydd.
Mae angen un arnat ti pan fydd nod yn clywed llai nag y dylai ger trosglwyddyddion
eraill. Mae ailadroddydd ar fast gyda gorsafoedd sylfaen ffonau symudol yn nod o'r
fath. Mae hidlydd yn costio signal i'r ddau gyfeiriad: cyfra ei golled fel colled cebl.

| | Hidlydd SAW | Hidlydd ceudod |
|---|---|---|
| Maint | Ychydig filimetrau, ar fwrdd bach | Bloc neu diwb metel |
| Colled un da | dan 2 dB | dan 1 dB |
| Uchafswm pŵer mewnbwn un da | 500 mW | sawl wat |

Mae'r sysmocom cf866.5-kt30, er enghraifft, yn hidlydd ceudod ar gyfer 863 i
870 MHz sy'n colli 1.0 dB ar y mwyaf ac yn gallu cymryd 30 W. Mae wedi'i wneud i'w
ddefnyddio dan do, felly rho fe mewn blwch wedi'i selio ar fast.

Mae hidlyddion yn amrywio llawer, felly gwiria'r daflen ddata cyn i ti brynu. Rhaid
i'w bŵer mewnbwn graddedig fod yn uwch na dy bŵer trosglwyddo, a rhaid i'w fand
pasio gynnwys amledd dy ragosodiad.

## Gosod {#mounting}

- **Uwchben ymyl y to.** Mae angen golygfa glir ar yr antena i bob cyfeiriad mae'n ei
  wasanaethu. Mae hyd yn oed ychydig fetrau uwchben y toeau o gwmpas yn helpu. Mae
  [Dewis safle](/repeater-guide/#site) yn y canllaw ailadroddydd yn dangos sut i
  wirio'r olygfa.
- **I ffwrdd o fetel.** Mae cwteri, mastiau, antenâu eraill a thoeau metel wrth
  ymyl yr antena yn newid ei batrwm a'i diwnio. Gosoda fe ar ben y mast, nid wrth
  ei ochr.
- **Yn syth i fyny.** Defnyddia lefel wirod; gwela [Pam yn fertigol](#vertical).
- **Dolen ddiferu.** Gad i'r cebl hongian o dan y cysylltydd cyn iddo fynd i fyny
  neu i mewn. Yna mae dŵr yn diferu i ffwrdd yn lle rhedeg i mewn i'r uniad.
- **Selia bob cysylltydd awyr agored.** Mae dŵr mewn cysylltydd yn codi'r golled
  ac yn cyrydu'r pin. Selia fe rhag glaw a gwiria'r sêl bob blwyddyn.
- **Mellt.** Mae antena ar do yn darged. Mae arestiwr rhyddhau nwy yn y cebl yn
  tanio pan ddaw ymchwydd ac yn ei anfon i'r ddaear. Dilyna
  [Caledwedd](/repeater-guide/#hardware) yn y canllaw ailadroddydd a dy reolau
  lleol ar gyfer daearu.

## O fewn y terfyn cyfreithiol {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
Yn Ewrop mae MeshCore yn defnyddio'r is-fand 869.40-869.65 MHz, gydag uchafswm o
**500 mW** o bŵer pelydrol effeithiol (e.r.p.). Mae'r terfyn yn cyfrif yr hyn sy'n
gadael yr antena: mae cynnydd antena yn adio, mae colled cebl a hidlydd yn tynnu.
Mae cynnydd mewn dBi yn cyfrif 2.15 dB yn llai, oherwydd bod y terfyn yn cael ei
fesur yn erbyn deupol.
{{< /callout >}}

Mae colinear 5.8 dBi ar fwrdd 22 dBm yn aros o fewn y terfyn. Dydy'r un antena ar
fwrdd ag amplifydd ddim, nes i ti ostwng y pŵer trosglwyddo. Mae
[Pŵer: e.r.p. a dy antena](/repeater-guide/#erp) yn y canllaw ailadroddydd yn rhoi'r
swm a 2 enghraifft wedi'u cyfrifo.

## Gwirio antena gyda NanoVNA {#nanovna}

Dadansoddwr rhwydwaith fector maint poced yw NanoVNA. Mae'n dangos ar ba amledd mae
antena wedi'i diwnio, felly rwyt ti'n gwybod cyn i ti ei osod. Mae'r NanoVNA-H yn
mesur hyd at 1.5 GHz, sy'n cynnwys 868 MHz.

1. Calibrada fe ar gyfer 800 i 950 MHz gyda'r darnau open, short a load o'i becyn.
2. Cysyllta'r antena trwy'r addasydd y bydd yn ei ddefnyddio ar y nod. Dal fe'n syth
   i fyny ac i ffwrdd o dy gorff a'r bwrdd.
3. Darllena gromlin SWR (cymhareb tonnau sefydlog): mae'n dangos faint o signal mae'r
   antena yn ei anfon yn ôl. Rhaid i'r pant fod ar amledd dy ragosodiad, 869.618 MHz
   ar gyfer EU/UK (Narrow). Mae pant gannoedd o MHz i ffwrdd yn golygu bod yr antena
   wedi'i wneud ar gyfer band arall.

Mae chwarter ton ar 868 MHz yn 86 mm (345 mm yw'r donfedd). Dydy'r hyd ar ei ben ei
hun ddim yn dweud y band wrthyt ti, oherwydd bod gwneuthurwyr yn plygu ac yn llwytho
chwipiau; mae'r NanoVNA yn dweud.

## Ffynonellau {#sources}

- Colled cebl: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  taflen ddata Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  taflenni data Times Microwave LMR-240 a LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antenâu: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  taflen ddata Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Cynnydd fel signal wedi'i wasgu i lai o ofod: [RF Cafe, cyflwyniad i antenâu](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Cysylltwyr: taflenni data Rosenberger 32S102 (SMA) a 53S101 (N), catalog Hirose U.FL.
- Hidlyddion: tudalen gynnyrch sysmocom cf866.5-kt30,
  [arestwyr rhyddhau nwy Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Colled polareiddiad: [Prifysgol Toronto, effeithiau Friis](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Cynnydd deupol yn ôl hyd: [Wikipedia, antena deupol](https://en.wikipedia.org/wiki/Dipole_antenna).
- Tonfedd: buanedd golau gan [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Terfyn cyfreithiol: [Argymhelliad CEPT ERC 70-03](https://docdb.cept.org/document/845),
  Atodiad 1, band h1.7; mae'r [canllaw ailadroddydd](/repeater-guide/#legal) yn rhestru'r
  gweddill.
