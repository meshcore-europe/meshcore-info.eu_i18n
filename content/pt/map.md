---
title: Mapas de cobertura
layout: map
lead: Vê até onde chega a mesh, onde estão os nós e que caminho fazem as mensagens. Há comunidades por toda a Europa que mantêm estes mapas.
description: Mapas MeshCore em tempo real, mapas de cobertura e analisadores de pacotes para a Europa e para cada país.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '351071aa'
  seeded: '2026-10-31'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['351071aa']
  blocks: ['dd5f039e', '9d4a2ad8', '70c417f2', '9fef7e16']
---

Um nó aparece nestes mapas quando o dono o publica, ou quando um
*observer* o ouve: um nó que reencaminha o que ouve por MQTT. Por isso,
nenhum mapa está completo. Os analisadores mostram o tráfego que os seus
observers recebem: pacotes, rotas e atividade nos canais. As mensagens diretas
continuam cifradas, por isso nenhum analisador mostra o seu conteúdo.

Um nó fica no mapa no sítio onde o dono o colocou. Essa posição pode estar
errada ou desatualizada. Uma mensagem flood segue vários caminhos ao mesmo tempo.
A rota que vês no mapa é o caminho da cópia que chegou primeiro. As outras
cópias não ficam registadas.

Estes mapas precisam de internet; a mesh não. [Porquê](/network/)

Tens um repetidor, um nó que reencaminha as mensagens? Define a posição dele com `set lat` e `set lon`, e os mapas
conseguem situá-lo. O [guia do repetidor](/repeater-guide/#config) explica como.
