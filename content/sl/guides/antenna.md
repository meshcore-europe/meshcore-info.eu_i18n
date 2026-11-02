---
title: Vodnik po antenah
lead: Prava antena, dobro nameščena, seže dlje kot večja moč. Preveri anteno na svojem companionu, nato izberi, priključi in namesti anteno za repetitor.
description: 'Izberi in namesti anteno MeshCore za 868 MHz: preverjanje paličaste antene na companionu, vrste anten in dobitek, konektorji, izgube kabla na meter, filtri, montaža in vpliv dobitka na zakonsko omejitev.'
eyebrow: Companion in repetitor · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-11-02'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Višina, uglašena antena in kratek kabel ti prinesejo več dosega kot vsak dodatni
milivat. Ta vodnik se začne pri companionu, radiu, s katerim pošiljaš
sporočila. Nato obravnava anteno na repetitorju, vozlišču, ki s strehe ali
droga posreduje sporočila naprej.

## Tvoj companion {#companion}

{{< callout type="warning" >}}
Anteno priključi, preden vklopiš radio. Radio LoRa, ki oddaja brez antene,
si lahko poškoduje čip.
{{< /callout >}}

Antena, priložena ploščici, zadošča. Priključi jo, drži vozlišče
pokonci in začni pošiljati sporočila. Boljša antena na companionu ti prinese
malo, repetitor v dosegu pa veliko.

Ločeno paličasto anteno kupi samo, če je priložena pokvarjena ali je ni.
Ni vsaka paličasta antena, ki jo prodajajo za 868 MHz, tudi uglašena za to
frekvenco. Preden ji zaupaš, [jo preveri z NanoVNA](#nanovna), žepnim
analizatorjem anten, ali si izposodi anteno s ploščice, ki deluje.

Vozlišče ob močnem oddajniku sliši slabše, kot bi moralo. Majhen
[filter SAW (filter s površinskim akustičnim valom)](#filters) med radiem in
anteno prepreči, da bi ta oddajnik prišel do sprejemnika. Najprej preveri
njegov podatkovni list:

- **Največja vhodna moč.** Skozi filter gre tudi signal, ki ga oddajaš. Ploščica,
  ki oddaja 22 dBm (160 mW) v filter, predviden za 15 dBm, filter uniči.
- **Prepustni pas.** Vsebovati mora frekvenco tvoje prednastavitve. Filter za
  868.65 do 869.25 MHz ne prepušča kanala EU/UK (Narrow) na
  869.618 MHz.

## Vrste anten za repetitor {#types}

Vsaka antena v mreži stoji pokonci. Vrsto izberi glede na to, kje so
vozlišča, ki jih želiš doseči:

- **Kolinearna antena iz steklenih vlaken.** Bela cev na drogu, z dobitkom po
  vsem obzorju. To je običajna izbira za repetitor, ki pokriva mesto.
- **Dipol.** Je krajši, ima manjši dobitek in visok snop. Vozlišča pod teboj
  in nad teboj doseže bolje kot kolinearna antena, na primer s hriba nad
  dolino.
- **Yagi.** Nosilec s prečnimi elementi, usmerjen v eno točko. Doseže en
  oddaljen repetitor in malo drugega. Namesti ga z elementi pokonci, ker
  njegova polarizacija sledi elementom.

## Dobitek in snop {#gain}

Dobitek ne dodaja moči. Signal, ki bi šel navzgor in navzdol, usmeri vzdolž
obzorja. Podobno je z žepno svetilko, ki ji izostriš snop: baterija je
ista, snop pa daljši in ožji. To se vidi pri dipolu in kolinearni anteni istega
proizvajalca:

| Antena | Dobitek | Navpična širina snopa |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 stopinj |
| Kolinearna antena iz steklenih vlaken (Sirio SPO 868-915-6) | 5.8 dBi | 23 stopinj |

{{< gain >}}

Diagram prikazuje prerez skozi drog, kot ga vidiš s strani. Če ga zavrtiš okoli
droga, dobiš celoten snop: krof pri dipolu in ploščat disk pri kolinearni
anteni. Pokončna antena oddaja enako v vse smeri okoli sebe. Zunaj narisanega
snopa se signal ne ustavi: je šibkejši, a še vedno zadošča za bližnje vozlišče.

Na strehi si želiš ploščat snop. Na hribu visoko nad vozlišči gre snop 23
stopinj čez njihove glave, dipol pa jih pokrije. Yagi gre še dlje: 16.6 dBi v
snopu, visokem 23 stopinj in širokem 25 stopinj (Amphenol Procom 7176870), ob
straneh pa nič.

Dobitek se meri glede na referenco. dBi ga primerja z idealno anteno, ki
oddaja enako v vse smeri. dBd ga primerja s polvalnim dipolom, ki ima sam
2.15 dBi: že najpreprostejša antena ne odda ničesar naravnost navzgor ali
navzdol. Daljši dipol, dolg 1.25 valovne dolžine, doseže 5.2 dBi. Kolinearna
antena namesto tega zlaga polvalne elemente enega nad drugega: več jih zloži,
večji je dobitek. Če isti signal stisneš v polovico prostora, je tam dvakrat
močnejši: 3 dB. Če ga stisneš v četrtino, je 4-krat močnejši: 6 dB. Proizvajalci
navajajo dobitek v dBi, zakonska omejitev pa se računa v dBd, glej
[Znotraj zakonske omejitve](#legal).

### Kateri dobitek ustreza tvoji lokaciji {#choose-gain}

- **Hribi, doline ali gosto mesto: približno 3 dBi.** Visok snop doseže
  vozlišča nad teboj in pod teboj ter okoli pobočij in stavb na poti. Velja
  tudi obratno: iz doline gre ploščat snop pod repetitorjem na hribu nad
  teboj. Takšna antena je RAKwireless RAKARG12: cev iz steklenih vlaken,
  dolga 36 cm.
- **Predmestja ali mesto z nizkimi strehami: 5 do 6 dBi.** Običajna kolinearna
  antena iz steklenih vlaken.
- **Ravna, odprta pokrajina: 8 do 10 dBi.** Najbolj ploščat snop seže najdlje
  vzdolž obzorja. Če je antena nameščena visoko, gre snop čez bližnja vozlišča.

Dobitek v imenu je najboljša vrednost v celotnem pasu antene. RAKARG12, ki ga
prodajajo kot anteno s 3 dBi, ima pri 865 do 870 MHz 2.8 dBi. V podatkovnem
listu preberi tabelo dobitka pri frekvenci svoje prednastavitve.

Nad 7 dBi ploščica z 22 dBm preseže zakonsko omejitev, razen če razliko
pokrijejo izgube kabla in filtra. Temu primerno znižaj oddajno moč.

Visok dobitek pomaga samo, če veš, kje so vozlišča: vzdolž obzorja okoli
repetitorja ali pri enem oddaljenem repetitorju v primeru antene Yagi.
Companion v tvoji roki kaže v vse smeri, zato mu najbolj ustreza nizek dobitek
priložene antene.

## Zakaj navpično {#vertical}

Anteni se najbolje slišita, kadar kažeta v isto smer. Izguba raste s kotom
med njima: pri 45 stopinjah izgubiš 3 dB, polovico svojega signala. Pri 90
stopinjah, torej med vodoravno in pokončno anteno, v teoriji ne pride nič.
Antene v mreži stojijo pokonci, zato naj stoji tudi tvoja. To velja tudi za
companion na mizi: če ga položiš vodoravno, te vsa vozlišča okoli tebe slišijo
slabše.

## Konektorji {#connectors}

Anteno naroči s konektorjem, ki ga ima tvoja ploščica. Vsak adapter je še en
spoj, ki ga moraš zatesniti, in dodatna izguba signala.

- **SMA.** Navojni konektor, širok približno 6 mm. Vtičnica na večini ploščic
  ima v sredini luknjo, antena pa pin. Izguba na takem konektorju je pri 868 MHz
  približno 0.03 dB.
- **RP-SMA.** Ima isto ohišje in navoj kot SMA, pin in luknja pa sta zamenjana.
  Videti je kot SMA, vendar se z njim ne spoji. Pred naročilom preveri, katerega
  ima tvoja ploščica.
- **U.FL (IPEX).** Drobna nasadna vtičnica neposredno na ploščici. Od nje vodi
  kratek priključni kabel (pigtail) do vtičnice SMA v ohišju. Predvidena je za
  30 priklopov, zato jo priključi enkrat in pusti pri miru.
- **N.** Velik navojni konektor na antenah iz steklenih vlaken in debelih
  kablih. Izguba na njem je največ 0.05 dB. Repetitor potrebuje en adapter ali
  pigtail z N na SMA ploščice.

## Izgube kabla {#cable}

Kabel pobere del signala, še preden ta zapusti anteno, in to v obeh smereh.
3 dB je polovica tvoje moči. Podatki proizvajalcev na meter, pri 868 do 900 MHz:

| Kabel | Izguba na meter | Izguba na 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

Na 3 metrih kabla RG174, tankega pigtaila, ki ga dobiš z mnogimi ploščicami,
izgubiš polovico moči. Ploščico namesti pri anteni s kratkim pigtailom
ali do antene napelji debel kabel. V vsoto prištej vsak adapter in filter na
poti.

## Filtri {#filters}

Filter je med radiem in anteno. Prepušča tvoj pas in blokira ostalo, zato
močan oddajnik v bližini ne preglasi sprejemnika. Potrebuješ ga, kadar vozlišče
v bližini drugih oddajnikov sliši slabše, kot bi moralo. Takšno vozlišče je
repetitor na drogu z baznimi postajami mobilne telefonije. Filter pobere del
signala v obeh smereh: njegovo izgubo upoštevaj kot pri kablu.

| | Filter SAW | Votlinski filter |
|---|---|---|
| Velikost | Nekaj milimetrov, na majhni ploščici | Kovinski blok ali cev |
| Izguba dobrega filtra | pod 2 dB | pod 1 dB |
| Največja vhodna moč dobrega filtra | 500 mW | več vatov |

Sysmocom cf866.5-kt30 je na primer votlinski filter za 863 do 870 MHz, ki
izgubi največ 1.0 dB in prenese 30 W. Narejen je za notranjo uporabo, zato ga
na drogu namesti v zatesnjeno škatlo.

Filtri se med seboj močno razlikujejo, zato pred nakupom preveri podatkovni
list. Nazivna vhodna moč mora presegati tvojo oddajno moč, prepustni pas pa
mora vsebovati frekvenco tvoje prednastavitve.

## Montaža {#mounting}

- **Nad robom strehe.** Antena potrebuje prost pogled v vse smeri, ki jih
  pokriva. Pomaga že nekaj metrov višine nad okoliškimi strehami. V vodniku za
  repetitorje razdelek [Izberi lokacijo](/repeater-guide/#site) pokaže, kako
  preveriš pogled.
- **Stran od kovine.** Žlebovi, drogovi, druge antene in kovinske strehe ob
  anteni spremenijo njen vzorec sevanja in uglasitev. Namesti jo na vrh droga,
  ne ob njem.
- **Pokonci.** Uporabi vodno tehtnico, glej [Zakaj navpično](#vertical).
- **Odkapna zanka.** Pusti, da kabel visi pod konektorjem, preden gre navzgor ali
  v notranjost. Voda tako odkaplja in ne teče v spoj.
- **Zatesni vsak zunanji konektor.** Voda v konektorju poveča izgube in povzroči
  korozijo pina. Zatesni ga proti dežju in tesnjenje vsako leto preveri.
- **Strela.** Antena na strehi je tarča. Plinski odvodnik v kablu se ob prenapetosti
  sproži in jo odvede v zemljo. Pri ozemljitvi upoštevaj razdelek
  [Strojna oprema](/repeater-guide/#hardware) v vodniku za repetitorje in
  lokalne predpise.

## Znotraj zakonske omejitve {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
V Evropi MeshCore uporablja podpas 869.40-869.65 MHz, z največ **500 mW**
efektivne sevane moči (e.r.p.). Omejitev velja za tisto, kar zapusti anteno:
dobitek antene se prišteje, izgube kabla in filtra se odštejejo. Dobitek v dBi
šteje 2.15 dB manj, ker se omejitev meri glede na dipol.
{{< /callout >}}

Kolinearna antena s 5.8 dBi na ploščici z 22 dBm ostane znotraj omejitve. Ista
antena na ploščici z ojačevalnikom omejitev preseže, dokler ne znižaš oddajne
moči. Razdelek [Moč: e.r.p. in tvoja antena](/repeater-guide/#erp) v vodniku za
repetitorje vsebuje izračun in 2 izračunana primera.

## Preveri anteno z NanoVNA {#nanovna}

NanoVNA je vektorski analizator omrežij žepne velikosti. Pokaže, na kateri
frekvenci je antena uglašena, zato to izveš še pred montažo. NanoVNA-H meri do
1.5 GHz, kar pokrije 868 MHz.

1. Umeri ga za 800 do 950 MHz z odprtim, kratkostičnim in bremenskim
   priključkom iz kompleta.
2. Anteno priključi prek adapterja, ki ga bo uporabljala na vozlišču. Drži jo
   pokonci ter stran od telesa in mize.
3. Preberi krivuljo SWR (razmerje stojnega vala): pokaže, koliko signala antena
   vrne nazaj. Najnižja točka mora biti na frekvenci tvoje prednastavitve, 869.618
   MHz za EU/UK (Narrow). Če je najnižja točka stotine MHz stran, je antena
   narejena za drug pas.

Četrtina valovne dolžine pri 868 MHz je 86 mm (valovna dolžina je 345 mm). Sama
dolžina ti ne pove pasu, ker proizvajalci paličaste antene zgibajo in
obremenjujejo, NanoVNA pa ti ga pove.

## Viri {#sources}

- Izgube kabla: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  podatkovni list Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  podatkovna lista Times Microwave LMR-240 in LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antene: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  podatkovni list Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Dobitek kot signal, stisnjen v manj prostora: [RF Cafe, uvod v antene](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Konektorji: podatkovna lista Rosenberger 32S102 (SMA) in 53S101 (N), katalog
  Hirose U.FL.
- Filtri: stran izdelka sysmocom cf866.5-kt30,
  [plinski odvodniki Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Izguba zaradi polarizacije: [University of Toronto, Friisovi učinki](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dobitek dipola glede na dolžino: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Valovna dolžina: hitrost svetlobe po podatkih [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Zakonska omejitev: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Priloga 1, pas h1.7; preostale vire navaja [vodnik za repetitorje](/repeater-guide/#legal).
