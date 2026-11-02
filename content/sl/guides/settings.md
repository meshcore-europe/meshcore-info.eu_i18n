---
title: Priporočene nastavitve
layout: settings
lead: Radijska prednastavitev tvojega območja in nastavitve, ki so jih spremenili tvoji sosedje. Izberi državo, nastavi prednastavitev in kopiraj ukaze.
description: Radijska prednastavitev za MeshCore po območjih v Evropi ter nastavitve repetitorjev in companionov, ki so jih lokalne skupine spremenile glede na privzete, skupaj z ukazi.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-11-02'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Vsako območje spodaj uporablja svojo radijsko prednastavitev ali spremeni nekaj
privzetih nastavitev MeshCore. Vse, česar ne navajamo, ostane privzeto, zato
spremeniš samo tisto, kar je spremenilo tvoje območje. Repetitor posreduje sporočila
za vse. Companion je vozlišče, s katerega pošiljaš sporočila: s telefonom ali
prenosnikom ga povežeš prek povezave Bluetooth ali USB, lahko pa ima svoj zaslon.

V [vodniku za repetitorje](/repeater-guide/#config) piše, kako prideš do ukazne
vrstice svojega repetitorja, v [serijsko konzolo](/firmware/console/) na tej strani
pa ukaze vpisuješ sam. Pri vsakem območju lahko njegove nastavitve pošlješ tudi
prek USB. V vodniku najdeš tudi [zakonske omejitve](/repeater-guide/#legal) na
868 MHz.

## Omeji promet {#traffic}

Te nastavitve veljajo za vsa območja. Vsak repetitor posreduje vsako sporočilo
flood, ki ga sliši. Eno tvoje sporočilo pomeni eno oddajo, poleg tega še po eno za
vsak repetitor, ki ga sliši. Pri omejitvi duty cycle 10 % lahko repetitor pošlje
približno 680 paketov na uro, to število pa si delijo vsi okoli njega. Sporočilo,
ki potuje dlje, kot je treba, porabi del teh paketov.

**Pošiljaj v najmanjšo regijo, ki še doseže ljudi, ki jim pišeš.**
Regije so vgnezdene druga v drugo: država, pokrajina, lokalna skupina, vsaka s svojo
kodo, na primer `nl`, `nl-ov` in `nl-ov-zwo`. Sporočilo za `nl-ov-zwo` ostane pri
repetitorjih v tej skupini. Repetitor posreduje samo regije, ki jih ima nastavljene:
če ima `nl`, zato še ne posreduje `nl-ov`. Vsak repetitor dodaj v vse regije, ki
jih pokriva, in samo vanje. Katere so te regije, ve tvoja [lokalna skupina](/community/).

**Omeji, kaj posreduje tvoj repetitor.** Z dvema nastavitvama ostane promet, ki mu
ni treba potovati daleč, blizu doma:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: oglasi, ki vozlišče najavijo omrežju, potujejo največ
  3 skoke.
- `flood.max.unscoped 1`: sporočilo brez regije gre skozi največ en repetitor.
