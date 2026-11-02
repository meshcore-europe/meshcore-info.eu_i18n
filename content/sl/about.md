---
title: Kaj je MeshCore?
lead: MeshCore pošilja besedilna sporočila po radiu, od vozlišča do vozlišča. Ne potrebuješ interneta ali naročnine.
description: 'Kaj MeshCore je in kaj ni: mreža, spremljevalci, repetitorji in strežniki sob, usmerjanje, šifriranje in pas 868 MHz v Evropi.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '78bc31e8'
  seeded: '2026-11-02'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['aa768ac3', 'c9b24089', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '655373a9', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b9fc8810', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '0eb54b47', '02f1fe2f', 'e6b5b258']
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
  približno tako dolga kot SMS na telefonu. Govora, fotografij, videa in
  spletnih strani ne prenaša, običajne telefonske številke pa ne moreš doseči.
- **Ni služba za nujno pomoč.** Mreže ne posluša nobena služba za nujno pomoč
  in nihče ne obljublja, da bo kdo prebral tvoje sporočilo. V nujnih primerih
  pokliči 112.
- **Ni takojšen in ne deluje povsod.** Sporočilo potuje od radia do radia.
  Lahko traja nekaj sekund ali pa sploh ne prispe. Ali pride do cilja, je odvisno
  od repetitorjev okoli tebe, višine, stavb in tvoje antene. Majhen radio v zaprtem
  prostoru pogosto ne doseže nikogar, repetitor na strehi pa seže kilometre daleč.
- **Ni storitev, ki bi jo kdo upravljal zate.** Ni ponudnika, ni službe za pomoč
  uporabnikom in nihče ne obljublja pokritosti. Mreža obstaja tam, kjer so ljudje
  iz skupnosti postavili repetitorje, drugje pa ne.
- **V mreži ni vse zasebno.** Neposredna sporočila so šifrirana, kanal Public in
  kanale s ključnikom pa lahko bere vsak. Ime tvojega vozlišča in položaj, ki ga
  deliš, vidijo vsi v dosegu.
  [Opazovalci](/network/) to, kar slišijo, sporočajo javnim zemljevidom. V
  [razdelku o šifriranju](#encryption) piše, kaj ostane zasebno.
- **Ni neomejen.** Vsi na istem območju si delijo en radijski kanal, pravila za
  [pas 868 MHz](#band) pa omejujejo, koliko časa sme posamezen radio oddajati.
  Vsako sporočilo vsem drugim vzame del časa za oddajanje, zato boti, pogosta
  oznanila in testna sporočila upočasnijo mrežo za vse.
- **Ni Meshtastic.** Meshtastic je drug sistem, ki teče na skoraj istih
  ploščah. Sistema ne moreta komunicirati med seboj.

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

- Za stik na pohodih, na morju in na festivalih, kjer je mobilno omrežje
  preobremenjeno ali ga ni.
- Kot rezervni kanal za družino ali sosede, ko odpove elektrika ali mobilno
  omrežje.
- Za lokalni klepet po radiih, ki so v lasti ljudi samih.
- Za eksperimentiranje z radiem, antenami, sončno energijo in odprtokodno programsko opremo.

## Od kod so podatki {#data}

Iskanje na strani [lokalne skupine](/community/) najde kraj s pomočjo kopije
brezplačnih seznamov krajev in poštnih številk [GeoNames](https://www.geonames.org/),
ki so na voljo pod licenco
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopija je na
tem spletnem mestu. Tvoje iskanje nikoli ne zapusti tvoje naprave in na GeoNames ne gre
nobena zahteva.
