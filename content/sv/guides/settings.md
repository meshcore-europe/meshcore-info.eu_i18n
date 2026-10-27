---
title: Rekommenderade inställningar
layout: settings
lead: Radioförinställningen som ditt område använder, och inställningarna som dina grannar har ändrat. Välj ditt land, ställ in förinställningen och kopiera kommandona.
description: MeshCores radioförinställning per område i Europa, och de repeater- och companion-inställningar som lokala grupper har ändrat från standardvärdena, med kommandona.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '9547ba62'
  seeded: '2026-10-26'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', '43cde8b4']
---

Varje område nedan använder sin egen radioförinställning, eller ändrar några av MeshCores standardvärden. Allt som inte står med behåller standardvärdet, så du ändrar bara det som ditt område har ändrat. En repeater skickar meddelanden vidare åt alla. En companion är noden du skriver meddelanden från, parkopplad med din telefon eller dator via Bluetooth eller USB, eller med egen skärm.

I [repeaterguiden](/repeater-guide/#config) ser du hur du når din repeaters kommandorad. I [seriekonsolen](/firmware/console/) på den här webbplatsen skriver du kommandon själv. Under varje område kan du också skicka områdets inställningar via USB. Guiden listar även de [lagliga gränserna](/repeater-guide/#legal) på 868 MHz.

## Håll trafiken nere {#traffic}

De här inställningarna gäller för alla områden. Varje repeater skickar vidare varje flood-meddelande den hör. Ett meddelande från dig kostar en sändning, plus en för varje repeater som hör det. Under duty cycle på 10% kan en repeater skicka ungefär 680 paket i timmen, och alla runt omkring delar på det antalet. Ett meddelande som färdas längre än det behöver förbrukar en del av det.

**Skicka till den minsta region som når dem du skriver till.** Regioner ligger i varandra: ett land, ett län, en lokal grupp, var och en med egen kod, till exempel `nl`, `nl-ov` och `nl-ov-zwo`. Ett meddelande till `nl-ov-zwo` stannar hos repeatrarna i den gruppen. Lägg varje repeater bara i de regioner den betjänar. Din [lokala grupp](/community/) vet vilka det är.

**Begränsa vad din repeater skickar vidare.** Två inställningar håller trafik som inte behöver färdas långt nära hemmet:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: adverts, som annonserar en nod för meshen, färdas högst 3 hopp.
- `flood.max.unscoped 1`: ett meddelande utan region passerar högst en repeater.
