---
title: Cos'è MeshCore?
lead: MeshCore invia messaggi di testo via radio, da nodo a nodo. Funziona senza internet e senza abbonamento.
description: 'Cosa MeshCore è e cosa non è: la mesh, companion, ripetitori e room server, instradamento, cifratura e la banda 868 MHz in Europa.'
eyebrow: MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '33e571f0'
  seeded: '2026-10-26'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['a3a6c1ff', '007314d2', 'f1f23981', '493b444f', '429f699c', 'f8008f48', '655373a9']
---

MeshCore è un software libero per piccole radio LoRa. LoRa è una tecnica radio
che trasmette pochi dati a grande distanza, con pochissima energia. Una radio con MeshCore
si chiama *nodo*. Abbinata all'app sul tuo telefono o portatile, oppure con il suo
schermo e la sua tastiera, invia testo a persone a chilometri di distanza. In mezzo non c'è nessun ripetitore telefonico, router o gestore.

MeshCore invia solo brevi messaggi di testo: niente voce, foto o traffico
internet.
Un messaggio può impiegare qualche secondo, e se arriva dipende dai
ripetitori intorno a te. Non sostituisce i servizi di emergenza: in caso di
emergenza, chiama il 112.

Il software è open source, sviluppato su
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) con licenza
MIT.

## La mesh in un minuto {#mesh}

Una radio LoRa copre qualche chilometro in città, e molto di più da una
collina o da un tetto. Per arrivare più lontano, le radio si passano i messaggi a vicenda: questa
è una *mesh*. In MeshCore, a passare i messaggi sono radio chiamate *ripetitori*. Un
ripetitore che sente un messaggio lo ritrasmette, così può attraversare un'intera regione.

La mesh non appartiene a nessuno. Ogni nodo e ogni ripetitore sono di qualcuno della
comunità. La mesh vale quanto i ripetitori che le persone installano.

## I 3 tipi di nodo {#roles}

Scegli il tipo di un nodo quando lo flashi. Il tuo primo nodo è un companion.

**Companion.** La tua radio personale. Si abbina all'app MeshCore sul tuo telefono o
portatile tramite Bluetooth o USB; alcuni hanno schermo e tastiera propri. Nell'app
leggi e scrivi. Il companion conserva i tuoi contatti e i tuoi canali,
e i messaggi arrivati mentre l'app non era collegata. Un companion non inoltra messaggi per gli altri.

**Ripetitore.** Una radio collocata in alto che inoltra i messaggi di tutti. La maggior parte
funziona a energia solare. Ne serve uno tuo solo dove la mesh non arriva
ancora. Non ha un'app propria. Lo configuri tramite USB, oppure
accedi con una password e lo gestisci via radio. La
[guida ai ripetitori](/repeater-guide/) spiega come fare.

**Room server.** Una piccola bacheca sulla mesh. Quando accedi, ricevi
i post persi mentre eri fuori portata, fino agli ultimi 32. Un gruppo locale
ne usa uno per gli avvisi.

## Come un messaggio trova la strada {#routing}

Ogni nodo ha una chiave segreta e una chiave pubblica. La chiave pubblica è la sua identità. Un nodo
si fa conoscere con un *annuncio*: un pacchetto firmato con il suo nome e, se
vuoi, la sua posizione. Una persona compare tra i tuoi contatti dopo che uno dei suoi
annunci ti ha raggiunto, oppure quando scansioni il suo codice QR. L'app ha un pulsante per inviare il tuo.

Il tuo primo messaggio a un contatto parte come *flood*. Ogni ripetitore che
lo sente lo inoltra una volta, e lungo la strada aggiunge il proprio ID breve. La risposta
riporta indietro quella lista di ID. Da quel momento i tuoi messaggi a quel contatto
seguono il percorso registrato, e trasmettono solo i ripetitori che ne fanno parte. Quando il percorso
si interrompe, l'app fa di nuovo un flood.

I messaggi a un canale non hanno un indirizzo unico, quindi vanno sempre in flood.
I ripetitori ricordano cosa hanno inoltrato di recente e scartano le copie che arrivano
di nuovo per un'altra strada. Un messaggio può attraversare fino a 64 ripetitori, o 32 dove il preset usa ID
a 2 byte.

## Cifratura e privacy {#encryption}

I tuoi messaggi diretti sono cifrati end-to-end: solo tu e l'altra persona
potete leggerli. Un ripetitore vede a chi è destinato un pacchetto solo come indizio di 1 byte.

I canali sono cifrati con una chiave condivisa, quindi chi può leggerli dipende da chi
possiede quella chiave:

- **Public** è configurato su ogni companion. La sua chiave è pubblicata, quindi chiunque
  può leggerlo.
- I **canali hashtag**, come `#utrecht`, ricavano la chiave dal loro nome.
  Chiunque conosca il nome può entrare, quindi considerali pubblici anche loro.
- I **canali privati** usano una chiave casuale che condividi tu stesso, per esempio
  come codice QR.

Gli annunci sono firmati ma non cifrati. Il nome del tuo nodo, e la sua posizione se
la condividi, sono visibili a chiunque sia in portata. Scegli un nome che dica solo
quello che vuoi.

## La banda 868 MHz in Europa {#band}

In Europa, MeshCore usa una piccola parte della banda 868 MHz che chiunque può usare
senza licenza. Il suo preset radio europeo, EU/UK (Narrow), si trova a
869.618 MHz su un canale di 62.5 kHz. Rientra nella sotto-banda
869.40-869.65 MHz, che consente fino a 500 mW e.r.p. Un dispositivo può trasmettere lì al massimo il 10%
del tempo. La
[sezione legale della guida ai ripetitori](/repeater-guide/#legal) riporta i dettagli
e i limiti per ogni paese.

Tutti in una zona usano lo stesso preset, altrimenti le radio non si sentono
tra loro. Alcuni paesi e regioni usano una variante: il tuo
[gruppo locale](/community/) sa quale.

## A cosa serve {#uses}

- Restare in contatto in escursione, in mare e ai festival dove la rete mobile
  è sovraccarica o assente.
- Un canale di riserva per famiglia o vicini quando la corrente o le reti mobili
  non funzionano.
- Chat locale su radio che le persone possiedono in prima persona.
- Sperimentare con radio, antenne, energia solare e software open source.
