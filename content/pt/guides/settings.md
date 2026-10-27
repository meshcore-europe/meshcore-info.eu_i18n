---
title: Definições recomendadas
layout: settings
lead: A predefinição de rádio que a tua zona usa, e as definições que os teus vizinhos alteraram. Escolhe o teu país, aplica a predefinição e copia os comandos.
description: A predefinição de rádio do MeshCore por zona na Europa, e as definições de repetidor e companion que os grupos locais alteraram face aos valores por omissão, com os comandos.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '9547ba62'
  seeded: '2026-10-26'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', '43cde8b4']
---

Cada zona abaixo usa a sua própria predefinição de rádio, ou altera alguns
valores por omissão do MeshCore. Tudo o que não está listado fica no valor por
omissão, por isso só alteras o que a tua zona alterou. Um repetidor reencaminha
mensagens para toda a gente. Um companion é o nó a partir do qual envias
mensagens, emparelhado com o teu telemóvel ou portátil por Bluetooth ou USB, ou
com ecrã próprio.

O [guia de repetidores](/repeater-guide/#config) mostra como aceder à linha de
comandos do teu repetidor. Na [consola série](/firmware/console/) deste site
escreves tu próprio os comandos. Em cada zona podes também enviar as respetivas
definições por USB. O guia lista ainda os [limites legais](/repeater-guide/#legal)
nos 868 MHz.

## Reduz o tráfego {#traffic}

Estas definições aplicam-se a todas as zonas. Cada repetidor reencaminha todas
as mensagens flood que ouve. Uma mensagem tua custa uma transmissão, mais uma
por cada repetidor que a ouve. Com o duty cycle de 10%, um repetidor pode
enviar cerca de 680 pacotes por hora, e toda a gente à volta partilha esse
número. Uma mensagem que viaja mais longe do que precisa gasta parte dele.

**Envia para a região mais pequena que chega às pessoas a quem escreves.**
As regiões encaixam umas nas outras: um país, uma província, um grupo local,
cada um com o seu código, como `nl`, `nl-ov` e `nl-ov-zwo`. Uma mensagem para
`nl-ov-zwo` fica nos repetidores desse grupo. Coloca cada repetidor apenas nas
regiões que ele serve. O teu [grupo local](/community/) sabe quais são.

**Limita o que o teu repetidor reencaminha.** Duas definições mantêm perto de
casa o tráfego que não precisa de viajar longe:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: os anúncios, que dão a conhecer um nó à mesh, viajam
  no máximo 3 saltos.
- `flood.max.unscoped 1`: uma mensagem sem região passa no máximo por um
  repetidor.
