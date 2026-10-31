---
title: Primeros pasos
lead: De una placa nueva a tu primer mensaje en la malla. Necesitas una placa LoRa, un ordenador con Chrome o Edge, y un móvil o portátil para la app.
description: Instala MeshCore desde el navegador, empareja la app, elige el preset de radio de tu zona, envía tu primer mensaje y únete a tu canal local.
eyebrow: 6 pasos · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-10-31'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Estos pasos siguen el firmware MeshCore v1.18.0 y las herramientas oficiales de
octubre de 2026. Los nombres de los menús de la app pueden variar un poco entre versiones.

## 1. Elige un dispositivo {#device}

Te sirve cualquier placa de la [página de dispositivos](/devices/) que indique companion.
Para tu primer nodo, elige un *companion*: la radio desde la que envías mensajes.
Lo emparejas con tu móvil o portátil por Bluetooth o USB. También puedes elegir uno
con pantalla y teclado propios que funcione de forma autónoma.

Compra la versión de 868 MHz. La antena incluida cumple su función. En la
[guía de antenas](/guides/antenna/) ves cómo comprobar una.

{{< callout type="warning" >}}
Conecta la antena antes de encender la radio. Si una radio LoRa transmite
sin antena, puede dañar su propio chip.
{{< /callout >}}

## 2. Instala el firmware {#flash}

1. Conecta el dispositivo al ordenador con un cable USB de datos.
2. Abre el instalador web en [flasher.meshcore.io](https://flasher.meshcore.io)
   con Chrome o Edge. Usa Web Serial, que otros navegadores no tienen.
3. Elige tu dispositivo y luego el firmware **Companion** para **Bluetooth** (o
   USB, si solo lo vas a usar con un cable al ordenador).
4. Instálalo. Algunas placas tienen que entrar antes en modo de actualización. El instalador
   te explica cómo.

Usa *erase* solo para empezar de cero: al borrar pierdes la identidad del dispositivo
y tus contactos. Para las actualizaciones posteriores, instala sin borrar. Si quieres
conservar tu identidad tras un borrado, exporta antes la clave privada de tu companion
desde la app. Después, vuelve a importarla.

## 3. Instala la app {#app}

La app oficial de MeshCore existe para Android, iOS, Windows y macOS.
En [meshcore.io](https://meshcore.io) encuentras los enlaces a todas las versiones. También hay una
app web en [app.meshcore.nz](https://app.meshcore.nz) que funciona en Chrome o
Edge en un ordenador.

## 4. Empareja tu nodo {#pair}

Enciende tu nodo, abre la app y conéctate a él por Bluetooth. Cuando
te pida un PIN:

- un nodo **con** pantalla muestra un PIN; escribe ese;
- un nodo **sin** pantalla usa `123456`.

Si el emparejamiento falla, elimina el dispositivo de los ajustes de Bluetooth del móvil y
vuelve a intentarlo. Después, ponle un nombre a tu nodo. Los demás ven este nombre. No uses
tu nombre completo ni tu dirección, salvo que quieras.

## 5. Elige el preset de radio de tu zona {#preset}

Todas las radios de una zona usan la misma frecuencia y los mismos ajustes. Si no, no se oyen
entre sí. En los ajustes de radio de la app, elige el preset de tu zona.
Fuera de las zonas de abajo, en Europa se usa **EU/UK (Narrow)**. Países Bajos,
Chequia, Hungría, Eslovaquia, Portugal y Suiza usan uno propio, y
Limburgo, en Países Bajos, tiene una variante:

{{< presets >}}

¿Tu dispositivo no ofrece el preset de tu zona? Introduce a mano los 4 valores de la
tabla en los ajustes de radio de la app: frecuencia, ancho de banda, factor de dispersión
y tasa de codificación. Un nodo con otros valores no oye la malla.

¿Tienes dudas? Tu [grupo local](/community/) sabe qué preset se usa en tu zona.
La app descarga esta lista del proyecto MeshCore. Por eso, un preset nuevo no
necesita actualizar la app.

## 6. Saluda {#hello}

1. **Anúnciate.** Envía un *anuncio* desde la app. Un anuncio por "inundación"
   pasa por los repetidores (nodos que reenvían mensajes). Así, cualquiera
   en la malla puede añadirte.
   Los companions nunca se anuncian solos.
2. **Encuentra a otros.** La gente aparece en tus contactos cuando te llegan
   sus anuncios. Por defecto, los repetidores envían un anuncio por inundación cada 47 horas.
   Tu lista puede tardar 2 días en llenarse.
3. **Envía un mensaje.** Abre un contacto y escribe. El primer mensaje inunda
   la red. El destinatario te devuelve la ruta que siguió, y los mensajes
   siguientes van por esa ruta.
4. **Únete a canales.** El canal **Public** ya viene configurado. Todo lo que
   escribes ahí llega a todos en la malla. Añade el *canal hashtag* de tu región
   (un nombre que empieza por `#`) escribiendo su nombre. Tu
   [grupo local](/community/) te dirá qué canales están activos.

## Cuando algo no funciona {#troubleshooting}

**La app no encuentra mi dispositivo por Bluetooth.**
Seguramente instalaste el companion USB. Vuelve a instalarlo y elige la
versión Bluetooth. En el Heltec V3, la pequeña antena Bluetooth integrada
tiene poco alcance. Mantén el móvil cerca.

**El emparejamiento falla una y otra vez.**
Elimina el dispositivo de los ajustes de Bluetooth del móvil, reinicia el Bluetooth
y vuelve a emparejar con el PIN de la pantalla o con `123456`.

**No aparece nadie en mis contactos.**
Comprueba que tu preset coincide con el de tu zona. Envía un anuncio por inundación. Si no hay
ningún repetidor a tu alcance, solo oirás las radios cercanas. En la
[página del mapa](/map/) ves dónde hay repetidores.

**Un contacto aparece como "visto por última vez" hace días, aunque está activo.**
Uno de los dos nodos tiene la hora mal. Un companion toma la hora de
tu móvil. En los repetidores y los room servers (nodos que guardan mensajes para un
grupo), su propietario tiene que ajustarla.

**Un mensaje directo nunca llega.**
Cada uno tiene que tener al otro como contacto. Un nodo descarta los mensajes de alguien
que no conoce, sin avisar al remitente. Envía un anuncio por inundación y pide
a la otra persona que envíe otro. Comprueba en la app que añade los contactos nuevos
automáticamente. Solo añade nodos dentro de su límite de saltos.

**Los contactos antiguos funcionan, pero los nuevos nunca llegan a conectar.**
Un primer mensaje va por inundación. Un repetidor solo lo reenvía si tiene asignada la
región del mensaje. Los mensajes siguientes van por una ruta aprendida, y ninguna comprobación
de región los detiene. Pregunta a tu [grupo local](/community/) qué regiones tienen los repetidores
de tu entorno, y revisa [los ajustes para tu zona](/guides/settings/#traffic).

**La app ya no conecta con tu companion.**
Algunas placas tienen un botón de usuario, como algunas placas RAK y el Heltec T114.
Mantenlo pulsado durante los primeros 8 segundos tras arrancar la placa. El companion abre
entonces una consola de rescate por USB. En la consola de
[flasher.meshcore.io](https://flasher.meshcore.io), `set pin <pin>` fija un
nuevo PIN de Bluetooth y `erase` borra el dispositivo.

**El instalador no puede abrir el puerto serie en Linux.**
Tu usuario necesita acceso al puerto, por ejemplo con
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, o pertenecer al grupo
`dialout`.

**Otro problema.** En las
[preguntas frecuentes de MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
encontrarás muchos más problemas resueltos.
