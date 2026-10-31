---
title: Het netwerk
layout: network
lead: Bekijk de mesh in heel Europa, en help hem meer te zien. Observers luisteren naar de mesh en melden wat ze horen. Elke nieuwe observer laat weer iets meer zien.
description: 'Zo wordt de MeshCore-mesh in Europa zichtbaar: observers melden wat ze horen aan de MeshCore Analyzer. Live cijfers, en hoe je zelf een observer toevoegt.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-10-31'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

De mesh houdt zelf niets bij: een bericht gaat van node naar node en is
daarna weg. Wat je op [dekkingskaarten](/map/) en in statistieken ziet, komt van
observers. Een observer is een node die ook meldt wat hij hoort. Dat doet hij via MQTT,
over Wi-Fi of het internet. De melding gaat maar één kant op: er komt niets terug
op de mesh. Een repeater (een node die berichten doorgeeft) met observer-firmware
blijft berichten doorgeven zoals voorheen.

Observers in heel Europa sturen hun meldingen naar de [MeshCore Analyzer](https://meshcore-analyzer.eu/)
op mqtt.meshcore-analyzer.eu. De Analyzer leest ook andere brokers uit. Een
observer die daar meldt, telt dus ook mee. Uit die meldingen maakt de Analyzer de kaarten, de
statistieken en de [kanaallijst](/guides/channels/) op deze site.

{{< callout type="tip" >}}
De mesh heeft dit allemaal niet nodig. De tools helpen je alleen om de mesh te zien en te plannen. De meldingen van de observers, de Analyzer, deze kaarten
en tools lopen via het internet. Bij een stroomstoring of als het internet uitvalt, stoppen ze. De
mesh blijft berichten over de radio doorgeven, via elke repeater die nog
stroom heeft, zoals de repeaters op zonne-energie.
{{< /callout >}}
