---
title: Rendi la mesh più resistente
lead: La mesh nella tua zona è lenta o piena di messaggi spazzatura? Scopri la causa, attiva sul ripetitore l'impostazione che la ferma e avvisa il tuo gruppo locale.
description: 'Flood e spam su una mesh MeshCore: come riconoscere ogni tipo, quale impostazione del ripetitore aiuta, come vedere un flood e come trovarne l''origine.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-10-31'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

I messaggi arrivano in ritardo o non arrivano affatto? Public si riempie di
spazzatura? Si tratta di un flood: più traffico di quanto la mesh riesca a
gestire, inviato per errore o di proposito. Cerca nelle tabelle qui sotto
quello che vedi. Ogni riga indica l'impostazione che lo ferma. Attivala sul
tuo ripetitore, il nodo che inoltra i messaggi. Poi avvisa il tuo
[gruppo locale](/community/), così anche i ripetitori intorno a te fanno lo
stesso. Ogni ripetitore che scarta un flood lascia tempo di trasmissione a
tutti gli altri.

## Flood per errore {#mistake}

Un flood per errore parte da un nodo il cui proprietario non sa di
causarlo. Finisce quando lo scopre. Nelle tabelle qui sotto, un annuncio è
il saluto che un nodo invia perché gli altri possano trovarlo.

Le impostazioni nelle tabelle derivano da ciò che fa il firmware. Non tutte
hanno già fermato un flood su una mesh reale.

{{< callout type="warning" >}}
Alcune impostazioni di questa pagina richiedono il firmware DMC. **MeshCore**
1.18.0 standard ha le regioni, i limiti di hop `flood.max.*`, il
rilevamento dei loop e il duty cycle. Il filtro dei pacchetti, cioè le
regole con cui il tuo ripetitore scarta la spazzatura, arriva con il
**firmware DMC** di
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Lo stesso
vale per il gating del duty cycle e per il filtro del companion. Questa
pagina segue la build di sviluppo DMC 1.18.0 `ecfb2d4` del 19 ottobre 2026;
la pagina sul [filtro dei pacchetti](/guides/filter/#firmware) spiega dove
trovarla.
{{< /callout >}}

| Cosa vedi | Di cosa si tratta | Cosa aiuta |
| --- | --- | --- |
| Richieste ai ripetitori da un solo nodo, giorno e notte, e una mesh che resta lenta per giorni | Una domotica o un bot che chiede troppo spesso lo stato ai ripetitori | `filter on`. Il filtro dei pacchetti lascia quindi passare 5 richieste al minuto. Avvisa il proprietario. |
| Lo stesso tipo di messaggio su un canale, ogni minuto | Un bot che pubblica troppo spesso | [Blocca il canale](/guides/filter/#channel) o [rallenta il mittente](/guides/filter/#sender). Avvisa il proprietario. |
| Messaggi illeggibili su Public e su altri canali | Un nodo con firmware difettoso o impostazioni radio sbagliate | `filter malformed on` li scarta su Public. Avvisa il proprietario. |
| L'annuncio di uno stesso nodo ogni pochi minuti | Un nodo impostato per inviare annunci troppo spesso | `filter advert 24` lascia passare l'annuncio di ogni nodo una volta al giorno. `set flood.max.advert 3` tiene gli annunci entro 3 hop. |
| Messaggi da molto lontano, con regioni che qui non c'entrano | Un bridge che collega più mesh via internet | `set flood.max.unscoped 1`, e inserisci il tuo ripetitore solo nelle [regioni che serve](/guides/settings/#traffic). |
| Lo stesso messaggio passa più e più volte, con l'ID del tuo ripetitore nel percorso più di una volta | Un ripetitore che modifica i pacchetti e li inoltra, così finiscono in loop | Il rilevamento dei loop è impostato su `minimal` di default. Con `set loop.detect moderate` il ripetitore scarta un loop prima. |

## Flood intenzionali {#purpose}

Alcuni flood sono spam: spazzatura inviata apposta per intasare la mesh. Il
mittente cambia nomi, chiavi e percorsi, quindi nessuna singola regola
ferma il flood.

| Cosa vedi | Di cosa si tratta | Cosa aiuta |
| --- | --- | --- |
| Tanti nodi nuovi con nomi casuali, ognuno con una chiave nuova | Annunci falsi | `filter rate 04 5 60` lascia passare 5 annunci al minuto. `filter advert` non aiuta: ogni annuncio arriva da una [chiave nuova](#forged). |
| Messaggi con testo illeggibile da mittenti inventati, spesso datati più di un anno fa | Spam sui canali | `filter malformed on` li scarta su Public. `filter age 60` scarta quelli con data vecchia su Public e sui [canali sorvegliati](/guides/filter/#settings). |
| Fino a 200 messaggi diretti al minuto verso nodi che non esistono, senza conferme di ritorno | Un flood di messaggi diretti | `filter rate 02 5 60`. La tua app non mostra questi messaggi; un observer sì. |
| Raffiche di richieste da un nodo verso decine di altri | Spam di richieste | Con `filter on`, il filtro dei pacchetti lascia passare 5 richieste al minuto. |
| Un messaggio torna 10-20 minuti dopo, con un percorso quasi identico | Replay: una copia inviata di nuovo | Un ripetitore ricorda gli ultimi 160 pacchetti che ha visto, quindi su una mesh trafficata una copia successiva passa di nuovo. `filter age` scarta un messaggio di gruppo più vecchio di quanto consenti. |
| Messaggi da Public inviati di nuovo con un mittente inventato, a volte con una data vecchia | Spam di eco | `filter age 60`. `filter malformed on` scarta anche una data sbagliata di oltre una settimana. |
| Un messaggio ogni pochi secondi su più canali, ognuno da un nome nuovo, con domande qualunque | Un'ondata di bot | `filter rate 05 10 60`, e [blocca i canali](/guides/filter/#channel) che nella tua zona nessuno usa. Ogni nome è nuovo, quindi le [regole sul mittente](#forged) non lo colgono. |

## Cosa ha funzionato {#worked}

I gruppi locali hanno fermato dei flood con questi passi:

1. **Avvisa il proprietario.** Un flood per errore finisce quando il
   proprietario lo scopre. Mandagli un messaggio cordiale.
2. **Non reagire sulla mesh.** Una risposta mostra allo spammer che lo spam
   funziona.
3. **Chiedi degli observer.** Un observer è un nodo che riporta via MQTT
   ogni pacchetto che sente. Più observer ci sono intorno a te, prima vedi
   da dove entra un flood. Trasforma il tuo ripetitore in un observer con
   [MQTT sul tuo observer](/guides/mqtt/).
4. **Trova l'origine.** Gli observer collocano il mittente in una zona.
   Per l'ultimo chilometro servono persone a piedi con una radio. Vedi
   [Trova l'origine](#source).
5. **Mobilita il tuo gruppo locale.** Un ripetitore con le impostazioni
   giuste aiuta. Tutti i ripetitori della zona insieme fermano un flood. Il
   tuo [gruppo locale](/community/) convince ogni proprietario ad attivare
   l'impostazione.

## Mittenti e percorsi inventati {#forged}

Il mittente scrive queste parti di un pacchetto, e niente le controlla:

- **Il nome del mittente.** In un messaggio di canale il nome fa parte del
  testo. Chiunque abbia la chiave del canale può scrivere qualsiasi nome.
- **L'inizio del percorso.** Ogni ripetitore aggiunge il proprio ID in fondo
  al percorso. Niente controlla gli ID che c'erano prima, quindi un mittente
  può iniziare il percorso con ID inventati. La fine del percorso è reale.

{{< forged-path >}}

Per questo `filter sender` e `filter path` fermano un mittente solo finché
non cambia nome o percorso. Un [blocco del percorso](/guides/filter/#path)
scarta anche il traffico reale del ripetitore il cui ID vi compare. I limiti
di frequenza, i limiti di hop, i controlli sull'età e sui messaggi
malformati, i blocchi dei canali, le regioni e il duty cycle continuano a
funzionare.

## Impostazioni per ogni flood {#always}

Queste valgono qualunque cosa intasi la mesh:

- **Duty cycle al 10%.** Così il tuo ripetitore non trasmette mai più di
  quanto consente la legge, qualunque cosa arrivi. Ne parla la
  [guida al ripetitore](/repeater-guide/#duty-cycle).
- **Regioni e limiti di hop.** Una regione è l'area in cui resta un
  messaggio. Un ripetitore inoltra solo i messaggi delle regioni che ha, e
  `flood.max.*` tiene il traffico vicino. Trovi entrambi in
  [Riduci il traffico](/guides/settings/#traffic).
- **Il filtro dei pacchetti per un ripetitore trafficato.** Le
  [impostazioni pronte](/guides/filter/#busy) dimezzano messaggi di gruppo
  e annunci. Provale prima in [dry-run](/guides/filter/#dryrun): in questa
  modalità il filtro conta solo ciò che scarterebbe.
- **Il filtro del companion, nel firmware DMC.** Il tuo companion, il nodo
  da cui invii i messaggi, tiene la spazzatura fuori dalla tua app. Nasconde
  i messaggi difettosi e vecchi, e quelli da un ripetitore, un mittente o
  una parola che blocchi. Una regola su mittente o parola
  nasconde il messaggio solo a te; gli altri lo ricevono comunque.

### Gating del duty cycle {#gate}

Nel firmware DMC, il tuo ripetitore può dare priorità alla propria regione
quando è sotto carico. Quando ha trasmesso per più del 35% dell'ultimo minuto,
smette di inoltrare i messaggi senza regione. Se resta sotto carico, scarta
poi la regione più ampia, un livello alla volta. La sua regione passa
sempre. Funziona solo se sul tuo ripetitore hai impostato delle regioni.
Attivalo e controllalo:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Ciò che scarta non compare in `filter stats`. Quando il ripetitore torna
tranquillo, le regioni tornano, a cominciare dalla più interna.

## Vedere un flood {#see}

La tua app mostra solo ciò che arriva a te. Solo un observer sente un flood
di messaggi diretti verso nodi che non esistono. Ogni observer invia i dati
al [MeshCore Analyzer](https://meshcore-analyzer.eu/), dove chiunque può
vederli. Trasforma il tuo ripetitore in un observer con
[MQTT sul tuo observer](/guides/mqtt/).

Sull'Analyzer, guarda ogni copia di uno stesso pacchetto. Di solito il suo
percorso mostra da dove è arrivato. Chi fa flood può iniziare il percorso
con [ID inventati](#forged), quindi i primi ID non ti dicono nulla. Però ogni
copia porta lo stesso inizio inventato. La copia con il percorso più breve
ha attraversato meno ripetitori reali, quindi è stata sentita più vicino al
mittente.

{{< copies >}}

Sul tuo ripetitore, `filter stats` mostra cosa ha scartato il filtro dei
pacchetti. `filter stats top` mostra il primo byte degli ID dei nodi
responsabili della maggior parte degli scarti. Molti nodi condividono quel
byte, quindi restringe la ricerca ma non identifica il mittente.

## Trova l'origine {#source}

Quando un flood continua a tornare:

1. **Segui i percorsi.** Leggi un percorso dalla fine: gli ultimi ID sono i
   ripetitori attraversati dal flood. Il primo ID reale è vicino
   all'origine; gli ID che lo precedono possono essere [inventati](#forged).
2. **Restringi la zona.** Più observer che sentono lo stesso pacchetto
   collocano il mittente in una zona. Il
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) la calcola a
   partire dai ripetitori che l'hanno sentito.
3. **Percorri a piedi l'ultimo chilometro.** I ripetitori sentono l'origine
   solo al limite della loro portata, quindi per l'ultimo tratto servono
   persone a piedi. [Mesh-Hunter](https://mesh-hunter.eu/) si abbina al tuo
   companion e registra ogni pacchetto che sente con la tua posizione GPS.
   Con più persone a piedi nello stesso momento, la trovi prima.
4. **Avvisa il tuo [gruppo locale](/community/).** Il gruppo vede una parte
   più ampia della mesh, decide i passi successivi e contatta chi fa flood
   di proposito.

## Aggiungi ciò che hai visto {#add}

Ti ha colpito un flood che non è
in queste tabelle? Un'impostazione ne ha fermato uno? Raccontacelo su
[Discord](https://discord.meshcore-info.eu/): cosa hai visto e cosa hai
attivato. Noi lo aggiungiamo alla pagina.
