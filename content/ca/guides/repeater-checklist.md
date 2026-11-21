---
title: Llista de comprovació del repetidor
lead: Revisa el repetidor abans d'instal·lar-lo a dalt. Cada línia indica què has de revisar, l'ordre que ho mostra i la guia que ho explica.
description: 'Una llista de comprovació per a un repetidor MeshCore abans de pujar-lo a un terrat o a un pal: què revises per USB, com el muntes i la prova que fas abans de marxar.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Costa arribar a un repetidor en un terrat, així que revisa'l mentre encara
el tens a la taula. La [guia del repetidor](/repeater-guide/) explica cada pas.
Els valors, com el preset i els límits de salts, surten de la
[configuració de la teva zona](/guides/settings/). Escriu les ordres per USB,
per exemple a la [consola sèrie](/firmware/console/). Aquesta llista es basa en
el firmware MeshCore v1.18.0.

## Abans de començar {#start}

- [ ] Els [mapes de cobertura](/map/) o el teu [grup local](/community/) diuen
      que la zona necessita un repetidor. Consulta [Te'n cal un?](/repeater-guide/#need)
- [ ] El propietari de l'emplaçament hi està d'acord, i pots accedir al
      repetidor per fer-ne el manteniment.
- [ ] Has dimensionat la bateria i el panell per al pitjor mes d'hivern.
      Consulta [Dimensionament de l'energia i el solar](/repeater-guide/#power).

## A la taula, per USB {#usb}

- [ ] La placa porta el firmware **Repeater**: `ver` en mostra la versió.
      Consulta [Configura'l](/repeater-guide/#config).
- [ ] En una placa nRF52, la resposta a `get bootloader.ver` conté `OTAFIX`.
      Consulta [Actualitza'l per ràdio](/repeater-guide/#update).
- [ ] `get radio` mostra el preset de la teva zona.
- [ ] `get dutycycle` mostra 10. Consulta [Cicle de treball](/repeater-guide/#duty-cycle).
- [ ] El valor de `get tx` més el guany de l'antena no supera 500 mW e.r.p.
      Consulta [Potència: e.r.p. i la teva antena](/repeater-guide/#erp).
- [ ] La contrasenya d'administrador ja no és `password`.
- [ ] `get guest.password` mostra una contrasenya.
- [ ] `get name` mostra el nom que el teu grup local fa servir per als seus
      repetidors.
- [ ] `get lat` i `get lon` mostren la posició de l'emplaçament.
- [ ] `get owner.info` mostra com et poden contactar altres operadors.
- [ ] `region` mostra les regions de la teva zona. `get flood.max.advert` i
      `get flood.max.unscoped` en mostren els límits de salts. Consulta
      [Redueix el trànsit](/guides/settings/#traffic).
- [ ] Has guardat en un lloc segur la clau privada que mostra `get prv.key`.
- [ ] `clock` mostra l'hora actual, en UTC.
- [ ] Amb energia solar, `powersaving` mostra `on`.

## Al terrat {#roof}

- [ ] Has connectat l'antena abans de donar corrent al repetidor.
- [ ] L'antena queda dreta a dalt del pal, lluny del metall. Consulta
      [Muntatge](/guides/antenna/#mounting).
- [ ] Has segellat cada connector exterior, i el cable fa un bucle de goteig.
- [ ] La caixa està tancada, amb un forat de ventilació o de drenatge. Consulta
      [Maquinari](/repeater-guide/#hardware).

## Abans de marxar {#leave}

- [ ] Des de lluny, arribes al repetidor amb el teu companion, a l'app.
- [ ] Has enviat `advert`, perquè els nodes de tota la malla coneguin el
      repetidor.
- [ ] El teu [grup local](/community/) sap que ja funciona.
