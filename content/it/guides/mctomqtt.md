---
title: Crea una configurazione bridge
lead: 'Invia ciò che il tuo ripetitore sente a qualsiasi broker MQTT: il tuo, o quello dell''Analyzer. Un computer accanto al ripetitore si occupa dell''invio.'
description: Esegui meshcoretomqtt su un Raspberry Pi o un altro computer per inviare ciò che un ripetitore MeshCore sente via USB al tuo broker MQTT, al MeshCore Analyzer, o a entrambi.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-26'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
---

Un ripetitore è un nodo che inoltra i messaggi. Vuoi il suo traffico su un
broker MQTT: il tuo, per una dashboard o un database, oppure quello del
[MeshCore Analyzer](https://meshcore-analyzer.eu/). Oppure il tuo ripetitore non
ha un Wi-Fi proprio, ma accanto c'è un Raspberry Pi o un server.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), uno strumento della
community, fa da bridge: invia il traffico da quel computer. Il tuo ripetitore
continua a ripetere, perché il bridge legge solo ciò che registra via USB.

## Cosa ti serve {#need}

- Un ripetitore compilato con la registrazione dei pacchetti (vedi sotto).
- Un Raspberry Pi Zero, 2, 3 o 4, oppure qualsiasi computer Linux o macOS, con
  Python 3.11 o più recente.
- Un cavo dati USB tra i due.

Il firmware standard per ripetitore del flasher non registra i pacchetti.
Compila tu stesso il firmware del ripetitore dal
[codice sorgente di MeshCore](https://github.com/meshcore-dev/MeshCore)
aggiungendo questo flag alla build della tua scheda:

```text
-D MESH_PACKET_LOGGING=1
```

## Installazione {#install}

Collega il ripetitore al computer, poi esegui su quel computer lo script di
installazione di meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Lo script installa il bridge come servizio che parte insieme al computer, e ti
chiede a quali broker inviare. L'Analyzer non è in quell'elenco; lo aggiungi
nel file di configurazione qui sotto. Le tue impostazioni stanno in
`/etc/mctomqtt/config.d/99-user.toml`; un aggiornamento non sovrascrive mai
quel file.

## Broker {#brokers}

Ogni broker ha il proprio blocco `[[broker]]`, così un solo ripetitore può
alimentarne diversi contemporaneamente. Il tuo broker accetta nome utente e
password, oppure nessun login (`method = "none"`).
Il MeshCore Analyzer accetta invece un token, firmato dalla chiave del tuo
ripetitore:

- indirizzo `mqtt.meshcore-analyzer.eu`, porta `443`, tramite websocket sicuro;
- l'audience del token è lo stesso indirizzo.

## Il tuo file di configurazione {#config}

Sostituisci il contenuto di `/etc/mctomqtt/config.d/99-user.toml` con questo.
Inserisci il codice aeroportuale più vicino al tuo ripetitore (`AMS`, per
esempio) e la porta USB a cui è collegato il ripetitore. Poi aggiungi il tuo
broker. Ometti i blocchi che non ti servono.

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

Riavvia il servizio dopo ogni modifica (`sudo systemctl restart mctomqtt` su
Linux). Il tuo ripetitore compare poi sull'Analyzer come observer, cioè un nodo
che carica ciò che sente, con il nome del ripetitore stesso. Il
[README di meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) descrive
tutte le altre impostazioni.
