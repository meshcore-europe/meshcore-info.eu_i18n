---
title: Täckningskartor
layout: map
lead: Se var meshen når, var noderna finns och hur meddelanden färdas. Communityn runt om i Europa driver de här kartorna.
description: Live-kartor för MeshCore, täckningskartor och paketanalysverktyg för Europa och enskilda länder.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '550066cc'
  seeded: '2026-10-26'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['550066cc']
---

En nod syns på de här kartorna när ägaren publicerar den, eller när en
*observer* hör den: en nod som vidarebefordrar det den hör via MQTT. Därför
är ingen karta komplett. Analysverktygen visar den trafik som deras observers
tar emot: paket, vägar och aktivitet på kanaler. Direktmeddelanden förblir
krypterade, så inget analysverktyg visar vad de innehåller.

De här kartorna behöver internet, det gör inte meshen. [Varför](/network/)

Driver du en repeater, en nod som skickar meddelanden vidare? Ange dess position med `set lat` och `set lon`, så
kan kartorna placera ut den. [Repeaterguiden](/repeater-guide/#config) visar hur du gör.
