---
title: Netværket
layout: network
lead: Se meshet i hele Europa, og hjælp det med at se mere. Observers hører meshet og rapporterer det, og hver ny observer viser lidt mere.
description: 'Sådan bliver MeshCore-meshet i Europa synligt: observers rapporterer det, de hører, til MeshCore Analyzer. Live-tal, og sådan tilføjer du din egen observer.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-10-31'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Meshet gemmer ingenting: en besked går fra node til node og er så
væk. Det, du ser på [dækningskort](/map/) og i statistikker, kommer fra
observers. En observer er en node, der også rapporterer det, den hører, over MQTT
via Wi-Fi eller internettet. Rapporten går kun én vej: intet kommer tilbage ud på
meshet. En repeater (en node, der sender beskeder videre) med observer-firmware
bliver ved med at videresende som før.

Observers i hele Europa rapporterer til [MeshCore Analyzer](https://meshcore-analyzer.eu/)
på mqtt.meshcore-analyzer.eu. Analyzer læser også fra andre brokere, så en
observer dér tæller også med. Ud fra disse rapporter laver Analyzer kortene,
statistikkerne og [kanallisten](/guides/channels/) på dette site.

{{< callout type="tip" >}}
Meshet har ikke brug for noget af dette. Værktøjerne hjælper dig kun med at se og planlægge det. Observernes rapporter, Analyzer, disse kort
og værktøjer går over internettet. Ved strømsvigt, eller når internettet er nede, stopper de. Meshet
bliver ved med at sende beskeder videre via radio, gennem alle repeatere, der stadig har
strøm, for eksempel dem på solenergi.
{{< /callout >}}
