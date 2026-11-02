---
title: Vygeneruj si kľúč
layout: keygen
lead: Daj svojmu repeateru prefix, ktorý nepoužíva žiadny repeater vo tvojom okolí. Nájdi voľný prefix, vytvor kľúč, ktorý ním začína, a nastav ho.
description: Vytvor si v prehliadači kľúč MeshCore s prefixom podľa vlastného výberu, aby žiadny repeater v okolí nemal v ceste rovnaký prefix.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-11-02'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

Repeater preposiela správy pre všetkých vo svojom okolí. V ceste MeshCore
označuje každý repeater prvými bajtmi jeho verejného kľúča:
to je jeho prefix. Keď má repeater vo tvojom okolí rovnaký prefix, z cesty
nespoznáš, ktorý z tých dvoch správu preposlal. MeshCore vyberá kľúč náhodne. Tu si
vytvoríš kľúč s prefixom, aký chceš.

Zvoľ si 2 bajty. 13. októbra 2026 [MeshCore Analyzer](https://meshcore-analyzer.eu/)
zistil, že v Európe používa každý 1-bajtový prefix viac repeaterov. Veľkosť hashu cesty je nastavenie
odosielateľa. Určuje, koľko bajtov z každého prefixu sa dostane do cesty; pozri [príkazy CLI](/guides/cli/).
