---
title: La rete
layout: network
lead: Guarda la mesh in tutta Europa e aiutala a vedere di più. Gli osservatori ascoltano la mesh e la segnalano, e ogni nuovo osservatore mostra un pezzo in più.
description: 'Come la mesh MeshCore in Europa diventa visibile: gli osservatori segnalano quello che sentono al MeshCore Analyzer. Numeri in tempo reale, e come aggiungere il tuo osservatore.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '05fa5ea3'
  seeded: '2026-10-26'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['05fa5ea3']
---

La mesh in sé non conserva nulla: un messaggio passa da nodo a nodo e poi sparisce. Quello che vedi sulle [mappe di copertura](/map/) e nelle statistiche arriva dagli osservatori. Un osservatore è un nodo che segnala anche quello che sente tramite MQTT, via Wi-Fi o internet. La segnalazione va in una sola direzione: nulla torna indietro sulla mesh. Un ripetitore (un nodo che inoltra i messaggi) con firmware osservatore continua a ripetere come prima.

Gli osservatori in tutta Europa segnalano al [MeshCore Analyzer](https://meshcore-analyzer.eu/) su mqtt.meshcore-analyzer.eu. L'Analyzer legge anche altri broker, quindi conta anche un osservatore collegato lì. Da queste segnalazioni costruisce le mappe, le statistiche e la [lista dei canali](/guides/channels/) di questo sito.

{{< callout type="tip" >}}
La mesh non ha bisogno di niente di tutto questo. Le segnalazioni degli osservatori, l'Analyzer, queste mappe e questi strumenti passano da internet. Se manca la corrente o internet non funziona, si fermano. La mesh continua a inoltrare i messaggi via radio, attraverso ogni ripetitore ancora alimentato, come quelli a energia solare. Gli strumenti servono a vedere e pianificare la mesh, non a farla funzionare.
{{< /callout >}}
