---
title: Pakketfilter
lead: 'Zorg dat je repeater geen rommel doorgeeft: floods van ver weg, een bot die nooit stopt, een druk kanaal. Probeer een instelling eerst uit en zet hem dan aan.'
description: 'Het pakketfilter van de DMC-repeaterfirmware: wat het weggooit, kant-en-klare instellingen voor een normale en een drukke repeater, elk filtercommando met zijn standaardwaarde, en hoe je ziet wat het weggooide.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-10-31'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Een repeater (een node die berichten doorgeeft) herhaalt alles wat hij hoort.
Op een drukke mesh zit daar ook rommel tussen. Een bot post elke minuut. Een
node stuurt om de paar minuten opnieuw zijn advertentie, het hallo waarmee
anderen hem vinden. Er komen berichten binnen die het halve land door zijn
gereisd. Elke herhaling kost zendtijd voor iedereen om je heen. Met het
pakketfilter gooit je repeater dat verkeer weg in plaats van het door te
geven. Hoe je eerst uitzoekt wat je mesh overspoelt, en wat er naast het
filter helpt, lees je in [Maak de mesh robuust](/guides/resilient/).

{{< callout type="warning" >}}
Het pakketfilter hoort bij de **DMC-repeaterfirmware**, de repeaterversie van
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Standaard
MeshCore heeft geen pakketfilter. Het heeft wel `region denyf *` en
`set flood.max.unscoped`, op de pagina [CLI-commando's](/guides/cli/). Deze
handleiding volgt de 1.18.0-devversie `ecfb2d4` van 19 oktober 2026. De
stabiele versie 1.17.1 heeft alleen de filters voor hops, rate, kanaal, hash
en kapotte berichten. Dry-run zit daar ook niet in.
{{< /callout >}}

## Wat het filter doet {#what}

Het filter kijkt alleen naar pakketten die je repeater via flood doorgeeft
(naar elke node binnen bereik). Wat je repeater zelf verstuurt, blijft
ongemoeid. Dat geldt ook voor pakketten die een bekende route naar één node
volgen. Directe berichten en verzoeken van en naar je eigen contacten komen
ook door. Het filter kan dit weggooien:

- pakketten die al zoveel repeaters (hops) zijn gepasseerd als je toestaat,
  per pakkettype;
- meer pakketten van één type per minuut dan je toestaat;
- een advertentie van een node die de afgelopen uren al een advertentie
  stuurde;
- berichten op een kanaal dat je blokkeert;
- alles wat via één repeater kwam die je blokkeert;
- groepsberichten van één afzender of met één woord, of maar een deel ervan;
- groepsberichten die kapot zijn, of ouder dan je toestaat.

Het filter staat **uit** tot je het aanzet. Je stelt het in met commando's.
Typ ze via USB in de [seriële console](/firmware/console/) op deze site. Of
stuur ze vanuit de MeshCore-app, zoals in de
[repeaterhandleiding](/repeater-guide/#config).

## De firmware installeren {#firmware}

Flash **DutchMeshCore Repeater** met de flasher in de
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). De
observerfirmware uit [MQTT op je observer](/guides/mqtt/) heeft hetzelfde
filter.

## Eerst uitproberen {#dryrun}

In dry-run telt het filter elk pakket dat het zou weggooien. Het geeft dat
pakket toch door. Zo stel je een instelling af voordat er iets verdwijnt:

```text
filter on
filter dryrun on
```

Zolang dry-run aanstaat, eindigt de statusregel van `filter` op `(dry-run)`.
De tellingen laten zien wat het filter zou hebben weggegooid. Laat het een
dag draaien en bekijk dan de cijfers (zie [Wat het weggooide](#stats)). Als
de cijfers kloppen, zet je het filter echt aan:

```text
filter dryrun off
```

## Aanbevolen instellingen {#configs}

### Een normale repeater {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Groepsberichten gaan door tot 20 per minuut, directe berichten tot 5 per
minuut. Kapotte groepsberichten gooit de repeater weg. De normale instelling
van de firmware zelf staat 20 directe berichten per minuut toe. Sinds een
flood van directe berichten in juli 2026 neemt deze pagina de 5 over die de
firmware aanraadt.

### Een drukke repeater {#busy}

Voor een repeater op een hoge plek die een hele regio hoort, of een repeater
die overspoeld wordt:

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

Dit halveert de groepsberichten en de advertenties. De advertentie van elke
node gaat nog één keer per dag door. Berichten die al 16 repeaters zijn
gepasseerd, gooit het filter weg. Na een herstart krijgt elke node één
advertentie door. De eigen documentatie van de firmware zet hier ook
`filter hash 2`. Deze pagina laat dat weg (zie [Alle instellingen](#settings)
voor de reden).

### Een druk kanaal blokkeren {#channel}

```text
filter channel add #bot
```

Je repeater hoort het kanaal nog steeds. Hij geeft het alleen niet meer door
aan andere repeaters en companions (de nodes waarmee mensen berichten sturen).
Maximaal 16 kanalen.

### Eén afzender afremmen {#sender}

Een bot post te vaak op een kanaal dat je wilt houden:

```text
filter watch add #test
filter sender add Bob 60
```

De berichten van Bob op het kanaal Public en op `#test` gaan nu één keer per
minuut door. De rest gooit het filter weg. Het filter kijkt naar de naam in
het bericht. Een afzender die zijn naam verandert, komt er dus langs.

### Eén repeater stroomopwaarts blokkeren {#path}

Als de rommel via één repeater binnenkomt, blokkeer je zijn prefix: het eerste
deel van zijn ID, in hexadecimaal (hex). Daarvoor heb je de 1.18-devversie
nodig. Versie 1.17.1 heeft geen padfilter.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` toont de prefixen die je blokkeert. `filter stats path`
toont hoeveel elk prefix heeft weggegooid. Met `filter path remove a1b2` laat
je hem weer door. Een kort prefix zoals `a1` blokkeert ook elke andere
repeater met een ID dat met `a1` begint. Kies het langste prefix dat je kunt.
Maximaal 8 prefixen.

## Alle instellingen {#settings}

Pakkettypen hebben een nummer. Op de repeater toont `filter types` dezelfde
nummers met de namen uit de firmware, zoals `TXT_MSG` en `GRP_TXT`:

| Nummer | Type | Nummer | Type |
| --- | --- | --- | --- |
| `00` | verzoek | `06` | groepsdata |
| `01` | antwoord | `07` | anoniem verzoek |
| `02` | direct bericht | `08` | pad |
| `03` | bevestiging | `09` | trace |
| `04` | advertentie | `10` | multipart |
| `05` | groepsbericht | `11` | besturing |

| Commando | Wat het doet | Standaard |
| --- | --- | --- |
| `filter on` / `filter off` | Zet het filter aan of uit. | uit |
| `filter dryrun on` / `off` | Telt wat het zou weggooien, maar geeft alles door. | uit |
| `filter hops <type> <max>` | Gooit een type weg dat al zoveel repeaters is gepasseerd, 0 tot 64. | 32 voor groepsberichten, 8 voor de rest |
| `filter rate <type> <limit> <secs> [soft]` | Geeft van een type hooguit `limit` per `secs` door. Met `soft` neemt het doorgeven geleidelijk af van `soft` naar `limit`. `0` zet de limiet uit. | 20 per 60 s voor directe berichten en groepsberichten, 10 voor advertenties, 5 voor de rest |
| `filter advert <hours>` | Geeft de advertentie van elke node één keer per zoveel uur door, tot 720. | 0 (uit) |
| `filter channel add <#name>` | Geeft een kanaal niet meer door. | geen |
| `filter path add <hex>` | Gooit alles weg wat via een repeater met dit prefix kwam, 2 tot 8 hexcijfers. | geen |
| `filter sender add <name> [secs] [prob]` | Gooit groepsberichten van een afzender weg, op Public en op gevolgde kanalen. `Bot*` past op elke naam die met Bot begint. | geen |
| `filter text add <word> [secs] [prob]` | Gooit groepsberichten met een bepaald woord weg, op Public en op gevolgde kanalen. `^word` past alleen aan het begin. | geen |
| `filter watch add <#name>` | Laat de afzender- en tekstregels ook dit kanaal lezen, maximaal 4. Public lezen ze altijd. | Public |
| `filter malformed on` / `off` | Gooit Public-berichten weg die leeg of kapot zijn, of waarvan de datum meer dan een week afwijkt (de datumcontrole wacht tot de klok is ingesteld). | uit |
| `filter age <minutes>` / `off` | Gooit groepsberichten weg die ouder zijn dan dit, op Public en op gevolgde kanalen, 1 tot 10080. | uit |
| `filter hash <bytes>` | Gooit pakketten weg met een korter pad-ID dan dit, 1 tot 3. | 1 |
| `filter reset` | Zet elke instelling terug op de standaardwaarde. | |

Bij elke `add` hoort een `remove` en een `list`, zoals
`filter channel remove #bot`. In afzender- en tekstregels laat `secs` één
bericht per zoveel seconden door. Met `prob` geldt de regel maar voor dat
deel van de treffers, 1 tot 100. Maximaal 8 afzenderregels en 8 tekstregels.
Namen en woorden zijn hoofdlettergevoelig. Een naam is maximaal 15 tekens
lang, een woord maximaal 23.

Twee instellingen gooien meer weg dan je misschien verwacht:

- `filter hash 2` gooit bijna al het verkeer weg. Nodes sturen standaard pad-ID's
  van 1 byte.
- `filter age` vertrouwt op de klok van je repeater. Stel die in met
  `clock sync` vanuit de app, controleer hem met `clock` en begin ruim:
  `filter age 60`.

Elke instelling blijft bewaard na een herstart.

## Wat het weggooide {#stats}

`filter` toont de totalen per reden:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` toont de details van één instelling. De onderwerpen
zijn `hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`,
`sender`, `text` en `age`. `filter stats top` toont de eerste byte van de
node-ID's achter de meeste weggegooide pakketten. Veel nodes delen die byte.
`filter stats air` toont hoeveel zendtijd je repeater heeft bespaard door
deze pakketten niet door te geven.

De tellers beginnen weer bij 0 na een herstart en na `clear stats`.
