---
title: Configura un bridge
lead: 'Invia ciò che sente il tuo ripetitore a qualsiasi broker MQTT: il tuo o quello dell''Analyzer. A inviare i dati è un computer accanto al ripetitore.'
description: Esegui meshcoretomqtt su un Raspberry Pi o su un altro computer per inviare ciò che un ripetitore MeshCore sente via USB al tuo broker MQTT, al MeshCore Analyzer o a entrambi.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-31'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Un ripetitore è un nodo che inoltra i messaggi. Vuoi portare il suo traffico su un broker
MQTT: il tuo, per una dashboard o un database, oppure quello del
[MeshCore Analyzer](https://meshcore-analyzer.eu/). Oppure il tuo ripetitore non ha
un proprio WiFi, ma accanto c'è un Raspberry Pi o un server.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), uno strumento della community,
è il bridge: invia il traffico da quel computer. Il tuo ripetitore continua
a ripetere, perché il bridge legge solo ciò che il ripetitore registra via USB.

## Cosa ti serve {#need}

- Un ripetitore compilato con il logging dei pacchetti (vedi sotto).
- Un Raspberry Pi Zero, 2, 3 o 4, oppure un qualsiasi computer Linux o macOS, con Python
  3.11 o più recente.
- Un cavo dati USB tra i due.

Il firmware standard per ripetitori del flasher non registra i pacchetti. Compila
tu il firmware del ripetitore dal
[codice sorgente di MeshCore](https://github.com/meshcore-dev/MeshCore) e aggiungi
questo flag alla build della tua scheda:

```text
-D MESH_PACKET_LOGGING=1
```

## Installazione {#install}

Collega il ripetitore al computer. Poi esegui su quel computer lo script
di installazione di meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Lo script installa il bridge come servizio che parte all'avvio del computer. Poi ti chiede
a quali broker inviare i dati. L'Analyzer non è in quell'elenco: lo aggiungi nel
file di configurazione qui sotto. Le tue impostazioni stanno in
`/etc/mctomqtt/config.d/99-user.toml`. Un aggiornamento non sovrascrive mai quel file.

## Broker {#brokers}

Ogni broker ha il suo blocco `[[broker]]`, quindi un ripetitore può alimentarne diversi
contemporaneamente. Per il tuo broker usi un nome utente e una password, oppure nessun login
(`method = "none"`).
Il MeshCore Analyzer invece richiede un token, firmato con la chiave del tuo ripetitore:

- indirizzo `mqtt.meshcore-analyzer.eu`, porta `443`, tramite websocket sicuro;
- l'audience del token è lo stesso indirizzo.

## Il tuo file di configurazione {#config}

Sostituisci il contenuto di `/etc/mctomqtt/config.d/99-user.toml` con questo. Inserisci
il codice dell'aeroporto più vicino al tuo ripetitore (per esempio `AMS`) e la porta
USB a cui è collegato il ripetitore. Poi aggiungi il tuo broker. Togli i blocchi che
non ti servono.

```toml
[general]
iata = "AMS"

[serial]
ports = ["/dev/ttyACM0"]

# Your own broker
[[broker]]
name = "my-broker"
enabled = true
server = "mqtt.example.org"
port = 1883

[broker.auth]
method = "password"
username = "my_username"
password = "my_password"

# The MeshCore Analyzer
[[broker]]
name = "meshcore-analyzer"
enabled = true
server = "mqtt.meshcore-analyzer.eu"
port = 443
transport = "websockets"

[broker.tls]
enabled = true
verify = true

[broker.auth]
method = "token"
audience = "mqtt.meshcore-analyzer.eu"
```

Dopo una modifica riavvia il servizio (`sudo systemctl restart mctomqtt` su
Linux). A quel punto il tuo ripetitore compare sull'Analyzer come observer, cioè un nodo che
carica ciò che sente, con il nome del tuo ripetitore. Nel
[README di meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) trovi tutte le
altre impostazioni.
