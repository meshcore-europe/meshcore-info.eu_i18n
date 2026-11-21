---
title: Lista de verificação do repetidor
lead: Verifica o teu repetidor antes de o instalares. Cada linha diz o que verificar, o comando que o mostra e o guia que o explica.
description: 'Uma lista de verificação para um repetidor MeshCore antes de ir para um telhado ou mastro: o que verificar por USB, como o montar e o teste antes de te ires embora.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Um repetidor num telhado é difícil de alcançar. Por isso, verifica-o enquanto ainda está na tua secretária. O [guia do repetidor](/repeater-guide/) explica cada passo. Os valores, como a predefinição e os limites de saltos, vêm das [definições da tua zona](/guides/settings/). Escreve os comandos por USB, por exemplo na [consola série](/firmware/console/). Esta lista segue o firmware MeshCore v1.18.0.

## Antes de começares {#start}

- [ ] Os [mapas de cobertura](/map/) ou o teu [grupo local](/community/) indicam
      que a zona precisa de um repetidor. Vê [Precisas de um?](/repeater-guide/#need)
- [ ] O dono do local deu autorização e consegues chegar ao repetidor para a
      manutenção.
- [ ] A bateria e o painel estão dimensionados para o pior mês de inverno. Vê
      [Energia e dimensionamento solar](/repeater-guide/#power).

## Na tua secretária, por USB {#usb}

- [ ] A placa corre o firmware **Repeater**: `ver` mostra a versão. Vê
      [Configura-o](/repeater-guide/#config).
- [ ] Numa placa nRF52, a resposta a `get bootloader.ver` contém `OTAFIX`.
      Vê [Atualiza-o sem fios](/repeater-guide/#update).
- [ ] `get radio` mostra a predefinição da tua zona.
- [ ] `get dutycycle` mostra 10. Vê [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] O valor de `get tx` somado ao ganho da tua antena não passa de 500 mW e.r.p.
      Vê [Potência: e.r.p. e a tua antena](/repeater-guide/#erp).
- [ ] A palavra-passe de administrador já não é `password`.
- [ ] `get guest.password` mostra uma palavra-passe.
- [ ] `get name` mostra o nome que o teu grupo local usa para os repetidores.
- [ ] `get lat` e `get lon` mostram a posição do local.
- [ ] `get owner.info` mostra como os outros operadores te contactam.
- [ ] `region` mostra as regiões da tua zona. `get flood.max.advert` e
      `get flood.max.unscoped` mostram os respetivos limites de saltos. Vê
      [Reduz o tráfego](/guides/settings/#traffic).
- [ ] Guardaste a chave privada de `get prv.key` num sítio seguro.
- [ ] `clock` mostra a hora atual, em UTC.
- [ ] Com energia solar, `powersaving` mostra `on`.

## No telhado {#roof}

- [ ] A antena está ligada antes de o repetidor receber energia.
- [ ] A antena está na vertical, no topo do mastro, longe de metal. Vê
      [Montagem](/guides/antenna/#mounting).
- [ ] Todos os conectores exteriores estão vedados e o cabo tem uma curva de
      escoamento.
- [ ] A caixa está fechada, com um respiradouro ou um furo de drenagem. Vê
      [Hardware](/repeater-guide/#hardware).

## Antes de te ires embora {#leave}

- [ ] À distância, o teu companion alcança o repetidor na app.
- [ ] Enviaste `advert`, para que os nós de toda a mesh fiquem a conhecer o
      repetidor.
- [ ] O teu [grupo local](/community/) sabe que o repetidor já está a funcionar.
