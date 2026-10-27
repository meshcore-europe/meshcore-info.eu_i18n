---
title: Aanbevolen instellingen
layout: settings
lead: De radiopreset die jouw gebied gebruikt, en de instellingen die je buren hebben aangepast. Kies je land, stel de preset in en kopieer de commando's.
description: De MeshCore-radiopreset per gebied in Europa, en de repeater- en companion-instellingen die lokale groepen hebben aangepast ten opzichte van de standaardwaarden, met de commando's.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '9547ba62'
  seeded: '2026-10-26'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', '43cde8b4']
---

Elk gebied hieronder gebruikt zijn eigen radiopreset, of past een paar
standaardwaarden van MeshCore aan. Alles wat niet genoemd wordt, blijft op de
standaardwaarde staan. Je past dus alleen aan wat jouw gebied heeft aangepast.
Een repeater geeft berichten door voor iedereen. Een companion is de node
waarmee je zelf berichten stuurt, gekoppeld aan je telefoon of laptop via
Bluetooth of USB, of met een eigen scherm.

In de [repeatergids](/repeater-guide/#config) lees je hoe je bij de
opdrachtregel van je repeater komt. Op de [seriële console](/firmware/console/)
op deze site typ je zelf commando's in. Onder elk gebied kun je de instellingen
ervan ook via USB versturen. De gids noemt ook de
[wettelijke grenzen](/repeater-guide/#legal) op 868 MHz.

## Houd het verkeer beperkt {#traffic}

Deze instellingen gelden voor elk gebied. Elke repeater geeft elk flood-bericht
door dat hij hoort. Eén bericht van jou kost één zending, plus één voor elke
repeater die het hoort. Binnen de duty cycle van 10% kan een repeater ongeveer
680 pakketten per uur versturen, en iedereen in de buurt deelt dat aantal. Een
bericht dat verder reist dan nodig, gebruikt daar een deel van op.

**Stuur naar de kleinste regio die de mensen bereikt aan wie je schrijft.**
Regio's liggen in elkaar: een land, een provincie, een lokale groep, elk met een
eigen code, zoals `nl`, `nl-ov` en `nl-ov-zwo`. Een bericht voor `nl-ov-zwo`
blijft bij de repeaters in die groep. Zet elke repeater alleen in de regio's die
hij bedient. Je [lokale groep](/community/) weet welke dat zijn.

**Beperk wat je repeater doorgeeft.** Twee instellingen houden verkeer dat
niet ver hoeft te reizen dicht bij huis:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: advertenties, die een node aan de mesh bekendmaken,
  reizen hoogstens 3 hops.
- `flood.max.unscoped 1`: een bericht zonder regio gaat door hoogstens één
  repeater.
