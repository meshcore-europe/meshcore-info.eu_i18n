---
title: Anbefalte innstillinger
layout: settings
lead: Radioforvalget området ditt bruker, og innstillingene naboene dine har endret. Velg landet ditt, sett forvalget og kopier kommandoene.
description: MeshCore-radioforvalget per område i Europa, og repeater- og companion-innstillingene lokale grupper har endret fra standardverdiene, med kommandoene.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '9547ba62'
  seeded: '2026-10-26'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', '43cde8b4']
---

Hvert område nedenfor bruker sitt eget radioforvalg, eller endrer noen få av
standardverdiene i MeshCore. Alt som ikke står oppført, beholder standardverdien,
så du endrer bare det området ditt har endret. En repeater sender meldinger
videre for alle. En companion er noden du sender meldinger fra, paret med
telefonen eller laptopen din over Bluetooth eller USB, eller med egen skjerm.

[Repeater-veiledningen](/repeater-guide/#config) viser hvordan du kommer til
kommandolinjen på repeateren din, og i [seriekonsollen](/firmware/console/) på
dette nettstedet skriver du kommandoer selv. Under hvert område kan du også
sende innstillingene over USB. Veiledningen lister også opp de
[juridiske grensene](/repeater-guide/#legal) på 868 MHz.

## Hold trafikken nede {#traffic}

Disse innstillingene gjelder for alle områder. Hver repeater sender videre alle
flood-meldinger den hører. Én melding fra deg koster én sending, pluss én for
hver repeater som hører den. Under 10 % duty cycle kan en repeater sende
omtrent 680 pakker i timen, og alle rundt den deler på det tallet. En melding
som går lenger enn den trenger, bruker opp noe av det.

**Send til den minste regionen som når dem du skriver til.**
Regioner ligger inni hverandre: et land, en provins, en lokal gruppe, hver med
sin egen kode, som `nl`, `nl-ov` og `nl-ov-zwo`. En melding til `nl-ov-zwo`
holder seg hos repeaterne i den gruppen. Legg hver repeater bare i regionene
den betjener. [Den lokale gruppen din](/community/) vet hvilke det er.

**Begrens hva repeateren din sender videre.** To innstillinger holder trafikk
som ikke trenger å gå langt, nær hjemme:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: adverts, som annonserer en node til meshen, går
  høyst 3 hopp.
- `flood.max.unscoped 1`: en melding uten region går gjennom høyst én
  repeater.
