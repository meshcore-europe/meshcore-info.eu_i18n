---
title: Filtro de pacotes
lead: 'Impede que o teu repetidor passe lixo adiante: floods vindos de longe, um bot que nunca para, um canal ruidoso. Experimenta primeiro uma configuração e só depois a ativas.'
description: 'O filtro de pacotes do firmware de repetidor DMC: o que descarta, configurações prontas para um repetidor normal e um repetidor muito ocupado, todos os comandos do filtro com o seu valor por omissão, e como ver o que foi descartado.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '2bf23d24'
  seeded: '2026-10-26'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['0625daa2', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', 'ffc3f3a0', '3fa1bb28', '09511608']
---

Um repetidor (um nó que passa mensagens adiante) repete tudo o que ouve.
Numa mesh ocupada, isso inclui lixo. Um bot publica a cada minuto. Um nó envia
o seu anúncio, o "olá" que permite aos outros encontrá-lo, outra vez a cada
poucos minutos. Chegam mensagens que atravessaram meio país. Cada repetição
rouba tempo de antena a todos à tua volta. Com o filtro de pacotes, o teu
repetidor descarta esse tráfego em vez de o passar adiante.

{{< callout type="warning" >}}
O filtro de pacotes faz parte do **firmware de repetidor DMC**, a versão
para repetidor do [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore).
O MeshCore original não tem filtro de pacotes; tem `region denyf *` e
`set flood.max.unscoped`, na página [Comandos CLI](/guides/cli/). Este
guia segue a versão de desenvolvimento 1.18.0 `ecfb2d4`, de 19 de outubro de
2026. A versão estável 1.17.1 tem apenas os filtros de saltos, ritmo, canal,
hash e malformados. Também não tem modo de simulação.
{{< /callout >}}

## O que o filtro faz {#what}

O filtro só olha para os pacotes que o teu repetidor passa adiante por flood
(enviando-os a todos os nós ao alcance). Nunca toca no que o teu repetidor
envia por si, nem nos pacotes que seguem um caminho conhecido até um nó.
As mensagens diretas e os pedidos de e para os teus próprios contactos também
passam. Pode descartar:

- pacotes que já passaram por tantos repetidores (saltos) quantos permites,
  por tipo de pacote;
- mais pacotes de um tipo do que permites por minuto;
- um anúncio de um nó que já se anunciou nas últimas horas;
- mensagens num canal que bloqueias;
- tudo o que veio através de um repetidor que bloqueias;
- mensagens de grupo de um remetente ou com uma palavra, ou só parte delas;
- mensagens de grupo corrompidas, ou mais antigas do que permites.

O filtro está **desligado** até o ativares. Configura-lo com comandos.
Escreve-os por USB na [consola série](/firmware/console/) deste site. Ou
envia-os a partir da app MeshCore, como no
[guia do repetidor](/repeater-guide/#config).

## Obter o firmware {#firmware}

Grava o **DutchMeshCore Repeater** com o flasher da
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). O firmware de
observador em [MQTT no teu observador](/guides/mqtt/) tem o mesmo filtro.

## Experimenta primeiro {#dryrun}

Em modo de simulação, o filtro conta cada pacote que descartaria, mas
continua a passá-lo adiante. Dimensiona uma configuração assim antes de ela
descartar seja o que for:

```text
filter on
filter dryrun on
```

Enquanto o modo de simulação está ligado, a linha de estado de `filter`
termina em `(dry-run)`. As contagens são o que teria sido descartado.
Deixa-o a correr um dia e depois vê os números (consulta
[O que descartou](#stats)). Quando os números parecerem certos, aplica o
filtro a sério:

```text
filter dryrun off
```

## Configurações recomendadas {#configs}

### Um repetidor normal {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Passam até 20 mensagens de grupo por minuto e até 5 mensagens diretas por
minuto, e as mensagens de grupo corrompidas são descartadas. A configuração
normal do próprio firmware permite 20 mensagens diretas por minuto. Esta
página adota as 5 que ele recomenda desde um flood de mensagens diretas em
julho de 2026.

### Um repetidor muito ocupado {#busy}

Para um repetidor num ponto alto que ouve uma região inteira, ou para um que
está a ser inundado:

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

Isto reduz para metade as mensagens de grupo e os anúncios, e passa o anúncio
de cada nó uma vez por dia. Descarta mensagens que já passaram por 16
repetidores. Depois de um reinício, cada nó consegue passar um anúncio. A
documentação do próprio firmware também define aqui `filter hash 2`; esta
página deixa-o de fora (vê porquê em [Todas as definições](#settings)).

### Bloquear um canal ruidoso {#channel}

```text
filter channel add #bot
```

O teu repetidor continua a ouvir o canal. Deixa de o passar adiante a outros
repetidores e companions (os nós a partir dos quais as pessoas enviam
mensagens). Até 16 canais.

### Abrandar um remetente {#sender}

Um bot que publica demasiadas vezes num canal que queres manter:

```text
filter watch add #test
filter sender add Bob 60
```

As mensagens do Bob no canal Public e em `#test` passam agora uma vez por
minuto; o resto é descartado. O filtro compara o nome que vem na mensagem, por
isso um remetente que mude de nome escapa-lhe.

### Bloquear um repetidor a montante {#path}

Quando o lixo entra através de um repetidor, bloqueia o seu prefixo: a
primeira parte do seu ID, em hexadecimal (hex).

```text
filter path add a1b2
```

Um prefixo curto como `a1` também bloqueia todos os outros repetidores cujo
ID começa por `a1`. Usa o prefixo mais longo que conseguires. Até 8 prefixos.

## Todas as definições {#settings}

Os tipos de pacote identificam-se por número. No repetidor, `filter types`
mostra os mesmos números com os nomes do firmware, como `TXT_MSG` e
`GRP_TXT`:

| Número | Tipo | Número | Tipo |
| --- | --- | --- | --- |
| `00` | pedido | `06` | dados de grupo |
| `01` | resposta | `07` | pedido anónimo |
| `02` | mensagem direta | `08` | caminho |
| `03` | confirmação | `09` | rastreio |
| `04` | anúncio | `10` | multiparte |
| `05` | mensagem de grupo | `11` | controlo |

| Comando | O que faz | Valor inicial |
| --- | --- | --- |
| `filter on` / `filter off` | Liga ou desliga o filtro. | desligado |
| `filter dryrun on` / `off` | Conta os descartes, mas continua a passar tudo adiante. | desligado |
| `filter hops <type> <max>` | Descarta um tipo que já passou por este número de repetidores, de 0 a 64. | 32 para mensagens de grupo, 8 para os restantes |
| `filter rate <type> <limit> <secs> [soft]` | Passa no máximo `limit` de um tipo por `secs`. Com `soft`, a passagem vai diminuindo de `soft` até `limit`. `0` desliga o limite. | 20 por 60 s para mensagens diretas e de grupo, 10 para anúncios, 5 para os restantes |
| `filter advert <hours>` | Passa o anúncio de cada nó uma vez por este número de horas, até 720. | 0 (desligado) |
| `filter channel add <#name>` | Deixa de passar um canal adiante. | nenhum |
| `filter path add <hex>` | Descarta tudo o que veio através de um repetidor com este prefixo, de 2 a 8 dígitos hex. | nenhum |
| `filter sender add <name> [secs] [prob]` | Descarta mensagens de grupo de um remetente, no Public e nos canais vigiados. `Bot*` corresponde a todos os nomes que começam por Bot. | nenhum |
| `filter text add <word> [secs] [prob]` | Descarta mensagens de grupo que contêm uma palavra, no Public e nos canais vigiados. `^word` só corresponde no início. | nenhum |
| `filter watch add <#name>` | Deixa as regras de remetente e texto ler também este canal, até 4. O Public é sempre lido. | Public |
| `filter malformed on` / `off` | Descarta mensagens do Public vazias, corrompidas ou com data desfasada mais de uma semana (a verificação da data espera até o relógio estar acertado). | desligado |
| `filter age <minutes>` / `off` | Descarta mensagens de grupo mais antigas do que isto, no Public e nos canais vigiados, de 1 a 10080. | desligado |
| `filter hash <bytes>` | Descarta pacotes com um ID de caminho mais curto do que isto, de 1 a 3. | 1 |
| `filter reset` | Repõe todas as definições nos valores por omissão. | |

Cada `add` tem um `remove` e um `list`, como `filter channel remove #bot`.
Nas regras de remetente e texto, `secs` deixa passar uma mensagem por cada
tantos segundos. `prob` aplica a regra apenas a essa percentagem das
correspondências, de 1 a 100. Até 8 regras de remetente e 8 de texto. Nomes e
palavras distinguem maiúsculas de minúsculas; um nome tem até 15 caracteres,
uma palavra até 23.

Duas definições descartam mais do que talvez esperes:

- `filter hash 2` descarta quase todo o tráfego. Por omissão, os nós enviam
  IDs de caminho de 1 byte.
- `filter age` confia no relógio do teu repetidor. Acerta-o com `clock sync`
  a partir da app, verifica-o com `clock` e começa com folga: `filter age 60`.

Todas as definições são mantidas depois de um reinício.

## O que descartou {#stats}

`filter` mostra os totais por motivo:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` mostra o detalhe de uma definição. Os tópicos são
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` e `age`. `filter stats top` mostra o primeiro byte dos IDs dos nós
por trás de mais descartes, uma pista e não uma prova.
`filter stats air` mostra o tempo de antena que o teu repetidor poupou ao não
passar estes pacotes adiante.

Os contadores voltam a 0 depois de um reinício e depois de `clear stats`.
