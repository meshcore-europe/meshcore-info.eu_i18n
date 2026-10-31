---
title: MQTT sul tuo observer
lead: Il tuo ripetitore invia via Wi-Fi al MeshCore Analyzer ciò che sente. Intanto continua a inoltrare i messaggi come prima.
description: Trasforma un ripetitore ESP32 in un observer MeshCore con il firmware DMC observer. Installalo, imposta il Wi-Fi e il codice aeroportuale, scegli i broker e verifica che invii i dati al MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-31'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Un observer è un nodo che invia anche via MQTT, tramite Wi-Fi, ciò che sente.
Ogni observer mostra un po' di più della mesh sul
[MeshCore Analyzer](https://meshcore-analyzer.eu/) e sulle
[mappe di copertura](/map/). Con questa guida trasformi un ripetitore (un nodo
che inoltra i messaggi) in un observer. Il nodo continua a ripetere, e i dati
vanno in una sola direzione: nulla torna sulla mesh.

{{< callout type="warning" >}}
Questa guida riguarda il **firmware DMC observer**, la build observer di
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), basata su
MeshCore 1.18.0. MeshCore standard non ha MQTT. Ogni comando qui sotto viene
dal codice sorgente del firmware, build `32dd8ad` del 19 ottobre 2026.
{{< /callout >}}

## Cosa ti serve {#need}

- Una scheda ESP32 con Wi-Fi, per esempio una Heltec V3 o V4, una LilyGo T3S3
  o una Xiao S3. La [release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  elenca tutte le schede. Le schede nRF52 come la RAK4631 non hanno Wi-Fi.
- Una rete Wi-Fi a 2.4 GHz nel punto in cui si trova la scheda.
- Un cavo USB dati, e Chrome, Edge o Opera sul tuo computer.
- Il codice dell'aeroporto più vicino al tuo nodo, 3 lettere come `AMS` o
  `BRU`. Con questo codice i broker (i server che ricevono i tuoi dati) sanno
  in quale zona si trova il tuo observer.

Non c'è Wi-Fi dove si trova il tuo ripetitore, ma hai un computer accanto?
In quel caso [crea una configurazione bridge](/guides/mctomqtt/).

## Installa il firmware {#flash}

Il [flasher](/firmware/flasher/) di questo sito contiene solo MeshCore
standard. Il firmware observer lo trovi nel flasher del
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Scegli la tua scheda, poi **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. La prima volta scegli **Full flash**: sostituisce tutto sulla scheda,
   compresa la tabella delle partizioni. L'aggiornamento dell'app conserva
   ciò che c'è già e serve per gli aggiornamenti successivi.
3. Configura il ripetitore come al solito: nome, preset radio e password di
   amministratore, come nella [guida al ripetitore](/repeater-guide/#config).

Questo firmware è la build **dev**. Quando digiti `ota update`, si aggiorna
dal canale dev. Il canale stabile offre ancora la 1.17.1, quindi per questa
guida resta su dev.

## Impostazioni {#settings}

Apri la [console seriale](/firmware/console/) di questo sito e collega la tua
scheda. Inserisci la tua rete Wi-Fi, la password e il codice aeroportuale,
poi incolla queste righe una alla volta:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Dopo il riavvio, la scheda si collega al tuo Wi-Fi e regola l'orologio via
internet. I broker usano quell'orologio per verificare l'identità del tuo
observer. Senza codice aeroportuale, la scheda non invia nulla.

Preferisci cliccare invece di digitare? Con `start webconfig` apri una pagina
di impostazioni sulla scheda, all'indirizzo indicato dalla console. Accedi con
la tua password di amministratore.

## Slot dei broker {#brokers}

Ogni slot contiene un broker. Il firmware parte con questi slot già compilati:

| Slot | Broker | Gestito da |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Una scheda senza memoria aggiuntiva (PSRAM), come la Heltec V3, ha 3 slot. Si
collega a 2 di essi contemporaneamente, quindi l'Analyzer nello slot 3 non si
collega mai. Spostalo nello slot 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Una scheda con PSRAM, come la Heltec V4, ha 6 slot e si collega a 5
contemporaneamente. Qui non devi cambiare nulla.

Il tuo nodo accede a ogni broker con la propria chiave, quindi non ti serve
un account. Con `get mqtt.presets` vedi gli altri broker della community che
il firmware conosce.

### Il tuo broker {#own}

Inserisci il tuo broker in uno slot libero. Indica indirizzo, porta, nome
utente e password. Su una scheda con PSRAM, lo slot 4 è libero:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Su una scheda senza PSRAM, usa invece lo slot 2: sostituisci `mqtt4` con
`mqtt2`. Il tuo broker prende così il posto di `dutchmeshcore-2`.

Con la porta `8883` la connessione è cifrata (TLS). Con la porta `443` è
cifrata tramite una connessione web (websocket). Con qualsiasi altra porta
non è cifrata. Puoi anche indicare l'indirizzo completo, come
`wss://mqtt.example.org:9002/mqtt`. In quel caso la regola delle porte non
vale.

## Verifica che funzioni {#check}

Digita `get mqtt.status`. Per ogni slot vedi il suo stato:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: connesso.
- `wait`: allo slot manca un'impostazione, per esempio il codice aeroportuale.
- `disc`: non ancora connesso. Controlla il Wi-Fi con `get wifi.status`.
- `fail`: lo slot ha fallito 7 volte di fila, in circa 20 minuti, e ora
  riprova una volta ogni 30 minuti. Controlla indirizzo e credenziali del
  broker.
- `inactive`: la scheda non ha spazio per questo slot. Vedi
  [Slot dei broker](#brokers).

Poi cerca il nome del tuo ripetitore nella
[pagina degli observer dell'Analyzer](https://meshcore-analyzer.eu/#observers).
Compare entro 5 minuti, insieme a ciò che ha sentito.
