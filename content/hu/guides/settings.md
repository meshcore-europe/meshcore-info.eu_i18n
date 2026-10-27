---
title: Ajánlott beállítások
layout: settings
lead: A rádióbeállítás, amelyet a környéked használ, és a szomszédaid által módosított beállítások. Válaszd ki az országod, állítsd be a presetet és másold ki a parancsokat.
description: A MeshCore rádióbeállítás Európa területei szerint, valamint a helyi csoportok által az alapértelmezettől eltérően beállított átjátszó- és companion-beállítások, a parancsokkal együtt.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '9547ba62'
  seeded: '2026-10-26'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', '43cde8b4']
---

Az alábbi területek mindegyike saját rádióbeállítást használ, vagy módosít néhányat a MeshCore alapértelmezésein. Minden, ami nincs felsorolva, az alapértelmezésen marad, így csak azt módosítod, amit a te területed módosított. Az átjátszó mindenki számára továbbadja az üzeneteket; a companion az a csomópont, amelyről te üzensz, Bluetooth-on vagy USB-n párosítva a telefonoddal vagy laptopoddal, vagy saját képernyővel.

Az [átjátszó útmutató](/repeater-guide/#config) megmutatja, hogyan éred el az átjátszód parancssorát, a [soros konzol](/firmware/console/) ezen az oldalon pedig az a hely, ahol te magad gépeled be a parancsokat. Minden terület alatt USB-n is elküldheted annak beállításait. Felsorolja a [jogi korlátokat](/repeater-guide/#legal) is a 868 MHz-en.

## Tartsd alacsonyan a forgalmat {#traffic}

Ezek a beállítások minden területre érvényesek. Minden átjátszó továbbadja az összes flood üzenetet, amit hall. Egy üzeneted egy adásba kerül, plusz egybe minden átjátszónál, amely hallja. A 10% kitöltési tényező mellett egy átjátszó körülbelül 680 csomagot küldhet óránként, és ezen a számon mindenki osztozik körülötte. Az az üzenet, amely messzebbre utazik a kelleténél, ebből használ fel.

**A legkisebb régióba küldj, amely eléri azokat, akiknek írsz.**
A régiók egymásba ágyazódnak: ország, megye, helyi csoport, mindegyik saját kóddal, például `nl`, `nl-ov` és `nl-ov-zwo`. Az `nl-ov-zwo` régiónak szóló üzenet annak a csoportnak az átjátszóinál marad. Minden átjátszót csak azokba a régiókba tedd, amelyeket kiszolgál; a [helyi csoportod](/community/) tudja, melyek ezek.

**Korlátozd, mit ad tovább az átjátszód.** Két beállítás tartja otthon közelében azt a forgalmat, amelynek nem kell messzire utaznia:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: az advertek, amelyek egy csomópontot jelentenek be a meshnek, legfeljebb 3 ugrást tesznek meg.
- `flood.max.unscoped 1`: egy régió nélküli üzenet legfeljebb egy átjátszón halad át.
