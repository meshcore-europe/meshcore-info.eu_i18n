---
title: A rede
layout: network
lead: Vê a mesh por toda a Europa e ajuda-a a ver mais. Os observers ouvem a mesh e relatam o que ouvem, e cada novo observer mostra um pouco mais.
description: 'Como a mesh MeshCore na Europa se torna visível: os observers enviam o que ouvem para o MeshCore Analyzer. Números ao vivo e como juntar o teu próprio observer.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-10-31'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

A mesh não guarda registos: uma mensagem passa de nó em nó e desaparece.
O que vês nos [mapas de cobertura](/map/) e nas estatísticas vem dos observers.
Um observer é um nó que também comunica o que ouve por MQTT, através de Wi-Fi ou
da internet. A comunicação segue num só sentido: nada volta para a mesh. Um repetidor
(um nó que reencaminha mensagens) com firmware de observer continua a
repetir como antes.

Há observers por toda a Europa que enviam relatos para o [MeshCore Analyzer](https://meshcore-analyzer.eu/)
em mqtt.meshcore-analyzer.eu. O Analyzer também lê outros brokers, por isso um
observer ligado a um deles também conta. Com esses relatos, o Analyzer constrói os mapas,
as estatísticas e a [lista de canais](/guides/channels/) deste site.

{{< callout type="tip" >}}
A mesh não precisa de nada disto: as ferramentas só te ajudam a vê-la e a planeá-la. Os relatos dos observers, o Analyzer, estes mapas
e estas ferramentas passam pela internet. Num corte de energia ou sem internet, deixam de funcionar. A
mesh continua a passar mensagens por rádio, através de cada repetidor que ainda tem
energia, como os que funcionam a energia solar.
{{< /callout >}}
