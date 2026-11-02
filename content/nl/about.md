---
title: Wat is MeshCore?
lead: MeshCore verstuurt tekstberichten via de radio, van node naar node. Je hebt geen internet of abonnement nodig.
description: 'Wat MeshCore wel en niet is: soorten nodes, routing, het verschil met Meshtastic, versleuteling en de 868 MHz-band.'
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

MeshCore is gratis software voor kleine LoRa-radio's. LoRa is een radiotechniek
die weinig data ver verstuurt, met heel weinig stroom. Een radio met MeshCore
heet een *node*. Je koppelt hem aan de app op je telefoon of laptop, of je
gebruikt zijn eigen scherm en toetsenbord. Zo stuur je tekst naar mensen die
kilometers verderop zitten. Er zit geen zendmast, router of provider tussen.

De software is open source. De ontwikkeling gebeurt op
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore), onder de
MIT-licentie.

## Wat MeshCore niet is {#not}

Heb je nog geen ervaring met radio? Dit zijn de dingen die mensen het vaakst van MeshCore
verwachten, maar die het niet doet.

- **Het is geen internet of telefoon.** MeshCore verstuurt korte tekstberichten,
  ongeveer zo lang als een sms op je telefoon. Geen spraak, foto's, video of
  websites, en je bereikt er geen gewoon telefoonnummer mee.
- **Het is geen hulpdienst.** Geen enkele hulpdienst luistert mee op de mesh, en
  niemand belooft dat iemand je bericht leest. Bel in een noodgeval 112.
- **Het werkt niet meteen, en niet overal.** Een bericht springt van radio naar
  radio en kan er een paar seconden over doen, of helemaal niet aankomen. Of het
  doorkomt, hangt af van de repeaters om je heen, van hoogte, gebouwen en je
  antenne. Met een kleine radio binnenshuis bereik je vaak niemand; een repeater
  op een dak reikt kilometers ver.
- **Het is geen dienst die iemand voor je beheert.** Er is geen provider, geen
  helpdesk en geen belofte over dekking. De mesh bestaat waar mensen uit de
  community repeaters hebben neergezet, en nergens anders.
- **Niet alles op de mesh is privé.** Directe berichten zijn versleuteld, maar
  Public en de hashtagkanalen kan iedereen lezen, en iedereen binnen bereik ziet
  de naam en gedeelde positie van je node.
  [Observers](/network/) geven wat ze horen door aan openbare kaarten. In het
  [gedeelte over versleuteling](#encryption) lees je wat privé blijft.
- **Het is niet onbeperkt.** Iedereen in een gebied deelt één radiokanaal, en de
  regels voor de [868 MHz-band](#band) beperken hoe lang elke radio mag zenden.
  Elk bericht kost alle anderen zendtijd, dus bots, frequente advertenties en
  testberichten vertragen de mesh voor iedereen.
- **Het is geen Meshtastic.** Meshtastic is een ander systeem dat op grotendeels
  dezelfde boards draait. De twee kunnen niet met elkaar communiceren.
  [Overstappen van Meshtastic](#meshtastic) laat zien wat er anders werkt.

## De mesh in een minuut {#mesh}

Eén LoRa-radio reikt in een stad een paar kilometer, en vanaf een heuvel of dak
veel verder. Om verder te komen, geven radio's berichten aan elkaar door: dat
is een *mesh*. In MeshCore doen radio's die *repeaters* heten het doorgeven.
Een repeater die een bericht hoort, zendt het opnieuw uit. Zo kan het een hele
regio doorkruisen.

Niemand is eigenaar van de mesh. Elke node en elke repeater is van iemand uit
de community. De mesh reikt zo ver als hun repeaters.

## De 3 soorten node {#roles}

Je kiest de soort van een node als je hem flasht. Je eerste node is een
companion.

**Companion.** Je eigen radio. Hij maakt via Bluetooth of USB een koppeling met
de MeshCore-app op je telefoon of laptop. Sommige hebben een eigen scherm en
toetsenbord. In de app lees en typ je. De companion bewaart je contacten en
kanalen, en de berichten die binnenkwamen terwijl de app niet verbonden was.
Een companion geeft geen berichten voor anderen door.

**Repeater.** Een radio op een hoge plek die berichten voor iedereen doorgeeft.
De meeste werken op zonne-energie. Een eigen repeater heb je alleen nodig waar
de mesh nog niet komt. Hij heeft geen eigen app. Je stelt hem in via USB, of
je logt in met een wachtwoord en beheert hem via de radio. In de
[repeatergids](/repeater-guide/) lees je hoe.

**Room server.** Een klein prikbord op de mesh. Als je inlogt, krijg je de
berichten die je miste toen je buiten bereik was, tot de laatste 32. Hij
bewaart ze alleen in het geheugen. Na een herstart of stroomstoring zijn ze
dus weg. Een lokale groep gebruikt er een voor aankondigingen.

## Hoe een bericht zijn weg vindt {#routing}

Elke node heeft een geheime sleutel en een publieke sleutel. De publieke
sleutel is zijn identiteit. Een node maakt zich bekend met een *advertentie*:
een ondertekend pakket met zijn naam en, als je dat wilt, zijn positie. Iemand
verschijnt in je contacten zodra een van zijn advertenties je bereikt heeft, of
als je zijn QR-code scant. In de app zit een knop om je eigen advertentie te
versturen.

Je eerste bericht aan een contact gaat als *flood* de lucht in. Elke repeater die het
hoort, geeft het één keer door en voegt onderweg zijn eigen korte ID toe. Het
antwoord neemt die lijst met ID's mee terug. Vanaf dan volgen je berichten aan
dat contact het vastgelegde pad, en zenden alleen de repeaters op dat pad. Valt
het pad weg, dan doet de app opnieuw een flood.

Berichten aan een kanaal hebben niet één adres, dus die gaan altijd als
flood. Repeaters onthouden wat ze kort geleden hebben doorgegeven. Kopieën die
via een andere route nog eens binnenkomen, gooien ze weg. Een bericht kan
langs maximaal 64 repeaters gaan, of 32 als de preset ID's van 2 bytes
gebruikt.

## Overstappen van Meshtastic {#meshtastic}

Op veel boards draait MeshCore of Meshtastic, en je flasht degene die je wilt. Dit zijn de verschillen die je het eerst opvallen. Ze gaan uit van MeshCore v1.18.0 en de documentatie van Meshtastic van november 2026.

- **Wie berichten doorgeeft.** In MeshCore doen alleen repeaters dat; je companion
  doet het nooit. In Meshtastic geeft ook de standaardrol client berichten door,
  tenzij een andere node dat al heeft gedaan.
- **Hoe ver een bericht komt.** Een MeshCore-bericht kan langs maximaal 64
  repeaters gaan. Meshtastic stopt standaard na 3 hops, en uiterlijk na 7.
- **Metingen van andere nodes.** In MeshCore sturen repeaters en sensornodes
  metingen zoals de batterijspanning als je erom vraagt. Ze sturen die niet naar
  de hele mesh.
- **Het internet.** De MeshCore-firmware kan meshes niet via het internet met
  elkaar verbinden. [Observers](/network/) melden wat ze horen aan kaarten, alleen
  in die richting. Meshtastic heeft een ingebouwde MQTT-module die berichten via
  het internet tussen meshes kan overbrengen.

## Versleuteling en privacy {#encryption}

Je directe berichten zijn end-to-end versleuteld: alleen jij en de ander
kunnen ze lezen. Van de ontvanger van een pakket ziet een repeater alleen een hint
van 1 byte.

Kanalen zijn versleuteld met een gedeelde sleutel. Wie ze kan lezen, hangt dus
af van wie die sleutel heeft:

- **Public** staat op elke companion ingesteld. De sleutel is openbaar, dus
  iedereen kan het lezen.
- **Hashtagkanalen**, zoals `#utrecht`, halen hun sleutel uit hun naam. Wie de
  naam kent, kan meedoen. Beschouw ze dus ook als openbaar.
- **Privékanalen** gebruiken een willekeurige sleutel die je zelf deelt,
  bijvoorbeeld als QR-code.

Advertenties zijn ondertekend, maar niet versleuteld. De naam van je node, en
zijn positie als je die deelt, ziet iedereen binnen bereik. Kies een naam die
niet meer zegt dan je wilt.

## De 868 MHz-band in Europa {#band}

In Europa gebruikt MeshCore een klein deel van de 868 MHz-band. Die band mag
iedereen zonder vergunning gebruiken. De Europese radiopreset, EU/UK (Narrow),
zit op 869.618 MHz met een kanaal van 62.5 kHz. Dat valt binnen de subband
869.40-869.65 MHz, die tot 500 mW e.r.p. toestaat. Een apparaat mag daar
hooguit 10% van de tijd zenden. Het
[juridische deel van de repeatergids](/repeater-guide/#legal) geeft de details
en de limieten per land.

Iedereen in een gebied gebruikt dezelfde preset, anders horen de radio's
elkaar niet. Sommige landen en regio's gebruiken een variant: je
[lokale groep](/community/) weet welke.

## Waar mensen het voor gebruiken {#uses}

- Contact houden tijdens wandeltochten, op zee en op festivals waar het mobiele netwerk
  overbelast is of ontbreekt.
- Een reservekanaal voor familie of buren als de stroom of de mobiele netwerken
  uitvallen.
- Lokaal chatten op radio's die van mensen zelf zijn.
- Vanuit huis een afgelegen plek controleren. Repeaters en sensornodes melden hun
  batterijspanning en andere meetwaarden als je erom vraagt.
- Een sensor in de gaten houden. Op een sensornode draait de MeshCore-firmware voor
  metingen. Hij bewaart de geschiedenis van zijn metingen. Als je je
  abonneert, waarschuwt hij je, bijvoorbeeld als zijn batterij bijna leeg is.
- Iets schakelen dat ver weg staat, zoals een pomp. Dat voeg je met je eigen code toe aan
  de sensorfirmware.
- Experimenteren met radio, antennes, zonne-energie en opensourcesoftware.

## Waar de gegevens vandaan komen {#data}

De zoekfunctie op de pagina [lokale groepen](/community/) vindt plaatsen in een
kopie van de gratis lijsten met plaatsen en postcodes van
[GeoNames](https://www.geonames.org/), met licentie
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Die kopie staat op
deze site. Je zoekopdracht blijft op je eigen apparaat, en er gaat geen verzoek
naar GeoNames.
