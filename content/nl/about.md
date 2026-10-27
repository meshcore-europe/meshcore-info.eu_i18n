---
title: Wat is MeshCore?
lead: MeshCore verstuurt tekstberichten via de radio, van node naar node. Het werkt zonder internet of abonnement.
description: 'Wat MeshCore wel en niet is: de mesh, companions, repeaters en room servers, routering, versleuteling en de 868 MHz-band in Europa.'
eyebrow: MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '33e571f0'
  seeded: '2026-10-26'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['a3a6c1ff', '007314d2', 'f1f23981', '493b444f', '429f699c', 'f8008f48', '655373a9']
---

MeshCore is gratis software voor kleine LoRa-radio's. LoRa is een radiotechniek
die weinig data ver verstuurt, op heel weinig stroom. Een radio met MeshCore
noem je een *node*. Gekoppeld aan de app op je telefoon of laptop, of met een
eigen scherm en toetsenbord, verstuurt hij tekst naar mensen kilometers verderop. Er zit geen zendmast, router of provider tussen.

MeshCore verstuurt alleen korte tekstberichten: geen spraak, foto's of
internetverkeer.
Een bericht kan een paar seconden onderweg zijn, en of het aankomt hangt af
van de repeaters in je omgeving. Het vervangt de hulpdiensten niet: bel bij
een noodgeval 112.

De software is open source en wordt ontwikkeld op
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) onder de
MIT-licentie.

## De mesh in een minuut {#mesh}

Eén LoRa-radio haalt een paar kilometer in een stad, en veel meer vanaf een
heuvel of een dak. Om verder te komen geven radio's berichten voor elkaar
door: dat is een *mesh*. In MeshCore doen radio's die *repeaters* heten dat
doorgeven. Een repeater die een bericht hoort, zendt het opnieuw uit, zodat
het een hele regio kan oversteken.

Niemand is eigenaar van de mesh. Elke node en elke repeater is van iemand uit
de community. De mesh is zo goed als de repeaters die mensen neerzetten.

## De 3 soorten node {#roles}

Je kiest de soort node op het moment dat je hem flasht. Je eerste node is een
companion.

**Companion.** Je eigen radio. Hij koppelt via Bluetooth of USB met de
MeshCore-app op je telefoon of laptop; sommige hebben een eigen scherm en
toetsenbord. In de app lees en typ je. De companion bewaart je contacten en
kanalen, en de berichten die binnenkwamen terwijl de app niet verbonden was. Een companion geeft geen berichten door voor anderen.

**Repeater.** Een radio die hoog hangt en berichten doorgeeft voor iedereen.
De meeste draaien op zonne-energie. Je hebt er alleen zelf een nodig waar de
mesh nog niet komt. Hij heeft geen eigen app. Je stelt hem in via USB, of je
logt in met een wachtwoord en beheert hem via de radio. De
[repeatergids](/repeater-guide/) laat zien hoe.

**Room server.** Een klein prikbord op de mesh. Als je inlogt, krijg je de
berichten die je miste terwijl je buiten bereik was, tot de laatste 32. Een
lokale groep gebruikt er een voor mededelingen.

## Hoe een bericht zijn weg vindt {#routing}

Elke node heeft een geheime sleutel en een publieke sleutel. De publieke
sleutel is zijn identiteit. Een node maakt zichzelf bekend met een
*advertentie*: een ondertekend pakket met zijn naam en, als je dat wilt, zijn
positie. Iemand verschijnt in je contacten nadat een van zijn advertenties
jou bereikte, of als je zijn QR-code scant. De app heeft een knop om je eigen
advertentie te versturen.

Je eerste bericht aan een contact gaat de deur uit als een *flood*. Elke
repeater die het hoort, geeft het één keer door en voegt onderweg zijn eigen
korte ID toe. Het antwoord brengt die lijst met ID's terug. Vanaf dan volgen
je berichten aan dat contact de vastgelegde route, en zenden alleen de
repeaters op die route. Als de route breekt, floodt de app opnieuw.

Berichten aan een kanaal hebben geen enkel adres, dus die flooden altijd.
Repeaters onthouden wat ze kort geleden doorgaven en laten kopieën vallen die
via een andere route nog eens aankomen. Een bericht kan tot 64 repeaters
passeren, of 32 waar de preset ID's van 2 bytes gebruikt.

## Versleuteling en privacy {#encryption}

Je directe berichten zijn end-to-end versleuteld: alleen jij en de ander
kunnen ze lezen. Een repeater ziet voor wie een pakket is alleen als een hint
van 1 byte.

Kanalen zijn versleuteld met een gedeelde sleutel, dus wie ze kan lezen hangt
af van wie die sleutel heeft:

- **Public** staat op elke companion ingesteld. De sleutel ervan is
  gepubliceerd, dus iedereen kan het lezen.
- **Hashtagkanalen**, zoals `#utrecht`, halen hun sleutel uit hun naam.
  Iedereen die de naam kent kan meedoen, dus behandel ze ook als openbaar.
- **Privékanalen** gebruiken een willekeurige sleutel die je zelf deelt,
  bijvoorbeeld als QR-code.

Advertenties zijn ondertekend maar niet versleuteld. De naam van je node, en
zijn positie als je die deelt, zijn zichtbaar voor iedereen binnen bereik.
Kies een naam die niet meer zegt dan je wilt.

## De 868 MHz-band in Europa {#band}

In Europa gebruikt MeshCore een klein deel van de 868 MHz-band dat iedereen
zonder vergunning mag gebruiken. De Europese radiopreset, EU/UK (Narrow), zit
op 869.618 MHz op een kanaal van 62.5 kHz. Dat valt binnen de subband
869.40-869.65 MHz, waar tot 500 mW e.r.p. is toegestaan. Een apparaat mag daar
hoogstens 10% van de tijd zenden. Het
[juridische deel van de repeatergids](/repeater-guide/#legal) geeft de
details en de limieten per land.

Iedereen in een gebied gebruikt dezelfde preset, anders kunnen de radio's
elkaar niet horen. Sommige landen en regio's gebruiken een variant: je
[lokale groep](/community/) weet welke.

## Waar mensen het voor gebruiken {#uses}

- Contact houden tijdens wandeltochten, op zee en op festivals waar het
  mobiele netwerk overbelast is of ontbreekt.
- Een reservekanaal voor familie of buren als de stroom of het mobiele
  netwerk uitvalt.
- Lokaal chatten op radio's die mensen zelf bezitten.
- Experimenteren met radio, antennes, zonne-energie en open-source software.
