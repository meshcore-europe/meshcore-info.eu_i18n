---
title: MQTT no teu observador
lead: Deixa o teu repetidor reportar o que ouve ao MeshCore Analyzer por Wi-Fi. Continua a reencaminhar mensagens como antes.
description: Transforma um repetidor ESP32 num observador MeshCore com o firmware de observador da DMC. Instala-o, configura o Wi-Fi e o teu código de aeroporto, escolhe os brokers e confirma que reporta ao MeshCore Analyzer.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-26'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
---

Um observador é um nó que também reporta o que ouve por MQTT, através
de Wi-Fi. Cada observador mostra um pouco mais da mesh no
[MeshCore Analyzer](https://meshcore-analyzer.eu/) e nos
[mapas de cobertura](/map/). Este guia transforma um repetidor (um nó que
reencaminha mensagens) num observador. Continua a repetir, e o relatório segue
só num sentido: nada volta para a mesh.

{{< callout type="warning" >}}
Este guia é para o **firmware de observador da DMC**, a versão de observador do
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), baseada no
MeshCore 1.18.0. O MeshCore original não tem MQTT. Todos os comandos abaixo
foram retirados do código-fonte do firmware na build `32dd8ad` de 19 de outubro de 2026.
{{< /callout >}}

## O que precisas {#need}

- Uma placa ESP32 com Wi-Fi, como uma Heltec V3 ou V4, uma LilyGo T3S3 ou uma
  Xiao S3. A [release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  lista todas as placas. As placas nRF52, como a RAK4631, não têm Wi-Fi.
- Uma rede Wi-Fi de 2.4 GHz no local onde está a placa.
- Um cabo USB de dados e o Chrome, Edge ou Opera no teu computador.
- O código do aeroporto mais próximo do teu nó, 3 letras como `AMS` ou `BRU`.
  Indica aos brokers (os servidores que recebem os teus relatórios) em que zona
  está o teu observador.

Não há Wi-Fi onde está o teu repetidor, mas tens um computador ao lado?
[Monta antes uma configuração de ponte](/guides/mctomqtt/).

## Instalar o firmware {#flash}

O [flasher](/firmware/flasher/) deste site só tem o MeshCore original.
O firmware de observador vem do flasher da
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Escolhe a tua placa e depois **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Da primeira vez, escolhe **Full flash**: substitui tudo o que está na
   placa, incluindo a tabela de partições. A atualização da app mantém o que lá
   está e serve para atualizações futuras.
3. Configura o teu repetidor como habitualmente: nome, preset de rádio e
   palavra-passe de administrador, como no [guia de repetidores](/repeater-guide/#config).

Este firmware é a build **dev** e atualiza-se a partir do canal dev quando
escreves `ota update`. O canal estável ainda tem a 1.17.1, por isso fica no dev
para este guia.

## Definições {#settings}

Abre a [consola série](/firmware/console/) deste site e liga a tua
placa. Preenche a tua rede Wi-Fi, a palavra-passe e o código de aeroporto, e
depois cola estas linhas uma de cada vez:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Depois de reiniciar, a placa liga-se ao teu Wi-Fi e acerta o relógio pela
internet. Os brokers precisam desse relógio para verificar quem é o teu
observador. Sem código de aeroporto, nada é reportado.

Preferes clicar a escrever? `start webconfig` abre uma página de definições
na placa, no endereço que a consola mostra. Entra com a tua palavra-passe de
administrador.

## Slots de brokers {#brokers}

Um slot guarda um broker. O firmware começa com estes slots preenchidos:

| Slot | Broker | Gerido por |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Uma placa sem memória extra (PSRAM), como a Heltec V3, tem 3 slots. Liga-se a
2 deles ao mesmo tempo, por isso o Analyzer no slot 3 nunca chega a ligar.
Passa-o para o slot 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Uma placa com PSRAM, como a Heltec V4, tem 6 slots e liga-se a 5 ao mesmo
tempo. Não precisa de alterações.

O teu nó autentica-se em cada broker com a sua própria chave, por isso não
precisas de conta. `get mqtt.presets` lista os outros brokers da comunidade que
o firmware conhece.

### O teu próprio broker {#own}

Coloca o teu próprio broker num slot livre. Preenche o endereço, a porta, o
nome de utilizador e a palavra-passe. Numa placa com PSRAM, o slot 4 está livre:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Numa placa sem PSRAM, usa antes o slot 2: substitui `mqtt4` por `mqtt2`.
O teu broker fica então no lugar do `dutchmeshcore-2`.

A porta `8883` liga de forma cifrada (TLS), a porta `443` de forma cifrada por
uma ligação web (websocket), e qualquer outra porta sem cifra. Também podes
indicar o endereço completo, como `wss://mqtt.example.org:9002/mqtt`; nesse
caso, a regra da porta não se aplica.

## Verificar se funciona {#check}

Escreve `get mqtt.status`. Cada slot mostra o seu estado:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: ligado.
- `wait`: falta uma definição ao slot, como o código de aeroporto.
- `disc`: ainda não está ligado. Verifica o teu Wi-Fi com `get wifi.status`.
- `fail`: o slot falhou 7 vezes seguidas, ao longo de cerca de 20 minutos, e
  agora tenta uma vez a cada 30 minutos. Verifica o endereço e as credenciais do broker.
- `inactive`: a placa não tem espaço para este slot. Vê
  [Slots de brokers](#brokers).

Depois procura o nome do teu repetidor na
[página de observadores do Analyzer](https://meshcore-analyzer.eu/#observers).
Aparece em 5 minutos, com aquilo que ouviu.
