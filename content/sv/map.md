---
title: Täckningskartor
layout: map
lead: Se hur långt meshen når, var noderna finns och vilka vägar meddelandena tar. Grupper runt om i Europa driver kartorna.
description: Livekartor, täckningskartor och paketanalysverktyg för MeshCore i Europa och enskilda länder.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '351071aa'
  seeded: '2026-10-31'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['351071aa']
  blocks: ['dd5f039e', '9d4a2ad8', '70c417f2', '9fef7e16']
---

En nod syns på kartorna när ägaren publicerar den, eller när en
*observer* hör den: en nod som skickar vidare det den hör via MQTT. Därför är ingen karta
komplett. Analysverktygen visar trafiken som deras observers tar emot: paket,
rutter och kanalaktivitet. Direktmeddelanden förblir krypterade, så inget analysverktyg
visar vad de innehåller.

En nod står på kartan där ägaren har placerat den. Den platsen kan vara fel eller
inaktuell. Ett flood-meddelande tar flera vägar samtidigt. En rutt på kartan är vägen
för den kopia som kom fram först. De andra sparas inte.

Kartorna behöver internet, men det gör inte meshen. [Varför](/network/)

Driver du en repeater, alltså en nod som skickar meddelanden vidare? Ange positionen med `set lat` och `set lon`, så kan kartorna
placera ut den. I [repeater-guiden](/repeater-guide/#config) ser du hur du gör.
