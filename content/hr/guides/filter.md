---
title: Filtar paketa
lead: 'Spriječi da tvoj repetitor prosljeđuje smeće: poplave izdaleka, bota koji nikad ne staje, bučan kanal. Prvo isprobaj postavku, a zatim je uključi.'
description: 'Filtar paketa u DMC firmwareu za repetitore: što odbacuje, gotove postavke za običan i opterećen repetitor, sve naredbe filtra sa zadanim vrijednostima i kako vidjeti što je odbacio.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-11-02'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Repetitor (čvor koji prosljeđuje poruke) ponavlja sve što čuje.
U opterećenoj mreži među tim porukama ima i smeća. Neki bot objavljuje poruku svake minute. Jedan čvor
svakih nekoliko minuta ponovno šalje svoj advert, pozdrav po kojem ga drugi pronalaze.
Stižu i poruke koje su prešle pola države. Svako ponavljanje oduzima
vrijeme emitiranja svima oko tebe. S filtrom paketa tvoj repetitor odbacuje
takav promet i ne prosljeđuje ga. Da prvo saznaš što preplavljuje tvoju mrežu i što
pomaže osim filtra, pročitaj vodič
[Otpornija mreža](/guides/resilient/).

{{< callout type="warning" >}}
Filtar paketa dio je **DMC firmwarea za repetitore**, inačice
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) za repetitore. Standardni
MeshCore nema filtar paketa. Ima naredbe `region denyf *` i
`set flood.max.unscoped`, opisane na stranici [Naredbe CLI](/guides/cli/). Ovaj
vodič prati razvojnu inačicu 1.18.0 `ecfb2d4` od 19. listopada 2026. Stabilna
inačica 1.17.1 ima samo filtre za skokove, učestalost, kanale, hash i neispravne poruke.
Nema ni probnog načina rada (dry-run).
{{< /callout >}}

## Što filtar radi {#what}

Filtar gleda samo pakete koje tvoj repetitor prosljeđuje preplavljivanjem (šalje ih
svim čvorovima u dometu). Nikad ne dira ono što tvoj repetitor sam šalje
ni pakete koji poznatom rutom idu do jednog čvora. Prolaze i izravne poruke
te zahtjevi prema tvojim kontaktima i od njih. Filtar može odbaciti:

- pakete koji su već prošli onoliko repetitora (skokova) koliko dopuštaš, po
  vrsti paketa;
- više paketa jedne vrste u minuti nego što dopuštaš;
- advert čvora koji je već poslao advert u posljednjih nekoliko sati;
- poruke na kanalu koji blokiraš;
- sve što je došlo preko jednog repetitora koji blokiraš;
- grupne poruke jednog pošiljatelja ili s jednom riječi, ili samo neke od njih;
- grupne poruke koje su neispravne ili starije nego što dopuštaš.

Filtar je **isključen** dok ga ne uključiš. Postavljaš ga naredbama. Upiši
ih preko USB-a u [serijsku konzolu](/firmware/console/) na ovom webu. Ili
ih pošalji iz aplikacije MeshCore, kao u
[vodiču za repetitore](/repeater-guide/#config).

## Nabavi firmware {#firmware}

Flashaj **DutchMeshCore Repeater** pomoću flashera u
[DutchMeshCore Toolboxu](https://toolbox.dutchmeshcore.nl/). Firmware za observer
iz vodiča [MQTT na tvojem observeru](/guides/mqtt/) ima isti filtar.

## Prvo isprobaj {#dryrun}

U probnom načinu rada (dry-run) filtar broji svaki paket koji bi odbacio, ali
ga i dalje prosljeđuje. Tako podesi vrijednost prije nego što filtar išta odbaci:

```text
filter on
filter dryrun on
```

Dok je dry-run uključen, statusni redak naredbe `filter` završava s `(dry-run)`.
Brojači pokazuju što bi filtar odbacio. Pusti ga da radi jedan dan, a zatim ih
pogledaj (vidi [Što je odbacio](#stats)). Kad ti brojke izgledaju dobro, uključi
stvarno odbacivanje:

```text
filter dryrun off
```

## Preporučene postavke {#configs}

### Običan repetitor {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Prolazi do 20 grupnih poruka u minuti i do 5 izravnih poruka u minuti,
a neispravne grupne poruke filtar odbacuje. Obične postavke samog firmwarea
dopuštaju 20 izravnih poruka u minuti. Ova stranica uzima 5, vrijednost koju
firmware savjetuje od poplave izravnih poruka u srpnju 2026.

### Opterećen repetitor {#busy}

Za repetitor na visokoj lokaciji koji čuje cijelu regiju ili za onaj koji je
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

Ove postavke prepolovljuju grupne poruke i adverte, a advert svakog čvora propuštaju
jednom dnevno. Odbacuju poruke koje su već prošle 16 repetitora. Nakon
ponovnog pokretanja svakom čvoru prolazi jedan advert. Dokumentacija firmwarea ovdje
postavlja i `filter hash 2`. Ova stranica to izostavlja (razlog pročitaj u odjeljku
[Sve postavke](#settings)).

### Blokiraj bučan kanal {#channel}

```text
filter channel add #bot
```

Tvoj repetitor i dalje čuje kanal. Više ga ne prosljeđuje drugim
repetitorima ni companion uređajima (čvorovima s kojih ljudi šalju poruke). Možeš blokirati do 16 kanala.

### Uspori jednog pošiljatelja {#sender}

Za bota koji prečesto objavljuje na kanalu koji želiš zadržati:

```text
filter watch add #test
filter sender add Bob 60
```

Bobove poruke na kanalu Public i na `#test` sada prolaze jednom u minuti, a
filtar odbacuje ostale. Filtar uspoređuje ime u poruci, pa pošiljatelj koji se
preimenuje prolazi kroz njega.

### Blokiraj jedan repetitor na putu {#path}

Kad smeće stiže preko jednog repetitora, blokiraj njegov prefiks: prvi
dio njegova ID-ja, u heksadecimalnom zapisu (hex). Za to ti treba razvojna inačica 1.18.
Inačica 1.17.1 nema filtar putanje.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` prikazuje prefikse koje blokiraš, a `filter stats path` koliko
je koji odbacio. `filter path remove a1b2` ponovno ga propušta.
Kratki prefiks poput `a1` blokira i svaki drugi repetitor čiji ID počinje
s `a1`. Koristi najdulji prefiks koji možeš. Možeš blokirati do 8 prefiksa.

## Sve postavke {#settings}

Vrste paketa imaju brojeve. Na repetitoru `filter types` prikazuje iste
brojeve s nazivima iz firmwarea, kao što su `TXT_MSG` i `GRP_TXT`:

| Broj | Vrsta | Broj | Vrsta |
| --- | --- | --- | --- |
| `00` | zahtjev | `06` | grupni podaci |
| `01` | odgovor | `07` | anonimni zahtjev |
| `02` | izravna poruka | `08` | putanja |
| `03` | potvrda | `09` | praćenje |
| `04` | advert | `10` | višedijelni paket |
| `05` | grupna poruka | `11` | kontrola |

| Naredba | Što radi | Početna vrijednost |
| --- | --- | --- |
| `filter on` / `filter off` | Uključuje ili isključuje filtar. | isključeno |
| `filter dryrun on` / `off` | Broji odbacivanja, ali i dalje sve prosljeđuje. | isključeno |
| `filter hops <type> <max>` | Odbacuje pakete te vrste koji su već prošli ovoliko repetitora, od 0 do 64. | 32 za grupne poruke, 8 za ostale |
| `filter rate <type> <limit> <secs> [soft]` | Propušta najviše `limit` paketa jedne vrste u `secs` sekundi. Uz `soft` prosljeđivanje postupno slabi od `soft` do `limit`. `0` isključuje ograničenje. | 20 u 60 s za izravne i grupne poruke, 10 za adverte, 5 za ostale |
| `filter advert <hours>` | Propušta advert svakog čvora jednom u toliko sati, do 720. | 0 (isključeno) |
| `filter channel add <#name>` | Prekida prosljeđivanje kanala. | nema |
| `filter path add <hex>` | Odbacuje sve što je došlo preko repetitora s ovim prefiksom, od 2 do 8 hex znamenki. | nema |
| `filter sender add <name> [secs] [prob]` | Odbacuje grupne poruke pošiljatelja na kanalu Public i na praćenim kanalima. `Bot*` obuhvaća svako ime koje počinje s Bot. | nema |
| `filter text add <word> [secs] [prob]` | Odbacuje grupne poruke koje sadrže riječ, na kanalu Public i na praćenim kanalima. `^word` obuhvaća riječ samo na početku. | nema |
| `filter watch add <#name>` | Pravila za pošiljatelje i tekst čitaju i ovaj kanal, a možeš dodati do 4 kanala. Kanal Public čitaju uvijek. | Public |
| `filter malformed on` / `off` | Odbacuje poruke na kanalu Public koje su prazne, neispravne ili im datum odstupa više od tjedan dana (provjera datuma čeka dok se ne postavi sat). | isključeno |
| `filter age <minutes>` / `off` | Odbacuje grupne poruke starije od ove vrijednosti, na kanalu Public i na praćenim kanalima, od 1 do 10080. | isključeno |
| `filter hash <bytes>` | Odbacuje pakete s ID-jem putanje kraćim od ove vrijednosti, od 1 do 3. | 1 |
| `filter reset` | Vraća sve postavke na zadane vrijednosti. | |

Svaki `add` ima svoj `remove` i `list`, na primjer `filter channel remove #bot`.
U pravilima za pošiljatelje i tekst `secs` propušta jednu poruku u toliko sekundi.
`prob` primjenjuje pravilo samo na taj udio podudaranja, od 1 do 100. Možeš imati do 8
pravila za pošiljatelje i 8 pravila za tekst. Imena i riječi razlikuju velika i mala slova. Ime ima
do 15 znakova, a riječ do 23.

Dvije postavke odbacuju više nego što možda očekuješ:

- `filter hash 2` odbacuje gotovo sav promet. Čvorovi prema zadanim postavkama šalju
  ID-jeve putanje od 1 bajta.
- `filter age` vjeruje satu tvojeg repetitora. Postavi ga naredbom `clock sync` iz
  aplikacije, provjeri ga naredbom `clock` i počni s velikom vrijednošću: `filter age 60`.

Sve postavke ostaju spremljene i nakon ponovnog pokretanja.

## Što je odbacio {#stats}

`filter` prikazuje ukupne brojke po razlogu:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` prikazuje pojedinosti za jednu postavku. Teme su
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` i `age`. `filter stats top` prikazuje prvi bajt ID-jeva čvorova
zbog kojih je odbačeno najviše paketa. Taj bajt dijeli mnogo čvorova.
`filter stats air` prikazuje vrijeme emitiranja koje je tvoj repetitor uštedio jer
te pakete nije proslijedio.

Brojači ponovno kreću od 0 nakon ponovnog pokretanja i nakon naredbe `clear stats`.
