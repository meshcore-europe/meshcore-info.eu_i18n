---
title: Dækningskort
layout: map
lead: Se hvor meshet når ud, hvor noderne står, og hvordan beskeder rejser. Fællesskaber i hele Europa driver disse kort.
description: Live MeshCore-kort, dækningskort og pakkeanalysatorer for Europa og de enkelte lande.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '550066cc'
  seeded: '2026-10-26'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['550066cc']
---

En node vises på disse kort, når ejeren offentliggør den, eller når en *observer* hører den: en node, der videresender det, den hører, over MQTT. Derfor er intet kort komplet. Analysatorer viser den trafik, deres observere modtager: pakker, ruter og aktivitet på kanaler. Direkte beskeder forbliver krypterede, så ingen analysator viser, hvad de indeholder.

Disse kort kræver internet. Det gør meshet ikke. [Hvorfor](/network/)

Driver du en repeater, en node der sender beskeder videre? Angiv dens position med `set lat` og `set lon`, så kan kortene placere den. [Repeater-guiden](/repeater-guide/#config) viser hvordan.
