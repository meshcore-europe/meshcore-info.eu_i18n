---
title: MQTT en tu observador
lead: Tu repetidor envía por Wi-Fi lo que oye al MeshCore Analyzer. Sigue reenviando mensajes como antes.
description: Convierte un repetidor ESP32 en un observador de MeshCore con el firmware DMC observer. Grábalo, configura el Wi-Fi y tu código de aeropuerto, elige los brokers y comprueba que informa al MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-31'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Un observador es un nodo que además informa por MQTT de lo que oye, a través
de Wi-Fi. Cada observador muestra un poco más de la malla en el
[MeshCore Analyzer](https://meshcore-analyzer.eu/) y en los
[mapas de cobertura](/map/). Con esta guía conviertes un repetidor (un nodo
que reenvía mensajes) en un observador. Sigue repitiendo, y el informe va en
un solo sentido: nada vuelve a la malla.

{{< callout type="warning" >}}
Esta guía es para el **firmware DMC observer**, la versión de observador de
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), basada en
MeshCore 1.18.0. MeshCore estándar no tiene MQTT. Hemos sacado cada comando
de esta guía del código fuente del firmware, versión `32dd8ad` del 19 de
octubre de 2026.
{{< /callout >}}

## Qué necesitas {#need}

- Una placa ESP32 con Wi-Fi, como una Heltec V3 o V4, una LilyGo T3S3 o una
  Xiao S3. En la [release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  aparecen todas las placas. Las placas nRF52, como la RAK4631, no tienen Wi-Fi.
- Una red Wi-Fi de 2.4 GHz donde esté la placa.
- Un cable USB de datos, y Chrome, Edge u Opera en tu ordenador.
- El código de aeropuerto más cercano a tu nodo, 3 letras como `AMS` o `BRU`.
  Con él, los brokers (los servidores que reciben tus informes) saben en qué
  zona está tu observador.

¿No hay Wi-Fi donde está tu repetidor, pero sí un ordenador al lado?
En ese caso, [crea una configuración de puente](/guides/mctomqtt/).

## Grabar el firmware {#flash}

El [flasher](/firmware/flasher/) de esta web solo incluye MeshCore estándar.
El firmware de observador lo encuentras en el flasher de la
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Elige tu placa y luego **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. La primera vez, elige **Full flash**: borra todo lo que hay en la placa,
   también la tabla de particiones. La actualización de app conserva lo que
   hay y sirve para actualizaciones posteriores.
3. Configura tu repetidor como siempre: nombre, preset de radio y contraseña
   de administrador, como en la [guía del repetidor](/repeater-guide/#config).

Este firmware es la versión **dev**. Se actualiza desde el canal dev cuando
escribes `ota update`. El canal estable sigue en 1.17.1, así que quédate en
dev para esta guía.

## Ajustes {#settings}

Abre la [consola serie](/firmware/console/) de esta web y conecta tu placa.
Pon tu propia red Wi-Fi, tu contraseña y tu código de aeropuerto. Después
pega estas líneas de una en una:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Tras reiniciar, la placa se conecta a tu Wi-Fi y pone su reloj en hora por
internet. Los brokers necesitan ese reloj para verificar quién es tu
observador. Sin código de aeropuerto, la placa no informa de nada.

¿Prefieres hacer clic a escribir? Con `start webconfig` abres una página de
ajustes en la placa, en la dirección que muestra la consola. Entra con tu
contraseña de administrador.

## Ranuras de broker {#brokers}

Cada ranura guarda un broker. El firmware viene con estas ranuras rellenadas:

| Ranura | Broker | Gestionado por |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Una placa sin memoria extra (PSRAM), como la Heltec V3, tiene 3 ranuras. Se
conecta a 2 de ellas a la vez, así que el Analyzer de la ranura 3 nunca se
conecta. Muévelo a la ranura 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Una placa con PSRAM, como la Heltec V4, tiene 6 ranuras y se conecta a 5 a
la vez. No necesitas cambiar nada.

Tu nodo inicia sesión en cada broker con su propia clave, así que no
necesitas cuenta. Con `get mqtt.presets` ves los demás brokers comunitarios
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

En una placa sin PSRAM, usa la ranura 2: cambia `mqtt4` por `mqtt2`. Tu
broker ocupa entonces el lugar de `dutchmeshcore-2`.

Con el puerto `8883` la conexión va cifrada (TLS). Con el puerto `443` va
cifrada sobre una conexión web (websocket). Con cualquier otro puerto va sin
cifrar. También puedes poner la dirección completa, como
`wss://mqtt.example.org:9002/mqtt`. En ese caso no se aplica la regla de los
puertos.

## Comprobar que funciona {#check}

Escribe `get mqtt.status`. Verás el estado de cada ranura:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: conectada.
- `wait`: a la ranura le falta un ajuste, como el código de aeropuerto.
- `disc`: todavía sin conectar. Comprueba tu Wi-Fi con `get wifi.status`.
- `fail`: la ranura ha fallado 7 veces seguidas, durante unos 20 minutos, y
  ahora lo intenta una vez cada 30 minutos. Comprueba la dirección y los
  datos de acceso del broker.
- `inactive`: la placa no tiene sitio para esta ranura. Consulta
  [Ranuras de broker](#brokers).

Después busca el nombre de tu repetidor en la
[página de observadores del Analyzer](https://meshcore-analyzer.eu/#observers).
Aparece en menos de 5 minutos, con lo que ha oído.
