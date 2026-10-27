---
title: Hărți de acoperire
layout: map
lead: Vezi până unde ajunge mesh-ul, unde sunt nodurile și cum circulă mesajele. Comunități din toată Europa întrețin aceste hărți.
description: Hărți MeshCore în timp real, hărți de acoperire și analizoare de pachete pentru Europa și pentru țări individuale.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '550066cc'
  seeded: '2026-10-26'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['550066cc']
---

Un nod apare pe aceste hărți când proprietarul îl publică sau când un
*observator* îl aude: un nod care transmite mai departe prin MQTT ce aude. De aceea nicio hartă
nu este completă. Analizoarele arată traficul pe care îl recepționează observatorii lor: pachete,
rute și activitate pe canale. Mesajele directe rămân criptate, așa că niciun analizor
nu arată ce conțin.

Aceste hărți au nevoie de internet; mesh-ul nu. [De ce](/network/)

Ai un repetor, adică un nod care transmite mesajele mai departe? Setează-i poziția cu `set lat` și `set lon`, iar hărțile
îl pot afișa la locul lui. [Ghidul pentru repetoare](/repeater-guide/#config) îți arată cum.
