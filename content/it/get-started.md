---
title: Primi passi
lead: Da una scheda nuova al tuo primo messaggio sulla mesh. Ti servono una scheda LoRa, un computer con Chrome o Edge e un telefono o un portatile per l'app.
description: Installa MeshCore dal browser, abbina l'app, scegli il preset radio della tua zona, invia il primo messaggio ed entra nel canale locale.
eyebrow: 6 passaggi · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-10-31'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Questi passaggi si basano sul firmware MeshCore v1.18.0 e sugli strumenti
ufficiali di ottobre 2026. I nomi dei menu nell'app possono cambiare un po'
da una versione all'altra.

## 1. Scegli un dispositivo {#device}

Va bene qualsiasi scheda della [pagina dei dispositivi](/devices/) che indica
companion. Come primo nodo scegli un *companion*: la radio da cui invii i
messaggi. Lo abbini al telefono o al portatile via Bluetooth o USB. In
alternativa ne scegli uno con schermo e tastiera propri, che funziona da solo.

Prendi la versione a 868 MHz. L'antenna in dotazione va bene; la
[guida alle antenne](/guides/antenna/) spiega come verificarne una.

{{< callout type="warning" >}}
Collega l'antenna prima di accendere la radio. Se una radio LoRa trasmette
senza antenna, può danneggiare il proprio chip.
{{< /callout >}}

## 2. Installa il firmware {#flash}

1. Collega il dispositivo al computer con un cavo USB dati.
2. Apri il flasher web su [flasher.meshcore.io](https://flasher.meshcore.io)
   in Chrome o Edge. Usa Web Serial, che gli altri browser non hanno.
3. Scegli il tuo dispositivo, poi il firmware **Companion** per **Bluetooth**
   (oppure USB, se lo userai solo con un cavo collegato al computer).
4. Avvia l'installazione. Alcune schede devono prima entrare in modalità di
   aggiornamento; il flasher ti dice come fare.

Usa *erase* solo per ripartire da zero: la cancellazione elimina l'identità
del dispositivo e i tuoi contatti. Per gli aggiornamenti successivi installa
senza cancellare. Per conservare l'identità dopo una cancellazione, esporta
prima dall'app la chiave privata del companion e poi reimportala.

## 3. Installa l'app {#app}

L'app ufficiale MeshCore esiste per Android, iOS, Windows e macOS;
[meshcore.io](https://meshcore.io) rimanda a tutte le versioni. C'è anche
un'app web su [app.meshcore.nz](https://app.meshcore.nz), che funziona in
Chrome o Edge su un computer.

## 4. Abbina il tuo nodo {#pair}

Accendi il nodo, apri l'app e collegati via Bluetooth. Quando l'app chiede
un PIN:

- un nodo **con** schermo mostra un PIN; inserisci quello;
- un nodo **senza** schermo usa `123456`.

Se l'abbinamento non riesce, rimuovi il dispositivo dalle impostazioni
Bluetooth del telefono e riprova. Poi dai un nome al nodo. Gli altri vedono
questo nome: non usare il tuo nome completo o il tuo indirizzo, a meno che
tu non lo voglia.

## 5. Scegli il preset radio della tua zona {#preset}

Tutte le radio di una zona usano la stessa frequenza e le stesse
impostazioni, altrimenti non si sentono. Nelle impostazioni radio dell'app
scegli il preset della tua zona. Fuori dalle zone qui sotto, in Europa si
usa **EU/UK (Narrow)**. Paesi Bassi, Cechia, Ungheria, Slovacchia, Portogallo
e Svizzera hanno un preset proprio, e il Limburgo nei Paesi Bassi ne ha una
variante:

{{< presets >}}

Il tuo dispositivo non offre il preset della tua zona? Inserisci a mano i 4
valori della tabella nelle impostazioni radio dell'app: frequenza, larghezza
di banda, spreading factor e coding rate. Un nodo con valori diversi non
sente la mesh.

Hai dubbi? Il tuo [gruppo locale](/community/) sa quale preset usa la tua
zona. L'app scarica questo elenco dal progetto MeshCore, quindi un nuovo
preset non richiede un aggiornamento dell'app.

## 6. Saluta {#hello}

1. **Fatti conoscere.** Invia un *annuncio* dall'app. Un annuncio "flood"
   passa attraverso i ripetitori (nodi che inoltrano i messaggi), così
   chiunque sulla mesh può aggiungerti.
   I companion non si annunciano mai da soli.
2. **Trova gli altri.** Le persone compaiono tra i tuoi contatti quando i
   loro annunci ti raggiungono. Per impostazione predefinita i ripetitori
   inviano un annuncio flood ogni 47 ore, quindi l'elenco può impiegare 2
   giorni a riempirsi.
3. **Invia un messaggio.** Apri un contatto e scrivi. Il primo messaggio
   viaggia in flood per tutta la rete; il destinatario ti comunica il
   percorso seguito, e i messaggi successivi usano quel percorso.
4. **Entra nei canali.** Il canale **Public** è già configurato; quello che
   scrivi lì arriva a tutti sulla mesh. Aggiungi il *canale hashtag* della
   tua regione (un nome che inizia con `#`) digitandone il nome. Il tuo
   [gruppo locale](/community/) ti dirà quali canali sono attivi.

## Quando qualcosa non funziona {#troubleshooting}

**L'app non trova il mio dispositivo via Bluetooth.**
Probabilmente hai installato il companion USB. Installa di nuovo e scegli la
versione Bluetooth. Sull'Heltec V3 la piccola antenna Bluetooth integrata ha
una portata ridotta; tieni il telefono vicino.

**L'abbinamento continua a fallire.**
Rimuovi il dispositivo dalle impostazioni Bluetooth del telefono, riavvia il
Bluetooth e abbinalo di nuovo con il PIN sullo schermo o con `123456`.

**Non compare nessuno tra i miei contatti.**
Controlla che il preset corrisponda alla tua zona. Invia un annuncio flood.
Se non c'è un ripetitore a portata, sentirai solo le radio vicine; la
[pagina della mappa](/map/) mostra dove si trovano i ripetitori.

**Un contatto risulta "visto l'ultima volta" giorni fa, anche se è attivo.**
Uno dei due nodi ha l'ora sbagliata. Un companion prende l'ora dal tuo
telefono. Nei ripetitori e nei room server (nodi che conservano i messaggi
per un gruppo) invece l'ora la deve impostare il proprietario.

**Un messaggio diretto non arriva mai.**
Dovete avervi a vicenda tra i contatti. Un nodo scarta i messaggi di chi
non conosce, senza avvisare il mittente. Invia un annuncio flood e chiedi
all'altra persona di inviarne uno anche lei. Controlla nell'app che aggiunga
in automatico i nuovi contatti; l'app aggiunge solo i nodi entro il suo
limite di hop.

**I vecchi contatti funzionano, i nuovi non si collegano mai.**
Il primo messaggio viaggia in flood, e un ripetitore lo inoltra solo se ha
la regione del messaggio. I messaggi successivi seguono un percorso appreso,
che nessun controllo di regione blocca. Chiedi al tuo
[gruppo locale](/community/) quali regioni hanno i ripetitori intorno a te, e
controlla [le impostazioni per la tua zona](/guides/settings/#traffic).

**L'app non si collega più al tuo companion.**
Alcune schede hanno un pulsante utente, per esempio alcune schede RAK e
l'Heltec T114. Tienilo premuto nei primi 8 secondi dopo l'avvio della
scheda. Il companion apre una console di emergenza via USB. Nella console su
[flasher.meshcore.io](https://flasher.meshcore.io), `set pin <pin>` imposta
un nuovo PIN Bluetooth ed `erase` cancella il dispositivo.

**Su Linux il flasher non riesce ad aprire la porta seriale.**
Il tuo utente deve avere accesso alla porta, per esempio con
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, oppure far parte del gruppo
`dialout`.

**Altro.** Le
[FAQ di MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
trattano molti altri problemi.
