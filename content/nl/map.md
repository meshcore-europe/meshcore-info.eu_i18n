---
title: Dekkingskaarten
layout: map
lead: Bekijk waar de mesh reikt, waar nodes staan en hoe berichten reizen. Communities in heel Europa beheren deze kaarten.
description: Live MeshCore-kaarten, dekkingskaarten en pakketanalysers voor Europa en afzonderlijke landen.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '550066cc'
  seeded: '2026-10-26'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['550066cc']
---

Een node verschijnt op deze kaarten als de eigenaar hem publiceert, of als een
*observer* hem hoort: een node die alles wat hij hoort doorstuurt via MQTT. Geen
enkele kaart is dus compleet. Analysers tonen het verkeer dat hun observers
ontvangen: pakketten, routes en activiteit op kanalen. Directe berichten blijven
versleuteld, dus geen enkele analyser laat zien wat erin staat.

Deze kaarten hebben internet nodig; de mesh niet. [Waarom](/network/)

Heb je een repeater, een node die berichten doorgeeft? Stel dan de positie in met `set lat` en `set lon`, zodat kaarten
hem kunnen plaatsen. De [repeatergids](/repeater-guide/#config) laat zien hoe.
