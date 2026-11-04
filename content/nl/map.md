---
title: Dekkingskaarten
layout: map
lead: Zie waar de mesh komt, waar nodes staan en hoe berichten reizen. Communities in heel Europa houden deze kaarten bij.
description: Live MeshCore-kaarten, dekkingskaarten en pakketanalysers voor Europa en afzonderlijke landen.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '24bfdf6b'
  seeded: '2026-11-04'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['24bfdf6b']
  blocks: ['dd5f039e', '9d4a2ad8', '763fc710', '70c417f2', '9fef7e16']
---

Een node verschijnt op deze kaarten als de eigenaar hem publiceert, of als een
*observer* hem hoort: een node die wat hij hoort via MQTT doorstuurt. Geen enkele kaart
is dus compleet. Analysers tonen het verkeer dat hun observers ontvangen: pakketten,
routes en kanaalactiviteit. Directe berichten blijven versleuteld. Geen analyser
laat dus zien wat erin staat.

Een node staat op de kaart op de plek die de eigenaar heeft ingevuld. Die plek kan fout
of verouderd zijn. Een flood-bericht reist tegelijk over meerdere paden. Een route op de kaart is het pad
van de kopie die als eerste aankwam. De andere kopieën worden niet vastgelegd.

Lijkt een route op een kaart onwaarschijnlijk? Controleer 2 nodes van die route met Line of Sight in
de MeshCore-app. De [repeatergids](/repeater-guide/#check-site) laat zien hoe dat moet.

Voor deze kaarten heb je internet nodig, voor de mesh niet. [Waarom](/network/)

Beheer je een repeater, een node die berichten doorgeeft? Stel de positie in met `set lat` en `set lon`,
dan kunnen kaarten hem plaatsen. In de [repeater-handleiding](/repeater-guide/#config) lees je hoe dat werkt.
