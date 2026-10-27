---
title: Pakkefilter
lead: 'Hindre repeateren din i å sende søppel videre: floods langveisfra, en bot som aldri stopper, en støyende kanal. Prøv en innstilling først, og slå den på etterpå.'
description: 'Pakkefilteret i DMC-repeaterfirmwaren: hva det kaster, ferdige innstillinger for en vanlig og en travel repeater, hver filterkommando med standardverdi, og hvordan du ser hva det kastet.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '2bf23d24'
  seeded: '2026-10-26'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['0625daa2', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', 'ffc3f3a0', '3fa1bb28', '09511608']
---

En repeater (en node som sender meldinger videre) gjentar alt den hører.
På et travelt mesh er det også søppel. En bot poster hvert minutt. Én node sender
adverten sin, hilsenen som lar andre finne den, på nytt med noen minutters mellomrom.
Det kommer meldinger som har reist over halve landet. Hver gjentakelse tar
sendetid fra alle rundt deg. Med pakkefilteret kan repeateren din kaste
den trafikken i stedet for å sende den videre.

{{< callout type="warning" >}}
Pakkefilteret er en del av **DMC-repeaterfirmwaren**, repeaterutgaven
av [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Standard
MeshCore har ikke noe pakkefilter; den har `region denyf *` og
`set flood.max.unscoped`, som du finner på siden [CLI-kommandoer](/guides/cli/). Denne
veiledningen følger 1.18.0 dev-byggen `ecfb2d4` fra 19. oktober 2026. Den stabile
1.17.1-byggen har bare hopp-, rate-, kanal-, hash- og malformed-filtrene. Den
har heller ikke dry-run.
{{< /callout >}}

## Hva filteret gjør {#what}

Filteret ser bare på pakker repeateren din sender videre ved flooding (sending
til hver node innen rekkevidde). Det rører aldri det repeateren din sender
selv, eller pakker som følger en kjent rute til én node. Direktemeldinger og
forespørsler til og fra dine egne kontakter slipper også gjennom. Det kan kaste:

- pakker som allerede har passert så mange repeatere (hopp) som du tillater, per
  pakketype;
- flere pakker av én type enn du tillater per minutt;
- en advert fra en node som allerede har sendt advert de siste timene;
- meldinger på en kanal du blokkerer;
- alt som kom gjennom én repeater du blokkerer;
- gruppemeldinger fra én avsender eller med ett ord, eller bare noen av dem;
- gruppemeldinger som er ødelagte, eller eldre enn du tillater.

Filteret er **av** til du slår det på. Du stiller det inn med kommandoer. Skriv
dem over USB i [seriekonsollen](/firmware/console/) på dette nettstedet. Eller
send dem fra MeshCore-appen, slik
[repeaterveiledningen](/repeater-guide/#config) viser.

## Hent firmwaren {#firmware}

Flash **DutchMeshCore Repeater** fra flasheren i
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Observer-firmwaren
fra [MQTT på observeren din](/guides/mqtt/) har det samme filteret.

## Prøv det først {#dryrun}

I dry-run teller filteret hver pakke det ville ha kastet, men sender den
likevel videre. Slik finner du riktig innstilling før det kaster noe:

```text
filter on
filter dryrun on
```

Mens dry-run er på, slutter statuslinjen til `filter` med `(dry-run)`. Tallene
viser hva det ville ha kastet. La det gå en dag, og se så
på dem (se [Hva det kastet](#stats)). Når tallene ser riktige ut, setter du
det i drift:

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

Gruppemeldinger slipper gjennom med inntil 20 i minuttet, direktemeldinger med inntil 5 i minuttet,
og ødelagte gruppemeldinger blir kastet. Firmwarens eget vanlige
oppsett tillater 20 direktemeldinger i minuttet. Denne siden bruker de 5 den
anbefaler etter en flood av direktemeldinger i juli 2026.

### En travel repeater {#busy}

For en repeater på et høyt sted som hører en hel region, eller en som
blir oversvømt:

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

Dette halverer gruppemeldingene og advertene, og slipper hver nodes
advert gjennom én gang i døgnet. Det kaster meldinger som allerede har passert 16 repeatere. Etter en
omstart får hver node én advert gjennom. Firmwarens egen dokumentasjon setter også
`filter hash 2` her; denne siden utelater det (se
[Hver innstilling](#settings) for hvorfor).

### Blokker en støyende kanal {#channel}

```text
filter channel add #bot
```

Repeateren din hører fortsatt kanalen. Den sender den ikke lenger videre til andre
repeatere og companions (nodene folk sender meldinger fra). Inntil 16 kanaler.

### Brems én avsender {#sender}

En bot som poster for ofte på en kanal du vil beholde:

```text
filter watch add #test
filter sender add Bob 60
```

Bobs meldinger på Public-kanalen og `#test` slipper nå gjennom én gang i minuttet;
resten blir kastet. Filteret matcher navnet i meldingen, så en avsender som
bytter navn kommer forbi det.

### Blokker én repeater oppstrøms {#path}

Når søppelet kommer inn gjennom én repeater, blokkerer du prefikset dens: den første
delen av ID-en, i heksadesimal (hex).

```text
filter path add a1b2
```

Et kort prefiks som `a1` blokkerer også hver annen repeater med ID som starter
med `a1`. Bruk det lengste prefikset du kan. Inntil 8 prefikser.

## Hver innstilling {#settings}

Pakketyper angis med nummer. På repeateren viser `filter types` de samme
numrene med firmwarens navn, som `TXT_MSG` og `GRP_TXT`:

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
| `filter dryrun on` / `off` | Teller kast, men sender likevel alt videre. | av |
| `filter hops <type> <max>` | Kaster en type som allerede har passert så mange repeatere, 0 til 64. | 32 for gruppemeldinger, 8 for resten |
| `filter rate <type> <limit> <secs> [soft]` | Slipper gjennom høyst `limit` av en type per `secs`. Med `soft` avtar gjennomslippet gradvis fra `soft` til `limit`. `0` slår grensen av. | 20 per 60 s for direkte- og gruppemeldinger, 10 for adverter, 5 for resten |
| `filter advert <hours>` | Slipper hver nodes advert gjennom én gang per så mange timer, inntil 720. | 0 (av) |
| `filter channel add <#name>` | Slutter å sende en kanal videre. | ingen |
| `filter path add <hex>` | Kaster alt som kom gjennom en repeater med dette prefikset, 2 til 8 hex-sifre. | ingen |
| `filter sender add <name> [secs] [prob]` | Kaster gruppemeldinger fra en avsender, på Public og overvåkede kanaler. `Bot*` matcher hvert navn som starter med Bot. | ingen |
| `filter text add <word> [secs] [prob]` | Kaster gruppemeldinger som inneholder et ord, på Public og overvåkede kanaler. `^word` matcher bare i starten. | ingen |
| `filter watch add <#name>` | Lar avsender- og tekstreglene lese denne kanalen også, inntil 4. Public leses alltid. | Public |
| `filter malformed on` / `off` | Kaster Public-meldinger som er tomme, ødelagte eller datert mer enn en uke feil (datosjekken venter til klokken er stilt). | av |
| `filter age <minutes>` / `off` | Kaster gruppemeldinger eldre enn dette, på Public og overvåkede kanaler, 1 til 10080. | av |
| `filter hash <bytes>` | Kaster pakker med kortere sti-ID enn dette, 1 til 3. | 1 |
| `filter reset` | Setter hver innstilling tilbake til standard. | |

Hver `add` har en `remove` og en `list`, som `filter channel remove #bot`.
I avsender- og tekstregler lar `secs` én melding slippe gjennom per så mange sekunder.
`prob` bruker regelen på bare den andelen av treffene, 1 til 100. Inntil 8
avsenderregler og 8 tekstregler. Navn og ord skiller mellom store og små bokstaver; et navn kan ha inntil
15 tegn, et ord inntil 23.

To innstillinger kaster mer enn du kanskje venter:

- `filter hash 2` kaster nesten all trafikk. Noder sender sti-ID-er på 1 byte som
  standard.
- `filter age` stoler på klokken i repeateren din. Still den med `clock sync` fra
  appen, sjekk den med `clock`, og start romslig: `filter age 60`.

Hver innstilling beholdes etter en omstart.

## Hva det kastet {#stats}

`filter` viser totalene per årsak:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` viser detaljene for én innstilling. Emnene er
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` og `age`. `filter stats top` viser den første byten i node-ID-ene
bak flest kast, et spor heller enn bevis.
`filter stats air` viser sendetiden repeateren din sparte ved ikke å sende disse
pakkene videre.

Tellerne starter på 0 igjen etter en omstart og etter `clear stats`.
