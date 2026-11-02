---
title: Soovitatavad seaded
layout: settings
lead: Sinu piirkonna raadio eelseadistus ja seaded, mida su naabrid on muutnud. Vali oma riik, määra eelseadistus ja kopeeri käsud.
description: MeshCore'i raadio eelseadistus iga Euroopa piirkonna kohta ning kordusjaama ja companioni seaded, mida kohalikud rühmad on vaikeväärtustest erinevaks muutnud, koos käskudega.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-11-02'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Iga allpool toodud piirkond kasutab oma raadioeelseadistust või muudab mõnda
MeshCore'i vaikeväärtust. Kõik, mida loetelus pole, jääb vaikeväärtusele, nii et
muudad ainult seda, mida su piirkond on muutnud. Kordusjaam (repeater) edastab
sõnumeid kõigi jaoks. Companion on sõlm, millelt sõnumeid saadad: see on Bluetoothi
või USB kaudu seotud su telefoni või sülearvutiga või sellel on oma ekraan.

[Kordusjaama juhendist](/repeater-guide/#config) leiad, kuidas kordusjaama
käsureale pääseda, ja selle saidi [jadakonsoolis](/firmware/console/) saad käske
ise sisestada. Iga piirkonna all saad selle seaded ka USB kaudu saata. Kordusjaama
juhendis on kirjas ka 868 MHz sagedusala [seaduslikud piirangud](/repeater-guide/#legal).

## Hoia andmeliiklus väikesena {#traffic}

Need seaded kehtivad kõigis piirkondades. Iga kordusjaam edastab kõik flood-sõnumid,
mida see kuuleb. Üks sinu sõnum nõuab ühe saatmise ja lisaks veel ühe iga kordusjaama
kohta, mis seda kuuleb. 10% töötsükli piires saab kordusjaam saata umbes 680 paketti
tunnis ja seda arvu jagavad kõik selle ümbruses. Sõnum, mis liigub vajalikust kaugemale,
kulutab sellest osa ära.

**Saada sõnum väikseimasse regiooni, mis jõuab inimesteni, kellele kirjutad.**
Regioonid paiknevad üksteise sees: riik, provints ja kohalik rühm, igaühel oma kood,
näiteks `nl`, `nl-ov` ja `nl-ov-zwo`. Regioonile `nl-ov-zwo` saadetud sõnum jääb selle
rühma kordusjaamade piiresse. Kordusjaam edastab ainult nende regioonide sõnumeid, mis
on sellele endale määratud: määratud `nl` ei pane seda edastama `nl-ov` sõnumeid. Lisa iga
kordusjaam kõigisse regioonidesse, mida see teenindab, ja ainult nendesse. Su
[kohalik rühm](/community/) teab, millised need on.

**Piira seda, mida su kordusjaam edastab.** Kaks seadet hoiavad kodu lähedal liikluse,
millel pole vaja kaugele minna:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: advertid, mis annavad võrgule sõlmest teada, liiguvad
  kõige rohkem 3 hüpet.
- `flood.max.unscoped 1`: regioonita sõnum läbib kõige rohkem ühe kordusjaama.
