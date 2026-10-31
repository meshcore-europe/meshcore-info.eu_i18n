---
title: Console seriale
layout: console
lead: Invia comandi al tuo ripetitore dal browser, tramite USB.
description: Configura un ripetitore, un room server o un sensore MeshCore tramite USB da Chrome, Edge o Opera, con una console seriale nel browser e senza installare nulla.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-31'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Un ripetitore (inoltra i messaggi), un room server (conserva i post di un
gruppo) o un sensore (invia le sue letture) non ha un'app. Per configurarlo,
quindi, scrivi i comandi tramite USB. Collega il tuo nodo al computer, apri
questa pagina in Chrome, Edge o Opera su un computer e scegli la porta del tuo
nodo. Per prima cosa la console invia `get role` e `ver`, così capisce che tipo
di nodo hai. Entrambi i comandi si limitano a leggere. Poi la console mostra le
risposte del tuo nodo. Scrivi un comando come `get name` e premi Invio. Mentre
scrivi, la console ti propone i comandi che il tuo nodo conosce. Con Tab
inserisci il primo.

Un companion, il nodo da cui invii i messaggi, comunica invece con l'app tramite USB. La sua riga di comando si trova
nell'app MeshCore, dalla versione 1.50 in poi.
