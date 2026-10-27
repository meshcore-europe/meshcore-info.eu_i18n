---
title: MQTT en tu observador
lead: Deja que tu repetidor informe por Wi-Fi de lo que oye al MeshCore Analyzer. Sigue reenviando mensajes como antes.
description: Convierte un repetidor ESP32 en un observador de MeshCore con el firmware observador de DMC. Flashéalo, configura el Wi-Fi y tu código de aeropuerto, elige los brokers y comprueba que informa al MeshCore Analyzer.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-26'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
---

Un observador es un nodo que además informa por MQTT, a través de Wi-Fi,
de lo que oye. Cada observador muestra un poco más de la malla en el
[MeshCore Analyzer](https://meshcore-analyzer.eu/) y en los
[mapas de cobertura](/map/). Esta guía convierte un repetidor (un nodo que
reenvía mensajes) en uno. Sigue repitiendo, y el informe va en un solo
sentido: nada vuelve a la malla.

{{< callout type="warning" >}}
Esta guía es para el **firmware observador de DMC**, la versión observadora
de [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), basada en
MeshCore 1.18.0. El MeshCore de serie no tiene MQTT. Cada comando de abajo
sale del código fuente del firmware en la compilación `32dd8ad` del 19 de
octubre de 2026.
{{< /callout >}}

## Qué necesitas {#need}

- Una placa ESP32 con Wi-Fi, como una Heltec V3 o V4, una LilyGo T3S3 o una
  Xiao S3. La [release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  enumera todas las placas. Las placas nRF52, como la RAK4631, no tienen Wi-Fi.
- Una red Wi-Fi de 2.4 GHz en el sitio donde está la placa.
- Un cable USB de datos, y Chrome, Edge u Opera en tu ordenador.
- El código del aeropuerto más cercano a tu nodo, 3 letras como `AMS` o `BRU`.
  Indica a los brokers (los servidores que reciben tus informes) en qué zona
  está tu observador.

¿No hay Wi-Fi donde está tu repetidor, pero sí un ordenador al lado?
Entonces [monta una configuración de puente](/guides/mctomqtt/).

## Flashea el firmware {#flash}

El [flasher](/firmware/flasher/) de este sitio solo lleva MeshCore de serie.
El firmware observador sale del flasher de la
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Elige tu placa y después **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. La primera vez, elige **Full flash**: sustituye todo lo que hay en la
   placa, incluida la tabla de particiones. La actualización de app conserva
   lo que ya hay y sirve para actualizaciones posteriores.
3. Configura tu repetidor como de costumbre: nombre, preajuste de radio y
   contraseña de administrador, como en la
   [guía del repetidor](/repeater-guide/#config).

Este firmware es la compilación **dev** y se actualiza solo desde el canal dev
cuando escribes `ota update`. El canal estable todavía lleva la 1.17.1, así
que quédate en dev para esta guía.

## Ajustes {#settings}

Abre la [consola serie](/firmware/console/) de este sitio y conecta tu placa.
Rellena tu propia red Wi-Fi, la contraseña y el código de aeropuerto, y pega
estas líneas una a una:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Tras el reinicio, la placa se conecta a tu Wi-Fi y pone su reloj en hora
desde internet. Los brokers necesitan ese reloj para comprobar quién es tu
observador. Sin código de aeropuerto, no se informa de nada.

¿Prefieres hacer clic a escribir? `start webconfig` abre una página de
ajustes en la placa, en la dirección que muestra la consola. Entra con tu
contraseña de administrador.

## Ranuras de broker {#brokers}

Una ranura contiene un broker. El firmware arranca con estas ranuras
rellenas:

| Ranura | Broker | Gestionado por |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Una placa sin memoria extra (PSRAM), como la Heltec V3, tiene 3 ranuras. Se
conecta a 2 de ellas a la vez, así que el Analyzer de la ranura 3 nunca se
conecta. Pásalo a la ranura 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Una placa con PSRAM, como la Heltec V4, tiene 6 ranuras y se conecta a 5 a
la vez. No necesita ningún cambio.

Tu nodo inicia sesión en cada broker con su propia clave, así que no
necesitas cuenta. `get mqtt.presets` enumera los demás brokers comunitarios
que conoce el firmware.

### Tu propio broker {#own}

Pon tu propio broker en una ranura libre. Rellena su dirección, puerto,
usuario y contraseña. En una placa con PSRAM, la ranura 4 está libre:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

En una placa sin PSRAM, usa la ranura 2: sustituye `mqtt4` por `mqtt2`. Tu
broker ocupa entonces el sitio de `dutchmeshcore-2`.

El puerto `8883` conecta cifrado (TLS), el puerto `443` cifrado sobre una
conexión web (websocket), y cualquier otro puerto sin cifrar. También puedes
dar la dirección completa, como `wss://mqtt.example.org:9002/mqtt`; entonces
la regla del puerto no se aplica.

## Comprueba que funciona {#check}

Escribe `get mqtt.status`. Cada ranura muestra su estado:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: conectado.
- `wait`: a la ranura le falta un ajuste, como el código de aeropuerto.
- `disc`: todavía no está conectado. Comprueba tu Wi-Fi con `get wifi.status`.
- `fail`: la ranura falló 7 veces seguidas, durante unos 20 minutos, y ahora
  lo intenta una vez cada 30 minutos. Comprueba la dirección y las
  credenciales del broker.
- `inactive`: la placa no tiene sitio para esta ranura. Mira
  [Ranuras de broker](#brokers).

Después busca el nombre de tu repetidor en la
[página de observadores del Analyzer](https://meshcore-analyzer.eu/#observers).
Aparece en menos de 5 minutos, con lo que ha oído.
