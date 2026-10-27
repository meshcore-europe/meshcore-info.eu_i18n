---
title: Comandi CLI
layout: cli
lead: Tutti i comandi del tuo ripetitore, room server, sensore o companion, raggruppati per quello che vuoi fare. Leggi cosa fa ciascuno e il valore con cui parte, inserisci il tuo e copialo.
description: 'Tutti i comandi del firmware MeshCore 1.18.0 per ripetitori, room server, sensori e companion, raggruppati per attività: cosa fanno, il valore con cui parte il firmware e quali nodi li hanno.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-26'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
---

Questi comandi seguono il firmware MeshCore 1.18.0, letti dal codice sorgente del
firmware. Un comando aggiunto in una versione recente indica quale versione richiede. Un
ripetitore inoltra i messaggi, un room server conserva i post di un gruppo, un sensore
riporta le letture. Room server, sensori e companion condividono molti comandi.
Ogni comando indica quali nodi lo hanno. "Quale nodo?" mostra solo i comandi
del tuo.

Su un ripetitore, room server o sensore li digiti via USB dal tuo
computer, per esempio nella [console seriale](/firmware/console/) di questo sito. L'app MeshCore li invia attraverso la mesh. La
[guida al ripetitore](/repeater-guide/#config) mostra entrambi i modi.

Dalla 1.18 anche un companion (il nodo da cui scrivi i messaggi, abbinato al tuo telefono o portatile, oppure
con il proprio schermo) ha una riga di comando.
Apri Command Line nelle impostazioni dell'app MeshCore, versione 1.50 o
successiva. Un contatto con il permesso Remote CLI può inviare al tuo companion gli
stessi comandi attraverso la mesh. Questo include i comandi WiFi e PIN.

Il valore con cui parte un comando è quello del ripetitore. Un room server, un sensore o un
companion possono partire da un altro valore. Un comando che ha solo un companion mostra il proprio.
