---
title: Dekningskart
layout: map
lead: Se hvor meshet når, hvor nodene står og hvordan meldinger går. Miljøer over hele Europa drifter disse kartene.
description: Live MeshCore-kart, dekningskart og pakkeanalysatorer for Europa og enkeltland.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '351071aa'
  seeded: '2026-10-31'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['351071aa']
  blocks: ['dd5f039e', '9d4a2ad8', '70c417f2', '9fef7e16']
---

En node dukker opp på disse kartene når eieren publiserer den, eller når en
*observer* hører den. En observer er en node som sender videre det den hører over MQTT. Derfor er
ingen kart komplette. Analysatorene viser trafikken som observerne deres tar imot: pakker,
ruter og aktivitet i kanalene. Direktemeldinger forblir krypterte, så ingen analysator
viser hva de inneholder.

En node står på kartet der eieren plasserte den. Plasseringen kan være feil eller
utdatert. En flood-melding går langs flere stier samtidig. En rute på kartet er stien
til kopien som kom fram først. De andre blir ikke registrert.

Disse kartene trenger internett. Det gjør ikke meshet. [Hvorfor](/network/)

Driver du en repeater, altså en node som sender meldinger videre? Sett posisjonen med `set lat` og `set lon`, så
kan kartene plassere den. [Repeater-guiden](/repeater-guide/#config) viser hvordan.
