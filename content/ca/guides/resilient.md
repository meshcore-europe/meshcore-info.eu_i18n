---
title: Fes més resistent la xarxa
lead: La xarxa del teu voltant va lenta o és plena de brossa? Descobreix què ho causa, activa l'opció del repetidor que ho atura i avisa el teu grup local.
description: 'Inundacions i spam en una xarxa MeshCore: com reconèixer cada tipus, quina opció del repetidor ajuda, com veure una inundació i com trobar-ne l''origen.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-11-02'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Els missatges arriben tard o no arriben? El canal Public s'omple de brossa? Això
és una inundació: més trànsit del que la xarxa pot suportar, enviat per error
o expressament. Busca el que veus a les taules següents. Cada fila indica
l'opció que ho atura. Activa-la al teu repetidor, el node que retransmet els
missatges. Després avisa el teu [grup local](/community/), perquè els repetidors
del teu voltant facin el mateix. Cada repetidor que descarta una inundació deixa
temps d'emissió per a tots els altres.

## Inundacions per error {#mistake}

Una inundació per error surt d'un node amb un propietari que no sap que la
provoca. S'atura quan ho descobreix. A les taules següents, un anunci és la
salutació que envia un node perquè els altres el puguin trobar.

Les opcions de les taules es basen en el que fa el firmware. No totes han aturat
encara una inundació en una xarxa real.

{{< callout type="warning" >}}
Algunes opcions d'aquesta pàgina necessiten el firmware DMC. **MeshCore** 1.18.0
de sèrie inclou les regions, els límits de salts `flood.max.*`, la detecció de
bucles i el cicle de treball. El filtre de paquets, les regles amb què el teu
repetidor descarta la brossa, ve amb el **firmware DMC** de
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). El mateix passa
amb la limitació per cicle de treball i el filtre del companion. Aquesta pàgina
segueix la versió de desenvolupament DMC 1.18.0 `ecfb2d4` del 19 d'octubre de 2026;
a la pàgina del [filtre de paquets](/guides/filter/#firmware) trobaràs on
aconseguir-la.
{{< /callout >}}

| Què veus | Què és | Què hi ajuda |
| --- | --- | --- |
| Peticions als repetidors des d'un sol node, dia i nit, i una xarxa que continua lenta durant dies | Un sistema domòtic o un bot que demana l'estat als repetidors massa sovint | `filter on`. Aleshores el filtre de paquets deixa passar 5 peticions per minut. Avisa el propietari. |
| El mateix tipus de missatge en un canal, cada minut | Un bot que publica massa sovint | [Bloqueja el canal](/guides/filter/#channel) o [frena el remitent](/guides/filter/#sender). Avisa el propietari. |
| Missatges il·legibles a Public i a altres canals | Un node amb el firmware malmès o amb una configuració de ràdio incorrecta | `filter malformed on` els descarta a Public. Avisa el propietari. |
| L'anunci d'un node cada pocs minuts | Un node configurat per anunciar-se massa sovint | `filter advert 24` deixa passar l'anunci de cada node un cop al dia. `set flood.max.advert 3` limita els anuncis a 3 salts. |
| Missatges de molt lluny, amb regions que no són d'aquí | Un pont que enllaça xarxes per internet | `set flood.max.unscoped 1`, i posa el teu repetidor només a les [regions que cobreix](/guides/settings/#traffic). |
| El mateix missatge passa una vegada i una altra, amb l'ID del teu repetidor més d'un cop al camí | Un repetidor que modifica els paquets i els retransmet, de manera que entren en bucle | La detecció de bucles funciona a `minimal` per defecte. `set loop.detect moderate` descarta un bucle abans. |

## Inundacions intencionades {#purpose}

Algunes inundacions són spam: brossa enviada expressament per col·lapsar la
xarxa. El remitent canvia de nom, de clau i de camí, de manera que cap regla
sola atura la inundació.

| Què veus | Què és | Què hi ajuda |
| --- | --- | --- |
| Molts nodes nous amb noms aleatoris, cadascun amb una clau nova | Anuncis falsos | `filter rate 04 5 60` deixa passar 5 anuncis per minut. `filter advert` no ajuda: cada anunci ve d'una [clau nova](#forged). |
| Missatges amb text il·legible de remitents inventats, sovint amb una data de fa més d'un any | Spam de canal | `filter malformed on` els descarta a Public. `filter age 60` descarta els que porten una data antiga a Public i als [canals vigilats](/guides/filter/#settings). |
| Fins a 200 missatges directes per minut a nodes que no existeixen, sense cap confirmació de tornada | Una inundació de missatges directes | `filter rate 02 5 60`. La teva aplicació no mostra aquests missatges; un observador sí. |
| Ràfegues de peticions d'un node a desenes d'altres | Spam de peticions | Amb `filter on`, el filtre de paquets deixa passar 5 peticions per minut. |
| Un missatge torna de 10 a 20 minuts més tard, amb gairebé el mateix camí | Repetició: una còpia enviada de nou | Un repetidor recorda els últims 160 paquets que ha vist, així que en una xarxa molt activa una còpia posterior torna a passar. `filter age` descarta un missatge de grup més antic del que permets. |
| Missatges de Public reenviats amb un remitent inventat, de vegades amb una data antiga | Spam d'eco | `filter age 60`. `filter malformed on` també descarta una data desviada més d'una setmana. |
| Un missatge cada pocs segons a diversos canals, cadascun amb un nom nou, amb preguntes corrents | Una onada de bots | `filter rate 05 10 60`, i [bloqueja els canals](/guides/filter/#channel) que la teva zona no fa servir. Cada nom és nou, així que les [regles de remitent](#forged) no la detecten. |

## Què ha funcionat {#worked}

Els grups locals han aturat inundacions amb aquests passos:

1. **Avisa el propietari.** Una inundació per error s'atura quan el propietari ho
   sap. Envia-li un missatge amable.
2. **No reaccionis a la xarxa.** Una resposta mostra a qui envia l'spam que funciona.
3. **Demana observadors.** Un observador és un node que informa per MQTT de cada
   paquet que sent. Com més observadors tinguis a prop, abans veuràs per on entra
   una inundació. Converteix el teu repetidor en un observador amb
   [MQTT al teu observador](/guides/mqtt/).
4. **Troba l'origen.** Els observadors situen el remitent en una zona. L'últim
   quilòmetre el fa la gent a peu amb una ràdio. Consulta
   [Troba l'origen](#source).
5. **Mobilitza el teu grup local.** Un repetidor amb les opcions correctes ajuda.
   Tots els repetidors de la zona junts aturen una inundació. El teu
   [grup local](/community/) aconsegueix que cada propietari activi l'opció.

## Remitents i camins inventats {#forged}

El remitent escriu aquestes parts d'un paquet, i res no les comprova:

- **El nom del remitent.** En un missatge de canal, el nom forma part del text.
  Qualsevol persona amb la clau del canal pot escriure-hi qualsevol nom.
- **L'inici del camí.** Cada repetidor afegeix el seu ID al final del camí. Res no
  comprova els ID que ja hi havia, així que un remitent pot començar el camí amb
  ID inventats. El final del camí és real.

{{< forged-path >}}

Per tant, `filter sender` i `filter path` només aturen un remitent fins que canvia
de nom o de camí. Un [bloqueig de camí](/guides/filter/#path) també descarta el
trànsit real del repetidor que hi té l'ID. Els límits de velocitat, els límits de
salts, les comprovacions d'antiguitat i de format, els bloquejos de canal, les
regions i el cicle de treball continuen funcionant.

## Opcions per a qualsevol inundació {#always}

Aquestes opcions valen per a qualsevol inundació de la xarxa:

- **Cicle de treball al 10%.** Així el teu repetidor mai no transmet més del que
  permet la llei, arribi el que arribi. La
  [guia del repetidor](/repeater-guide/#duty-cycle) ho explica.
- **Regions i límits de salts.** Una regió és la zona on es queda un missatge. Un
  repetidor només retransmet missatges de les regions que té, i `flood.max.*`
  manté el trànsit a prop. Trobaràs totes dues coses a
  [Redueix el trànsit](/guides/settings/#traffic).
- **El filtre de paquets per a un repetidor molt actiu.** Les
  [opcions predefinides](/guides/filter/#busy) redueixen a la meitat els missatges
  de grup i els anuncis. Prova-les primer en [dry-run](/guides/filter/#dryrun):
  aquest mode només compta el que descartaria.
- **El filtre del companion, al firmware DMC.** El teu companion, el node des del
  qual envies missatges, evita que la brossa arribi a la teva aplicació. Amaga els
  missatges malmesos i antics, i els que bloquegis per repetidor, remitent o
  paraula. Una regla de remitent o de paraula només t'amaga el missatge a
  tu; els altres el continuen rebent.

### Limitació per cicle de treball {#gate}

Al firmware DMC, pots fer que el teu repetidor doni prioritat a la seva regió
quan està molt ocupat. Quan ha transmès durant més del 35% de l'últim minut, deixa
de retransmetre missatges sense regió. Si continua ocupat, després descarta la
regió més àmplia, nivell a nivell. La seva regió sempre passa. Això només funciona
si has configurat regions al teu repetidor. Activa-ho i comprova-ho:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

El que descarta no apareix a `filter stats`. Quan el repetidor es calma, les
regions tornen, començant per la més interior.

## Veure una inundació {#see}

La teva aplicació només mostra el que t'arriba. Només un observador sent una
inundació de missatges directes a nodes que no existeixen. Cada observador informa
al [MeshCore Analyzer](https://meshcore-analyzer.eu/), on tothom ho pot veure.
Converteix el teu repetidor en un observador amb
[MQTT al teu observador](/guides/mqtt/).

A l'Analyzer, mira cada còpia d'un paquet. El seu camí sol mostrar d'on ve. Qui
provoca la inundació pot començar el camí amb [ID inventats](#forged), així que
els primers ID no t'indiquen res. Però cada còpia porta el mateix inici inventat.
La còpia amb el camí més curt ha passat per menys repetidors reals, així que s'ha
sentit més a prop del remitent.

{{< copies >}}

Al teu repetidor, `filter stats` mostra el que ha descartat el filtre de paquets.
`filter stats top` mostra el primer byte dels ID de node responsables de la majoria
de descarts. Molts nodes comparteixen aquest byte, així que redueix la cerca però
no identifica el remitent.

## Troba l'origen {#source}

Quan una inundació torna una vegada i una altra:

1. **Segueix els camins.** Llegeix un camí des del final: els últims ID són els
   repetidors per on ha passat la inundació. El primer ID real és a prop de l'origen;
   els anteriors poden ser [inventats](#forged).
2. **Delimita la zona.** Diversos observadors que senten el mateix paquet situen el
   remitent en una zona. El
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) la calcula a partir
   dels repetidors que l'han sentit.
3. **Fes l'últim quilòmetre a peu.** Els repetidors només senten l'origen al límit
   del seu abast, així que l'últim tram el fa la gent a peu.
   [Mesh-Hunter](https://mesh-hunter.eu/) s'aparella amb el teu companion i registra
   cada paquet que sent amb la teva posició GPS. Diverses persones que caminen
   alhora el troben abans.
4. **Avisa el teu [grup local](/community/).** Els seus membres veuen una part més
   gran de la xarxa, decideixen què es fa després i contacten amb qui inunda
   expressament.

## Afegeix el que has vist {#add}

T'ha afectat una inundació que no surt en aquestes taules? Alguna opció n'ha aturat
una? Explica'ns-ho a [Discord](https://discord.meshcore-info.eu/): què has vist i què
has activat. Ho afegim a la pàgina.
