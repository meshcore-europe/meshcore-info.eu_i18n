---
title: Zemljevidi pokritosti
layout: map
lead: Oglej si, kam seže omrežje, kje so vozlišča in kako potujejo sporočila. Te zemljevide vzdržujejo skupnosti po vsej Evropi.
description: Zemljevidi MeshCore v živo, zemljevidi pokritosti in analizatorji paketov za Evropo in posamezne države.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '24bfdf6b'
  seeded: '2026-11-04'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['24bfdf6b']
  blocks: ['dd5f039e', '9d4a2ad8', '763fc710', '70c417f2', '9fef7e16']
---

Vozlišče se na teh zemljevidih pojavi, ko ga objavi lastnik ali ko ga sliši *observer*: vozlišče, ki prek MQTT posreduje, kar sliši. Zato noben zemljevid ni popoln. Analizatorji prikazujejo promet, ki ga prejmejo njihovi observerji: pakete, poti in dejavnost na kanalih. Neposredna sporočila ostanejo šifrirana, zato v nobenem analizatorju ne moreš prebrati njihove vsebine.

Vozlišče je na zemljevidu tam, kamor ga je postavil lastnik, in ta položaj je lahko napačen ali zastarel. Sporočilo flood potuje po več poteh hkrati. Pot na zemljevidu je pot kopije, ki je prispela prva. Druge poti niso zabeležene.

Se ti pot na zemljevidu zdi malo verjetna? S funkcijo Line of Sight v aplikaciji MeshCore preveri 2 vozlišči na njej. Kako to narediš, kaže [vodnik za repetitorje](/repeater-guide/#check-site).

Ti zemljevidi potrebujejo internet, omrežje pa ne. [Zakaj](/network/)

Imaš repeater, vozlišče, ki posreduje sporočila naprej? Njegov položaj nastavi z ukazoma `set lat` in `set lon`, da ga lahko zemljevidi umestijo. Kako to narediš, piše v [vodniku za repeater](/repeater-guide/#config).
