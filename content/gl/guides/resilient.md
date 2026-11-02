---
title: Fai a rede máis resistente
lead: A rede da túa zona vai lenta ou está chea de lixo? Descobre a causa, activa o axuste do repetidor que o frea e avisa o teu grupo local.
description: 'Inundacións e spam nunha rede MeshCore: como recoñecer cada tipo, que axuste do repetidor axuda, como ver unha inundación e como atopar a súa orixe.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-11-02'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

As mensaxes chegan tarde ou non chegan? Public énchese de lixo? Iso é unha
inundación: máis tráfico do que a rede pode levar, enviado por erro ou a
propósito. Busca o que ves nas táboas de abaixo. Cada fila indica o axuste
que o detén. Activa ese axuste no teu repetidor, o nodo que reenvía as
mensaxes. Despois avisa o teu [grupo local](/community/), para que os
repetidores da túa contorna fagan o mesmo. Cada repetidor que descarta unha
inundación deixa tempo de emisión para os demais.

## Inundacións por erro {#mistake}

Unha inundación por erro vén dun nodo cuxo dono non sabe que a causa. Para
en canto o sabe. Un anuncio (advert), nas táboas de abaixo, é o saúdo que
envía un nodo para que os outros o atopen.

Os axustes das táboas baséanse no que fai o firmware. Non todos detiveron
aínda unha inundación nunha rede real.

{{< callout type="warning" >}}
Algúns axustes desta páxina precisan o firmware DMC. **MeshCore** 1.18.0 de
serie trae as rexións, os límites de saltos `flood.max.*`, a detección de
bucles e o ciclo de traballo. O filtro de paquetes, as regras coas que o teu
repetidor descarta o lixo, vén co **firmware DMC** de
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). O mesmo pasa
coa restrición por ciclo de traballo e co filtro do companion. Esta páxina
segue a compilación de desenvolvemento DMC 1.18.0 `ecfb2d4` do 19 de outubro
de 2026. Na páxina do [filtro de paquetes](/guides/filter/#firmware) podes
ver onde conseguila.
{{< /callout >}}

| O que ves | Que é | Que axuda |
| --- | --- | --- |
| Peticións aos repetidores desde un mesmo nodo, día e noite, e unha rede que segue lenta durante días | Unha automatización doméstica ou un bot que lles pide o estado aos repetidores demasiado a miúdo | `filter on`. Entón o filtro de paquetes deixa pasar 5 peticións por minuto. Avisa o dono. |
| O mesmo tipo de mensaxe nunha canle, cada minuto | Un bot que publica demasiado a miúdo | [Bloquea a canle](/guides/filter/#channel) ou [frea o remitente](/guides/filter/#sender). Avisa o dono. |
| Mensaxes ilexibles en Public e noutras canles | Un nodo con firmware danado ou con axustes de radio incorrectos | `filter malformed on` descártaas en Public. Avisa o dono. |
| O anuncio dun mesmo nodo cada poucos minutos | Un nodo configurado para anunciarse demasiado a miúdo | `filter advert 24` deixa pasar o anuncio de cada nodo unha vez ao día. `set flood.max.advert 3` mantén os anuncios dentro de 3 saltos. |
| Mensaxes de moi lonxe, con rexións que non son de aquí | Unha ponte que une redes por internet | `set flood.max.unscoped 1`, e pon o teu repetidor só nas [rexións que atende](/guides/settings/#traffic). |
| A mesma mensaxe pasa unha e outra vez, co ID do teu repetidor na ruta máis dunha vez | Un repetidor que modifica os paquetes e os reenvía, de xeito que entran en bucle | A detección de bucles funciona en `minimal` por defecto. `set loop.detect moderate` descarta un bucle antes. |

## Inundacións a propósito {#purpose}

Algunhas inundacións son spam: lixo enviado a propósito para atascar a rede.
O remitente cambia de nome, de chave e de ruta, así que ningunha regra soa
detén a inundación.

| O que ves | Que é | Que axuda |
| --- | --- | --- |
| Moitos nodos novos con nomes aleatorios, cada un cunha chave nova | Anuncios falsos | `filter rate 04 5 60` deixa pasar 5 anuncios por minuto. `filter advert` non axuda: cada anuncio vén dunha [chave nova](#forged). |
| Mensaxes con texto ilexible de remitentes inventados, a miúdo con data de hai máis dun ano | Spam de canle | `filter malformed on` descártaas en Public. `filter age 60` descarta as de data antiga en Public e nas [canles vixiadas](/guides/filter/#settings). |
| Ata 200 mensaxes directas por minuto a nodos que non existen, e ningunha confirmación de volta | Unha inundación de mensaxes directas | `filter rate 02 5 60`. A túa aplicación non amosa estas mensaxes; un observador si. |
| Ráfagas de peticións desde un nodo a ducias doutros | Spam de peticións | Con `filter on`, o filtro de paquetes deixa pasar 5 peticións por minuto. |
| Unha mensaxe volve entre 10 e 20 minutos despois, case coa mesma ruta | Replay: unha copia enviada de novo | Un repetidor lembra os últimos 160 paquetes que viu, así que nunha rede con moito tráfico unha copia posterior volve pasar. `filter age` descarta unha mensaxe de grupo máis antiga do que permites. |
| Mensaxes de Public enviadas de novo cun remitente inventado, ás veces cunha data antiga | Spam de eco | `filter age 60`. `filter malformed on` tamén descarta as que teñen a data desviada máis dunha semana. |
| Unha mensaxe cada poucos segundos en varias canles, cada unha cun nome novo, con preguntas corrientes | Unha vaga de bots | `filter rate 05 10 60`, e [bloquea as canles](/guides/filter/#channel) que non se usan na túa zona. Cada nome é novo, así que as [regras de remitente](#forged) non a detectan. |

## O que funcionou {#worked}

Os grupos locais detiveron inundacións con estes pasos:

1. **Avisa o dono.** Unha inundación por erro para en canto o dono o sabe.
   Mándalle unha mensaxe amable.
2. **Non reacciones na rede.** Unha resposta móstralle ao spammer que o spam
   funciona.
3. **Pide observadores.** Un observador é un nodo que informa por MQTT de
   cada paquete que escoita. Canto máis observadores haxa na túa contorna,
   antes verás por onde entra unha inundación. Converte o teu propio
   repetidor nun deles con [MQTT no teu observador](/guides/mqtt/).
4. **Atopa a orixe.** Os observadores sitúan o remitente nunha zona. Para o
   último quilómetro fai falta xente a pé cunha radio. Consulta
   [Atopa a orixe](#source).
5. **Pon en marcha o teu grupo local.** Un repetidor cos axustes correctos
   axuda. Todos os repetidores da zona xuntos deteñen unha inundación. O teu
   [grupo local](/community/) consegue que cada dono active o axuste.

## Remitentes e rutas inventados {#forged}

O remitente escribe estas partes dun paquete, e nada as comproba:

- **O nome do remitente.** Nunha mensaxe de canle, o nome forma parte do
  texto. Calquera que teña a chave da canle pode escribir calquera nome.
- **O inicio da ruta.** Cada repetidor engade o seu propio ID ao final da
  ruta. Nada comproba os ID que xa estaban, así que un remitente pode
  comezar a ruta con ID inventados. O final da ruta é real.

{{< forged-path >}}

Por iso `filter sender` e `filter path` só deteñen un remitente ata que cambia
de nome ou de ruta. Un [bloqueo de ruta](/guides/filter/#path) tamén descarta
o tráfico real do repetidor cuxo ID contén. Os límites de frecuencia, os
límites de saltos, as comprobacións de idade e de mensaxes mal formadas, os
bloqueos de canle, as rexións e o ciclo de traballo seguen funcionando.

## Axustes para calquera inundación {#always}

Estes axustes valen sexa cal sexa a inundación que chegue á rede:

- **Ciclo de traballo ao 10%.** Así o teu repetidor nunca transmite máis do
  que permite a lei, entre o que entre. A
  [guía do repetidor](/repeater-guide/#duty-cycle) explícao.
- **Rexións e límites de saltos.** Unha rexión é a zona na que se queda unha
  mensaxe. Un repetidor só reenvía mensaxes das rexións que ten, e
  `flood.max.*` mantén o tráfico preto. Tes as dúas cousas en
  [Reducir o tráfico](/guides/settings/#traffic).
- **O filtro de paquetes para un repetidor con moito tráfico.** Os
  [axustes predefinidos](/guides/filter/#busy) reducen á metade as mensaxes
  de grupo e os anuncios. Próbaos primeiro en
  [dry-run](/guides/filter/#dryrun): este modo só conta o que descartaría.
- **O filtro do companion, no firmware DMC.** O teu companion, o nodo desde
  o que envías mensaxes, mantén o lixo fóra da túa aplicación. Oculta as
  mensaxes danadas e antigas, e as dun repetidor, un remitente ou unha
  palabra que bloquees. Unha regra de remitente ou de palabra só che oculta
  a mensaxe a ti; os demais seguen recibíndoa.

### Restrición por ciclo de traballo {#gate}

No firmware DMC, o teu repetidor pode darlle prioridade á súa propia rexión
cando ten moito tráfico. En canto transmite máis do 35% do último minuto,
deixa de reenviar as mensaxes sen rexión. Se segue ocupado, descarta despois
a rexión máis ampla, nivel a nivel. A súa propia rexión pasa sempre. Só
funciona se tes rexións configuradas no repetidor. Actívaa e compróbaa:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

O que descarta non aparece en `filter stats`. Cando o repetidor volve estar
tranquilo, as rexións regresan, empezando pola máis interior.

## Ver unha inundación {#see}

A túa aplicación só amosa o que che chega a ti. Unha inundación de mensaxes
directas a nodos que non existen só a escoita un observador. Cada observador
informa ao [MeshCore Analyzer](https://meshcore-analyzer.eu/), onde todo o
mundo pode velo. Converte o teu repetidor nun deles con
[MQTT no teu observador](/guides/mqtt/).

No Analyzer, mira todas as copias dun paquete. A súa ruta adoita indicar de
onde veu. Quen inunda pode comezar a ruta con [ID inventados](#forged), así
que os primeiros ID non che din nada. Pero todas as copias levan o mesmo
inicio inventado. A copia coa ruta máis curta pasou polos menos repetidores
reais, así que se escoitou máis preto do remitente.

{{< copies >}}

No teu propio repetidor, `filter stats` amosa o que descartou o filtro de
paquetes. `filter stats top` amosa o primeiro byte dos ID de nodo que hai
detrás da maioría dos descartes. Moitos nodos comparten ese byte, así que
acouta a busca pero non identifica o remitente.

## Atopa a orixe {#source}

Cando unha inundación volve unha e outra vez:

1. **Segue as rutas.** Le a ruta desde o final: os últimos ID son os
   repetidores polos que pasou a inundación. O primeiro real está preto da
   orixe; os ID anteriores poden ser [inventados](#forged).
2. **Acouta a zona.** Varios observadores que escoitan o mesmo paquete sitúan
   o remitente nunha zona. O
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) calcúlaa a
   partir dos repetidores que o escoitaron.
3. **Percorre a pé o último quilómetro.** Os repetidores só escoitan a orixe
   no límite do seu alcance, así que a última parte require xente a pé.
   [Mesh-Hunter](https://mesh-hunter.eu/) enlázase co teu companion e rexistra
   cada paquete que escoita coa túa posición GPS. Varias persoas camiñando á
   vez atópana antes.
4. **Avisa o teu [grupo local](/community/).** Eles ven máis da rede,
   deciden que facer despois e contactan con quen inunda a propósito.

## Engade o que viches {#add}

Sufriches unha inundación que non está nestas táboas? Algún axuste detivo
unha? Cóntanolo en [Discord](https://discord.meshcore-info.eu/): o que viches
e o que activaches. Engadímolo á páxina.
