---
title: Anbefalte innstillinger
layout: settings
lead: Radiopresetet området ditt bruker, og innstillingene naboene dine har endret. Velg land, still inn presetet og kopier kommandoene.
description: MeshCore-radiopresetet for hvert område i Europa, og repeater- og companion-innstillingene lokale grupper har endret fra standardverdiene, med kommandoene.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-10-31'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Hvert område nedenfor bruker sitt eget radiopreset, eller endrer noen av
MeshCores standardverdier. Alt som ikke står oppført, beholder standardverdien.
Du endrer altså bare det området ditt har endret. En repeater sender meldinger
videre for alle. En companion er noden du sender meldinger fra. Den er paret med
telefonen eller den bærbare PC-en din via Bluetooth eller USB, eller har sin
egen skjerm.

I [repeater-guiden](/repeater-guide/#config) ser du hvordan du kommer til
kommandolinjen på repeateren din. I [seriekonsollen](/firmware/console/) her på
nettstedet skriver du kommandoene selv. Under hvert område kan du også sende
innstillingene over USB. Repeater-guiden viser også de [lovlige grensene](/repeater-guide/#legal)
på 868 MHz.

## Hold trafikken nede {#traffic}

Disse innstillingene gjelder for alle områder. Hver repeater sender videre alle
flood-meldinger den hører. Én melding fra deg koster én sending, pluss én for
hver repeater som hører den. Med en duty cycle på 10% kan en repeater sende
rundt 680 pakker i timen. Alle rundt den deler på dette tallet. En melding som
går lenger enn nødvendig, bruker opp noe av det.

**Send til den minste regionen som når dem du skriver til.**
Regioner ligger inni hverandre: et land, et fylke, en lokal gruppe. Hver har sin
egen kode, for eksempel `nl`, `nl-ov` og `nl-ov-zwo`. En melding til `nl-ov-zwo`
blir værende hos repeaterne i den gruppen. En repeater sender bare videre de
regionene den selv har: har den `nl`, sender den ikke videre `nl-ov`. Legg hver
repeater i alle regionene den betjener, og bare i dem. Den [lokale gruppen din](/community/)
vet hvilke det er.

**Begrens hva repeateren din sender videre.** To innstillinger sørger for at
trafikk som ikke trenger å gå langt, holder seg i nærområdet:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: adverts, som gjør en node kjent i meshet, går
  maksimalt 3 hopp.
- `flood.max.unscoped 1`: en melding uten region går gjennom maksimalt én
  repeater.
