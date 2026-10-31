---
title: Pakketfilter
lead: 'Hâld dyn repeater derfan om rommel troch te jaan: floods fan fier fuort, in bot dy''t nea ophâldt, in lawaaierich kanaal. Probearje earst in ynstelling, set it filter dan oan.'
description: 'It pakketfilter fan de DMC-repeaterfirmware: wat it weismyt, klearmakke ynstellingen foar in gewoane en in drokke repeater, alle filterkommando''s mei harren standertwearde, en hoe''tsto sjochst wat it weismiten hat.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-10-31'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

In repeater (in node dy't berjochten trochjout) werhellet alles wat er heart.
Op in drok mesh sit dêr ek rommel by. In bot pleatst elke minút wat. Ien node stjoert
syn advert, it hallo wêrmei oaren him fine kinne, om de pear minuten op 'e nij.
Der komme berjochten binnen dy't troch it heale lân reizge hawwe. Elke werhelling nimt
stjoertiid ôf fan elkenien om dy hinne. Mei it pakketfilter smyt dyn repeater
dat ferkear wei, yn stee fan it troch te jaan. Wolsto earst witte wat dyn mesh
oerstreamt, en wat njonken it filter helpt, sjoch dan
[Meitsje it mesh bestindich](/guides/resilient/).

{{< callout type="warning" >}}
It pakketfilter heart by de **DMC-repeaterfirmware**, de repeaterbuild
fan [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Standert
MeshCore hat gjin pakketfilter. It hat wol `region denyf *` en
`set flood.max.unscoped`, op de side [CLI-kommando's](/guides/cli/). Dizze
hantlieding folget de 1.18.0-devbuild `ecfb2d4` fan 19 oktober 2026. De stabile
build 1.17.1 hat allinne de filters foar hops, tempo, kanaal, hash en misfoarme pakketten. Dy
hat ek gjin dry-run.
{{< /callout >}}

## Wat it filter docht {#what}

It filter sjocht allinne nei pakketten dy't dyn repeater trochjout troch flooding (dêrby
stjoert er se nei elke node binnen berik). It komt nea oan wat dyn repeater sels
stjoert, of oan pakketten dy't in bekende rûte nei ien node folgje. Direkte berjochten en
fersiken fan en nei dyn eigen kontakten geane ek troch. It kin weismite:

- pakketten dy't al safolle repeaters (hops) passearre binne as dysto tastiest, per
  pakkettype;
- mear pakketten fan ien type per minút as dysto tastiest;
- in advert fan in node dy't yn 'e lêste oeren al in advert stjoerd hat;
- berjochten op in kanaal datsto blokkearrest;
- alles wat troch ien repeater kaam dy'tsto blokkearrest;
- groepsberjochten fan ien stjoerder of mei ien wurd, of mar in part dêrfan;
- groepsberjochten dy't stikken binne, of âlder as dysto tastiest.

It filter stiet **út** oantsto it oansetst. Do stelst it yn mei kommando's. Typ
se oer USB yn 'e [seriële konsole](/firmware/console/) op dizze side. Of
stjoer se fanút de MeshCore-app, lykas yn 'e
[repeaterhantlieding](/repeater-guide/#config).

## De firmware krije {#firmware}

Flash **DutchMeshCore Repeater** mei de flasher yn 'e
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). De observerfirmware
fan [MQTT op dyn observer](/guides/mqtt/) hat itselde filter.

## Probearje it earst {#dryrun}

Yn dry-run telt it filter elk pakket dat it weismite soe, mar it jout it
dochs troch. Sa bepalsto in ynstelling foardat it wat weismyt:

```text
filter on
filter dryrun on
```

Salang't dry-run oan stiet, einiget de statusrigel fan `filter` op `(dry-run)`. De
tellingen litte sjen wat it weismiten hawwe soe. Lit it in dei rinne, sjoch dan
nei de tellingen (sjoch [Wat it weismiten hat](#stats)). Lykje de getallen goed, set it
filter dan echt oan it wurk:

```text
filter dryrun off
```

## Oanrekommandearre ynstellingen {#configs}

### In gewoane repeater {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Groepsberjochten geane troch oant 20 per minút, direkte berjochten oant 5 per minút,
en stikkene groepsberjochten smyt it filter wei. De eigen gewoane ynstelling fan
de firmware lit 20 direkte berjochten per minút ta. Dizze side nimt de 5 dy't
de firmware oanrikt sûnt in flood fan direkte berjochten yn july 2026.

### In drokke repeater {#busy}

Foar in repeater op in hege lokaasje dy't in hiele regio heart, of ien dy't
oerstreamd wurdt:

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

Hjirmei giet it oantal groepsberjochten en adverts nei de helte, en it advert fan elke node giet ien kear deis troch. It filter smyt berjochten wei dy't al 16 repeaters passearre binne. Nei in
herstart komt fan elke node ien advert troch. De eigen dokumintaasje fan de firmware set hjir ek
`filter hash 2`. Dizze side lit dat wei (sjoch
[Alle ynstellingen](#settings) foar it wêrom).

### In lawaaierich kanaal blokkearje {#channel}

```text
filter channel add #bot
```

Dyn repeater heart it kanaal noch. Hy jout it net mear troch oan oare
repeaters en companions (de nodes dêr't minsken berjochten mei stjoere). Oant 16 kanalen.

### Ien stjoerder ôfremje {#sender}

In bot dy't te faak pleatst op in kanaal datsto hâlde wolst:

```text
filter watch add #test
filter sender add Bob 60
```

De berjochten fan Bob op it Public-kanaal en `#test` geane no ien kear per minút troch. De
rest smyt it filter wei. It filter fergeliket de namme yn it berjocht, dus in stjoerder dy't
syn namme feroaret, komt der lâns.

### Ien repeater streamop blokkearje {#path}

Komt de rommel binnen fia ien repeater, blokkearje dan syn prefix: it earste
part fan syn ID, yn heksadesimaal (hex). Dêr hasto de 1.18-devbuild foar nedich. 1.17.1
hat gjin paadfilter.

```text
filter path add a1b2
filter path list
filter stats path
```

Mei `filter path list` sjochsto de prefixen dy'tsto blokkearrest, mei `filter stats path` hoefolle
elk derfan weismiten hat. Mei `filter path remove a1b2` litsto him wer troch.
In koarte prefix lykas `a1` blokkearret ek elke oare repeater mei in ID dy't begjint
mei `a1`. Brûk de langste prefix dy'tsto kinst. Oant 8 prefixen.

## Alle ynstellingen {#settings}

Pakkettypen hawwe in nûmer. Op 'e repeater lit `filter types` deselde
nûmers sjen mei de nammen fan de firmware, lykas `TXT_MSG` en `GRP_TXT`:

| Nûmer | Type | Nûmer | Type |
| --- | --- | --- | --- |
| `00` | fersyk | `06` | groepsdata |
| `01` | antwurd | `07` | anonym fersyk |
| `02` | direkt berjocht | `08` | paad |
| `03` | befêstiging | `09` | trace |
| `04` | advert | `10` | multipart |
| `05` | groepsberjocht | `11` | kontrôle |

| Kommando | Wat it docht | Begjint by |
| --- | --- | --- |
| `filter on` / `filter off` | Set it filter oan of út. | út |
| `filter dryrun on` / `off` | Tel wat it weismite soe, mar jou alles dochs troch. | út |
| `filter hops <type> <max>` | Smyt in type wei dat al safolle repeaters passearre is, 0 oant 64. | 32 foar groepsberjochten, 8 foar de rest |
| `filter rate <type> <limit> <secs> [soft]` | Jou op syn heechst `limit` fan in type per `secs` troch. Mei `soft` nimt it trochjaan stadichoan ôf fan `soft` nei `limit`. `0` set de limyt út. | 20 per 60 s foar direkte en groepsberjochten, 10 foar adverts, 5 foar de rest |
| `filter advert <hours>` | Jou it advert fan elke node ien kear per safolle oeren troch, oant 720. | 0 (út) |
| `filter channel add <#name>` | Hâld op mei it trochjaan fan in kanaal. | gjin |
| `filter path add <hex>` | Smyt alles wei dat troch in repeater mei dizze prefix kaam, 2 oant 8 hex-sifers. | gjin |
| `filter sender add <name> [secs] [prob]` | Smyt groepsberjochten fan in stjoerder wei, op Public en folge kanalen. `Bot*` past by elke namme dy't begjint mei Bot. | gjin |
| `filter text add <word> [secs] [prob]` | Smyt groepsberjochten mei in bepaald wurd wei, op Public en folge kanalen. `^word` past allinne oan it begjin. | gjin |
| `filter watch add <#name>` | Lit de stjoerder- en tekstregels dit kanaal ek lêze, oant 4. Public lêze se altyd. | Public |
| `filter malformed on` / `off` | Smyt Public-berjochten wei dy't leech of stikken binne, of in datum hawwe dy't mear as in wike ôfwykt (de datumkontrôle wachtet oant de klok ynsteld is). | út |
| `filter age <minutes>` / `off` | Smyt groepsberjochten wei dy't âlder binne as dit, op Public en folge kanalen, 1 oant 10080. | út |
| `filter hash <bytes>` | Smyt pakketten wei mei in koartere paad-ID as dit, 1 oant 3. | 1 |
| `filter reset` | Set alle ynstellingen werom nei harren standertwearde. | |

Elke `add` hat in `remove` en in `list`, lykas `filter channel remove #bot`.
Yn stjoerder- en tekstregels lit `secs` ien berjocht per safolle sekonden troch.
Mei `prob` jildt de regel foar mar dat part fan de treffers, 1 oant 100. Oant 8
stjoerderregels en 8 tekstregels. Nammen en wurden binne gefoelich foar haadletters. In namme hat op syn heechst
15 tekens, in wurd 23.

Twa ynstellingen smite mear wei as dosto miskien ferwachtest:

- `filter hash 2` smyt hast al it ferkear wei. Nodes stjoere standert paad-ID's fan 1 byte.
- `filter age` fertrout op de klok fan dyn repeater. Set him gelyk mei `clock sync` fanút de
  app, kontrolearje him mei `clock`, en begjin rom: `filter age 60`.

Alle ynstellingen bliuwe bewarre nei in herstart.

## Wat it weismiten hat {#stats}

`filter` lit de totalen per reden sjen:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` lit de details fan ien ynstelling sjen. De ûnderwerpen binne
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` en `age`. `filter stats top` lit de earste byte sjen fan de node-ID's
efter de measte weismiten pakketten. In soad nodes hawwe dy byte mienskiplik.
`filter stats air` lit de stjoertiid sjen dy't dyn repeater besparre hat troch dizze
pakketten net troch te jaan.

De tellers begjinne wer by 0 nei in herstart en nei `clear stats`.
