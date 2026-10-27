---
title: MQTT sul tuo observer
lead: Fai in modo che il tuo ripetitore riferisca al MeshCore Analyzer, via Wi-Fi, ciò che sente. Continua a trasmettere i messaggi come prima.
description: Trasforma un ripetitore ESP32 in un observer MeshCore con il firmware observer DMC. Flashalo, imposta Wi-Fi e codice aeroportuale, scegli i broker e verifica che riferisca al MeshCore Analyzer.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-26'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
---

Un observer è un nodo che riferisce via MQTT, attraverso il Wi-Fi, anche ciò
che sente. Ogni observer mostra un pezzo in più della mesh sul
[MeshCore Analyzer](https://meshcore-analyzer.eu/) e sulle
[mappe di copertura](/map/). Questa guida trasforma in observer un ripetitore
(un nodo che trasmette i messaggi oltre). Il ripetitore continua a ripetere, e
il rapporto va in una sola direzione: nulla torna sulla mesh.

{{< callout type="warning" >}}
Questa guida riguarda il **firmware observer DMC**, la build observer di
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), basata su
MeshCore 1.18.0. Il MeshCore standard non ha MQTT. Ogni comando qui sotto
viene dal codice sorgente del firmware alla build `32dd8ad` del 19 ottobre 2026.
{{< /callout >}}

## Cosa ti serve {#need}

- Una scheda ESP32 con Wi-Fi, come una Heltec V3 o V4, una LilyGo T3S3 o una
  Xiao S3. La [release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  elenca tutte le schede. Le schede nRF52 come la RAK4631 non hanno Wi-Fi.
- Una rete Wi-Fi a 2.4 GHz nel punto in cui sta la scheda.
- Un cavo USB dati, e Chrome, Edge o Opera sul tuo computer.
- Il codice aeroportuale più vicino al tuo nodo, 3 lettere come `AMS` o `BRU`.
  Indica ai broker (i server che ricevono i tuoi rapporti) in quale zona si
  trova il tuo observer.

Niente Wi-Fi dove sta il tuo ripetitore, ma un computer accanto?
[Costruisci invece una configurazione bridge](/guides/mctomqtt/).

## Flasha il firmware {#flash}

Il [flasher](/firmware/flasher/) di questo sito offre solo il MeshCore standard.
Il firmware observer lo trovi nel flasher della
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Scegli la tua scheda, poi **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. La prima volta scegli **Full flash**: sostituisce tutto ciò che c'è sulla
   scheda, tabella delle partizioni compresa. L'app update conserva ciò che
   c'è già e serve per gli aggiornamenti successivi.
3. Configura il tuo ripetitore come al solito: nome, preset radio e password
   admin, come nella [guida al ripetitore](/repeater-guide/#config).

Questo firmware è la build **dev** e si aggiorna da solo dal canale dev
quando digiti `ota update`. Il canale stable è ancora alla 1.17.1, quindi per
questa guida resta su dev.

## Impostazioni {#settings}

Apri la [console seriale](/firmware/console/) di questo sito e collega la tua
scheda. Inserisci la tua rete Wi-Fi, la password e il codice aeroportuale, poi
incolla queste righe una alla volta:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Dopo il riavvio, la scheda entra nel tuo Wi-Fi e regola l'orologio da
internet. I broker usano quell'orologio per verificare chi è il tuo observer.
Senza codice aeroportuale, non viene riferito nulla.

Preferisci cliccare invece di digitare? `start webconfig` apre una pagina di
impostazioni sulla scheda, all'indirizzo che la console mostra. Accedi con la
tua password admin.

## Slot dei broker {#brokers}

Uno slot contiene un broker. Il firmware parte con questi slot già compilati:

| Slot | Broker | Gestito da |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Una scheda senza memoria aggiuntiva (PSRAM), come la Heltec V3, ha 3 slot. Si
collega a 2 di essi alla volta, quindi l'Analyzer nello slot 3 non si collega
mai. Spostalo nello slot 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Una scheda con PSRAM, come la Heltec V4, ha 6 slot e si collega a 5 alla
volta. Non ha bisogno di modifiche.

Il tuo nodo accede a ogni broker con la propria chiave, quindi non ti serve
un account. `get mqtt.presets` elenca gli altri broker della community che il
firmware conosce.

### Il tuo broker {#own}

Metti il tuo broker in uno slot libero. Inserisci indirizzo, porta, nome utente
e password. Su una scheda con PSRAM, lo slot 4 è libero:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Su una scheda senza PSRAM usa invece lo slot 2: sostituisci `mqtt4` con
`mqtt2`. Il tuo broker prende allora il posto di `dutchmeshcore-2`.

La porta `8883` si collega in modo cifrato (TLS), la porta `443` in modo
cifrato su una connessione web (websocket), e qualsiasi altra porta in chiaro.
Puoi anche indicare l'indirizzo completo, come
`wss://mqtt.example.org:9002/mqtt`; in quel caso la regola delle porte non vale.

## Verifica che funzioni {#check}

Digita `get mqtt.status`. Ogni slot mostra il suo stato:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: collegato.
- `wait`: allo slot manca un'impostazione, come il codice aeroportuale.
- `disc`: non ancora collegato. Controlla il tuo Wi-Fi con `get wifi.status`.
- `fail`: lo slot ha fallito 7 volte di fila, nell'arco di circa 20 minuti, e
  ora riprova una volta ogni 30 minuti. Controlla indirizzo e credenziali del
  broker.
- `inactive`: la scheda non ha spazio per questo slot. Vedi
  [Slot dei broker](#brokers).

Poi cerca il nome del tuo ripetitore nella
[pagina degli observer dell'Analyzer](https://meshcore-analyzer.eu/#observers).
Compare entro 5 minuti, con ciò che ha sentito.
