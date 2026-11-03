---
title: ¿Qué es MeshCore?
lead: MeshCore envía mensajes de texto por radio, de nodo a nodo. Funciona sin internet y sin suscripción.
description: 'Qué es MeshCore y qué no es: tipos de nodo, enrutamiento, en qué se diferencia de Meshtastic, cifrado y la banda de 868 MHz.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '279b56a4'
  seeded: '2026-11-02'
  fields: {title: '06eda66b', lead: 'c0174569', description: '15e6d2a7', eyebrow: '8610c822'}
  sections: ['aa768ac3', '16fde264', '0a55792c', 'c3de803d', '493b444f', 'a8b2b9b4', '429f699c', 'f8008f48', '88af2bd3', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'fab378a5', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', 'fc8f3129', '8dec428a', '07cbac35', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '95e18f18', '02f1fe2f', 'e6b5b258']
---

MeshCore es software libre para radios LoRa pequeñas. LoRa es una técnica de
radio que envía pocos datos a mucha distancia con muy poca energía. Una radio
con MeshCore se llama *nodo*. Lo emparejas con la app de tu móvil o portátil,
o lo usas con su propia pantalla y teclado. Así envías texto a personas a
kilómetros de distancia. No hay ninguna antena de telefonía, router ni proveedor de por medio.

El software es de código abierto y se desarrolla en
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) bajo la
licencia MIT.

## Lo que MeshCore no es {#not}

¿Eres nuevo en la radio? Estas son las cosas que la gente suele esperar de
MeshCore y que no hace.

- **No es internet ni un teléfono.** MeshCore envía mensajes cortos de texto,
  más o menos tan largos como un SMS en tu móvil. No hay voz, fotos, vídeo
  ni páginas web, y no puedes contactar con un número de teléfono normal.
- **No es un servicio de emergencias.** Ningún servicio de emergencias escucha
  la malla, y nadie promete que alguien lea tu mensaje. En una emergencia,
  llama al 112.
- **No es instantáneo ni llega a todas partes.** Un mensaje salta de radio en
  radio y puede tardar unos segundos, o no llegar nunca. Que llegue depende de
  los repetidores que tengas cerca, de la altura, los edificios y tu antena.
  Una radio pequeña en interiores a menudo no llega a nadie. Un repetidor en
  un tejado llega a kilómetros de distancia.
- **No es un servicio que alguien gestione por ti.** No hay proveedor, ni
  servicio de asistencia, ni promesa de cobertura. La malla existe donde la
  gente de la comunidad ha instalado repetidores, y en ningún otro sitio.
- **No todo lo que circula es privado.** Los mensajes directos van cifrados,
  pero cualquiera puede leer Public y los canales con hashtag. Cualquiera que
  esté al alcance ve el nombre de tu nodo y la posición que compartes.
  Los [observadores](/network/) envían a mapas públicos lo que oyen. La
  [sección sobre cifrado](#encryption) explica qué sigue siendo privado.
- **No es ilimitado.** Todos los que están en una zona comparten un mismo canal
  de radio. Las normas de la [banda de 868 MHz](#band) limitan cuánto tiempo
  puede transmitir cada radio. Cada mensaje quita tiempo de emisión a todos los
  demás, así que los bots, los anuncios frecuentes y los mensajes de prueba
  ralentizan la malla para todos.
- **No es Meshtastic.** Meshtastic es un sistema distinto que funciona en casi
  las mismas placas. Los dos sistemas no pueden comunicarse entre sí.
  [Si vienes de Meshtastic](#meshtastic) recoge lo que funciona de otra manera.

## La malla en un minuto {#mesh}

Una radio LoRa llega a unos pocos kilómetros en una ciudad, y mucho más lejos
desde una colina o un tejado. Para llegar más lejos, las radios se pasan los
mensajes unas a otras: eso es una *malla*. En MeshCore, unas radios llamadas
*repetidores* se encargan de reenviarlos. Un repetidor que oye un mensaje lo
vuelve a enviar. Así el mensaje puede cruzar toda una región.

La malla no es de nadie. Cada nodo y cada repetidor pertenece a alguien de la
comunidad. La malla llega hasta donde llegan sus repetidores.

## Los 3 tipos de nodo {#roles}

Eliges el tipo de un nodo cuando le instalas el firmware. Tu primer nodo es un
companion.

**Companion.** Tu propia radio. Se empareja con la app de MeshCore de tu móvil
o portátil por Bluetooth o USB; algunos tienen su propia pantalla y teclado.
En la app lees y escribes. El companion guarda tus contactos y canales, y
también los mensajes que llegaron mientras la app no estaba conectada. Un companion no reenvía mensajes de otros.

**Repetidor.** Una radio colocada en alto que reenvía los mensajes de todos.
La mayoría funcionan con energía solar. Solo necesitas uno propio donde la
malla todavía no llega. No tiene app propia. Lo configuras por USB, o inicias
sesión con una contraseña y lo gestionas por radio. En la
[guía del repetidor](/repeater-guide/) te explicamos cómo.

**Room server.** Un pequeño tablón de mensajes en la malla. Cuando inicias
sesión, recibes las publicaciones que te perdiste mientras estabas fuera de
alcance, hasta las últimas 32. Solo las guarda en memoria, así que un reinicio
o un corte de luz las borra. Los grupos locales lo usan para sus avisos.

## Cómo encuentra su camino un mensaje {#routing}

Cada nodo tiene una clave secreta y una clave pública. La clave pública es su identidad. Un
nodo se presenta con un *anuncio*: un paquete firmado con su nombre y, si tú
quieres, su posición. Alguien aparece en tus contactos cuando te ha llegado
uno de sus anuncios, o cuando escaneas su código QR. En la app tienes un botón para enviar el tuyo.

Tu primer mensaje a un contacto sale como *inundación*. Cada repetidor que lo
oye lo reenvía una vez y añade por el camino su propio ID corto. La respuesta
trae de vuelta esa lista de IDs. A partir de ahí, tus mensajes a ese contacto
siguen la ruta registrada, y solo transmiten los repetidores que están en
ella. Cuando la ruta se rompe, la app vuelve a hacer una inundación.

Los mensajes a un canal no tienen una única dirección, así que siempre van por
inundación. Los repetidores recuerdan lo que han reenviado hace poco y
descartan las copias que vuelven a llegar por otra ruta. Un mensaje puede cruzar hasta 64 repetidores, o 32 si el preset usa IDs
de 2 bytes.

## Si vienes de Meshtastic {#meshtastic}

Muchas placas funcionan con MeshCore o con Meshtastic, e instalas el que quieras. Estas son las diferencias que notarás primero. Se basan en MeshCore
v1.18.0 y en la documentación de Meshtastic de noviembre de 2026.

- **Quién reenvía los mensajes.** En MeshCore solo lo hacen los repetidores; tu
  companion nunca lo hace. En Meshtastic, el rol de cliente predeterminado
  también reenvía los mensajes, salvo que otro nodo ya lo haya hecho.
- **Hasta dónde llega un mensaje.** Un mensaje de MeshCore puede pasar por hasta
  64 repetidores. Meshtastic se detiene por defecto tras 3 saltos, y como máximo
  tras 7.
- **Lecturas de otros nodos.** En MeshCore, los repetidores y los nodos de
  sensores envían lecturas como el voltaje de la batería cuando se las pides. No
  las envían a toda la malla.
- **Internet.** El firmware de MeshCore no tiene ningún enlace entre mallas por
  internet. Los [observadores](/network/) comunican a los mapas lo que oyen,
  solo en un sentido. Meshtastic tiene un módulo MQTT integrado que puede
  transportar mensajes entre mallas por internet.

## Cifrado y privacidad {#encryption}

Tus mensajes directos van cifrados de extremo a extremo: solo tú y la otra
persona podéis leerlos. Un repetidor solo ve para quién es un paquete a través
de una pista de 1 byte.

Los canales se cifran con una clave compartida. Quién puede leerlos depende de
quién tenga esa clave:

- **Public** viene configurado en todos los companions. Su clave está publicada,
  así que cualquiera puede leerlo.
- **Los canales hashtag**, como `#utrecht`, sacan su clave de su nombre.
  Cualquiera que conozca el nombre puede unirse, así que trátalos también como
  públicos.
- **Los canales privados** usan una clave aleatoria que compartes tú mismo,
  por ejemplo como código QR.

Los anuncios van firmados, pero no cifrados. Todos los que estén a tu alcance
ven el nombre de tu nodo y también su posición, si la compartes. Elige un
nombre que no diga más de lo que quieres.

## La banda de 868 MHz en Europa {#band}

En Europa, MeshCore usa una pequeña parte de la banda de 868 MHz, que
cualquiera puede usar sin licencia. Su preset de radio europeo, EU/UK
(Narrow), está en 869.618 MHz con un canal de 62.5 kHz. Eso queda dentro de la
subbanda de 869.40-869.65 MHz, que permite hasta 500 mW e.r.p. Un dispositivo
puede transmitir ahí como máximo el 10% del tiempo. En la
[sección legal de la guía del repetidor](/repeater-guide/#legal) tienes los
detalles y los límites de cada país.

Todos los de una zona usan el mismo preset; si no, sus radios no se oyen entre
sí. Algunos países y regiones usan una variante: tu
[grupo local](/community/) sabe cuál.

## Para qué lo usa la gente {#uses}

- Mantener el contacto en rutas de senderismo, en el mar y en festivales donde la red
  móvil está saturada o no existe.
- Un canal de reserva para la familia o los vecinos cuando fallan la luz o las
  redes móviles.
- Chat local en radios que son de quienes las usan.
- Revisar un lugar remoto desde casa. Los repetidores y los nodos de sensores
  informan del voltaje de su batería y de otras lecturas cuando se las pides.
- Vigilar un sensor. Un nodo de sensores ejecuta el firmware de MeshCore para
  medir cosas. Guarda un historial de sus lecturas. Si te suscribes, te avisa,
  por ejemplo cuando se le está agotando la batería.
- Accionar algo que está lejos, como una bomba. Añades esa función al firmware
  del sensor con tu propio código.
- Experimentar con radio, antenas, energía solar y software de código abierto.

## De dónde salen los datos {#data}

La búsqueda de la página de [grupos locales](/community/) encuentra un lugar
con una copia de las listas libres de lugares y códigos postales de
[GeoNames](https://www.geonames.org/), con licencia
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). La copia está en
este sitio. Tu búsqueda nunca sale de tu dispositivo, y no se envía ninguna
petición a GeoNames.
