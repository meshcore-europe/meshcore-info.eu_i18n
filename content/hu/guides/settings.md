---
title: Ajánlott beállítások
layout: settings
lead: A területeden használt rádiós preset, és a beállítások, amelyeket a szomszédaid módosítottak. Válaszd ki az országodat, állítsd be a presetet, és másold ki a parancsokat.
description: A MeshCore rádiós presetje Európa egyes területein, valamint az átjátszó- és companion-beállítások, amelyeket a helyi csoportok az alapértéktől eltérően állítottak be, a parancsokkal együtt.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-10-31'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Az alábbi területek mindegyike saját rádiós presetet használ, vagy a MeshCore
néhány alapértékét módosítja. Ami nem szerepel a listában, az marad
alapértéken, így csak azt kell átállítanod, amit a területed is átállított.
Az átjátszó mindenki üzeneteit továbbítja. A companion az a csomópont,
amelyről te üzensz: Bluetooth-on vagy USB-n párosítod a telefonoddal vagy a
laptopoddal, vagy saját kijelzője van.

Az [átjátszó-útmutatóból](/repeater-guide/#config) megtudod, hogyan éred el
az átjátszód parancssorát. Az oldal [soros konzolján](/firmware/console/)
magad írhatod be a parancsokat. Minden terület alatt USB-n is elküldheted az
adott terület beállításait. Az útmutató a 868 MHz-es sáv
[jogi korlátait](/repeater-guide/#legal) is felsorolja.

## Tartsd alacsonyan a forgalmat {#traffic}

Ezek a beállítások minden területre érvényesek. Az átjátszó minden flood
üzenetet továbbít, amelyet hall. Egy üzeneted egy adásba kerül, plusz egy
adásba minden átjátszónál, amely hallja. A 10%-os kitöltési tényező mellett
egy átjátszó óránként körülbelül 680 csomagot küldhet, és ezen a számon a
környéken mindenki osztozik. Ha egy üzenet messzebbre jut a szükségesnél,
ebből a keretből fogyaszt.

**Arra a legkisebb régióra küldj, amely még eléri a címzettjeidet.**
A régiók egymásba ágyazódnak: ország, megye, helyi csoport, mindegyik saját
kóddal, például `nl`, `nl-ov` és `nl-ov-zwo`. Az `nl-ov-zwo` régiónak szóló
üzenet az adott csoport átjátszóinál marad. Az átjátszó csak azokat a
régiókat továbbítja, amelyekhez maga is tartozik: ha az `nl` régióban van,
attól még nem továbbítja az `nl-ov` régiót. Minden átjátszót vegyél fel az
összes régióba, amelyet kiszolgál, de csak azokba. A
[helyi csoportod](/community/) tudja, melyek ezek.

**Korlátozd, mit továbbít az átjátszód.** Két beállítással a közelben
tarthatod azt a forgalmat, amelynek nem kell messzire jutnia:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: az advertek, amelyekkel egy csomópont bejelenti
  magát a mesh hálózatnak, legfeljebb 3 ugrást tesznek meg.
- `flood.max.unscoped 1`: a régió nélküli üzenet legfeljebb egy átjátszón
  halad át.
