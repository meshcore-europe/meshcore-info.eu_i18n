---
title: Mappe di copertura
layout: map
lead: Scopri fin dove arriva la mesh, dove si trovano i nodi e come viaggiano i messaggi. Queste mappe sono gestite da community di tutta Europa.
description: Mappe MeshCore in tempo reale, mappe di copertura e analizzatori di pacchetti per l'Europa e per i singoli paesi.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '550066cc'
  seeded: '2026-10-26'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['550066cc']
---

Un nodo compare su queste mappe quando il suo proprietario lo pubblica, oppure quando lo sente un *osservatore*: un nodo che inoltra via MQTT quello che riceve. Per questo nessuna mappa è completa. Gli analizzatori mostrano il traffico ricevuto dai loro osservatori: pacchetti, percorsi e attività dei canali. I messaggi diretti restano cifrati, quindi nessun analizzatore ne mostra il contenuto.

Queste mappe hanno bisogno di internet; la mesh no. [Perché](/network/)

Gestisci un ripetitore, cioè un nodo che inoltra i messaggi? Imposta la sua posizione con `set lat` e `set lon`, così le mappe possono collocarlo. La [guida ai ripetitori](/repeater-guide/#config) spiega come fare.
