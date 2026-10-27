---
title: Inizia subito
lead: Da una scheda nuova al tuo primo messaggio sulla mesh. Ti servono una scheda LoRa, un computer con Chrome o Edge, e un telefono o un portatile per l'app.
description: Installa MeshCore dal browser, abbina l'app, scegli il preset radio usato nella tua zona, invia il primo messaggio ed entra nel canale locale.
eyebrow: 6 passi · MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '68c89544'
  seeded: '2026-10-26'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', '36a3eba3', '6da9fd7a', 'cb5fb72e', '89626504', 'a419ce79', 'aa273b20']
---

Questi passi seguono il firmware MeshCore v1.18.0 e gli strumenti ufficiali di
ottobre 2026. I nomi dei menu nell'app possono cambiare un po' tra le versioni.

## 1. Scegli un dispositivo {#device}

Va bene qualsiasi scheda della [pagina dei dispositivi](/devices/) indicata come companion. Per
il tuo primo nodo scegli un *companion*: la radio da cui invii i messaggi. Lo abbini
al telefono o al portatile via Bluetooth o USB, oppure ne scegli uno con schermo
e tastiera propri, che funziona da solo.

Prendi la versione a 868 MHz. L'antenna in dotazione fa il suo lavoro; la
[guida alle antenne](/guides/antenna/) spiega come verificarne una.

{{< callout type="warning" >}}
Monta l'antenna prima di accendere la radio. Una radio LoRa che
trasmette senza antenna può danneggiare il proprio chip.
{{< /callout >}}

## 2. Installa il firmware {#flash}

1. Collega il dispositivo al computer con un cavo dati USB.
2. Apri il flasher web su [flasher.meshcore.io](https://flasher.meshcore.io)
   con Chrome o Edge. Usa Web Serial, che gli altri browser non hanno.
3. Scegli il tuo dispositivo, poi il firmware **Companion** per **Bluetooth** (o
   USB, se lo userai solo con il cavo del computer).
4. Avvia l'installazione. Alcune schede entrano prima in modalità aggiornamento; il flasher ti spiega
   come fare.

Usa *erase* solo per ripartire da zero: la cancellazione elimina l'identità del dispositivo
e i tuoi contatti. Per gli aggiornamenti successivi installa senza cancellare.

## 3. Installa l'app {#app}

L'app ufficiale MeshCore è disponibile per Android, iOS, Windows e macOS;
su [meshcore.io](https://meshcore.io) trovi i link a tutte le versioni. Esiste anche una
app web su [app.meshcore.nz](https://app.meshcore.nz), che funziona in Chrome o
Edge su un computer.

## 4. Abbina il tuo nodo {#pair}

Accendi il nodo, apri l'app e collegati via Bluetooth. Quando
ti chiede un PIN:

- un nodo **con** schermo mostra un PIN; inserisci quello;
- un nodo **senza** schermo usa `123456`.

Se l'abbinamento fallisce, rimuovi il dispositivo dalle impostazioni Bluetooth del telefono e
riprova. Poi dai un nome al tuo nodo. Gli altri vedono questo nome, quindi non usare
il tuo nome completo o il tuo indirizzo, a meno che tu non lo voglia.

## 5. Scegli il preset radio della tua zona {#preset}

Tutte le radio di una zona usano la stessa frequenza e le stesse impostazioni, altrimenti non
si sentono tra loro. Nelle impostazioni radio dell'app scegli il preset usato nella tua zona.
Fuori dalle zone elencate sotto, l'Europa usa **EU/UK (Narrow)**. Paesi Bassi,
Cechia, Ungheria, Slovacchia, Portogallo e Svizzera ne usano uno proprio, e
il Limburgo nei Paesi Bassi ha una variante:

{{< presets >}}

Non sei sicuro? Il tuo [gruppo locale](/community/) sa quale preset usa la tua zona.
L'app scarica questa lista dal progetto MeshCore, quindi un nuovo preset non richiede
un aggiornamento dell'app.

## 6. Saluta {#hello}

1. **Fatti conoscere.** Invia un *annuncio* dall'app. Un annuncio in "flood"
   passa attraverso i ripetitori (nodi che inoltrano i messaggi), così tutti
   sulla mesh possono aggiungerti.
   I companion non si annunciano mai da soli.
2. **Trova gli altri.** Le persone compaiono tra i tuoi contatti quando i loro annunci ti
   raggiungono. I ripetitori inviano un annuncio flood ogni 47 ore per impostazione predefinita, quindi la tua lista
   può impiegare 2 giorni a riempirsi.
3. **Invia un messaggio.** Apri un contatto e scrivi. Il primo messaggio va in flood
   sulla rete; il destinatario risponde con il percorso seguito, e i messaggi
   successivi seguono quel percorso.
4. **Entra nei canali.** Il canale **Public** è già configurato; tutto ciò che
   scrivi lì arriva a tutti sulla mesh. Aggiungi il *canale hashtag* della tua
   regione (un nome che inizia con `#`) digitandone il nome. Il tuo
   [gruppo locale](/community/) ti dirà quali canali sono attivi.

## Quando qualcosa non funziona {#troubleshooting}

**L'app non trova il mio dispositivo via Bluetooth.**
Probabilmente hai installato il companion USB. Installa di nuovo e scegli la
versione Bluetooth. Sull'Heltec V3 la piccola antenna Bluetooth integrata
ha una portata corta; tieni il telefono vicino.

**L'abbinamento continua a fallire.**
Rimuovi il dispositivo dalle impostazioni Bluetooth del telefono, riavvia il Bluetooth
e abbina di nuovo con il PIN sullo schermo o con `123456`.

**Nessuno compare tra i miei contatti.**
Controlla che il preset corrisponda alla tua zona. Invia un annuncio flood. Se non c'è nessun
ripetitore a portata, sentirai solo le radio vicine; la
[pagina della mappa](/map/) mostra dove si trovano i ripetitori.

**Un contatto risulta "visto l'ultima volta" giorni fa anche se è attivo.**
Uno dei due nodi ha l'ora sbagliata. Un companion prende l'ora dal
tuo telefono; i ripetitori e i room server (nodi che conservano i messaggi per un
gruppo) hanno bisogno che il proprietario la imposti.

**Il flasher non riesce ad aprire la porta seriale su Linux.**
Il tuo utente deve avere accesso alla porta, per esempio con
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, oppure facendo parte del gruppo `dialout`.

**Qualcos'altro.** Le
[FAQ di MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
trattano molti altri problemi.
