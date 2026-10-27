---
title: Het netwerk
layout: network
lead: Bekijk de mesh in heel Europa en help hem meer te zien. Observers horen de mesh en melden wat ze horen, en elke nieuwe observer laat een stukje meer zien.
description: 'Hoe de MeshCore-mesh in Europa zichtbaar wordt: observers melden wat ze horen aan de MeshCore Analyzer. Live cijfers, en hoe je je eigen observer toevoegt.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '05fa5ea3'
  seeded: '2026-10-26'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['05fa5ea3']
---

De mesh zelf houdt niets bij: een bericht gaat van node naar node en is daarna
weg. Wat je op [dekkingskaarten](/map/) en in statistieken ziet, komt van
observers. Een observer is een node die daarnaast via MQTT meldt wat hij hoort,
over Wi-Fi of internet. Die melding gaat maar één kant op: er komt niets terug
de mesh in. Een repeater (een node die berichten doorgeeft) met observer-firmware
blijft gewoon doorgeven zoals eerst.

Observers in heel Europa melden aan de [MeshCore Analyzer](https://meshcore-analyzer.eu/)
op mqtt.meshcore-analyzer.eu. De Analyzer leest ook andere brokers, dus een
observer daar telt ook mee. Uit die meldingen bouwt hij de kaarten, de
statistieken en de [kanaallijst](/guides/channels/) op deze site.

{{< callout type="tip" >}}
De mesh heeft dit allemaal niet nodig. De meldingen van observers, de Analyzer, deze kaarten
en tools lopen over internet. Bij een stroomstoring of als internet uitvalt, stoppen ze. De
mesh blijft berichten doorgeven via de radio, over elke repeater die nog stroom
heeft, zoals die op zonne-energie. De tools zijn er om de mesh te bekijken en te
plannen, niet om hem te laten draaien.
{{< /callout >}}
