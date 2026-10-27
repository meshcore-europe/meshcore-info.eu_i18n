---
title: Primeros pasos
lead: De una placa nueva a tu primer mensaje en la malla. Necesitas una placa LoRa, un ordenador con Chrome o Edge, y un teléfono o portátil para la app.
description: Instala MeshCore desde el navegador, empareja la app, elige el preajuste de radio de tu zona, envía tu primer mensaje y únete a tu canal local.
eyebrow: 6 pasos · MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '68c89544'
  seeded: '2026-10-26'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', '36a3eba3', '6da9fd7a', 'cb5fb72e', '89626504', 'a419ce79', 'aa273b20']
---

Estos pasos siguen el firmware MeshCore v1.18.0 y las herramientas oficiales de
octubre de 2026. Los nombres de los menús de la app pueden variar un poco entre versiones.

## 1. Elige un dispositivo {#device}

Sirve cualquier placa de la [página de dispositivos](/devices/) que indique companion. Para
tu primer nodo, elige un *companion*: la radio desde la que envías mensajes. Emparéjala con
tu teléfono o portátil por Bluetooth o USB, o elige una con pantalla y teclado propios
que funcione por sí sola.

Compra la versión de 868 MHz. La antena incluida cumple; la
[guía de antenas](/guides/antenna/) explica cómo comprobar una.

{{< callout type="warning" >}}
Conecta la antena antes de encender la radio. Una radio LoRa que
transmite sin antena puede dañar su propio chip.
{{< /callout >}}

## 2. Instala el firmware {#flash}

1. Conecta el dispositivo al ordenador con un cable USB de datos.
2. Abre el flasher web en [flasher.meshcore.io](https://flasher.meshcore.io)
   con Chrome o Edge. Usa Web Serial, que otros navegadores no tienen.
3. Elige tu dispositivo y luego el firmware **Companion** para **Bluetooth** (o
   USB, si solo lo vas a usar con cable conectado a un ordenador).
4. Instala. Algunas placas entran primero en modo de actualización; el flasher te
   explica cómo.

Usa *erase* solo para empezar de cero: borrar elimina la identidad del dispositivo
y tus contactos. Para actualizaciones posteriores, instala sin borrar.

## 3. Instala la app {#app}

La app oficial de MeshCore está disponible para Android, iOS, Windows y macOS;
[meshcore.io](https://meshcore.io) enlaza a todas las versiones. También hay una
app web en [app.meshcore.nz](https://app.meshcore.nz) que funciona en Chrome o
Edge en un ordenador.

## 4. Empareja tu nodo {#pair}

Enciende tu nodo, abre la app y conéctate a él por Bluetooth. Cuando
te pida un PIN:

- un nodo **con** pantalla muestra un PIN; escribe ese;
- un nodo **sin** pantalla usa `123456`.

Si el emparejamiento falla, elimina el dispositivo de los ajustes de Bluetooth de tu teléfono
e inténtalo de nuevo. Después ponle un nombre a tu nodo. Los demás ven este nombre, así que no uses
tu nombre completo ni tu dirección a menos que quieras.

## 5. Elige el preajuste de radio de tu zona {#preset}

Todas las radios de una zona usan la misma frecuencia y los mismos ajustes, o no pueden
oírse entre sí. En los ajustes de radio de la app, elige el preajuste que usa tu zona.
Fuera de las zonas de abajo, Europa usa **EU/UK (Narrow)**. Países Bajos,
Chequia, Hungría, Eslovaquia, Portugal y Suiza usan el suyo propio, y
Limburgo, en Países Bajos, tiene una variante:

{{< presets >}}

¿No lo tienes claro? Tu [grupo local](/community/) sabe qué preajuste usa tu zona.
La app descarga esta lista del proyecto MeshCore, así que un preajuste nuevo no requiere
actualizar la app.

## 6. Saluda {#hello}

1. **Anúnciate.** Envía un *anuncio* desde la app. Un anuncio por "inundación"
   viaja a través de los repetidores (nodos que retransmiten mensajes), así que todos
   en la malla pueden añadirte.
   Los companions nunca se anuncian de forma automática.
2. **Encuentra a otros.** Las personas aparecen en tus contactos cuando sus anuncios te
   llegan. Los repetidores envían un anuncio por inundación cada 47 horas por defecto, así que tu lista
   puede tardar 2 días en llenarse.
3. **Envía un mensaje.** Abre un contacto y escribe. El primer mensaje inunda
   la red; el receptor devuelve la ruta que siguió, y los mensajes
   posteriores siguen esa ruta.
4. **Únete a canales.** El canal **Public** ya está configurado; todo lo que
   escribas ahí llega a todos en la malla. Añade el *canal hashtag* de tu región
   (un nombre que empieza por `#`) escribiendo su nombre. Tu
   [grupo local](/community/) te dirá qué canales están activos.

## Cuando algo no funciona {#troubleshooting}

**La app no encuentra mi dispositivo por Bluetooth.**
Seguramente instalaste el companion USB. Vuelve a instalar y elige la
versión Bluetooth. En el Heltec V3, la pequeña antena Bluetooth integrada
tiene poco alcance; mantén el teléfono cerca.

**El emparejamiento falla una y otra vez.**
Elimina el dispositivo de los ajustes de Bluetooth de tu teléfono, reinicia el Bluetooth
y empareja de nuevo con el PIN de la pantalla o `123456`.

**No aparece nadie en mis contactos.**
Comprueba que tu preajuste coincide con tu zona. Envía un anuncio por inundación. Si no hay
ningún repetidor al alcance, solo oirás las radios cercanas; la
[página del mapa](/map/) muestra dónde están los repetidores.

**Un contacto muestra "visto por última vez" hace días aunque está activo.**
Uno de los dos nodos tiene la hora mal. Un companion toma la hora de
tu teléfono; los repetidores y los room servers (nodos que guardan mensajes para un
grupo) necesitan que su propietario la ajuste.

**El flasher no puede abrir el puerto serie en Linux.**
Tu usuario necesita acceso al puerto, por ejemplo con
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, o perteneciendo al grupo
`dialout`.

**Otra cosa.** Las
[preguntas frecuentes de MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
cubren muchos más problemas.
