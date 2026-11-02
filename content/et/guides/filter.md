---
title: Pakettfilter
lead: 'Ära lase oma kordajal rämpsu edasi saata: kaugelt tulevaid üleujutusi, lõputult postitavat botti, lärmakat kanalit. Proovi seadistust kõigepealt järele, seejärel lülita see sisse.'
description: 'DMC kordaja püsivara pakettfilter: mida see ära viskab, valmis seadistused tavalisele ja koormatud kordajale, kõik filtri käsud koos vaikeväärtustega ja kuidas näha, mida filter ära viskas.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-11-02'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Kordaja (sõlm, mis saadab sõnumeid edasi) kordab kõike, mida kuuleb.
Koormatud mesh-võrgus on selle hulgas ka rämpsu. Mõni bott postitab iga minut. Mõni sõlm saadab
iga paari minuti tagant uuesti oma kuulutuse, tervituse, mille järgi teised selle üles leiavad.
Kohale jõuab sõnumeid, mis on läbinud pool riiki. Iga kordus võtab eetriaega
kõigilt sinu ümber. Pakettfiltriga viskab sinu kordaja sellise liikluse ära
ega saada seda edasi. Et kõigepealt teada saada, mis sinu mesh-võrku üle ujutab ja mis peale filtri veel aitab,
loe lehte [Tee mesh-võrk vastupidavaks](/guides/resilient/).

{{< callout type="warning" >}}
Pakettfilter kuulub **DMC kordaja püsivara** juurde, see on
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) kordajaversioon. Tavalises
MeshCore'is pakettfiltrit ei ole. Seal on `region denyf *` ja
`set flood.max.unscoped`, need leiad lehelt [CLI-käsud](/guides/cli/). See
juhend põhineb 19. oktoobri 2026 arendusversioonil 1.18.0 `ecfb2d4`. Stabiilses
versioonis 1.17.1 on ainult hüpete, kiiruse, kanali, räsi ja vigaste pakettide filtrid.
Dry-run-režiimi selles samuti ei ole.
{{< /callout >}}

## Mida filter teeb {#what}

Filter vaatab ainult pakette, mida sinu kordaja üleujutusega edasi saadab (ehk saadab
need igale levialas olevale sõlmele). See ei puuduta kunagi seda, mida sinu kordaja ise saadab,
ega pakette, mis liiguvad tuntud teed pidi ühele sõlmele. Otsesõnumid ja
päringud sinu enda kontaktidele ja kontaktidelt pääsevad samuti läbi. Filter saab ära visata:

- paketid, mis on juba läbinud nii palju kordajaid (hüppeid), kui sa lubad, iga
  paketitüübi kohta eraldi;
- ühe tüübi paketid, mida on minutis rohkem, kui sa lubad;
- kuulutuse sõlmelt, mis on viimastel tundidel juba kuulutuse saatnud;
- sõnumid kanalil, mille sa blokeerid;
- kõik, mis on tulnud läbi ühe sinu blokeeritud kordaja;
- grupisõnumid ühelt saatjalt või ühe kindla sõnaga, kas kõik või ainult osa neist;
- grupisõnumid, mis on katki või vanemad, kui sa lubad.

Filter on **väljas**, kuni sa selle sisse lülitad. Seadistad seda käskudega. Sisesta
need USB kaudu selle saidi [jadakonsoolis](/firmware/console/). Või
saada need MeshCore'i rakendusest, nagu kirjeldab
[kordaja juhend](/repeater-guide/#config).

## Hangi püsivara {#firmware}

Laadi **DutchMeshCore Repeater** seadmesse välkijaga, mille leiad
[DutchMeshCore Toolboxist](https://toolbox.dutchmeshcore.nl/). Lehel [MQTT sinu vaatlejal](/guides/mqtt/)
kirjeldatud vaatleja püsivaras on sama filter.

## Proovi kõigepealt {#dryrun}

Dry-run-režiimis loeb filter kokku iga paketi, mille ta ära viskaks, kuid saadab selle
siiski edasi. Nii saad seadistuse paika panna, enne kui filter midagi ära viskab:

```text
filter on
filter dryrun on
```

Kui dry-run on sees, lõpeb käsu `filter` olekurida märkega `(dry-run)`. Loendurid
näitavad, mida filter oleks ära visanud. Jäta see ööpäevaks tööle ja vaata siis
loendurid üle (vaata [Mida filter ära viskas](#stats)). Kui numbrid tunduvad õiged, rakenda
filter päriselt:

```text
filter dryrun off
```

## Soovitatud seadistused {#configs}

### Tavaline kordaja {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Grupisõnumeid läheb läbi kuni 20 minutis, otsesõnumeid kuni 5 minutis
ja katkised grupisõnumid visatakse ära. Püsivara enda tavaseadistus lubab
20 otsesõnumit minutis. See leht kasutab väärtust 5, mida püsivara soovitab
alates otsesõnumite üleujutusest 2026. aasta juulis.

### Koormatud kordaja {#busy}

Kordajale, mis asub kõrges kohas ja kuuleb tervet piirkonda, või kordajale, mis on
üle ujutatud:

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

See seadistus vähendab grupisõnumeid ja kuulutusi poole võrra ning laseb iga sõlme
kuulutuse läbi kord ööpäevas. Sõnumid, mis on juba läbinud 16 kordajat, viskab see ära. Pärast
taaskäivitust pääseb iga sõlme üks kuulutus läbi. Püsivara enda dokumentatsioon lisab siia ka
`filter hash 2`. See leht jätab selle välja (põhjuse leiad jaotisest
[Kõik seadistused](#settings)).

### Blokeeri lärmakas kanal {#channel}

```text
filter channel add #bot
```

Sinu kordaja kuuleb kanalit endiselt. Teistele kordajatele ja kaasseadmetele (sõlmedele,
millelt inimesed sõnumeid saadavad) ta seda enam edasi ei saada. Kuni 16 kanalit.

### Aeglusta ühte saatjat {#sender}

Bott, kes postitab liiga tihti kanalil, mida tahad alles hoida:

```text
filter watch add #test
filter sender add Bob 60
```

Bobi sõnumid Public-kanalil ja kanalil `#test` lähevad nüüd läbi kord minutis, ülejäänud
visatakse ära. Filter võrdleb sõnumis olevat nime, nii et saatja pääseb
sellest nime vahetades mööda.

### Blokeeri üks kordaja ülesvoolus {#path}

Kui rämps tuleb läbi ühe kordaja, blokeeri selle prefiks: ID esimene
osa kuueteistkümnendsüsteemis (hex). Selleks on vaja arendusversiooni 1.18, versioonis 1.17.1
teefiltrit ei ole.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` näitab sinu blokeeritud prefikseid, `filter stats path` seda, kui
palju iga prefiks ära viskas. `filter path remove a1b2` laseb selle jälle läbi.
Lühike prefiks nagu `a1` blokeerib ka iga teise kordaja, mille ID algab
väärtusega `a1`. Kasuta võimalikult pikka prefiksit. Kuni 8 prefiksit.

## Kõik seadistused {#settings}

Paketitüüpe tähistavad numbrid. Kordajal näitab `filter types` samu
numbreid koos püsivara nimedega, näiteks `TXT_MSG` ja `GRP_TXT`:

| Number | Tüüp | Number | Tüüp |
| --- | --- | --- | --- |
| `00` | päring | `06` | grupiandmed |
| `01` | vastus | `07` | anonüümne päring |
| `02` | otsesõnum | `08` | tee |
| `03` | kinnitus | `09` | jälitus |
| `04` | kuulutus | `10` | mitmeosaline |
| `05` | grupisõnum | `11` | juhtimine |

| Käsk | Mida see teeb | Algväärtus |
| --- | --- | --- |
| `filter on` / `filter off` | Lülitab filtri sisse või välja. | väljas |
| `filter dryrun on` / `off` | Loeb äravisatavad paketid kokku, kuid saadab kõik siiski edasi. | väljas |
| `filter hops <type> <max>` | Viskab ära selle tüübi paketid, mis on juba läbinud nii palju kordajaid, 0 kuni 64. | grupisõnumitel 32, ülejäänutel 8 |
| `filter rate <type> <limit> <secs> [soft]` | Laseb tüübist läbi kõige rohkem `limit` paketti `secs` sekundi kohta. Valikuga `soft` väheneb läbilaskmine sujuvalt väärtuselt `soft` väärtuseni `limit`. `0` lülitab piirangu välja. | otse- ja grupisõnumitel 20 paketti 60 s kohta, kuulutustel 10, ülejäänutel 5 |
| `filter advert <hours>` | Laseb iga sõlme kuulutuse läbi kord nii mitme tunni jooksul, kuni 720. | 0 (väljas) |
| `filter channel add <#name>` | Lõpetab kanali edasisaatmise. | puudub |
| `filter path add <hex>` | Viskab ära kõik, mis on tulnud läbi selle prefiksiga kordaja, 2 kuni 8 hex-numbrit. | puudub |
| `filter sender add <name> [secs] [prob]` | Viskab ära saatja grupisõnumid Public-kanalil ja jälgitavatel kanalitel. `Bot*` sobib iga nimega, mis algab sõnaga Bot. | puudub |
| `filter text add <word> [secs] [prob]` | Viskab ära grupisõnumid, milles on see sõna, Public-kanalil ja jälgitavatel kanalitel. `^word` sobib ainult sõnumi alguses. | puudub |
| `filter watch add <#name>` | Laseb saatja- ja tekstireeglitel lugeda ka seda kanalit, kuni 4. Public-kanalit loetakse alati. | Public |
| `filter malformed on` / `off` | Viskab ära Public-sõnumid, mis on tühjad, katki või mille kuupäev erineb üle nädala (kuupäeva kontroll ootab, kuni kell on seatud). | väljas |
| `filter age <minutes>` / `off` | Viskab ära sellest vanemad grupisõnumid Public-kanalil ja jälgitavatel kanalitel, 1 kuni 10080. | väljas |
| `filter hash <bytes>` | Viskab ära paketid, mille tee-ID on sellest lühem, 1 kuni 3. | 1 |
| `filter reset` | Taastab kõigi seadistuste vaikeväärtused. | |

Igal käsul `add` on ka `remove` ja `list`, näiteks `filter channel remove #bot`.
Saatja- ja tekstireeglites laseb `secs` läbi ühe sõnumi nii mitme sekundi kohta.
`prob` rakendab reeglit ainult sellele osale vastetest, 1 kuni 100. Kuni 8
saatjareeglit ja 8 tekstireeglit. Nimedes ja sõnades eristatakse suur- ja väiketähti. Nimi on kuni
15 märki, sõna kuni 23 märki.

Need seadistused viskavad ära rohkem, kui võid arvata:

- `filter hash 2` viskab ära peaaegu kogu liikluse. Sõlmed saadavad vaikimisi 1-baidiseid
  tee-ID-sid.
- `filter age` usaldab sinu kordaja kella. Sea kell rakenduses käsuga `clock sync`,
  kontrolli seda käsuga `clock` ja alusta suure varuga: `filter age 60`.

Kõik seadistused säilivad pärast taaskäivitust.

## Mida filter ära viskas {#stats}

`filter` näitab kogusummasid põhjuste kaupa:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` näitab ühe seadistuse üksikasju. Teemad on
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` ja `age`. `filter stats top` näitab nende sõlme-ID-de esimest baiti, mille taga on
kõige rohkem äraviskamisi. Sama baiti jagavad paljud sõlmed.
`filter stats air` näitab eetriaega, mille sinu kordaja säästis, kui ei saatnud neid
pakette edasi.

Loendurid alustavad uuesti 0-st pärast taaskäivitust ja pärast käsku `clear stats`.
