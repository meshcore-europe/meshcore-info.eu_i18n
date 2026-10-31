---
title: Filtro de pacotes
lead: 'Impede que o teu repetidor reencaminhe lixo: floods de longe, um bot que nunca para, um canal ruidoso. Experimenta primeiro uma configuração e depois ativa-a.'
description: 'O filtro de pacotes do firmware de repetidor DMC: o que descarta, configurações prontas para um repetidor normal e para um repetidor movimentado, todos os comandos do filtro com o valor predefinido, e como ver o que foi descartado.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-10-31'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Um repetidor (um nó que reencaminha mensagens) repete tudo o que ouve.
Numa mesh movimentada, isso inclui lixo. Um bot publica a cada minuto. Um nó
envia o seu anúncio, a saudação que permite aos outros encontrá-lo, de poucos
em poucos minutos. Chegam mensagens que atravessaram meio país. Cada repetição
tira tempo de antena a todos à tua volta. Com o filtro de pacotes, o teu
repetidor descarta esse tráfego em vez de o reencaminhar. Para descobrires
primeiro o que inunda a tua mesh, e o que ajuda além do filtro, consulta
[Torna a mesh resiliente](/guides/resilient/).

{{< callout type="warning" >}}
O filtro de pacotes faz parte do **firmware de repetidor DMC**, a versão de
repetidor do [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). O
MeshCore original não tem filtro de pacotes. Tem `region denyf *` e
`set flood.max.unscoped`, descritos na página [Comandos CLI](/guides/cli/).
Este guia segue a versão de desenvolvimento 1.18.0 `ecfb2d4` de 19 de outubro
de 2026. A versão estável 1.17.1 só tem os filtros de saltos, de ritmo, de
canal, de hash e de pacotes malformados. Também não tem dry-run.
{{< /callout >}}

## O que o filtro faz {#what}

O filtro só analisa os pacotes que o teu repetidor reencaminha por flood
(envio para todos os nós ao alcance). Nunca mexe no que o teu repetidor envia,
nem nos pacotes que seguem uma rota conhecida até um nó. As mensagens diretas
e os pedidos de e para os teus próprios contactos também passam. Pode
descartar:

- pacotes que já passaram por tantos repetidores (saltos) quantos permites,
  por tipo de pacote;
- mais pacotes de um tipo por minuto do que permites;
- um anúncio de um nó que já se anunciou nas últimas horas;
- mensagens num canal que bloqueias;
- tudo o que chegou através de um repetidor que bloqueias;
- mensagens de grupo de um remetente ou com uma palavra, ou só algumas delas;
- mensagens de grupo danificadas, ou mais antigas do que permites.

O filtro está **desligado** até o ativares. Configuras o filtro com comandos.
Escreve-os por USB na [consola série](/firmware/console/) deste site. Ou
envia-os a partir da app MeshCore, como no
[guia do repetidor](/repeater-guide/#config).

## Obter o firmware {#firmware}

Instala o **DutchMeshCore Repeater** com o flasher da
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). O firmware de
observer de [MQTT no teu observer](/guides/mqtt/) tem o mesmo filtro.

## Experimenta primeiro {#dryrun}

Em dry-run, o filtro conta cada pacote que descartaria, mas continua a
reencaminhá-lo. Assim afinas uma configuração antes de ela descartar algo:

```text
filter on
filter dryrun on
```

Com o dry-run ativo, a linha de estado de `filter` termina em `(dry-run)`. As
contagens mostram o que o filtro teria descartado. Deixa-o a correr durante
um dia e depois analisa-as (consulta [O que foi descartado](#stats)). Quando
os números te parecerem certos, aplica o filtro a sério:

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
minuto. As mensagens de grupo danificadas são descartadas. A configuração
normal do próprio firmware permite 20 mensagens diretas por minuto. Esta
página usa as 5 que o firmware recomenda desde um flood de mensagens diretas
em julho de 2026.

### Um repetidor movimentado {#busy}

Para um repetidor num local alto que ouve uma região inteira, ou um repetidor
inundado:

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

Esta configuração reduz para metade as mensagens de grupo e os anúncios, e
deixa passar o anúncio de cada nó uma vez por dia. Descarta mensagens que já
passaram por 16 repetidores. Depois de um reinício, cada nó consegue passar
um anúncio. A documentação do próprio firmware também define aqui
`filter hash 2`. Esta página deixa-o de fora (consulta
[Todas as configurações](#settings) para saberes porquê).

### Bloquear um canal ruidoso {#channel}

```text
filter channel add #bot
```

O teu repetidor continua a ouvir o canal. Deixa de o reencaminhar para outros
repetidores e companions (os nós a partir dos quais as pessoas enviam
mensagens). Até 16 canais.

### Abrandar um remetente {#sender}

Um bot que publica com demasiada frequência num canal que queres manter:

```text
filter watch add #test
filter sender add Bob 60
```

As mensagens do Bob no canal Public e em `#test` passam agora uma vez por
minuto. O resto é descartado. O filtro compara o nome que vem na mensagem.
Por isso, um remetente que mude de nome escapa-lhe.

### Bloquear um repetidor a montante {#path}

Quando o lixo chega através de um repetidor, bloqueia o prefixo dele: a
primeira parte do seu ID, em hexadecimal (hex). Precisas da versão de
desenvolvimento 1.18. A 1.17.1 não tem filtro de caminho.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` mostra os prefixos que bloqueias, e `filter stats path`
mostra quanto cada um descartou. `filter path remove a1b2` volta a deixá-lo
passar. Um prefixo curto como `a1` bloqueia também todos os outros
repetidores cujo ID começa por `a1`. Usa o prefixo mais longo que puderes.
Até 8 prefixos.

## Todas as configurações {#settings}

Os tipos de pacote identificam-se por número. No repetidor, `filter types`
mostra os mesmos números com os nomes do firmware, como `TXT_MSG` e `GRP_TXT`:

| Número | Tipo | Número | Tipo |
| --- | --- | --- | --- |
| `00` | pedido | `06` | dados de grupo |
| `01` | resposta | `07` | pedido anónimo |
| `02` | mensagem direta | `08` | caminho |
| `03` | confirmação | `09` | trace |
| `04` | anúncio | `10` | multipart |
| `05` | mensagem de grupo | `11` | controlo |

| Comando | O que faz | Valor inicial |
| --- | --- | --- |
| `filter on` / `filter off` | Liga ou desliga o filtro. | desligado |
| `filter dryrun on` / `off` | Conta as rejeições, mas continua a reencaminhar tudo. | desligado |
| `filter hops <type> <max>` | Descarta um tipo que já passou por este número de repetidores, de 0 a 64. | 32 para mensagens de grupo, 8 para os restantes |
| `filter rate <type> <limit> <secs> [soft]` | Deixa passar no máximo `limit` pacotes de um tipo a cada `secs`. Com `soft`, a passagem diminui gradualmente de `soft` até `limit`. `0` desativa o limite. | 20 por 60 s para mensagens diretas e de grupo, 10 para anúncios, 5 para os restantes |
| `filter advert <hours>` | Deixa passar o anúncio de cada nó uma vez a cada este número de horas, até 720. | 0 (desligado) |
| `filter channel add <#name>` | Deixa de reencaminhar um canal. | nenhum |
| `filter path add <hex>` | Descarta tudo o que chegou através de um repetidor com este prefixo, de 2 a 8 dígitos hex. | nenhum |
| `filter sender add <name> [secs] [prob]` | Descarta mensagens de grupo de um remetente, no Public e nos canais vigiados. `Bot*` corresponde a todos os nomes que começam por Bot. | nenhum |
| `filter text add <word> [secs] [prob]` | Descarta mensagens de grupo que contêm uma palavra, no Public e nos canais vigiados. `^word` só corresponde no início. | nenhum |
| `filter watch add <#name>` | Faz com que as regras de remetente e de texto leiam também este canal, até 4. O Public é sempre lido. | Public |
| `filter malformed on` / `off` | Descarta mensagens do Public vazias, danificadas ou com uma data desviada em mais de uma semana (a verificação da data espera até o relógio estar acertado). | desligado |
| `filter age <minutes>` / `off` | Descarta mensagens de grupo mais antigas do que isto, no Public e nos canais vigiados, de 1 a 10080. | desligado |
| `filter hash <bytes>` | Descarta pacotes com um ID de caminho mais curto do que isto, de 1 a 3. | 1 |
| `filter reset` | Repõe todas as configurações nos valores predefinidos. | |

Cada `add` tem um `remove` e um `list`, como `filter channel remove #bot`.
Nas regras de remetente e de texto, `secs` deixa passar uma mensagem a cada
esse número de segundos. `prob` aplica a regra só a essa percentagem das
correspondências, de 1 a 100. Até 8 regras de remetente e 8 regras de texto.
Os nomes e as palavras distinguem maiúsculas de minúsculas. Um nome tem até
15 caracteres, e uma palavra até 23.

Duas configurações descartam mais do que talvez esperes:

- `filter hash 2` descarta quase todo o tráfego. Por predefinição, os nós
  enviam IDs de caminho de 1 byte.
- `filter age` confia no relógio do teu repetidor. Acerta-o com `clock sync`
  a partir da app, verifica-o com `clock` e começa com uma margem generosa:
  `filter age 60`.

Todas as configurações se mantêm depois de um reinício.

## O que foi descartado {#stats}

`filter` mostra os totais por motivo:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` mostra o detalhe de uma configuração. Os tópicos são
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` e `age`. `filter stats top` mostra o primeiro byte dos IDs dos nós
responsáveis pelo maior número de rejeições. Muitos nós partilham esse byte.
`filter stats air` mostra o tempo de antena que o teu repetidor poupou ao não
reencaminhar estes pacotes.

Os contadores voltam a 0 depois de um reinício e depois de `clear stats`.
