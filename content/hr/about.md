---
title: Što je MeshCore?
lead: MeshCore šalje tekstualne poruke radiovezom, od čvora do čvora. Radi bez interneta i bez pretplate.
description: 'Što MeshCore jest, a što nije: mesh, companioni, repetitori i room serveri, usmjeravanje, šifriranje i pojas 868 MHz u Europi.'
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

MeshCore je besplatan softver za male LoRa radiouređaje. LoRa je radijska tehnika koja malo podataka šalje daleko, uz vrlo malo energije. Radiouređaj s MeshCoreom zove se *čvor*. Povežeš li ga s aplikacijom na mobitelu ili laptopu, ili koristiš njegov vlastiti zaslon i tipkovnicu, šalješ tekst ljudima udaljenima kilometrima. Između tebe i njih nema ni antenskog stupa, ni usmjerivača, ni operatera.

Softver je otvorenog koda. Razvija se na [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) pod licencom MIT.

## Što MeshCore nije {#not}

Radio ti je novost? Evo što ljudi najčešće očekuju od MeshCorea, a on to ne radi.

- **Nije internet ni telefon.** MeshCore šalje kratke tekstualne poruke, otprilike duljine SMS-a na mobitelu. Nema glasa, fotografija, videa ni web-stranica, a do običnog telefonskog broja ne možeš doprijeti.
- **Nije hitna služba.** Nijedna hitna služba ne prati mesh i nitko ne jamči da će netko pročitati tvoju poruku. U hitnom slučaju nazovi 112.
- **Nije trenutačan i nije svugdje.** Poruka skače s radiouređaja na radiouređaj i može putovati nekoliko sekundi ili uopće ne stići. Hoće li proći, ovisi o repetitorima oko tebe, o visini, zgradama i tvojoj anteni. Mali radiouređaj u zatvorenom često ne dosegne nikoga, a repetitor na krovu doseže kilometrima daleko.
- **Nije usluga koju netko vodi za tebe.** Nema operatera, korisničke podrške ni obećane pokrivenosti. Mesh postoji tamo gdje su ljudi iz zajednice postavili repetitore, i nigdje drugdje.
- **Nije sve na njemu privatno.** Izravne poruke su šifrirane, ali Public i hashtag kanale može čitati svatko. Ime tvojeg čvora i položaj koji dijeliš vidi svatko u dometu. [Promatrači](/network/) ono što čuju javljaju javnim kartama. [Odjeljak o šifriranju](#encryption) objašnjava što ostaje privatno.
- **Nije neograničen.** Svi na nekom području dijele jedan radijski kanal, a pravila za [pojas 868 MHz](#band) ograničavaju koliko dugo svaki radiouređaj smije slati. Svaka poruka svima ostalima oduzima vrijeme u eteru, pa botovi, česti oglasi i testne poruke usporavaju mesh za sve.
- **Nije Meshtastic.** Meshtastic je drugi sustav koji radi na uglavnom istim pločicama. Ta dva sustava ne mogu međusobno komunicirati.

## Mesh u jednoj minuti {#mesh}

Jedan LoRa radiouređaj u gradu doseže nekoliko kilometara, a s brda ili krova mnogo dalje. Za veći domet radiouređaji prenose poruke jedni za druge: to je *mesh*. U MeshCoreu poruke prenose radiouređaji koji se zovu *repetitori*. Repetitor koji čuje poruku ponovno je pošalje, pa ona može prijeći cijelu regiju.

Mesh nije ničiji. Svaki čvor i svaki repetitor pripada nekome iz zajednice. Mesh seže dokle sežu njihovi repetitori.

## 3 vrste čvorova {#roles}

Vrstu čvora biraš kad ga flashaš. Tvoj prvi čvor je companion.

**Companion.** Tvoj osobni radiouređaj. Povezuje se s aplikacijom MeshCore na mobitelu ili laptopu preko Bluetootha ili USB-a, a neki imaju vlastiti zaslon i tipkovnicu. U aplikaciji čitaš i tipkaš. Companion čuva tvoje kontakte i kanale te poruke koje su stigle dok aplikacija nije bila povezana. Companion ne prenosi poruke za druge.

**Repetitor.** Radiouređaj postavljen visoko koji prenosi poruke za sve. Većina radi na solarnu energiju. Vlastiti ti treba samo tamo gdje mesh još ne doseže. Nema vlastite aplikacije. Postavljaš ga preko USB-a ili se prijaviš lozinkom i upravljaš njime radiovezom. [Vodič za repetitore](/repeater-guide/) pokazuje kako.

**Room server.** Mala oglasna ploča na meshu. Kad se prijaviš, dobiješ objave koje si propustio dok si bio izvan dometa, najviše zadnje 32. Room server ih čuva samo u memoriji, pa ih ponovno pokretanje ili nestanak struje briše. Lokalna ga grupa koristi za obavijesti.

## Kako poruka pronalazi put {#routing}

Svaki čvor ima tajni i javni ključ. Javni ključ je njegov identitet. Čvor se najavljuje *oglasom*: to je potpisani paket s njegovim imenom i, ako želiš, položajem. Netko se pojavi među tvojim kontaktima kad do tebe stigne jedan od njegovih oglasa ili kad skeniraš njegov QR kod. Aplikacija ima gumb za slanje tvojeg oglasa.

Tvoja prva poruka kontaktu odlazi kao *flood*. Svaki repetitor koji je čuje prenese je jednom i usput doda svoj kratki ID. Odgovor vraća taj popis ID-ova. Otada tvoje poruke tom kontaktu idu zabilježenom rutom i šalju ih samo repetitori na njoj. Kad se ruta prekine, aplikacija ponovno šalje flood.

Poruke na kanal nemaju jednu adresu, pa uvijek idu kao flood. Repetitori pamte što su nedavno prenijeli i odbacuju kopije koje ponovno stignu drugom rutom. Poruka može proći kroz najviše 64 repetitora, ili 32 ako preset koristi 2-bajtne ID-ove.

## Šifriranje i privatnost {#encryption}

Tvoje izravne poruke šifrirane su s kraja na kraj: mogu ih čitati samo ti i druga osoba. Repetitor o primatelju paketa vidi samo 1-bajtni nagovještaj.

Kanali su šifrirani zajedničkim ključem, pa njihovo čitanje ovisi o tome tko ima taj ključ:

- **Public** je postavljen na svakom companionu. Njegov ključ je objavljen, pa taj kanal svatko može čitati.
- **Hashtag kanali**, poput `#utrecht`, dobivaju ključ iz svojeg imena. Svatko tko zna ime može se pridružiti, pa i njih smatraj javnima.
- **Privatni kanali** koriste nasumičan ključ koji sam dijeliš, na primjer kao QR kod.

Oglasi su potpisani, ali nisu šifrirani. Ime tvojeg čvora i njegov položaj, ako ga dijeliš, vidi svatko u dometu. Odaberi ime koje ne otkriva više nego što želiš.

## Pojas 868 MHz u Europi {#band}

U Europi MeshCore koristi mali dio pojasa 868 MHz koji svatko smije koristiti bez dozvole. Njegov europski radijski preset, EU/UK (Narrow), nalazi se na 869.618 MHz, na kanalu širine 62.5 kHz. To je unutar podpojasa 869.40-869.65 MHz, koji dopušta najviše 500 mW e.r.p. Uređaj tamo smije slati najviše 10% vremena. [Pravni odjeljak vodiča za repetitore](/repeater-guide/#legal) donosi pojedinosti i ograničenja po državama.

Svi na nekom području koriste isti preset, inače se njihovi radiouređaji ne mogu čuti. Neke države i regije koriste inačicu: tvoja [lokalna grupa](/community/) zna koju.

## Za što ga ljudi koriste {#uses}

- Za održavanje kontakta na planinarenju, na moru i na festivalima gdje je mobilna mreža preopterećena ili je nema.
- Kao rezervni kanal za obitelj ili susjede kad nestane struje ili mobilne mreže.
- Za lokalni chat na radiouređajima koje ljudi sami posjeduju.
- Za eksperimentiranje s radiovezom, antenama, solarnom energijom i softverom otvorenog koda.

## Odakle dolaze podaci {#data}

Pretraga na stranici [lokalnih grupa](/community/) pronalazi mjesto pomoću kopije besplatnih popisa mjesta i poštanskih brojeva iz [GeoNamesa](https://www.geonames.org/), pod licencom [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopija se nalazi na ovom web-mjestu. Tvoja pretraga nikad ne napušta tvoj uređaj i nijedan zahtjev ne ide prema GeoNamesu.
