---
title: Meitsje it mesh robúst
lead: Is de mesh by dy yn 'e buert stadich of fol rommel? Fyn út wat it feroarsaket, set de repeaterynstelling oan dy't it stopet, en fertel it dyn pleatslike groep.
description: 'Floods en spam op in MeshCore-mesh: hoe''tsto elke soart werkenst, hokker repeaterynstelling helpt, hoe''tsto in flood sjochst en hoe''tsto de boarne fynst.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-10-31'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Komme berjochten let of hielendal net oan? Rint Public fol mei rommel? Dat is
in flood: mear ferkear as it mesh drage kin, troch fersin of mei opset
stjoerd. Sykje wat do sjochst yn de tabellen hjirûnder. Elke rige neamt de
ynstelling dy't it tsjinhâldt. Set dy oan op dyn repeater, de node dy't
berjochten trochjout. Fertel it dan dyn [pleatslike groep](/community/), sadat
de repeaters om dy hinne itselde dogge. Elke repeater dy't in flood tsjinhâldt,
lit stjoertiid oer foar alle oaren.

## Floods troch fersin {#mistake}

In flood troch fersin komt fan in node wêrfan't de eigener net wit dat dy him
feroarsaket. Hy hâldt op as de eigener it wit. In advert, yn de tabellen
hjirûnder, is de groet dy't in node stjoert, sadat oaren him fine kinne.

De ynstellings yn de tabellen binne basearre op wat de firmware docht. Net
elke ynstelling hat al in flood op in echt mesh tsjinhâlden.

{{< callout type="warning" >}}
Guon ynstellings op dizze side hawwe de DMC-firmware nedich. Standert
**MeshCore** 1.18.0 hat regio's, de hoplimiten `flood.max.*`, lusdeteksje en de
duty cycle. It pakketfilter, de regels wêrmei't dyn repeater rommel weismyt,
komt mei de **DMC-firmware** fan
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Dat jildt ek foar
duty-cycle-gating en it companionfilter. Dizze side folget de DMC 1.18.0
dev-build `ecfb2d4` fan 19 oktober 2026. De side oer it
[pakketfilter](/guides/filter/#firmware) seit wêr'tst him krijst.
{{< /callout >}}

| Wat do sjochst | Wat it is | Wat helpt |
| --- | --- | --- |
| Fersiken oan repeaters fan ien node, dei en nacht, en in mesh dat dagenlang stadich bliuwt | In hûsautomatisearring of in bot dy't repeaters te faak om harren status freget | `filter on`. It pakketfilter lit dan 5 fersiken yn 'e minút troch. Fertel it de eigener. |
| Itselde soarte berjocht op in kanaal, elke minút | In bot dy't te faak berjochten pleatst | [Blokkearje it kanaal](/guides/filter/#channel) of [rem de stjoerder ôf](/guides/filter/#sender). Fertel it de eigener. |
| Net te lêzen berjochten op Public en oare kanalen | In node mei stikkene firmware of ferkearde radio-ynstellings | `filter malformed on` smyt se op Public wei. Fertel it de eigener. |
| It advert fan ien node elke pear minuten | In node dy't ynsteld is om te faak in advert te stjoeren | `filter advert 24` lit it advert fan elke node ien kear deis troch. `set flood.max.advert 3` hâldt adverts binnen 3 hops. |
| Berjochten fan fier fuort, mei regio's dy't hjir net hearre | In brêge dy't meshes oer it ynternet keppelet | `set flood.max.unscoped 1`, en set dyn repeater allinnich yn de [regio's dy't er betsjinnet](/guides/settings/#traffic). |
| Itselde berjocht komt hieltyd wer foarby, mei de ID fan dyn repeater mear as ien kear yn it paad | In repeater dy't pakketten feroaret en trochjout, sadat se yn in lus rinne | Lusdeteksje stiet standert op `minimal`. `set loop.detect moderate` smyt in lus earder wei. |

## Floods mei opset {#purpose}

Guon floods binne spam: rommel dy't ien mei opset stjoert om it mesh te
ferstopjen. De stjoerder feroaret nammen, kaaien en paden. Dêrom hâldt gjin
inkele regel de flood tsjin.

| Wat do sjochst | Wat it is | Wat helpt |
| --- | --- | --- |
| In protte nije nodes mei willekeurige nammen, elk mei in nije kaai | Falske adverts | `filter rate 04 5 60` lit 5 adverts yn 'e minút troch. `filter advert` helpt net: elk advert komt fan in [nije kaai](#forged). |
| Berjochten mei net te lêzen tekst fan betochte stjoerders, faak mei in datum fan mear as in jier lyn | Kanaalspam | `filter malformed on` smyt se op Public wei. `filter age 60` smyt de berjochten mei in âlde datum wei op Public en op [kanalen dy'tst yn 'e gaten hâldst](/guides/filter/#settings). |
| Oant 200 direkte berjochten yn 'e minút oan nodes dy't net besteane, en gjin befêstigings werom | In flood fan direkte berjochten | `filter rate 02 5 60`. Dyn app lit dizze berjochten net sjen. In observer docht dat wol. |
| Salvo's fersiken fan ien node oan tsientallen oaren | Fersykspam | Mei `filter on` lit it pakketfilter 5 fersiken yn 'e minút troch. |
| In berjocht komt 10 oant 20 minuten letter werom, mei hast itselde paad | Replay: in kopy dy't ien op 'e nij stjoert | In repeater ûnthâldt de lêste 160 pakketten dy't er seach. Op in drok mesh komt in lettere kopy dêrom wer troch. `filter age` smyt in groepsberjocht wei dat âlder is as dyst tastiest. |
| Berjochten fan Public op 'e nij stjoerd ûnder in betochte stjoerder, soms mei in âlde datum | Echospam | `filter age 60`. `filter malformed on` smyt ek in datum wei dy't mear as in wike ôfwykt. |
| Elke pear sekonden in berjocht op ferskate kanalen, elk fan in nije namme, mei gewoane fragen | In botgolf | `filter rate 05 10 60`, en [blokkearje de kanalen](/guides/filter/#channel) dy't dyn omkriten net brûkt. Elke namme is nij, dus de [stjoerderregels](#forged) misse it. |

## Wat wurke hat {#worked}

Pleatslike groepen hawwe floods mei dizze stappen tsjinhâlden:

1. **Fertel it de eigener.** In flood troch fersin hâldt op as de eigener it
   wit. Stjoer harren in freonlik berjocht.
2. **Reagearje net op it mesh.** In antwurd lit in spammer sjen dat de spam
   wurket.
3. **Freegje om observers.** In observer is in node dy't elk pakket dat er
   heart oer MQTT trochjout. Hoe mear observers om dy hinne, hoe earder
   sjochst do wêr't in flood binnenkomt. Meitsje fan dyn eigen repeater ien mei
   [MQTT op dyn observer](/guides/mqtt/).
4. **Fyn de boarne.** Observers pleatse de stjoerder yn in gebiet. Foar de
   lêste kilometer moatte minsken te foet mei in radio op paad. Sjoch
   [Fyn de boarne](#source).
5. **Set dyn pleatslike groep yn beweging.** Ien repeater mei de goede
   ynstellings helpt. Alle repeaters yn it gebiet tegearre hâlde in flood
   tsjin. Dyn [pleatslike groep](/community/) soarget dat elke eigener de
   ynstelling oanset.

## Betochte stjoerders en paden {#forged}

Dizze dielen fan in pakket skriuwt de stjoerder, en neat kontrolearret se:

- **De namme fan de stjoerder.** Yn in kanaalberjocht heart de namme by de
  tekst. Elkenien mei de kaai fan it kanaal kin elke namme skriuwe.
- **It begjin fan it paad.** Elke repeater set syn eigen ID oan it ein fan
  it paad. Neat kontrolearret de ID's dy't der al stiene. Dêrom kin in
  stjoerder it paad begjinne mei betochte ID's. It ein fan it paad is echt.

{{< forged-path >}}

Dêrom hâlde `filter sender` en `filter path` in stjoerder allinnich tsjin
oant er syn namme of paad feroaret. In [paadblokkade](/guides/filter/#path)
smyt ek it echte ferkear wei fan de repeater waans ID deryn stiet.
Limiten op it tal berjochten, hoplimiten, de kontrôles op âldens en net te
lêzen berjochten, kanaalblokkades, regio's en de duty cycle bliuwe wurkjen.

## Ynstellings foar elke flood {#always}

Dizze bliuwe wurkjen, hokker flood it mesh ek treft:

- **Duty cycle op 10%.** Dyn repeater stjoert dan nea mear as de wet
  tastiet, wat der ek binnenkomt. De
  [repeatergids](/repeater-guide/#duty-cycle) beskriuwt it.
- **Regio's en hoplimiten.** In regio is it gebiet dêr't in berjocht yn
  bliuwt. In repeater jout allinnich berjochten troch yn de regio's dy't er
  hat, en `flood.max.*` hâldt ferkear tichtby. Beide steane yn
  [Hâld it ferkear leech](/guides/settings/#traffic).
- **It pakketfilter foar in drokke repeater.** De
  [klearmakke ynstellings](/guides/filter/#busy) halvearje groepsberjochten
  en adverts. Besykje se earst yn [dry-run](/guides/filter/#dryrun): dan
  telt it filter allinnich wat it weismite soe.
- **It companionfilter, yn de DMC-firmware.** Dyn companion, de node dêr'tst
  berjochten mei stjoerst, hâldt rommel út dyn app. Hy ferberget stikkene en
  âlde berjochten, en berjochten fan in repeater, in stjoerder of in wurd
  dat do blokkearrest. In regel foar in stjoerder of wurd ferberget it
  berjocht allinnich foar dy. Oaren krije it noch wol.

### Duty-cycle-gating {#gate}

Yn de DMC-firmware kin dyn repeater syn eigen regio foarrang jaan as it
drok wurdt. As er mear as 35% fan de lêste minút stjoerd hat, jout er gjin
berjochten sûnder regio mear troch. Bliuwt it drok, dan smyt er dêrnei de
breedste regio wei, ien nivo tagelyk. Syn eigen regio komt altyd troch. It
wurket allinnich mei regio's dy'tst op dyn repeater ynsteld hast. Set it oan
en kontrolearje it:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Wat er weismyt, stiet net yn `filter stats`. As de repeater wer stil is,
komme de regio's werom, de binnenste earst.

## In flood sjen {#see}

Dyn app lit allinnich sjen wat by dy oankomt. Allinnich in observer heart in
flood fan direkte berjochten oan nodes dy't net besteane. Elke observer jout
it troch oan de [MeshCore Analyzer](https://meshcore-analyzer.eu/), dêr't
elkenien it sjen kin. Meitsje fan dyn repeater ien mei
[MQTT op dyn observer](/guides/mqtt/).

Sjoch op de Analyzer nei elke kopy fan ien pakket. It paad lit meastal sjen
wêr't it weikaam. In flooder kin it paad begjinne mei
[betochte ID's](#forged), dus de earste ID's fertelle dy neat. Mar elke kopy
draacht itselde betochte begjin. De kopy mei it koartste paad gie troch de
minste echte repeaters. Dy kopy waard dus it tichtst by de stjoerder heard.

{{< copies >}}

Op dyn eigen repeater lit `filter stats` sjen wat it pakketfilter weismiten
hat. `filter stats top` lit de earste byte sjen fan de node-ID's efter de
measte weismiten pakketten. In protte nodes diele dy byte. Dêrom beheint er it
sykjen, mar hy neamt de stjoerder net.

## Fyn de boarne {#source}

As in flood hieltyd werom komt:

1. **Folgje de paden.** Lês in paad fan it ein ôf: de lêste ID's binne de
   repeaters dêr't de flood troch kaam. De ierste echte stiet tichtby de boarne.
   De ID's dêrfoar kinne [betocht](#forged) wêze.
2. **Meitsje it gebiet lytser.** Ferskate observers dy't itselde pakket hearre,
   pleatse de stjoerder yn in gebiet. De
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) rekkenet it út
   op basis fan de repeaters dy't it hearden.
3. **Rin de lêste kilometer.** De repeaters hearre de boarne allinnich oan de
   râne fan harren berik. Dêrom dogge minsken it lêste stik te foet.
   [Mesh-Hunter](https://mesh-hunter.eu/) keppelet oan dyn companion en
   skriuwt elk pakket dat er heart op, mei dyn GPS-posysje. Rinne ferskate
   minsken tagelyk, dan fine se it earder.
4. **Fertel it dyn [pleatslike groep](/community/).** Sy sjogge mear fan it
   mesh, beslisse wat der dêrnei bart en nimme kontakt op mei wa't mei
   opset in flood stjoert.

## Foegje ta wat do seachst {#add}

Hat in flood dy rekke dy't net yn dizze tabellen stiet? Hat in ynstelling
ien tsjinhâlden? Fertel it ús op
[Discord](https://discord.meshcore-info.eu/): wat do seachst en wat do
oansetten hast. Wy foegje it ta oan de side.
