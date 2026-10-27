---
title: Crea una configuración de puente
lead: 'Envía lo que escucha tu repetidor a cualquier broker MQTT: el tuyo propio o el del Analyzer. Un ordenador junto al repetidor se encarga del envío.'
description: Ejecuta meshcoretomqtt en una Raspberry Pi u otro ordenador para enviar lo que un repetidor MeshCore escucha por USB a tu propio broker MQTT, al MeshCore Analyzer o a ambos.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-26'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
---

Un repetidor es un nodo que reenvía mensajes. Quieres tener su tráfico en un
broker MQTT: el tuyo propio para un panel o una base de datos, o el del
[MeshCore Analyzer](https://meshcore-analyzer.eu/). O tu repetidor no tiene
Wi-Fi propio, pero hay una Raspberry Pi o un servidor a su lado.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), una herramienta de
la comunidad, es el puente: envía el tráfico desde ese ordenador. Tu repetidor
sigue repitiendo, porque el puente solo lee lo que registra por USB.

## Qué necesitas {#need}

- Un repetidor compilado con registro de paquetes (más abajo).
- Una Raspberry Pi Zero, 2, 3 o 4, o cualquier ordenador con Linux o macOS, con
  Python 3.11 o más reciente.
- Un cable USB de datos entre los dos.

El firmware estándar de repetidor del flasher no registra paquetes. Compila tú
mismo el firmware de repetidor desde el
[código fuente de MeshCore](https://github.com/meshcore-dev/MeshCore) con este
indicador añadido a la compilación de tu placa:

```text
-D MESH_PACKET_LOGGING=1
```

## Instalación {#install}

Conecta el repetidor al ordenador y luego ejecuta en ese ordenador el script de
instalación de meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

El script instala el puente como un servicio que arranca con el ordenador y te
pregunta a qué brokers enviar. El Analyzer no está en esa lista; lo añades en
el archivo de configuración de más abajo. Tus propios ajustes están en
`/etc/mctomqtt/config.d/99-user.toml`; una actualización nunca sobrescribe ese
archivo.

## Brokers {#brokers}

Cada broker tiene su propio bloque `[[broker]]`, así que un repetidor puede
alimentar varios a la vez. Tu propio broker acepta un nombre de usuario y una
contraseña, o ningún inicio de sesión (`method = "none"`).
El MeshCore Analyzer acepta en su lugar un token, que firma la clave de tu
repetidor:

- dirección `mqtt.meshcore-analyzer.eu`, puerto `443`, por websocket seguro;
- la audiencia del token es esa misma dirección.

## Tu archivo de configuración {#config}

Sustituye el contenido de `/etc/mctomqtt/config.d/99-user.toml` por esto.
Indica el código de aeropuerto más cercano a tu repetidor (por ejemplo, `AMS`)
y el puerto USB en el que está conectado tu repetidor. Después añade tu propio
broker. Omite cualquier bloque que no necesites.

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
en Linux). Tu repetidor aparece entonces en el Analyzer como observador, un
nodo que sube lo que escucha, con el nombre de tu propio repetidor. En el
[README de meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) encuentras
todos los demás ajustes.
