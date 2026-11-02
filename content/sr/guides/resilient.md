---
title: Učini mrežu otpornom
lead: Da li je mreža u tvojoj blizini spora ili puna smeća? Otkrij uzrok, uključi podešavanje repetitora koje to zaustavlja i javi svojoj lokalnoj grupi.
description: 'Poplave i spam na MeshCore mreži: kako da prepoznaš svaku vrstu, koje podešavanje repetitora pomaže, kako da vidiš poplavu i pronađeš njen izvor.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-11-02'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Stižu li poruke kasno ili uopšte ne stižu? Puni li se Public smećem? To je
poplava: više saobraćaja nego što mreža može da podnese, poslatog greškom ili
namerno. U tabelama ispod pronađi ono što vidiš. U svakom redu piše koje
podešavanje to zaustavlja. Uključi ga na svom repetitoru, čvoru koji prosleđuje
poruke. Zatim javi svojoj [lokalnoj grupi](/community/), da isto urade i
repetitori oko tebe. Svaki repetitor koji odbaci poplavu ostavlja vreme za
emitovanje svima ostalima.

## Poplave nastale greškom {#mistake}

Poplavu nastalu greškom izaziva čvor čiji vlasnik to ne zna. Prestaje čim
vlasnik sazna. U tabelama ispod, advert je pozdrav koji čvor šalje da bi ga
drugi pronašli.

Podešavanja u tabelama proizlaze iz onoga što firmver radi. Neka od njih još
nisu zaustavila poplavu na stvarnoj mreži.

{{< callout type="warning" >}}
Neka podešavanja na ovoj stranici zahtevaju DMC firmver. Standardni **MeshCore** 1.18.0
ima regione, ograničenja hopova `flood.max.*`, detekciju petlji i duty cycle. Filter
paketa, pravila kojima tvoj repetitor odbacuje smeće, dolazi sa **DMC firmverom** iz
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Isto važi za
duty-cycle gating i companion filter. Ova stranica prati DMC
1.18.0 dev build `ecfb2d4` od 19. oktobra 2026; na stranici
[filter paketa](/guides/filter/#firmware) piše gde možeš da ga nabaviš.
{{< /callout >}}

| Šta vidiš | Šta je to | Šta pomaže |
| --- | --- | --- |
| Zahtevi repetitorima sa jednog čvora, danju i noću, i mreža koja danima ostaje spora | Kućna automatizacija ili bot koji prečesto traži status od repetitora | `filter on`. Filter paketa tada propušta 5 zahteva u minuti. Javi vlasniku. |
| Ista vrsta poruke na kanalu, svakog minuta | Bot koji prečesto objavljuje | [Blokiraj kanal](/guides/filter/#channel) ili [uspori pošiljaoca](/guides/filter/#sender). Javi vlasniku. |
| Nečitljive poruke na kanalu Public i drugim kanalima | Čvor sa neispravnim firmverom ili pogrešnim radio podešavanjima | `filter malformed on` ih odbacuje na kanalu Public. Javi vlasniku. |
| Advert jednog čvora na svakih nekoliko minuta | Čvor podešen da prečesto šalje advert | `filter advert 24` propušta advert svakog čvora jednom dnevno. `set flood.max.advert 3` zadržava adverte unutar 3 hopa. |
| Poruke izdaleka, sa regionima kojima ovde nije mesto | Most koji povezuje mreže preko interneta | `set flood.max.unscoped 1`, a repetitor stavi samo u [regione koje pokriva](/guides/settings/#traffic). |
| Ista poruka prolazi iznova i iznova, a ID tvog repetitora se u putanji javlja više puta | Repetitor koji menja pakete i prosleđuje ih, pa oni kruže u petlji | Detekcija petlji podrazumevano radi na `minimal`. `set loop.detect moderate` ranije odbacuje petlju. |

## Namerne poplave {#purpose}

Neke poplave su spam: smeće koje neko namerno šalje da zaguši mrežu. Pošiljalac
menja imena, ključeve i putanje, pa nijedno pojedinačno pravilo ne zaustavlja
poplavu.

| Šta vidiš | Šta je to | Šta pomaže |
| --- | --- | --- |
| Mnogo novih čvorova sa nasumičnim imenima, svaki sa novim ključem | Lažni adverti | `filter rate 04 5 60` propušta 5 adverta u minuti. `filter advert` ne pomaže: svaki advert dolazi sa [novog ključa](#forged). |
| Poruke sa nečitljivim tekstom od izmišljenih pošiljalaca, često sa datumom starijim od godinu dana | Spam na kanalima | `filter malformed on` ih odbacuje na kanalu Public. `filter age 60` odbacuje one sa starim datumom na kanalu Public i na [praćenim kanalima](/guides/filter/#settings). |
| Do 200 direktnih poruka u minuti ka čvorovima koji ne postoje, bez potvrda prijema | Poplava direktnih poruka | `filter rate 02 5 60`. Tvoja aplikacija ne prikazuje ove poruke, ali observer ih prikazuje. |
| Naleti zahteva sa jednog čvora ka desetinama drugih | Spam zahtevima | Sa `filter on`, filter paketa propušta 5 zahteva u minuti. |
| Poruka se vraća 10 do 20 minuta kasnije, sa skoro istom putanjom | Replay: kopija poslata ponovo | Repetitor pamti poslednjih 160 paketa koje je video, pa na prometnoj mreži kasnija kopija opet prolazi. `filter age` odbacuje grupnu poruku stariju od granice koju zadaš. |
| Poruke sa kanala Public ponovo poslate pod izmišljenim pošiljaocem, ponekad sa starim datumom | Echo spam | `filter age 60`. `filter malformed on` odbacuje i poruku čiji datum odstupa više od nedelju dana. |
| Poruka na svakih nekoliko sekundi na više kanala, svaka pod novim imenom, sa običnim pitanjima | Talas botova | `filter rate 05 10 60`, a uz to [blokiraj kanale](/guides/filter/#channel) koje tvoje područje ne koristi. Svako ime je novo, pa ih [pravila za pošiljaoce](#forged) ne hvataju. |

## Šta je pomoglo {#worked}

Lokalne grupe su zaustavljale poplave ovim koracima:

1. **Javi vlasniku.** Poplava nastala greškom prestaje čim vlasnik sazna. Pošalji
   mu prijateljsku poruku.
2. **Ne reaguj na mreži.** Odgovor pokazuje spameru da spam deluje.
3. **Zatraži observere.** Observer je čvor koji preko MQTT-a prijavljuje svaki paket
   koji čuje. Što je više observera oko tebe, to pre vidiš gde poplava ulazi.
   Svoj repetitor pretvori u observer pomoću vodiča
   [MQTT na tvom observeru](/guides/mqtt/).
4. **Pronađi izvor.** Observeri određuju područje u kome je pošiljalac. Za poslednji
   kilometar ljudi moraju peške, sa radiom. Pogledaj
   [Pronađi izvor](#source).
5. **Pokreni svoju lokalnu grupu.** Jedan repetitor sa pravim podešavanjima
   pomaže. Svi repetitori u području zajedno zaustavljaju poplavu. Tvoja
   [lokalna grupa](/community/) navodi svakog vlasnika da uključi podešavanje.

## Izmišljeni pošiljaoci i putanje {#forged}

Ove delove paketa piše pošiljalac i niko ih ne proverava:

- **Ime pošiljaoca.** U poruci na kanalu ime je deo teksta. Svako ko ima
  ključ kanala može da upiše bilo koje ime.
- **Početak putanje.** Svaki repetitor dodaje svoj ID na kraj putanje. Niko ne
  proverava ID-jeve koji su već tu, pa pošiljalac može da započne putanju
  izmišljenim ID-jevima. Kraj putanje je stvaran.

{{< forged-path >}}

Zato `filter sender` i `filter path` zaustavljaju pošiljaoca samo dok ne promeni
ime ili putanju. [Blokada putanje](/guides/filter/#path) odbacuje i stvarni
saobraćaj repetitora čiji je ID u njoj. Ograničenja brzine, ograničenja hopova,
provere starosti i neispravnih poruka, blokade kanala, regioni i duty cycle i
dalje rade.

## Podešavanja za svaku poplavu {#always}

Ovo važi bez obzira na to čime je mreža preplavljena:

- **Duty cycle na 10%.** Tvoj repetitor tada nikad ne emituje više nego što zakon
  dozvoljava, šta god da stigne. O tome piše
  [vodič za repetitore](/repeater-guide/#duty-cycle).
- **Regioni i ograničenja hopova.** Region je područje u kome poruka ostaje.
  Repetitor prosleđuje samo poruke iz regiona koje ima, a
  `flood.max.*` drži saobraćaj u blizini. Oboje je opisano u delu
  [Smanji saobraćaj](/guides/settings/#traffic).
- **Filter paketa za prometan repetitor.** [Gotova podešavanja](/guides/filter/#busy)
  prepolovljuju grupne poruke i adverte. Prvo ih isprobaj u
  [dry-run režimu](/guides/filter/#dryrun): on samo broji ono što bi odbacio.
- **Companion filter, u DMC firmveru.** Tvoj companion, čvor sa kog šalješ poruke,
  sprečava da smeće stigne u tvoju aplikaciju. Skriva neispravne i stare poruke,
  kao i poruke od repetitora ili pošiljaoca koje blokiraš i poruke sa rečju koju
  blokiraš. Pravilo za pošiljaoca ili reč
  skriva poruku samo od tebe; drugi je i dalje primaju.

### Duty-cycle gating {#gate}

U DMC firmveru tvoj repetitor može da daje prednost svom regionu kad postane
zauzet. Kad emituje tokom više od 35% poslednjeg minuta, prestaje da prosleđuje
poruke bez regiona. Ako ostane zauzet, zatim odbacuje najširi region, nivo po nivo.
Njegov region uvek prolazi. Ovo radi samo ako su na tvom repetitoru podešeni
regioni. Uključi gating i proveri:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Ono što gating odbaci ne vidi se u `filter stats`. Kad se repetitor ponovo smiri,
regioni se vraćaju, prvo oni najuži.

## Kako da vidiš poplavu {#see}

Tvoja aplikacija prikazuje samo ono što stigne do tebe. Poplavu direktnih poruka
ka nepostojećim čvorovima čuje samo observer. Svaki observer šalje izveštaje
na [MeshCore Analyzer](https://meshcore-analyzer.eu/), gde svako može da ih vidi.
Svoj repetitor pretvori u observer pomoću vodiča
[MQTT na tvom observeru](/guides/mqtt/).

Na Analyzeru pogledaj svaku kopiju jednog paketa. Njegova putanja obično pokazuje
odakle je došao. Pošiljalac poplave može da započne putanju
[izmišljenim ID-jevima](#forged), pa ti prvi ID-jevi ništa ne govore. Ali svaka kopija
nosi isti izmišljeni početak. Kopija sa najkraćom putanjom prošla je kroz najmanje
stvarnih repetitora, pa je čuta najbliže pošiljaocu.

{{< copies >}}

Na tvom repetitoru `filter stats` pokazuje šta je filter paketa odbacio.
`filter stats top` pokazuje prvi bajt ID-jeva čvorova koji stoje iza većine
odbacivanja. Mnogi čvorovi imaju isti taj bajt, pa on sužava pretragu, ali ne
otkriva pošiljaoca.

## Pronađi izvor {#source}

Kad se poplava stalno vraća:

1. **Prati putanje.** Čitaj putanju od kraja: poslednji ID-jevi su repetitori kroz
   koje je poplava prošla. Najraniji stvarni je blizu izvora; ID-jevi pre njega
   mogu biti [izmišljeni](#forged).
2. **Suzi područje.** Više observera koji čuju isti paket određuje područje u kome
   je pošiljalac. [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) to izračunava
   na osnovu repetitora koji su ga čuli.
3. **Pređi poslednji kilometar peške.** Repetitori čuju izvor samo na ivici svog
   dometa, pa za poslednji deo ljudi moraju peške.
   [Mesh-Hunter](https://mesh-hunter.eu/) se povezuje sa tvojim companionom i beleži
   svaki paket koji čuje, uz tvoju GPS poziciju. Više ljudi koji hodaju u isto vreme
   brže ga pronalazi.
4. **Javi svojoj [lokalnoj grupi](/community/).** Oni vide veći deo mreže, odlučuju
   šta dalje i kontaktiraju onog ko namerno pravi poplavu.

## Dodaj ono što si video {#add}

Da li te je pogodila poplava koje nema
u ovim tabelama? Da li je neko podešavanje zaustavilo poplavu? Javi nam na
[Discordu](https://discord.meshcore-info.eu/): šta si video i šta si
uključio. Mi to dodajemo na stranicu.
