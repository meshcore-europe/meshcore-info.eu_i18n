---
title: Anbefalede indstillinger
layout: settings
lead: Den radio-preset dit område bruger, og de indstillinger dine naboer har ændret. Vælg dit land, sæt presettet og kopier kommandoerne.
description: MeshCores radio-preset per område i Europa, og de repeater- og companion-indstillinger lokale grupper har ændret fra standardværdierne, med kommandoerne.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '9547ba62'
  seeded: '2026-10-26'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', '43cde8b4']
---

Hvert område herunder bruger sin egen radio-preset eller ændrer nogle få af MeshCores standardværdier. Alt det, der ikke står på listen, bliver ved standardværdien. Du ændrer altså kun det, dit område har ændret. En repeater sender beskeder videre for alle. En companion er den node, du skriver beskeder fra. Den er parret med din telefon eller bærbare over Bluetooth eller USB, eller den har sin egen skærm.

I [repeater-guiden](/repeater-guide/#config) kan du se, hvordan du kommer ind på din repeaters kommandolinje. I [seriekonsollen](/firmware/console/) her på siden skriver du selv kommandoerne. Under hvert område kan du også sende dets indstillinger over USB. Guiden beskriver også de [lovlige grænser](/repeater-guide/#legal) på 868 MHz.

## Hold trafikken nede {#traffic}

De her indstillinger gælder for alle områder. Hver repeater sender alle de flood-beskeder videre, den hører. En besked fra dig koster én udsendelse, plus én for hver repeater, der hører den. Med en duty cycle på 10% kan en repeater sende omkring 680 pakker i timen, og alle omkring den deler det antal. En besked, der rejser længere end nødvendigt, bruger af det.

**Send til den mindste region, der når de folk, du skriver til.**
Regioner ligger inden i hinanden: et land, en provins, en lokal gruppe, hver med sin egen kode, for eksempel `nl`, `nl-ov` og `nl-ov-zwo`. En besked til `nl-ov-zwo` bliver hos repeaterne i den gruppe. Sæt kun hver repeater i de regioner, den betjener. Din [lokale gruppe](/community/) ved, hvilke det er.

**Begræns det, din repeater sender videre.** To indstillinger holder trafik, der ikke behøver at rejse langt, tæt på hjemme:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: adverts, som gør en node kendt for meshet, rejser højst 3 hop.
- `flood.max.unscoped 1`: en besked uden region passerer højst gennem én repeater.
