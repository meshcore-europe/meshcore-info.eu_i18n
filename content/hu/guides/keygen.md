---
title: Kulcs generálása
layout: keygen
lead: Adj az átjátszódnak olyan előtagot, amelyet a közeledben egyik átjátszó sem használ. Keress egy szabad előtagot, készíts vele kezdődő kulcsot, és állítsd be.
description: Készíts MeshCore-kulcsot a böngésződben, általad választott előtaggal, hogy a közeledben egyik átjátszó előtagja se egyezzen a tiéddel az útvonalban.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-26'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
---

Az átjátszó mindenkinek továbbítja az üzeneteket a környezetében. Az útvonalban a MeshCore
minden átjátszót a nyilvános kulcsának első bájtjaival jelöli:
ez az előtag. Ha a közeledben egy átjátszónak ugyanaz az előtagja, az útvonalból nem derül ki,
melyikük továbbította az üzenetet. A MeshCore véletlenszerűen választja a kulcsot. Itt
olyan kulcsot készíthetsz, amelynek előtagját te választod.

Használj 2 bájtot. 2026. október 13-án a [MeshCore Analyzer](https://meshcore-analyzer.eu/)
Európában minden 1 bájtos előtagot többszörösen látta. Az útvonal-hash mérete, a küldő
egyik beállítása, dönti el, hogy az egyes előtagokból hány bájt kerül az útvonalba; lásd: [CLI-parancsok](/guides/cli/).
