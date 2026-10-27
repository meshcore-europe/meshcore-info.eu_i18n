---
title: Vygeneruj si klíč
layout: keygen
lead: Dej svému repeateru prefix, který žádný repeater v tvém okolí nepoužívá. Najdi volný prefix, vytvoř klíč, který jím začíná, a nastav ho.
description: Vytvoř si v prohlížeči klíč MeshCore s prefixem podle vlastního výběru, aby žádný repeater poblíž tvého neměl v cestě stejný prefix.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-26'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
---

Repeater předává zprávy dál všem ve svém okolí. V cestě MeshCore
označuje každý repeater prvními bajty jeho veřejného klíče:
jeho prefixem. Když má repeater v tvém okolí stejný prefix, z cesty nepoznáš,
který z těch dvou zprávu předal. MeshCore volí klíč náhodně. Tady
si vytvoříš klíč s prefixem, jaký chceš.

Zvol 2 bajty. Dne 13. října 2026 viděl [MeshCore Analyzer](https://meshcore-analyzer.eu/)
v Evropě každý 1bajtový prefix sdílený. Velikost hashe cesty, nastavení
odesílatele, určuje, kolik bajtů z každého prefixu jde do cesty; viz [příkazy CLI](/guides/cli/).
