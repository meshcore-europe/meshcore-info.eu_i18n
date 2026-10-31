---
title: Definições recomendadas
layout: settings
lead: O preset de rádio que a tua zona usa e as definições que os teus vizinhos alteraram. Escolhe o teu país, define o preset e copia os comandos.
description: O preset de rádio do MeshCore por zona na Europa e as definições de repetidor e companion que os grupos locais alteraram face aos valores predefinidos, com os comandos.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-10-31'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Cada zona abaixo usa o seu próprio preset de rádio ou altera alguns dos
valores predefinidos do MeshCore. Tudo o que não está na lista fica com o
valor predefinido, por isso só alteras o que a tua zona alterou. Um repetidor
reencaminha mensagens para todos. Um companion é o nó a partir do qual envias
mensagens: está emparelhado com o teu telemóvel ou portátil por Bluetooth ou
USB, ou tem o seu próprio ecrã.

No [guia do repetidor](/repeater-guide/#config) vês como aceder à linha de
comandos do teu repetidor. Na [consola série](/firmware/console/) deste site
escreves tu próprio os comandos. Em cada zona também podes enviar as
definições por USB. O guia indica ainda os [limites legais](/repeater-guide/#legal)
nos 868 MHz.

## Reduz o tráfego {#traffic}

Estas definições valem para todas as zonas. Cada repetidor reencaminha todas
as mensagens flood que ouve. Uma mensagem tua custa uma transmissão, mais uma
por cada repetidor que a ouve. Com o duty cycle de 10%, um repetidor pode
enviar cerca de 680 pacotes por hora. Todos à volta dele partilham esse
número. Uma mensagem que vai mais longe do que precisa gasta parte dele.

**Envia para a região mais pequena que alcança as pessoas a quem escreves.**
As regiões encaixam umas nas outras: um país, uma província, um grupo local.
Cada uma tem o seu código, como `nl`, `nl-ov` e `nl-ov-zwo`. Uma mensagem para
`nl-ov-zwo` fica nos repetidores desse grupo. Um repetidor só reencaminha as
regiões que ele próprio tem: ter `nl` não faz com que reencaminhe `nl-ov`.
Coloca cada repetidor em todas as regiões que serve, e só nessas. O teu
[grupo local](/community/) sabe quais são.

**Limita o que o teu repetidor reencaminha.** Com duas definições, o tráfego
que não precisa de ir longe fica perto de casa:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: os anúncios, que apresentam um nó à mesh, percorrem
  no máximo 3 saltos.
- `flood.max.unscoped 1`: uma mensagem sem região passa no máximo por um
  repetidor.
