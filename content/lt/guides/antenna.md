---
title: Antenų vadovas
lead: Tinkama ir gerai sumontuota antena pasiekia toliau nei didesnė galia. Patikrink savo companion anteną, tada kartotuvui pasirink, prijunk ir sumontuok tinkamą anteną.
description: 'Kaip pasirinkti ir sumontuoti MeshCore anteną 868 MHz dažniui: companion strypinės antenos patikra, antenų tipai ir stiprinimas, jungtys, kabelio nuostoliai metrui, filtrai, montavimas ir stiprinimo įtaka teisinei ribai.'
eyebrow: Companion ir kartotuvas · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-11-02'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Aukštis, suderinta antena ir trumpas kabelis duoda daugiau nuotolio nei bet
kuris papildomas milivatas. Šiame vadove pradedame nuo companion, radijo, iš
kurio rašai žinutes. Paskui aptariame kartotuvo anteną. Kartotuvas yra mazgas,
kuris nuo stogo ar stiebo perduoda žinutes toliau.

## Tavo companion {#companion}

{{< callout type="warning" >}}
Pirma prijunk anteną, tik tada įjunk radiją. LoRa radijas, siųsdamas be
antenos, gali sugadinti savo paties lustą.
{{< /callout >}}

Antenos, kurią gavai su plokšte, pakanka. Prijunk ją, laikyk mazgą
vertikaliai ir pradėk rašyti žinutes. Geresnė companion antena duoda
nedaug, o kartotuvas pasiekiamu atstumu duoda labai daug.

Atskirą strypinę anteną pirk tik tada, kai gautoji sugedusi arba jos nėra. Ne
kiekviena 868 MHz dažniui parduodama strypinė antena tam dažniui suderinta.
Prieš pasitikint ja, [patikrink ją su NanoVNA](#nanovna), kišeniniu antenų
analizatoriumi, arba pasiskolink anteną nuo veikiančios plokštės.

Šalia stipraus siųstuvo mazgas girdi prasčiau, nei turėtų. Mažas
[SAW (paviršinių akustinių bangų) filtras](#filters) tarp radijo ir antenos
neįleidžia to siųstuvo signalo į imtuvą. Pirma patikrink filtro techninius
duomenis:

- **Didžiausia įėjimo galia.** Pro filtrą eina ir tavo paties siunčiamas
  signalas. Jei plokštė siunčia 22 dBm (160 mW) į filtrą, skirtą 15 dBm,
  filtras sugenda.
- **Praleidžiamoji juosta.** Ji turi apimti tavo profilio dažnį. Filtras,
  skirtas 868.65–869.25 MHz, nepraleidžia EU/UK (Narrow) kanalo, kurio dažnis
  869.618 MHz.

## Kartotuvo antenų tipai {#types}

Visos tinklo antenos stovi vertikaliai. Tipą rinkis pagal tai, kur yra mazgai,
kuriuos nori pasiekti:

- **Stiklo pluošto kolinearinė antena.** Tai baltas vamzdis ant stiebo, o jo
  stiprinimas tolygus visame horizonte. Tai įprastas pasirinkimas kartotuvui,
  kuris aptarnauja miestą.
- **Dipolis.** Jis trumpesnis, jo stiprinimas mažesnis, o spindulys aukštas.
  Žemiau ir aukščiau tavęs esančius mazgus jis pasiekia geriau nei kolinearinė
  antena, pavyzdžiui, nuo kalvos virš slėnio.
- **Yagi.** Tai strypas su skersiniais elementais, nukreiptas į vieną vietą. Ši
  antena pasiekia vieną tolimą kartotuvą ir beveik nieko daugiau. Montuok ją
  taip, kad elementai stovėtų vertikaliai, nes poliarizacija priklauso nuo
  elementų krypties.

## Stiprinimas ir spindulys {#gain}

Stiprinimas nepadidina galios. Antena paima signalą, kuris eitų aukštyn ir
žemyn, ir nukreipia jį išilgai horizonto. Tai kaip sufokusuotas žibintuvėlis:
baterija ta pati, o spindulys ilgesnis ir siauresnis. Tai matyti palyginus to
paties gamintojo dipolį ir kolinearinę anteną:

| Antena | Stiprinimas | Vertikalus spindulio plotis |
|---|---|---|
| Dipolis (Sirio SO 868-915-2) | 2.2 dBi | 88 laipsniai |
| Stiklo pluošto kolinearinė antena (Sirio SPO 868-915-6) | 5.8 dBi | 23 laipsniai |

{{< gain >}}

Diagrama rodo pjūvį per stiebą, matomą iš šono. Pasuk ją aplink stiebą ir
pamatysi visą spindulį: dipolio spindulys primena spurgą, o kolinearinės
antenos spindulys yra plokščias diskas. Vertikali antena siunčia vienodai į
visas puses aplink save. Už nubraižyto spindulio ribų signalas nedingsta: jis
silpnesnis, bet artimam mazgui jo vis tiek pakanka.

Ant stogo tau reikia plokščio spindulio. Ant kalvos, aukštai virš mazgų,
23 laipsnių spindulys praeina jiems virš galvų, o dipolis juos padengia. Yagi
antena šiuo keliu eina dar toliau: 16.6 dBi spindulyje, kurio aukštis 23 laipsniai,
o plotis 25 laipsniai (Amphenol Procom 7176870), ir nieko į šonus.

Stiprinimas skaičiuojamas lyginant su atskaitos antena. dBi lygina su idealia antena,
kuri siunčia vienodai į visas puses. dBd lygina su pusės bangos dipoliu, kurio
paties stiprinimas yra 2.15 dBi: net paprasčiausia antena nesiunčia nieko tiesiai
aukštyn ar žemyn. Ilgesnis 1.25 bangos ilgio dipolis pasiekia 5.2 dBi. Kolinearinė
antena vietoj to išdėsto pusės bangos elementus vieną virš kito: kuo jų daugiau,
tuo didesnis stiprinimas. Suspausk tą patį signalą į perpus mažesnę erdvę, ir ten
jis bus dvigubai stipresnis: 3 dB. Suspausk į ketvirtadalį, ir jis bus 4 kartus
stipresnis: 6 dB. Gamintojai stiprinimą nurodo dBi, o teisinė riba skaičiuojama
dBd, žr. [Neviršyk teisinės ribos](#legal).

### Koks stiprinimas tinka tavo vietai {#choose-gain}

- **Kalvos, slėniai ar tankus miestas: maždaug 3 dBi.** Aukštas spindulys
  pasiekia mazgus virš tavęs ir žemiau tavęs, taip pat apeina kelyje esančius
  šlaitus ir pastatus. Tai veikia ir atvirkščiai: iš slėnio plokščias spindulys
  praeina po kartotuvu, kuris stovi ant kalvos virš tavęs. Tokia antena yra
  RAKwireless RAKARG12, 36 cm stiklo pluošto vamzdis.
- **Priemiesčiai ar miestas su žemais stogais: 5–6 dBi.** Tai įprasta stiklo
  pluošto kolinearinė antena.
- **Lygi, atvira vietovė: 8–10 dBi.** Plokščiausias spindulys išilgai horizonto
  pasiekia toliausiai. Aukštai sumontuotas, jis praeina virš artimų mazgų.

Pavadinime nurodytas stiprinimas yra geriausias rodiklis visoje antenos juostoje.
RAKARG12 parduodama kaip 3 dBi antena, bet 865–870 MHz juostoje jos stiprinimas
yra 2.8 dBi. Techninių duomenų stiprinimo lentelėje žiūrėk vertę ties savo
profilio dažniu.

Kai stiprinimas didesnis nei 7 dBi, 22 dBm plokštė viršija teisinę ribą, nebent
skirtumą kompensuoja kabelio ir filtro nuostoliai. Atitinkamai sumažink siuntimo
galią.

Didelis stiprinimas padeda tik tada, kai žinai, kur yra mazgai: išilgai horizonto
aplink kartotuvą arba, Yagi atveju, ties vienu tolimu kartotuvu. Tavo rankoje
esantis companion būna nukreiptas į visas puses, todėl jam geriausiai tinka mažo
stiprinimo antena, su kuria jį gavai.

## Kodėl vertikaliai {#vertical}

Antenos geriausiai girdi viena kitą, kai yra nukreiptos ta pačia kryptimi.
Nuostoliai didėja kartu su kampu tarp jų: 45 laipsnių kampas atima 3 dB, pusę tavo
signalo. Esant 90 laipsnių, kai viena antena gulsčia, o kita vertikali, teoriškai
neatkeliauja nieko. Tinklo antenos stovi vertikaliai, tad taip turi stovėti ir
tavoji. Tai galioja ir companion ant stalo: paguldyk jį, ir visi aplinkiniai
mazgai girdės prasčiau.

## Jungtys {#connectors}

Užsisakyk anteną su tokia jungtimi, kokią turi tavo plokštė. Kiekvienas
adapteris reiškia dar vieną jungtį, kurią reikia sandarinti, ir papildomus signalo
nuostolius.

- **SMA.** Tai maždaug 6 mm pločio srieginė jungtis. Daugumos plokščių lizdo
  centre yra skylutė, o antena turi kaištį. Tokio tipo jungtis ties 868 MHz
  praranda maždaug 0.03 dB.
- **RP-SMA.** Korpusas ir sriegis tokie patys kaip SMA, tik kaištis ir skylutė
  sukeisti vietomis. Ji atrodo kaip SMA, bet su ja nesusijungia. Prieš užsakant
  patikrink, kurią jungtį turi tavo plokštė.
- **U.FL (IPEX).** Tai mažytis užspaudžiamas lizdas ant pačios plokštės. Nuo jo
  trumpas pigtail kabelis eina iki SMA lizdo korpuse. Jungtis skirta 30 sujungimo
  ciklų, tad prijunk ją vieną kartą ir nebeliesk.
- **N.** Tai didelė srieginė jungtis ant stiklo pluošto antenų ir storo kabelio.
  Ji praranda ne daugiau kaip 0.05 dB. Kartotuvui reikia vieno adapterio arba
  pigtail kabelio nuo N iki plokštės SMA.

## Kabelio nuostoliai {#cable}

Kabelis atima signalo dar prieš jam paliekant anteną, ir abiem kryptimis.
3 dB yra pusė tavo galios. Gamintojų duomenys vienam metrui, ties 868–900 MHz:

| Kabelis | Nuostoliai metrui | Nuostoliai per 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metrai RG174 (tai plonas pigtail kabelis, kurį gauni su daugeliu plokščių) atima
pusę tavo galios. Sumontuok plokštę prie antenos su trumpu pigtail kabeliu arba
nutiesk iki antenos storą kabelį. Į sumą įtrauk kiekvieną kelyje esantį adapterį
ir filtrą.

## Filtrai {#filters}

Filtras yra tarp radijo ir antenos. Jis praleidžia tavo juostą ir blokuoja
visa kita, todėl stiprus artimas siųstuvas neužgožia imtuvo. Filtro tau reikia, kai
mazgas šalia kitų siųstuvų girdi prasčiau, nei turėtų. Toks mazgas yra kartotuvas
ant stiebo su mobiliojo ryšio bazinėmis stotimis. Filtras atima signalo abiem
kryptimis: jo nuostolius skaičiuok kaip kabelio.

| | SAW filtras | Ertminis filtras |
|---|---|---|
| Dydis | Keli milimetrai, ant mažos plokštės | Metalinis blokas arba vamzdis |
| Gero filtro nuostoliai | mažiau nei 2 dB | mažiau nei 1 dB |
| Gero filtro didžiausia įėjimo galia | 500 mW | keli vatai |

Pavyzdžiui, sysmocom cf866.5-kt30 yra ertminis filtras 863–870 MHz juostai. Jis
praranda daugiausia 1.0 dB ir atlaiko 30 W. Jis skirtas naudoti patalpose, tad ant
stiebo dėk jį į sandarią dėžutę.

Filtrai labai skiriasi, tad prieš perkant patikrink techninius duomenis. Nurodyta
įėjimo galia turi viršyti tavo siuntimo galią, o praleidžiamoji juosta turi apimti
tavo profilio dažnį.

## Montavimas {#mounting}

- **Virš stogo krašto.** Antenai reikia laisvo matomumo į kiekvieną aptarnaujamą
  pusę. Net keli metrai virš aplinkinių stogų jau padeda. Kaip patikrinti
  matomumą, rasi kartotuvo vadovo skyriuje [Pasirink vietą](/repeater-guide/#site).
- **Toliau nuo metalo.** Lietvamzdžiai, stiebai, kitos antenos ir metaliniai
  stogai šalia antenos keičia jos spinduliuotės diagramą ir suderinimą. Montuok ją
  ant stiebo viršaus, ne šalia jo.
- **Vertikaliai.** Naudok gulsčiuką, žr. [Kodėl vertikaliai](#vertical).
- **Lašėjimo kilpa.** Leisk kabeliui nusvirti žemiau jungties, prieš jam kylant
  aukštyn ar einant į vidų. Tada vanduo nulaša, o ne teka į jungtį.
- **Sandarink kiekvieną lauko jungtį.** Jungtyje esantis vanduo didina nuostolius
  ir ėda kaištį. Užsandarink ją nuo lietaus ir kasmet tikrink sandarinimą.
- **Žaibas.** Antena ant stogo yra taikinys. Kabelyje įtaisytas dujinis iškroviklis
  suveikia per viršįtampį ir nukreipia jį į įžeminimą. Dėl įžeminimo vadovaukis
  kartotuvo vadovo skyriumi [Įranga](/repeater-guide/#hardware) ir vietinėmis
  taisyklėmis.

## Neviršyk teisinės ribos {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
Europoje MeshCore naudoja 869.40-869.65 MHz pajuostę, kurioje efektyvioji
spinduliuojamoji galia (e.r.p.) gali siekti daugiausia **500 mW**. Riba taikoma
tam, kas palieka anteną: antenos stiprinimas pridedamas, o kabelio ir filtro
nuostoliai atimami. Stiprinimas dBi skaičiuojamas 2.15 dB mažesnis, nes riba
matuojama lyginant su dipoliu.
{{< /callout >}}

5.8 dBi kolinearinė antena ant 22 dBm plokštės neviršija ribos. Ta pati antena ant
plokštės su stiprintuvu ribą viršija, kol nesumažini siuntimo galios. Skaičiavimą
ir 2 pavyzdžius rasi kartotuvo vadovo skyriuje
[Galia: e.r.p. ir tavo antena](/repeater-guide/#erp).

## Antenos patikra su NanoVNA {#nanovna}

NanoVNA yra kišeninio dydžio vektorinis tinklo analizatorius. Jis parodo, kokiam
dažniui suderinta antena, todėl tai sužinai dar prieš montavimą. NanoVNA-H matuoja
iki 1.5 GHz, o tai apima 868 MHz.

1. Sukalibruok jį 800–950 MHz juostai su rinkinyje esančiais atviros grandinės,
   trumpojo jungimo ir apkrovos antgaliais.
2. Prijunk anteną per adapterį, kurį naudosi ant mazgo. Laikyk ją vertikaliai,
   atokiau nuo kūno ir stalo.
3. Pažiūrėk SWR (stovinčios bangos santykio) kreivę: ji rodo, kiek signalo antena
   grąžina atgal. Kreivės įduba turi būti ties tavo profilio dažniu, EU/UK (Narrow)
   atveju ties 869.618 MHz. Jei įduba nutolusi šimtais MHz, antena skirta kitai
   juostai.

Ties 868 MHz bangos ketvirtis yra 86 mm (bangos ilgis yra 345 mm). Vien ilgis
juostos neparodo, nes gamintojai strypines antenas sulenkia ir papildo apkrova.
Juostą parodo NanoVNA.

## Šaltiniai {#sources}

- Kabelio nuostoliai: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  Huber+Suhner RG316 techniniai duomenys,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  Times Microwave LMR-240 ir LMR-400 techniniai duomenys,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antenos: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  Sirio SO 868-915-2 techniniai duomenys,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Stiprinimas kaip į mažesnę erdvę suspaustas signalas: [RF Cafe, įvadas į antenas](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Jungtys: Rosenberger 32S102 (SMA) ir 53S101 (N) techniniai duomenys, Hirose U.FL
  katalogas.
- Filtrai: sysmocom cf866.5-kt30 produkto puslapis,
  [Citel dujiniai iškrovikliai](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Poliarizacijos nuostoliai: [Toronto universitetas, Friis efektai](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipolio stiprinimas pagal ilgį: [Wikipedia, dipolio antena](https://en.wikipedia.org/wiki/Dipole_antenna).
- Bangos ilgis: šviesos greitis iš [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Teisinė riba: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  1 priedas, juosta h1.7; kitus šaltinius rasi [kartotuvo vadove](/repeater-guide/#legal).
