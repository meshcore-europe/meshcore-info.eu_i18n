---
title: Mapas de cobertura
layout: map
lead: Vê até onde chega a mesh, onde estão os nós e como viajam as mensagens. Comunidades de toda a Europa mantêm estes mapas.
description: Mapas MeshCore em tempo real, mapas de cobertura e analisadores de pacotes para a Europa e para países individuais.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '550066cc'
  seeded: '2026-10-26'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['550066cc']
---

Um nó aparece nestes mapas quando o dono o publica, ou quando um *observador* o ouve: um nó que reencaminha por MQTT o que ouve. Por isso, nenhum mapa está completo. Os analisadores mostram o tráfego que os seus observadores recebem: pacotes, rotas e atividade dos canais. As mensagens diretas ficam cifradas, por isso nenhum analisador mostra o seu conteúdo.

Estes mapas precisam de internet; a mesh não. [Porquê](/network/)

Tens um repetidor, um nó que passa mensagens adiante? Define a posição dele com `set lat` e `set lon`, e os mapas conseguem colocá-lo. O [guia de repetidores](/repeater-guide/#config) explica como.
