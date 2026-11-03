---
title: Kaj je MeshCore?
lead: MeshCore pošilja besedilna sporočila po radiu, od vozlišča do vozlišča. Ne potrebuješ interneta ali naročnine.
description: 'Kaj MeshCore je in česa ni: vrste vozlišč, usmerjanje, razlike od Meshtastica, šifriranje in pas 868 MHz.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '279b56a4'
  seeded: '2026-11-03'
  fields: {title: '06eda66b', lead: 'c0174569', description: '15e6d2a7', eyebrow: '8610c822'}
  sections: ['aa768ac3', '16fde264', '0a55792c', 'c3de803d', '493b444f', 'a8b2b9b4', '429f699c', 'f8008f48', '88af2bd3', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'fab378a5', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', 'fc8f3129', '8dec428a', '07cbac35', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '95e18f18', '02f1fe2f', 'e6b5b258']
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

- **Ni internet in ni telefon.** MeshCore pošilja kratka besedilna sporočila,
  približno tako dolga kot SMS na telefonu. Glasu, fotografij, videa
  in spletnih strani ni, običajne telefonske številke pa ne moreš doseči.
- **Ni služba za nujne primere.** Nobena služba za nujne primere ne spremlja
  omrežja in nihče ne obljublja, da bo kdo prebral tvoje sporočilo. V
  nujnem primeru pokliči 112.
- **Ne deluje takoj in ne povsod.** Sporočilo skače od radia do
  radia in lahko potrebuje nekaj sekund ali pa sploh ne prispe. Ali pride do cilja, je odvisno od repetitorjev okoli tebe, višine, stavb in tvoje
  antene. Majhen radio v zaprtem prostoru pogosto ne doseže nikogar, repetitor na strehi
  pa seže kilometre daleč.
- **Ni storitev, ki bi jo kdo upravljal zate.** Ni ponudnika, ni službe za pomoč
  in ni zagotovila o pokritosti. Omrežje obstaja tam, kjer so člani
  skupnosti postavili repetitorje, in nikjer drugje.
- **V njem ni vse zasebno.** Neposredna sporočila so šifrirana, a
  Public in kanale s ključnikom lahko bere vsak, ime tvojega vozlišča in
  položaj, ki ga deliš, pa vidijo vsi v dosegu.
  [Opazovalci](/network/) javnim zemljevidom sporočajo, kar slišijo.
  [Razdelek o šifriranju](#encryption) pojasnjuje, kaj ostane zasebno.
- **Ni brez omejitev.** Vsi na območju si delijo en radijski kanal,
  pravila za [pas 868 MHz](#band) pa omejujejo, kako dolgo sme oddajati vsak radio.
  Vsako sporočilo vsem drugim vzame del časa oddajanja, zato boti, pogosta oglaševanja
  in testna sporočila upočasnijo omrežje za vse.
- **Ni Meshtastic.** Meshtastic je drug sistem, ki deluje na
  skoraj enakih ploščicah. Sistema med seboj ne moreta komunicirati.
  [Prehod z Meshtastica](#meshtastic) navaja, kaj deluje drugače.

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

## Prehod z Meshtastica {#meshtastic}

Na številnih ploščicah deluje MeshCore ali Meshtastic, nanje pa naložiš tistega, ki ga želiš.
To so razlike, ki jih opaziš najprej. Temeljijo na MeshCoru
v1.18.0 in dokumentaciji Meshtastica iz novembra 2026.

- **Kdo posreduje sporočila.** V sistemu MeshCore to počnejo le repetitorji, tvoj spremljevalec
  nikoli. V sistemu Meshtastic sporočila posreduje tudi privzeta vloga odjemalca,
  razen če jih je že posredovalo drugo vozlišče.
- **Kako daleč seže sporočilo.** Sporočilo v sistemu MeshCore lahko prečka do 64
  repetitorjev. Meshtastic sporočilo privzeto ustavi po 3 skokih, največ pa jih dovoli 7.
- **Odčitki drugih vozlišč.** Repetitorji in senzorska vozlišča v sistemu MeshCore pošljejo
  odčitke, kot je napetost baterije, ko jih zanje prosiš. Ne pošiljajo jih
  celotni mreži.
- **Internet.** Vdelana programska oprema MeshCore nima povezave med mrežami prek
  interneta. [Opazovalci](/network/) to, kar slišijo, sporočajo zemljevidom, le v
  eno smer. Meshtastic ima vgrajen modul MQTT, ki lahko prenaša sporočila med
  mrežami prek interneta.

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

- Ostaneš v stiku na pohodih, na morju in na festivalih, kjer je mobilno omrežje
  preobremenjeno ali ga ni.
- Rezervni kanal za družino ali sosede, ko odpove elektrika ali mobilno omrežje.
- Lokalni klepet na radijskih postajah, ki jih imajo ljudje sami v lasti.
- Od doma preverjaš oddaljeno lokacijo. Repetitorji in senzorska vozlišča ti na zahtevo
  sporočijo napetost baterije in druge odčitke.
- Spremljaš senzor. Na senzorskem vozlišču teče vdelana programska oprema MeshCore za
  meritve. Vozlišče hrani zgodovino svojih odčitkov. Če se naročiš nanj, te opozori,
  na primer ko mu zmanjkuje baterije.
- Na daljavo nekaj vklapljaš ali izklapljaš, na primer črpalko. To s svojo kodo dodaš
  v vdelano programsko opremo senzorja.
- Eksperimentiraš z radiem, antenami, sončno energijo in odprtokodno programsko opremo.

## Od kod so podatki {#data}

Iskanje na strani [lokalne skupine](/community/) najde kraj s pomočjo kopije
brezplačnih seznamov krajev in poštnih številk [GeoNames](https://www.geonames.org/),
ki so na voljo pod licenco
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopija je na
tem spletnem mestu. Tvoje iskanje nikoli ne zapusti tvoje naprave in na GeoNames ne gre
nobena zahteva.
