---
title: Soros konzol
layout: console
lead: Parancsokat írhatsz az átjátszódnak a böngészőből, USB-n keresztül.
description: MeshCore átjátszót, room servert vagy szenzort USB-n keresztül állíthatsz be Chrome-ból, Edge-ből vagy Operából, egy böngészős soros konzollal, telepítés nélkül.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-31'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Egy átjátszónak (továbbítja az üzeneteket), egy room servernek (bejegyzéseket tárol
egy csoportnak) vagy egy szenzornak (méréseket küld) nincs alkalmazása. Ezért USB-n
keresztül, parancsok beírásával állítod be. Csatlakoztasd a csomópontodat a
számítógéphez. Nyisd meg ezt az oldalt Chrome-ban, Edge-ben vagy Operában egy
számítógépen, és válaszd ki a csomópontod portját. A konzol először a `get role` és
a `ver` parancsot küldi el, így megtudja, milyen csomópontod van. Mindkettő csak
olvas. Utána megjeleníti, amit a csomópontod válaszol. Írj be egy parancsot,
például a `get name` parancsot, és nyomd meg az Entert. Gépelés közben a konzol
felajánlja azokat a parancsokat, amelyeket a csomópontod ért. A Tab kitölti az elsőt.

A companion az a csomópont, amelyről üzenetet küldesz. Ez viszont USB-n keresztül
az alkalmazással kommunikál. A parancssora a MeshCore alkalmazásban érhető el, az 1.50-es
vagy újabb verzióban.
