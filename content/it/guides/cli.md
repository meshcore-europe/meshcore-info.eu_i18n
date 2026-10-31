---
title: Comandi CLI
layout: cli
lead: Tutti i comandi del tuo ripetitore, room server, sensore o companion, raggruppati in base a cosa vuoi fare. Leggi cosa fa ogni comando e il valore con cui parte, inserisci il tuo e copialo.
description: 'Tutti i comandi del firmware MeshCore 1.18.0 per ripetitori, room server, sensori e companion, raggruppati per attività: cosa fanno, il valore con cui parte il firmware e quali nodi li hanno.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-31'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Questi comandi seguono il firmware MeshCore 1.18.0 e li abbiamo ricavati dal codice sorgente del firmware. Per un comando aggiunto in una versione recente indichiamo la versione che serve. Un ripetitore inoltra i messaggi, un room server conserva i post per un gruppo, un sensore invia le sue misure. Room server, sensori e companion hanno molti comandi in comune. Per ogni comando indichiamo quali nodi lo hanno. Con "Quale nodo?" vedi solo i comandi del tuo.

Su un ripetitore, un room server o un sensore li digiti via USB dal tuo computer, per esempio nella [console seriale](/firmware/console/) di questo sito. Con l'app MeshCore li invii attraverso la mesh. La [guida al ripetitore](/repeater-guide/#config) mostra entrambi i modi.

Dalla 1.18 anche un companion ha una riga di comando. Il companion è il nodo da cui invii i messaggi, abbinato al tuo telefono o portatile, oppure con un suo schermo. Apri Command Line nelle impostazioni dell'app MeshCore, versione 1.50 o successiva. Un contatto con il permesso Remote CLI può inviare al tuo companion gli stessi comandi attraverso la mesh. Questo vale anche per i comandi WiFi e PIN.

Il valore iniziale di un comando è quello del ripetitore. Un room server, un sensore o un companion possono avere un altro valore iniziale. Un comando presente solo sul companion mostra il suo valore iniziale.
