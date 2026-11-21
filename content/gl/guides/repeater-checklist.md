---
title: Lista de comprobación do repetidor
lead: Comproba o teu repetidor antes de subilo. Cada liña indica que comprobar, o comando que o mostra e a guía que o explica.
description: 'Unha lista de comprobación para un repetidor MeshCore antes de levalo a un tellado ou a un mastro: que comprobar por USB, como montalo e a proba antes de marchar.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Un repetidor nun tellado é difícil de alcanzar, así que compróbao mentres aínda o tes
na mesa. A [guía do repetidor](/repeater-guide/) explica cada paso. Os
valores, como o preset e os límites de saltos, saen da
[configuración da túa zona](/guides/settings/). Escribe os comandos por USB, por
exemplo na [consola serie](/firmware/console/). Esta lista segue o firmware
MeshCore v1.18.0.

## Antes de comezar {#start}

- [ ] Os [mapas de cobertura](/map/) ou o teu [grupo local](/community/) indican
      que a zona precisa un repetidor. Consulta [Precisas un?](/repeater-guide/#need)
- [ ] O dono do lugar está de acordo e podes acceder ao repetidor para o
      mantemento.
- [ ] A batería e o panel están dimensionados para o peor mes do inverno.
      Consulta [Enerxía e dimensionamento solar](/repeater-guide/#power).

## Na mesa, por USB {#usb}

- [ ] A placa leva o firmware **Repeater**: `ver` mostra a súa versión. Consulta
      [Configúrao](/repeater-guide/#config).
- [ ] Nunha placa nRF52, a resposta a `get bootloader.ver` contén `OTAFIX`.
      Consulta [Actualízao polo aire](/repeater-guide/#update).
- [ ] `get radio` mostra o preset da túa zona.
- [ ] `get dutycycle` mostra 10. Consulta [Ciclo de traballo](/repeater-guide/#duty-cycle).
- [ ] `get tx` máis a ganancia da túa antena non supera os 500 mW e.r.p. Consulta
      [Potencia: e.r.p. e a túa antena](/repeater-guide/#erp).
- [ ] O contrasinal de administración xa non é `password`.
- [ ] `get guest.password` mostra un contrasinal.
- [ ] `get name` mostra o nome que o teu grupo local usa para os seus repetidores.
- [ ] `get lat` e `get lon` mostran a posición do lugar.
- [ ] `get owner.info` mostra como te contactan outros operadores.
- [ ] `region` mostra as rexións da túa zona. `get flood.max.advert` e
      `get flood.max.unscoped` mostran os límites de saltos da zona. Consulta
      [Reduce o tráfico](/guides/settings/#traffic).
- [ ] Gardaches nun lugar seguro a chave privada de `get prv.key`.
- [ ] `clock` mostra a hora actual, en UTC.
- [ ] Con enerxía solar, `powersaving` mostra `on`.

## No tellado {#roof}

- [ ] A antena está conectada antes de que o repetidor reciba corrente.
- [ ] A antena está vertical no alto do mastro, lonxe do metal. Consulta
      [Montaxe](/guides/antenna/#mounting).
- [ ] Cada conector exterior está selado e o cable ten un bucle de goteo.
- [ ] A caixa está pechada, cun respiradoiro ou un burato de drenaxe. Consulta
      [Hardware](/repeater-guide/#hardware).

## Antes de marchar {#leave}

- [ ] Desde lonxe, o teu companion chega ao repetidor na app.
- [ ] Enviaches `advert`, para que os nodos de toda a malla coñezan o repetidor.
- [ ] O teu [grupo local](/community/) sabe que está en funcionamento.
