---
title: Dækningskort
layout: map
lead: Se, hvor mesh'et når ud, hvor nodes står, og hvordan beskeder bevæger sig. Fællesskaber i hele Europa driver disse kort.
description: Live-kort over MeshCore, dækningskort og pakkeanalysatorer for Europa og de enkelte lande.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '351071aa'
  seeded: '2026-10-31'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['351071aa']
  blocks: ['dd5f039e', '9d4a2ad8', '70c417f2', '9fef7e16']
---

En node kommer på disse kort, når ejeren offentliggør den, eller når en
*observer* hører den: en node, der sender det, den hører, videre over MQTT. Derfor
er intet kort komplet. Analysatorer viser den trafik, som deres observers modtager:
pakker, ruter og aktivitet på kanaler. Direkte beskeder forbliver krypterede, så
ingen analysator viser, hvad der står i dem.

En node står på kortet der, hvor ejeren har placeret den. Placeringen kan være
forkert eller forældet. En flood-besked bevæger sig ad flere stier på én gang. En
rute på et kort er stien for den kopi, der kom først frem. De andre bliver ikke
registreret.

Kortene kræver internet. Det gør mesh'et ikke. [Hvorfor](/network/)

Driver du en repeater, altså en node, der sender beskeder videre? Angiv dens position med `set lat` og `set lon`, så kan kortene
placere den. [Guiden til repeatere](/repeater-guide/#config) viser hvordan.
