---
title: Gomendatutako ezarpenak
layout: settings
lead: Zure eremuak erabiltzen duen irrati-aurrezarpena, eta zure bizilagunek aldatutako ezarpenak. Aukeratu zure herrialdea, ezarri aurrezarpena eta kopiatu komandoak.
description: MeshCore irrati-aurrezarpena Europako eremu bakoitzerako, eta tokiko taldeek balio lehenetsietatik aldatu dituzten errepikagailu- eta laguntzaile-ezarpenak, komandoekin.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-11-02'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Beheko eremu bakoitzak bere irrati-aurrezarpena erabiltzen du, edo
MeshCoreren balio lehenetsi batzuk aldatzen ditu. Zerrendan ez dagoen guztia
balio lehenetsian geratzen da, beraz zure eremuak aldatutakoa bakarrik aldatu
behar duzu. Errepikagailuak denentzat birbidaltzen ditu mezuak; laguntzailea
mezuak bidaltzeko erabiltzen duzun nodoa da, telefonoarekin edo ordenagailu
eramangarriarekin Bluetooth edo USB bidez parekatuta, edo bere pantailarekin.

[Errepikagailuen gidan](/repeater-guide/#config) ikusiko duzu nola sartu zure
errepikagailuaren komando-lerrora, eta webgune honetako
[serieko kontsolan](/firmware/console/) zuk zeuk idazten dituzu komandoak.
Eremu bakoitzaren azpian, ezarpenak USB bidez ere bidal ditzakezu. Gida horrek
868 MHz-eko [muga legalak](/repeater-guide/#legal) ere zerrendatzen ditu.

## Murriztu trafikoa {#traffic}

Ezarpen hauek eremu guztietan balio dute. Errepikagailu bakoitzak entzuten duen
flood mezu oro birbidaltzen du. Zure mezu batek transmisio bat behar du, gehi
bat mezua entzuten duen errepikagailu bakoitzeko. % 10eko duty cycle-aren barruan,
errepikagailu batek orduko 680 pakete inguru bidal ditzake, eta inguruko guztiek
kopuru hori partekatzen dute. Behar baino urrunago doan mezuak kopuru horren
zati bat erabiltzen du.

**Bidali mezua idazten diezun pertsonengana iristen den eskualderik txikienera.**
Eskualdeak bata bestearen barruan daude: herrialdea, probintzia eta tokiko
taldea, bakoitza bere kodearekin, adibidez `nl`, `nl-ov` eta `nl-ov-zwo`.
`nl-ov-zwo` eskualderako mezua talde horretako errepikagailuetan geratzen da.
Errepikagailuak berak dituen eskualdeak bakarrik birbidaltzen ditu: `nl` izateak
ez dio `nl-ov` birbidalarazten. Sartu errepikagailu bakoitza zerbitzatzen duen
eskualde guztietan, eta horietan bakarrik; zure [tokiko taldeak](/community/)
badaki zein diren.

**Mugatu zure errepikagailuak birbidaltzen duena.** Bi ezarpenek etxetik gertu
gordetzen dute urrutira joan beharrik ez duen trafikoa:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: iragarkiek (adverts), nodo bat sareari iragartzen
  diotenek, gehienez 3 jauzi egiten dituzte.
- `flood.max.unscoped 1`: eskualderik gabeko mezua gehienez errepikagailu
  batetik igarotzen da.
