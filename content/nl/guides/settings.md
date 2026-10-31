---
title: Aanbevolen instellingen
layout: settings
lead: De radiopreset in jouw omgeving, en de instellingen die je buren hebben aangepast. Kies je land, stel de preset in en kopieer de commando's.
description: De MeshCore-radiopreset per gebied in Europa, en de instellingen voor repeaters en companions die lokale groepen anders hebben ingesteld dan de standaard, met de commando's.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-10-31'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Elk gebied hieronder heeft een eigen radiopreset, of past een paar standaardwaarden
van MeshCore aan. Alles wat er niet staat, blijft op de standaardwaarde. Je past
dus alleen aan wat jouw gebied heeft aangepast. Een repeater stuurt berichten door
voor iedereen. Een companion is de node waarmee jij berichten verstuurt. Je koppelt
hem via Bluetooth of USB aan je telefoon of laptop, of hij heeft een eigen scherm.

In de [repeatergids](/repeater-guide/#config) lees je hoe je bij de opdrachtregel
van je repeater komt. In de [seriële console](/firmware/console/) op deze site typ
je zelf commando's. Onder elk gebied kun je de instellingen ook via USB versturen.
De gids noemt ook de [wettelijke grenzen](/repeater-guide/#legal) op 868 MHz.

## Houd het verkeer laag {#traffic}

Deze instellingen gelden voor elk gebied. Elke repeater stuurt elk flood-bericht
door dat hij ontvangt. Eén bericht van jou kost één uitzending, plus één voor elke
repeater die het ontvangt. Met de duty cycle van 10% kan een repeater ongeveer 680
pakketten per uur versturen. Iedereen in de buurt deelt dat aantal. Een bericht dat
verder reist dan nodig, verbruikt daar een deel van.

**Stuur naar de kleinste regio waarmee je de mensen bereikt aan wie je schrijft.**
Regio's vallen binnen elkaar: een land, een provincie, een lokale groep, elk met een
eigen code, zoals `nl`, `nl-ov` en `nl-ov-zwo`. Een bericht voor `nl-ov-zwo` blijft
bij de repeaters in die groep. Een repeater stuurt alleen de regio's door die hij
zelf heeft. Heeft hij `nl`, dan stuurt hij `nl-ov` nog niet door. Zet elke repeater
in elke regio die hij bedient, en alleen in die regio's. Je [lokale groep](/community/)
weet welke dat zijn.

**Beperk wat je repeater doorstuurt.** Met twee instellingen houd je verkeer dat
niet ver hoeft te reizen dicht bij huis:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: advertenties, waarmee een node zich bij de mesh meldt,
  reizen hooguit 3 hops.
- `flood.max.unscoped 1`: een bericht zonder regio gaat via hooguit één repeater.
