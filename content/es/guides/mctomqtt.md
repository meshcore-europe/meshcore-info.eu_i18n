---
title: Configura un puente
lead: 'Envía lo que oye tu repetidor a cualquier broker MQTT: el tuyo o el del Analyzer. Un ordenador junto al repetidor se encarga del envío.'
description: Ejecuta meshcoretomqtt en una Raspberry Pi u otro ordenador para enviar lo que un repetidor MeshCore oye por USB a tu propio broker MQTT, al MeshCore Analyzer o a ambos.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-31'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Un repetidor es un nodo que retransmite mensajes. Quieres llevar su tráfico a un broker
MQTT: el tuyo, para un panel o una base de datos, o el del
[MeshCore Analyzer](https://meshcore-analyzer.eu/). O tu repetidor no tiene
WiFi propio, pero tiene al lado una Raspberry Pi o un servidor.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), una herramienta de
la comunidad, es el puente: envía el tráfico desde ese ordenador. Tu repetidor
sigue repitiendo, porque el puente solo lee lo que este registra por USB.

## Qué necesitas {#need}

- Un repetidor compilado con registro de paquetes (ver abajo).
- Una Raspberry Pi Zero, 2, 3 o 4, o cualquier ordenador con Linux o macOS, con
  Python 3.11 o posterior.
- Un cable USB de datos entre los dos.

El firmware estándar de repetidor del flasher no registra paquetes. Compila tú
mismo el firmware del repetidor a partir del
[código fuente de MeshCore](https://github.com/meshcore-dev/MeshCore) y añade
esta opción a la compilación de tu placa:

```text
-D MESH_PACKET_LOGGING=1
```

## Instalación {#install}

Conecta el repetidor al ordenador y ejecuta en ese ordenador el script de
instalación de meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

El script instala el puente como un servicio que arranca con el ordenador. Luego
te pregunta a qué brokers enviar. El Analyzer no está en esa lista: lo añades en
el archivo de configuración de abajo. Tus propios ajustes están en
`/etc/mctomqtt/config.d/99-user.toml`. Una actualización nunca sobrescribe ese
archivo.

## Brokers {#brokers}

Cada broker tiene su propio bloque `[[broker]]`. Así un repetidor puede
alimentar a varios a la vez. Tu propio broker usa un usuario y una contraseña, o
ningún inicio de sesión (`method = "none"`).
El MeshCore Analyzer usa en cambio un token, firmado con la clave de tu repetidor:

- dirección `mqtt.meshcore-analyzer.eu`, puerto `443`, por un websocket seguro;
- la audiencia del token es esa misma dirección.

## Tu archivo de configuración {#config}

Sustituye el contenido de `/etc/mctomqtt/config.d/99-user.toml` por esto. Pon
el código del aeropuerto más cercano a tu repetidor (por ejemplo, `AMS`) y el
puerto USB donde está conectado. Después añade tu propio broker. Quita los
bloques que no necesites.

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

Reinicia el servicio después de cada cambio (`sudo systemctl restart mctomqtt`
en Linux). Tu repetidor aparece entonces en el Analyzer como observador, un nodo
que sube lo que oye, con el nombre propio de tu repetidor. En el
[README de meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) encontrarás
todos los demás ajustes.
