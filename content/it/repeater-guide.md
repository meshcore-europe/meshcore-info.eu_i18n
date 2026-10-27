---
title: Guida ai ripetitori
lead: Un ripetitore in posizione alta inoltra i messaggi di tutti quelli intorno, su un'intera città o valle. Scegli un sito, alimentalo con il sole, configuralo e resta nei limiti di legge.
description: 'Pianifica, alimenta, configura e usa legalmente un ripetitore MeshCore in Europa: scelta del sito, dimensionamento solare, comandi CLI, limiti di potenza e di duty cycle a 868 MHz.'
eyebrow: 868 MHz · fino a 500 mW · senza licenza
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '4a0fe39f'
  seeded: '2026-10-26'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['1de4a4f7', '766086be', '70faf508', '8bc641aa', '2018aa04', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
---

I ripetitori reggono la mesh. I companion, cioè le radio da cui scrivi i messaggi, non li inoltrano. Senza ripetitori raggiungi quindi solo le persone a portata diretta. Ogni ripetitore che installi estende la mesh per tutti quelli intorno. Questa guida segue il firmware MeshCore v1.18.0.

Prima di iniziare, parla con il tuo [gruppo locale](/community/). Sanno dove manca copertura, quale [preset usa la tua zona](/guides/settings/) e come chiamare i ripetitori. Controlla sulle [mappe di copertura](/map/) i ripetitori vicino a te e saluta sui [canali](/guides/channels/) pubblici o locali.

## Scegli un sito {#site}

L'altezza conta più della potenza. A 868 MHz LoRa viaggia meglio lungo una linea di vista libera. Colline, edifici e alberi fitti costano molta più portata di quanta ne recuperino pochi milliwatt in più.

- **Sali in alto.** Un tetto, un palo, un edificio alto o una collina coprono molto più di un davanzale. Anche pochi metri sopra i tetti circostanti aiutano.
- **Lascia l'antenna libera.** Montala sopra i bordi del tetto, lontano da metallo, grondaie e altre antenne.
- **Controlla la visuale.** Strumenti come [HeyWhatsThat](https://www.heywhatsthat.com/) mostrano cosa si vede da un punto. Se vedi un luogo, un ripetitore lì è raggiungibile.
- **Lascia spazio libero.** Un collegamento radio ha bisogno di spazio libero intorno alla linea diretta, non solo della linea stessa. Sulle lunghe distanze, a metà percorso gli ostacoli devono restare diversi metri sotto la linea.
- **Chiedi il permesso.** Ottieni il consenso del proprietario del tetto o del palo e concordate come raggiungerai il ripetitore per la manutenzione.

## Hardware {#hardware}

- **Scheda.** Scegli una scheda nRF52 a basso consumo come la [Heltec T114](/devices/), la RAK WisBlock o il SenseCAP Solar Node. Le schede ESP32 consumano di più (la pagina dei dispositivi le segna come High), e questo rende difficile l'alimentazione solare.
- **Antenna.** Usa un'antenna fatta per gli 868 MHz, montata in verticale. La [guida alle antenne](/guides/antenna/) tratta tipi, connettori, cavo e montaggio. Il guadagno dell'antenna conta nel limite legale di potenza; vedi [Limiti di legge](#legal).
- **Cavo.** Tieni corto il cavo coassiale, oppure usa un cavo a bassa perdita. A 868 MHz pochi metri di cavo sottile possono dimezzare la tua potenza.
- **Contenitore.** Una scatola stagna (IP65 o superiore) con pressacavo, un foro di sfiato o drenaggio contro la condensa, e un colore chiaro o un parasole. Le batterie soffrono il caldo e non si possono caricare sotto zero.
- **Fulmini.** Un'antenna su un tetto è un bersaglio. Segui le regole locali per la messa a terra, oppure montala dove un fulmine non raggiungerebbe l'impianto elettrico dell'edificio.

## Alimentazione e dimensionamento solare {#power}

Un ripetitore solare deve superare le settimane più buie dell'inverno. Dimensionalo per quelle:

1. **Misura il consumo.** Fai girare il ripetitore configurato attraverso un misuratore di potenza USB per un giorno. Leggi l'energia consumata in wattora (Wh). Il traffico nella tua zona cambia il valore, quindi misura sul posto se puoi.
2. **Aggiungi una riserva.** Prevedi una capacità della batteria per almeno 5-7 giorni senza sole utile.
3. **Trova il tuo sole invernale.** Lo strumento gratuito dell'UE [PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) mostra, per qualsiasi luogo, quanta energia produce un pannello ogni mese. Usa il mese con meno sole.
4. **Dimensiona il pannello.** Il pannello deve rimpiazzare il consumo di ogni giorno in quel mese peggiore, con margine per le perdite di ricarica.

Un esempio pratico, con numeri ipotetici: un ripetitore che consuma 1 Wh al giorno ha bisogno di una batteria di almeno 7 Wh per una settimana di riserva, circa 2 Ah di capacità utile a 3.7 V. Se PVGIS dice che un pannello da 1 W nel tuo sito rende 0.5 Wh al giorno a dicembre, ti serve un pannello di almeno 2 W, e 3-5 W lasciano margine per nuvole, neve e invecchiamento.

## Configuralo {#config}

**Flash.** Usa il [web flasher](https://flasher.meshcore.io) e scegli il firmware **Repeater** per la tua scheda. I passaggi del flash sono in [Inizia](/get-started/#flash).

**Configura via USB.** Con il ripetitore ancora collegato al computer, apri [config.meshcore.io](https://config.meshcore.io) o la console del flasher. Puoi anche usare un qualsiasi terminale seriale a 115200 baud. I comandi più importanti:

| Cosa | Comando |
|---|---|
| Cambiare la password di amministratore | `password <new password>` |
| Dargli un nome | `set name <name>` |
| Preset radio: frequenza, larghezza di banda, SF, CR (riavvia per applicare) | `set radio 869.618,62.5,8,8` |
| Limite di duty cycle, in percentuale | `set dutycycle 10` |
| Potenza di trasmissione del chip radio, in dBm | `set tx <dBm>` |
| Posizione, così compare sulle mappe | `set lat <degrees>` e `set lon <degrees>` |
| Recapiti per gli altri operatori | `set owner.info <text>` |
| Ore tra gli annunci flood, quelli che sente tutta la mesh | `set flood.advert.interval <hours>` |
| Annunciarlo subito | `advert` |
| Riavviare | `reboot` |

La password di amministratore predefinita è `password`, e chiunque entri con quella diventa amministratore. Cambiala prima che il ripetitore vada in onda.

L'esempio di `set radio` qui sopra è EU/UK (Narrow). Usa invece i valori del preset della tua zona: [Impostazioni consigliate](/guides/settings/) li elenca per paese.

**Imposta l'orologio.** Senza un modulo orologio (RTC), un ripetitore perde l'ora a ogni interruzione di corrente e riparte da maggio 2024, e mentre funziona il suo orologio deriva. Accedi da remoto dall'app e usa `clock sync`, oppure imposta l'ora via USB. Un modulo RTC è un'aggiunta che vale la pena per un ripetitore: mantiene l'ora durante le interruzioni di corrente e deriva molto meno.

**Gestiscilo da remoto.** Una volta sulla mesh, accedi dall'app MeshCore con la password di amministratore. Lì leggi il suo stato e usi gli stessi comandi via radio. Alcuni comandi funzionano solo via USB, come `set freq` e il ripristino di fabbrica `erase`.

L'elenco completo dei comandi è nel [riferimento CLI di MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Limiti di legge {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
I preset europei di MeshCore stanno nella sottobanda **869.40-869.65 MHz**. In UE, Regno Unito, Svizzera e Norvegia è aperta ai dispositivi a corto raggio senza licenza, entro questi limiti:

- al massimo **500 mW e.r.p.** di potenza irradiata;
- al massimo **10% di duty cycle**: non più di 360 secondi di trasmissione in un'ora qualsiasi, per dispositivo. In alternativa un dispositivo può usare il listen-before-talk con adaptive frequency agility come definito in ETSI EN 300 220-2;
- l'intero segnale, largo al massimo 250 kHz, deve restare dentro la sottobanda.

La banda è condivisa: non devi disturbare i servizi con licenza, e altri possono disturbare te.
La radio deve avere la marcatura CE (in Gran Bretagna, CE o UKCA).
{{< /callout >}}

Fonti: [Raccomandazione CEPT ERC 70-03](https://docdb.cept.org/document/845), Allegato 1, banda h1.7;
[Decisione della Commissione 2006/771/CE](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
e le sue modifiche;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
banda O.

### Potenza: e.r.p. e la tua antenna {#erp}

Il limite vale per la potenza *irradiata*, misurata rispetto a una semplice antenna a dipolo (e.r.p.). Il guadagno dell'antenna conta; la perdita del cavo si sottrae. I produttori indicano il guadagno dell'antenna in dBi, che è 2.15 dB più dello stesso guadagno in dBd (rispetto a un dipolo). Tieni questa somma a 27 dBm (500 mW) o sotto:

> potenza di trasmissione (dBm) + guadagno dell'antenna (dBi) − perdita del cavo (dB) − 2.15 ≤ 27

- Una scheda che trasmette 22 dBm in un'antenna da 5 dBi attraverso 1 dB di cavo: 22 + 5 − 1 − 2.15 = 23.85 dBm, circa 240 mW e.r.p. Entro il limite.
- Una scheda con un amplificatore da 30 dBm (1 W) in un'antenna da 3 dBi: 30 + 3 − 2.15 = 30.85 dBm, circa 1.2 W e.r.p. Oltre il limite; abbassa la potenza di trasmissione.

`set tx` imposta l'uscita del chip LoRa, in dBm. Il chip SX1262 da solo arriva al massimo a 22 dBm; il firmware non controlla il numero che inserisci. Le schede con un amplificatore aggiuntivo, come la Heltec V4 o la Station G2, trasmettono molto più del numero che imposti. Controlla la tabella del produttore prima di impostarlo, e parti basso.

### Duty cycle {#duty-cycle}

Un ripetitore trasmette per tutti quelli intorno, quindi esaurisce il suo tempo d'aria più in fretta di un companion. Il limitatore di duty cycle di MeshCore è impostato di default al 50%, più di quanto consenta questa banda. Impostalo al 10% su ogni ripetitore:

```text
set dutycycle 10
```

### Precisione di frequenza {#frequency}

Il canale EU/UK (Narrow), 869.618 MHz con 62.5 kHz di larghezza di banda, arriva fino a 869.649 MHz: meno di 1 kHz sotto il limite superiore della sottobanda. Il segnale deve restare dentro la banda a ogni temperatura. Per questo serve un quarzo compensato in temperatura (TCXO). Quasi tutte le schede attuali ne hanno uno; le schede più vecchie senza, come la Heltec V2, derivano troppo per funzionare in modo affidabile a 62.5 kHz.

### Note per paese {#countries}

- **Gli stati membri dell'UE** devono rendere disponibile questa sottobanda a queste condizioni (Decisione 2006/771/CE, articolo 3).
- **Regno Unito:** gli stessi limiti, in Ofcom [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Svizzera e Liechtenstein:** gli stessi limiti, in UFCOM [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norvegia:** gli stessi limiti, nel [regolamento sulle autorizzazioni generali](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Queste note non sono una consulenza legale. Le regole cambiano; nel dubbio, verifica con il regolatore del tuo paese.

## Lista di controllo per l'installazione {#checklist}

- [ ] Il proprietario del sito è d'accordo e puoi raggiungere il ripetitore per la manutenzione.
- [ ] La scheda ha il firmware **Repeater** e l'antenna era collegata prima della prima accensione.
- [ ] La password di amministratore è cambiata.
- [ ] La radio corrisponde al [preset della tua zona](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` è impostato.
- [ ] Potenza di trasmissione più guadagno dell'antenna restano entro 500 mW e.r.p.
- [ ] Nome, posizione e `owner.info` sono impostati, così gli altri sanno chi lo gestisce.
- [ ] L'orologio è impostato (`clock`).
- [ ] Il contenitore è sigillato, con un foro di drenaggio o sfiato, e il cavo ha un'ansa gocciolatoio.
- [ ] Batteria e pannello sono dimensionati per il mese invernale peggiore.
- [ ] L'hai provato a distanza con l'app prima di lasciare il sito.
- [ ] Il tuo gruppo locale sa che è attivo.
