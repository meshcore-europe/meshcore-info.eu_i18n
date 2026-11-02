---
title: Crea unha configuración de ponte
lead: 'Envía o que oe o teu repetidor a calquera broker MQTT: o teu ou o do Analyzer. Un ordenador situado ao carón do repetidor encárgase do envío.'
description: Executa meshcoretomqtt nunha Raspberry Pi ou noutro ordenador para enviar o que un repetidor MeshCore oe, a través de USB, ao teu propio broker MQTT, ao MeshCore Analyzer ou a ambos.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Un repetidor é un nodo que reenvía mensaxes. Queres ter o seu tráfico nun broker MQTT:
o teu propio, para un panel ou unha base de datos, ou o do
[MeshCore Analyzer](https://meshcore-analyzer.eu/). Ou o teu repetidor non ten
Wi-Fi propia, pero tes unha Raspberry Pi ou un servidor ao seu carón.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), unha ferramenta da comunidade,
é a ponte: envía o tráfico desde ese ordenador. O teu repetidor segue
repetindo, porque a ponte só le o que el rexistra por USB.

## Que necesitas {#need}

- Un repetidor compilado con rexistro de paquetes (mira máis abaixo).
- Unha Raspberry Pi Zero, 2, 3 ou 4, ou calquera ordenador con Linux ou macOS, con Python
  3.11 ou posterior.
- Un cable USB de datos entre os dous.

O firmware estándar de repetidor do flasher non rexistra paquetes. Compila ti
o firmware do repetidor a partir do
[código fonte de MeshCore](https://github.com/meshcore-dev/MeshCore), con esta opción
engadida á compilación da túa placa:

```text
-D MESH_PACKET_LOGGING=1
```

## Instalación {#install}

Conecta o repetidor ao ordenador e despois executa nese ordenador o script de instalación de
meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

O script instala a ponte como un servizo que arranca co ordenador e pregúntache
a que brokers enviar. O Analyzer non está nesa lista: engádelo no
ficheiro de configuración que tes máis abaixo. A túa configuración propia está en
`/etc/mctomqtt/config.d/99-user.toml`; unha actualización nunca sobrescribe ese ficheiro.

## Brokers {#brokers}

Cada broker ten o seu propio bloque `[[broker]]`, así que un repetidor pode enviarlles datos a varios
á vez. O teu propio broker usa un nome de usuario e un contrasinal, ou funciona sen inicio de sesión
(`method = "none"`).
En cambio, o MeshCore Analyzer usa un token, que asina a chave do teu repetidor:

- enderezo `mqtt.meshcore-analyzer.eu`, porto `443`, por un websocket seguro;
- a audiencia do token é ese mesmo enderezo.

## O teu ficheiro de configuración {#config}

Substitúe o contido de `/etc/mctomqtt/config.d/99-user.toml` polo seguinte. Pon
o código do aeroporto máis próximo ao teu repetidor (`AMS`, por exemplo) e o porto USB
onde está conectado. Despois engade o teu propio broker. Deixa fóra os bloques que non
necesites.

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

Reinicia o servizo despois de cada cambio (`sudo systemctl restart mctomqtt` en
Linux). Despois, o teu repetidor aparece no Analyzer como observador, un nodo que
sube o que oe, co seu propio nome. No
[README de meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) tes todas as
demais opcións.
