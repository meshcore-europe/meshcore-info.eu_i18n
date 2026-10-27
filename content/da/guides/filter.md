---
title: Pakkefilter
lead: 'Undgå at din repeater sender skrald videre: floods langvejsfra, en bot der aldrig holder pause, en støjende kanal. Prøv en indstilling først, og slå den så til.'
description: 'Pakkefilteret i DMC-repeater-firmwaren: hvad det smider væk, færdige indstillinger til en almindelig og en travl repeater, alle filterkommandoer med deres standardværdi, og hvordan du ser, hvad det smed væk.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '2bf23d24'
  seeded: '2026-10-26'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['0625daa2', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', 'ffc3f3a0', '3fa1bb28', '09511608']
---

En repeater (en node, der sender beskeder videre) gentager alt, hvad den hører.
På et travlt mesh er der også skrald imellem. En bot skriver hvert minut. En node
sender sin advert, det hej der lader andre finde den, igen med få minutters mellemrum.
Der kommer beskeder ind, som har rejst tværs over det halve land. Hver gentagelse
tager sendetid fra alle omkring dig. Med pakkefilteret kan din repeater smide den
trafik væk i stedet for at sende den videre.

{{< callout type="warning" >}}
Pakkefilteret er en del af **DMC-repeater-firmwaren**, repeater-udgaven af
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Standard-MeshCore
har ikke noget pakkefilter; det har `region denyf *` og
`set flood.max.unscoped`, som står på siden med [CLI-kommandoer](/guides/cli/).
Denne guide følger 1.18.0 dev-buildet `ecfb2d4` fra 19. oktober 2026. Det stabile
1.17.1-build har kun filtrene hop, rate, channel, hash og malformed. Det har
heller ikke dry-run.
{{< /callout >}}

## Hvad filteret gør {#what}

Filteret ser kun på pakker, som din repeater sender videre ved flooding (sender
dem til alle noder inden for rækkevidde). Det rører aldrig det, din repeater selv
sender, eller pakker, der følger en kendt rute til én node. Direkte beskeder og
forespørgsler til og fra dine egne kontakter går også igennem. Det kan smide væk:

- pakker, der allerede har passeret så mange repeatere (hop), som du tillader, pr.
  pakketype;
- flere pakker af én type, end du tillader pr. minut;
- en advert fra en node, der allerede har sendt advert inden for de seneste timer;
- beskeder på en kanal, du blokerer;
- alt, hvad der kom gennem én repeater, du blokerer;
- gruppebeskeder fra én afsender eller med ét ord, eller kun nogle af dem;
- gruppebeskeder, der er ødelagte eller ældre, end du tillader.

Filteret er **slået fra**, indtil du slår det til. Du indstiller det med kommandoer.
Skriv dem over USB i [den serielle konsol](/firmware/console/) her på siden. Eller
send dem fra MeshCore-appen, som beskrevet i
[repeater-guiden](/repeater-guide/#config).

## Hent firmwaren {#firmware}

Flash **DutchMeshCore Repeater** med flasheren i
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Observer-firmwaren
fra [MQTT på din observer](/guides/mqtt/) har det samme filter.

## Prøv det først {#dryrun}

I dry-run tæller filteret hver pakke, det ville smide væk, men sender den
stadig videre. Sådan finder du den rette størrelse på en indstilling, før den
smider noget væk:

```text
filter on
filter dryrun on
```

Mens dry-run er slået til, slutter statuslinjen fra `filter` med `(dry-run)`.
Tallene viser, hvad det ville have smidt væk. Lad det køre en dag, og se så på
dem (se [Hvad det smed væk](#stats)). Når tallene ser rigtige ud, sætter du
filteret i kraft:

```text
filter dryrun off
```

## Anbefalede opsætninger {#configs}

### En almindelig repeater {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Gruppebeskeder går igennem op til 20 i minuttet, direkte beskeder op til 5 i
minuttet, og ødelagte gruppebeskeder bliver smidt væk. Firmwarens egen normale
opsætning tillader 20 direkte beskeder i minuttet. Denne side bruger de 5, som
den anbefaler siden en flood af direkte beskeder i juli 2026.

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

Det halverer gruppebeskederne og adverts og sender hver nodes advert igennem én
gang om dagen. Det smider beskeder væk, der allerede har passeret 16 repeatere.
Efter en genstart får hver node én advert igennem. Firmwarens egen dokumentation
sætter her også `filter hash 2`; denne side lader det ude (se
[Alle indstillinger](#settings) for hvorfor).

### Bloker en støjende kanal {#channel}

```text
filter channel add #bot
```

Din repeater hører stadig kanalen. Den sender den ikke længere videre til andre
repeatere og companions (de noder, folk skriver fra). Op til 16 kanaler.

### Sæt én afsender ned i tempo {#sender}

En bot, der skriver for ofte på en kanal, du vil beholde:

```text
filter watch add #test
filter sender add Bob 60
```

Bobs beskeder på Public-kanalen og `#test` går nu igennem én gang i minuttet;
resten bliver smidt væk. Filteret matcher navnet i beskeden, så en afsender, der
skifter navn, slipper forbi det.

### Bloker én repeater opstrøms {#path}

Når skraldet kommer ind gennem én repeater, blokerer du dens præfiks: den første
del af dens ID, i hexadecimal (hex).

```text
filter path add a1b2
```

Et kort præfiks som `a1` blokerer også alle andre repeatere, hvis ID begynder med
`a1`. Brug det længste præfiks, du kan. Op til 8 præfikser.

## Alle indstillinger {#settings}

Pakketyper angives med et nummer. På repeateren viser `filter types` de samme
numre med firmwarens navne, såsom `TXT_MSG` og `GRP_TXT`:

| Nummer | Type | Nummer | Type |
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
| `filter dryrun on` / `off` | Tæller det, der ville blive smidt væk, men sender stadig alt videre. | fra |
| `filter hops <type> <max>` | Smider en type væk, der allerede har passeret så mange repeatere, 0 til 64. | 32 for gruppebeskeder, 8 for resten |
| `filter rate <type> <limit> <secs> [soft]` | Sender højst `limit` af en type igennem pr. `secs`. Med `soft` aftager gennemgangen gradvist fra `soft` til `limit`. `0` slår grænsen fra. | 20 pr. 60 s for direkte beskeder og gruppebeskeder, 10 for adverts, 5 for resten |
| `filter advert <hours>` | Sender hver nodes advert igennem én gang pr. så mange timer, op til 720. | 0 (fra) |
| `filter channel add <#name>` | Holder op med at sende en kanal videre. | ingen |
| `filter path add <hex>` | Smider alt væk, der kom gennem en repeater med dette præfiks, 2 til 8 hex-cifre. | ingen |
| `filter sender add <name> [secs] [prob]` | Smider gruppebeskeder fra en afsender væk, på Public og overvågede kanaler. `Bot*` matcher alle navne, der begynder med Bot. | ingen |
| `filter text add <word> [secs] [prob]` | Smider gruppebeskeder væk, der indeholder et ord, på Public og overvågede kanaler. `^word` matcher kun i begyndelsen. | ingen |
| `filter watch add <#name>` | Lader afsender- og tekstreglerne også læse denne kanal, op til 4. Public læses altid. | Public |
| `filter malformed on` / `off` | Smider Public-beskeder væk, der er tomme, ødelagte eller dateret mere end en uge forkert (datokontrollen venter, til klokken er sat). | fra |
| `filter age <minutes>` / `off` | Smider gruppebeskeder væk, der er ældre end dette, på Public og overvågede kanaler, 1 til 10080. | fra |
| `filter hash <bytes>` | Smider pakker væk med et kortere sti-ID end dette, 1 til 3. | 1 |
| `filter reset` | Sætter alle indstillinger tilbage til standard. | |

Hver `add` har en `remove` og en `list`, såsom `filter channel remove #bot`.
I afsender- og tekstregler lader `secs` én besked gå igennem pr. så mange sekunder.
`prob` anvender reglen på kun den andel af matchene, 1 til 100. Op til 8
afsenderregler og 8 tekstregler. Navne og ord skelner mellem store og små bogstaver;
et navn kan være op til 15 tegn, et ord op til 23.

To indstillinger smider mere væk, end du måske venter:

- `filter hash 2` smider næsten al trafik væk. Noder sender som standard sti-ID'er
  på 1 byte.
- `filter age` stoler på din repeaters klokke. Sæt den med `clock sync` fra appen,
  tjek den med `clock`, og begynd rundhåndet: `filter age 60`.

Alle indstillinger bliver gemt efter en genstart.

## Hvad det smed væk {#stats}

`filter` viser totalerne pr. årsag:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` viser detaljerne for én indstilling. Emnerne er
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` og `age`. `filter stats top` viser den første byte af de node-ID'er, der
står bag flest smidte pakker, et spor snarere end et bevis.
`filter stats air` viser den sendetid, din repeater sparede ved ikke at sende
disse pakker videre.

Tællerne begynder igen fra 0 efter en genstart og efter `clear stats`.
