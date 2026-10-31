---
title: Filtro pacchetti
lead: 'Impedisci al tuo ripetitore di inoltrare traffico inutile: flood da lontano, un bot che non si ferma mai, un canale rumoroso. Prova prima un''impostazione, poi attivala.'
description: 'Il filtro pacchetti del firmware ripetitore DMC: cosa scarta, configurazioni pronte per un ripetitore normale e uno molto trafficato, ogni comando del filtro con il suo valore predefinito e come vedere cosa ha scartato.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-10-31'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Un ripetitore (un nodo che inoltra i messaggi) ripete tutto ciò che sente.
Su una mesh trafficata questo include traffico inutile. Un bot scrive ogni minuto.
Un nodo invia di nuovo il suo annuncio, il saluto che permette agli altri di
trovarlo, a distanza di pochi minuti. Arrivano messaggi che hanno attraversato mezzo paese.
Ogni ripetizione toglie tempo di trasmissione a tutti quelli intorno a te.
Con il filtro pacchetti il tuo ripetitore scarta questo traffico invece di
inoltrarlo. Per capire prima cosa intasa la tua mesh, e cosa aiuta oltre al
filtro, leggi [Rendi la mesh resiliente](/guides/resilient/).

{{< callout type="warning" >}}
Il filtro pacchetti fa parte del **firmware ripetitore DMC**, la versione
ripetitore di [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore).
MeshCore standard non ha un filtro pacchetti. Ha `region denyf *` e
`set flood.max.unscoped`, descritti nella pagina [comandi CLI](/guides/cli/).
Questa guida segue la build di sviluppo 1.18.0 `ecfb2d4` del 19 ottobre 2026.
La build stabile 1.17.1 ha solo i filtri hop, rate, channel, hash e malformed.
Non ha nemmeno il dry-run.
{{< /callout >}}

## Cosa fa il filtro {#what}

Il filtro esamina solo i pacchetti che il tuo ripetitore inoltra in flood
(cioè li invia a ogni nodo a portata). Non tocca mai ciò che il tuo ripetitore
invia da sé, né i pacchetti che seguono un percorso noto verso un nodo.
Passano anche i messaggi diretti e le richieste da e verso i tuoi contatti.
Può scartare:

- pacchetti che hanno già attraversato il numero di ripetitori (hop) che
  consenti, per tipo di pacchetto;
- più pacchetti di un tipo di quanti ne consenti al minuto;
- un annuncio di un nodo che si è già annunciato nelle ultime ore;
- messaggi su un canale che blocchi;
- tutto ciò che è arrivato tramite un ripetitore che blocchi;
- messaggi di gruppo di un mittente o con una certa parola, o solo una parte di essi;
- messaggi di gruppo danneggiati, o più vecchi di quanto consenti.

Il filtro è **disattivato** finché non lo attivi. Lo configuri con dei comandi.
Puoi digitarli via USB nella [console seriale](/firmware/console/) di questo sito.
Oppure puoi inviarli dall'app MeshCore, come nella
[guida al ripetitore](/repeater-guide/#config).

## Scarica il firmware {#firmware}

Installa **DutchMeshCore Repeater** con il flasher della
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Il firmware
observer di [MQTT sul tuo observer](/guides/mqtt/) ha lo stesso filtro.

## Prima provalo {#dryrun}

In dry-run il filtro conta ogni pacchetto che scarterebbe, ma lo inoltra
comunque. Così puoi calibrare un'impostazione prima che scarti qualcosa:

```text
filter on
filter dryrun on
```

Con il dry-run attivo, la riga di stato di `filter` finisce con `(dry-run)`.
I conteggi indicano cosa avrebbe scartato. Lascialo attivo per un giorno, poi
guarda i numeri (vedi [Cosa ha scartato](#stats)). Quando i numeri ti
convincono, applicalo davvero:

```text
filter dryrun off
```

## Configurazioni consigliate {#configs}

### Un ripetitore normale {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Passano fino a 20 messaggi di gruppo al minuto e fino a 5 messaggi diretti al
minuto. I messaggi di gruppo danneggiati vengono scartati. La configurazione
normale del firmware consente 20 messaggi diretti al minuto. Questa pagina usa
i 5 che il firmware consiglia dal flood di messaggi diretti di luglio 2026.

### Un ripetitore molto trafficato {#busy}

Per un ripetitore in posizione elevata che sente un'intera regione, o uno che
viene inondato:

```text
filter on
filter malformed on
filter rate 05 10 60
filter rate 02 5 60
filter rate 04 5 60
filter advert 24
filter hops 05 16
filter hops 02 16
filter hops 04 8
```

Così dimezzi i messaggi di gruppo e gli annunci, e passa un solo annuncio al
giorno per nodo. I messaggi che hanno già attraversato 16 ripetitori vengono
scartati. Dopo un riavvio, per ogni nodo passa un annuncio. Anche la
documentazione del firmware imposta qui `filter hash 2`. Questa pagina lo
omette (il motivo è in [Tutte le impostazioni](#settings)).

### Blocca un canale rumoroso {#channel}

```text
filter channel add #bot
```

Il tuo ripetitore sente ancora il canale. Non lo inoltra più ad altri
ripetitori e ai companion (i nodi da cui le persone inviano messaggi).
Al massimo 16 canali.

### Rallenta un mittente {#sender}

Un bot che scrive troppo spesso su un canale che vuoi tenere:

```text
filter watch add #test
filter sender add Bob 60
```

Ora i messaggi di Bob sul canale Public e su `#test` passano una volta al
minuto. Il resto viene scartato. Il filtro confronta il nome nel messaggio:
un mittente che cambia nome lo aggira.

### Blocca un ripetitore a monte {#path}

Se il traffico inutile arriva tramite un ripetitore, blocca il suo prefisso:
la prima parte del suo ID, in esadecimale (hex). Ti serve la build di sviluppo
1.18. La 1.17.1 non ha il filtro path.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` mostra i prefissi che blocchi, `filter stats path` quanto
ha scartato ciascuno. Con `filter path remove a1b2` lo lasci di nuovo passare.
Un prefisso corto come `a1` blocca anche ogni altro ripetitore con un ID che
inizia con `a1`. Usa il prefisso più lungo possibile. Al massimo 8 prefissi.

## Tutte le impostazioni {#settings}

I tipi di pacchetto si indicano con un numero. Sul ripetitore, `filter types`
mostra gli stessi numeri con i nomi del firmware, come `TXT_MSG` e `GRP_TXT`:

| Numero | Tipo | Numero | Tipo |
| --- | --- | --- | --- |
| `00` | richiesta | `06` | dati di gruppo |
| `01` | risposta | `07` | richiesta anonima |
| `02` | messaggio diretto | `08` | percorso |
| `03` | conferma di ricezione | `09` | trace |
| `04` | annuncio | `10` | multiparte |
| `05` | messaggio di gruppo | `11` | controllo |

| Comando | Cosa fa | Valore iniziale |
| --- | --- | --- |
| `filter on` / `filter off` | Attiva o disattiva il filtro. | disattivato |
| `filter dryrun on` / `off` | Conta gli scarti ma inoltra comunque tutto. | disattivato |
| `filter hops <type> <max>` | Scarta un tipo che ha già attraversato questo numero di ripetitori, da 0 a 64. | 32 per i messaggi di gruppo, 8 per il resto |
| `filter rate <type> <limit> <secs> [soft]` | Fa passare al massimo `limit` pacchetti di un tipo ogni `secs`. Con `soft`, il passaggio cala gradualmente da `soft` a `limit`. `0` disattiva il limite. | 20 ogni 60 s per messaggi diretti e di gruppo, 10 per gli annunci, 5 per il resto |
| `filter advert <hours>` | Fa passare l'annuncio di ogni nodo una volta ogni tante ore quante ne indichi, fino a 720. | 0 (disattivato) |
| `filter channel add <#name>` | Smette di inoltrare un canale. | nessuno |
| `filter path add <hex>` | Scarta tutto ciò che è arrivato tramite un ripetitore con questo prefisso, da 2 a 8 cifre hex. | nessuno |
| `filter sender add <name> [secs] [prob]` | Scarta i messaggi di gruppo di un mittente, su Public e sui canali sorvegliati. `Bot*` corrisponde a ogni nome che inizia con Bot. | nessuno |
| `filter text add <word> [secs] [prob]` | Scarta i messaggi di gruppo che contengono una parola, su Public e sui canali sorvegliati. `^word` corrisponde solo all'inizio. | nessuno |
| `filter watch add <#name>` | Fa leggere questo canale anche alle regole sender e text, fino a 4. Public viene sempre letto. | Public |
| `filter malformed on` / `off` | Scarta i messaggi Public vuoti, danneggiati o con una data sfasata di oltre una settimana (il controllo della data attende che l'orologio sia impostato). | disattivato |
| `filter age <minutes>` / `off` | Scarta i messaggi di gruppo più vecchi di questo valore, su Public e sui canali sorvegliati, da 1 a 10080. | disattivato |
| `filter hash <bytes>` | Scarta i pacchetti con un ID di percorso più corto di questo valore, da 1 a 3. | 1 |
| `filter reset` | Riporta ogni impostazione al valore predefinito. | |

Ogni `add` ha un `remove` e un `list`, come `filter channel remove #bot`.
Nelle regole sender e text, `secs` fa passare un messaggio ogni tanti secondi quanti ne indichi.
`prob` applica la regola solo a quella percentuale delle corrispondenze, da 1
a 100. Al massimo 8 regole sender e 8 regole text. Nomi e parole distinguono
maiuscole e minuscole. Un nome ha al massimo 15 caratteri, una parola 23.

Due impostazioni scartano più di quanto ti aspetteresti:

- `filter hash 2` scarta quasi tutto il traffico. Per impostazione predefinita
  i nodi inviano ID di percorso da 1 byte.
- `filter age` si fida dell'orologio del tuo ripetitore. Impostalo con
  `clock sync` dall'app, controllalo con `clock` e inizia con un valore
  generoso: `filter age 60`.

Ogni impostazione resta salvata dopo un riavvio.

## Cosa ha scartato {#stats}

`filter` mostra i totali per motivo:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` mostra il dettaglio di una singola impostazione. Gli
argomenti sono `hops`, `rate`, `channel`, `hash`, `malformed`, `advert`,
`path`, `sender`, `text` e `age`. `filter stats top` mostra il primo byte
degli ID dei nodi responsabili del maggior numero di scarti. Molti nodi
condividono quel byte. `filter stats air` mostra il tempo di trasmissione che
il tuo ripetitore ha risparmiato non inoltrando questi pacchetti.

I contatori ripartono da 0 dopo un riavvio e dopo `clear stats`.
