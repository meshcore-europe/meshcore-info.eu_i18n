---
title: ¿Qué es MeshCore?
lead: MeshCore envía mensajes de texto por radio, de nodo a nodo. Funciona sin internet y sin suscripción.
description: 'Qué es MeshCore y qué no es: la malla, los companions, los repetidores y los room servers, el enrutamiento, el cifrado y la banda de 868 MHz en Europa.'
eyebrow: MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '33e571f0'
  seeded: '2026-10-26'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['a3a6c1ff', '007314d2', 'f1f23981', '493b444f', '429f699c', 'f8008f48', '655373a9']
---

MeshCore es software libre para pequeñas radios LoRa. LoRa es una técnica de radio
que envía pocos datos a mucha distancia con muy poca energía. Una radio con MeshCore
se llama *nodo*. Emparejada con la app de tu móvil o portátil, o con su propia
pantalla y teclado, envía texto a personas a kilómetros de distancia. No hay ninguna antena de telefonía, router ni operador de por medio.

MeshCore solo envía mensajes de texto cortos: nada de voz, fotos ni tráfico
de internet.
Un mensaje puede tardar unos segundos, y que llegue o no depende de los
repetidores que tengas cerca. No sustituye a los servicios de emergencia: si hay
una emergencia, llama al 112.

El software es de código abierto y se desarrolla en
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) bajo licencia
MIT.

## La malla en un minuto {#mesh}

Una radio LoRa alcanza unos pocos kilómetros en una ciudad, y mucho más desde una
colina o un tejado. Para llegar más lejos, las radios se reenvían los mensajes unas a otras: eso
es una *malla*. En MeshCore, las radios llamadas *repetidores* se encargan del reenvío. Un
repetidor que oye un mensaje lo vuelve a enviar, y así el mensaje puede cruzar toda una región.

La malla no es de nadie. Cada nodo y cada repetidor pertenece a alguien de la
comunidad. La malla es tan buena como los repetidores que la gente instala.

## Los 3 tipos de nodo {#roles}

El tipo de nodo lo eliges al flashearlo. Tu primer nodo es un companion.

**Companion.** Tu propia radio. Se empareja con la app de MeshCore en tu móvil o
portátil por Bluetooth o USB; algunos tienen su propia pantalla y teclado. En la app
lees y escribes. El companion guarda tus contactos y canales,
y los mensajes que llegaron mientras la app no estaba conectada. Un companion no reenvía mensajes de otros.

**Repetidor.** Una radio colocada en alto que reenvía los mensajes de todos. La mayoría
funciona con energía solar. Solo necesitas uno propio donde la malla todavía no
llega. No tiene app propia. Lo configuras por USB, o
inicias sesión con una contraseña y lo gestionas por radio. La
[guía de repetidores](/repeater-guide/) explica cómo.

**Room server.** Un pequeño tablón de mensajes en la malla. Al iniciar sesión, recibes
las publicaciones que te perdiste mientras estabas fuera de alcance, hasta las últimas 32. Un grupo local
lo usa para avisos.

## Cómo encuentra su camino un mensaje {#routing}

Cada nodo tiene una clave secreta y una clave pública. La clave pública es su identidad. Un nodo
se da a conocer con un *anuncio*: un paquete firmado con su nombre y, si tú
quieres, su posición. Alguien aparece en tus contactos cuando uno de sus
anuncios te ha llegado, o cuando escaneas su código QR. La app tiene un botón para enviar el tuyo.

Tu primer mensaje a un contacto sale como una *inundación*. Cada repetidor que
lo oye lo reenvía una vez y añade su propio ID corto por el camino. La respuesta
trae de vuelta esa lista de IDs. A partir de entonces, tus mensajes a ese contacto
siguen la ruta registrada, y solo envían los repetidores que están en ella. Cuando la ruta
se rompe, la app vuelve a inundar.

Los mensajes a un canal no tienen una dirección única, así que siempre se inundan.
Los repetidores recuerdan lo que han reenviado hace poco y descartan las copias que
vuelven a llegar por otra ruta. Un mensaje puede cruzar hasta 64 repetidores, o 32 donde el preajuste usa IDs
de 2 bytes.

## Cifrado y privacidad {#encryption}

Tus mensajes directos van cifrados de extremo a extremo: solo tú y la otra persona
podéis leerlos. Un repetidor solo ve para quién es un paquete como una pista de 1 byte.

Los canales se cifran con una clave compartida, así que quién puede leerlos depende de quién
tiene esa clave:

- **Public** viene configurado en todos los companions. Su clave está publicada, así que cualquiera
  puede leerlo.
- Los **canales de hashtag**, como `#utrecht`, derivan su clave del nombre.
  Cualquiera que conozca el nombre puede unirse, así que trátalos también como públicos.
- Los **canales privados** usan una clave aleatoria que compartes tú mismo, por ejemplo
  como código QR.

Los anuncios van firmados pero no cifrados. El nombre de tu nodo, y su posición si
la compartes, los ve cualquiera que esté al alcance. Elige un nombre que no diga más
de lo que quieres.

## La banda de 868 MHz en Europa {#band}

En Europa, MeshCore usa una pequeña parte de la banda de 868 MHz que cualquiera puede usar
sin licencia. Su preajuste de radio europeo, EU/UK (Narrow), está en
869.618 MHz con un canal de 62.5 kHz. Eso queda dentro de la subbanda
869.40-869.65 MHz, que permite hasta 500 mW e.r.p. Un dispositivo puede transmitir ahí como máximo el 10%
del tiempo. La
[sección legal de la guía de repetidores](/repeater-guide/#legal) tiene los detalles
y los límites por país.

Todos los de una zona usan el mismo preajuste, o sus radios no pueden oírse
entre sí. Algunos países y regiones usan una variante: tu
[grupo local](/community/) sabe cuál.

## Para qué lo usa la gente {#uses}

- Mantener el contacto en excursiones, en el mar y en festivales donde la red móvil
  está saturada o no existe.
- Un canal de respaldo para la familia o los vecinos cuando fallan la luz o las redes
  móviles.
- Chat local en radios que la gente tiene en propiedad.
- Experimentar con radio, antenas, energía solar y software de código abierto.
