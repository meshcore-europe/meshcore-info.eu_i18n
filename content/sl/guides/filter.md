---
title: Filter paketov
lead: 'Prepreči, da bi tvoj repetitor posredoval smeti: poplave od daleč, bota, ki se nikoli ne ustavi, in hrupen kanal. Nastavitev najprej preizkusi, nato jo vklopi.'
description: 'Filter paketov v vdelani programski opremi DMC za repetitorje: kaj zavrže, pripravljene nastavitve za običajen in zelo obremenjen repetitor, vsi ukazi filtra s privzetimi vrednostmi in pregled zavrženih paketov.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-11-02'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Repetitor (vozlišče, ki posreduje sporočila) ponovi vse, kar sliši.
V obremenjenem omrežju mesh so med tem tudi smeti. Bot objavlja vsako minuto. Neko vozlišče vsakih nekaj minut znova pošlje svoj oglas, pozdrav, po katerem ga druga vozlišča najdejo. Prihajajo sporočila, ki so prepotovala pol države. Vsaka ponovitev vzame čas oddajanja vsem okoli tebe. S filtrom paketov tvoj repetitor tak promet zavrže in ga ne posreduje. Kako najprej ugotoviš, kaj preplavlja tvoje omrežje, in kaj poleg filtra še pomaga, izveš v vodniku [Naredi omrežje odporno](/guides/resilient/).

{{< callout type="warning" >}}
Filter paketov je del **vdelane programske opreme DMC za repetitorje**, to je različice [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) za repetitorje. Standardni MeshCore nima filtra paketov. Ima `region denyf *` in `set flood.max.unscoped`, opisana na strani [Ukazi CLI](/guides/cli/). Ta vodnik se nanaša na razvojno različico 1.18.0 `ecfb2d4` z dne 19. oktobra 2026. Stabilna različica 1.17.1 ima samo filtre skokov, hitrosti, kanalov, zgoščene vrednosti in pokvarjenih sporočil. Prav tako nima načina dry-run.
{{< /callout >}}

## Kaj filter počne {#what}

Filter pregleduje samo pakete, ki jih tvoj repetitor posreduje s poplavljanjem (pošilja jih vsem vozliščem v dosegu). Nikoli se ne dotakne tega, kar tvoj repetitor pošlje sam, ali paketov, ki po znani poti potujejo do enega vozlišča. Prepusti tudi neposredna sporočila in zahteve, ki so namenjeni tvojim stikom ali prihajajo od njih. Zavrže lahko:

- pakete, ki so šli že skozi toliko repetitorjev (skokov), kot jih dovoliš za posamezno vrsto paketa;
- več paketov ene vrste na minuto, kot jih dovoliš;
- oglas vozlišča, ki je oglas poslalo že v zadnjih urah;
- sporočila na kanalu, ki ga blokiraš;
- vse, kar je prišlo prek enega repetitorja, ki ga blokiraš;
- skupinska sporočila enega pošiljatelja ali z določeno besedo, lahko pa tudi le nekatera med njimi;
- skupinska sporočila, ki so pokvarjena ali starejša, kot dovoliš.

Filter je **izklopljen**, dokler ga ne vklopiš. Nastaviš ga z ukazi. Vnesi jih prek USB v [serijski konzoli](/firmware/console/) na tem spletnem mestu. Lahko pa jih pošlješ iz aplikacije MeshCore, kot opisuje [vodnik za repetitorje](/repeater-guide/#config).

## Pridobi vdelano programsko opremo {#firmware}

**DutchMeshCore Repeater** naloži s programatorjem v orodju [DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Enak filter ima tudi vdelana programska oprema za opazovalce iz vodnika [MQTT na tvojem opazovalcu](/guides/mqtt/).

## Najprej preizkusi {#dryrun}

V načinu dry-run filter prešteje vsak paket, ki bi ga zavrgel, a ga vseeno posreduje. Tako določiš vrednost nastavitve, preden filter karkoli zavrže:

```text
filter on
filter dryrun on
```

Dokler je dry-run vklopljen, se vrstica stanja ukaza `filter` konča z `(dry-run)`. Števci kažejo, kaj bi filter zavrgel. Filter pusti teči en dan, nato si števce oglej (glej [Kaj je filter zavrgel](#stats)). Ko so številke videti prave, vklopi pravo zavračanje:

```text
filter dryrun off
```

## Priporočene nastavitve {#configs}

### Običajen repetitor {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Filter prepusti do 20 skupinskih sporočil na minuto in do 5 neposrednih sporočil na minuto, pokvarjena skupinska sporočila pa zavrže. Običajna nastavitev same vdelane programske opreme dovoljuje 20 neposrednih sporočil na minuto. Ta stran uporablja vrednost 5, ki jo vdelana programska oprema priporoča od poplave neposrednih sporočil julija 2026.

### Zelo obremenjen repetitor {#busy}

Za repetitor na visoki lokaciji, ki sliši celo regijo, ali za repetitor, ki ga preplavlja promet:

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

Tako prepoloviš skupinska sporočila in oglase, oglas vsakega vozlišča pa prepustiš enkrat na dan. Sporočila, ki so šla že skozi 16 repetitorjev, repetitor zavrže. Po ponovnem zagonu filter od vsakega vozlišča prepusti en oglas. Dokumentacija vdelane programske opreme tukaj nastavi še `filter hash 2`, ta stran pa to nastavitev izpušča (razlog najdeš v razdelku [Vse nastavitve](#settings)).

### Blokiraj hrupen kanal {#channel}

```text
filter channel add #bot
```

Tvoj repetitor kanal še vedno sliši. Ne posreduje pa ga več drugim repetitorjem in spremljevalnim vozliščem (vozliščem, s katerih ljudje pošiljajo sporočila). Blokiraš lahko do 16 kanalov.

### Upočasni enega pošiljatelja {#sender}

Za bota, ki prepogosto objavlja na kanalu, ki ga želiš obdržati:

```text
filter watch add #test
filter sender add Bob 60
```

Bobova sporočila na kanalih Public in `#test` filter zdaj prepusti enkrat na minuto, ostala zavrže. Filter primerja ime v sporočilu, zato ga pošiljatelj z novim imenom obide.

### Blokiraj en repetitor na poti {#path}

Če smeti prihajajo prek enega repetitorja, blokiraj njegovo predpono: prvi del njegovega ID-ja v šestnajstiškem zapisu (hex). Za to potrebuješ razvojno različico 1.18, saj 1.17.1 nima filtra poti.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` pokaže predpone, ki jih blokiraš, `filter stats path` pa, koliko je zavrgla vsaka od njih. Z ukazom `filter path remove a1b2` predpono spet prepustiš. Kratka predpona, kot je `a1`, blokira tudi vsak drug repetitor, katerega ID se začne z `a1`. Uporabi čim daljšo predpono. Blokiraš lahko do 8 predpon.

## Vse nastavitve {#settings}

Vrste paketov imajo številke. Na repetitorju ukaz `filter types` pokaže iste številke z imeni iz vdelane programske opreme, kot sta `TXT_MSG` in `GRP_TXT`:

| Številka | Vrsta | Številka | Vrsta |
| --- | --- | --- | --- |
| `00` | zahteva | `06` | skupinski podatki |
| `01` | odgovor | `07` | anonimna zahteva |
| `02` | neposredno sporočilo | `08` | pot |
| `03` | potrditev | `09` | sled |
| `04` | oglas | `10` | večdelni paket |
| `05` | skupinsko sporočilo | `11` | nadzor |

| Ukaz | Kaj naredi | Začetna vrednost |
| --- | --- | --- |
| `filter on` / `filter off` | Vklopi ali izklopi filter. | izklopljeno |
| `filter dryrun on` / `off` | Šteje zavržene pakete, a vseeno vse posreduje. | izklopljeno |
| `filter hops <type> <max>` | Zavrže pakete te vrste, ki so šli že skozi toliko repetitorjev, od 0 do 64. | 32 za skupinska sporočila, 8 za ostale |
| `filter rate <type> <limit> <secs> [soft]` | Prepusti največ `limit` paketov ene vrste na `secs` sekund. S `soft` se prepuščanje postopno zmanjšuje od `soft` do `limit`. `0` izklopi omejitev. | 20 na 60 s za neposredna in skupinska sporočila, 10 za oglase, 5 za ostale |
| `filter advert <hours>` | Prepusti oglas vsakega vozlišča enkrat na toliko ur, največ 720. | 0 (izklopljeno) |
| `filter channel add <#name>` | Ustavi posredovanje kanala. | brez |
| `filter path add <hex>` | Zavrže vse, kar je prišlo prek repetitorja s to predpono, od 2 do 8 šestnajstiških števk. | brez |
| `filter sender add <name> [secs] [prob]` | Zavrže skupinska sporočila pošiljatelja na kanalu Public in spremljanih kanalih. `Bot*` ustreza vsakemu imenu, ki se začne z Bot. | brez |
| `filter text add <word> [secs] [prob]` | Zavrže skupinska sporočila z določeno besedo na kanalu Public in spremljanih kanalih. `^word` se ujema samo na začetku. | brez |
| `filter watch add <#name>` | Pravilom za pošiljatelje in besedilo dovoli branje tudi tega kanala, največ 4. Kanal Public berejo vedno. | Public |
| `filter malformed on` / `off` | Zavrže sporočila na kanalu Public, ki so prazna, pokvarjena ali imajo datum, ki odstopa za več kot en teden (preverjanje datuma počaka, da je ura nastavljena). | izklopljeno |
| `filter age <minutes>` / `off` | Zavrže skupinska sporočila, starejša od te vrednosti, na kanalu Public in spremljanih kanalih, od 1 do 10080. | izklopljeno |
| `filter hash <bytes>` | Zavrže pakete s krajšim ID-jem poti od te vrednosti, od 1 do 3. | 1 |
| `filter reset` | Vse nastavitve vrne na privzete vrednosti. | |

Vsak `add` ima tudi `remove` in `list`, na primer `filter channel remove #bot`.
V pravilih za pošiljatelje in besedilo `secs` prepusti eno sporočilo na toliko sekund. `prob` uporabi pravilo samo za ta delež ujemanj, od 1 do 100. Nastaviš lahko do 8 pravil za pošiljatelje in 8 pravil za besedilo. Pri imenih in besedah se velike in male črke razlikujejo. Ime ima lahko do 15 znakov, beseda do 23.

Dve nastavitvi zavržeta več, kot morda pričakuješ:

- `filter hash 2` zavrže skoraj ves promet. Vozlišča privzeto pošiljajo 1-bajtne ID-je poti.
- `filter age` se zanaša na uro tvojega repetitorja. Nastavi jo z ukazom `clock sync` iz aplikacije, preveri jo z ukazom `clock` in začni z ohlapno vrednostjo: `filter age 60`.

Vse nastavitve ostanejo shranjene tudi po ponovnem zagonu.

## Kaj je filter zavrgel {#stats}

`filter` pokaže seštevke po razlogih:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` pokaže podrobnosti za eno nastavitev. Teme so `hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`, `text` in `age`. `filter stats top` pokaže prvi bajt ID-jev vozlišč, zaradi katerih je zavrženih največ paketov. Ta bajt si deli veliko vozlišč.
`filter stats air` pokaže čas oddajanja, ki ga je tvoj repetitor prihranil, ker teh paketov ni posredoval.

Števci začnejo znova pri 0 po ponovnem zagonu in po ukazu `clear stats`.
