---
title: Lefedettségi térképek
layout: map
lead: Nézd meg, hová ér el a mesh, hol vannak a csomópontok, és hogyan haladnak az üzenetek. Ezeket a térképeket Európa közösségei működtetik.
description: Élő MeshCore-térképek, lefedettségi térképek és csomagelemzők Európához és egyes országokhoz.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '550066cc'
  seeded: '2026-10-26'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['550066cc']
---

Egy csomópont akkor jelenik meg ezeken a térképeken, ha a tulajdonosa közzéteszi, vagy ha egy *megfigyelő* hallja. A megfigyelő olyan csomópont, amely MQTT-n továbbítja, amit hall. Ezért egyik térkép sem teljes. Az elemzők azt a forgalmat mutatják, amelyet a megfigyelőik fogadnak: csomagokat, útvonalakat és csatornaaktivitást. A közvetlen üzenetek titkosítva maradnak, így egyik elemző sem mutatja a tartalmukat.

Ezekhez a térképekhez internet kell, a mesh-hez nem. [Miért](/network/)

Átjátszót működtetsz, vagyis olyan csomópontot, amely továbbadja az üzeneteket? Állítsd be a helyzetét a `set lat` és `set lon` parancsokkal, és a térképek el tudják helyezni. Az [átjátszó-útmutató](/repeater-guide/#config) megmutatja, hogyan.
