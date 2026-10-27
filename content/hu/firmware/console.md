---
title: Soros konzol
layout: console
lead: Küldj parancsokat az átjátszódnak a böngésződből, USB-n keresztül.
description: Állíts be MeshCore átjátszót, szobaszervert vagy szenzort USB-n keresztül Chrome, Edge vagy Opera böngészőből, böngészőben futó soros konzollal. Nem kell programot telepítened.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-26'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: 'a2fe0704'}
  sections: ['c33167ce']
---

Az átjátszónak (továbbadja az üzeneteket), a szobaszervernek (egy csoport bejegyzéseit tárolja) és a szenzornak (mérési adatokat jelent) nincs alkalmazása. Ezért USB-n keresztül, parancsok begépelésével állítod be. Csatlakoztasd a csomópontodat a számítógépedhez. Nyisd meg ezt az oldalt számítógépen, Chrome, Edge vagy Opera böngészőben, és válaszd ki a csomópontod portját. A konzol először a `get role` és a `ver` parancsot küldi el, így megtudja, mi a csomópontod. Mindkettő csak olvas. Ezután megmutatja, mit válaszol a csomópontod. Gépelj be egy parancsot, például `get name`, és nyomj Entert. Gépelés közben felajánlja azokat a parancsokat, amelyeket a csomópontod ismer. A Tab billentyű az elsőt beírja helyetted.

A companion, vagyis az a csomópont, amelyikről üzenetet küldesz, ehelyett USB-n az alkalmazással beszél. Ennek parancssora a MeshCore alkalmazásban van, az 1.50-es vagy újabb verzióban.
