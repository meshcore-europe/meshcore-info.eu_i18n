---
title: Paketfilter
lead: 'Hindra din repeater från att skicka vidare skräp: flood från långt bort, en bot som aldrig slutar, en bullrig kanal. Testa en inställning först och slå sedan på den.'
description: 'Paketfiltret i DMC:s repeater-firmware: vad det slänger, färdiga inställningar för en vanlig och en hårt belastad repeater, alla filterkommandon med standardvärden och hur du ser vad det har slängt.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-10-31'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

En repeater (en nod som skickar meddelanden vidare) upprepar allt den hör.
På ett livligt mesh blir det också skräp. En bot skriver varje minut. En nod
skickar sin advert, hälsningen som låter andra hitta den, om och om igen med
några minuters mellanrum. Det kommer meddelanden som har färdats genom halva
landet. Varje upprepning tar sändningstid från alla runt omkring dig. Med
paketfiltret kan din repeater slänga den trafiken i stället för att skicka den
vidare. Läs [Gör meshet tåligt](/guides/resilient/) för att först ta reda på
vad som översvämmar ditt mesh, och vad som hjälper utöver filtret.

{{< callout type="warning" >}}
Paketfiltret ingår i **DMC:s repeater-firmware**, repeaterbygget av
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Vanliga
MeshCore har inget paketfilter. Där finns `region denyf *` och
`set flood.max.unscoped`, som du hittar på sidan
[CLI-kommandon](/guides/cli/). Den här guiden utgår från dev-bygget 1.18.0
`ecfb2d4` från 19 oktober 2026. Det stabila bygget 1.17.1 har bara filtren
för hopp, takt, kanal, hash och trasiga paket. Det saknar också dry-run.
{{< /callout >}}

## Vad filtret gör {#what}

Filtret granskar bara paket som din repeater skickar vidare med flood (till
alla noder inom räckhåll). Det rör aldrig det som din repeater själv skickar.
Det rör inte heller paket som följer en känd väg till en enda nod.
Direktmeddelanden och förfrågningar till och från dina egna kontakter går
också igenom. Filtret kan slänga:

- paket som redan har passerat så många repeatrar (hopp) som du tillåter, per
  pakettyp;
- fler paket av en typ per minut än du tillåter;
- en advert från en nod som redan har skickat en advert de senaste timmarna;
- meddelanden på en kanal som du blockerar;
- allt som har kommit via en repeater som du blockerar;
- gruppmeddelanden från en viss avsändare eller med ett visst ord, eller bara
  en del av dem;
- gruppmeddelanden som är trasiga eller äldre än du tillåter.

Filtret är **avstängt** tills du slår på det. Du ställer in det med kommandon.
Skriv dem via USB i [seriekonsolen](/firmware/console/) här på sajten. Du kan
också skicka dem från MeshCore-appen, som i
[repeaterguiden](/repeater-guide/#config).

## Skaffa firmware {#firmware}

Flasha **DutchMeshCore Repeater** med flashverktyget i
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Observer-firmwaren
från [MQTT på din observer](/guides/mqtt/) har samma filter.

## Testa först {#dryrun}

I dry-run räknar filtret varje paket som det skulle ha slängt, men skickar
ändå det vidare. På så sätt provar du ut en inställning innan något slängs:

```text
filter on
filter dryrun on
```

Medan dry-run är på slutar statusraden för `filter` med `(dry-run)`. Siffrorna
visar vad filtret skulle ha slängt. Låt det gå i ett dygn och titta sedan på
dem (se [Vad filtret slängde](#stats)). När siffrorna ser rimliga ut slår du
på filtret på riktigt:

```text
filter dryrun off
```

## Rekommenderade inställningar {#configs}

### En vanlig repeater {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Upp till 20 gruppmeddelanden i minuten går igenom, och upp till 5
direktmeddelanden i minuten. Trasiga gruppmeddelanden slängs. Firmwarens egen
standardinställning tillåter 20 direktmeddelanden i minuten. Den här sidan
följer i stället rådet om 5, efter en flood av direktmeddelanden i juli 2026.

### En hårt belastad repeater {#busy}

För en repeater på en hög plats som hör en hel region, eller en som
översvämmas:

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

Det här halverar gruppmeddelandena och adverts. Varje nods advert går igenom
en gång per dygn. Meddelanden som redan har passerat 16 repeatrar slängs.
Efter en omstart får varje nod igenom en advert. Firmwarens egen dokumentation
sätter också `filter hash 2` här. Den här sidan utelämnar det (se
[Alla inställningar](#settings) för varför).

### Blockera en bullrig kanal {#channel}

```text
filter channel add #bot
```

Din repeater hör fortfarande kanalen. Den skickar inte längre kanalen vidare
till andra repeatrar och companions (noderna som folk skickar meddelanden
från). Du kan blockera upp till 16 kanaler.

### Bromsa en avsändare {#sender}

En bot som skriver för ofta på en kanal som du vill behålla:

```text
filter watch add #test
filter sender add Bob 60
```

Nu går Bobs meddelanden på Public-kanalen och `#test` igenom en gång i
minuten. Resten slängs. Filtret jämför namnet i meddelandet, så en avsändare
som byter namn kommer förbi.

### Blockera en repeater uppströms {#path}

När skräpet kommer in via en viss repeater blockerar du dess prefix: den första
delen av dess ID, i hexadecimal form (hex). Det kräver dev-bygget 1.18.
Version 1.17.1 har inget vägfilter.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` visar prefixen du blockerar. `filter stats path` visar hur
mycket varje prefix har slängt. Med `filter path remove a1b2` släpper du
igenom repeatern igen. Ett kort prefix som `a1` blockerar också alla andra
repeatrar vars ID börjar med `a1`. Använd så långt prefix som möjligt. Du kan
blockera upp till 8 prefix.

## Alla inställningar {#settings}

Pakettyper anges med nummer. På repeatern visar `filter types` samma nummer
med firmwarens namn, till exempel `TXT_MSG` och `GRP_TXT`:

| Nummer | Typ | Nummer | Typ |
| --- | --- | --- | --- |
| `00` | förfrågan | `06` | gruppdata |
| `01` | svar | `07` | anonym förfrågan |
| `02` | direktmeddelande | `08` | väg |
| `03` | kvittens | `09` | spårning |
| `04` | advert | `10` | flerdelat |
| `05` | gruppmeddelande | `11` | styrning |

| Kommando | Vad det gör | Startvärde |
| --- | --- | --- |
| `filter on` / `filter off` | Slår på eller stänger av filtret. | av |
| `filter dryrun on` / `off` | Räknar det som skulle slängas men skickar ändå allt vidare. | av |
| `filter hops <type> <max>` | Slänger en typ som redan har passerat så här många repeatrar, 0 till 64. | 32 för gruppmeddelanden, 8 för resten |
| `filter rate <type> <limit> <secs> [soft]` | Släpper igenom högst `limit` av en typ per `secs`. Med `soft` minskar genomsläppet gradvis från `soft` till `limit`. `0` stänger av gränsen. | 20 per 60 s för direkt- och gruppmeddelanden, 10 för adverts, 5 för resten |
| `filter advert <hours>` | Släpper igenom varje nods advert en gång per så här många timmar, upp till 720. | 0 (av) |
| `filter channel add <#name>` | Slutar skicka vidare en kanal. | ingen |
| `filter path add <hex>` | Slänger allt som har kommit via en repeater med det här prefixet, 2 till 8 hexsiffror. | ingen |
| `filter sender add <name> [secs] [prob]` | Slänger gruppmeddelanden från en avsändare, på Public och bevakade kanaler. `Bot*` matchar alla namn som börjar med Bot. | ingen |
| `filter text add <word> [secs] [prob]` | Slänger gruppmeddelanden som innehåller ett ord, på Public och bevakade kanaler. `^word` matchar bara i början. | ingen |
| `filter watch add <#name>` | Låter reglerna för avsändare och text läsa även den här kanalen, upp till 4. Public läses alltid. | Public |
| `filter malformed on` / `off` | Slänger Public-meddelanden som är tomma, trasiga eller har ett datum som avviker mer än en vecka (datumkontrollen väntar tills klockan är ställd). | av |
| `filter age <minutes>` / `off` | Slänger gruppmeddelanden som är äldre än så här, på Public och bevakade kanaler, 1 till 10080. | av |
| `filter hash <bytes>` | Slänger paket med ett kortare väg-ID än så här, 1 till 3. | 1 |
| `filter reset` | Återställer alla inställningar till standard. | |

Varje `add` har en `remove` och en `list`, till exempel
`filter channel remove #bot`. I regler för avsändare och text släpper `secs`
igenom ett meddelande per så många sekunder. `prob` tillämpar regeln på bara
den andelen av träffarna, 1 till 100. Du kan ha upp till 8 avsändarregler och
8 textregler. Namn och ord är skiftlägeskänsliga. Ett namn får vara upp till
15 tecken och ett ord upp till 23.

Två inställningar slänger mer än du kanske väntar dig:

- `filter hash 2` slänger nästan all trafik. Noder skickar väg-ID på 1 byte
  som standard.
- `filter age` litar på din repeaters klocka. Ställ den med `clock sync` från
  appen, kontrollera den med `clock` och börja generöst: `filter age 60`.

Alla inställningar sparas vid omstart.

## Vad filtret slängde {#stats}

`filter` visar summorna per orsak:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` visar detaljerna för en inställning. Ämnena är
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` och `age`. `filter stats top` visar första byten i nod-ID:na bakom
flest slängda paket. Många noder delar den byten.
`filter stats air` visar hur mycket sändningstid din repeater har sparat genom
att inte skicka de här paketen vidare.

Räknarna börjar om från 0 efter en omstart och efter `clear stats`.
