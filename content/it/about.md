---
title: Che cos'è MeshCore?
lead: MeshCore invia messaggi di testo via radio, da nodo a nodo. Funziona senza internet e senza abbonamento.
description: 'Che cosa è MeshCore e che cosa non è: la mesh, companion, ripetitori e room server, l''instradamento, la cifratura e la banda 868 MHz in Europa.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '78bc31e8'
  seeded: '2026-10-31'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['aa768ac3', 'c9b24089', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '655373a9', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b9fc8810', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '0eb54b47', '02f1fe2f', 'e6b5b258']
---

MeshCore è un software gratuito per piccole radio LoRa. LoRa è una tecnica radio
che trasmette pochi dati a grande distanza, con pochissima energia. Una radio con
MeshCore si chiama *nodo*. Lo abbini all'app sul telefono o sul portatile, oppure
lo usi con il suo schermo e la sua tastiera. Così mandi messaggi di testo a persone
a chilometri di distanza. In mezzo non ci sono antenne di operatori, router o provider.

Il software è open source. Lo sviluppano su
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) con licenza
MIT.

## Che cosa non è MeshCore {#not}

Sei alle prime armi con la radio? Ecco le cose che la gente si aspetta più spesso
da MeshCore, e che MeshCore non fa.

- **Non è internet e non è un telefono.** MeshCore invia brevi messaggi di testo,
  lunghi più o meno come un SMS sul telefono. Niente voce, foto, video o siti
  web, e non puoi raggiungere un normale numero di telefono.
- **Non è un servizio di emergenza.** Nessun servizio di emergenza ascolta la
  mesh, e nessuno garantisce che qualcuno legga il tuo messaggio. In caso di
  emergenza, chiama il 112.
- **Non è immediato e non arriva ovunque.** Un messaggio salta da una radio
  all'altra e può metterci qualche secondo, oppure non arrivare affatto. Se passa
  o no dipende dai ripetitori intorno a te, dall'altezza, dagli edifici e dalla
  tua antenna. Una piccola radio in casa spesso non raggiunge nessuno. Un
  ripetitore su un tetto arriva a chilometri di distanza.
- **Non è un servizio che qualcuno gestisce per te.** Non c'è un provider, non
  c'è assistenza e nessuno promette copertura. La mesh esiste dove le persone
  della community hanno installato ripetitori, e da nessun'altra parte.
- **Non tutto è privato.** I messaggi diretti sono cifrati. Public e i canali
  hashtag invece li può leggere chiunque. Il nome del tuo nodo e la posizione
  che condividi li vedono tutti quelli nel raggio di ricezione.
  Gli [observer](/network/) riportano su mappe pubbliche quello che ricevono. La
  [sezione sulla cifratura](#encryption) spiega che cosa resta privato.
- **Non è illimitato.** Tutti in una zona condividono un solo canale radio, e le
  regole della [banda 868 MHz](#band) limitano quanto a lungo ogni radio può
  trasmettere. Ogni messaggio toglie tempo di trasmissione a tutti gli altri.
  Per questo bot, annunci frequenti e messaggi di prova rallentano la mesh per
  tutti.
- **Non è Meshtastic.** Meshtastic è un sistema diverso che gira più o meno
  sulle stesse schede. I due sistemi non possono comunicare tra loro.

## La mesh in un minuto {#mesh}

Una radio LoRa arriva a qualche chilometro in città, e molto più lontano da una
collina o da un tetto. Per andare oltre, le radio si passano i messaggi a
vicenda: questa è una *mesh*. In MeshCore a passare i messaggi sono radio dette
*ripetitori*. Un ripetitore che riceve un messaggio lo ritrasmette. Così il
messaggio può attraversare un'intera regione.

La mesh non appartiene a nessuno. Ogni nodo e ogni ripetitore è di qualcuno
della community. La mesh arriva fin dove arrivano i loro ripetitori.

## I 3 tipi di nodo {#roles}

Scegli il tipo di un nodo quando ci installi il firmware. Il tuo primo nodo è un
companion.

**Companion.** La tua radio personale. Si abbina all'app MeshCore sul telefono o
sul portatile via Bluetooth o USB. Alcuni hanno schermo e tastiera propri. Nell'app
leggi e scrivi. Il companion conserva i tuoi contatti e canali, e i messaggi
arrivati mentre l'app non era collegata. Un companion non inoltra i messaggi degli altri.

**Ripetitore.** Una radio messa in alto che inoltra i messaggi di tutti. La
maggior parte funziona a energia solare. Te ne serve uno tuo solo dove la mesh non
arriva ancora. Non ha un'app propria. Lo configuri via USB, oppure
accedi con una password e lo gestisci via radio. La
[guida ai ripetitori](/repeater-guide/) spiega come fare.

**Room server.** Una piccola bacheca sulla mesh. Quando accedi, ricevi i post
che hai perso mentre eri fuori portata, fino agli ultimi 32. Il room server li
tiene solo in memoria, quindi un riavvio o un'interruzione di corrente li
cancella. Un gruppo locale lo usa per gli avvisi.

## Come un messaggio trova la strada {#routing}

Ogni nodo ha una chiave segreta e una chiave pubblica. La chiave pubblica è la sua identità. Un nodo
si presenta con un *annuncio*: un pacchetto firmato con il suo nome e, se vuoi,
la sua posizione. Una persona compare nei tuoi contatti dopo che ti è arrivato
uno dei suoi annunci, o quando scansioni il suo codice QR. Nell'app c'è un pulsante per inviare il tuo.

Il tuo primo messaggio a un contatto parte come *flood*. Ogni ripetitore che lo
riceve lo ritrasmette una volta, e lungo la strada aggiunge il proprio ID breve.
La risposta riporta indietro quell'elenco di ID. Da quel momento i tuoi messaggi
a quel contatto seguono il percorso registrato, e trasmettono solo i ripetitori
che ne fanno parte. Quando il percorso si interrompe, l'app manda di nuovo un flood.

I messaggi a un canale non hanno un unico destinatario, quindi vanno sempre in flood.
I ripetitori ricordano che cosa hanno inoltrato di recente e scartano le copie
che arrivano di nuovo per un'altra strada. Un messaggio può attraversare fino a 64 ripetitori, oppure 32 se il preset usa ID da
2 byte.

## Cifratura e privacy {#encryption}

I tuoi messaggi diretti sono cifrati end-to-end: solo tu e l'altra persona potete
leggerli. Un ripetitore vede il destinatario di un pacchetto solo come un indizio
da 1 byte.

I canali sono cifrati con una chiave condivisa. Chi può leggerli dipende quindi
da chi ha quella chiave:

- **Public** è già configurato su ogni companion. La sua chiave è pubblicata,
  quindi chiunque può leggerlo.
- **I canali hashtag**, come `#utrecht`, ricavano la chiave dal loro nome.
  Chiunque conosca il nome può entrare, quindi considera pubblici anche questi.
- **I canali privati** usano una chiave casuale che condividi tu, per esempio
  con un codice QR.

Gli annunci sono firmati ma non cifrati. Il nome del tuo nodo, e la sua posizione
se la condividi, li vedono tutti nel raggio di ricezione. Scegli un nome che non
dica più di quanto vuoi.

## La banda 868 MHz in Europa {#band}

In Europa MeshCore usa una piccola parte della banda 868 MHz, che chiunque può
usare senza licenza. Il suo preset radio europeo, EU/UK (Narrow), sta su
869.618 MHz con un canale da 62.5 kHz. Rientra nella sotto-banda 869.40-869.65 MHz,
che ammette fino a 500 mW e.r.p. Lì un dispositivo può trasmettere al massimo per
il 10% del tempo. La
[sezione legale della guida ai ripetitori](/repeater-guide/#legal) riporta i
dettagli e i limiti per ogni paese.

Tutti in una zona usano lo stesso preset, altrimenti le loro radio non si
sentono. Alcuni paesi e regioni usano una variante: il tuo
[gruppo locale](/community/) sa quale.

## A che cosa serve {#uses}

- Restare in contatto durante le escursioni, in mare e ai festival, dove la rete
  mobile è sovraccarica o assente.
- Un canale di riserva per la famiglia o i vicini quando manca la corrente o
  cadono le reti mobili.
- Chat locali su radio che appartengono alle persone stesse.
- Sperimentare con radio, antenne, energia solare e software open source.

## Da dove vengono i dati {#data}

La ricerca nella pagina dei [gruppi locali](/community/) trova un luogo grazie a
una copia degli elenchi gratuiti di località e codici postali di
[GeoNames](https://www.geonames.org/), con licenza
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). La copia si trova su
questo sito. La tua ricerca resta sul tuo dispositivo, e nessuna richiesta arriva
a GeoNames.
