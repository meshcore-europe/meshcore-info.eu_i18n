---
title: Csomagszűrő
lead: 'Ne engedd, hogy az átjátszód továbbadja a szemetet: a messziről jövő floodot, a soha le nem álló botot, a zajos csatornát. Előbb próbálj ki egy beállítást, aztán kapcsold be.'
description: 'A DMC átjátszó-firmware csomagszűrője: mit dob el, kész beállítások egy átlagos és egy forgalmas átjátszóhoz, minden szűrőparancs az alapértékével, és hogyan nézheted meg, mit dobott el.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-10-31'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Az átjátszó (egy csomópont, amely továbbadja az üzeneteket) mindent megismétel, amit hall.
Egy forgalmas mesh-en ez szemetet is jelent. Egy bot percenként posztol. Egy csomópont
pár percenként újra elküldi az advertjét, azt a köszönést, amelyből a többiek megtalálják.
Olyan üzenetek érkeznek, amelyek fél országon át utaztak. Minden ismétlés adásidőt vesz
el mindenkitől körülötted. A csomagszűrővel az átjátszód eldobja ezt a forgalmat, és nem
adja tovább. Ha előbb azt akarod kideríteni, mi árasztja el a mesh-edet, és mi segít még
a szűrőn kívül, olvasd el a
[Tedd ellenállóbbá a mesh-t](/guides/resilient/) oldalt.

{{< callout type="warning" >}}
A csomagszűrő a **DMC átjátszó-firmware** része, ez a
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) átjátszó-változata. A gyári
MeshCore-ban nincs csomagszűrő. Abban a `region denyf *` és a
`set flood.max.unscoped` parancs van, lásd a [CLI-parancsok](/guides/cli/) oldalt. Ez az
útmutató a 2026. október 19-i 1.18.0 dev buildet (`ecfb2d4`) követi. A stabil
1.17.1 buildben csak az ugrás-, sebesség-, csatorna-, hash- és hibáscsomag-szűrő van.
Dry-run sincs benne.
{{< /callout >}}

## Mit csinál a szűrő {#what}

A szűrő csak azokat a csomagokat nézi, amelyeket az átjátszód flooddal ad tovább (vagyis
minden hatótávon belüli csomópontnak elküldi). Soha nem nyúl ahhoz, amit az átjátszód maga
küld. Azokhoz a csomagokhoz sem, amelyek ismert útvonalon mennek egy csomóponthoz. A saját
kapcsolataidtól jövő és nekik szóló közvetlen üzenetek és kérések is átmennek. Ezeket dobhatja el:

- csomagokat, amelyek már annyi átjátszón (ugráson) mentek át, amennyit engedsz,
  csomagtípusonként;
- egy típusból több csomagot, mint amennyit percenként engedsz;
- egy csomópont advertjét, ha az az elmúlt órákban már küldött advertet;
- üzeneteket egy általad tiltott csatornán;
- mindent, ami egy általad tiltott átjátszón keresztül jött;
- egy feladó csoportüzeneteit vagy egy adott szót tartalmazó csoportüzeneteket, vagy csak egy részüket;
- hibás vagy a megengedettnél régebbi csoportüzeneteket.

A szűrő **ki van kapcsolva**, amíg be nem kapcsolod. Parancsokkal állítod be. Ezeket USB-n
gépelheted be az oldal [soros konzoljában](/firmware/console/). Vagy elküldheted őket a
MeshCore appból, ahogy az [átjátszó-útmutatóban](/repeater-guide/#config) látod.

## A firmware beszerzése {#firmware}

Flasheld a **DutchMeshCore Repeater** firmware-t a
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/) flasherével. Az
[MQTT az observereden](/guides/mqtt/) oldal observer-firmware-ében ugyanez a szűrő van.

## Előbb próbáld ki {#dryrun}

Dry-run módban a szűrő megszámol minden csomagot, amelyet eldobna, de továbbra is
továbbadja őket. Így belőheted a beállítást, mielőtt a szűrő bármit eldobna:

```text
filter on
filter dryrun on
```

Amíg a dry-run be van kapcsolva, a `filter` állapotsora `(dry-run)` végződésű. A
számlálók azt mutatják, mit dobott volna el. Hagyd futni egy napig, aztán nézd meg
őket (lásd [Mit dobott el](#stats)). Ha a számok rendben vannak, élesítsd a szűrőt:

```text
filter dryrun off
```

## Ajánlott beállítások {#configs}

### Átlagos átjátszó {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

A csoportüzenetekből percenként legfeljebb 20, a közvetlen üzenetekből legfeljebb 5
megy át, a hibás csoportüzeneteket pedig a szűrő eldobja. A firmware saját átlagos beállítása
percenként 20 közvetlen üzenetet enged. Ez az oldal az 5-öt használja, amelyet a firmware
a 2026 júliusi közvetlenüzenet-áradat óta javasol.

### Forgalmas átjátszó {#busy}

Magaslaton álló átjátszóhoz, amely egy egész régiót hall, vagy amelyet elárasztanak:

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

Ez megfelezi a csoportüzeneteket és az advertöket, és minden csomópont advertjét naponta
egyszer engedi át. Eldobja azokat az üzeneteket, amelyek már 16 átjátszón mentek át.
Újraindítás után minden csomópontnak egy advertje átjut. A firmware saját dokumentációja itt
a `filter hash 2` parancsot is beállítja. Ez az oldal kihagyja (az okát lásd a
[Minden beállítás](#settings) részben).

### Zajos csatorna tiltása {#channel}

```text
filter channel add #bot
```

Az átjátszód továbbra is hallja a csatornát. Viszont már nem adja tovább más
átjátszóknak és companionöknek (azoknak a csomópontoknak, amelyekről az emberek üzennek).
Legfeljebb 16 csatorna.

### Egy feladó lassítása {#sender}

Egy bot túl gyakran posztol egy csatornán, amelyet meg akarsz tartani:

```text
filter watch add #test
filter sender add Bob 60
```

Bob üzenetei a Public csatornán és a `#test` csatornán mostantól percenként egyszer
mennek át. A többit a szűrő eldobja. A szűrő az üzenetben szereplő nevet nézi, ezért
az a feladó, aki átnevezi magát, átjut rajta.

### Egy korábbi átjátszó tiltása {#path}

Ha a szemét egy átjátszón keresztül jön, tiltsd le az előtagját: az azonosítója első
részét hexadecimálisan (hex). Ehhez az 1.18 dev build kell. Az 1.17.1-ben nincs
útvonalszűrő.

```text
filter path add a1b2
filter path list
filter stats path
```

A `filter path list` megmutatja a tiltott előtagokat, a `filter stats path` pedig azt,
mennyit dobott el mindegyik. A `filter path remove a1b2` újra átengedi. Egy rövid
előtag, például az `a1`, minden más átjátszót is letilt, amelynek az azonosítója
`a1`-gyel kezdődik. A lehető leghosszabb előtagot használd. Legfeljebb 8 előtag.

## Minden beállítás {#settings}

A csomagtípusokat szám jelöli. Az átjátszón a `filter types` ugyanezeket a számokat
mutatja a firmware neveivel, például `TXT_MSG` és `GRP_TXT`:

| Szám | Típus | Szám | Típus |
| --- | --- | --- | --- |
| `00` | kérés | `06` | csoportadat |
| `01` | válasz | `07` | névtelen kérés |
| `02` | közvetlen üzenet | `08` | útvonal |
| `03` | nyugtázás | `09` | trace |
| `04` | advert | `10` | többrészes |
| `05` | csoportüzenet | `11` | vezérlés |

| Parancs | Mit csinál | Alapérték |
| --- | --- | --- |
| `filter on` / `filter off` | Be- vagy kikapcsolja a szűrőt. | ki |
| `filter dryrun on` / `off` | Számolja az eldobásokat, de mindent továbbad. | ki |
| `filter hops <type> <max>` | Eldobja a típust, ha már ennyi átjátszón átment, 0 és 64 között. | csoportüzeneteknél 32, a többinél 8 |
| `filter rate <type> <limit> <secs> [soft]` | Egy típusból legfeljebb `limit` darabot enged át `secs` másodpercenként. `soft` megadásával az átengedés `soft`-tól `limit`-ig fokozatosan csökken. A `0` kikapcsolja a korlátot. | 60 s alatt 20 közvetlen és csoportüzenet, 10 advert, 5 a többiből |
| `filter advert <hours>` | Minden csomópont advertjét ennyi óránként egyszer engedi át, legfeljebb 720. | 0 (ki) |
| `filter channel add <#name>` | Nem adja tovább a csatornát. | nincs |
| `filter path add <hex>` | Eldob mindent, ami ilyen előtagú átjátszón jött, 2 és 8 közötti hexa számjegy. | nincs |
| `filter sender add <name> [secs] [prob]` | Eldobja egy feladó csoportüzeneteit a Public és a figyelt csatornákon. A `Bot*` minden Bot kezdetű névre illeszkedik. | nincs |
| `filter text add <word> [secs] [prob]` | Eldobja az adott szót tartalmazó csoportüzeneteket a Public és a figyelt csatornákon. A `^word` csak az elejére illeszkedik. | nincs |
| `filter watch add <#name>` | A feladó- és szövegszabályok ezt a csatornát is olvassák, legfeljebb 4 csatornát. A Publicot mindig olvassák. | Public |
| `filter malformed on` / `off` | Eldobja az üres, hibás vagy egy hétnél többel eltérő dátumú Public üzeneteket (a dátumellenőrzés megvárja, hogy beálljon az óra). | ki |
| `filter age <minutes>` / `off` | Eldobja az ennél régebbi csoportüzeneteket a Public és a figyelt csatornákon, 1 és 10080 között. | ki |
| `filter hash <bytes>` | Eldobja az ennél rövidebb útvonal-azonosítójú csomagokat, 1 és 3 között. | 1 |
| `filter reset` | Minden beállítást visszaállít az alapértékre. | |

Minden `add` parancsnak van `remove` és `list` párja, például `filter channel remove #bot`.
A feladó- és szövegszabályokban a `secs` ennyi másodpercenként egy üzenetet átenged.
A `prob` a szabályt csak a találatok ekkora részére alkalmazza, 1 és 100 között.
Legfeljebb 8 feladó- és 8 szövegszabály lehet. A nevek és szavak kis- és nagybetűérzékenyek.
Egy név legfeljebb 15, egy szó legfeljebb 23 karakter.

Két beállítás többet dob el, mint várnád:

- A `filter hash 2` szinte az összes forgalmat eldobja. A csomópontok alapból 1 bájtos
  útvonal-azonosítót küldenek.
- A `filter age` az átjátszód órájára hagyatkozik. Állítsd be az appból a `clock sync`
  paranccsal, ellenőrizd a `clock` paranccsal, és kezdj bőkezű értékkel: `filter age 60`.

Újraindítás után minden beállítás megmarad.

## Mit dobott el {#stats}

A `filter` okonként mutatja az összesítést:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

A `filter stats <topic>` egy beállítás részleteit mutatja. A témák:
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` és `age`. A `filter stats top` azoknak a csomópont-azonosítóknak az első bájtját
mutatja, amelyek a legtöbb eldobás mögött állnak. Ezen a bájton sok csomópont osztozik.
A `filter stats air` megmutatja, mennyi adásidőt spórolt az átjátszód azzal, hogy nem
adta tovább ezeket a csomagokat.

Újraindítás és a `clear stats` után a számlálók újra 0-ról indulnak.
