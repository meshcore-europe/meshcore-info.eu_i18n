---
title: Doporučená nastavení
layout: settings
lead: Rádiový preset, který se používá ve tvé oblasti, a nastavení, která tvoji sousedé změnili. Vyber si zemi, nastav preset a zkopíruj příkazy.
description: Rádiový preset MeshCore pro jednotlivé oblasti v Evropě a nastavení repeaterů a companionů, která místní skupiny změnily oproti výchozím hodnotám, včetně příkazů.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '9547ba62'
  seeded: '2026-10-26'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', '43cde8b4']
---

Každá oblast níže používá vlastní rádiový preset nebo mění několik výchozích hodnot MeshCore. Vše, co tu není uvedeno, zůstává ve výchozím nastavení, takže měníš jen to, co změnila tvoje oblast. Repeater předává zprávy dál pro všechny. Companion je uzel, ze kterého píšeš zprávy: je spárovaný s tvým telefonem nebo notebookem přes Bluetooth nebo USB, nebo má vlastní displej.

V [průvodci repeaterem](/repeater-guide/#config) najdeš, jak se dostat na příkazový řádek svého repeateru. Příkazy pak sám zadáváš v [sériové konzoli](/firmware/console/) na tomto webu. U každé oblasti můžeš její nastavení také poslat přes USB. Průvodce uvádí i [zákonné limity](/repeater-guide/#legal) na 868 MHz.

## Omez provoz {#traffic}

Tato nastavení platí pro všechny oblasti. Každý repeater předá dál každou flood zprávu, kterou zachytí. Jedna tvoje zpráva stojí jedno vysílání, plus jedno za každý repeater, který ji zachytí. Při 10% duty cycle může repeater odeslat zhruba 680 paketů za hodinu a o tento počet se dělí všichni kolem něj. Zpráva, která cestuje dál, než musí, část z něj spotřebuje.

**Posílej do nejmenšího regionu, který dosáhne k lidem, kterým píšeš.** Regiony se vnořují: země, provincie, místní skupina, každý má vlastní kód, například `nl`, `nl-ov` a `nl-ov-zwo`. Zpráva pro `nl-ov-zwo` zůstane u repeaterů v této skupině. Zařaď každý repeater jen do regionů, které obsluhuje. Tvoje [místní skupina](/community/) ví, které to jsou.

**Omez, co tvůj repeater předává dál.** Dvě nastavení udrží provoz, který nemusí cestovat daleko, blízko domova:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: adverty, které oznamují uzel do meshe, urazí nejvýše 3 skoky.
- `flood.max.unscoped 1`: zpráva bez regionu projde nejvýše jedním repeaterem.
