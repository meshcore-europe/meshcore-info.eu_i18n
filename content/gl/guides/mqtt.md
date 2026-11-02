---
title: MQTT no teu observador
lead: Fai que o teu repetidor lle informe ao MeshCore Analyzer do que escoita, a través da wifi. Seguirá retransmitindo as mensaxes coma antes.
description: Converte un repetidor ESP32 nun observador de MeshCore co firmware DMC observer. Instálao, configura a wifi e o teu código de aeroporto, escolle os brókers e comproba que informa ao MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-11-02'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Un observador é un nodo que ademais informa do que escoita por MQTT, a través
da Wi-Fi. Cada observador amosa un pouco máis da malla no
[MeshCore Analyzer](https://meshcore-analyzer.eu/) e nos
[mapas de cobertura](/map/). Con esta guía, convertes un repetidor (un nodo que retransmite
as mensaxes) nun observador. O nodo segue repetindo, e a información vai nun só sentido:
nada volve á malla.

{{< callout type="warning" >}}
Esta guía é para o **firmware DMC observer**, a versión para observadores de
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), baseada en
MeshCore 1.18.0. O MeshCore estándar non ten MQTT. Todos os comandos de abaixo saen
do código fonte do firmware, na compilación `32dd8ad` do 19 de outubro de 2026.
{{< /callout >}}

## Que necesitas {#need}

- Unha placa ESP32 con Wi-Fi, como unha Heltec V3 ou V4, unha LilyGo T3S3 ou unha
  Xiao S3. A [versión publicada](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  enumera todas as placas. As placas nRF52, como a RAK4631, non teñen Wi-Fi.
- Unha rede Wi-Fi de 2.4 GHz no lugar onde está a placa.
- Un cable USB de datos, e Chrome, Edge ou Opera no teu ordenador.
- O código do aeroporto máis próximo ao teu nodo, de 3 letras, como `AMS` ou `BRU`.
  Con el, os brókers (os servidores que reciben os teus informes) saben en que zona
  está o teu observador.

Non tes Wi-Fi onde está o repetidor, pero si un ordenador ao lado?
Nese caso, [crea unha configuración de ponte](/guides/mctomqtt/).

## Instala o firmware {#flash}

O [instalador](/firmware/flasher/) deste sitio só inclúe o MeshCore estándar.
O firmware de observador está no instalador da
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Escolle a túa placa e despois **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. A primeira vez, escolle **Full flash**: substitúe todo o que hai na
   placa, incluída a táboa de particións. A actualización da aplicación conserva o que hai
   e serve para as actualizacións posteriores.
3. Configura o repetidor como sempre: nome, axuste de radio e contrasinal de administración, como
   indica a [guía do repetidor](/repeater-guide/#config).

Este firmware é a versión **dev** e actualízase desde a canle dev
cando escribes `ota update`. A canle estable aínda ten a 1.17.1, así que mantente
na dev para seguir esta guía.

## Configuración {#settings}

Abre a [consola serie](/firmware/console/) deste sitio e conecta a
placa. Pon a túa rede Wi-Fi, o contrasinal e o código de aeroporto, e despois pega
estas liñas de unha en unha:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Despois do reinicio, a placa conéctase á túa Wi-Fi e pon o reloxo en hora desde
internet. Os brókers necesitan ese reloxo para comprobar quen é o teu observador. Sen
código de aeroporto, a placa non informa de nada.

Prefires premer a escribir? `start webconfig` abre unha páxina de configuración na
placa, no enderezo que amosa a consola. Entra co teu contrasinal de administración.

## Rañuras de bróker {#brokers}

Cada rañura garda un bróker. O firmware trae estas rañuras xa cubertas:

| Rañura | Bróker | Xestionado por |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Unha placa sen memoria adicional (PSRAM), como a Heltec V3, ten 3 rañuras. Conéctase
a 2 delas á vez, polo que o Analyzer da rañura 3 nunca se conecta.
Móveo á rañura 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Unha placa con PSRAM, como a Heltec V4, ten 6 rañuras e conéctase a 5
á vez. Nela non tes que cambiar nada.

O teu nodo entra en cada bróker coa súa propia chave, así que non necesitas conta.
`get mqtt.presets` enumera os demais brókers comunitarios que coñece o firmware.

### O teu propio bróker {#own}

Pon o teu propio bróker nunha rañura libre. Indica o enderezo, o porto, o nome de usuario e
o contrasinal. Nunha placa con PSRAM, a rañura 4 está libre:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Nunha placa sen PSRAM, usa a rañura 2: substitúe `mqtt4` por `mqtt2`.
O teu bróker ocupa entón o lugar de `dutchmeshcore-2`.

O porto `8883` conecta con cifrado (TLS), o porto `443` con cifrado a través dunha conexión web
(websocket), e calquera outro porto sen cifrado. Tamén podes indicar o
enderezo completo, como `wss://mqtt.example.org:9002/mqtt`; nese caso, a regra dos portos
non se aplica.

## Comproba que funciona {#check}

Escribe `get mqtt.status`. Verás o estado de cada rañura:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: conectada.
- `wait`: á rañura fáltalle un axuste, como o código de aeroporto.
- `disc`: aínda sen conectar. Comproba a túa Wi-Fi con `get wifi.status`.
- `fail`: a rañura fallou 7 veces seguidas, durante uns 20 minutos, e agora
  téntao unha vez cada 30 minutos. Comproba o enderezo e os datos de acceso do bróker.
- `inactive`: a placa non ten espazo para esta rañura. Consulta
  [Rañuras de bróker](#brokers).

Despois busca o nome do teu repetidor na
[páxina de observadores do Analyzer](https://meshcore-analyzer.eu/#observers).
Aparecerá en 5 minutos como máximo, co que escoitou.
