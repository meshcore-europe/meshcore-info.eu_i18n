---
title: Wat is MeshCore?
lead: MeshCore stjoert tekstberjochten oer de radio, fan node nei node. It wurket sûnder ynternet en sûnder abonnemint.
description: 'Wat MeshCore is en wat net: de mesh, companions, repeaters en room servers, routearring, fersifering en de 868 MHz-bân yn Europa.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '78bc31e8'
  seeded: '2026-10-31'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['aa768ac3', 'c9b24089', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '655373a9', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b9fc8810', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '0eb54b47', '02f1fe2f', 'e6b5b258']
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

- **It is gjin ynternet en gjin telefoan.** MeshCore stjoert koarte
  tekstberjochten, sawat sa lang as in sms op dyn telefoan. Gjin spraak, foto's,
  fideo of websites, en do kinst gjin gewoan telefoannûmer berikke.
- **It is gjin needtsjinst.** Gjin needtsjinst harket mei op de mesh, en
  nimmen belooft dat ien dyn berjocht lêst. By need belsto 112.
- **It is net direkt, en net oeral.** In berjocht springt fan radio nei
  radio. Dat kin in pear sekonden duorje, of it komt hielendal net oan. Oft it
  trochkomt, hinget ôf fan de repeaters om dy hinne, fan hichte, gebouwen en
  dyn antenne. In lytse radio binnen berikt faak nimmen; in repeater op in dak
  berikt kilometers.
- **It is gjin tsjinst dy't ien foar dy draait.** Der is gjin provider, gjin
  helpdesk en gjin tasizzing oer dekking. De mesh bestiet dêr't minsken út de
  mienskip repeaters pleatst hawwe, en nearne oars.
- **Net alles is privee.** Direkte berjochten binne fersifere. Mar Public en
  de hashtag-kanalen kin elkenien lêze. De namme fan dyn node en de posysje
  dy'tst dielst, sjocht elkenien binnen berik.
  [Observers](/network/) melde wat se hearre oan iepenbiere kaarten. Yn
  it [diel oer fersifering](#encryption) lêsto wat privee bliuwt.
- **It is net ûnbeheind.** Elkenien yn in gebiet dielt ien radiokanaal. De
  regels foar de [868 MHz-bân](#band) beheine hoe lang elke radio stjoere mei.
  Elk berjocht nimt stjoertiid ôf fan alle oaren. Bots, faak stjoerde adverts en
  testberjochten meitsje de mesh dus stadiger foar elkenien.
- **It is gjin Meshtastic.** Meshtastic is in oar systeem dat op sawat
  deselde boards draait. De twa kinne net mei inoar prate.

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

- Kontakt hâlde by kuiertochten, op see en op festivals dêr't it mobile
  netwurk oerbelêste is of ûntbrekt.
- In reservekanaal foar famylje of buorlju as stroom of mobile netwurken
  útfalle.
- Pleatslik petearjen op radio's dy't minsken sels hawwe.
- Eksperimintearje mei radio, antennes, sinne-enerzjy en iepenboarnesoftware.

## Wêr't de gegevens weikomme {#data}

It sykjen op de side [pleatslike groepen](/community/) fynt in plak mei in
kopy fan de fergese plak- en postkoadelisten fan [GeoNames](https://www.geonames.org/),
ûnder de lisinsje
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Dy kopy stiet op
dizze side. Dyn sykopdracht giet nea fan dyn apparaat ôf, en der giet gjin
fersyk nei GeoNames.
