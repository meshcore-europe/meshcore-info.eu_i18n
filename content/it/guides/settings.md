---
title: Impostazioni consigliate
layout: settings
lead: Il preset radio della tua zona e le impostazioni che hanno cambiato i tuoi vicini. Scegli il tuo paese, imposta il preset e copia i comandi.
description: Il preset radio di MeshCore per ogni zona d'Europa e le impostazioni di ripetitore e companion che i gruppi locali hanno cambiato rispetto ai valori predefiniti, con i comandi.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-10-31'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Ogni zona qui sotto usa un proprio preset radio, oppure cambia alcuni
valori predefiniti di MeshCore. Tutto ciò che non compare nell'elenco resta al
valore predefinito: cambi quindi solo ciò che ha cambiato la tua zona. Un
ripetitore inoltra i messaggi per tutti. Un companion è il nodo da cui scrivi i
messaggi: lo abbini al telefono o al portatile via Bluetooth o USB, oppure ha
uno schermo proprio.

Nella [guida al ripetitore](/repeater-guide/#config) trovi come raggiungere la
riga di comando del tuo ripetitore. Nella [console seriale](/firmware/console/)
di questo sito scrivi tu stesso i comandi. Sotto ogni zona puoi anche inviarne
le impostazioni via USB. La guida riporta anche i [limiti di legge](/repeater-guide/#legal)
sugli 868 MHz.

## Limitare il traffico {#traffic}

Queste impostazioni valgono per ogni zona. Ogni ripetitore inoltra ogni
messaggio flood che riceve. Un tuo messaggio costa una trasmissione, più una
per ogni ripetitore che lo riceve. Con il duty cycle del 10% un ripetitore può
inviare circa 680 pacchetti all'ora. Tutti quelli nei dintorni si dividono
questa quota. Un messaggio che va più lontano del necessario ne consuma una
parte.

**Invia alla regione più piccola che raggiunge le persone a cui scrivi.**
Le regioni sono annidate: un paese, una provincia, un gruppo locale. Ognuna ha
un proprio codice, come `nl`, `nl-ov` e `nl-ov-zwo`. Un messaggio per
`nl-ov-zwo` resta tra i ripetitori di quel gruppo. Un ripetitore inoltra solo
le regioni che ha configurato: avere `nl` non basta perché inoltri `nl-ov`. Metti
ogni ripetitore in tutte le regioni che serve, e solo in quelle. Il tuo
[gruppo locale](/community/) sa quali sono.

**Limita ciò che il tuo ripetitore inoltra.** Due impostazioni tengono vicino
a casa il traffico che non ha bisogno di andare lontano:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: gli annunci, che presentano un nodo alla mesh,
  percorrono al massimo 3 hop.
- `flood.max.unscoped 1`: un messaggio senza regione attraversa al massimo un
  ripetitore.
