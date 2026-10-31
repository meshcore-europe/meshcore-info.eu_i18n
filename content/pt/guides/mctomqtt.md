---
title: Configurar uma ponte
lead: 'Envia o que o teu repetidor ouve para qualquer broker MQTT: o teu ou o do Analyzer. Quem faz o envio é um computador ao lado do repetidor.'
description: Corre o meshcoretomqtt num Raspberry Pi ou noutro computador para enviar o que um repetidor MeshCore ouve por USB para o teu broker MQTT, para o MeshCore Analyzer ou para ambos.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-31'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Um repetidor é um nó que reencaminha mensagens. Queres o tráfego dele num broker
MQTT: no teu, para um painel ou uma base de dados, ou no do
[MeshCore Analyzer](https://meshcore-analyzer.eu/). Ou então o teu repetidor não
tem WiFi próprio, mas tens um Raspberry Pi ou um servidor ao lado dele.
O [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), uma ferramenta da
comunidade, faz de ponte: envia o tráfego a partir desse computador. O teu
repetidor continua a repetir, porque a ponte só lê o que ele regista por USB.

## Do que precisas {#need}

- Um repetidor compilado com registo de pacotes (ver abaixo).
- Um Raspberry Pi Zero, 2, 3 ou 4, ou qualquer computador Linux ou macOS, com
  Python 3.11 ou mais recente.
- Um cabo USB de dados entre os dois.

O firmware de repetidor padrão do flasher não regista pacotes. Compila tu o
firmware de repetidor a partir do
[código-fonte do MeshCore](https://github.com/meshcore-dev/MeshCore). Acrescenta
esta flag à compilação da tua placa:

```text
-D MESH_PACKET_LOGGING=1
```

## Instalar {#install}

Liga o repetidor ao computador. Depois corre nesse computador o script de
instalação do meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

O script instala a ponte como um serviço que arranca com o computador. Também
te pergunta para que brokers queres enviar. O Analyzer não está nessa lista:
acrescenta-lo no ficheiro de configuração abaixo. As tuas definições ficam em
`/etc/mctomqtt/config.d/99-user.toml`. Uma atualização nunca substitui esse ficheiro.

## Brokers {#brokers}

Cada broker tem o seu próprio bloco `[[broker]]`. Assim, um repetidor pode
alimentar vários ao mesmo tempo. O teu broker usa um nome de utilizador e uma
palavra-passe, ou nenhum login (`method = "none"`).
O MeshCore Analyzer usa antes um token, que a chave do teu repetidor assina:

- endereço `mqtt.meshcore-analyzer.eu`, porta `443`, por websocket seguro;
- a audiência do token é esse mesmo endereço.

## O teu ficheiro de configuração {#config}

Substitui o conteúdo de `/etc/mctomqtt/config.d/99-user.toml` por isto. Indica
o código de aeroporto mais próximo do teu repetidor (por exemplo, `AMS`) e a
porta USB onde o repetidor está ligado. Depois acrescenta o teu broker. Retira
os blocos de que não precisas.

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

Reinicia o serviço depois de cada alteração (`sudo systemctl restart mctomqtt`
no Linux). O teu repetidor aparece então no Analyzer como observer, um nó que
envia o que ouve, com o nome do próprio repetidor. O
[README do meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) tem todas
as outras definições.
