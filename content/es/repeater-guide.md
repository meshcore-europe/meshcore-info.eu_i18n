---
title: Guía del repetidor
lead: Un repetidor colocado en alto reenvía los mensajes de todos los que tiene alrededor, en todo un pueblo o un valle. Elige un emplazamiento, aliméntalo con energía solar, configúralo y respeta la ley.
description: 'Planifica, alimenta, configura y opera legalmente un repetidor MeshCore en Europa: elección del emplazamiento, dimensionado solar, ajustes por CLI, límites de potencia y de ciclo de trabajo en 868 MHz.'
eyebrow: 868 MHz · hasta 500 mW · sin licencia
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-10-31'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Los repetidores sostienen la malla. Los companions, las radios desde las que envías mensajes, no
reenvían mensajes. Por eso, sin
repetidores solo llegas a las personas que tienes a alcance directo. Un repetidor en el lugar
adecuado amplía la malla para todos los que lo rodean. Esta guía corresponde al firmware
MeshCore v1.18.0.

Antes de empezar, habla con tu [grupo local](/community/). Saben dónde
falta cobertura, qué [preset usa tu zona](/guides/settings/) y cómo se nombran los repetidores. Consulta los
[mapas de cobertura](/map/) para ver los repetidores cercanos y saluda en los [canales](/guides/channels/)
públicos o locales.

## ¿Lo necesitas? {#need}

Un repetidor reenvía cada mensaje de inundación que oye. Todos los repetidores
a su alcance comparten el mismo tiempo de emisión. Donde la malla ya te llega, un repetidor
más añade tráfico y no cobertura. Un companion colocado en alto, en la ventana de un desván
o en un balcón, puede bastarte.

Instala un repetidor donde falte cobertura:

- los [mapas de cobertura](/map/) no muestran ningún repetidor cerca de ti, o solo algunos que tu
  companion no oye;
- tu grupo local dice que la zona lo necesita.

## Elige un emplazamiento {#site}

La altura gana a la potencia. LoRa en 868 MHz llega más lejos con una línea de
visión despejada. Las colinas, los edificios y los árboles densos restan mucho más alcance
del que recuperan unos pocos milivatios extra.

- **Busca altura.** Un tejado, un mástil, un edificio alto o una colina cubren mucho más
  que el alféizar de una ventana. Incluso unos pocos metros por encima de los tejados de alrededor ayudan.
- **Deja la antena despejada.** Móntala por encima del borde del tejado, lejos del
  metal, de los canalones y de otras antenas.
- **Comprueba la visibilidad.** Con herramientas como [HeyWhatsThat](https://www.heywhatsthat.com/)
  ves lo que se divisa desde un lugar. Si ves un punto, un repetidor
  colocado allí queda a tu alcance.
- **Deja margen libre.** Una ruta de radio necesita algo de espacio libre alrededor de la línea
  directa, no solo la línea en sí. En distancias largas, el centro de la ruta
  debe pasar varios metros por encima de los obstáculos.
- **Pide permiso.** Consigue el consentimiento del propietario del tejado o del mástil y acuerda
  con él cómo accederás al repetidor para el mantenimiento.

## Hardware {#hardware}

- **Placa.** Elige una placa nRF52 de bajo consumo, como la
  [Heltec T114](/devices/), la RAK WisBlock o el SenseCAP Solar Node. Las placas ESP32
  consumen más (la página de dispositivos las marca como High). Eso complica
  alimentarlas con energía solar.
- **Antena.** Usa una antena diseñada para 868 MHz, montada en vertical. La
  [guía de antenas](/guides/antenna/) explica tipos, conectores, cable y
  montaje. La ganancia de la antena cuenta para el límite legal de potencia; consulta
  [Límites legales](#legal).
- **Cable.** Usa un cable coaxial corto o un cable de bajas pérdidas. En 868 MHz, unos pocos
  metros de cable fino pueden hacerte perder la mitad de la potencia.
- **Caja.** Usa una caja estanca (IP65 o superior) con prensaestopas, un orificio
  de ventilación o de drenaje contra la condensación, y un color claro o un parasol.
  Las baterías sufren con el calor y no se pueden cargar por debajo de cero grados.
- **Rayos.** Una antena en un tejado es un blanco. Sigue las normas locales de
  puesta a tierra, o móntala donde un rayo no alcance el cableado del
  edificio.

## Energía y dimensionado solar {#power}

Un repetidor solar debe aguantar las semanas más oscuras del invierno. Dimensiónalo
para ellas:

1. **Mide el consumo.** Conecta el repetidor ya configurado a un medidor de potencia USB
   durante un día. Lee la energía consumida en vatios hora (Wh). El tráfico de
   tu zona cambia la cifra, así que mide en el emplazamiento si puedes.
2. **Añade reserva.** Prevé una batería con capacidad para al menos 5 a 7 días
   sin sol útil.
3. **Averigua tu sol de invierno.** La
   [herramienta PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) gratuita de la UE muestra, para cualquier
   lugar, cuánta energía produce un panel cada mes. Usa el mes con
   menos sol.
4. **Dimensiona el panel.** El panel debe reponer el consumo de cada día en ese peor
   mes, con margen para las pérdidas de carga.

Un ejemplo práctico, con cifras supuestas: un repetidor que consume 1 Wh al día
necesita una batería de al menos 7 Wh para una semana de reserva, unos 2 Ah de
capacidad útil a 3.7 V. Si PVGIS indica que un panel de 1 W en tu emplazamiento da
0.5 Wh al día en diciembre, necesitas al menos un panel de 2 W. Con 3 a 5 W
tienes margen para nubes, nieve y envejecimiento.

## Configúralo {#config}

**Flashea.** Usa el [flasher web](https://flasher.meshcore.io) y elige el
firmware **Repeater** para tu placa. Los pasos para flashear están en
[Primeros pasos](/get-started/#flash).

**Configura por USB.** Con el repetidor aún conectado al ordenador,
abre [config.meshcore.io](https://config.meshcore.io) o la consola del flasher.
También puedes usar cualquier terminal serie a 115200 baudios. Los comandos
más importantes:

| Qué | Comando |
|---|---|
| Cambiar la contraseña de administrador | `password <new password>` |
| Ponerle nombre | `set name <name>` |
| Preset de radio: frecuencia, ancho de banda, SF, CR (reinicia para aplicarlo) | `set radio 869.618,62.5,8,8` |
| Límite de ciclo de trabajo, en porcentaje | `set dutycycle 10` |
| Potencia de transmisión del chip de radio, en dBm | `set tx <dBm>` |
| Posición, para que aparezca en los mapas | `set lat <degrees>` y `set lon <degrees>` |
| Datos de contacto para otros operadores | `set owner.info <text>` |
| Horas entre anuncios de inundación, los que oye toda la malla | `set flood.advert.interval <hours>` |
| Anunciarlo ahora | `advert` |
| Reiniciar | `reboot` |

La contraseña de administrador por defecto es `password`. Quien inicie sesión con ella
pasa a ser administrador. Cámbiala antes de que el repetidor empiece a emitir.

El ejemplo de `set radio` de arriba es EU/UK (Narrow). Usa en su lugar los valores del preset
de tu zona: en [Ajustes recomendados](/guides/settings/) los encuentras
por país.

**Pon la hora.** Sin un módulo de reloj (RTC), un repetidor pierde la hora en
cada corte de corriente y al arrancar vuelve a mayo de 2024. Mientras funciona, su reloj también
deriva: se adelanta o se atrasa. Así que ajusta la hora de vez en cuando: inicia
sesión en remoto desde la app y usa `clock sync`, o pon la hora por USB. Con
un módulo RTC rara vez hace falta: mantiene la hora durante los cortes de corriente y
deriva mucho menos.

**Gestiónalo en remoto.** Cuando ya esté en la malla, inicia sesión desde la app de MeshCore
con la contraseña de administrador. Allí ves su estado y usas los mismos comandos
por radio. Algunos comandos solo funcionan por USB, como `set freq` y el
restablecimiento de fábrica `erase`.

**Conserva su identidad.** Antes de un borrado, escribe `get prv.key` por USB y guarda
en un lugar seguro la clave privada que aparece. Después del borrado, con `set prv.key <key>`
y un `reboot` el repetidor recupera su identidad anterior. Así los nodos que lo conocen
lo encuentran con el mismo prefijo.

La lista completa de comandos está en la
[referencia de la CLI de MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Actualízalo por el aire {#update}

Cuando el repetidor ya esté en lo alto, lo actualizas desde el suelo. Inicia sesión desde la
app de MeshCore con la contraseña de administrador, abre su línea de comandos y escribe
`start ota`. Lo que sigue depende de la placa. Otras placas responden `Error`
y esas las actualizas por USB.

**Placas nRF52**, como RAK, Heltec T114, Seeed XIAO y SenseCAP Solar:

1. Descarga el **ZIP** del nuevo firmware para tu placa desde el
   [flasher web](https://flasher.meshcore.io).
2. Escribe `start ota`. El repetidor responde `OK` y aparece por Bluetooth
   como `<board>_OTA`, por ejemplo `RAK4631_OTA`.
3. Abre en tu móvil la app nRF Device Firmware Update, elige el ZIP y
   el repetidor, y súbelo. Tarda unos minutos.

Instala el [bootloader OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
en una placa nRF52 antes de instalarla en lo alto. Con el bootloader de serie, una actualización
fallida solo se puede reparar por USB. Con OTAFIX la placa vuelve al
modo de actualización y lo intentas de nuevo por Bluetooth.

**Placas ESP32**, como la Heltec V3 y V4:

1. Descarga desde el flasher web el `.bin` **no fusionado** para tu placa:
   el archivo sin "merged" en el nombre.
2. Escribe `start ota`. El repetidor abre una red WiFi llamada `MeshCore-OTA`
   y responde con la dirección de su página de subida.
3. Dentro del alcance de la WiFi, conecta tu móvil o portátil a esa red, abre la
   dirección y sube el archivo.

## Límites legales {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Los presets europeos de MeshCore están en la subbanda **869.40-869.65 MHz**. En la
UE, el Reino Unido, Suiza y Noruega está abierta sin licencia a los dispositivos de corto
alcance, dentro de estos límites:

- como máximo **500 mW e.r.p.** de potencia radiada;
- como máximo un **10% de ciclo de trabajo**: no más de 360 segundos de transmisión en
  cualquier hora, por dispositivo. Como alternativa, un dispositivo puede usar listen-before-talk
  con agilidad de frecuencia adaptativa, tal como la define ETSI EN 300 220-2;
- toda la señal, de 250 kHz de ancho como máximo, debe quedar dentro de la subbanda.

La banda es compartida: no debes interferir con servicios con licencia, y otros pueden
interferir contigo.
La radio debe llevar el marcado CE (en Gran Bretaña, CE o UKCA).
{{< /callout >}}

Fuentes: [Recomendación CEPT ERC 70-03](https://docdb.cept.org/document/845),
Anexo 1, banda h1.7;
[Decisión de la Comisión 2006/771/CE](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
y sus modificaciones;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
banda O.

### Potencia: e.r.p. y tu antena {#erp}

El límite se aplica a la potencia *radiada*, medida respecto a una antena dipolo
simple (e.r.p.). La ganancia de la antena suma; la pérdida del cable resta. Los fabricantes indican
la ganancia de la antena en dBi, que son 2.15 dB más que la misma ganancia en dBd
(respecto a un dipolo). Mantén esta suma en 27 dBm (500 mW) o por debajo:

> potencia de transmisión (dBm) + ganancia de la antena (dBi) − pérdida del cable (dB) − 2.15 ≤ 27

- Una placa que transmite 22 dBm a una antena de 5 dBi con 1 dB de pérdida de cable:
  22 + 5 − 1 − 2.15 = 23.85 dBm, unos 240 mW e.r.p. Dentro del límite.
- Una placa con un amplificador de 30 dBm (1 W) y una antena de 3 dBi:
  30 + 3 − 2.15 = 30.85 dBm, unos 1.2 W e.r.p. Por encima del límite; baja la
  potencia de transmisión.

`set tx` fija la salida del chip LoRa, en dBm. El propio chip SX1262
llega como máximo a 22 dBm. El firmware no comprueba el número que introduces. Las placas con un
amplificador adicional, como la Heltec V4 o la Station G2, transmiten mucho más que
el número que fijas. Consulta la tabla del fabricante antes de ajustarlo y
empieza con un valor bajo.

### Ciclo de trabajo {#duty-cycle}

Un repetidor transmite para todos los que lo rodean, así que agota su tiempo de emisión antes
que un companion. El limitador de ciclo de trabajo de MeshCore viene al 50% por defecto, por encima
de lo que permite esta banda. Ajústalo al 10% en cada repetidor:

```text
set dutycycle 10
```

### Precisión de frecuencia {#frequency}

El canal EU/UK (Narrow), 869.618 MHz con 62.5 kHz de ancho de banda, llega hasta
869.649 MHz: menos de 1 kHz por debajo del límite superior de la subbanda. La señal
debe quedar dentro de la banda a cualquier temperatura. Para eso hace falta un
cristal compensado en temperatura (TCXO). Casi todas las placas actuales lo llevan.
Las placas antiguas sin él, como la Heltec V2, derivan demasiado para funcionar de forma fiable
a 62.5 kHz.

### Notas por país {#countries}

- **Los Estados miembros de la UE** deben poner esta subbanda a disposición en estas condiciones
  (Decisión 2006/771/CE, artículo 3).
- **Reino Unido:** los mismos límites, en la
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices) de Ofcom.
- **Suiza y Liechtenstein:** los mismos límites, en la
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09) de OFCOM.
- **Noruega:** los mismos límites, en el
  [reglamento sobre autorizaciones generales](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Estas notas no son asesoramiento legal. Las normas cambian; si tienes dudas, consulta
a tu regulador nacional.

## Lista de comprobación para la instalación {#checklist}

- [ ] El propietario del emplazamiento está de acuerdo y puedes acceder al repetidor para el mantenimiento.
- [ ] La placa lleva el firmware **Repeater** y has conectado la antena
      antes del primer encendido.
- [ ] Has cambiado la contraseña de administrador.
- [ ] La radio coincide con el [preset de tu zona](/guides/settings/) (`get radio`).
- [ ] Has ejecutado `set dutycycle 10`.
- [ ] La potencia de transmisión más la ganancia de la antena no superan los 500 mW e.r.p.
- [ ] El nombre, la posición y `owner.info` están configurados, para que otros sepan quién lo gestiona.
- [ ] La hora está ajustada (`clock`).
- [ ] La caja está sellada, con un orificio de drenaje o de ventilación, y el cable tiene un
      bucle de goteo.
- [ ] La batería y el panel están dimensionados para el peor mes de invierno.
- [ ] Lo has probado a distancia con la app antes de dejar el emplazamiento.
- [ ] Tu grupo local sabe que está en marcha.
