---
title: Učini mesh otpornijim
lead: Je li mesh u tvojoj blizini spor ili pun smeća? Otkrij što to uzrokuje, uključi postavku repetitora koja to zaustavlja i javi svojoj lokalnoj grupi.
description: 'Poplave i spam na MeshCore meshu: kako prepoznati svaku vrstu, koja postavka repetitora pomaže, kako vidjeti poplavu i kako pronaći njezin izvor.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-11-02'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Stižu li ti poruke kasno ili uopće ne stižu? Puni li se Public smećem? To je
poplava: više prometa nego što mesh može prenijeti, poslano greškom ili
namjerno. Pronađi u tablicama ispod ono što vidiš. U svakom retku piše koja
postavka to zaustavlja. Uključi je na svojem repetitoru, čvoru koji prosljeđuje
poruke. Zatim javi svojoj [lokalnoj grupi](/community/) da isto učine i
repetitori oko tebe. Svaki repetitor koji odbaci poplavu ostavlja vrijeme u
eteru svima ostalima.

## Poplave nastale greškom {#mistake}

Poplavu nastalu greškom stvara čvor čiji vlasnik ne zna da je uzrokuje. Prestaje
čim to sazna. U tablicama ispod advert je pozdrav koji čvor šalje da ga drugi
mogu pronaći.

Postavke u tablicama temelje se na onome što firmware radi. Nije svaka od njih
dosad zaustavila poplavu na stvarnom meshu.

{{< callout type="warning" >}}
Za neke postavke na ovoj stranici treba ti DMC firmware. Standardni **MeshCore** 1.18.0
ima regije, ograničenja skokova `flood.max.*`, otkrivanje petlji i duty cycle. Filtar
paketa, pravila kojima tvoj repetitor odbacuje smeće, dolazi s **DMC firmwareom**
od [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). S njim dolaze i
duty-cycle gating i companion filtar. Ova stranica prati DMC 1.18.0 dev build
`ecfb2d4` od 19. listopada 2026.; na stranici
[filtar paketa](/guides/filter/#firmware) piše gdje ga možeš nabaviti.
{{< /callout >}}

| Što vidiš | Što je to | Što pomaže |
| --- | --- | --- |
| Zahtjevi repetitorima s jednog čvora, danju i noću, i mesh koji danima ostaje spor | Kućna automatizacija ili bot koji prečesto traži status od repetitora | `filter on`. Filtar paketa tada propušta 5 zahtjeva u minuti. Javi vlasniku. |
| Ista vrsta poruke na kanalu, svake minute | Bot koji prečesto objavljuje | [Blokiraj kanal](/guides/filter/#channel) ili [uspori pošiljatelja](/guides/filter/#sender). Javi vlasniku. |
| Nečitljive poruke na Publicu i drugim kanalima | Čvor s neispravnim firmwareom ili pogrešnim radijskim postavkama | `filter malformed on` odbacuje ih na Publicu. Javi vlasniku. |
| Advert jednog čvora svakih nekoliko minuta | Čvor namješten da prečesto šalje advert | `filter advert 24` propušta advert svakog čvora jednom dnevno. `set flood.max.advert 3` drži adverte unutar 3 skoka. |
| Poruke izdaleka, s regijama koje ovamo ne pripadaju | Most koji povezuje meshove preko interneta | `set flood.max.unscoped 1`, a repetitor stavi samo u [regije koje pokriva](/guides/settings/#traffic). |
| Ista poruka prolazi opet i opet, a ID tvojeg repetitora više se puta pojavljuje u njezinoj putanji | Repetitor koji mijenja pakete i prosljeđuje ih dalje, pa se vrte u petlji | Otkrivanje petlji zadano radi na razini `minimal`. `set loop.detect moderate` ranije odbacuje petlju. |

## Namjerne poplave {#purpose}

Neke poplave su spam: smeće koje netko namjerno šalje da zaguši mesh. Pošiljatelj
mijenja imena, ključeve i putanje, pa nijedno pojedinačno pravilo ne zaustavlja
poplavu.

| Što vidiš | Što je to | Što pomaže |
| --- | --- | --- |
| Mnogo novih čvorova s nasumičnim imenima, svaki s novim ključem | Lažni adverti | `filter rate 04 5 60` propušta 5 adverta u minuti. `filter advert` ne pomaže: svaki advert dolazi s [novog ključa](#forged). |
| Poruke s nečitljivim tekstom od izmišljenih pošiljatelja, često s datumom starijim od godine dana | Spam na kanalima | `filter malformed on` odbacuje ih na Publicu. `filter age 60` odbacuje one sa starim datumom na Publicu i na [nadziranim kanalima](/guides/filter/#settings). |
| Do 200 izravnih poruka u minuti prema čvorovima koji ne postoje, bez ijedne potvrde primitka | Poplava izravnih poruka | `filter rate 02 5 60`. Te poruke ne vidiš u svojoj aplikaciji, ali ih vidi promatrač. |
| Naleti zahtjeva s jednog čvora prema desecima drugih | Spam zahtjevima | Uz `filter on`, filtar paketa propušta 5 zahtjeva u minuti. |
| Poruka se vraća 10 do 20 minuta kasnije, s gotovo istom putanjom | Replay: ponovno poslana kopija | Repetitor pamti zadnjih 160 paketa koje je vidio, pa na prometnom meshu kasnija kopija opet prolazi. `filter age` odbacuje grupnu poruku stariju od granice koju zadaš. |
| Poruke s Publica ponovno poslane pod izmišljenim pošiljateljem, ponekad sa starim datumom | Echo spam | `filter age 60`. `filter malformed on` odbacuje i poruku čiji datum odstupa više od tjedan dana. |
| Poruka svakih nekoliko sekundi na više kanala, svaka s novim imenom i običnim pitanjima | Val botova | `filter rate 05 10 60`, a [blokiraj i kanale](/guides/filter/#channel) koje se u tvojem području ne koriste. Svako je ime novo, pa ga [pravila za pošiljatelje](#forged) ne hvataju. |

## Što je pomoglo {#worked}

Lokalne grupe zaustavile su poplave ovim koracima:

1. **Javi vlasniku.** Poplava nastala greškom prestaje čim njezin vlasnik sazna
   za nju. Pošalji mu prijateljsku poruku.
2. **Ne reagiraj na meshu.** Odgovor pokazuje spameru da spam djeluje.
3. **Zatraži promatrače.** Promatrač (observer) je čvor koji preko MQTT-a javlja
   svaki paket koji čuje. Što je više promatrača oko tebe, to ćeš prije vidjeti
   gdje poplava ulazi. Pretvori svoj repetitor u promatrača uz
   [MQTT na svojem promatraču](/guides/mqtt/).
4. **Pronađi izvor.** Promatrači smještaju pošiljatelja u neko područje. Zadnji
   kilometar ljudi prelaze pješice, s radiom u ruci. Pogledaj
   [Pronađi izvor](#source).
5. **Pokreni svoju lokalnu grupu.** Jedan repetitor s pravim postavkama pomaže.
   Poplavu zaustavljaju svi repetitori u području zajedno. Tvoja
   [lokalna grupa](/community/) potiče svakog vlasnika da uključi postavku.

## Izmišljeni pošiljatelji i putanje {#forged}

Ove dijelove paketa piše pošiljatelj i ništa ih ne provjerava:

- **Ime pošiljatelja.** U poruci na kanalu ime je dio teksta. Svatko tko ima
  ključ kanala može upisati bilo koje ime.
- **Početak putanje.** Svaki repetitor dodaje svoj ID na kraj putanje. Ništa ne
  provjerava ID-ove koji su već tamo, pa pošiljatelj može započeti putanju
  izmišljenima. Kraj putanje je stvaran.

{{< forged-path >}}

Zato `filter sender` i `filter path` zaustavljaju pošiljatelja samo dok ne
promijeni ime ili putanju. [Blokada putanje](/guides/filter/#path) odbacuje i
stvarni promet repetitora čiji se ID u njoj nalazi. Ograničenja brzine,
ograničenja skokova, provjere starosti i neispravnih poruka, blokade kanala,
regije i duty cycle i dalje rade.

## Postavke za svaku poplavu {#always}

Ove postavke vrijede kakva god poplava zahvatila mesh:

- **Duty cycle na 10%.** Tvoj repetitor tada nikad ne odašilje više nego što
  zakon dopušta, što god stizalo. Više o tome piše u
  [vodiču za repetitore](/repeater-guide/#duty-cycle).
- **Regije i ograničenja skokova.** Regija je područje unutar kojeg poruka ostaje.
  Repetitor prosljeđuje samo poruke u regijama koje ima, a `flood.max.*` drži
  promet u blizini. Oboje je opisano u
  [Smanji promet](/guides/settings/#traffic).
- **Filtar paketa za prometan repetitor.**
  [Gotove postavke](/guides/filter/#busy) prepolovljuju grupne poruke i adverte.
  Prvo ih isprobaj u načinu [dry-run](/guides/filter/#dryrun): on samo broji što
  bi odbacio.
- **Companion filtar, u DMC firmwareu.** Tvoj companion, čvor s kojeg šalješ
  poruke, ne pušta smeće u tvoju aplikaciju. Skriva neispravne i stare poruke te
  poruke od repetitora ili pošiljatelja koje blokiraš, kao i one s blokiranom
  riječi. Pravilo za pošiljatelja ili riječ skriva poruku samo od tebe; drugi je
  i dalje primaju.

### Duty-cycle gating {#gate}

U DMC firmwareu tvoj repetitor može dati prednost vlastitoj regiji kad postane
opterećen. Čim je odašiljao više od 35% zadnje minute, prestaje prosljeđivati
poruke bez regije. Ako ostane opterećen, zatim odbacuje najširu regiju, razinu po
razinu. Njegova vlastita regija uvijek prolazi. Gating radi samo s regijama
postavljenima na tvojem repetitoru. Uključi ga i provjeri:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Ono što odbaci ne vidi se u `filter stats`. Kad se repetitor ponovno smiri, regije
se vraćaju, počevši od najuže.

## Kako vidjeti poplavu {#see}

Tvoja aplikacija prikazuje samo ono što stigne do tebe. Poplavu izravnih poruka
prema nepostojećim čvorovima čuje samo promatrač. Svaki promatrač javlja promet
[MeshCore Analyzeru](https://meshcore-analyzer.eu/), gdje ga svatko može vidjeti.
Pretvori svoj repetitor u promatrača uz
[MQTT na svojem promatraču](/guides/mqtt/).

Na Analyzeru pogledaj svaku kopiju jednog paketa. Njegova putanja obično pokazuje
odakle je došao. Pošiljatelj poplave može započeti putanju
[izmišljenim ID-ovima](#forged), pa ti njezini prvi ID-ovi ne govore ništa. No
svaka kopija nosi isti izmišljeni početak. Kopija s najkraćom putanjom prošla je
najmanje stvarnih repetitora, pa je čuta najbliže pošiljatelju.

{{< copies >}}

Na tvojem repetitoru `filter stats` pokazuje što je filtar paketa odbacio.
`filter stats top` pokazuje prvi bajt ID-ova čvorova koji stoje iza većine
odbacivanja. Taj bajt dijele mnogi čvorovi, pa on sužava potragu, ali ne otkriva
pošiljatelja.

## Pronađi izvor {#source}

Kad se poplava stalno vraća:

1. **Prati putanje.** Čitaj putanju od kraja: zadnji ID-ovi su repetitori kroz
   koje je poplava prošla. Najraniji stvarni repetitor nalazi se blizu izvora;
   ID-ovi ispred njega mogu biti [izmišljeni](#forged).
2. **Suzi područje.** Više promatrača koji čuju isti paket smješta pošiljatelja u
   neko područje. [DMC Triangulator](https://triangulator.dutchmeshcore.nl/)
   izračunava područje na temelju repetitora koji su čuli paket.
3. **Prijeđi zadnji kilometar pješice.** Repetitori čuju izvor samo na rubu svojeg
   dometa, pa zadnji dio ljudi prelaze pješice.
   [Mesh-Hunter](https://mesh-hunter.eu/) se povezuje s tvojim companionom i uz tvoj
   GPS položaj bilježi svaki paket koji čuje. Više ljudi koji hodaju istodobno
   pronaći će izvor prije.
4. **Javi svojoj [lokalnoj grupi](/community/).** Oni vide veći dio mesha, odlučuju
   što dalje i kontaktiraju onoga tko namjerno stvara poplavu.

## Dodaj ono što si vidio {#add}

Je li te pogodila poplava koje nema u ovim tablicama? Je li neka postavka
zaustavila poplavu? Javi nam na [Discord](https://discord.meshcore-info.eu/): što
si vidio i što si uključio. Dodajemo to na stranicu.
