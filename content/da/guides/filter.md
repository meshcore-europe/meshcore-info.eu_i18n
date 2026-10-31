---
title: Pakkefilter
lead: 'Undgå, at din repeater sender skrald videre: flood fra langt væk, en bot, der aldrig stopper, en støjende kanal. Prøv en indstilling først, og slå den så til.'
description: 'Pakkefilteret i DMC-repeaterfirmwaren: hvad det smider væk, færdige indstillinger til en normal og en travl repeater, alle filterkommandoer med standardværdi, og hvordan du ser, hvad det smed væk.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-10-31'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

En repeater (en node, der sender beskeder videre) gentager alt, hvad den hører.
På et travlt mesh er der også skrald imellem. En bot poster hvert minut. En node
sender sin advert, den hilsen, der lader andre finde den, igen med få minutters
mellemrum. Der kommer beskeder, som har rejst gennem halvdelen af landet. Hver
gentagelse tager sendetid fra alle omkring dig. Med pakkefilteret kan din
repeater smide den trafik væk i stedet for at sende den videre. Vil du først
finde ud af, hvad der oversvømmer dit mesh, og hvad der hjælper ud over
filteret, så læs [Gør meshet robust](/guides/resilient/).

{{< callout type="warning" >}}
Pakkefilteret er en del af **DMC-repeaterfirmwaren**, repeaterudgaven af
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Standard-MeshCore
har intet pakkefilter. Den har `region denyf *` og `set flood.max.unscoped`,
som du finder på siden [CLI-kommandoer](/guides/cli/). Denne guide følger
1.18.0-dev-buildet `ecfb2d4` fra 19. oktober 2026. Det stabile 1.17.1-build har
kun filtrene for hop, rate, kanal, hash og ødelagte pakker. Det har heller
ingen dry-run.
{{< /callout >}}

## Hvad filteret gør {#what}

Filteret ser kun på pakker, som din repeater sender videre med flood (til alle
noder inden for rækkevidde). Det rører aldrig det, din repeater selv sender,
eller pakker, der følger en kendt rute til én node. Direkte beskeder og
forespørgsler til og fra dine egne kontakter slipper også igennem. Filteret kan
smide følgende væk:

- pakker, der allerede er gået gennem så mange repeatere (hop), som du tillader,
  pr. pakketype;
- flere pakker af én type pr. minut, end du tillader;
- en advert fra en node, der allerede har sendt en advert inden for de seneste
  timer;
- beskeder på en kanal, du blokerer;
- alt, der er kommet gennem én repeater, du blokerer;
- gruppebeskeder fra én afsender eller med ét ord, eller kun nogle af dem;
- gruppebeskeder, der er ødelagte eller ældre, end du tillader.

Filteret er **slået fra**, indtil du slår det til. Du indstiller det med
kommandoer. Skriv dem over USB i [den serielle konsol](/firmware/console/) her
på siden. Eller send dem fra MeshCore-appen, som beskrevet i
[repeaterguiden](/repeater-guide/#config).

## Hent firmwaren {#firmware}

Flash **DutchMeshCore Repeater** med flasheren i
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Observer-firmwaren
fra [MQTT på din observer](/guides/mqtt/) har det samme filter.

## Prøv det først {#dryrun}

I dry-run tæller filteret hver pakke, det ville smide væk, men sender den
stadig videre. Sådan finder du den rette indstilling, før den smider noget væk:

```text
filter on
filter dryrun on
```

Mens dry-run er slået til, slutter statuslinjen fra `filter` med `(dry-run)`.
Tallene viser, hvad filteret ville have smidt væk. Lad det køre et døgn, og se
så på tallene (se [Hvad det smed væk](#stats)). Når tallene ser rigtige ud,
gør du filteret aktivt:

```text
filter dryrun off
```

## Anbefalede opsætninger {#configs}

### En normal repeater {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Op til 20 gruppebeskeder pr. minut slipper igennem, og op til 5 direkte
beskeder pr. minut. Ødelagte gruppebeskeder bliver smidt væk. Firmwarens egen
normale opsætning tillader 20 direkte beskeder pr. minut. Denne side bruger de
5, som firmwaren har anbefalet siden en flood af direkte beskeder i juli 2026.

### En travl repeater {#busy}

Til en repeater på et højt sted, der hører en hel region, eller en, der bliver
oversvømmet:

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

Det halverer gruppebeskederne og adverts, og hver nodes advert slipper igennem
én gang i døgnet. Beskeder, der allerede er gået gennem 16 repeatere, bliver
smidt væk. Efter en genstart får hver node én advert igennem. Firmwarens egen
dokumentation sætter også `filter hash 2` her. Denne side udelader den (se
[Alle indstillinger](#settings) for hvorfor).

### Bloker en støjende kanal {#channel}

```text
filter channel add #bot
```

Din repeater hører stadig kanalen. Den sender den ikke længere videre til
andre repeatere og companions (de noder, folk skriver beskeder fra). Op til 16
kanaler.

### Sæt farten ned for én afsender {#sender}

En bot, der poster for tit på en kanal, du gerne vil beholde:

```text
filter watch add #test
filter sender add Bob 60
```

Nu slipper Bobs beskeder på Public-kanalen og `#test` igennem én gang i
minuttet. Resten bliver smidt væk. Filteret sammenligner med navnet i beskeden,
så en afsender, der skifter navn, slipper udenom.

### Bloker én repeater længere oppe {#path}

Kommer skraldet ind gennem én repeater, så bloker dens præfiks: den første del
af dens ID i hexadecimal (hex). Det kræver 1.18-dev-buildet. 1.17.1 har intet
sti-filter.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` viser de præfikser, du blokerer, og `filter stats path`
viser, hvor meget hvert præfiks har smidt væk. Med `filter path remove a1b2`
slipper repeateren igennem igen. Et kort præfiks som `a1` blokerer også alle
andre repeatere, hvis ID starter med `a1`. Brug det længste præfiks, du kan.
Op til 8 præfikser.

## Alle indstillinger {#settings}

Pakketyper angives med tal. På repeateren viser `filter types` de samme tal med
firmwarens navne, fx `TXT_MSG` og `GRP_TXT`:

| Tal | Type | Tal | Type |
| --- | --- | --- | --- |
| `00` | forespørgsel | `06` | gruppedata |
| `01` | svar | `07` | anonym forespørgsel |
| `02` | direkte besked | `08` | sti |
| `03` | kvittering | `09` | trace |
| `04` | advert | `10` | flerdelt |
| `05` | gruppebesked | `11` | kontrol |

| Kommando | Hvad den gør | Standard |
| --- | --- | --- |
| `filter on` / `filter off` | Slår filteret til eller fra. | fra |
| `filter dryrun on` / `off` | Tæller frasorteringer, men sender stadig alt videre. | fra |
| `filter hops <type> <max>` | Smider en type væk, der allerede er gået gennem så mange repeatere, 0 til 64. | 32 for gruppebeskeder, 8 for resten |
| `filter rate <type> <limit> <secs> [soft]` | Sender højst `limit` af en type videre pr. `secs`. Med `soft` aftager videresendingen gradvist fra `soft` til `limit`. `0` slår grænsen fra. | 20 pr. 60 s for direkte beskeder og gruppebeskeder, 10 for adverts, 5 for resten |
| `filter advert <hours>` | Sender hver nodes advert videre én gang pr. det antal timer, op til 720. | 0 (fra) |
| `filter channel add <#name>` | Stopper videresending af en kanal. | ingen |
| `filter path add <hex>` | Smider alt væk, der er kommet gennem en repeater med dette præfiks, 2 til 8 hex-cifre. | ingen |
| `filter sender add <name> [secs] [prob]` | Smider gruppebeskeder fra en afsender væk på Public og overvågede kanaler. `Bot*` passer på alle navne, der starter med Bot. | ingen |
| `filter text add <word> [secs] [prob]` | Smider gruppebeskeder med et bestemt ord væk på Public og overvågede kanaler. `^word` passer kun i starten. | ingen |
| `filter watch add <#name>` | Lader afsender- og tekstreglerne også læse denne kanal, op til 4. Public bliver altid læst. | Public |
| `filter malformed on` / `off` | Smider Public-beskeder væk, der er tomme, ødelagte eller dateret mere end en uge forkert (datotjekket venter, til uret er stillet). | fra |
| `filter age <minutes>` / `off` | Smider gruppebeskeder ældre end dette væk på Public og overvågede kanaler, 1 til 10080. | fra |
| `filter hash <bytes>` | Smider pakker med et kortere sti-ID end dette væk, 1 til 3. | 1 |
| `filter reset` | Sætter alle indstillinger tilbage til standard. | |

Hver `add` har en `remove` og en `list`, fx `filter channel remove #bot`.
I afsender- og tekstregler lader `secs` én besked pr. det antal sekunder slippe
igennem. `prob` anvender kun reglen på den andel af træfferne, 1 til 100. Op til
8 afsenderregler og 8 tekstregler. Navne og ord skelner mellem store og små
bogstaver. Et navn er højst 15 tegn, et ord højst 23.

To indstillinger smider mere væk, end du måske regner med:

- `filter hash 2` smider næsten al trafik væk. Noder sender som standard sti-ID'er
  på 1 byte.
- `filter age` stoler på din repeaters ur. Stil det med `clock sync` fra appen,
  tjek det med `clock`, og start med en rummelig værdi: `filter age 60`.

Alle indstillinger bevares efter en genstart.

## Hvad det smed væk {#stats}

`filter` viser totalerne pr. årsag:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` viser detaljerne for én indstilling. Emnerne er `hops`,
`rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`, `text` og
`age`. `filter stats top` viser den første byte af node-ID'erne bag flest
frasorteringer. Mange noder deler den byte.
`filter stats air` viser den sendetid, din repeater har sparet ved ikke at
sende disse pakker videre.

Tællerne starter forfra ved 0 efter en genstart og efter `clear stats`.
