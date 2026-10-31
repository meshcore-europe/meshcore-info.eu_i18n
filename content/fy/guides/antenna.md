---
title: Antennegids
lead: De goede antenne, goed monteard, rikt fierder as mear fermogen. Kontrolearje de antenne op dyn companion, en kies, ferbyn en montearje dan ien foar in repeater.
description: 'In MeshCore-antenne foar 868 MHz kieze en montearje: in companion-sprút kontrolearje, antennetypen en winst, konnektors, kabelferlies per meter, filters, montaazje en hoe''t winst meitelt foar de wetlike limyt.'
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

Hichte, in ôfstimde antenne en in koarte kabel jouwe mear berik as hokker ekstra
milliwatt ek. Dizze gids begjint by de companion, de radio dêr't do mei
berjochtest. Dêrnei komt de antenne op in repeater oan bod: in node dy't
berjochten fan in dak of mêst ôf trochjout.

## Dyn companion {#companion}

{{< callout type="warning" >}}
Set de antenne derop foardatsto de radio oansetst. In LoRa-radio dy't
sûnder antenne útstjoert, kin syn eigen chip skansearje.
{{< /callout >}}

De antenne dy't by dyn board siet, docht wat er dwaan moat. Set him derop, hâld
de node rjochtop en begjin mei berjochtsjen. In bettere
antenne op in companion wint net folle. In repeater binnen berik wint in protte.

Keapje allinnich in losse sprút as de meilevere stikken is of ûntbrekt. Net
elke sprút dy't foar 868 MHz ferkocht wurdt, is dêrop ôfstimd. [Kontrolearje him mei in
NanoVNA](#nanovna), in antenne-analyzer yn bûsformaat, foardatsto him fertroust. Of lien ien fan in board dat
wurket.

In node njonken in sterke stjoerder heart minder as er hearre moat. In lyts
[SAW-filter (surface acoustic wave)](#filters) tusken de radio en de
antenne hâldt dy stjoerder út de ûntfanger. Sjoch earst yn it datasheet:

- **Maksimaal ynfierfermogen.** It filter sit ek yn it paad fan dyn eigen
  útstjoering. As in board 22 dBm (160 mW) stjoert yn in filter foar 15 dBm,
  giet it filter stikken.
- **Trochlitbân.** Dy moat de frekwinsje fan dyn preset befetsje. In filter foar
  868.65 oant 869.25 MHz lit it EU/UK (Narrow)-kanaal op
  869.618 MHz net troch.

## Antennetypen foar in repeater {#types}

Elke antenne op it mesh stiet rjochtop. Kies it type nei it plak dêr't de nodes
steane dy'tsto berikke wolst:

- **Glêsfiber-collinear.** In wite buis op in mêst, mei winst rûnom
  oan 'e kim. De standertkar foar in repeater dy't in stêd betsjinnet.
- **Dipoal.** Koarter, mei minder winst en in hege bondel. Hy berikt nodes
  ûnder en boppe dy better as in collinear, bygelyks fan in heuvel
  boppe in delling.
- **Yagi.** In boom mei dwerselemininten, rjochte op ien plak. Hy berikt in
  inkele fiere repeater en amper wat oars. Montearje him mei de elemininten rjochtop,
  want syn polarisaasje folget de elemininten.

## Winst en de bondel {#gain}

Winst foeget gjin fermogen ta. Winst nimt it sinjaal dat omheech en omleech
gean soe, en stjoert it lâns de kim. Lykas in bûslampe dy'tsto skerpstelst: deselde batterij,
in langere en smellere bondel. In dipoal en in collinear fan deselde makker
litte it sjen:

| Antenne | Winst | Fertikale bondelbreedte |
|---|---|---|
| Dipoal (Sirio SO 868-915-2) | 2.2 dBi | 88 graden |
| Glêsfiber-collinear (Sirio SPO 868-915-6) | 5.8 dBi | 23 graden |

{{< gain >}}

It diagram is in trochsneed troch de mêst, fan 'e kant sjoen. Draaisto it om de
mêst, dan hasto de hiele bondel: in donut foar de dipoal, in platte skiif
foar de collinear. In rjochtopsteande antenne stjoert yn elke rjochting om him hinne
itselde. Bûten de tekene bondel hâldt it sinjaal net op. It is swakker, mar
noch genôch foar in node tichteby.

Op in dak wolsto in platte bondel. Op in heuvel heech boppe de nodes
giet in bondel fan 23 graden oer harren hollen hinne. In dipoal dekt se wol. In Yagi
giet hjir noch fierder yn: 16.6 dBi yn in bondel fan 23 graden heech
en 25 graden breed (Amphenol Procom
7176870), en neat nei de kanten.

Winst mjitsto tsjin in referinsje. dBi fergeliket mei in ideale antenne dy't
yn elke rjochting gelyk stjoert. dBd fergeliket mei in heale-golf-dipoal,
dy't sels 2.15 dBi hat: sels de ienfâldichste antenne stjoert neat rjocht
omheech of omleech. In langere dipoal, fan 1.25 golflingten, komt op 5.2 dBi. In collinear
stapelet ynstee heale-golf-elemininten boppe-inoar: hoe mear er stapelet, hoe
heger de winst. Parsto itselde sinjaal yn de helte fan de romte, dan is it dêr
twa kear sa sterk: 3 dB. Yn in kwart is it 4 kear sa sterk: 6 dB.
Makkers jouwe winst yn dBi. De wetlike limyt telt yn dBd, sjoch
[Binnen de wetlike limyt](#legal).

### Hokker winst foar dyn lokaasje {#choose-gain}

- **Heuvels, dellingen of in tichte stêd: sawat 3 dBi.** De hege bondel berikt
  nodes boppe en ûnder dy, en om de hellingen en gebouwen hinne dy't yn 'e wei steane.
  It wurket ek oarsom: út in delling giet in platte bondel ûnder in
  repeater op 'e heuvel boppe dy troch. De RAKwireless RAKARG12 is sa'n antenne: in
  glêsfiberbuis fan 36 cm.
- **Bûtenwiken of in stêd mei lege dakken: 5 oant 6 dBi.** De standert
  glêsfiber-collinear.
- **Flak, iepen lân: 8 oant 10 dBi.** De platste bondel rikt it fierst
  lâns de kim. Heech monteard giet er oer de nodes tichteby hinne.

De winst yn 'e namme is it bêste sifer oer de hiele bân fan de antenne.
De RAKARG12, ferkocht as 3 dBi, hat 2.8 dBi by 865 oant 870 MHz. Lês de winsttabel
yn it datasheet by de frekwinsje fan dyn preset.

Boppe 7 dBi giet in board fan 22 dBm oer de wetlike limyt, útsein as kabel- en filterferlies
it ferskil goedmeitsje. Ferleegje it stjoerfermogen dan dêrop.

Hege winst helpt allinnich asto witst wêr't de nodes binne: lâns de kim
om in repeater hinne, of by ien fiere repeater foar in Yagi. In companion yn dyn hân
wiist alle kanten út, dus de lege winst dêr't er mei kaam, past him it bêste.

## Wêrom fertikaal {#vertical}

Antennes hearre inoar it bêste as se deselde kant út wize. It ferlies groeit
mei de hoeke tusken harren: 45 graden kostet 3 dB, de helte fan dyn sinjaal. By
90 graden, in platte antenne tsjin in rjochtopsteande, komt der yn teory neat
oan. It mesh stiet rjochtop, dus dyn antenne ek. Dat jildt ek
foar in companion op in buro: lizt er plat, dan heart elke node om dy hinne
minder.

## Konnektors {#connectors}

Bestel de antenne mei de konnektor
dy't dyn board hat. Elke adapter is in ferbining mear om ôf te sluten, en mear
sinjaal dat ferlern giet.

- **SMA.** In skroefkonnektor fan sawat 6 mm breed. De bus op de measte boards
  hat in gatsje yn it midden. De antenne hat de pin. In konnektor fan dit
  soarte ferliest sawat 0.03 dB by 868 MHz.
- **RP-SMA.** Itselde lichem en deselde skroefdraad as SMA, mei de pin en it gatsje
  omwiksele. Hy liket op SMA en past der net op. Sjoch hokker
  dyn board hat, foardatsto bestelst.
- **U.FL (IPEX).** In lytse drukbus op it board sels. In koarte
  pigtailkabel rint dêrfan nei in SMA-bus yn de kast. De bus is makke foar
  30 kear oan- en loskeppeljen. Ferbyn him dus ien kear en lit him sitte.
- **N.** De grutte skroefkonnektor op glêsfiberantennes en dikke
  kabel. Hy ferliest op syn heechst 0.05 dB. In repeater hat ien
  adapter of pigtail fan N nei de SMA fan it board nedich.

## Kabelferlies {#cable}

Kabel kostet sinjaal foardat it de antenne ferlit, yn beide rjochtingen. 3 dB
is de helte fan dyn fermogen. De sifers fan de makkers per meter, by 868 oant 900 MHz:

| Kabel | Ferlies per meter | Ferlies oer 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 meter RG174, de tinne pigtail dy't by in protte boards sit, kostet de helte
fan dyn fermogen. Montearje it board by de antenne mei in koarte pigtail, of
lis dikke kabel dêrhinne. Tel elke adapter en elk filter yn it paad by de som op.

## Filters {#filters}

In filter sit tusken de radio en de antenne. It lit dyn bân troch en
hâldt de rest tsjin. Sa oerstimmet in sterke stjoerder tichteby de ûntfanger net.
Do hast ien nedich as in node minder heart as er moat, tichteby oare
stjoerders. In repeater op in mêst mei basisstasjons foar mobile tillefoans is sa'n
node. In filter kostet sinjaal yn beide rjochtingen: tel syn ferlies lykas
kabel.

| | SAW-filter | Holteresonatorfilter |
|---|---|---|
| Grutte | In pear millimeter, op in lyts board | In metalen blok of buis |
| Ferlies fan in goed filter | ûnder 2 dB | ûnder 1 dB |
| Maksimaal ynfierfermogen fan in goed filter | 500 mW | ferskate watt |

De sysmocom cf866.5-kt30 bygelyks is in holteresonatorfilter foar 863 oant
870 MHz dat op syn heechst 1.0 dB ferliest en 30 W ferdraacht. It is makke foar binnen,
dus set it op in mêst yn in wetterticht kastje.

Filters ferskille in protte, dus sjoch yn it datasheet foardatsto keapest. It
ynfierfermogen dêr't it filter foar makke is, moat heger wêze as dyn stjoerfermogen. De trochlitbân moat
de frekwinsje fan dyn preset befetsje.

## Montaazje {#mounting}

- **Boppe de dakrâne.** De antenne hat frij sicht nedich yn elke
  rjochting dy't er betsjinnet. Sels in pear meter boppe de dakken der omhinne
  helpt. Yn [Kies in lokaasje](/repeater-guide/#site) yn de repeatergids
  sjochsto hoe'tsto it sicht kontrolearrest.
- **Fuort fan metaal.** Dakgoaten, mêsten, oare antennes en metalen dakken
  njonken de antenne feroarje syn patroan en ôfstimming. Montearje him boppe op de
  mêst, net dernjonken.
- **Rjochtop.** Brûk in wetterpas, sjoch [Wêrom fertikaal](#vertical).
- **Drippelbôge.** Lit de kabel ûnder de konnektor hingje foardat er omheech
  of nei binnen giet. It wetter drippet dan ôf en rint net yn de ferbining.
- **Slút elke konnektor bûten wetterticht ôf.** Wetter yn in konnektor fergruttet it ferlies
  en lit de pin roastje. Slút him ôf tsjin rein en kontrolearje de ôfsluting alle jierren.
- **Wjerljocht.** In antenne op in dak is in doelwyt. In gasûntladingsôflieder
  yn de kabel giet by in oerspanning oan en liedt dy nei de ierde. Folgje
  [Hardware](/repeater-guide/#hardware) yn de repeatergids en dyn pleatslike
  regels foar it ierden.

## Binnen de wetlike limyt {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
Yn Europa brûkt MeshCore de subbân 869.40-869.65 MHz, mei op syn heechst
**500 mW** effektyf útstrielle fermogen (e.r.p.). De limyt telt wat de antenne ferlit:
antennewinst komt der by, kabel- en filterferlies gean der ôf. Winst yn dBi telt
2.15 dB minder, om't de limyt tsjin in dipoal mjitten wurdt.
{{< /callout >}}

In collinear fan 5.8 dBi op in board fan 22 dBm bliuwt binnen de limyt. Deselde
antenne op in board mei in fersterker docht dat net, oant do it stjoerfermogen
ferleegest. Yn [Fermogen: e.r.p. en dyn antenne](/repeater-guide/#erp) yn de
repeatergids stiet de som mei 2 útwurke foarbylden.

## In antenne kontrolearje mei in NanoVNA {#nanovna}

In NanoVNA is in vector network analyzer yn bûsformaat. Dêrmei sjochsto op hokker
frekwinsje in antenne ôfstimd is, dus do witst it foardatsto him montearrest. De
NanoVNA-H mjit oant 1.5 GHz, en dat dekt 868 MHz.

1. Kalibrearje him foar 800 oant 950 MHz mei de stikken foar iepen, koartsluting en lading
   út syn kit.
2. Ferbyn de antenne fia de adapter dy'tsto op de node brûkst. Hâld him
   rjochtop en fuort fan dyn lichem en de tafel.
3. Lês de SWR-kromme (standing wave ratio) ôf: dy lit sjen hoefolle sinjaal
   de antenne weromstjoert. De dip moat op de frekwinsje fan dyn preset lizze, 869.618
   MHz foar EU/UK (Narrow). In dip hûnderten MHz derneist betsjut dat de antenne
   foar in oare bân makke is.

In kwartgolf by 868 MHz is 86 mm (de golflingte is 345 mm). De lingte
allinnich fertelt dy de bân net, want makkers falde en laden sprúten. De
NanoVNA fertelt it dy wol.

## Boarnen {#sources}

- Kabelferlies: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  it datasheet fan de Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  de datasheets fan Times Microwave LMR-240 en LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antennes: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  it datasheet fan de Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Winst as sinjaal yn minder romte parst: [RF Cafe, antenna introduction](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Konnektors: de datasheets fan Rosenberger 32S102 (SMA) en 53S101 (N), de
  U.FL-katalogus fan Hirose.
- Filters: de produktside fan de sysmocom cf866.5-kt30,
  [Citel gasûntladingsôflieders](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarisaasjeferlies: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipoalwinst neffens lingte: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Golflingte: ljochtsnelheid fan [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Wetlike limyt: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Annex 1, bân h1.7. De [repeatergids](/repeater-guide/#legal) neamt de
  rest.
