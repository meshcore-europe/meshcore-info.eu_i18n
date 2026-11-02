---
title: Maach de Mesh méi robust
lead: Ass de Mesh bei dir lues oder voller Müll? Fann eraus, wourun et läit, schalt d'Repeater-Astellung an, déi et stoppt, a so denger lokaler Grupp Bescheed.
description: 'Floods a Spam op engem MeshCore-Mesh: wéi s du all Aart erkenns, wéi eng Repeater-Astellung hëlleft, wéi s du e Flood gesäis a wéi s du seng Quell fënns.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-11-02'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Kommen Noriichten ze spéit oder guer net un? Fëllt Public sech mat Müll? Dat
ass e Flood: méi Traffic, wéi de Mesh packt, aus Versinn oder mat Absicht
geschéckt. Sich dat, wat s du gesäis, an den Tabellen hei drënner. All Rei nennt
d'Astellung, déi et stoppt. Schalt se op dengem Repeater an, dem Node, deen
Noriichte weiderleet. So duerno denger [lokaler Grupp](/community/) Bescheed,
fir datt d'Repeatere ronderëm dech datselwecht maachen. All Repeater, deen e
Flood verwerft, léisst Sendezäit fir all déi aner fräi.

## Floods aus Versinn {#mistake}

E Flood aus Versinn kënnt vun engem Node, deem säi Besëtzer net weess, datt
en ee verursaacht. En hält op, soubal de Besëtzer et weess. An den Tabellen hei
drënner ass en Advert de Gréiss, deen e Node schéckt, fir datt anerer en
fannen.

D'Astellungen an den Tabelle baséieren op deem, wat d'Firmware mécht. Nach net
all Astellung huet op engem richtege Mesh e Flood gestoppt.

{{< callout type="warning" >}}
Verschidden Astellungen op dëser Säit brauchen d'DMC-Firmware. D'Standardversioun
**MeshCore** 1.18.0 huet Regiounen, d'Hop-Limitten `flood.max.*`, d'Loop-Detektioun
an den Duty Cycle. De Paketfilter, d'Regelen, mat deenen däi Repeater Müll
verwerft, kënnt mat der **DMC-Firmware** vun
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Dat selwecht gëllt
fir d'Duty-Cycle-Gating an de Companion-Filter. Dës Säit hält sech un den DMC
1.18.0 Dev-Build `ecfb2d4` vum 19. Oktober 2026; op der Säit
[Paketfilter](/guides/filter/#firmware) steet, wou s du e kriss.
{{< /callout >}}

| Wat s du gesäis | Wat et ass | Wat hëlleft |
| --- | --- | --- |
| Ufroe vun engem Node un d'Repeateren, Dag an Nuecht, an e Mesh, dee fir Deeg lues bleift | Eng Hausautomatisatioun oder e Bot, déi d'Repeateren ze dacks no hirem Status freet | `filter on`. De Paketfilter léisst dann 5 Ufroen d'Minutt duerch. So dem Besëtzer Bescheed. |
| Déi selwecht Zort Noriicht op engem Kanal, all Minutt | E Bot, dee ze dacks postt | [Spär de Kanal](/guides/filter/#channel) oder [brems de Sender](/guides/filter/#sender). So dem Besëtzer Bescheed. |
| Onliesbar Noriichten op Public an anere Kanäl | En Node mat futtisser Firmware oder falsche Funkastellungen | `filter malformed on` verwerft se op Public. So dem Besëtzer Bescheed. |
| Den Advert vun engem Node all puer Minutten | En Node, deen esou agestallt ass, datt en ze dacks en Advert schéckt | `filter advert 24` léisst den Advert vun all Node eemol den Dag duerch. `set flood.max.advert 3` hält Adverts bannent 3 Hops. |
| Noriichte vu wäit ewech, mat Regiounen, déi net heihi gehéieren | Eng Bréck, déi Meshes iwwer den Internet verbënnt | `set flood.max.unscoped 1`, a setz däi Repeater nëmmen an d'[Regiounen, déi en ofdeckt](/guides/settings/#traffic). |
| Déi selwecht Noriicht kënnt ëmmer erëm laanscht, an d'ID vun dengem Repeater steet méi wéi eemol an hirem Path | E Repeater, dee Paketen ännert a weiderleet, sou datt se an engem Loop lafen | D'Loop-Detektioun leeft standardméisseg op `minimal`. `set loop.detect moderate` verwerft e Loop méi fréi. |

## Floods mat Absicht {#purpose}

Verschidde Floods si Spam: Müll, deen ee mat Absicht schéckt, fir de Mesh
zouzestoppen. De Sender wiesselt Nimm, Schlësselen a Pathen, dofir stoppt keng
eenzeg Regel de Flood.

| Wat s du gesäis | Wat et ass | Wat hëlleft |
| --- | --- | --- |
| Vill nei Node mat zoufällegen Nimm, all mat engem neie Schlëssel | Gefälscht Adverts | `filter rate 04 5 60` léisst 5 Adverts d'Minutt duerch. `filter advert` hëlleft net: all Advert kënnt vun engem [neie Schlëssel](#forged). |
| Noriichte mat onliesbarem Text vun erfonnte Sender, dacks mat engem Datum, dee méi wéi ee Joer zeréckläit | Kanal-Spam | `filter malformed on` verwerft se op Public. `filter age 60` verwerft déi mat alem Datum op Public an op [iwwerwaachte Kanäl](/guides/filter/#settings). |
| Bis zu 200 direkt Noriichten d'Minutt un Noden, déi et net gëtt, a keng Bestätegungen zeréck | E Flood vun direkte Noriichten | `filter rate 02 5 60`. Deng App weist dës Noriichten net, en Observer awer. |
| Vill Ufroen op eemol vun engem Node un Dosende vun aneren | Ufro-Spam | Mat `filter on` léisst de Paketfilter 5 Ufroen d'Minutt duerch. |
| Eng Noriicht kënnt 10 bis 20 Minutte méi spéit zeréck, mat bal deemselwechte Path | Replay: eng Kopie, déi nach eng Kéier geschéckt gëtt | E Repeater behält déi lescht 160 Paketen, déi e gesinn huet, dofir kënnt op engem ausgelaaschte Mesh eng méi spéit Kopie nees duerch. `filter age` verwerft eng Gruppenoriicht, déi méi al ass, wéi s du erlaabs. |
| Noriichte vu Public, déi nees ënner engem erfonnte Sender geschéckt ginn, heiansdo mat engem alen Datum | Echo-Spam | `filter age 60`. `filter malformed on` verwerft och en Datum, deen ëm méi wéi eng Woch falsch ass. |
| All puer Sekonnen eng Noriicht op e puer Kanäl, all Kéier vun engem neien Numm, mat alldeegleche Froen | Eng Bot-Well | `filter rate 05 10 60`, a [spär d'Kanäl](/guides/filter/#channel), déi deng Géigend net benotzt. All Numm ass nei, dofir erwëschen d'[Sender-Regelen](#forged) se net. |

## Wat geklappt huet {#worked}

Lokal Gruppen hunn Floods mat dëse Schrëtt gestoppt:

1. **So dem Besëtzer Bescheed.** E Flood aus Versinn hält op, soubal säi
   Besëtzer et weess. Schéck him eng frëndlech Noriicht.
2. **Reagéier net um Mesh.** Eng Äntwert weist engem Spammer, datt de Spam
   funktionéiert.
3. **Fro no Observeren.** En Observer ass en Node, deen all Paket, deen en
   héiert, iwwer MQTT mellt. Wat méi Observere ronderëm dech sinn, wat s du méi
   séier gesäis, wou e Flood erakënnt. Maach aus dengem eegene Repeater een, mat
   [MQTT op dengem Observer](/guides/mqtt/).
4. **Fann d'Quell.** Observere lokaliséieren de Sender an enger Géigend. Fir de
   leschte Kilometer musse Leit mat engem Funkgeräit trëppele goen. Kuck
   [Fann d'Quell](#source).
5. **Bréng deng lokal Grupp a Beweegung.** Ee Repeater mat de richtegen
   Astellungen hëlleft. All d'Repeateren an der Géigend zesumme stoppen e Flood.
   Deng [lokal Grupp](/community/) kritt all Besëtzer dozou, d'Astellung
   anzeschalten.

## Erfonnte Sender a Pathen {#forged}

Dës Deeler vun engem Paket schreift de Sender, an näischt kontrolléiert se:

- **Den Numm vum Sender.** An enger Kanalnoriicht ass den Numm en Deel vum Text.
  Jiddereen, deen de Kanalschlëssel huet, kann all Numm schreiwen.
- **Den Ufank vum Path.** All Repeater setzt seng eegen ID un d'Enn vum Path.
  Näischt kontrolléiert d'IDen, déi virdru do stoungen, dofir kann e Sender de
  Path mat erfonnten IDen ufänken. D'Enn vum Path ass echt.

{{< forged-path >}}

Dofir stoppen `filter sender` a `filter path` e Sender nëmme, bis e säin Numm oder
säi Path ännert. Eng [Path-Spär](/guides/filter/#path) verwerft och den echte
Traffic vum Repeater, deem seng ID dra steet. Rate-Limitten, Hop-Limitten,
d'Kontrolle vum Alter a vu fehlerhafte Paketen, Kanal-Spären, Regiounen an den
Duty Cycle funktionéiere weider.

## Astellunge fir all Flood {#always}

Dës Astellunge gëllen, egal wat de Mesh iwwerschwemmt:

- **Duty Cycle op 10%.** Däi Repeater sent dann ni méi, wéi d'Gesetz erlaabt,
  egal wat erakënnt. De [Repeater-Guide](/repeater-guide/#duty-cycle) erkläert
  dat.
- **Regiounen an Hop-Limitten.** Eng Regioun ass d'Géigend, an där eng Noriicht
  bleift. E Repeater leet nëmmen Noriichten aus de Regiounen weider, déi en huet,
  an `flood.max.*` hält den Traffic an der Géigend. Béid stinn am Abschnitt
  [Hal den Traffic niddreg](/guides/settings/#traffic).
- **De Paketfilter fir en ausgelaaschte Repeater.** Déi
  [fäerdeg Astellungen](/guides/filter/#busy) hallwéiere Gruppenoriichten an
  Adverts. Probéier se als éischt am [Dry-Run](/guides/filter/#dryrun): deen
  zielt nëmmen, wat e géif verwerfen.
- **De Companion-Filter, an der DMC-Firmware.** Däi Companion, den Node, vun deem
  aus s du Noriichte schéckt, hält Müll aus denger App. E verstoppt futtis an al
  Noriichten, an Noriichte vun engem Repeater, engem Sender oder mat engem Wuert,
  déi s du spärs. Eng Regel fir e Sender oder e Wuert verstoppt d'Noriicht nëmme
  fir dech; anerer kréie se weiderhin.

### Duty-Cycle-Gating {#gate}

An der DMC-Firmware kann däi Repeater senger eegener Regioun Virrang ginn, wann
en ausgelaascht ass. Soubal e méi wéi 35% vun der leschter Minutt gesent huet,
leet e keng Noriichten ouni Regioun méi weider. Bleift en ausgelaascht, verwerft
en duerno déi breetste Regioun, ëmmer een Niveau op eemol. Seng eege Regioun kënnt
ëmmer duerch. Dat funktionéiert nëmmen, wann s du op dengem Repeater Regiounen
agestallt hues. Schalt et an a kontrolléier et:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Wat dëst Gating verwerft, steet net a `filter stats`. Wann de Repeater erëm
roueg ass, komme d'Regiounen zeréck, déi bannescht als éischt.

## E Flood gesinn {#see}

Deng App weist nëmmen, wat bei dech kënnt. Nëmmen en Observer héiert e Flood vun
direkte Noriichten un Noden, déi et net gëtt. All Observer mellt un den
[MeshCore Analyzer](https://meshcore-analyzer.eu/), wou jiddereen et gesi kann.
Maach aus dengem Repeater een, mat
[MQTT op dengem Observer](/guides/mqtt/).

Kuck dir um Analyzer all Kopie vun engem Paket un. Säi Path weist normalerweis,
wouhier e kënnt. E Flooder kann de Path mat [erfonnten IDen](#forged) ufänken,
dofir soen dir seng éischt IDen näischt. Mee all Kopie huet deeselwechten
erfonnten Ufank. D'Kopie mam kierzste Path ass duerch déi mannst echt Repeatere
gaangen, also gouf se am nooste beim Sender héieren.

{{< copies >}}

Op dengem eegene Repeater weist `filter stats`, wat de Paketfilter verworf huet.
`filter stats top` weist den éischte Byte vun de Node-IDen, op déi déi meescht
verworfe Paketen zeréckginn. Vill Noden deelen dëse Byte, dofir schränkt en d'Sich
an, nennt awer net de Sender.

## Fann d'Quell {#source}

Wann e Flood ëmmer erëm kënnt:

1. **Verfolleg d'Pathen.** Lies e Path vum Enn hir: déi lescht IDe sinn d'Repeateren,
   duerch déi de Flood gaangen ass. Déi fréist echt ID ass no bei der Quell; d'IDen
   dovir kënnen [erfonnt](#forged) sinn.
2. **Grenz d'Géigend an.** Wa verschidden Observeren dee selwechte Paket héieren,
   lokaliséiere si de Sender an enger Géigend. Den
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) rechent dat aus de
   Repeateren aus, déi de Paket héieren hunn.
3. **Trëppel de leschte Kilometer.** D'Repeateren héieren d'Quell nëmmen um Rand
   vun hirer Reechwäit, dofir musse Leit dee leschten Deel zu Fouss maachen.
   [Mesh-Hunter](https://mesh-hunter.eu/) verbënnt sech mat dengem Companion a
   protokolléiert all Paket, deen en héiert, mat denger GPS-Positioun. Wa méi Leit
   gläichzäiteg trëppelen, fanne se d'Quell méi séier.
4. **So denger [lokaler Grupp](/community/) Bescheed.** Si gesinn méi vum Mesh, si
   entscheeden, wéi et weidergeet, a si kontaktéieren deen, dee mat Absicht floodt.

## Setz derbäi, wat s du gesinn hues {#add}

Hues du e Flood erlieft, deen net an dësen Tabelle steet? Huet eng Astellung ee
gestoppt? So eis et op [Discord](https://discord.meshcore-info.eu/): wat s du
gesinn an ageschalt hues. Mir setzen et op d'Säit.
