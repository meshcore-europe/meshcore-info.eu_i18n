---
title: Wat is MeshCore?
lead: MeshCore stjoert tekstberjochten oer de radio, fan node nei node. It wurket sûnder ynternet en sûnder abonnemint.
description: 'Wat MeshCore is en net is: soarten nodes, routing, it ferskil mei Meshtastic, fersifering en de 868 MHz-bân.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '279b56a4'
  seeded: '2026-11-02'
  fields: {title: '06eda66b', lead: 'c0174569', description: '15e6d2a7', eyebrow: '8610c822'}
  sections: ['aa768ac3', '16fde264', '0a55792c', 'c3de803d', '493b444f', 'a8b2b9b4', '429f699c', 'f8008f48', '88af2bd3', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'fab378a5', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', 'fc8f3129', '8dec428a', '07cbac35', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '95e18f18', '02f1fe2f', 'e6b5b258']
---

MeshCore is fergese software foar lytse LoRa-radio's. LoRa is in radiotechyk
dy't in bytsje data fier stjoert, mei hiel min stroom. In radio mei MeshCore
hjit in *node*. Mei de app op dyn telefoan of laptop, of mei in eigen
skerm en toetseboerd, stjoerst do tekst nei minsken dy't kilometers fier fuort binne. Der sit gjin mêst, router of provider tusken.

De software is iepen boarne. De ûntwikkeling bart by
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore), ûnder de
MIT-lisinsje.

## Wat MeshCore net is {#not}

Bist nij yn de radiowrâld? Dit binne de dingen dy't minsken it faakst fan MeshCore
ferwachtsje, en dy't it net docht.

- **It is net it ynternet of in telefoan.** MeshCore stjoert koarte tekstberjochten,
  sawat sa lang as in tekstberjocht op dyn telefoan. Gjin spraak, foto's, fideo
  of websites, en do kinst gjin gewoan telefoannûmer berikke.
- **It is gjin needtsjinst.** Gjin inkelde needtsjinst harket mei op it mesh, en
  nimmen belooft dat ien dyn berjocht lêst. Is der need, belje dan 112.
- **It wurket net daliks, en net oeral.** In berjocht springt fan radio nei
  radio en kin der in pear sekonden oer dwaan, of hielendal net oankomme. Oft it
  trochkomt, hinget ôf fan de repeaters om dy hinne, fan hichte, gebouwen en dyn
  antenne. In lytse radio binnendoar berikt faak nimmen; in repeater op in dak
  komt kilometers fier.
- **It is gjin tsjinst dy't ien foar dy fersoarget.** Der is gjin provider, gjin
  helpdesk en gjin dekkingsbelofte. It mesh bestiet dêr't minsken út de mienskip
  repeaters opset hawwe, en nearne oars.
- **Net alles derop is privee.** Direkte berjochten binne fersifere, mar Public
  en de hashtagkanalen kin elkenien lêze, en de namme fan dyn node en dyn dielde
  posysje binne te sjen foar elkenien binnen berik.
  [Observers](/network/) jouwe wat se hearre troch oan iepenbiere kaarten. De
  [seksje oer fersifering](#encryption) leit út wat privee bliuwt.
- **It is net ûnbeheind.** Elkenien yn in gebiet dielt ien radiokanaal, en de
  regels foar de [band fan 868 MHz](#band) beheine hoe lang elke radio stjoere
  mei. Elk berjocht nimt stjoertiid fan alle oaren ôf, dus bots, faak stjoerde
  adverts en testberjochten meitsje it mesh stadiger foar elkenien.
- **It is net Meshtastic.** Meshtastic is in oar systeem dat op sawat deselde
  boards draait. Dy twa kinne net mei-inoar prate.
  [Oerstappe fan Meshtastic](#meshtastic) lit sjen wat oars wurket.

## De mesh yn in minút {#mesh}

Ien LoRa-radio berikt yn in stêd in pear kilometer, en folle fierder fan in
heuvel of in dak. Om fierder te kommen, jouwe radio's berjochten foar elkoar
troch: dat is in *mesh*. Yn MeshCore dogge radio's dy't *repeaters* hjitte
dat trochjaan. Heart in repeater in berjocht, dan stjoert er it opnij út. Sa
kin it berjocht in hiele regio oerstekke.

Nimmen is eigner fan de mesh. Elke node en elke repeater heart by ien út de
mienskip. De mesh rikt sa fier as harren repeaters.

## De 3 soarten node {#roles}

Do kiest de soarte fan in node as do him flashest. Dyn earste node is in companion.

**Companion.** Dyn eigen radio. Do koppelst him oer Bluetooth of USB oan de
MeshCore-app op dyn telefoan of laptop; guon hawwe in eigen skerm en
toetseboerd. Yn de app lêst en typest do. De companion bewarret dyn kontakten
en kanalen, en de berjochten dy't oankamen wylst de app net ferbûn wie. In companion jout gjin berjochten foar oaren troch.

**Repeater.** In radio dy't heech stiet en berjochten foar elkenien trochjout.
De measte rinne op sinne-enerzjy. Do hast allinnich in eigen repeater nedich
dêr't de mesh noch net komt. Hy hat gjin eigen app. Do stelst him yn oer USB,
of do logst yn mei in wachtwurd en behearst him oer de radio. Yn de
[repeater-hantlieding](/repeater-guide/) lêsto hoe.

**Room server.** In lyts prikboerd op de mesh. As do ynlogst, krijst de
berjochten dy'tst mist hast wylst do bûten berik wiest, oant de lêste 32. Hy
bewarret se allinnich yn it ûnthâld, dus in herstart of in stroomûnderbrekking
wisket se. In pleatslike groep brûkt der ien foar oankundigingen.

## Hoe't in berjocht syn wei fynt {#routing}

Elke node hat in geheime kaai en in iepenbiere kaai. De iepenbiere kaai is syn identiteit. In node
kundiget him oan mei in *advert*: in ûndertekene pakket mei syn namme en, as do dat
wolst, syn posysje. Ien ferskynt yn dyn kontakten as ien fan syn adverts dy
berikt hat, of as do syn QR-koade scanst. Yn de app sit in knop om dyn eigen advert te stjoeren.

Dyn earste berjocht oan in kontakt giet út as *flood*. Elke repeater dy't it
heart, jout it ien kear troch en foeget ûnderweis syn eigen koarte ID ta. It
antwurd nimt dy list mei ID's werom. Fan dan ôf folgje dyn berjochten oan dat
kontakt de fêstleine rûte, en stjoere allinnich de repeaters op dy rûte. Giet
de rûte stikken, dan floodet de app opnij.

Berjochten oan in kanaal hawwe net ien adres, dus dy geane altyd as flood út.
Repeaters ûnthâlde wat se koartlyn trochjûn hawwe, en smite kopyen fuort dy't
oer in oare rûte nochris oankomme. In berjocht kin oer maksimaal 64 repeaters gean, of 32 as de preset 2-byte
ID's brûkt.

## Oerstappe fan Meshtastic {#meshtastic}

Op in protte boards draait MeshCore of Meshtastic, en do flashest de ien dy'tst wolst. Dit binne de ferskillen dy'tst it earst fernimst. Se binne basearre op MeshCore
v1.18.0 en de dokumintaasje fan Meshtastic fan novimber 2026.

- **Wa't berjochten trochjout.** Yn MeshCore dogge allinnich repeaters dat; dyn companion
  docht dat nea. Yn Meshtastic jout de standert clientrol berjochten ek troch,
  útsein as in oare node dat al dien hat.
- **Hoe fier in berjocht giet.** In MeshCore-berjocht kin oer op syn heechst 64
  repeaters gean. Meshtastic hâldt standert op nei 3 hops, en op syn heechst nei 7.
- **Mjitwearden fan oare nodes.** Repeaters en sensornodes yn MeshCore stjoere
  mjitwearden lykas batterijspanning as do derom freegest. Se stjoere se net
  nei de hiele mesh.
- **It ynternet.** De MeshCore-firmware hat gjin ferbining tusken meshes oer
  it ynternet. [Observers](/network/) jouwe wat se hearre troch oan kaarten, allinnich yn
  ien rjochting. Meshtastic hat in ynboude MQTT-module
  dy't berjochten tusken meshes oer it ynternet ferfiere kin.

## Fersifering en privacy {#encryption}

Dyn direkte berjochten binne fan ein ta ein fersifere: allinnich do en de oare
persoan kinne se lêze. In repeater sjocht foar wa't in pakket is allinnich as
in hint fan 1 byte.

Kanalen binne fersifere mei in dielde kaai. Wa't se lêze kin, hinget dus ôf
fan wa't dy kaai hat:

- **Public** stiet op elke companion klear. De kaai is iepenbier, dus
  elkenien kin it lêze.
- **Hashtag-kanalen**, lykas `#utrecht`, helje harren kaai út harren namme.
  Elkenien dy't de namme wit, kin meidwaan. Sjoch se dus ek as iepenbier.
- **Privee kanalen** brûke in willekeurige kaai dy'tst sels dielst,
  bygelyks as QR-koade.

Adverts binne ûndertekene, mar net fersifere. De namme fan dyn node, en syn
posysje as do dy dielst, sjocht elkenien binnen berik. Kies in namme dy't net
mear seit as do wolst.

## De 868 MHz-bân yn Europa {#band}

Yn Europa brûkt MeshCore in lyts stik fan de 868 MHz-bân. Dat stik mei
elkenien sûnder lisinsje brûke. De Europeeske radiopreset, EU/UK (Narrow),
leit op 869.618 MHz mei in kanaal fan 62.5 kHz. Dat falt binnen de
sub-bân fan 869.40-869.65 MHz, dy't maksimaal 500 mW e.r.p. talit. In apparaat
mei dêr op syn heechst 10% fan de tiid stjoere. Yn it
[juridyske diel fan de repeater-hantlieding](/repeater-guide/#legal) steane
de details en de grinzen per lân.

Elkenien yn in gebiet brûkt deselde preset, oars kinne de radio's elkoar net
hearre. Guon lannen en regio's brûke in fariant: dyn
[pleatslike groep](/community/) wit hokker.

## Wêr't minsken it foar brûke {#uses}

- Yn kontakt bliuwe op kuiertochten, op see en op festivals dêr't it mobile netwurk
  oerbelêste is of ûntbrekt.
- In reservekanaal foar famylje of buorlju as de stroom of de mobile netwurken
  útfalle.
- Pleatslik chatte op radio's dy't fan de minsken sels binne.
- Fan hûs út in plak op ôfstân kontrolearje. Repeaters en sensornodes jouwe harren
  batterijspanning en oare mjitwearden troch as do derom freegest.
- In sensor yn de gaten hâlde. In sensornode draait de firmware fan MeshCore foar mjittingen.
  Hy hâldt in skiednis fan syn mjitwearden by. As do dy abonnearrest, warskôget er
  dy, bygelyks as syn batterij leech rekket.
- Eat fier fuort skeakelje, lykas in pomp. Dat foegest do mei dyn eigen koade
  ta oan de sensorfirmware.
- Eksperimintearje mei radio, antennes, sinne-enerzjy en iepenboarnesoftware.

## Wêr't de gegevens weikomme {#data}

It sykjen op de side [pleatslike groepen](/community/) fynt in plak mei in
kopy fan de fergese plak- en postkoadelisten fan [GeoNames](https://www.geonames.org/),
ûnder de lisinsje
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Dy kopy stiet op
dizze side. Dyn sykopdracht giet nea fan dyn apparaat ôf, en der giet gjin
fersyk nei GeoNames.
