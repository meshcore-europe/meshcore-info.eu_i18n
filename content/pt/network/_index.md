---
title: A rede
layout: network
lead: Vê a mesh por toda a Europa e ajuda-a a ver mais. Os observadores escutam a mesh e reportam o que ouvem, e cada novo observador mostra um pouco mais.
description: 'Como a mesh MeshCore na Europa se torna visível: os observadores reportam o que ouvem ao MeshCore Analyzer. Números em direto, e como adicionar o teu próprio observador.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '05fa5ea3'
  seeded: '2026-10-26'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['05fa5ea3']
---

A própria mesh não guarda qualquer registo: uma mensagem passa de nó em nó e
desaparece. O que vês nos [mapas de cobertura](/map/) e nas estatísticas vem
dos observadores. Um observador é um nó que também reporta o que ouve por MQTT,
através de Wi-Fi ou da internet. O relato segue num só sentido: nada volta para
a mesh. Um repetidor (um nó que reencaminha mensagens) com firmware de observador
continua a repetir como antes.

Os observadores por toda a Europa reportam ao [MeshCore Analyzer](https://meshcore-analyzer.eu/)
em mqtt.meshcore-analyzer.eu. O Analyzer também lê outros brokers, por isso um
observador ligado a esses também conta. Com esses relatos, constrói os mapas, as
estatísticas e a [lista de canais](/guides/channels/) deste site.

{{< callout type="tip" >}}
A mesh não precisa de nada disto. Os relatos dos observadores, o Analyzer, estes mapas
e ferramentas passam pela internet. Num corte de energia ou quando a internet falha, param. A
mesh continua a passar mensagens por rádio, através de cada repetidor que ainda tenha
energia, como os que funcionam a energia solar. As ferramentas servem para ver e planear a
mesh, não para a fazer funcionar.
{{< /callout >}}
