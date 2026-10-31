---
title: Rekommenderade inställningar
layout: settings
lead: Radioförinställningen i ditt område och inställningarna som dina grannar har ändrat. Välj ditt land, ställ in förinställningen och kopiera kommandona.
description: MeshCores radioförinställning per område i Europa, och de repeater- och companion-inställningar som lokala grupper har ändrat från standardvärdena, med kommandona.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-10-31'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Varje område nedan använder en egen radioförinställning eller ändrar några av
MeshCores standardvärden. Allt som inte står med behåller standardvärdet. Du
ändrar alltså bara det som ditt område har ändrat. En repeater skickar vidare
meddelanden åt alla. En companion är noden du skickar meddelanden från. Du
parkopplar den med din telefon eller dator via Bluetooth eller USB, eller så
har den en egen skärm.

I [repeater-guiden](/repeater-guide/#config) ser du hur du når din repeaters
kommandorad. I [seriekonsolen](/firmware/console/) här på sajten skriver du
själv in kommandon. Under varje område kan du också skicka dess inställningar
via USB. Där står också de [lagliga gränserna](/repeater-guide/#legal) för
868 MHz.

## Håll nere trafiken {#traffic}

De här inställningarna gäller för alla områden. Varje repeater skickar vidare
alla flood-meddelanden den hör. Ett meddelande från dig kostar en sändning,
plus en för varje repeater som hör det. Med en arbetscykel på 10 % kan en
repeater sända ungefär 680 paket i timmen. Alla runt omkring den delar på det
antalet. Ett meddelande som går längre än det behöver förbrukar en del av dem.

**Skicka till den minsta region som når dem du skriver till.** Regioner ligger
inuti varandra: ett land, en provins, en lokal grupp, var och en med en egen kod,
till exempel `nl`, `nl-ov` och `nl-ov-zwo`. Ett meddelande till `nl-ov-zwo`
stannar hos repeatrarna i den gruppen. En repeater skickar bara vidare de
regioner den själv har. En repeater med `nl` skickar alltså inte vidare
`nl-ov`. Lägg varje repeater i alla regioner den täcker, och bara i dem. Din
[lokala grupp](/community/) vet vilka det är.

**Begränsa vad din repeater skickar vidare.** Med två inställningar håller du
trafik som inte behöver gå långt kvar i närheten:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: adverts, som presenterar en nod för mesh-nätet, går
  högst 3 hopp.
- `flood.max.unscoped 1`: ett meddelande utan region går genom högst en
  repeater.
