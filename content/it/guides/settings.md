---
title: Impostazioni consigliate
layout: settings
lead: Il preset radio usato nella tua zona e le impostazioni che i tuoi vicini hanno cambiato. Scegli il tuo paese, imposta il preset e copia i comandi.
description: Il preset radio MeshCore per ogni zona d'Europa, e le impostazioni di ripetitore e companion che i gruppi locali hanno cambiato rispetto ai valori predefiniti, con i comandi.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '9547ba62'
  seeded: '2026-10-26'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', '43cde8b4']
---

Ogni zona qui sotto usa un proprio preset radio, oppure modifica alcuni valori predefiniti di MeshCore. Tutto ciò che non è elencato resta al valore predefinito, quindi cambi solo quello che la tua zona ha cambiato. Un ripetitore inoltra i messaggi per tutti; un companion è il nodo da cui scrivi, abbinato al tuo telefono o portatile via Bluetooth o USB, oppure dotato di un proprio schermo.

La [guida ai ripetitori](/repeater-guide/#config) mostra come arrivare alla riga di comando del tuo ripetitore, e nella [console seriale](/firmware/console/) di questo sito digiti i comandi tu stesso. Sotto ogni zona puoi anche inviare le sue impostazioni via USB. La guida elenca anche i [limiti di legge](/repeater-guide/#legal) sugli 868 MHz.

## Riduci il traffico {#traffic}

Queste impostazioni valgono per ogni zona. Ogni ripetitore inoltra ogni messaggio flood che sente. Un tuo messaggio costa una trasmissione, più una per ogni ripetitore che lo sente. Con il duty cycle del 10% un ripetitore può inviare circa 680 pacchetti l'ora, e tutti quelli intorno condividono quel numero. Un messaggio che viaggia più lontano del necessario ne consuma una parte.

**Invia alla regione più piccola che raggiunge le persone a cui scrivi.** Le regioni sono annidate: un paese, una provincia, un gruppo locale, ognuno con il proprio codice, come `nl`, `nl-ov` e `nl-ov-zwo`. Un messaggio per `nl-ov-zwo` resta tra i ripetitori di quel gruppo. Metti ogni ripetitore solo nelle regioni che serve; il tuo [gruppo locale](/community/) sa quali sono.

**Limita ciò che il tuo ripetitore inoltra.** Due impostazioni tengono vicino a casa il traffico che non ha bisogno di viaggiare lontano:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: gli annunci, che presentano un nodo alla mesh, viaggiano al massimo per 3 hop.
- `flood.max.unscoped 1`: un messaggio senza regione passa al massimo per un ripetitore.
