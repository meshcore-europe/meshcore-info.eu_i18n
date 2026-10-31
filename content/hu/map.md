---
title: Lefedettségi térképek
layout: map
lead: Nézd meg, meddig ér el a mesh, hol vannak a csomópontok, és merre haladnak az üzenetek. Ezeket a térképeket közösségek működtetik szerte Európában.
description: Élő MeshCore-térképek, lefedettségi térképek és csomagelemzők Európához és az egyes országokhoz.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '351071aa'
  seeded: '2026-10-31'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['351071aa']
  blocks: ['dd5f039e', '9d4a2ad8', '70c417f2', '9fef7e16']
---

Egy csomópont akkor jelenik meg ezeken a térképeken, ha a tulajdonosa közzéteszi,
vagy ha egy *observer* hallja. Az observer olyan csomópont, amely MQTT-n
továbbítja, amit hall. Ezért egyik térkép sem teljes. Az elemzők azt a forgalmat
mutatják, amelyet az observereik vesznek: csomagokat, útvonalakat és a csatornák
aktivitását. A közvetlen üzenetek titkosítva maradnak, így egyik elemző sem mutatja a
tartalmukat.

A csomópont ott látszik a térképen, ahová a tulajdonosa tette. Ez a hely lehet téves
vagy elavult. Egy flood üzenet egyszerre több útvonalon halad. A térképen látható
útvonal annak a példánynak az útja, amelyik elsőként érkezett meg. A többit senki
nem rögzíti.

Ezekhez a térképekhez internet kell, a mesh-hez nem. [Miért](/network/)

Átjátszót üzemeltetsz, vagyis olyan csomópontot, amely továbbadja az üzeneteket? Állítsd be a helyzetét a `set lat` és a `set lon` paranccsal, így a térképek el tudják helyezni. Hogy hogyan, azt az [átjátszó-útmutató](/repeater-guide/#config) mutatja meg.
