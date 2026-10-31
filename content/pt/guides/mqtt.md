---
title: MQTT no teu observer
lead: Deixa o teu repetidor enviar ao MeshCore Analyzer o que ouve, por Wi-Fi. Continua a reencaminhar mensagens como antes.
description: Transforma um repetidor ESP32 num observer MeshCore com o firmware DMC observer. Instala-o, configura o Wi-Fi e o código de aeroporto, escolhe os brokers e confirma que envia relatórios ao MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-31'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Um observer é um nó que também comunica o que ouve por MQTT, através de
Wi-Fi. Cada observer mostra um pouco mais da mesh no
[MeshCore Analyzer](https://meshcore-analyzer.eu/) e nos
[mapas de cobertura](/map/). Com este guia transformas um repetidor (um nó
que reencaminha mensagens) num observer. O repetidor continua a repetir, e
os relatórios seguem num só sentido: nada volta para a mesh.

{{< callout type="warning" >}}
Este guia é para o **firmware DMC observer**, a versão observer do
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), baseada no
MeshCore 1.18.0. O MeshCore original não tem MQTT. Tirámos todos os comandos
abaixo do código-fonte do firmware, na build `32dd8ad` de 19 de outubro de 2026.
{{< /callout >}}

## O que precisas {#need}

- Uma placa ESP32 com Wi-Fi, como uma Heltec V3 ou V4, uma LilyGo T3S3 ou
  uma Xiao S3. A [release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  indica todas as placas. As placas nRF52, como a RAK4631, não têm Wi-Fi.
- Uma rede Wi-Fi de 2.4 GHz no sítio onde está a placa.
- Um cabo USB de dados, e o Chrome, o Edge ou o Opera no teu computador.
- O código do aeroporto mais próximo do teu nó, com 3 letras, como `AMS` ou
  `BRU`. Com ele, os brokers (os servidores que recebem os teus relatórios)
  sabem em que zona está o teu observer.

Não tens Wi-Fi onde está o repetidor, mas tens um computador ao lado?
Nesse caso, [cria uma configuração de bridge](/guides/mctomqtt/).

## Instalar o firmware {#flash}

O [flasher](/firmware/flasher/) deste site só tem o MeshCore original.
Instalas o firmware observer com o flasher da
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Escolhe a tua placa e depois **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Da primeira vez, escolhe **Full flash**: substitui tudo o que está na placa,
   incluindo a tabela de partições. A atualização da app mantém o que lá está
   e serve para as atualizações seguintes.
3. Configura o repetidor como de costume: nome, predefinição de rádio e
   palavra-passe de admin, como no [guia do repetidor](/repeater-guide/#config).

Este firmware é a build **dev**. Quando escreves `ota update`, o firmware
atualiza-se a partir do canal dev. O canal estável ainda tem a 1.17.1, por
isso fica no dev para seguir este guia.

## Definições {#settings}

Abre a [consola série](/firmware/console/) deste site e liga a tua placa.
Preenche a tua rede Wi-Fi, a palavra-passe e o código de aeroporto. Depois
cola estas linhas, uma de cada vez:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Depois do reinício, a placa liga-se ao teu Wi-Fi e acerta o relógio pela
internet. Os brokers precisam desse relógio para verificar quem é o teu
observer. Sem código de aeroporto, a placa não envia nenhum relatório.

Preferes clicar a escrever? Com `start webconfig` abres uma página de
definições na placa, no endereço que a consola mostra. Entra com a tua
palavra-passe de admin.

## Slots de broker {#brokers}

Cada slot guarda um broker. O firmware já vem com estes slots preenchidos:

| Slot | Broker | Gerido por |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Uma placa sem memória extra (PSRAM), como a Heltec V3, tem 3 slots. Liga-se
a 2 deles ao mesmo tempo, por isso o Analyzer no slot 3 nunca chega a ligar.
Passa-o para o slot 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Uma placa com PSRAM, como a Heltec V4, tem 6 slots e liga-se a 5 ao mesmo
tempo. Aí não tens de mudar nada.

O teu nó entra em cada broker com a sua própria chave, por isso não precisas
de conta. Com `get mqtt.presets` vês os outros brokers da comunidade que o
firmware conhece.

### O teu próprio broker {#own}

Coloca o teu broker num slot livre. Preenche o endereço, a porta, o nome de
utilizador e a palavra-passe. Numa placa com PSRAM, o slot 4 está livre:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Numa placa sem PSRAM, usa antes o slot 2: troca `mqtt4` por `mqtt2`.
O teu broker fica então no lugar do `dutchmeshcore-2`.

A porta `8883` liga com encriptação (TLS), a porta `443` liga com encriptação
sobre uma ligação web (websocket), e qualquer outra porta liga sem
encriptação. Também podes indicar o endereço completo, como
`wss://mqtt.example.org:9002/mqtt`. Nesse caso, a regra das portas não se
aplica.

## Confirmar que funciona {#check}

Escreve `get mqtt.status`. Vês o estado de cada slot:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: ligado.
- `wait`: falta uma definição no slot, como o código de aeroporto.
- `disc`: ainda não está ligado. Verifica o teu Wi-Fi com `get wifi.status`.
- `fail`: o slot falhou 7 vezes seguidas, ao longo de cerca de 20 minutos, e
  agora tenta uma vez a cada 30 minutos. Verifica o endereço e o login do broker.
- `inactive`: a placa não tem espaço para este slot. Vê
  [Slots de broker](#brokers).

Depois procura o nome do teu repetidor na
[página de observers do Analyzer](https://meshcore-analyzer.eu/#observers).
Aparece no prazo de 5 minutos, com o que ouviu.
