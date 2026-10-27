---
title: Netværket
layout: network
lead: Se meshet på tværs af Europa, og hjælp det med at se mere. Observatører lytter til meshet og rapporterer det, og hver ny observatør viser lidt mere.
description: 'Sådan bliver MeshCore-meshet i Europa synligt: observatører rapporterer det, de hører, til MeshCore Analyzer. Live-tal, og sådan tilføjer du din egen observatør.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '05fa5ea3'
  seeded: '2026-10-26'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['05fa5ea3']
---

Meshet selv gemmer intet: en besked går fra node til node og er væk. Det, du ser på [dækningskort](/map/) og i statistikker, kommer fra observatører. En observatør er en node, der også rapporterer det, den hører, over MQTT via Wi-Fi eller internettet. Rapporten går kun den ene vej: intet kommer tilbage på meshet. En repeater (en node, der sender beskeder videre) med observatør-firmware bliver ved med at repeate som før.

Observatører i hele Europa rapporterer til [MeshCore Analyzer](https://meshcore-analyzer.eu/) på mqtt.meshcore-analyzer.eu. Analyzeren læser også andre brokere, så en observatør dér tæller også med. Ud fra de rapporter bygger den kortene, statistikkerne og [kanallisten](/guides/channels/) på dette site.

{{< callout type="tip" >}}
Meshet har ikke brug for noget af det her. Observatørernes rapporter, Analyzeren, kortene og værktøjerne går over internettet. Ved strømafbrydelse, eller når internettet er nede, stopper de. Meshet sender fortsat beskeder videre over radio gennem hver repeater, der stadig har strøm, for eksempel dem på solceller. Værktøjerne er der for at se og planlægge meshet, ikke for at drive det.
{{< /callout >}}
