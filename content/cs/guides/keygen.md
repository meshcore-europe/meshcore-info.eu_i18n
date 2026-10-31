---
title: Vygeneruj klíč
layout: keygen
lead: Dej svému repeateru prefix, který nepoužívá žádný repeater v tvém okolí. Najdi volný prefix, vytvoř klíč, který jím začíná, a nastav ho.
description: Vytvoř si v prohlížeči klíč pro MeshCore s prefixem, který si zvolíš. Žádný repeater poblíž tvého pak nebude mít v cestě stejný prefix.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-31'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

Repeater předává zprávy dál pro všechny ve svém okolí. MeshCore v cestě
označuje každý repeater prvními bajty jeho veřejného klíče: to je jeho prefix.
Když má repeater poblíž tebe stejný prefix, z cesty nepoznáš, který z nich
zprávu předal. MeshCore volí klíč náhodně. Tady si vytvoříš klíč s prefixem,
který chceš.

Použij 2 bajty. Dne 13. října 2026 zaznamenal [MeshCore Analyzer](https://meshcore-analyzer.eu/)
v Evropě každý 1bajtový prefix u více repeaterů. Kolik bajtů z každého prefixu
se zapíše do cesty, určuje velikost hashe cesty. Tu nastavuje odesílatel, viz
[příkazy CLI](/guides/cli/).
