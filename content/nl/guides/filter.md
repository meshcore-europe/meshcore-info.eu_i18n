---
title: Pakketfilter
lead: 'Zorg dat je repeater geen rommel doorgeeft: floods van ver weg, een bot die nooit stopt, een druk kanaal. Probeer een instelling eerst uit, zet hem dan aan.'
description: 'Het pakketfilter van de DMC-repeaterfirmware: wat het laat vallen, kant-en-klare instellingen voor een gewone en een drukke repeater, elk filtercommando met zijn standaardwaarde, en hoe je ziet wat het heeft laten vallen.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '2bf23d24'
  seeded: '2026-10-26'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['0625daa2', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', 'ffc3f3a0', '3fa1bb28', '09511608']
---

Een repeater (een node die berichten doorgeeft) herhaalt alles wat hij hoort.
Op een drukke mesh zit daar ook rommel bij. Een bot post elke minuut. Eén
node stuurt elke paar minuten opnieuw zijn advertentie, het hallo waarmee
anderen hem vinden. Er komen berichten binnen die het halve land hebben
doorkruist. Elke herhaling kost zendtijd van iedereen om je heen. Met het
pakketfilter laat je repeater dat verkeer vallen in plaats van het door te
geven.

{{< callout type="warning" >}}
Het pakketfilter zit in de **DMC-repeaterfirmware**, de repeaterbuild van
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Standaard
MeshCore heeft geen pakketfilter; het heeft `region denyf *` en
`set flood.max.unscoped`, op de pagina [CLI-commando's](/guides/cli/). Deze
gids volgt de 1.18.0 dev-build `ecfb2d4` van 19 oktober 2026. De stabiele
build 1.17.1 heeft alleen de filters voor hops, snelheid, kanaal, hash en
kapotte berichten. Ook heeft die geen dry-run.
{{< /callout >}}

## Wat het filter doet {#what}

Het filter kijkt alleen naar pakketten die je repeater doorgeeft via flood
(sturen naar elke node binnen bereik). Het raakt nooit aan wat je repeater
zelf verstuurt, of aan pakketten die een bekende route naar één node volgen.
Directe berichten en verzoeken van en naar je eigen contacten komen ook
door. Het kan laten vallen:

- pakketten die al zoveel repeaters (hops) hebben gepasseerd als jij
  toestaat, per pakkettype;
- meer pakketten van één type dan jij per minuut toestaat;
- een advertentie van een node die de afgelopen uren al adverteerde;
- berichten op een kanaal dat jij blokkeert;
- alles wat via één repeater kwam die jij blokkeert;
- groepsberichten van één afzender of met één woord, of alleen een deel
  ervan;
- groepsberichten die kapot zijn, of ouder dan jij toestaat.

Het filter staat **uit** tot jij het aanzet. Je stelt het in met commando's.
Typ ze via USB in de [seriële console](/firmware/console/) op deze site. Of
stuur ze vanuit de MeshCore-app, zoals in de
[repeatergids](/repeater-guide/#config).

## Haal de firmware {#firmware}

Flash **DutchMeshCore Repeater** met de flasher in de
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). De
observerfirmware uit [MQTT op je observer](/guides/mqtt/) heeft hetzelfde
filter.

## Probeer het eerst uit {#dryrun}

In dry-run telt het filter elk pakket dat het zou laten vallen, maar geeft
het nog wel door. Zo bepaal je de juiste waarde van een instelling voordat
het iets laat vallen:

```text
filter on
filter dryrun on
```

Zolang dry-run aanstaat, eindigt de statusregel van `filter` op `(dry-run)`.
De tellingen zijn wat het zou hebben laten vallen. Laat het een dag draaien
en bekijk ze dan (zie [Wat het heeft laten vallen](#stats)). Zien de
getallen er goed uit, dan zet je het echt aan:

```text
filter dryrun off
```

## Aanbevolen configuraties {#configs}

### Een gewone repeater {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Groepsberichten komen door tot 20 per minuut, directe berichten tot 5 per
minuut, en kapotte groepsberichten vallen weg. De eigen gewone configuratie
van de firmware staat 20 directe berichten per minuut toe. Deze pagina neemt
de 5 die zij adviseert sinds een flood van directe berichten in juli 2026.

### Een drukke repeater {#busy}

Voor een repeater op een hoge plek die een hele regio hoort, of een die
overspoeld wordt:

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

Dit halveert de groepsberichten en de advertenties, en geeft de advertentie
van elke node eens per dag door. Berichten die al 16 repeaters hebben
gepasseerd vallen weg. Na een herstart krijgt elke node één advertentie
door. De eigen documentatie van de firmware zet hier ook `filter hash 2`;
deze pagina laat dat weg (zie [Elke instelling](#settings) voor de reden).

### Blokkeer een druk kanaal {#channel}

```text
filter channel add #bot
```

Je repeater hoort het kanaal nog steeds. Hij geeft het niet meer door aan
andere repeaters en companions (de nodes waarmee mensen berichten sturen).
Maximaal 16 kanalen.

### Rem één afzender af {#sender}

Een bot die te vaak post op een kanaal dat je wilt houden:

```text
filter watch add #test
filter sender add Bob 60
```

Bobs berichten op het kanaal Public en `#test` komen nu eens per minuut
door; de rest valt weg. Het filter kijkt naar de naam in het bericht, dus
een afzender die zijn naam wijzigt komt er langs.

### Blokkeer één repeater stroomopwaarts {#path}

Komt de rommel via één repeater binnen, blokkeer dan zijn prefix: het eerste
deel van zijn ID, in hexadecimaal (hex).

```text
filter path add a1b2
```

Een korte prefix zoals `a1` blokkeert ook elke andere repeater met een ID
dat met `a1` begint. Gebruik de langste prefix die je kunt. Maximaal 8
prefixen.

## Elke instelling {#settings}

Pakkettypes gaan op nummer. Op de repeater toont `filter types` dezelfde
nummers met de namen van de firmware, zoals `TXT_MSG` en `GRP_TXT`:

| Nummer | Type | Nummer | Type |
| --- | --- | --- | --- |
| `00` | verzoek | `06` | groepsdata |
| `01` | antwoord | `07` | anoniem verzoek |
| `02` | direct bericht | `08` | pad |
| `03` | bevestiging | `09` | trace |
| `04` | advertentie | `10` | meerdelig |
| `05` | groepsbericht | `11` | besturing |

| Commando | Wat het doet | Standaard |
| --- | --- | --- |
| `filter on` / `filter off` | Zet het filter aan of uit. | uit |
| `filter dryrun on` / `off` | Tel wat zou wegvallen, maar geef alles nog door. | uit |
| `filter hops <type> <max>` | Laat een type vallen dat al zoveel repeaters heeft gepasseerd, 0 tot 64. | 32 voor groepsberichten, 8 voor de rest |
| `filter rate <type> <limit> <secs> [soft]` | Geef hoogstens `limit` van een type door per `secs`. Met `soft` neemt het doorgeven geleidelijk af van `soft` naar `limit`. `0` zet de limiet uit. | 20 per 60 s voor directe en groepsberichten, 10 voor advertenties, 5 voor de rest |
| `filter advert <hours>` | Geef de advertentie van elke node eens per zoveel uur door, tot 720. | 0 (uit) |
| `filter channel add <#name>` | Geef een kanaal niet meer door. | geen |
| `filter path add <hex>` | Laat alles vallen dat via een repeater met deze prefix kwam, 2 tot 8 hex-cijfers. | geen |
| `filter sender add <name> [secs] [prob]` | Laat groepsberichten van een afzender vallen, op Public en bewaakte kanalen. `Bot*` matcht elke naam die met Bot begint. | geen |
| `filter text add <word> [secs] [prob]` | Laat groepsberichten vallen die een woord bevatten, op Public en bewaakte kanalen. `^word` matcht alleen aan het begin. | geen |
| `filter watch add <#name>` | Laat de afzender- en tekstregels ook dit kanaal lezen, tot 4. Public wordt altijd gelezen. | Public |
| `filter malformed on` / `off` | Laat Public-berichten vallen die leeg of kapot zijn, of waarvan de datum meer dan een week afwijkt (de datumcontrole wacht tot de klok is gezet). | uit |
| `filter age <minutes>` / `off` | Laat groepsberichten vallen die ouder zijn dan dit, op Public en bewaakte kanalen, 1 tot 10080. | uit |
| `filter hash <bytes>` | Laat pakketten vallen met een korter pad-ID dan dit, 1 tot 3. | 1 |
| `filter reset` | Zet elke instelling terug op de standaardwaarde. | |

Elke `add` heeft een `remove` en een `list`, zoals `filter channel remove #bot`.
In afzender- en tekstregels laat `secs` één bericht per zoveel seconden door.
`prob` past de regel toe op alleen dat deel van de matches, 1 tot 100.
Maximaal 8 afzender- en 8 tekstregels. Namen en woorden zijn
hoofdlettergevoelig; een naam is maximaal 15 tekens, een woord maximaal 23.

Twee instellingen laten meer vallen dan je misschien verwacht:

- `filter hash 2` laat bijna al het verkeer vallen. Nodes sturen standaard
  pad-ID's van 1 byte.
- `filter age` vertrouwt op de klok van je repeater. Zet die met
  `clock sync` vanuit de app, controleer hem met `clock`, en begin ruim:
  `filter age 60`.

Elke instelling blijft bewaard na een herstart.

## Wat het heeft laten vallen {#stats}

`filter` toont de totalen per reden:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` toont de details van één instelling. De onderwerpen
zijn `hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`,
`sender`, `text` en `age`. `filter stats top` toont de eerste byte van de
node-ID's achter de meeste drops, een aanwijzing en geen bewijs.
`filter stats air` toont de zendtijd die je repeater heeft bespaard door
deze pakketten niet door te geven.

De tellers beginnen weer op 0 na een herstart en na `clear stats`.
