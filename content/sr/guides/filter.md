---
title: Filter paketa
lead: 'Spreči da tvoj repetitor prosleđuje smeće: poplave iz daljine, bota koji nikad ne staje, bučan kanal. Prvo isprobaj podešavanje, pa ga onda uključi.'
description: 'Filter paketa u DMC firmveru za repetitore: šta odbacuje, gotova podešavanja za običan i opterećen repetitor, sve komande filtera s početnim vrednostima i kako da vidiš šta je odbačeno.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-11-02'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Repetitor (čvor koji prosleđuje poruke) ponavlja sve što čuje.
U opterećenoj mreži među tim ima i smeća. Neki bot objavljuje poruku svakog minuta. Neki čvor
na svakih nekoliko minuta ponovo šalje svoj advert, pozdrav po kojem ga drugi pronalaze.
Stižu i poruke koje su prešle pola zemlje. Svako ponavljanje oduzima
vreme emitovanja svima oko tebe. Uz filter paketa tvoj repetitor odbacuje
takav saobraćaj i ne prosleđuje ga. Da prvo saznaš šta preplavljuje tvoju mrežu
i šta još pomaže osim filtera, pogledaj
[Kako da mreža bude otpornija](/guides/resilient/).

{{< callout type="warning" >}}
Filter paketa je deo **DMC firmvera za repetitore**, verzije
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) za repetitore. Standardni
MeshCore nema filter paketa. Ima `region denyf *` i
`set flood.max.unscoped`, opisane na stranici [CLI komande](/guides/cli/). Ovaj
vodič prati dev verziju 1.18.0 `ecfb2d4` od 19. oktobra 2026. Stabilna
verzija 1.17.1 ima samo filtere za hopove, učestalost, kanale, hash i neispravne poruke.
Nema ni dry-run.
{{< /callout >}}

## Šta filter radi {#what}

Filter proverava samo pakete koje tvoj repetitor prosleđuje plavljenjem (šalje ih
svim čvorovima u dometu). Nikad ne dira ono što tvoj repetitor sam šalje,
niti pakete koji poznatom rutom idu do jednog čvora. Prolaze i direktne poruke
i zahtevi od tvojih kontakata i ka njima. Filter može da odbaci:

- pakete koji su već prošli kroz onoliko repetitora (hopova) koliko dozvoljavaš,
  posebno za svaki tip paketa;
- više paketa jednog tipa u minutu nego što dozvoljavaš;
- advert čvora koji je već poslao advert u poslednjih nekoliko sati;
- poruke na kanalu koji blokiraš;
- sve što je prošlo kroz jedan repetitor koji blokiraš;
- grupne poruke jednog pošiljaoca ili s jednom rečju, ili samo deo njih;
- grupne poruke koje su neispravne ili starije nego što dozvoljavaš.

Filter je **isključen** dok ga ne uključiš. Podešavaš ga komandama. Možeš da ih
ukucaš preko USB-a u [serijskoj konzoli](/firmware/console/) na ovom sajtu. Možeš i da ih
pošalješ iz MeshCore aplikacije, kao u
[vodiču za repetitore](/repeater-guide/#config).

## Nabavi firmver {#firmware}

Fleširaj **DutchMeshCore Repeater** pomoću flešera u
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Observer
firmver iz vodiča [MQTT na tvom observeru](/guides/mqtt/) ima isti filter.

## Prvo isprobaj {#dryrun}

U dry-run režimu filter broji svaki paket koji bi odbacio, ali ga ipak
prosleđuje. Tako možeš da odmeriš podešavanje pre nego što filter išta odbaci:

```text
filter on
filter dryrun on
```

Dok je dry-run uključen, statusni red komande `filter` završava se sa `(dry-run)`. Brojači
pokazuju šta bi filter odbacio. Pusti ga da radi jedan dan, pa ih pogledaj
(vidi [Šta je odbačeno](#stats)). Kad ti brojevi deluju kako treba, uključi
pravo odbacivanje:

```text
filter dryrun off
```

## Preporučena podešavanja {#configs}

### Običan repetitor {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Prolazi do 20 grupnih poruka u minutu i do 5 direktnih poruka u minutu,
a neispravne grupne poruke se odbacuju. Uobičajeno podešavanje samog firmvera dozvoljava
20 direktnih poruka u minutu. Ova stranica koristi 5, koliko firmver savetuje
od poplave direktnih poruka u julu 2026.

### Opterećen repetitor {#busy}

Za repetitor na visokoj lokaciji koji čuje ceo region ili za repetitor koji je
preplavljen:

```text
filter on
filter malformed on
filter rate 05 10 60
filter rate 02 5 60
filter rate 04 5 60
filter advert 24
filter hops 05 16
filter hops 02 16
filter hops 04 8
```

Ovo prepolovljava grupne poruke i adverte i propušta advert svakog čvora jednom dnevno.
Odbacuju se poruke koje su već prošle kroz 16 repetitora. Posle
restarta prolazi po jedan advert svakog čvora. Dokumentacija firmvera ovde navodi i
`filter hash 2`, a ova stranica to izostavlja (razlog je u odeljku
[Sva podešavanja](#settings)).

### Blokiraj bučan kanal {#channel}

```text
filter channel add #bot
```

Tvoj repetitor i dalje čuje kanal. Više ga ne prosleđuje drugim
repetitorima i companion uređajima (čvorovima s kojih ljudi šalju poruke). Najviše 16 kanala.

### Uspori jednog pošiljaoca {#sender}

Za bota koji prečesto objavljuje na kanalu koji želiš da zadržiš:

```text
filter watch add #test
filter sender add Bob 60
```

Bobove poruke na kanalu Public i na `#test` sada prolaze jednom u minutu, a
ostale se odbacuju. Filter proverava ime u poruci, pa ga pošiljalac koji promeni ime
zaobilazi.

### Blokiraj jedan repetitor na putanji {#path}

Kad smeće stiže kroz jedan repetitor, blokiraj njegov prefiks: prvi
deo njegovog ID-a, u heksadecimalnom zapisu (hex). Za to ti treba dev verzija 1.18. Verzija 1.17.1
nema filter putanje.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` prikazuje prefikse koje blokiraš, a `filter stats path` koliko
je koji odbacio. `filter path remove a1b2` ga ponovo propušta.
Kratak prefiks kao `a1` blokira i svaki drugi repetitor čiji ID počinje
sa `a1`. Koristi najduži prefiks koji možeš. Najviše 8 prefiksa.

## Sva podešavanja {#settings}

Tipove paketa navodiš brojem. Na repetitoru `filter types` prikazuje iste
brojeve s nazivima iz firmvera, kao što su `TXT_MSG` i `GRP_TXT`:

| Broj | Tip | Broj | Tip |
| --- | --- | --- | --- |
| `00` | zahtev | `06` | grupni podaci |
| `01` | odgovor | `07` | anonimni zahtev |
| `02` | direktna poruka | `08` | putanja |
| `03` | potvrda | `09` | praćenje |
| `04` | advert | `10` | višedelni paket |
| `05` | grupna poruka | `11` | kontrolni paket |

| Komanda | Šta radi | Početna vrednost |
| --- | --- | --- |
| `filter on` / `filter off` | Uključuje ili isključuje filter. | isključeno |
| `filter dryrun on` / `off` | Broji odbacivanja, ali i dalje sve prosleđuje. | isključeno |
| `filter hops <type> <max>` | Odbacuje tip paketa koji je već prošao kroz ovoliko repetitora, od 0 do 64. | 32 za grupne poruke, 8 za ostale |
| `filter rate <type> <limit> <secs> [soft]` | Prosleđuje najviše `limit` paketa jednog tipa na svakih `secs` sekundi. Sa `soft` prosleđivanje postepeno opada od `soft` do `limit`. `0` isključuje ograničenje. | 20 na 60 s za direktne i grupne poruke, 10 za adverte, 5 za ostale |
| `filter advert <hours>` | Propušta advert svakog čvora jednom na ovoliko sati, najviše 720. | 0 (isključeno) |
| `filter channel add <#name>` | Prestaje da prosleđuje kanal. | nema |
| `filter path add <hex>` | Odbacuje sve što je prošlo kroz repetitor s ovim prefiksom, od 2 do 8 hex cifara. | nema |
| `filter sender add <name> [secs] [prob]` | Odbacuje grupne poruke pošiljaoca na kanalu Public i na praćenim kanalima. `Bot*` obuhvata svako ime koje počinje sa Bot. | nema |
| `filter text add <word> [secs] [prob]` | Odbacuje grupne poruke koje sadrže reč, na kanalu Public i na praćenim kanalima. `^word` se poklapa samo na početku. | nema |
| `filter watch add <#name>` | Pravila za pošiljaoce i tekst čitaju i ovaj kanal, a možeš da dodaš do 4 kanala. Public se uvek čita. | Public |
| `filter malformed on` / `off` | Odbacuje Public poruke koje su prazne, neispravne ili s datumom koji odstupa više od nedelju dana (provera datuma čeka da sat bude podešen). | isključeno |
| `filter age <minutes>` / `off` | Odbacuje grupne poruke starije od ove vrednosti, na kanalu Public i na praćenim kanalima, od 1 do 10080. | isključeno |
| `filter hash <bytes>` | Odbacuje pakete čiji je ID putanje kraći od ove vrednosti, od 1 do 3. | 1 |
| `filter reset` | Vraća svako podešavanje na početnu vrednost. | |

Svako `add` ima svoje `remove` i `list`, na primer `filter channel remove #bot`.
U pravilima za pošiljaoce i tekst `secs` propušta jednu poruku na toliko sekundi.
`prob` primenjuje pravilo samo na taj udeo poklapanja, od 1 do 100. Najviše 8
pravila za pošiljaoce i 8 pravila za tekst. Imena i reči razlikuju velika i mala slova. Ime ima najviše
15 znakova, a reč najviše 23.

Dva podešavanja odbacuju više nego što možda očekuješ:

- `filter hash 2` odbacuje skoro sav saobraćaj. Čvorovi podrazumevano šalju ID-ove putanje
  od 1 bajta.
- `filter age` se oslanja na sat tvog repetitora. Podesi ga sa `clock sync` iz
  aplikacije, proveri ga sa `clock` i kreni s velikom rezervom: `filter age 60`.

Svako podešavanje ostaje sačuvano posle restarta.

## Šta je odbačeno {#stats}

`filter` prikazuje zbirove po razlogu:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` prikazuje detalje za jedno podešavanje. Teme su
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` i `age`. `filter stats top` prikazuje prvi bajt ID-ova čvorova
koji stoje iza najviše odbacivanja. Mnogo čvorova ima isti taj bajt.
`filter stats air` prikazuje vreme emitovanja koje je tvoj repetitor uštedeo jer ove
pakete nije prosledio.

Brojači ponovo kreću od 0 posle restarta i posle `clear stats`.
