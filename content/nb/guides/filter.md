---
title: Pakkefilter
lead: 'Hindre at repeateren din sender videre søppel: flood fra langt unna, en bot som aldri stopper, en støyende kanal. Prøv en innstilling først, og slå den så på.'
description: 'Pakkefilteret i DMC-repeaterfirmwaren: hva det forkaster, ferdige innstillinger for en vanlig og en travel repeater, alle filterkommandoer med standardverdi, og hvordan du ser hva det forkastet.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-10-31'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

En repeater (en node som sender meldinger videre) gjentar alt den hører.
På et travelt mesh er noe av det søppel. En bot poster hvert minutt. En node
sender advert, hilsenen som lar andre finne den, på nytt med noen minutters
mellomrom. Det kommer meldinger som har reist over halve landet. Hver
gjentakelse tar sendetid fra alle rundt deg. Med pakkefilteret kan repeateren
din forkaste denne trafikken i stedet for å sende den videre. Vil du først
finne ut hva som oversvømmer meshet ditt, og hva som hjelper utenom filteret,
les [Gjør meshet robust](/guides/resilient/).

{{< callout type="warning" >}}
Pakkefilteret er en del av **DMC-repeaterfirmwaren**, repeaterversjonen av
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Vanlig
MeshCore har ikke pakkefilter. Der finnes `region denyf *` og
`set flood.max.unscoped`, beskrevet på siden [CLI-kommandoer](/guides/cli/).
Denne veiledningen bygger på 1.18.0-utviklingsversjonen `ecfb2d4` fra 19. oktober 2026. Den stabile
1.17.1-versjonen har bare filtrene for hopp, rate, kanal, hash og ødelagte
pakker. Den har heller ikke dry-run.
{{< /callout >}}

## Hva filteret gjør {#what}

Filteret ser bare på pakker som repeateren din sender videre med flood (til
alle noder innen rekkevidde). Det rører aldri det repeateren selv sender,
eller pakker som følger en kjent rute til én node. Direktemeldinger og
forespørsler til og fra dine egne kontakter slipper også gjennom. Filteret kan forkaste:

- pakker som allerede har gått gjennom så mange repeatere (hopp) som du
  tillater, per pakketype;
- flere pakker av én type per minutt enn du tillater;
- en advert fra en node som allerede har sendt advert de siste timene;
- meldinger på en kanal du blokkerer;
- alt som har kommet gjennom én repeater du blokkerer;
- gruppemeldinger fra én avsender eller med ett bestemt ord, eller bare noen av dem;
- gruppemeldinger som er ødelagte, eller eldre enn du tillater.

Filteret er **av** til du slår det på. Du stiller det inn med kommandoer.
Skriv dem over USB i [seriekonsollen](/firmware/console/) her på nettstedet.
Du kan også sende dem fra MeshCore-appen, som i
[repeaterveiledningen](/repeater-guide/#config).

## Skaff firmwaren {#firmware}

Flash **DutchMeshCore Repeater** med flasheren i
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Observer-firmwaren
fra [MQTT på observeren din](/guides/mqtt/) har det samme filteret.

## Prøv det først {#dryrun}

I dry-run teller filteret hver pakke det ville ha forkastet, men sender den
likevel videre. Slik finner du riktig innstilling før noe blir forkastet:

```text
filter on
filter dryrun on
```

Mens dry-run er på, slutter statuslinjen til `filter` med `(dry-run)`.
Tellerne viser hva filteret ville ha forkastet. La det stå på i et døgn, og
se så på tallene (se [Hva det forkastet](#stats)). Når tallene ser riktige
ut, slår du filteret på for alvor:

```text
filter dryrun off
```

## Anbefalte oppsett {#configs}

### En vanlig repeater {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Opptil 20 gruppemeldinger i minuttet slipper gjennom, og opptil 5
direktemeldinger i minuttet. Ødelagte gruppemeldinger blir forkastet. Firmwarens eget
vanlige oppsett tillater 20 direktemeldinger i minuttet. Denne siden bruker
de 5 som firmwaren har anbefalt siden en flood av direktemeldinger i juli 2026.

### En travel repeater {#busy}

For en repeater på et høyt punkt som hører en hel region, eller en som blir
oversvømt:

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

Dette halverer gruppemeldingene og advertene, og slipper gjennom advert fra
hver node én gang i døgnet. Meldinger som allerede har gått gjennom 16
repeatere, blir forkastet. Etter en omstart får hver node én advert gjennom.
Firmwarens egen dokumentasjon setter også `filter hash 2` her. Denne siden
utelater den (se [Alle innstillinger](#settings) for hvorfor).

### Blokker en støyende kanal {#channel}

```text
filter channel add #bot
```

Repeateren din hører fortsatt kanalen. Den sender den ikke lenger videre til
andre repeatere og companions (nodene folk sender meldinger fra). Opptil 16 kanaler.

### Brems én avsender {#sender}

En bot som poster for ofte på en kanal du vil beholde:

```text
filter watch add #test
filter sender add Bob 60
```

Meldingene fra Bob på Public-kanalen og `#test` slipper nå gjennom én gang i
minuttet. Resten blir forkastet. Filteret kjenner igjen navnet i meldingen, så
en avsender som bytter navn, slipper forbi.

### Blokker én repeater lenger opp {#path}

Når søppelet kommer inn gjennom én repeater, blokkerer du prefikset til den:
første del av ID-en, i heksadesimal (hex). Dette krever 1.18-utviklingsversjonen.
1.17.1 har ikke sti-filter.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` viser prefiksene du blokkerer, og `filter stats path` hvor
mye hvert av dem har forkastet. `filter path remove a1b2` slipper repeateren
gjennom igjen. Et kort prefiks som `a1` blokkerer også alle andre repeatere
med ID som begynner på `a1`. Bruk så langt prefiks du kan. Opptil 8 prefikser.

## Alle innstillinger {#settings}

Pakketyper angis med nummer. På repeateren viser `filter types` de samme
numrene med firmwarens navn, for eksempel `TXT_MSG` og `GRP_TXT`:

| Nummer | Type | Nummer | Type |
| --- | --- | --- | --- |
| `00` | forespørsel | `06` | gruppedata |
| `01` | svar | `07` | anonym forespørsel |
| `02` | direktemelding | `08` | sti |
| `03` | kvittering | `09` | trace |
| `04` | advert | `10` | flerdelt |
| `05` | gruppemelding | `11` | kontroll |

| Kommando | Hva den gjør | Standard |
| --- | --- | --- |
| `filter on` / `filter off` | Slår filteret på eller av. | av |
| `filter dryrun on` / `off` | Teller forkastinger, men sender likevel alt videre. | av |
| `filter hops <type> <max>` | Forkaster en type som allerede har gått gjennom så mange repeatere, 0 til 64. | 32 for gruppemeldinger, 8 for resten |
| `filter rate <type> <limit> <secs> [soft]` | Slipper gjennom høyst `limit` av en type per `secs`. Med `soft` trappes gjennomslippet ned fra `soft` til `limit`. `0` slår grensen av. | 20 per 60 s for direkte- og gruppemeldinger, 10 for adverts, 5 for resten |
| `filter advert <hours>` | Slipper gjennom advert fra hver node én gang per så mange timer, opptil 720. | 0 (av) |
| `filter channel add <#name>` | Slutter å sende en kanal videre. | ingen |
| `filter path add <hex>` | Forkaster alt som har kommet gjennom en repeater med dette prefikset, 2 til 8 hex-sifre. | ingen |
| `filter sender add <name> [secs] [prob]` | Forkaster gruppemeldinger fra en avsender, på Public og overvåkede kanaler. `Bot*` treffer alle navn som begynner på Bot. | ingen |
| `filter text add <word> [secs] [prob]` | Forkaster gruppemeldinger som inneholder et ord, på Public og overvåkede kanaler. `^word` treffer bare i starten. | ingen |
| `filter watch add <#name>` | Lar avsender- og tekstreglene lese denne kanalen også, opptil 4. Public blir alltid lest. | Public |
| `filter malformed on` / `off` | Forkaster Public-meldinger som er tomme, ødelagte eller datert mer enn en uke feil (datosjekken venter til klokken er stilt). | av |
| `filter age <minutes>` / `off` | Forkaster gruppemeldinger eldre enn dette, på Public og overvåkede kanaler, 1 til 10080. | av |
| `filter hash <bytes>` | Forkaster pakker med kortere sti-ID enn dette, 1 til 3. | 1 |
| `filter reset` | Setter alle innstillinger tilbake til standard. | |

Hver `add` har en `remove` og en `list`, for eksempel `filter channel remove #bot`.
I avsender- og tekstregler slipper `secs` gjennom én melding per så mange
sekunder. `prob` bruker regelen bare på den andelen av treffene, 1 til 100.
Opptil 8 avsenderregler og 8 tekstregler. Navn og ord skiller mellom store og
små bokstaver. Et navn kan være opptil 15 tegn, et ord opptil 23.

Disse to innstillingene forkaster mer enn du kanskje tror:

- `filter hash 2` forkaster nesten all trafikk. Noder sender 1-byte sti-ID-er
  som standard.
- `filter age` stoler på klokken i repeateren din. Still den med `clock sync`
  fra appen, sjekk den med `clock`, og begynn romslig: `filter age 60`.

Alle innstillinger beholdes etter en omstart.

## Hva det forkastet {#stats}

`filter` viser totalene per årsak:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` viser detaljene for én innstilling. Emnene er
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` og `age`. `filter stats top` viser første byte av node-ID-ene som står
bak flest forkastinger. Mange noder deler den byten.
`filter stats air` viser sendetiden repeateren din sparte ved ikke å sende
disse pakkene videre.

Tellerne starter på 0 igjen etter en omstart og etter `clear stats`.
