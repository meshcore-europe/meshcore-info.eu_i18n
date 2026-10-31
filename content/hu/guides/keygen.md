---
title: Kulcs generálása
layout: keygen
lead: Adj az átjátszódnak olyan prefixet, amelyet egyetlen közeli átjátszó sem használ. Keress egy szabad prefixet, készíts egy vele kezdődő kulcsot, és állítsd be.
description: Készíts a böngésződben olyan MeshCore-kulcsot, amelynek prefixét te választod, így egyetlen közeli átjátszónak sem lesz ugyanez a prefixe egy útvonalban.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-31'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

Az átjátszó a környezetében mindenkinek továbbítja az üzeneteket. Egy útvonalban
a MeshCore minden átjátszót a nyilvános kulcsa első bájtjaival jelöl:
ez a prefixe. Ha egy átjátszónak a közeledben ugyanaz a prefixe, az útvonalból nem
derül ki, melyikük továbbította az üzenetet. A MeshCore véletlenszerűen
választja a kulcsot. Itt te készítesz egyet a kívánt prefixszel.

Használj 2 bájtot. 2026. október 13-án a [MeshCore Analyzer](https://meshcore-analyzer.eu/)
azt látta, hogy Európában minden 1 bájtos prefixen több átjátszó osztozik. Az útvonal-hash mérete a
küldő egyik beállítása. Ez határozza meg, hogy az egyes prefixekből hány bájt kerül
az útvonalba; lásd: [CLI-parancsok](/guides/cli/).
