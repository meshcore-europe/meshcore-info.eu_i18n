---
title: Crea una configuració de pont
lead: 'Envia el que sent el teu repetidor a qualsevol broker MQTT: el teu o el de l''Analyzer. Un ordinador al costat del repetidor s''encarrega de l''enviament.'
description: Executa meshcoretomqtt en una Raspberry Pi o en un altre ordinador per enviar el que un repetidor MeshCore sent per USB al teu broker MQTT, al MeshCore Analyzer o a tots dos.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Un repetidor és un node que retransmet missatges. Vols tenir-ne el trànsit en un
broker MQTT: el teu, per a un tauler o una base de dades, o el del
[MeshCore Analyzer](https://meshcore-analyzer.eu/). O bé el teu repetidor no té
Wi-Fi propi, però al costat hi tens una Raspberry Pi o un servidor.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), una eina de la
comunitat, fa de pont: envia el trànsit des d'aquell ordinador. El teu repetidor
continua repetint, perquè el pont només llegeix el que el repetidor registra per USB.

## Què necessites {#need}

- Un repetidor compilat amb el registre de paquets (més avall).
- Una Raspberry Pi Zero, 2, 3 o 4, o qualsevol ordinador amb Linux o macOS, amb
  Python 3.11 o més recent.
- Un cable USB de dades entre tots dos.

El firmware estàndard de repetidor que instal·les amb el flasher no registra
paquets. Compila tu mateix el firmware de repetidor a partir del
[codi font de MeshCore](https://github.com/meshcore-dev/MeshCore) i afegeix
aquest indicador a la compilació de la teva placa:

```text
-D MESH_PACKET_LOGGING=1
```

## Instal·lació {#install}

Connecta el repetidor a l'ordinador i executa-hi l'script d'instal·lació de
meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

L'script instal·la el pont com a servei que s'inicia amb l'ordinador i et
pregunta a quins brokers vols enviar. L'Analyzer no surt en aquesta llista:
l'afegeixes al fitxer de configuració de més avall. La teva configuració es
guarda a `/etc/mctomqtt/config.d/99-user.toml`, i cap actualització no
sobreescriu mai aquest fitxer.

## Brokers {#brokers}

Cada broker té el seu propi bloc `[[broker]]`, de manera que un sol repetidor pot
enviar el trànsit a uns quants alhora. El teu broker fa servir un nom d'usuari i
una contrasenya, o cap inici de sessió (`method = "none"`).
En canvi, el MeshCore Analyzer demana un token signat amb la clau del teu repetidor:

- adreça `mqtt.meshcore-analyzer.eu`, port `443`, per un websocket segur;
- l'audiència del token és la mateixa adreça.

## El teu fitxer de configuració {#config}

Substitueix el contingut de `/etc/mctomqtt/config.d/99-user.toml` per aquest text.
Indica el codi de l'aeroport més proper al teu repetidor (per exemple, `AMS`) i
el port USB on l'has connectat. Després afegeix el teu broker. Omet els blocs
que no necessitis.

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

Reinicia el servei després de cada canvi (`sudo systemctl restart mctomqtt` a
Linux). Aleshores el teu repetidor apareix a l'Analyzer com a observador, un node
que puja el que capta, amb el nom del teu repetidor. Al
[README de meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) trobaràs
totes les altres opcions.
