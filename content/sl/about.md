---
title: Kaj je MeshCore?
lead: MeshCore pošilja besedilna sporočila po radiu, od vozlišča do vozlišča. Ne potrebuješ interneta ali naročnine.
description: 'Kaj MeshCore je in česa ne: vrste vozlišč, usmerjanje, šifriranje in pas 868 MHz.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '2a40da22'
  seeded: '2026-11-04'
  fields: {title: '06eda66b', lead: 'c0174569', description: 'c2255f49', eyebrow: '8610c822'}
  sections: ['aa768ac3', '92fc3ea7', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '203a07ef', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'ac039316', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '5d796ffb', '1a490368', 'f0dd237f', '3182d5c8', '02f1fe2f', 'e6b5b258']
---

MeshCore je brezplačna programska oprema za majhne radie LoRa. LoRa je radijska tehnika,
ki z zelo malo energije pošilja malo podatkov daleč. Radiu z MeshCore
pravimo *vozlišče*. Povežeš ga z aplikacijo na telefonu ali prenosniku, nekateri pa imajo
svoj zaslon in tipkovnico. Tako pošiljaš besedilo ljudem, ki so kilometre stran. Vmes ni stolpa, usmerjevalnika ali ponudnika.

Programska oprema je odprtokodna, razvoj poteka na
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) pod licenco
MIT.

## Česa MeshCore ni {#not}

Šele začenjaš z radiem? To ljudje od sistema MeshCore najpogosteje pričakujejo,
a tega ne zmore.

- **To ni internet in ni telefon.** MeshCore pošilja kratka besedilna sporočila,
  približno dolga kot SMS na tvojem telefonu. Glasu, fotografij, videa
  in spletnih strani ne prenaša, običajne telefonske številke pa ne moreš doseči.
- **To ni služba za nujne primere.** Nobena služba za nujne primere ne obljublja,
  da spremlja mrežo. Nihče ne obljublja, da bo kdo prebral tvoje sporočilo.
- **Ne deluje takoj in ne povsod.** Sporočilo skače od radia do
  radia. Lahko traja nekaj sekund ali pa sploh ne pride do cilja. Ali pride
  do cilja, je odvisno od repetitorjev okoli tebe, od višine, stavb in tvoje
  antene. Majhen radio v zaprtem prostoru pogosto ne doseže nikogar. Repetitor na strehi
  seže kilometre daleč.
- **To ni storitev, ki jo nekdo upravlja zate.** Ni ponudnika, ni
  službe za pomoč uporabnikom in ni obljube o pokritosti. Mreža obstaja tam, kjer so ljudje iz
  skupnosti postavili repetitorje.
- **Na njej ni vse zasebno.** Neposredna sporočila so šifrirana. Kanal
  Public in kanale s ključnikom pa lahko bere vsak. Ime tvojega vozlišča
  in deljeni položaj vidijo vsi v dosegu.
  [Opazovalci](/network/) to, kar slišijo, pošiljajo na javne zemljevide.
  [Razdelek o šifriranju](#encryption) pojasni, kaj ostane zasebno.
- **To ni neomejeno.** Vsi na nekem območju si delijo en radijski kanal.
  Pravila za [pas 868 MHz](#band) omejujejo, kako dolgo sme vsak radio oddajati.
  Vsako sporočilo vzame čas oddajanja vsem drugim. Zato roboti, pogoste najave
  in testna sporočila upočasnijo mrežo za vse.
- **To ni Meshtastic.** Meshtastic je drug sistem, ki teče na
  skoraj enakih ploščah. Sistema se med seboj ne moreta sporazumevati.

## Mreža v eni minuti {#mesh}

En radio LoRa v mestu seže nekaj kilometrov, s hriba ali strehe pa precej dlje.
Za večji doseg si radii med seboj posredujejo sporočila: to je *mreža*. V sistemu
MeshCore to delo opravljajo radii, ki jim pravimo *repetitorji*. Repetitor, ki
sliši sporočilo, ga pošlje naprej, zato lahko sporočilo prečka celo regijo.

Mreža ni nikogaršnja last. Vsako vozlišče in vsak repetitor je last nekoga iz
skupnosti. Mreža seže tako daleč, kot sežejo njihovi repetitorji.

## 3 vrste vozlišč {#roles}

Vrsto vozlišča izbereš, ko nanj naložiš programsko opremo. Tvoje prvo vozlišče je spremljevalec.

**Spremljevalec.** Tvoj lastni radio. Z aplikacijo MeshCore na telefonu ali
prenosniku ga povežeš prek povezave Bluetooth ali USB, nekateri pa imajo svoj zaslon in
tipkovnico. V aplikaciji bereš in tipkaš. Spremljevalec hrani tvoje stike in
kanale ter sporočila, ki so prispela, ko aplikacija ni bila povezana. Spremljevalec ne posreduje sporočil za druge.

**Repetitor.** Radio na visoki točki, ki posreduje sporočila za vse. Večina jih
deluje na sončno energijo. Svojega potrebuješ le tam, kamor mreža še ne seže.
Svoje aplikacije nima. Nastaviš ga prek USB ali pa se prijaviš z geslom in ga
upravljaš prek radia. Kako to narediš, piše v
[vodniku za repetitorje](/repeater-guide/).

**Strežnik sobe.** Majhna oglasna deska v mreži. Ko se prijaviš, dobiš objave,
ki so ti ušle zunaj dosega, največ zadnjih 32. Hrani jih le v
pomnilniku, zato jih ponovni zagon ali izpad elektrike izbriše. Lokalna skupina
ga uporablja za obvestila.

## Kako sporočilo najde pot {#routing}

Vsako vozlišče ima skrivni in javni ključ. Javni ključ je njegova identiteta. Vozlišče
se predstavi z *oznanilom*: to je podpisan paket z njegovim imenom in, če tako
izbereš, položajem. Nekdo se pojavi med tvojimi stiki, ko te doseže eno od njegovih
oznanil ali ko skeniraš njegovo kodo QR. V aplikaciji je gumb, s katerim pošlješ svoje.

Tvoje prvo sporočilo stiku se razširi s *poplavljanjem*. Vsak repetitor, ki ga
sliši, ga enkrat posreduje in na poti doda svoj kratki ID. Odgovor prinese ta
seznam ID-jev nazaj. Od takrat naprej tvoja sporočila temu stiku sledijo zabeleženi
poti in oddajajo le repetitorji na njej. Ko se pot prekine, aplikacija spet
uporabi poplavljanje.

Sporočila za kanal nimajo enega samega naslova, zato se vedno širijo s poplavljanjem.
Repetitorji si zapomnijo, kaj so nedavno posredovali, in zavržejo kopije, ki
pridejo znova po drugi poti. Sporočilo lahko prečka do 64 repetitorjev oziroma 32, kjer prednastavitev uporablja 2-bajtne
ID-je.

## Šifriranje in zasebnost {#encryption}

Tvoja neposredna sporočila so šifrirana od konca do konca: brati jih morata le ti
in druga oseba. Repetitor vidi, komu je paket namenjen, le kot 1-bajtni namig.

Kanali so šifrirani s skupnim ključem, zato jih lahko bere tisti, ki ima ta ključ:

- **Public** je nastavljen na vsakem spremljevalcu. Njegov ključ je objavljen,
  zato ga lahko bere vsak.
- **Kanali s ključnikom**, kot je `#utrecht`, dobijo ključ iz svojega imena.
  Pridruži se jim lahko vsak, ki pozna ime, zato jih prav tako obravnavaj kot javne.
- **Zasebni kanali** uporabljajo naključen ključ, ki ga deliš sam, na primer
  v obliki kode QR.

Oznanila so podpisana, niso pa šifrirana. Ime tvojega vozlišča in njegov položaj,
če ga deliš, vidijo vsi v dosegu. Izberi ime, ki ne pove več, kot želiš.

## Pas 868 MHz v Evropi {#band}

V Evropi MeshCore uporablja majhen del pasu 868 MHz, ki ga sme vsak uporabljati
brez licence. Njegova evropska radijska prednastavitev, EU/UK (Narrow), je na
869.618 MHz na kanalu širine 62.5 kHz. To je znotraj podpasa 869.40-869.65 MHz,
ki dovoljuje do 500 mW e.r.p. Naprava sme tam oddajati največ 10%
časa. Podrobnosti in omejitve po državah najdeš v
[pravnem razdelku vodnika za repetitorje](/repeater-guide/#legal).

Vsi na istem območju uporabljajo isto prednastavitev, sicer se njihovi radii med seboj ne
slišijo. Nekatere države in regije uporabljajo različico: katero, ve tvoja
[lokalna skupina](/community/).

## Za kaj ga ljudje uporabljajo {#uses}

- Komunikacija na pohodih, na morju in na festivalih, kjer je mobilno omrežje
  preobremenjeno ali ga ni.
- Rezervni kanal za družino ali sosede, ko odpove elektrika ali mobilno
  omrežje.
- Rezerva za lokalne oblasti, ko odpovejo njihova običajna omrežja.
- Lokalni klepet na radiih, ki so v lasti ljudi samih.
- Povezava ekipe za iskanje in reševanje tam, kjer ni mobilnega omrežja.
  MeshCore SAR, skupnostna aplikacija na strani [Projekti](/projects/), doda
  zemljevide in deljene lokacije.
- Preverjanje oddaljene lokacije z doma. Repetitorji in senzorska vozlišča ti na
  zahtevo sporočijo napetost baterije in druge meritve.
- Spremljanje senzorja. Na senzorskem vozlišču teče vdelana programska oprema
  MeshCore za meritve. Hrani zgodovino napetosti svoje baterije. Če se prijaviš
  kot skrbnik, te opozori, ko je baterija skoraj prazna. Opozorila za druge
  meritve dodaš s svojo kodo.
- Vklop in izklop nečesa na daljavo, na primer črpalke. To dodaš v vdelano
  programsko opremo senzorja s svojo kodo.
- Eksperimentiranje z radiem, antenami, sončno energijo in odprtokodno
  programsko opremo.

Nekatere oblasti gradijo ali preizkušajo rezervni sistem na osnovi MeshCore. Te primere smo preverili novembra 2026.

- Ciklon Gabrielle je v regiji Tairāwhiti na Novi Zelandiji prekinil vse komunikacijske povezave.
  Septembra 2025 je regijska služba za izredne razmere MeshCore uvrstila med
  [vsaj 6 rezervnih načinov komunikacije](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Kot hrbtenico je gradila tudi repetitorje na sončni pogon.
- Nemško okrožje Bad Kissingen
  [gradi besedilno mrežo na osnovi MeshCore](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  za organe oblasti, reševalne službe in objekte kritične infrastrukture. Najprej se povežejo
  gasilski domovi.
- Občinski svet mesta Hilversum na Nizozemskem je
  [s 34 glasovi proti 1 podprl preizkus](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  z repetitorjem na stolpu mestne hiše. Občina
  [ga bo ocenila jeseni 2027](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Dve nizozemski varnostni regiji, ki organizirata odziv na krizo,
  preizkušata MeshCore:
  [Južni Limburg](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  in [Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  V regiji Drenthe pravijo, da je še prezgodaj reči, kako ali kdaj bi ga lahko uporabili.
- V kraju Dalfsen, prav tako na Nizozemskem, prostovoljci
  [izvajajo pilotni projekt skupaj z občinami](https://noodnetoverijssel.nl/).
  Najprej uporabljajo govorne radijske zveze, MeshCore pa kot drugo plast za besedilna sporočila.

Nihče ne obljublja, da bo kdo v mreži blizu tebe prebral tvoje sporočilo.

## Od kod so podatki {#data}

Iskanje na strani [lokalne skupine](/community/) najde kraj s pomočjo kopije
brezplačnih seznamov krajev in poštnih številk [GeoNames](https://www.geonames.org/),
ki so na voljo pod licenco
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopija je na
tem spletnem mestu. Tvoje iskanje nikoli ne zapusti tvoje naprave in na GeoNames ne gre
nobena zahteva.
