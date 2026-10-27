---
title: Console seriale
layout: console
lead: Invia comandi al tuo ripetitore dal browser, via USB.
description: Configura un ripetitore, un room server o un sensore MeshCore via USB da Chrome, Edge o Opera, con una console seriale nel browser. Nessun programma da installare.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-26'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: 'a2fe0704'}
  sections: ['c33167ce']
---

Un ripetitore (inoltra i messaggi), un room server (conserva i post di un gruppo) o un sensore (riporta le misurazioni) non ha un'app, quindi lo configuri scrivendo comandi via USB. Collega il tuo nodo al computer, apri questa pagina in Chrome, Edge o Opera su un computer e scegli la porta del tuo nodo. La console invia prima `get role` e `ver`, così sa che cos'è il tuo nodo. Entrambi si limitano a leggere. Poi mostra quello che dice il tuo nodo: scrivi un comando come `get name` e premi Invio. Mentre scrivi, ti suggerisce i comandi che il tuo nodo capisce, e con Tab inserisci il primo.

Un companion, il nodo da cui invii i messaggi, parla invece con l'app via USB. La sua riga di comando si trova nell'app MeshCore, versione 1.50 o successiva.
