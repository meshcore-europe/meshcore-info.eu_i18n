---
title: Preporučena podešavanja
layout: settings
lead: Radio preset koji koristi tvoja oblast i podešavanja koja su promenili tvoji susedi. Izaberi svoju zemlju, podesi preset i kopiraj komande.
description: MeshCore radio preset po oblastima u Evropi i podešavanja repetitora i companion uređaja koja su lokalne grupe promenile u odnosu na podrazumevana, sa komandama.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-11-02'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Svaka oblast u nastavku koristi sopstveni radio preset ili menja nekoliko
podrazumevanih MeshCore podešavanja. Sve što nije navedeno ostaje podrazumevano,
pa menjaš samo ono što je tvoja oblast promenila. Repetitor prosleđuje poruke
za sve. Companion je čvor sa kog šalješ poruke, a povezuješ ga sa telefonom ili
laptopom preko Bluetooth ili USB veze, ili koristiš njegov ekran.

U [vodiču za repetitore](/repeater-guide/#config) piše kako da dođeš do komandne
linije svog repetitora, a komande sam kucaš u [serijskoj konzoli](/firmware/console/)
na ovom sajtu. Ispod svake oblasti možeš i da pošalješ njena podešavanja preko
USB veze. U vodiču su navedena i [zakonska ograničenja](/repeater-guide/#legal)
na 868 MHz.

## Smanji saobraćaj {#traffic}

Ova podešavanja važe za svaku oblast. Svaki repetitor prosleđuje svaku flood
poruku koju čuje. Jedna tvoja poruka znači jedno slanje, plus po jedno za svaki
repetitor koji je čuje. Uz radni ciklus od 10% repetitor može da pošalje oko
680 paketa na sat, a taj broj dele svi oko njega. Poruka koja putuje dalje nego
što treba troši deo tih paketa.

**Šalji u najmanji region preko kog stižeš do ljudi kojima pišeš.**
Regioni su ugnežđeni: zemlja, pokrajina i lokalna grupa, svaka sa svojim kodom,
na primer `nl`, `nl-ov` i `nl-ov-zwo`. Poruka za `nl-ov-zwo` ostaje kod
repetitora u toj grupi. Repetitor prosleđuje samo regione koje sam ima:
ako ima `nl`, to ne znači da prosleđuje i `nl-ov`. Stavi svaki repetitor u sve
regione koje opslužuje, i samo u njih. Tvoja [lokalna grupa](/community/) zna
koji su to regioni.

**Ograniči šta tvoj repetitor prosleđuje.** Dva podešavanja zadržavaju u
blizini saobraćaj kome nije potrebno da putuje daleko:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: adverti, kojima se čvor najavljuje mreži, putuju
  najviše 3 skoka.
- `flood.max.unscoped 1`: poruka bez regiona prolazi kroz najviše jedan
  repetitor.
