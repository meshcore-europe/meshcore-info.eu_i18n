---
title: Hărți de acoperire
layout: map
lead: Vezi până unde ajunge mesh-ul, unde sunt nodurile și pe ce drum circulă mesajele. Comunități din toată Europa întrețin aceste hărți.
description: Hărți MeshCore live, hărți de acoperire și analizoare de pachete pentru Europa și pentru fiecare țară.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '351071aa'
  seeded: '2026-10-31'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['351071aa']
  blocks: ['dd5f039e', '9d4a2ad8', '70c417f2', '9fef7e16']
---

Un nod apare pe aceste hărți când proprietarul lui îl publică sau când îl aude un
*observer*: un nod care trimite mai departe prin MQTT ce aude. De aceea, nicio hartă
nu e completă. Analizoarele arată traficul primit de observerii lor: pachete,
rute și activitatea pe canale. Mesajele directe rămân criptate, deci niciun analizor
nu le arată conținutul.

Pe hartă, un nod stă unde l-a pus proprietarul. Poziția poate fi greșită sau
depășită. Un mesaj flood circulă pe mai multe rute în același timp. Ruta de pe hartă e cea
a copiei care a ajuns prima. Celelalte nu se înregistrează.

Aceste hărți au nevoie de internet. Mesh-ul nu are nevoie. [De ce](/network/)

Ai un repetor, adică un nod care dă mesajele mai departe? Setează-i poziția cu `set lat` și `set lon`, iar hărțile
îl pot plasa. [Ghidul pentru repetor](/repeater-guide/#config) îți arată cum.
