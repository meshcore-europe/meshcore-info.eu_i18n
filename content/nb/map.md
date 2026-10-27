---
title: Dekningskart
layout: map
lead: Se hvor meshen rekker, hvor nodene står og hvordan meldinger beveger seg. Fellesskap over hele Europa driver disse kartene.
description: Sanntidskart for MeshCore, dekningskart og pakkeanalysatorer for Europa og enkeltland.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '550066cc'
  seeded: '2026-10-26'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['550066cc']
---

En node dukker opp på disse kartene når eieren publiserer den, eller når en
*observatør* hører den: en node som sender videre det den hører over MQTT. Derfor
er ingen kart komplette. Analysatorer viser trafikken observatørene deres mottar:
pakker, ruter og aktivitet på kanaler. Direktemeldinger forblir kryptert, så ingen
analysator viser hva de inneholder.

Disse kartene trenger internett, det gjør ikke meshen. [Hvorfor](/network/)

Driver du en repeater, en node som sender meldinger videre? Sett posisjonen med `set lat` og `set lon`, så
kan kartene plassere den. [Repeaterguiden](/repeater-guide/#config) viser hvordan.
