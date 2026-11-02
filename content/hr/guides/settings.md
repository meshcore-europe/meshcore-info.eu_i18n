---
title: Preporučene postavke
layout: settings
lead: Radijski preset koji koristi tvoje područje i postavke koje su tvoji susjedi promijenili. Odaberi državu, postavi preset i kopiraj naredbe.
description: MeshCore radijski preset po području u Europi te postavke repetitora i companiona koje su lokalne grupe promijenile u odnosu na zadane, uz pripadne naredbe.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-11-02'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Svako područje u nastavku koristi vlastiti radijski preset ili mijenja nekoliko
zadanih postavki MeshCorea. Sve što nije navedeno ostaje na zadanoj vrijednosti,
pa mijenjaš samo ono što je promijenilo tvoje područje. Repetitor prosljeđuje
poruke za sve; companion je čvor s kojeg šalješ poruke, uparen s mobitelom ili
laptopom preko Bluetooth veze ili USB-a, ili opremljen vlastitim zaslonom.

U [vodiču za repetitore](/repeater-guide/#config) piše kako doći do naredbenog
retka svojeg repetitora, a naredbe sam upisuješ u
[serijskoj konzoli](/firmware/console/) na ovom webu. Kod svakog područja
njegove postavke možeš poslati i preko USB-a. U vodiču su navedena i
[zakonska ograničenja](/repeater-guide/#legal) na 868 MHz.

## Smanji promet {#traffic}

Ove postavke vrijede za svako područje. Svaki repetitor prosljeđuje svaku flood
poruku koju čuje. Jedna tvoja poruka znači jedno slanje i još po jedno za svaki
repetitor koji je čuje. Uz duty cycle od 10% repetitor može poslati oko 680
paketa na sat, a taj broj dijele svi oko njega. Poruka koja putuje dalje nego
što treba troši dio tog broja.

**Šalji u najmanju regiju kojom dosežeš ljude kojima pišeš.**
Regije su ugniježđene: država, pokrajina, lokalna grupa, svaka sa svojim kodom,
na primjer `nl`, `nl-ov` i `nl-ov-zwo`. Poruka za `nl-ov-zwo` ostaje kod
repetitora u toj grupi. Repetitor prosljeđuje samo regije koje sam ima: ako ima
`nl`, to ne znači da prosljeđuje i `nl-ov`. Svaki repetitor stavi u sve regije
koje poslužuje, i samo u njih; tvoja [lokalna grupa](/community/) zna koje su to.

**Ograniči što prosljeđuje tvoj repetitor.** Dvije postavke zadržavaju u blizini
promet koji ne mora putovati daleko:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: adverti, kojima se čvor najavljuje mreži, putuju
  najviše 3 skoka.
- `flood.max.unscoped 1`: poruka bez regije prolazi kroz najviše jedan repetitor.
