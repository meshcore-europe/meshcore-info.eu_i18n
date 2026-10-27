---
title: Criar uma configuração de ponte
lead: 'Envia o que o teu repetidor ouve para qualquer broker MQTT: o teu, ou o do Analyzer. Um computador ao lado do repetidor trata do envio.'
description: Corre o meshcoretomqtt num Raspberry Pi ou noutro computador para enviar o que um repetidor MeshCore ouve por USB para o teu broker MQTT, para o MeshCore Analyzer, ou para ambos.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-26'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
---

Um repetidor é um nó que reencaminha mensagens. Queres o tráfego dele num broker MQTT: o teu, para um painel ou uma base de dados, ou o do [MeshCore Analyzer](https://meshcore-analyzer.eu/). Ou o teu repetidor não tem Wi-Fi próprio, mas tens um Raspberry Pi ou um servidor ao lado dele. O [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), uma ferramenta da comunidade, é a ponte: envia o tráfego a partir desse computador. O teu repetidor continua a repetir, porque a ponte só lê o que ele regista por USB.

## O que precisas {#need}

- Um repetidor compilado com registo de pacotes (ver abaixo).
- Um Raspberry Pi Zero, 2, 3 ou 4, ou qualquer computador Linux ou macOS, com Python 3.11 ou mais recente.
- Um cabo USB de dados a ligar os dois.

O firmware de repetidor padrão do flasher não regista pacotes. Compila tu o firmware de repetidor a partir do [código-fonte do MeshCore](https://github.com/meshcore-dev/MeshCore), com esta flag adicionada à compilação da tua placa:

```text
-D MESH_PACKET_LOGGING=1
```

## Instalar {#install}

Liga o repetidor ao computador e depois corre o script de instalação do meshcoretomqtt nesse computador:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

O script instala a ponte como um serviço que arranca com o computador e pergunta para que brokers enviar. O Analyzer não está nessa lista; adiciona-lo no ficheiro de configuração abaixo. As tuas definições ficam em `/etc/mctomqtt/config.d/99-user.toml`; uma atualização nunca substitui esse ficheiro.

## Brokers {#brokers}

Cada broker tem o seu próprio bloco `[[broker]]`, por isso um repetidor pode alimentar vários ao mesmo tempo. O teu broker aceita um nome de utilizador e uma palavra-passe, ou nenhum login (`method = "none"`). O MeshCore Analyzer aceita em vez disso um token, que a chave do teu repetidor assina:

- endereço `mqtt.meshcore-analyzer.eu`, porta `443`, por websocket seguro;
- a audiência do token é esse mesmo endereço.

## O teu ficheiro de configuração {#config}

Substitui o conteúdo de `/etc/mctomqtt/config.d/99-user.toml` por isto. Preenche o código de aeroporto mais próximo do teu repetidor (`AMS`, por exemplo) e a porta USB onde o teu repetidor está ligado. Depois adiciona o teu broker. Omite qualquer bloco de que não precises.

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

Reinicia o serviço depois de cada alteração (`sudo systemctl restart mctomqtt` em Linux). O teu repetidor aparece então no Analyzer como observador, um nó que envia o que ouve, com o nome do próprio repetidor. O [README do meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) tem todas as outras definições.
