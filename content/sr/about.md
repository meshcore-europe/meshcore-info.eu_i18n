---
title: Šta je MeshCore?
lead: MeshCore šalje tekstualne poruke radio-talasima, od čvora do čvora. Za to ti ne trebaju internet ni pretplata.
description: 'Šta MeshCore jeste, a šta nije: mesh, companion uređaji, repetitori i room serveri, rutiranje, šifrovanje i opseg 868 MHz u Evropi.'
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

- **Nije internet ni telefon.** MeshCore šalje kratke tekstualne poruke,
  otprilike dužine SMS poruke na telefonu. Nema glasa, fotografija, videa
  ni veb-sajtova, a ne možeš ni da dopreš do običnog telefonskog broja.
- **Nije hitna služba.** Nijedna hitna služba ne prati mesh
  i niko ne garantuje da će neko pročitati tvoju poruku. U
  hitnom slučaju pozovi 112.
- **Nije trenutan i ne radi svuda.** Poruka skače od radija do
  radija i može da putuje nekoliko sekundi ili da uopšte ne stigne. Da li će stići
  zavisi od repetitora oko tebe, od visine, zgrada i tvoje
  antene. Mali radio u zatvorenom prostoru često ne dobacuje ni do koga, a repetitor na krovu
  dobacuje kilometrima daleko.
- **Nije usluga koju neko održava za tebe.** Nema operatera, korisničke podrške
  ni garantovane pokrivenosti. Mesh postoji tamo gde su ljudi iz
  zajednice postavili repetitore, i nigde drugde.
- **Nije sve na njemu privatno.** Direktne poruke su šifrovane, ali
  Public i hashtag kanale može da čita svako, a ime tvog čvora
  i pozicija koju deliš vidljivi su svima u dometu.
  [Observeri](/network/) javljaju javnim mapama šta čuju. U
  [odeljku o šifrovanju](#encryption) piše šta ostaje privatno.
- **Nije neograničen.** Svi na jednom području dele jedan radio-kanal, a
  pravila za [opseg 868 MHz](#band) ograničavaju koliko dugo svaki radio sme da emituje.
  Svaka poruka svima ostalima oduzima vreme emitovanja, pa botovi, česti adverti
  i probne poruke usporavaju mesh za sve.
- **Nije Meshtastic.** Meshtastic je drugi sistem koji radi na
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

- Za održavanje kontakta na planinarenju, na moru i na festivalima gde je mobilna mreža
  preopterećena ili je nema.
- Kao rezervni kanal za porodicu ili komšije kada nestane struje ili otkažu mobilne mreže.
- Za lokalno dopisivanje na radio-uređajima koji pripadaju samim korisnicima.
- Za eksperimentisanje sa radiom, antenama, solarnom energijom i softverom otvorenog koda.

## Odakle potiču podaci {#data}

Pretraga na stranici [lokalnih grupa](/community/) pronalazi mesto pomoću kopije
besplatnih spiskova mesta i poštanskih brojeva sa sajta [GeoNames](https://www.geonames.org/),
pod licencom
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopija se nalazi na
ovom sajtu. Tvoja pretraga nikada ne napušta tvoj uređaj i nijedan zahtev ne ide ka
sajtu GeoNames.
