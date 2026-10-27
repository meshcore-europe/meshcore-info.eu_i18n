---
title: Guía de repetidores
lead: Un repetidor colocado en alto reenvía los mensajes de todos los que tiene alrededor, por todo un pueblo o un valle. Elige un sitio, aliméntalo con el sol, configúralo y respeta la ley.
description: 'Planifica, alimenta, configura y opera legalmente un repetidor MeshCore en Europa: elección del sitio, cálculo solar, ajustes de la CLI, potencia en 868 MHz y límites de ciclo de trabajo.'
eyebrow: 868 MHz · hasta 500 mW · sin licencia
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '4a0fe39f'
  seeded: '2026-10-26'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['1de4a4f7', '766086be', '70faf508', '8bc641aa', '2018aa04', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
---

Los repetidores sostienen la malla. Los companions, las radios desde las que escribes, no reenvían mensajes. Sin repetidores solo llegas a quienes están a tu alcance directo. Cada repetidor que instalas amplía la malla para todos los que tiene alrededor. Esta guía sigue el firmware v1.18.0 de MeshCore.

Antes de empezar, habla con tu [grupo local](/community/). Ellos saben dónde falta cobertura, qué [preajuste usa tu zona](/guides/settings/) y cómo se nombran los repetidores. Mira los [mapas de cobertura](/map/) para ver los repetidores cercanos y saluda en los [canales](/guides/channels/) públicos o locales.

## Elige un sitio {#site}

La altura vale más que la potencia. LoRa en 868 MHz viaja mejor con línea de visión despejada. Colinas, edificios y árboles densos quitan mucho más alcance del que recuperan unos milivatios extra.

- **Sube alto.** Un tejado, un mástil, un edificio alto o una colina cubren mucho más que un alféizar. Incluso unos metros por encima de los tejados vecinos ayudan.
- **Deja la antena despejada.** Móntala por encima del borde del tejado, lejos de metales, canalones y otras antenas.
- **Comprueba la vista.** Herramientas como [HeyWhatsThat](https://www.heywhatsthat.com/) muestran qué se ve desde un lugar. Si ves un punto, un repetidor allí está a tu alcance.
- **Deja espacio libre.** Un enlace de radio necesita algo de espacio alrededor de la línea directa, no solo la línea. En distancias largas, el centro del trayecto debe librar los obstáculos por varios metros.
- **Pide permiso.** Consigue el consentimiento del dueño del tejado o del mástil, y acuerda cómo llegarás al repetidor para mantenerlo.

## Hardware {#hardware}

- **Placa.** Elige una placa nRF52 de bajo consumo, como la [Heltec T114](/devices/), RAK WisBlock o el SenseCAP Solar Node. Las placas ESP32 consumen más (la página de dispositivos las marca como High), y eso dificulta alimentarlas con sol.
- **Antena.** Usa una antena hecha para 868 MHz, montada en vertical. La [guía de antenas](/guides/antenna/) explica tipos, conectores, cable y montaje. La ganancia de la antena cuenta para el límite legal de potencia; mira [Límites legales](#legal).
- **Cable.** Usa cable coaxial corto, o cable de bajas pérdidas. En 868 MHz, unos metros de cable fino pueden perder la mitad de tu potencia.
- **Caja.** Una caja estanca (IP65 o mejor) con prensaestopas, un orificio de ventilación o drenaje contra la condensación, y color claro o parasol. Las baterías sufren con el calor y no se pueden cargar bajo cero.
- **Rayos.** Una antena en un tejado es un blanco. Sigue las normas locales de puesta a tierra, o móntala donde un impacto no alcance el cableado del edificio.

## Alimentación y cálculo solar {#power}

Un repetidor solar debe sobrevivir a las semanas más oscuras del invierno. Dimensiónalo para ellas:

1. **Mide el consumo.** Conecta el repetidor ya configurado a un medidor de potencia USB durante un día. Lee la energía usada en vatios-hora (Wh). El tráfico de tu zona cambia la cifra, así que mide en el sitio si puedes.
2. **Añade reserva.** Calcula la capacidad de la batería para al menos 5 a 7 días sin sol útil.
3. **Averigua tu sol de invierno.** La herramienta gratuita de la UE [PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) muestra, para cualquier lugar, cuánta energía produce un panel cada mes. Usa el mes con menos sol.
4. **Dimensiona el panel.** El panel debe reponer el consumo diario en ese peor mes, con margen para las pérdidas de carga.

Un ejemplo con cifras supuestas: un repetidor que consume 1 Wh al día necesita una batería de al menos 7 Wh para una semana de reserva, unos 2 Ah de capacidad útil a 3,7 V. Si PVGIS dice que un panel de 1 W en tu sitio da 0,5 Wh al día en diciembre, necesitas al menos un panel de 2 W, y uno de 3 a 5 W deja margen para nubes, nieve y envejecimiento.

## Configúralo {#config}

**Flashea.** Usa el [flasher web](https://flasher.meshcore.io) y elige el firmware **Repeater** para tu placa. Los pasos del flasheo están en [Primeros pasos](/get-started/#flash).

**Configura por USB.** Con el repetidor aún conectado al ordenador, abre [config.meshcore.io](https://config.meshcore.io) o la consola del flasher. También puedes usar cualquier terminal serie a 115200 baudios. Los comandos más importantes:

| Qué | Comando |
|---|---|
| Cambiar la contraseña de administrador | `password <new password>` |
| Ponerle nombre | `set name <name>` |
| Preajuste de radio: frecuencia, ancho de banda, SF, CR (reinicia para aplicarlo) | `set radio 869.618,62.5,8,8` |
| Límite de ciclo de trabajo, en porcentaje | `set dutycycle 10` |
| Potencia de transmisión del chip de radio, en dBm | `set tx <dBm>` |
| Posición, para que aparezca en los mapas | `set lat <degrees>` y `set lon <degrees>` |
| Datos de contacto para otros operadores | `set owner.info <text>` |
| Horas entre anuncios por inundación, los que oye toda la malla | `set flood.advert.interval <hours>` |
| Anunciarlo ahora | `advert` |
| Reiniciar | `reboot` |

La contraseña de administrador por defecto es `password`, y cualquiera que entre con ella se convierte en administrador. Cámbiala antes de que el repetidor salga al aire.

El ejemplo de `set radio` de arriba es EU/UK (Narrow). Usa en su lugar los valores del preajuste de tu zona: [Ajustes recomendados](/guides/settings/) los lista por país.

**Pon en hora el reloj.** Sin módulo de reloj (RTC), un repetidor pierde la hora con cada corte de luz y arranca en mayo de 2024, y mientras funciona su reloj se desvía. Entra en remoto desde la app y usa `clock sync`, o pon la hora por USB. Un módulo RTC es un añadido que merece la pena en un repetidor: conserva la hora durante los cortes y se desvía mucho menos.

**Gestiónalo en remoto.** Cuando ya esté en la malla, entra desde la app de MeshCore con la contraseña de administrador. Allí lees su estado y usas los mismos comandos por radio. Algunos comandos solo funcionan por USB, como `set freq` y el restablecimiento de fábrica `erase`.

La lista completa de comandos está en la [referencia de la CLI de MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Límites legales {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Los preajustes europeos de MeshCore están en la subbanda **869.40-869.65 MHz**. En la UE, el Reino Unido, Suiza y Noruega está abierta a dispositivos de corto alcance sin licencia, dentro de estos límites:

- como máximo **500 mW e.r.p.** de potencia radiada;
- como máximo **10% de ciclo de trabajo**: no más de 360 segundos de transmisión en cualquier hora, por dispositivo. Como alternativa, un dispositivo puede usar escucha antes de transmitir con agilidad de frecuencia adaptativa según define ETSI EN 300 220-2;
- toda la señal, de 250 kHz de ancho como máximo, debe quedar dentro de la subbanda.

La banda es compartida: no debes perturbar servicios con licencia, y otros pueden perturbarte a ti.
La radio debe llevar marcado CE (en Gran Bretaña, CE o UKCA).
{{< /callout >}}

Fuentes: [Recomendación ERC 70-03 de la CEPT](https://docdb.cept.org/document/845), anexo 1, banda h1.7;
[Decisión 2006/771/CE de la Comisión](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) y sus modificaciones;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), banda O.

### Potencia: e.r.p. y tu antena {#erp}

El límite se aplica a la potencia *radiada*, medida frente a una antena dipolo simple (e.r.p.). La ganancia de la antena suma; la pérdida del cable resta. Los fabricantes indican la ganancia de la antena en dBi, que son 2.15 dB más que la misma ganancia en dBd (relativa a un dipolo). Mantén esta suma en 27 dBm (500 mW) o por debajo:

> potencia de transmisión (dBm) + ganancia de la antena (dBi) − pérdida del cable (dB) − 2.15 ≤ 27

- Una placa que transmite 22 dBm a una antena de 5 dBi a través de 1 dB de cable:
  22 + 5 − 1 − 2.15 = 23.85 dBm, unos 240 mW e.r.p. Dentro del límite.
- Una placa con un amplificador de 30 dBm (1 W) a una antena de 3 dBi:
  30 + 3 − 2.15 = 30.85 dBm, unos 1.2 W e.r.p. Supera el límite; baja la potencia de transmisión.

`set tx` fija la salida del chip LoRa, en dBm. El chip SX1262 llega como máximo a 22 dBm; el firmware no comprueba el número que introduces. Las placas con amplificador extra, como la Heltec V4 o la Station G2, transmiten mucho más que el número que fijas. Consulta la tabla del fabricante antes de fijarlo, y empieza bajo.

### Ciclo de trabajo {#duty-cycle}

Un repetidor transmite para todos los que tiene alrededor, así que gasta su tiempo en el aire más rápido que un companion. El limitador de ciclo de trabajo de MeshCore viene por defecto al 50%, más de lo que permite esta banda. Ponlo al 10% en cada repetidor:

```text
set dutycycle 10
```

### Precisión de frecuencia {#frequency}

El canal EU/UK (Narrow), 869.618 MHz con 62.5 kHz de ancho de banda, llega hasta 869.649 MHz: menos de 1 kHz por debajo del tope de la subbanda. La señal debe quedarse dentro de la banda a cualquier temperatura. Eso exige un cristal con compensación de temperatura (TCXO). Casi todas las placas actuales lo llevan; las placas antiguas sin él, como la Heltec V2, se desvían demasiado para funcionar con fiabilidad a 62.5 kHz.

### Notas por país {#countries}

- **Los Estados miembros de la UE** deben habilitar esta subbanda en estas condiciones (Decisión 2006/771/CE, artículo 3).
- **Reino Unido:** los mismos límites, en la [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices) de Ofcom.
- **Suiza y Liechtenstein:** los mismos límites, en la [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09) de la OFCOM.
- **Noruega:** los mismos límites, en el [reglamento de autorizaciones generales](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Estas notas no son asesoramiento legal. Las normas cambian; en caso de duda, consulta a tu regulador nacional.

## Lista de comprobación para la instalación {#checklist}

- [ ] El dueño del sitio está de acuerdo, y puedes llegar al repetidor para mantenerlo.
- [ ] La placa lleva el firmware **Repeater**, y la antena se conectó antes del primer encendido.
- [ ] La contraseña de administrador está cambiada.
- [ ] La radio coincide con [el preajuste de tu zona](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` está aplicado.
- [ ] La potencia de transmisión más la ganancia de la antena se queda dentro de 500 mW e.r.p.
- [ ] El nombre, la posición y `owner.info` están puestos, para que otros sepan quién lo opera.
- [ ] El reloj está en hora (`clock`).
- [ ] La caja está sellada, con orificio de drenaje o ventilación, y el cable tiene un bucle antigoteo.
- [ ] La batería y el panel están dimensionados para el peor mes de invierno.
- [ ] Lo probaste a distancia con la app antes de irte del sitio.
- [ ] Tu grupo local sabe que está en marcha.
