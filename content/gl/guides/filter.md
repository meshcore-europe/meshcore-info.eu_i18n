---
title: Filtro de paquetes
lead: 'Evita que o teu repetidor reenvíe lixo: inundacións de lonxe, un bot que nunca para, unha canle ruidosa. Proba primeiro un axuste e despois actívao.'
description: 'O filtro de paquetes do firmware de repetidor DMC: que descarta, axustes listos para un repetidor normal e para un con moito tráfico, cada orde do filtro co seu valor predeterminado e como ver o que descartou.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-11-02'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Un repetidor (un nodo que reenvía as mensaxes) repite todo o que escoita.
Nunha rede con moito tráfico, iso inclúe lixo. Un bot publica cada minuto. Un nodo envía
o seu anuncio, o saúdo que permite que outros o atopen, cada poucos minutos.
Chegan mensaxes que percorreron medio país. Cada repetición quítalles tempo de emisión
a todos os que están ao teu redor. Co filtro de paquetes, o teu repetidor descarta
ese tráfico en vez de reenvialo. Para saber primeiro que inunda a túa rede
e que axuda ademais do filtro, consulta
[Fai a rede resiliente](/guides/resilient/).

{{< callout type="warning" >}}
O filtro de paquetes forma parte do **firmware de repetidor DMC**, a compilación para repetidores
de [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). O MeshCore
estándar non ten filtro de paquetes; ten `region denyf *` e
`set flood.max.unscoped`, na páxina de [ordes da CLI](/guides/cli/). Esta
guía segue a compilación de desenvolvemento 1.18.0 `ecfb2d4` do 19 de outubro de 2026. A compilación estable
1.17.1 só ten os filtros de saltos, taxa, canle, hash e mensaxes defectuosas. Tampouco
ten dry-run.
{{< /callout >}}

## Que fai o filtro {#what}

O filtro só examina os paquetes que o teu repetidor reenvía por inundación (envíoos
a todos os nodos ao seu alcance). Nunca toca o que envía o propio repetidor
nin os paquetes que seguen unha ruta coñecida cara a un nodo. Tamén pasan as mensaxes directas
e as solicitudes que van ou veñen dos teus propios contactos. Pode descartar:

- paquetes que xa pasaron por tantos repetidores (saltos) como permites, por
  tipo de paquete;
- máis paquetes dun tipo dos que permites por minuto;
- un anuncio dun nodo que xa se anunciou nas últimas horas;
- mensaxes dunha canle que bloqueas;
- todo o que chegou a través dun repetidor que bloqueas;
- mensaxes de grupo dun remitente ou cunha palabra, ou só unha parte delas;
- mensaxes de grupo defectuosas ou máis antigas do que permites.

O filtro está **desactivado** ata que ti o activas. Configúralo con ordes. Escríbeas
por USB na [consola serie](/firmware/console/) deste sitio. Ou
envíaas desde a aplicación de MeshCore, como se explica na
[guía do repetidor](/repeater-guide/#config).

## Consegue o firmware {#firmware}

Grava **DutchMeshCore Repeater** co flasher da
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). O firmware de
observador de [MQTT no teu observador](/guides/mqtt/) ten o mesmo filtro.

## Próbao primeiro {#dryrun}

En modo dry-run, o filtro conta cada paquete que descartaría, pero segue reenviándoo.
Así podes axustar un valor antes de que descarte nada:

```text
filter on
filter dryrun on
```

Mentres dry-run está activo, a liña de estado de `filter` remata en `(dry-run)`. Os
contadores indican o que descartaría. Déixao funcionar un día e despois
revísaos (consulta [Que descartou](#stats)). Cando os números che parezan correctos, aplícao de verdade:

```text
filter dryrun off
```

## Configuracións recomendadas {#configs}

### Un repetidor normal {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Pasan ata 20 mensaxes de grupo por minuto e ata 5 mensaxes directas por minuto,
e o filtro descarta as mensaxes de grupo defectuosas. A configuración normal do propio firmware
permite 20 mensaxes directas por minuto. Esta páxina usa as 5 que o firmware aconsella
desde unha inundación de mensaxes directas en xullo de 2026.

### Un repetidor con moito tráfico {#busy}

Para un repetidor nun lugar alto que escoita toda unha rexión, ou para un que sofre
unha inundación:

```text
filter on
filter malformed on
filter rate 05 10 60
filter rate 02 5 60
filter rate 04 5 60
filter advert 24
filter hops 05 16
filter hops 02 16
filter hops 04 8
```

Isto reduce á metade as mensaxes de grupo e os anuncios, e deixa pasar o anuncio de cada nodo
unha vez ao día. Descarta as mensaxes que xa pasaron por 16 repetidores. Despois dun
reinicio, cada nodo consegue pasar un anuncio. A documentación do propio firmware tamén define
aquí `filter hash 2`; esta páxina omíteo (o motivo está en
[Todos os axustes](#settings)).

### Bloquea unha canle ruidosa {#channel}

```text
filter channel add #bot
```

O teu repetidor segue escoitando a canle. Xa non a reenvía a outros
repetidores nin aos companions (os nodos desde os que a xente envía mensaxes). Ata 16 canles.

### Limita a un remitente {#sender}

Un bot que publica demasiado nunha canle que queres conservar:

```text
filter watch add #test
filter sender add Bob 60
```

As mensaxes de Bob na canle Public e en `#test` agora pasan unha vez por minuto; o filtro
descarta o resto. O filtro compara o nome que aparece na mensaxe, así que un remitente que
cambia de nome consegue evitalo.

### Bloquea un repetidor anterior {#path}

Cando o lixo entra a través dun repetidor, bloquea o seu prefixo: a primeira
parte do seu ID, en hexadecimal (hex). Para isto necesitas a compilación de desenvolvemento 1.18; a 1.17.1
non ten filtro de ruta.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` mostra os prefixos que bloqueas, e `filter stats path` canto
descartou cada un. `filter path remove a1b2` volve deixalo pasar.
Un prefixo curto como `a1` tamén bloquea calquera outro repetidor cun ID que empece
por `a1`. Usa o prefixo máis longo que poidas. Ata 8 prefixos.

## Todos os axustes {#settings}

Os tipos de paquete indícanse por número. No repetidor, `filter types` mostra os mesmos
números cos nomes do firmware, como `TXT_MSG` e `GRP_TXT`:

| Número | Tipo | Número | Tipo |
| --- | --- | --- | --- |
| `00` | solicitude | `06` | datos de grupo |
| `01` | resposta | `07` | solicitude anónima |
| `02` | mensaxe directa | `08` | ruta |
| `03` | confirmación | `09` | traza |
| `04` | anuncio | `10` | multiparte |
| `05` | mensaxe de grupo | `11` | control |

| Orde | Que fai | Valor inicial |
| --- | --- | --- |
| `filter on` / `filter off` | Activa ou desactiva o filtro. | desactivado |
| `filter dryrun on` / `off` | Conta os descartes, pero segue reenviándoo todo. | desactivado |
| `filter hops <type> <max>` | Descarta un tipo que xa pasou por este número de repetidores, de 0 a 64. | 32 para mensaxes de grupo, 8 para o resto |
| `filter rate <type> <limit> <secs> [soft]` | Deixa pasar como máximo `limit` paquetes dun tipo por cada `secs`. Con `soft`, o paso redúcese aos poucos desde `soft` ata `limit`. `0` desactiva o límite. | 20 por 60 s para mensaxes directas e de grupo, 10 para anuncios, 5 para o resto |
| `filter advert <hours>` | Deixa pasar o anuncio de cada nodo unha vez por cada este número de horas, ata 720. | 0 (desactivado) |
| `filter channel add <#name>` | Deixa de reenviar unha canle. | ningunha |
| `filter path add <hex>` | Descarta todo o que chegou a través dun repetidor con este prefixo, de 2 a 8 díxitos hex. | ningún |
| `filter sender add <name> [secs] [prob]` | Descarta mensaxes de grupo dun remitente, en Public e nas canles vixiadas. `Bot*` coincide con todos os nomes que empezan por Bot. | ningún |
| `filter text add <word> [secs] [prob]` | Descarta mensaxes de grupo que conteñen unha palabra, en Public e nas canles vixiadas. `^word` só coincide ao principio. | ningún |
| `filter watch add <#name>` | Fai que as regras de remitente e de texto tamén lean esta canle, ata 4. Public sempre se le. | Public |
| `filter malformed on` / `off` | Descarta mensaxes de Public baleiras, defectuosas ou cunha data desviada máis dunha semana (a comprobación da data agarda a que o reloxo estea axustado). | desactivado |
| `filter age <minutes>` / `off` | Descarta mensaxes de grupo máis antigas ca isto, en Public e nas canles vixiadas, de 1 a 10080. | desactivado |
| `filter hash <bytes>` | Descarta paquetes cun ID de ruta máis curto ca este, de 1 a 3. | 1 |
| `filter reset` | Devolve todos os axustes ao seu valor predeterminado. | |

Cada `add` ten un `remove` e un `list`, como `filter channel remove #bot`.
Nas regras de remitente e de texto, `secs` deixa pasar unha mensaxe por cada ese número de segundos.
`prob` aplica a regra só a esa porcentaxe das coincidencias, de 1 a 100. Ata 8
regras de remitente e 8 de texto. Os nomes e as palabras distinguen maiúsculas e minúsculas; un nome ten ata
15 caracteres, unha palabra ata 23.

Dous axustes descartan máis do que podes esperar:

- `filter hash 2` descarta case todo o tráfico. Os nodos envían de forma predeterminada
  IDs de ruta de 1 byte.
- `filter age` fíase do reloxo do teu repetidor. Axústao con `clock sync` desde a
  aplicación, compróbao con `clock` e empeza cun valor xeneroso: `filter age 60`.

Todos os axustes consérvanse despois dun reinicio.

## Que descartou {#stats}

`filter` mostra os totais por motivo:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` mostra o detalle dun axuste. Os temas son
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` e `age`. `filter stats top` mostra o primeiro byte dos IDs dos nodos
responsables de máis descartes. Moitos nodos comparten ese byte.
`filter stats air` mostra o tempo de emisión que aforrou o teu repetidor ao non reenviar
estes paquetes.

Os contadores volven a 0 despois dun reinicio e despois de `clear stats`.
