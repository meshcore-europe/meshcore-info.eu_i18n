---
title: Što je MeshCore?
lead: MeshCore šalje tekstualne poruke radiovezom, od čvora do čvora. Radi bez interneta i bez pretplate.
description: 'Što MeshCore jest, a što nije: vrste čvorova, usmjeravanje, šifriranje i pojas od 868 MHz.'
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

MeshCore je besplatan softver za male LoRa radiouređaje. LoRa je radijska tehnika koja malo podataka šalje daleko, uz vrlo malo energije. Radiouređaj s MeshCoreom zove se *čvor*. Povežeš li ga s aplikacijom na mobitelu ili laptopu, ili koristiš njegov vlastiti zaslon i tipkovnicu, šalješ tekst ljudima udaljenima kilometrima. Između tebe i njih nema ni antenskog stupa, ni usmjerivača, ni operatera.

Softver je otvorenog koda. Razvija se na [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) pod licencom MIT.

## Što MeshCore nije {#not}

Radio ti je novost? Evo što ljudi najčešće očekuju od MeshCorea, a on to ne radi.

- **Nije internet ni telefon.** MeshCore šalje kratke tekstualne poruke,
  otprilike duge kao SMS na tvom mobitelu. Nema glasa, fotografija, videa
  ni web-stranica, a običan telefonski broj ne možeš dobiti.
- **Nije hitna služba.** Nijedna hitna služba ne obećava da sluša mesh.
  Znamo da mesh može raditi. Radi li i u hitnom slučaju, nitko ne zna.
- **Nije trenutačan i nije posvuda.** Poruka skače od radija do radija i
  može putovati nekoliko sekundi, ili uopće ne stići. Hoće li proći, ovisi o
  repetitorima oko tebe, o visini, zgradama i tvojoj anteni. Mali radio u
  zatvorenom često ne dosegne nikoga. Repetitor na krovu dosegne kilometre.
- **Nije usluga koju netko vodi za tebe.** Nema pružatelja usluge, nema
  korisničke podrške i nema obećanja o pokrivenosti. Mesh postoji tamo gdje
  su ljudi iz zajednice postavili repetitore.
- **Nije sve na njemu privatno.** Izravne poruke su šifrirane. Public i
  hashtag kanale ipak može čitati svatko, a ime tvog čvora i podijeljenu
  poziciju vide svi u dometu.
  [Observeri](/network/) šalju ono što čuju na javne karte. U
  [odjeljku o šifriranju](#encryption) piše što ostaje privatno.
- **Nije neograničen.** Svi na jednom području dijele jedan radijski kanal,
  a pravila za [pojas od 868 MHz](#band) ograničavaju koliko dugo svaki radio
  smije slati. Svaka poruka oduzima vrijeme emitiranja svima ostalima. Zato
  botovi, česti adverti i probne poruke usporavaju mesh za sve.
- **Nije Meshtastic.** Meshtastic je drugi sustav koji radi na gotovo istim
  pločicama. Ta dva sustava ne mogu međusobno komunicirati.

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

- Održavanje veze na planinarenju, na moru i na festivalima gdje je mobilna mreža
  preopterećena ili je nema.
- Rezervni kanal za obitelj ili susjede kad nestane struje ili mobilne
  mreže.
- Rezervna veza za lokalne vlasti kad njihove uobičajene mreže zakažu.
- Lokalni razgovor na radiouređajima koje ljudi sami posjeduju.
- Održavanje veze unutar tima za potragu i spašavanje gdje nema mobilne mreže.
  MeshCore SAR, aplikacija zajednice na stranici [Projekti](/projects/), dodaje karte i
  dijeljene lokacije.
- Provjera udaljene lokacije od kuće. Repetitori i senzorski čvorovi javljaju
  napon baterije i druga očitanja kad ih pitaš.
- Praćenje senzora. Na senzorskom čvoru radi MeshCoreov firmware za mjerenje.
  Čuva povijest napona svoje baterije. Prijavi se kao admin i upozorit će te
  kad baterija oslabi. Upozorenja za druga očitanja dodaješ
  vlastitim kodom.
- Uključivanje i isključivanje nečega udaljenog, poput pumpe. To dodaješ u
  firmware senzora vlastitim kodom.
- Eksperimentiranje s radiom, antenama, solarnom energijom i softverom otvorenog koda.

Neke vlasti grade ili testiraju rezervnu vezu na MeshCoreu. Ove smo primjere
provjerili u studenom 2026.

- Ciklon Gabrielle prekinuo je sve komunikacije u Tairāwhitiju na Novom Zelandu. U
  rujnu 2025. tamošnja služba za upravljanje kriznim situacijama navela je MeshCore kao
  [jedan od najmanje 6 rezervnih načina komunikacije](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Ta je služba gradila i solarne repetitore kao okosnicu mreže.
- Njemački okrug Bad Kissingen
  [gradi tekstualnu mrežu na MeshCoreu](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  za vlasti, hitne službe i ključne objekte. Prve se spajaju
  vatrogasne postaje.
- Gradsko vijeće Hilversuma u Nizozemskoj
  [s 34 glasa prema 1 odobrilo je probu](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  s repetitorom na tornju gradske vijećnice. Općina
  [će je ocijeniti u jesen 2027.](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/)
- Dvije nizozemske sigurnosne regije, koje organiziraju odgovor na krizu,
  eksperimentiraju s MeshCoreom:
  [Južni Limburg](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  i [Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Drenthe kaže da je prerano reći kako ili kada bi ga mogla koristiti.
- U Dalfsenu, također u Nizozemskoj, volonteri
  [vode pilot-projekt zajedno s općinama](https://noodnetoverijssel.nl/).
  Kao prvi sloj koriste glasovni radio, a MeshCore kao drugi sloj za tekst.

Radi li mesh u tvojoj blizini u hitnom slučaju, nitko ne zna.

## Odakle dolaze podaci {#data}

Pretraga na stranici [lokalnih grupa](/community/) pronalazi mjesto pomoću kopije besplatnih popisa mjesta i poštanskih brojeva iz [GeoNamesa](https://www.geonames.org/), pod licencom [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopija se nalazi na ovom web-mjestu. Tvoja pretraga nikad ne napušta tvoj uređaj i nijedan zahtjev ne ide prema GeoNamesu.
