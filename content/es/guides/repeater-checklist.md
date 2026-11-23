---
title: Lista de comprobación del repetidor
lead: Revisa tu repetidor antes de subirlo. Cada línea indica qué comprobar, qué comando lo muestra y qué guía lo explica.
description: 'Una lista de comprobación para un repetidor MeshCore antes de instalarlo en un tejado o un mástil: qué comprobar por USB, cómo montarlo y la prueba antes de irte.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Un repetidor en un tejado es difícil de alcanzar. Por eso, revísalo mientras
aún está en tu mesa. La [guía del repetidor](/repeater-guide/) explica cada
paso. Los valores, como el preajuste y los límites de saltos, salen de los
[ajustes de tu zona](/guides/settings/). Escribe los comandos por USB, por
ejemplo en la [consola serie](/firmware/console/). Esta lista corresponde al
firmware de MeshCore v1.18.0.

## Antes de empezar {#start}

- [ ] Los [mapas de cobertura](/map/) o tu [grupo local](/community/) indican
      que la zona necesita un repetidor. Consulta [¿Te hace falta uno?](/repeater-guide/#need)
- [ ] El propietario del lugar está de acuerdo y puedes acceder al repetidor
      para el mantenimiento.
- [ ] Has dimensionado la batería y el panel para el peor mes de invierno.
      Consulta [Alimentación y dimensionado solar](/repeater-guide/#power).

## En tu mesa, por USB {#usb}

- [ ] La placa lleva el firmware **Repeater**: `ver` muestra su versión.
      Consulta [Configúralo](/repeater-guide/#config).
- [ ] En una placa nRF52, la respuesta a `get bootloader.ver` contiene
      `OTAFIX`. Consulta [Actualízalo por radio](/repeater-guide/#update).
- [ ] `get radio` muestra el preajuste de tu zona.
- [ ] `get dutycycle` muestra 10. Consulta [Ciclo de trabajo](/repeater-guide/#duty-cycle).
- [ ] `get tx` más la ganancia de tu antena no supera los 500 mW e.r.p. Consulta
      [Potencia: e.r.p. y tu antena](/repeater-guide/#erp).
- [ ] La contraseña de administrador ya no es `password`.
- [ ] `get guest.password` muestra una contraseña.
- [ ] `get name` muestra el nombre que usa tu grupo local para sus repetidores.
- [ ] `get lat` y `get lon` muestran la posición del lugar.
- [ ] `get owner.info` muestra cómo pueden contactarte otros operadores.
- [ ] `region` muestra las regiones de tu zona. `get flood.max.advert` y
      `get flood.max.unscoped` muestran sus límites de saltos. Consulta
      [Reduce el tráfico](/guides/settings/#traffic).
- [ ] Has guardado en un sitio seguro la clave privada que da `get prv.key`.
- [ ] `clock` muestra la hora actual, en UTC.
- [ ] Con energía solar, `powersaving` muestra `on`.

## En el tejado {#roof}

- [ ] Has conectado la antena antes de alimentar el repetidor.
- [ ] La antena está en vertical en lo alto del mástil, lejos del metal.
      Consulta [Montaje](/guides/antenna/#mounting).
- [ ] Todos los conectores exteriores están sellados y el cable tiene un bucle
      de goteo.
- [ ] La caja está cerrada y tiene un respiradero o un orificio de drenaje.
      Consulta [Hardware](/repeater-guide/#hardware).

## Antes de irte {#leave}

- [ ] Desde lejos, tu companion alcanza el repetidor en la app.
- [ ] Has enviado `advert` para que los nodos de toda la malla conozcan el repetidor.
- [ ] Tu [grupo local](/community/) sabe que el repetidor ya funciona.
