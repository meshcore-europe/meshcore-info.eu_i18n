---
title: Torna a mesh resistente
lead: A mesh perto de ti está lenta ou cheia de lixo? Descobre o que a causa, liga a definição do repetidor que a trava e avisa o teu grupo local.
description: 'Floods e spam numa mesh MeshCore: como reconhecer cada tipo, que definição do repetidor ajuda, como ver um flood e como encontrar a sua origem.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-10-31'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

As mensagens chegam tarde ou não chegam? O Public enche-se de lixo? Isso é
um flood: mais tráfego do que a mesh consegue transportar, enviado por
engano ou de propósito. Procura o que vês nas tabelas abaixo. Cada linha
indica a definição que o trava. Liga-a no teu repetidor, o nó que
reencaminha as mensagens. Depois avisa o teu [grupo local](/community/),
para que os repetidores à tua volta façam o mesmo. Cada repetidor que
descarta um flood deixa tempo de antena livre para todos os outros.

## Floods por engano {#mistake}

Um flood por engano vem de um nó cujo dono não sabe que o provoca. Para
assim que o dono fica a saber. Nas tabelas abaixo, um anúncio é a saudação
que um nó envia para que os outros o encontrem.

As definições nas tabelas baseiam-se no que o firmware faz. Nem todas já
travaram um flood numa mesh real.

{{< callout type="warning" >}}
Algumas definições desta página precisam do firmware DMC. O **MeshCore**
1.18.0 de origem tem regiões, os limites de saltos `flood.max.*`, deteção
de loops e o duty cycle. O filtro de pacotes, as regras com que o teu
repetidor descarta lixo, vem com o **firmware DMC** do
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). O mesmo vale
para o duty-cycle gating e o filtro do companion. Esta página segue a build
de desenvolvimento DMC 1.18.0 `ecfb2d4` de 19 de outubro de 2026. A página
do [filtro de pacotes](/guides/filter/#firmware) diz onde a obter.
{{< /callout >}}

| O que vês | O que é | O que ajuda |
| --- | --- | --- |
| Pedidos de um nó a repetidores, dia e noite, e uma mesh que fica lenta durante dias | Uma automação doméstica ou um bot que pede o estado aos repetidores com demasiada frequência | `filter on`. O filtro de pacotes deixa então passar 5 pedidos por minuto. Avisa o dono. |
| O mesmo tipo de mensagem num canal, a cada minuto | Um bot que publica com demasiada frequência | [Bloqueia o canal](/guides/filter/#channel) ou [abranda o remetente](/guides/filter/#sender). Avisa o dono. |
| Mensagens ilegíveis no Public e noutros canais | Um nó com firmware com defeito ou definições de rádio erradas | `filter malformed on` descarta-as no Public. Avisa o dono. |
| O anúncio de um nó a cada poucos minutos | Um nó configurado para anunciar com demasiada frequência | `filter advert 24` deixa passar o anúncio de cada nó uma vez por dia. `set flood.max.advert 3` mantém os anúncios dentro de 3 saltos. |
| Mensagens de longe, com regiões que não pertencem aqui | Uma ponte que liga meshes pela internet | `set flood.max.unscoped 1`, e coloca o teu repetidor só nas [regiões que serve](/guides/settings/#traffic). |
| A mesma mensagem passa uma e outra vez, com o ID do teu repetidor no caminho mais do que uma vez | Um repetidor que altera pacotes e os reencaminha, o que os põe em loop | A deteção de loops corre em `minimal` por omissão. Com `set loop.detect moderate`, o repetidor descarta um loop mais cedo. |

## Floods de propósito {#purpose}

Alguns floods são spam: lixo enviado de propósito para entupir a mesh. O
remetente muda de nomes, chaves e caminhos, por isso nenhuma regra isolada
trava o flood.

| O que vês | O que é | O que ajuda |
| --- | --- | --- |
| Muitos nós novos com nomes aleatórios, cada um com uma chave nova | Anúncios falsos | `filter rate 04 5 60` deixa passar 5 anúncios por minuto. `filter advert` não ajuda: cada anúncio vem de uma [chave nova](#forged). |
| Mensagens com texto ilegível de remetentes inventados, muitas vezes datadas de há mais de um ano | Spam em canais | `filter malformed on` descarta-as no Public. `filter age 60` descarta as de data antiga no Public e nos [canais vigiados](/guides/filter/#settings). |
| Até 200 mensagens diretas por minuto para nós que não existem, sem confirmações de volta | Um flood de mensagens diretas | `filter rate 02 5 60`. A tua app não mostra estas mensagens. Um observer mostra. |
| Rajadas de pedidos de um nó para dezenas de outros | Spam de pedidos | Com `filter on`, o filtro de pacotes deixa passar 5 pedidos por minuto. |
| Uma mensagem volta 10 a 20 minutos depois, com quase o mesmo caminho | Replay: uma cópia enviada de novo | Um repetidor lembra-se dos últimos 160 pacotes que viu. Por isso, numa mesh movimentada, uma cópia posterior passa de novo. `filter age` descarta uma mensagem de grupo mais antiga do que permites. |
| Mensagens do Public reenviadas com um remetente inventado, às vezes com uma data antiga | Spam de eco | `filter age 60`. `filter malformed on` também descarta uma data desfasada mais de uma semana. |
| Uma mensagem a cada poucos segundos em vários canais, cada uma de um nome novo, com perguntas banais | Uma vaga de bots | `filter rate 05 10 60`, e [bloqueia os canais](/guides/filter/#channel) que a tua zona não usa. Cada nome é novo, por isso as [regras de remetente](#forged) falham. |

## O que já resultou {#worked}

Grupos locais travaram floods com estes passos:

1. **Avisa o dono.** Um flood por engano para assim que o dono sabe. Manda-lhe
   uma mensagem simpática.
2. **Não reajas na mesh.** Uma resposta mostra ao spammer que o spam resulta.
3. **Pede observers.** Um observer é um nó que reporta por MQTT cada
   pacote que ouve. Quantos mais observers à tua volta, mais depressa vês
   por onde entra um flood. Transforma o teu repetidor num deles com
   [MQTT no teu observer](/guides/mqtt/).
4. **Encontra a origem.** Os observers situam o remetente numa zona. O
   último quilómetro faz-se a pé, com um rádio. Vê
   [Encontra a origem](#source).
5. **Mobiliza o teu grupo local.** Um repetidor com as definições
   certas ajuda. Todos os repetidores da zona juntos travam um flood. O teu
   [grupo local](/community/) leva cada dono a ligar a definição.

## Remetentes e caminhos inventados {#forged}

O remetente escreve estas partes de um pacote, e ninguém as verifica:

- **O nome do remetente.** Numa mensagem de canal, o nome faz parte do
  texto. Quem tiver a chave do canal pode escrever qualquer nome.
- **O início do caminho.** Cada repetidor acrescenta o seu ID ao fim do
  caminho. Ninguém verifica os IDs que já lá estavam, por isso um remetente
  pode começar o caminho com IDs inventados. O fim do caminho é real.

{{< forged-path >}}

Por isso, `filter sender` e `filter path` só travam um remetente até ele
mudar de nome ou de caminho. Um [bloqueio de caminho](/guides/filter/#path)
também descarta o tráfego real do repetidor cujo ID lá está. Os limites de
taxa, os limites de saltos, as verificações de idade e de mensagens
malformadas, os bloqueios de canal, as regiões e o duty cycle continuam a
funcionar.

## Definições para qualquer flood {#always}

Estas valem seja qual for o flood na mesh:

- **Duty cycle a 10%.** Assim, o teu repetidor nunca transmite mais do que
  a lei permite, venha o que vier. O
  [guia do repetidor](/repeater-guide/#duty-cycle) trata disso.
- **Regiões e limites de saltos.** Uma região é a zona onde uma mensagem
  fica. Um repetidor só reencaminha mensagens das regiões que tem, e
  `flood.max.*` mantém o tráfego por perto. Ambos estão em
  [Reduz o tráfego](/guides/settings/#traffic).
- **O filtro de pacotes para um repetidor movimentado.** As
  [definições prontas](/guides/filter/#busy) reduzem para metade as
  mensagens de grupo e os anúncios. Experimenta-as primeiro em
  [dry-run](/guides/filter/#dryrun): nesse modo, o filtro só conta o que
  descartaria.
- **O filtro do companion, no firmware DMC.** O teu companion, o nó a
  partir do qual envias mensagens, mantém o lixo fora da tua app. Esconde
  mensagens com defeito e antigas, e mensagens de um repetidor, de um
  remetente ou com uma palavra que bloqueias. Uma regra de remetente ou de
  palavra só esconde a mensagem de ti. Os outros continuam a recebê-la.

### Duty-cycle gating {#gate}

No firmware DMC, o teu repetidor pode dar prioridade à sua própria região
quando fica sobrecarregado. Quando já transmitiu durante mais de 35% do
último minuto, deixa de reencaminhar mensagens sem região. Se continuar
sobrecarregado, descarta a seguir a região mais ampla, um nível de cada vez.
A sua própria região passa sempre. Só funciona com regiões definidas no teu
repetidor. Liga-o e verifica-o:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

O que o gating descarta não aparece em `filter stats`. Quando o repetidor
volta a ficar calmo, as regiões regressam, a mais interior primeiro.

## Vê um flood {#see}

A tua app só mostra o que te chega. Só um observer ouve um flood de
mensagens diretas para nós que não existem. Cada observer reporta ao
[MeshCore Analyzer](https://meshcore-analyzer.eu/), onde todos o podem ver.
Transforma o teu repetidor num observer com
[MQTT no teu observer](/guides/mqtt/).

No Analyzer, olha para todas as cópias de um pacote. O caminho costuma
mostrar de onde veio. Quem faz o flood pode começar o caminho com
[IDs inventados](#forged), por isso os primeiros IDs não te dizem nada. Mas
todas as cópias trazem o mesmo início inventado. A cópia com o caminho mais
curto passou pelo menor número de repetidores reais. Por isso foi ouvida
mais perto do remetente.

{{< copies >}}

No teu próprio repetidor, `filter stats` mostra o que o filtro de pacotes
descartou. `filter stats top` mostra o primeiro byte dos IDs dos nós por
trás da maioria dos pacotes descartados. Muitos nós partilham esse byte.
Assim, restringes a procura, mas não ficas a saber quem é o remetente.

## Encontra a origem {#source}

Quando um flood volta sempre:

1. **Segue os caminhos.** Lê um caminho a partir do fim: os últimos IDs são
   os repetidores por onde o flood passou. O primeiro ID real está perto da
   origem. Os IDs antes dele podem ser [inventados](#forged).
2. **Restringe a zona.** Vários observers que ouvem o mesmo pacote situam o
   remetente numa zona. O
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) calcula-a a
   partir dos repetidores que o ouviram.
3. **Percorre o último quilómetro a pé.** Os repetidores só ouvem a origem
   no limite do seu alcance, por isso a última parte faz-se a pé.
   [Mesh-Hunter](https://mesh-hunter.eu/) emparelha com o teu companion e
   regista cada pacote que ouve com a tua posição GPS. Várias pessoas a
   caminhar ao mesmo tempo encontram-na mais depressa.
4. **Avisa o teu [grupo local](/community/).** O grupo vê mais da mesh,
   decide o que acontece a seguir e contacta quem faz floods de propósito.

## Acrescenta o que viste {#add}

Apanhaste um flood que não está
nestas tabelas? Alguma definição travou um? Conta-nos no
[Discord](https://discord.meshcore-info.eu/): o que viste e o que ligaste.
Acrescentamo-lo à página.
