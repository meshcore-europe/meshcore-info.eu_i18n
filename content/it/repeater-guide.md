---
title: Guida al ripetitore
lead: Un ripetitore messo in alto inoltra i messaggi per tutti quelli intorno, su un'intera città o valle. Scegli un posto, alimentalo con il sole, configuralo e resta nei limiti di legge.
description: 'Pianifica, alimenta, configura e usa a norma di legge un ripetitore MeshCore in Europa: scelta del sito, dimensionamento solare, impostazioni CLI, limiti di potenza e duty cycle a 868 MHz.'
eyebrow: 868 MHz · fino a 500 mW · senza licenza
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-10-31'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

I ripetitori reggono la mesh. I companion, cioè le radio da cui invii i messaggi, non inoltrano i messaggi. Senza ripetitori raggiungi solo chi è nel tuo raggio diretto. Un ripetitore nel posto giusto estende la mesh per tutti quelli intorno. Questa guida segue il firmware MeshCore v1.18.0.

Prima di iniziare, parla con il tuo [gruppo locale](/community/). Sanno dove manca copertura, quale [preset usa la tua zona](/guides/settings/) e che nome dare ai ripetitori. Guarda le [mappe di copertura](/map/) per trovare i ripetitori vicini e saluta sui [canali](/guides/channels/) pubblici o locali.

## Ti serve davvero? {#need}

Un ripetitore ritrasmette ogni messaggio flood che sente. Tutti i ripetitori in portata condividono lo stesso tempo di trasmissione. Dove la mesh ti raggiunge già, un ripetitore in più aggiunge traffico, non copertura. Un companion messo in alto, a una finestra della soffitta o su un balcone, può bastarti.

Installa un ripetitore dove manca copertura:

- le [mappe di copertura](/map/) non mostrano ripetitori vicino a te, o solo ripetitori che il tuo companion non sente;
- il tuo gruppo locale dice che la zona ne ha bisogno.

## Scegli il sito {#site}

L'altezza conta più della potenza. A 868 MHz il segnale LoRa viaggia meglio in vista ottica libera. Colline, edifici e alberi fitti tolgono molta più portata di quanta ne recuperino pochi milliwatt in più.

- **Sali in alto.** Un tetto, un palo, un edificio alto o una collina coprono molto più di un davanzale. Anche pochi metri sopra i tetti circostanti aiutano.
- **Tieni libera l'antenna.** Montala sopra il bordo del tetto, lontano da metallo, grondaie e altre antenne.
- **Controlla la visuale.** Strumenti come [HeyWhatsThat](https://www.heywhatsthat.com/) mostrano cosa si vede da un punto. Se vedi un luogo, un ripetitore lì è alla tua portata.
- **Lascia spazio libero.** Un percorso radio ha bisogno di spazio libero anche intorno alla linea diretta. Sulle lunghe distanze, a metà percorso il segnale deve passare diversi metri sopra gli ostacoli.
- **Chiedi il permesso.** Ottieni il consenso del proprietario del tetto o del palo e concorda come accederai al ripetitore per la manutenzione.

## Hardware {#hardware}

- **Scheda.** Scegli una scheda nRF52 a basso consumo come la [Heltec T114](/devices/), RAK WisBlock o il SenseCAP Solar Node. Le schede ESP32 consumano di più (la pagina dei dispositivi le segna come High), e così l'alimentazione solare diventa difficile.
- **Antenna.** Usa un'antenna fatta per 868 MHz, montata in verticale; la [guida alle antenne](/guides/antenna/) tratta tipi, connettori, cavi e montaggio. Il guadagno d'antenna rientra nel limite legale di potenza; vedi [Limiti di legge](#legal).
- **Cavo.** Usa un cavo coassiale corto, oppure un cavo a bassa perdita. A 868 MHz pochi metri di cavo sottile possono dimezzare la tua potenza.
- **Contenitore.** Una scatola stagna (IP65 o superiore) con pressacavo, un foro di sfiato o di drenaggio contro la condensa, e un colore chiaro o un parasole. Le batterie soffrono il caldo e non si possono caricare sotto zero.
- **Fulmini.** Un'antenna sul tetto è un bersaglio. Segui le norme locali sulla messa a terra, o montala dove un fulmine non raggiungerebbe l'impianto elettrico dell'edificio.

## Alimentazione e dimensionamento solare {#power}

Un ripetitore solare deve superare le settimane più buie dell'inverno. Dimensionalo per quelle:

1. **Misura il consumo.** Collega il ripetitore configurato a un misuratore di potenza USB per un giorno. Leggi l'energia consumata in wattora (Wh). Il traffico della tua zona cambia il valore, quindi se puoi misura sul posto.
2. **Aggiungi una riserva.** Prevedi una batteria che basti per almeno 5-7 giorni senza sole utile.
3. **Trova il tuo sole invernale.** Lo [strumento PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) gratuito dell'UE mostra, per qualsiasi luogo, quanta energia produce un pannello ogni mese. Usa il mese con meno sole.
4. **Dimensiona il pannello.** Il pannello deve reintegrare il consumo di ogni giorno in quel mese peggiore, con un margine per le perdite di carica.

Un esempio pratico, con numeri ipotetici: un ripetitore che consuma 1 Wh al giorno richiede una batteria di almeno 7 Wh per una settimana di riserva, circa 2 Ah di capacità utile a 3.7 V. Se PVGIS dice che un pannello da 1 W nel tuo sito dà 0.5 Wh al giorno a dicembre, ti serve un pannello di almeno 2 W. Con 3-5 W hai margine per nuvole, neve e invecchiamento.

## Configuralo {#config}

**Flash.** Usa il [web flasher](https://flasher.meshcore.io) e scegli il firmware **Repeater** per la tua scheda. Trovi i passaggi per il flash in [Inizia](/get-started/#flash).

**Configura via USB.** Con il ripetitore ancora collegato al computer, apri [config.meshcore.io](https://config.meshcore.io) o la console del flasher. Puoi anche usare un qualsiasi terminale seriale a 115200 baud. I comandi più importanti:

| Cosa | Comando |
|---|---|
| Cambiare la password di amministratore | `password <new password>` |
| Dargli un nome | `set name <name>` |
| Preset radio: frequenza, larghezza di banda, SF, CR (riavvia per applicarlo) | `set radio 869.618,62.5,8,8` |
| Limite di duty cycle, in percentuale | `set dutycycle 10` |
| Potenza di trasmissione del chip radio, in dBm | `set tx <dBm>` |
| Posizione, per farlo comparire sulle mappe | `set lat <degrees>` e `set lon <degrees>` |
| Recapiti per gli altri operatori | `set owner.info <text>` |
| Ore tra un annuncio flood e l'altro, quelli che sente tutta la mesh | `set flood.advert.interval <hours>` |
| Annunciarlo subito | `advert` |
| Riavviare | `reboot` |

La password di amministratore predefinita è `password`, e chiunque accede con questa diventa amministratore. Cambiala prima che il ripetitore vada in onda.

L'esempio `set radio` qui sopra è EU/UK (Narrow). Usa invece i valori del preset della tua zona: in [Impostazioni consigliate](/guides/settings/) li trovi per paese.

**Imposta l'orologio.** Senza un modulo orologio (RTC), un ripetitore perde l'ora a ogni interruzione di corrente e riparte da maggio 2024. Anche mentre funziona, il suo orologio deriva: va sempre più avanti o indietro. Quindi imposta l'orologio ogni tanto: accedi da remoto dall'app e usa `clock sync`, o imposta l'ora via USB. Con un modulo RTC capita di rado: mantiene l'ora durante le interruzioni di corrente e deriva molto meno.

**Gestiscilo da remoto.** Quando è nella mesh, accedi dall'app MeshCore con la password di amministratore. Lì leggi il suo stato e usi gli stessi comandi via radio. Alcuni comandi funzionano solo via USB, come `set freq` e il reset di fabbrica `erase`.

**Conserva la sua identità.** Prima di un erase, digita `get prv.key` via USB e conserva in un posto sicuro la chiave privata che compare. Dopo l'erase, `set prv.key <key>` e un `reboot` ridanno al ripetitore la sua vecchia identità. Così i nodi che lo conoscono lo ritrovano con lo stesso prefisso.

L'elenco completo dei comandi è nel [riferimento CLI di MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Aggiornalo via radio {#update}

Quando il ripetitore è in alto, lo aggiorni da terra. Accedi dall'app MeshCore con la password di amministratore, apri la sua riga di comando e digita `start ota`. Il seguito dipende dalla scheda; le altre schede rispondono `Error`, e quelle le aggiorni via USB.

**Schede nRF52**, come RAK, Heltec T114, Seeed XIAO e SenseCAP Solar:

1. Scarica lo **ZIP** del nuovo firmware per la tua scheda dal [web flasher](https://flasher.meshcore.io).
2. Digita `start ota`. Il ripetitore risponde `OK` e compare via Bluetooth come `<board>_OTA`, per esempio `RAK4631_OTA`.
3. Apri l'app nRF Device Firmware Update sul telefono, scegli lo ZIP e il ripetitore, e avvia il caricamento. Ci vogliono pochi minuti.

Installa il [bootloader OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX) su una scheda nRF52 prima di montarla in alto. Con il bootloader originale, un aggiornamento fallito si ripara solo via USB. Con OTAFIX la scheda torna in modalità aggiornamento, e tu riprovi via Bluetooth.

**Schede ESP32**, come le Heltec V3 e V4:

1. Scarica dal web flasher il `.bin` **non-merged** per la tua scheda: il file senza "merged" nel nome.
2. Digita `start ota`. Il ripetitore apre una rete WiFi chiamata `MeshCore-OTA` e risponde con l'indirizzo della sua pagina di caricamento.
3. Nel raggio del WiFi, collega il telefono o il portatile a quella rete, apri l'indirizzo e carica il file.

## Limiti di legge {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
I preset europei di MeshCore stanno nella sottobanda **869.40-869.65 MHz**. Nell'UE, nel Regno Unito, in Svizzera e in Norvegia è aperta ai dispositivi a corto raggio senza licenza, entro questi limiti:

- al massimo **500 mW e.r.p.** di potenza irradiata;
- al massimo **10% di duty cycle**: non più di 360 secondi di trasmissione in un'ora, per dispositivo. In alternativa un dispositivo può usare il listen-before-talk con adaptive frequency agility come definito in ETSI EN 300 220-2;
- l'intero segnale, largo al massimo 250 kHz, deve restare dentro la sottobanda.

La banda è condivisa: non devi disturbare i servizi con licenza, e altri possono disturbare te.
La radio deve avere la marcatura CE (in Gran Bretagna, CE o UKCA).
{{< /callout >}}

Fonti: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845), Allegato 1, banda h1.7;
[Decisione della Commissione 2006/771/CE](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) e le sue modifiche;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), banda O.

### Potenza: e.r.p. e la tua antenna {#erp}

Il limite vale per la potenza *irradiata*, misurata rispetto a una semplice antenna a dipolo (e.r.p.). Il guadagno d'antenna si somma; la perdita del cavo si sottrae. I produttori indicano il guadagno d'antenna in dBi, cioè 2.15 dB in più dello stesso guadagno in dBd (rispetto a un dipolo). Tieni questa somma a 27 dBm (500 mW) o meno:

> potenza di trasmissione (dBm) + guadagno d'antenna (dBi) − perdita del cavo (dB) − 2.15 ≤ 27

- Una scheda che trasmette 22 dBm in un'antenna da 5 dBi con 1 dB di perdita nel cavo: 22 + 5 − 1 − 2.15 = 23.85 dBm, circa 240 mW e.r.p. Entro il limite.
- Una scheda con un amplificatore da 30 dBm (1 W) in un'antenna da 3 dBi: 30 + 3 − 2.15 = 30.85 dBm, circa 1.2 W e.r.p. Oltre il limite; abbassa la potenza di trasmissione.

`set tx` imposta l'uscita del chip LoRa, in dBm. Il chip SX1262 arriva al massimo a 22 dBm; il firmware non controlla il numero che inserisci. Le schede con un amplificatore aggiuntivo, come la Heltec V4 o la Station G2, trasmettono molto più del numero che imposti. Controlla la tabella del produttore prima di impostarlo, e parti da valori bassi.

### Duty cycle {#duty-cycle}

Un ripetitore trasmette per tutti quelli intorno, quindi consuma il suo tempo di trasmissione più in fretta di un companion. Il limitatore di duty cycle di MeshCore è impostato di default al 50%, più di quanto consente questa banda. Impostalo al 10% su ogni ripetitore:

```text
set dutycycle 10
```

### Precisione della frequenza {#frequency}

Il canale EU/UK (Narrow), 869.618 MHz con 62.5 kHz di larghezza di banda, arriva fino a 869.649 MHz: meno di 1 kHz sotto il limite superiore della sottobanda. Il segnale deve restare nella banda a ogni temperatura. Per questo serve un quarzo compensato in temperatura (TCXO). Quasi tutte le schede attuali ne hanno uno; le schede più vecchie senza TCXO, come la Heltec V2, derivano troppo per funzionare in modo affidabile a 62.5 kHz.

### Note per paese {#countries}

- **Gli Stati membri dell'UE** devono rendere disponibile questa sottobanda a queste condizioni (Decisione 2006/771/CE, Articolo 3).
- **Regno Unito:** gli stessi limiti, nella [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices) di Ofcom.
- **Svizzera e Liechtenstein:** gli stessi limiti, nella [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09) dell'UFCOM.
- **Norvegia:** gli stessi limiti, nel [regolamento sulle autorizzazioni generali](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Queste note non sono una consulenza legale. Le norme cambiano; nel dubbio, verifica con l'autorità nazionale competente.

## Checklist di installazione {#checklist}

- [ ] Il proprietario del sito è d'accordo, e puoi accedere al ripetitore per la manutenzione.
- [ ] La scheda ha il firmware **Repeater**, e l'antenna era collegata prima della prima accensione.
- [ ] La password di amministratore è cambiata.
- [ ] La radio corrisponde al [preset della tua zona](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` è impostato.
- [ ] La potenza di trasmissione più il guadagno d'antenna resta entro 500 mW e.r.p.
- [ ] Nome, posizione e `owner.info` sono impostati, così gli altri sanno chi lo gestisce.
- [ ] L'orologio è impostato (`clock`).
- [ ] Il contenitore è sigillato, con un foro di drenaggio o di sfiato, e il cavo ha un'ansa di gocciolamento.
- [ ] Batteria e pannello sono dimensionati per il mese invernale peggiore.
- [ ] L'hai provato a distanza con l'app prima di lasciare il sito.
- [ ] Il tuo gruppo locale sa che è attivo.
