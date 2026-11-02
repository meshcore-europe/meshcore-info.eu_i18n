---
title: Odporúčané nastavenia
layout: settings
lead: Rádiová predvoľba tvojej oblasti a nastavenia, ktoré zmenili tvoji susedia. Vyber si krajinu, nastav predvoľbu a skopíruj príkazy.
description: Rádiová predvoľba MeshCore pre jednotlivé oblasti Európy a nastavenia repeatera a companionu, ktoré miestne skupiny zmenili oproti predvoleným hodnotám, aj s príkazmi.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-11-02'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Každá oblasť nižšie používa vlastnú rádiovú predvoľbu alebo mení niekoľko predvolených hodnôt MeshCore. Všetko, čo tu nie je uvedené, ostáva na predvolenej hodnote, takže meníš len to, čo zmenila tvoja oblasť. Repeater preposiela správy pre všetkých. Companion je uzol, z ktorého píšeš správy. Spáruješ ho s telefónom alebo notebookom cez Bluetooth alebo USB, prípadne má vlastnú obrazovku.

V [sprievodcovi repeaterom](/repeater-guide/#config) nájdeš postup, ako sa dostať do príkazového riadka svojho repeatera. V [sériovej konzole](/firmware/console/) na tomto webe zadávaš príkazy sám. Pri každej oblasti môžeš jej nastavenia poslať aj cez USB. Sprievodca uvádza aj [zákonné limity](/repeater-guide/#legal) pre 868 MHz.

## Obmedzuj prevádzku {#traffic}

Tieto nastavenia platia pre každú oblasť. Každý repeater preposiela každú flood správu, ktorú zachytí. Jedna tvoja správa znamená jedno vysielanie a k tomu jedno ďalšie za každý repeater, ktorý ju zachytí. Pri limite duty cycle 10 % môže repeater odoslať približne 680 paketov za hodinu. O tento počet sa delia všetci v jeho okolí. Správa, ktorá putuje ďalej, než musí, z neho časť spotrebuje.

**Posielaj správy do najmenšieho regiónu, v ktorom zastihneš ľudí, ktorým píšeš.**
Regióny sú vnorené do seba: krajina, provincia, miestna skupina, každý s vlastným kódom, napríklad `nl`, `nl-ov` a `nl-ov-zwo`. Správa pre `nl-ov-zwo` ostane medzi repeatermi tejto skupiny. Repeater preposiela len regióny, ktoré má sám nastavené: ak má `nl`, ešte to neznamená, že bude preposielať aj `nl-ov`. Zaraď každý repeater do všetkých regiónov, ktoré obsluhuje, a len do nich. Tvoja [miestna skupina](/community/) vie, ktoré to sú.

**Obmedz, čo tvoj repeater preposiela.** Prevádzku, ktorá nemusí putovať ďaleko, udržíš nablízku pomocou dvoch nastavení:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: adverty, ktoré ohlasujú uzol v sieti, urobia najviac 3 skoky.
- `flood.max.unscoped 1`: správa bez regiónu prejde cez najviac jeden repeater.
