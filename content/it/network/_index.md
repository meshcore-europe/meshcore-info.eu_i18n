---
title: La rete
layout: network
lead: Guarda la mesh in tutta Europa e aiutala a vedere di più. Gli observer ascoltano la mesh e riferiscono ciò che sentono. Ogni nuovo observer mostra un po' di più.
description: 'Come la mesh MeshCore in Europa diventa visibile: gli observer inviano al MeshCore Analyzer ciò che sentono. Numeri in tempo reale e come aggiungere il tuo observer.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-10-31'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

La mesh in sé non conserva nulla: un messaggio passa da nodo a nodo e poi
sparisce. Ciò che vedi sulle [mappe di copertura](/map/) e nelle statistiche
arriva dagli observer. Un observer è un nodo che invia anche ciò che sente via
MQTT, tramite WiFi o internet. Il resoconto va in una sola direzione: nulla
torna sulla mesh. Un ripetitore (un nodo che inoltra i messaggi) con firmware
da observer continua a ripetere come prima.

Gli observer di tutta Europa inviano i loro dati al [MeshCore Analyzer](https://meshcore-analyzer.eu/)
su mqtt.meshcore-analyzer.eu. L'Analyzer legge anche altri broker, quindi conta
anche un observer collegato a uno di questi. Con questi dati l'Analyzer crea le
mappe, le statistiche e l'[elenco dei canali](/guides/channels/) di questo sito.

{{< callout type="tip" >}}
La mesh non ha bisogno di nulla di tutto questo: gli strumenti ti aiutano solo a vederla e a pianificarla. I dati degli observer, l'Analyzer, queste mappe
e questi strumenti passano per internet. Se manca la corrente o cade internet, si fermano. La
mesh continua a inoltrare i messaggi via radio, attraverso ogni ripetitore che ha ancora
corrente, come quelli a energia solare.
{{< /callout >}}
