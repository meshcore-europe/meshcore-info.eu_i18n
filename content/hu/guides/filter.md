---
title: Csomagszűrő
lead: 'Ne engedd, hogy az átjátszód szemetet továbbítson: távoli floodokat, egy soha le nem álló botot, egy zajos csatornát. Először próbáld ki a beállítást, aztán kapcsold be.'
description: 'A DMC átjátszó firmware csomagszűrője: mit dob el, kész beállítások egy átlagos és egy forgalmas átjátszóhoz, minden szűrőparancs az alapértékével, és hogyan nézed meg, mit dobott el.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '2bf23d24'
  seeded: '2026-10-26'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['0625daa2', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', 'ffc3f3a0', '3fa1bb28', '09511608']
---

Az átjátszó (egy csomópont, amely továbbadja az üzeneteket) mindent megismétel, amit hall.
Egy forgalmas meshben ebbe a szemét is beletartozik. Egy bot percenként posztol. Egy
csomópont pár percenként újra elküldi az advertjét, a köszönést, amelyből a többiek
megtalálják. Olyan üzenetek érkeznek, amelyek a fél országon át utaztak. Minden
ismétlés légidőt vesz el mindenkitől körülötted. A csomagszűrővel az átjátszód
eldobja ezt a forgalmat, ahelyett hogy továbbadná.

{{< callout type="warning" >}}
A csomagszűrő a **DMC átjátszó firmware** része, ez a
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) átjátszó buildje. A
gyári MeshCore-ban nincs csomagszűrő; ott a `region denyf *` és a
`set flood.max.unscoped` létezik, lásd a [CLI-parancsok](/guides/cli/) oldalt. Ez
az útmutató az 1.18.0 dev build `ecfb2d4` változatát követi, 2026. október 19-ről.
A stabil 1.17.1 buildben csak az ugrás-, sebesség-, csatorna-, hash- és
hibás-csomag-szűrő van. Száraz futtatás sincs benne.
{{< /callout >}}

## Mit csinál a szűrő {#what}

A szűrő csak azokat a csomagokat nézi, amelyeket az átjátszód flooddal továbbít
(vagyis minden hatótávon belüli csomópontnak elküld). Soha nem nyúl ahhoz, amit az
átjátszód maga küld, sem az ismert útvonalon egy csomóponthoz tartó csomagokhoz. A
saját kapcsolataidtól és kapcsolataidhoz menő közvetlen üzenetek és kérések is
átmennek. Ezeket tudja eldobni:

- csomagokat, amelyek már annyi átjátszón (ugráson) átmentek, amennyit megengedsz,
  csomagtípusonként;
- egy típusból több csomagot percenként, mint amennyit megengedsz;
- advertet olyan csomóponttól, amely az utolsó órákban már advertet küldött;
- üzeneteket egy csatornán, amelyet tiltasz;
- mindent, ami egy tiltott átjátszón keresztül jött;
- csoportüzeneteket egy feladótól vagy egy adott szóval, vagy csak egy részüket;
- hibás csoportüzeneteket, vagy a megengedettnél régebbieket.

A szűrő **kikapcsolva** marad, amíg be nem kapcsolod. Parancsokkal állítod be.
Begépelheted őket USB-n a [soros konzolban](/firmware/console/) ezen az oldalon. Vagy
elküldheted a MeshCore appból, ahogy az
[átjátszó-útmutató](/repeater-guide/#config) mutatja.

## Szerezd be a firmware-t {#firmware}

Flasheld a **DutchMeshCore Repeater** firmware-t a
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/) flasherével. Az
[MQTT az observeren](/guides/mqtt/) oldalon leírt observer firmware ugyanezt a szűrőt
tartalmazza.

## Először próbáld ki {#dryrun}

Száraz futtatásban a szűrő megszámol minden csomagot, amelyet eldobna, de mégis
továbbadja. Így méretezd a beállítást, mielőtt bármit eldobna:

```text
filter on
filter dryrun on
```

Amíg a száraz futtatás be van kapcsolva, a `filter` állapotsora `(dry-run)`
szóval végződik. A számok azt mutatják, mit dobott volna el. Hagyd futni egy napot,
aztán nézd meg őket (lásd [Mit dobott el](#stats)). Ha a számok jónak tűnnek,
élesítsd:

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

Percenként legfeljebb 20 csoportüzenet és 5 közvetlen üzenet megy át, a hibás
csoportüzeneteket pedig eldobja. A firmware saját átlagos beállítása percenként
20 közvetlen üzenetet enged. Ez az oldal az általa ajánlott 5-öt veszi át, egy
2026. júliusi közvetlen üzenet flood óta.

### Forgalmas átjátszó {#busy}

Egy magas ponton álló átjátszóhoz, amely egy egész régiót hall, vagy egy
floodolt átjátszóhoz:

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

Ez felére csökkenti a csoportüzeneteket és az adverteket, és minden csomópont
advertjét naponta egyszer engedi át. Eldobja az üzeneteket, amelyek már 16 átjátszón
átmentek. Újraindítás után minden csomópont egy advertet átvisz. A firmware saját
dokumentációja itt a `filter hash 2` beállítást is megadja; ez az oldal kihagyja
(a [Minden beállítás](#settings) fejezet elmondja, miért).

### Zajos csatorna tiltása {#channel}

```text
filter channel add #bot
```

Az átjátszód továbbra is hallja a csatornát. Már nem adja tovább más átjátszóknak és
companionoknak (a csomópontoknak, amelyekről az emberek üzennek). Legfeljebb 16
csatorna.

### Egy feladó lassítása {#sender}

Egy bot, amely túl gyakran posztol egy csatornán, amelyet meg akarsz tartani:

```text
filter watch add #test
filter sender add Bob 60
```

Bob üzenetei a Public csatornán és a `#test` csatornán mostantól percenként egyszer
mennek át; a többit a szűrő eldobja. A szűrő az üzenetben szereplő nevet nézi,
így egy feladó, aki átnevezi magát, átjut rajta.

### Egy feljebb lévő átjátszó tiltása {#path}

Ha a szemét egy átjátszón keresztül jön, tiltsd az előtagját: az azonosítója első
részét, hexadecimális (hex) alakban.

```text
filter path add a1b2
```

Egy rövid előtag, például `a1`, minden más átjátszót is tilt, amelynek azonosítója
`a1`-gyel kezdődik. Használd a leghosszabb előtagot, amit csak tudsz. Legfeljebb 8
előtag.

## Minden beállítás {#settings}

A csomagtípusokat szám jelöli. Az átjátszón a `filter types` ugyanezeket a számokat
mutatja a firmware neveivel, például `TXT_MSG` és `GRP_TXT`:

| Szám | Típus | Szám | Típus |
| --- | --- | --- | --- |
| `00` | kérés | `06` | csoportadat |
| `01` | válasz | `07` | névtelen kérés |
| `02` | közvetlen üzenet | `08` | útvonal |
| `03` | visszaigazolás | `09` | trace |
| `04` | advert | `10` | többrészes |
| `05` | csoportüzenet | `11` | vezérlés |

| Parancs | Mit csinál | Alapérték |
| --- | --- | --- |
| `filter on` / `filter off` | Be- vagy kikapcsolja a szűrőt. | ki |
| `filter dryrun on` / `off` | Számolja az eldobásokat, de mindent továbbad. | ki |
| `filter hops <type> <max>` | Eldob egy típust, amely már ennyi átjátszón átment, 0-tól 64-ig. | 32 csoportüzeneteknél, 8 a többinél |
| `filter rate <type> <limit> <secs> [soft]` | Egy típusból legfeljebb `limit` darabot ad át `secs` másodpercenként. `soft` megadásával az átadás `soft`-tól `limit`-ig fokozatosan csökken. A `0` kikapcsolja a korlátot. | 20 per 60 s közvetlen és csoportüzeneteknél, 10 adverteknél, 5 a többinél |
| `filter advert <hours>` | Minden csomópont advertjét ennyi óránként egyszer adja át, legfeljebb 720. | 0 (ki) |
| `filter channel add <#name>` | Nem adja tovább a csatornát. | nincs |
| `filter path add <hex>` | Eldob mindent, ami ilyen előtagú átjátszón keresztül jött, 2-től 8 hex jegyig. | nincs |
| `filter sender add <name> [secs] [prob]` | Eldobja egy feladó csoportüzeneteit a Public és a figyelt csatornákon. A `Bot*` minden Bot-tal kezdődő névre illeszkedik. | nincs |
| `filter text add <word> [secs] [prob]` | Eldobja az adott szót tartalmazó csoportüzeneteket a Public és a figyelt csatornákon. A `^word` csak a szöveg elején illeszkedik. | nincs |
| `filter watch add <#name>` | A feladó- és szövegszabályok ezt a csatornát is olvassák, legfeljebb 4. A Public csatornát mindig olvassák. | Public |
| `filter malformed on` / `off` | Eldobja az üres, hibás vagy több mint egy héttel eltérő dátumú Public üzeneteket (a dátumellenőrzés vár, amíg az óra be nincs állítva). | ki |
| `filter age <minutes>` / `off` | Eldobja az ennél régebbi csoportüzeneteket a Public és a figyelt csatornákon, 1-től 10080-ig. | ki |
| `filter hash <bytes>` | Eldobja az ennél rövidebb útvonal-azonosítójú csomagokat, 1-től 3-ig. | 1 |
| `filter reset` | Minden beállítást visszaállít az alapértékére. | |

Minden `add` parancsnak van `remove` és `list` párja, például `filter channel remove #bot`.
A feladó- és szövegszabályokban a `secs` ennyi másodpercenként egy üzenetet enged át.
A `prob` a szabályt csak a találatok ekkora hányadára alkalmazza, 1-től 100-ig.
Legfeljebb 8 feladó- és 8 szövegszabály lehet. A nevek és szavak kis- és nagybetű
érzékenyek; egy név legfeljebb 15 karakter, egy szó legfeljebb 23.

Két beállítás többet dob el, mint várnád:

- A `filter hash 2` szinte az összes forgalmat eldobja. A csomópontok
  alapértelmezetten 1 bájtos útvonal-azonosítót küldenek.
- A `filter age` az átjátszód órájára hagyatkozik. Állítsd be az appból a
  `clock sync` paranccsal, ellenőrizd a `clock` paranccsal, és kezdd bőkezűen:
  `filter age 60`.

Minden beállítás megmarad újraindítás után.

## Mit dobott el {#stats}

A `filter` az összesítést mutatja okonként:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

A `filter stats <topic>` egy beállítás részleteit mutatja. A témák: `hops`, `rate`,
`channel`, `hash`, `malformed`, `advert`, `path`, `sender`, `text` és `age`. A
`filter stats top` a legtöbb eldobás mögött álló csomópont-azonosítók első bájtját
mutatja, ez inkább nyom, mint bizonyíték. A `filter stats air` azt a légidőt mutatja,
amelyet az átjátszód megtakarított azzal, hogy nem adta tovább ezeket a csomagokat.

A számlálók újraindítás után és a `clear stats` parancs után újra 0-ról indulnak.
