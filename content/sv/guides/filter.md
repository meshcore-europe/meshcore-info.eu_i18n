---
title: Paketfilter
lead: 'Hindra din repeater från att skicka skräp vidare: floods långt bortifrån, en bot som aldrig slutar, en stökig kanal. Prova en inställning först, slå sedan på den.'
description: 'Paketfiltret i DMC-repeaterfirmware: vad det kastar, färdiga inställningar för en vanlig och en hårt belastad repeater, varje filterkommando med sitt standardvärde, och hur du ser vad det kastade.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '2bf23d24'
  seeded: '2026-10-26'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['0625daa2', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', 'ffc3f3a0', '3fa1bb28', '09511608']
---

En repeater (en nod som skickar meddelanden vidare) upprepar allt den hör.
På en livlig mesh ingår skräp i det. En bot postar varje minut. En nod
skickar sin advert, hälsningen som låter andra hitta den, på nytt med några
minuters mellanrum. Meddelanden kommer in som har rest genom halva landet.
Varje upprepning tar sändningstid från alla runt omkring dig. Med paketfiltret
kan din repeater kasta den trafiken i stället för att skicka den vidare.

{{< callout type="warning" >}}
Paketfiltret ingår i **DMC-repeaterfirmware**, repeaterbygget av
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Standard-MeshCore
har inget paketfilter; där finns `region denyf *` och
`set flood.max.unscoped`, på sidan [CLI-kommandon](/guides/cli/). Den här
guiden följer dev-bygget 1.18.0 `ecfb2d4` från 19 oktober 2026. Det stabila
bygget 1.17.1 har bara filtren för hopp, takt, kanal, hash och trasiga paket.
Det saknar också torrkörning.
{{< /callout >}}

## Vad filtret gör {#what}

Filtret tittar bara på paket som din repeater skickar vidare genom flood (till
varje nod inom räckhåll). Det rör aldrig det din repeater själv sänder, eller
paket som följer en känd väg till en nod. Direktmeddelanden och förfrågningar
till och från dina egna kontakter passerar också. Det kan kasta:

- paket som redan har passerat så många repeatrar (hopp) som du tillåter, per
  pakettyp;
- fler paket av en typ än du tillåter per minut;
- en advert från en nod som redan har annonserat under de senaste timmarna;
- meddelanden på en kanal du blockerar;
- allt som kom via en repeater du blockerar;
- gruppmeddelanden från en avsändare eller med ett visst ord, eller bara en
  del av dem;
- gruppmeddelanden som är trasiga, eller äldre än du tillåter.

Filtret är **av** tills du slår på det. Du ställer in det med kommandon. Skriv
dem över USB i [seriekonsolen](/firmware/console/) på den här webbplatsen.
Eller skicka dem från MeshCore-appen, som i
[repeaterguiden](/repeater-guide/#config).

## Hämta firmware {#firmware}

Flasha **DutchMeshCore Repeater** från flashern i
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Observer-firmware
från [MQTT på din observer](/guides/mqtt/) har samma filter.

## Prova först {#dryrun}

I torrkörning räknar filtret varje paket det skulle kasta, men skickar ändå
vidare det. Så dimensionerar du en inställning innan den kastar något:

```text
filter on
filter dryrun on
```

Medan torrkörning är på slutar statusraden i `filter` med `(dry-run)`.
Räknarna visar vad filtret skulle ha kastat. Låt det gå en dag och titta
sedan på dem (se [Vad det kastade](#stats)). När siffrorna ser rätt ut
aktiverar du det på riktigt:

```text
filter dryrun off
```

## Rekommenderade konfigurationer {#configs}

### En vanlig repeater {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Gruppmeddelanden passerar upp till 20 per minut, direktmeddelanden upp till 5
per minut, och trasiga gruppmeddelanden kastas. Firmwarens egen normala
konfiguration tillåter 20 direktmeddelanden per minut. Den här sidan använder
de 5 som den rekommenderar sedan en flood av direktmeddelanden i juli 2026.

### En hårt belastad repeater {#busy}

För en repeater på en hög plats som hör en hel region, eller en som drabbas
av flood:

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

Det halverar gruppmeddelandena och adverts, och släpper igenom varje nods
advert en gång per dygn. Det kastar meddelanden som redan har passerat 16
repeatrar. Efter en omstart får varje nod en advert igenom. Firmwarens egna
dokument sätter också `filter hash 2` här; den här sidan utelämnar det (se
[Varje inställning](#settings) för varför).

### Blockera en stökig kanal {#channel}

```text
filter channel add #bot
```

Din repeater hör fortfarande kanalen. Den skickar den inte längre vidare till
andra repeatrar och companions (noderna som folk skickar meddelanden från).
Upp till 16 kanaler.

### Bromsa en avsändare {#sender}

En bot som postar för ofta på en kanal du vill behålla:

```text
filter watch add #test
filter sender add Bob 60
```

Bobs meddelanden på kanalen Public och `#test` passerar nu en gång per minut;
resten kastas. Filtret matchar namnet i meddelandet, så en avsändare som byter
namn tar sig förbi det.

### Blockera en repeater uppströms {#path}

När skräpet kommer in via en enda repeater blockerar du dess prefix: den
första delen av dess ID, i hexadecimal form (hex).

```text
filter path add a1b2
```

Ett kort prefix som `a1` blockerar också varje annan repeater vars ID börjar
med `a1`. Använd det längsta prefix du kan. Upp till 8 prefix.

## Varje inställning {#settings}

Pakettyper anges med nummer. På repeatern visar `filter types` samma nummer
med firmwarens namn, som `TXT_MSG` och `GRP_TXT`:

| Nummer | Typ | Nummer | Typ |
| --- | --- | --- | --- |
| `00` | förfrågan | `06` | gruppdata |
| `01` | svar | `07` | anonym förfrågan |
| `02` | direktmeddelande | `08` | väg |
| `03` | bekräftelse | `09` | spårning |
| `04` | advert | `10` | flerdelat |
| `05` | gruppmeddelande | `11` | styrning |

| Kommando | Vad det gör | Standardvärde |
| --- | --- | --- |
| `filter on` / `filter off` | Slår på eller av filtret. | av |
| `filter dryrun on` / `off` | Räknar kast men skickar ändå allt vidare. | av |
| `filter hops <type> <max>` | Kastar en typ som redan har passerat så här många repeatrar, 0 till 64. | 32 för gruppmeddelanden, 8 för resten |
| `filter rate <type> <limit> <secs> [soft]` | Släpper igenom högst `limit` av en typ per `secs`. Med `soft` avtar genomsläppet gradvis från `soft` till `limit`. `0` stänger av gränsen. | 20 per 60 s för direkt- och gruppmeddelanden, 10 för adverts, 5 för resten |
| `filter advert <hours>` | Släpper igenom varje nods advert en gång per så här många timmar, upp till 720. | 0 (av) |
| `filter channel add <#name>` | Slutar skicka en kanal vidare. | ingen |
| `filter path add <hex>` | Kastar allt som kom via en repeater med det här prefixet, 2 till 8 hex-siffror. | ingen |
| `filter sender add <name> [secs] [prob]` | Kastar gruppmeddelanden från en avsändare, på Public och bevakade kanaler. `Bot*` matchar varje namn som börjar med Bot. | ingen |
| `filter text add <word> [secs] [prob]` | Kastar gruppmeddelanden som innehåller ett ord, på Public och bevakade kanaler. `^word` matchar bara i början. | ingen |
| `filter watch add <#name>` | Låter avsändar- och textreglerna läsa den här kanalen också, upp till 4. Public läses alltid. | Public |
| `filter malformed on` / `off` | Kastar Public-meddelanden som är tomma, trasiga eller daterade mer än en vecka fel (datumkontrollen väntar tills klockan är ställd). | av |
| `filter age <minutes>` / `off` | Kastar gruppmeddelanden äldre än så här, på Public och bevakade kanaler, 1 till 10080. | av |
| `filter hash <bytes>` | Kastar paket med kortare väg-ID än så här, 1 till 3. | 1 |
| `filter reset` | Återställer varje inställning till standardvärdet. | |

Varje `add` har ett `remove` och ett `list`, till exempel
`filter channel remove #bot`. I avsändar- och textregler låter `secs` ett
meddelande passera per så många sekunder. `prob` tillämpar regeln på bara den
andelen av träffarna, 1 till 100. Upp till 8 avsändarregler och 8 textregler.
Namn och ord är skiftlägeskänsliga; ett namn får vara upp till 15 tecken, ett
ord upp till 23.

Två inställningar kastar mer än du kanske väntar dig:

- `filter hash 2` kastar nästan all trafik. Noder skickar väg-ID på 1 byte som
  standard.
- `filter age` litar på din repeaters klocka. Ställ den med `clock sync` från
  appen, kontrollera den med `clock`, och börja generöst: `filter age 60`.

Varje inställning behålls efter en omstart.

## Vad det kastade {#stats}

`filter` visar totalerna per orsak:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` visar detaljerna för en inställning. Ämnena är
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` och `age`. `filter stats top` visar första byten i nod-ID:na bakom
flest kast, en ledtråd snarare än bevis.
`filter stats air` visar sändningstiden din repeater sparade genom att inte
skicka de här paketen vidare.

Räknarna börjar om från 0 efter en omstart och efter `clear stats`.
