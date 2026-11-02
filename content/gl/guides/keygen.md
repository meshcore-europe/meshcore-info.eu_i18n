---
title: Xerar unha chave
layout: keygen
lead: Dálle ao teu repetidor un prefixo que non use ningún repetidor preto de ti. Busca un prefixo libre, crea unha chave que comece por el e configúraa.
description: Crea no navegador unha chave de MeshCore co prefixo que elixas, para que ningún repetidor preto do teu comparta o seu prefixo nunha ruta.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-11-02'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

Un repetidor reenvía as mensaxes de todos os que ten arredor. Nunha ruta, MeshCore
identifica cada repetidor polos primeiros bytes da súa chave pública:
o seu prefixo. Se un repetidor preto de ti ten o mesmo prefixo, a ruta non mostra
cal dos dous reenviou a mensaxe. MeshCore escolle a chave ao chou. Aquí
creas ti unha co prefixo que queres.

Usa 2 bytes. O 13 de outubro de 2026, o [MeshCore Analyzer](https://meshcore-analyzer.eu/)
detectou que todos os prefixos de 1 byte estaban compartidos en Europa. O tamaño do hash da ruta, un axuste
do remitente, decide cantos bytes de cada prefixo van nunha ruta; consulta [Comandos CLI](/guides/cli/).
