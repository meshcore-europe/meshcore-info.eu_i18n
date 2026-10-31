---
title: Doporučená nastavení
layout: settings
lead: Rádiový preset tvé oblasti a nastavení, která změnili tví sousedé. Vyber zemi, nastav preset a zkopíruj příkazy.
description: Rádiový preset MeshCore pro každou oblast v Evropě a nastavení repeateru a companionu, která místní skupiny změnily oproti výchozím hodnotám, včetně příkazů.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-10-31'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Každá oblast níže používá vlastní rádiový preset, nebo mění několik
výchozích hodnot MeshCore. Vše, co tu není uvedené, zůstává ve výchozím
stavu. Měníš tedy jen to, co změnila tvoje oblast. Repeater předává zprávy
dál pro všechny. Companion je uzel, ze kterého píšeš zprávy. Spáruješ ho
s telefonem nebo notebookem přes Bluetooth nebo USB, případně má vlastní displej.

V [průvodci repeaterem](/repeater-guide/#config) zjistíš, jak se dostaneš
k příkazové řádce svého repeateru. Příkazy sám zadáváš v [sériové
konzoli](/firmware/console/) na tomto webu. U každé oblasti můžeš její
nastavení odeslat také přes USB. Průvodce uvádí i [zákonné limity](/repeater-guide/#legal)
pro pásmo 868 MHz.

## Omez provoz {#traffic}

Tato nastavení platí pro všechny oblasti. Každý repeater předá dál každou
flood zprávu, kterou zachytí. Jedna tvoje zpráva stojí jedno vysílání a k tomu
jedno za každý repeater, který ji zachytí. Při střídě 10 % může repeater
odeslat asi 680 paketů za hodinu. O tento počet se dělí všichni v jeho okolí.
Zpráva, která doletí dál, než potřebuje, z něj část spotřebuje.

**Posílej do nejmenšího regionu, který pokryje lidi, kterým píšeš.**
Regiony jsou do sebe vnořené: země, kraj, místní skupina. Každý má vlastní
kód, například `nl`, `nl-ov` a `nl-ov-zwo`. Zpráva pro `nl-ov-zwo` zůstane
u repeaterů v této skupině. Repeater předává dál jen regiony, které má sám
nastavené. Když má `nl`, neznamená to, že předá dál `nl-ov`. Zařaď každý
repeater do všech regionů, které obsluhuje, a jen do nich. Které to jsou,
ti řekne tvoje [místní skupina](/community/).

**Omez, co tvůj repeater předává dál.** Dvě nastavení udrží v blízkém okolí
provoz, který nemusí cestovat daleko:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: adverty, které ohlašují uzel v mesh síti, urazí
  nejvýše 3 skoky.
- `flood.max.unscoped 1`: zpráva bez regionu projde nejvýše jedním
  repeaterem.
