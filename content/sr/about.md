---
title: Šta je MeshCore?
lead: MeshCore šalje tekstualne poruke radio-talasima, od čvora do čvora. Za to ti ne trebaju internet ni pretplata.
description: 'Šta MeshCore jeste, a šta nije: vrste čvorova, rutiranje, enkripcija i opseg od 868 MHz.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '70b86ac3'
  seeded: '2026-11-11'
  fields: {title: '06eda66b', lead: 'c0174569', description: 'c2255f49', eyebrow: '8610c822'}
  sections: ['aa768ac3', '9e1e2d85', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', 'd516c212', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b7b981e6', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '5d796ffb', '1a490368', 'f0dd237f', '053d85bc', '02f1fe2f', 'e6b5b258']
---

MeshCore je besplatan softver za male LoRa radio-uređaje. LoRa je radio-tehnika
koja šalje malo podataka daleko, uz vrlo malu potrošnju energije. Radio-uređaj sa MeshCore softverom
zove se *čvor*. Možeš ga upariti sa aplikacijom na telefonu ili laptopu, a neki imaju sopstveni
ekran i tastaturu. Tako šalješ tekst ljudima koji su kilometrima daleko. Između tebe i njih nema antenskog stuba, rutera ni operatera.

Softver je otvorenog koda. Razvija se na adresi
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore), pod MIT
licencom.

## Šta MeshCore nije {#not}

Tek otkrivaš radio? Ovo ljudi najčešće očekuju od MeshCore-a,
a on to ne radi.

- **To nije internet ni telefon.** MeshCore šalje kratke tekstualne poruke,
  otprilike dužine SMS poruke na tvom telefonu. Nema glasa, fotografija, videa
  ni sajtova, a običan broj telefona ne možeš da pozoveš.
- **To nije hitna služba.** Nijedna hitna služba ne obećava da sluša
  mesh. Znamo da mesh može da radi. Da li radi u hitnom slučaju, niko ne zna.
- **Nije trenutan, i nije svuda.** Poruka skače od radio-uređaja do
  radio-uređaja i može da joj treba nekoliko sekundi, ili da uopšte ne stigne. Da li će stići,
  zavisi od repetitora oko tebe, od visine, zgrada i tvoje antene.
  Mali radio-uređaj u zatvorenom često ne dopire ni do koga. Repetitor na krovu
  dopire kilometrima daleko.
- **To nije usluga koju neko vodi za tebe.** Nema provajdera, službe za podršku
  ni obećane pokrivenosti. Mesh postoji tamo gde su ljudi iz zajednice
  postavili repetitore.
- **Nije sve na njemu privatno.** Direktne poruke su šifrovane, ali
  Public i hashtag kanale može da čita svako. Ime tvog čvora i pozicija koju
  deliš vidljivi su svima u dometu.
  [Observeri](/network/) šalju ono što čuju na javne mape.
  [Odeljak o šifrovanju](#encryption) objašnjava šta ostaje privatno.
- **Nije neograničen.** Svi u jednoj oblasti dele jedan radio-kanal, a
  pravila za [opseg od 868 MHz](#band) ograničavaju koliko dugo svaki radio-uređaj sme da emituje.
  Svaka poruka oduzima vreme emitovanja svima ostalima. Zato botovi, česti adverti
  i probne poruke usporavaju mesh za sve.
- **To nije Meshtastic.** Meshtastic je drugi sistem koji radi na
  uglavnom istim pločama. Ta dva sistema ne mogu međusobno da komuniciraju.

## Mesh za minut {#mesh}

Jedan LoRa radio u gradu dobacuje nekoliko kilometara, a sa brda ili krova
mnogo dalje. Da bi poruke stigle dalje, radio-uređaji ih prenose jedni za druge: to
je *mesh*. U MeshCore mreži taj prenos obavljaju radio-uređaji koji se zovu *repetitori*. Kada
repetitor čuje poruku, ponovo je šalje, pa ona može da pređe ceo region.

Mesh nema vlasnika. Svaki čvor i svaki repetitor pripada nekom iz
zajednice. Mesh dopire dokle dopiru njihovi repetitori.

## 3 vrste čvorova {#roles}

Vrstu čvora biraš kada na njega instaliraš firmver. Tvoj prvi čvor je companion.

**Companion.** Tvoj lični radio. Uparuješ ga sa MeshCore aplikacijom na telefonu ili
laptopu preko Bluetooth veze ili USB kabla, a neki imaju sopstveni ekran i tastaturu. U aplikaciji
čitaš i kucaš poruke. Companion čuva tvoje kontakte i kanale,
kao i poruke koje su stigle dok aplikacija nije bila povezana. Companion ne prenosi poruke za druge.

**Repetitor.** Radio na visokom mestu, koji prenosi poruke za sve. Većina
repetitora radi na solarnu energiju. Sopstveni ti treba samo tamo gde mesh još ne
dopire. Repetitor nema svoju aplikaciju. Podešavaš ga preko USB kabla, ili se
prijaviš lozinkom i upravljaš njime preko radija. U
[vodiču za repetitore](/repeater-guide/) piše kako se to radi.

**Room server.** Mala oglasna tabla na mesh mreži. Kada se prijaviš, dobiješ
objave koje si propustio dok si bio van dometa, najviše poslednje 32. Room server ih čuva
samo u memoriji, pa ih restart ili nestanak struje briše. Lokalna grupa ga koristi
za obaveštenja.

## Kako poruka pronalazi put {#routing}

Svaki čvor ima tajni i javni ključ. Javni ključ je njegov identitet. Čvor
se predstavlja *advertom*: to je potpisani paket sa njegovim imenom i, ako
tako izabereš, pozicijom. Neko se pojavljuje među tvojim kontaktima kada do tebe stigne njegov
advert ili kada skeniraš njegov QR kôd. U aplikaciji postoji dugme kojim šalješ svoj advert.

Tvoja prva poruka nekom kontaktu odlazi kao *flood*. Svaki repetitor koji
je čuje prenosi je jednom i usput dodaje svoj kratki ID. Odgovor
vraća taj spisak ID-jeva. Od tada tvoje poruke tom kontaktu
idu zabeleženom rutom i emituju ih samo repetitori na njoj. Kada se ruta
prekine, aplikacija ponovo šalje flood.

Poruke na kanalu nemaju jednu adresu, pa uvek idu kao flood.
Repetitori pamte šta su nedavno preneli i odbacuju kopije koje ponovo stignu
drugom rutom. Poruka može da prođe kroz najviše 64 repetitora, ili 32 tamo gde preset koristi 2-bajtne
ID-jeve.

## Šifrovanje i privatnost {#encryption}

Tvoje direktne poruke su šifrovane od kraja do kraja: samo ti i druga
osoba možete da ih čitate. Od primaoca paketa repetitor vidi samo nagoveštaj od 1 bajta.

Kanali su šifrovani zajedničkim ključem, pa od toga ko ima taj ključ
zavisi ko može da ih čita:

- **Public** je podešen na svakom companion uređaju. Njegov ključ je objavljen, pa svako
  može da ga čita.
- **Hashtag kanali**, kao što je `#utrecht`, dobijaju ključ iz svog imena.
  Svako ko zna ime može da se pridruži, zato i njih smatraj javnim.
- **Privatni kanali** koriste nasumičan ključ koji sam deliš, na primer
  kao QR kôd.

Adverti su potpisani, ali nisu šifrovani. Ime tvog čvora i njegova pozicija, ako
je deliš, vidljivi su svima u dometu. Izaberi ime koje ne otkriva više
nego što želiš.

## Opseg 868 MHz u Evropi {#band}

U Evropi MeshCore koristi mali deo opsega 868 MHz koji svako sme da koristi
bez licence. Njegov evropski radio-preset, EU/UK (Narrow), nalazi se na
869.618 MHz, na kanalu širine 62.5 kHz. To je unutar podopsega 869.40-869.65 MHz,
koji dozvoljava do 500 mW e.r.p. Uređaj tamo sme da emituje najviše 10%
vremena. U
[pravnom odeljku vodiča za repetitore](/repeater-guide/#legal) naći ćeš detalje
i ograničenja po zemljama.

Svi na jednom području koriste isti preset, inače se njihovi radio-uređaji ne čuju
međusobno. Neke zemlje i regioni koriste varijantu: tvoja
[lokalna grupa](/community/) zna koju.

## Za šta ga ljudi koriste {#uses}

- Da ostaneš u vezi na planinarenju, na moru i na festivalima gde je mobilna mreža
  preopterećena ili je nema.
- Rezervni kanal za porodicu ili komšije kada nestane struje ili mobilne
  mreže.
- Rezerva za lokalne vlasti kada njihove uobičajene mreže otkažu.
- Lokalni čet na radio-uređajima koje ljudi sami poseduju.
- Da tim za potragu i spasavanje ostane u vezi tamo gde nema mobilne mreže.
  MeshCore SAR, aplikacija zajednice sa stranice [Projekti](/projects/), dodaje mape i
  deljene lokacije.
- Da od kuće proveriš udaljenu lokaciju. Repetitori i senzorski čvorovi javljaju
  napon baterije i druga merenja kada ih pitaš.
- Da pratiš senzor. Senzorski čvor pokreće MeshCore firmver za merenje.
  On čuva istoriju napona svoje baterije. Prijavi se kao admin i on
  te upozorava kada je baterija pri kraju. Upozorenja za druga merenja dodaješ
  sopstvenim kodom.
- Da nešto uključiš ili isključiš na daljinu, na primer pumpu. To dodaješ u firmver
  senzora sopstvenim kodom.
- Da eksperimentišeš sa radiom, antenama, solarnom energijom i softverom otvorenog koda.

Neki organi vlasti grade ili testiraju rezervni sistem na MeshCore-u. Ove primere smo proverili
u novembru 2026.

- Ciklon Gabrijela prekinuo je sve veze u oblasti Tairāwhiti, na Novom Zelandu. U
  septembru 2025. tamošnja služba za vanredne situacije navela je MeshCore kao
  [jedan od najmanje 6 rezervnih načina komunikacije](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Služba je gradila i solarne repetitore kao okosnicu mreže.
- Nemački okrug Bad Kissingen
  [gradi mrežu za tekstualne poruke na MeshCore-u](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  za organe vlasti, hitne službe i kritične objekte. Prve se
  povezuju vatrogasne stanice.
- Opštinsko veće Hilversuma, u Holandiji,
  [glasalo je 34 prema 1 za probni rad](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  uz repetitor na tornju gradske kuće. Opština
  [ocenjuje probni rad na jesen 2027.](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/)
- Dva holandska bezbednosna regiona, koji organizuju reagovanje u kriznim situacijama,
  eksperimentišu sa MeshCore-om:
  [Južni Limburg](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  i [Drente](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Drente smatra da je prerano reći kako ili kada bi ga mogla koristiti.
- U Dalfsenu, takođe u Holandiji, volonteri
  [vode pilot-projekat zajedno sa opštinama](https://noodnetoverijssel.nl/).
  Prvo koriste glasovni radio, a MeshCore kao drugi sloj za tekst.

Da li mesh u tvojoj blizini radi u hitnom slučaju, to niko ne zna.

## Odakle potiču podaci {#data}

Pretraga na stranici [lokalnih grupa](/community/) pronalazi mesto pomoću kopije
besplatnih spiskova mesta i poštanskih brojeva sa sajta [GeoNames](https://www.geonames.org/),
pod licencom
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopija se nalazi na
ovom sajtu. Tvoja pretraga nikada ne napušta tvoj uređaj i nijedan zahtev ne ide ka
sajtu GeoNames.
