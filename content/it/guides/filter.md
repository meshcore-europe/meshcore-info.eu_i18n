---
title: Filtro pacchetti
lead: 'Evita che il tuo ripetitore ritrasmetta spazzatura: flood da lontano, un bot che non si ferma mai, un canale rumoroso. Prova prima un''impostazione, poi attivala.'
description: 'Il filtro pacchetti del firmware DMC per ripetitori: cosa scarta, impostazioni pronte per un ripetitore normale e uno molto attivo, ogni comando del filtro con il suo valore predefinito, e come vedere cosa ha scartato.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '2bf23d24'
  seeded: '2026-10-26'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['0625daa2', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', 'ffc3f3a0', '3fa1bb28', '09511608']
---

Un ripetitore (un nodo che inoltra i messaggi) ripete tutto ciò che sente.
Su una mesh affollata questo include anche spazzatura. Un bot pubblica ogni minuto.
Un nodo invia il suo annuncio, il saluto che permette agli altri di trovarlo,
di nuovo ogni pochi minuti. Arrivano messaggi che hanno attraversato mezzo paese.
Ogni ripetizione toglie tempo in aria a tutti quelli intorno a te. Il filtro
pacchetti permette al tuo ripetitore di scartare quel traffico invece di inoltrarlo.

{{< callout type="warning" >}}
Il filtro pacchetti fa parte del **firmware ripetitore DMC**, la build ripetitore
di [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). MeshCore
standard non ha un filtro pacchetti; ha `region denyf *` e
`set flood.max.unscoped`, nella pagina [comandi CLI](/guides/cli/). Questa
guida segue la build dev 1.18.0 `ecfb2d4` del 19 ottobre 2026. La build stabile
1.17.1 ha solo i filtri hop, frequenza, canale, hash e malformati. Non ha
nemmeno la prova a secco.
{{< /callout >}}

## Cosa fa il filtro {#what}

Il filtro guarda solo i pacchetti che il tuo ripetitore inoltra in flood (inviandoli
a ogni nodo a portata). Non tocca mai ciò che il tuo ripetitore invia da sé,
né i pacchetti che seguono un percorso noto verso un nodo. Passano anche i
messaggi diretti e le richieste da e verso i tuoi contatti. Può scartare:

- pacchetti che hanno già attraversato tanti ripetitori (hop) quanti ne permetti,
  per tipo di pacchetto;
- più pacchetti di un tipo di quanti ne permetti al minuto;
- un annuncio da un nodo che ha già annunciato nelle ultime ore;
- messaggi su un canale che blocchi;
- tutto ciò che è passato da un ripetitore che blocchi;
- messaggi di gruppo di un mittente o con una parola, o solo alcuni di essi;
- messaggi di gruppo corrotti, o più vecchi di quanto permetti.

Il filtro è **spento** finché non lo accendi. Lo imposti con comandi. Digitali
via USB nella [console seriale](/firmware/console/) di questo sito. Oppure
inviali dall'app MeshCore, come nella
[guida ripetitore](/repeater-guide/#config).

## Scarica il firmware {#firmware}

Flasha **DutchMeshCore Repeater** dal flasher nella
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Il firmware
observer di [MQTT sul tuo observer](/guides/mqtt/) ha lo stesso filtro.

## Provalo prima {#dryrun}

In prova a secco, il filtro conta ogni pacchetto che scarterebbe, ma lo inoltra
comunque. Dimensiona un'impostazione così prima che scarti qualcosa:

```text
filter on
filter dryrun on
```

Finché la prova a secco è attiva, la riga di stato di `filter` termina con `(dry-run)`.
I conteggi sono ciò che avrebbe scartato. Lascialo girare per un giorno, poi guardali
(vedi [Cosa ha scartato](#stats)). Quando i numeri ti sembrano giusti, applicalo:

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

I messaggi di gruppo passano fino a 20 al minuto, i messaggi diretti fino a 5 al minuto,
e i messaggi di gruppo corrotti vengono scartati. La configurazione normale del firmware
stesso permette 20 messaggi diretti al minuto. Questa pagina prende i 5 che
consiglia da un flood di messaggi diretti nel luglio 2026.

### Un ripetitore affollato {#busy}

Per un ripetitore su un sito alto che sente un'intera regione, o uno che è
sotto flood:

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

Questo dimezza i messaggi di gruppo e gli annunci, e fa passare l'annuncio di
ogni nodo una volta al giorno. Scarta i messaggi che hanno già attraversato 16 ripetitori.
Dopo un riavvio, ogni nodo fa passare un annuncio. La documentazione del firmware
stesso imposta qui anche `filter hash 2`; questa pagina lo lascia fuori (vedi
[Ogni impostazione](#settings) per il motivo).

### Blocca un canale rumoroso {#channel}

```text
filter channel add #bot
```

Il tuo ripetitore sente ancora il canale. Non lo inoltra più ad altri
ripetitori e companion (i nodi da cui le persone inviano messaggi). Fino a 16 canali.

### Rallenta un mittente {#sender}

Un bot che pubblica troppo spesso su un canale che vuoi tenere:

```text
filter watch add #test
filter sender add Bob 60
```

I messaggi di Bob sul canale Public e su `#test` ora passano una volta al minuto; il
resto viene scartato. Il filtro confronta il nome nel messaggio, quindi un mittente che
si rinomina lo supera.

### Blocca un ripetitore a monte {#path}

Quando la spazzatura arriva da un solo ripetitore, blocca il suo prefisso: la prima
parte del suo ID, in esadecimale (hex).

```text
filter path add a1b2
```

Un prefisso corto come `a1` blocca anche ogni altro ripetitore il cui ID inizia
con `a1`. Usa il prefisso più lungo che puoi. Fino a 8 prefissi.

## Ogni impostazione {#settings}

I tipi di pacchetto vanno per numero. Sul ripetitore, `filter types` mostra gli stessi
numeri con i nomi del firmware, come `TXT_MSG` e `GRP_TXT`:

| Numero | Tipo | Numero | Tipo |
| --- | --- | --- | --- |
| `00` | richiesta | `06` | dati di gruppo |
| `01` | risposta | `07` | richiesta anonima |
| `02` | messaggio diretto | `08` | percorso |
| `03` | conferma di ricezione | `09` | trace |
| `04` | annuncio | `10` | multipart |
| `05` | messaggio di gruppo | `11` | controllo |

| Comando | Cosa fa | Valore iniziale |
| --- | --- | --- |
| `filter on` / `filter off` | Accende o spegne il filtro. | off |
| `filter dryrun on` / `off` | Conta gli scarti ma inoltra comunque tutto. | off |
| `filter hops <type> <max>` | Scarta un tipo che ha già attraversato tanti ripetitori, da 0 a 64. | 32 per i messaggi di gruppo, 8 per il resto |
| `filter rate <type> <limit> <secs> [soft]` | Fa passare al massimo `limit` pacchetti di un tipo ogni `secs` secondi. Con `soft`, il passaggio diminuisce gradualmente da `soft` a `limit`. `0` spegne il limite. | 20 ogni 60 s per messaggi diretti e di gruppo, 10 per gli annunci, 5 per il resto |
| `filter advert <hours>` | Fa passare l'annuncio di ogni nodo una volta ogni tante ore, fino a 720. | 0 (off) |
| `filter channel add <#name>` | Smette di inoltrare un canale. | nessuno |
| `filter path add <hex>` | Scarta tutto ciò che è passato da un ripetitore con questo prefisso, da 2 a 8 cifre hex. | nessuno |
| `filter sender add <name> [secs] [prob]` | Scarta i messaggi di gruppo di un mittente, su Public e sui canali osservati. `Bot*` corrisponde a ogni nome che inizia con Bot. | nessuno |
| `filter text add <word> [secs] [prob]` | Scarta i messaggi di gruppo che contengono una parola, su Public e sui canali osservati. `^word` corrisponde solo all'inizio. | nessuno |
| `filter watch add <#name>` | Fa leggere anche questo canale alle regole mittente e testo, fino a 4. Public viene letto sempre. | Public |
| `filter malformed on` / `off` | Scarta i messaggi Public vuoti, corrotti o con una data sbagliata di oltre una settimana (il controllo della data aspetta che l'orologio sia impostato). | off |
| `filter age <minutes>` / `off` | Scarta i messaggi di gruppo più vecchi di così, su Public e sui canali osservati, da 1 a 10080. | off |
| `filter hash <bytes>` | Scarta i pacchetti con un ID percorso più corto di così, da 1 a 3. | 1 |
| `filter reset` | Riporta ogni impostazione al valore predefinito. | |

Ogni `add` ha un `remove` e un `list`, come `filter channel remove #bot`.
Nelle regole mittente e testo, `secs` fa passare un messaggio ogni tanti secondi.
`prob` applica la regola solo a quella quota delle corrispondenze, da 1 a 100. Fino a 8
regole mittente e 8 regole testo. Nomi e parole distinguono maiuscole e minuscole; un nome
ha fino a 15 caratteri, una parola fino a 23.

Due impostazioni scartano più di quanto ti aspetti:

- `filter hash 2` scarta quasi tutto il traffico. I nodi inviano ID percorso da 1 byte
  come impostazione predefinita.
- `filter age` si fida dell'orologio del tuo ripetitore. Impostalo con `clock sync`
  dall'app, controllalo con `clock` e parti largo: `filter age 60`.

Ogni impostazione resta dopo un riavvio.

## Cosa ha scartato {#stats}

`filter` mostra i totali per motivo:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` mostra il dettaglio di una singola impostazione. Gli argomenti sono
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` e `age`. `filter stats top` mostra il primo byte degli ID dei nodi
dietro la maggior parte degli scarti, un indizio più che una prova.
`filter stats air` mostra il tempo in aria che il tuo ripetitore ha risparmiato non
inoltrando questi pacchetti.

I contatori ripartono da 0 dopo un riavvio e dopo `clear stats`.
