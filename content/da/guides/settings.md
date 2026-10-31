---
title: Anbefalede indstillinger
layout: settings
lead: Det radio-preset, dit område bruger, og de indstillinger, dine naboer har ændret. Vælg dit land, indstil preset'et, og kopiér kommandoerne.
description: MeshCore-radio-preset'et for hvert område i Europa og de repeater- og companion-indstillinger, lokale grupper har ændret fra standarden, med kommandoerne.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-10-31'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Hvert område nedenfor bruger sit eget radio-preset eller ændrer nogle få af
MeshCores standardindstillinger. Alt, der ikke står her, beholder standarden.
Du ændrer altså kun det, dit område har ændret. En repeater sender beskeder
videre for alle. En companion er den node, du sender beskeder fra. Den er parret
med din telefon eller bærbare over Bluetooth eller USB, eller den har sin egen
skærm.

I [repeater-guiden](/repeater-guide/#config) kan du se, hvordan du får adgang til
din repeaters kommandolinje. I [den serielle konsol](/firmware/console/) her på
siden skriver du selv kommandoerne. Under hvert område kan du også sende dets
indstillinger over USB. Guiden viser også de [lovmæssige grænser](/repeater-guide/#legal)
på 868 MHz.

## Hold trafikken nede {#traffic}

Disse indstillinger gælder for alle områder. Hver repeater sender alle de
flood-beskeder, den hører, videre. Én besked fra dig koster én udsendelse
plus én for hver repeater, der hører den. Med en duty cycle på 10% kan en
repeater sende omkring 680 pakker i timen. Alle omkring den deler det antal.
En besked, der rejser længere end nødvendigt, bruger en del af det.

**Send til den mindste region, der når dem, du skriver til.**
Regioner ligger inden i hinanden: et land, en provins, en lokal gruppe. Hver
har sin egen kode, for eksempel `nl`, `nl-ov` og `nl-ov-zwo`. En besked til
`nl-ov-zwo` bliver hos repeaterne i den gruppe. En repeater sender kun de
regioner videre, den selv har. Har den `nl`, sender den ikke `nl-ov` videre.
Sæt hver repeater i alle de regioner, den dækker, og kun dem. Din
[lokale gruppe](/community/) ved, hvilke det er.

**Begræns, hvad din repeater sender videre.** To indstillinger holder trafik,
der ikke behøver at nå langt, i nærområdet:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: adverts, som annoncerer en node i mesh'et, rejser
  højst 3 hop.
- `flood.max.unscoped 1`: en besked uden region går højst gennem én repeater.
