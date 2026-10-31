---
title: Aan de slag
lead: Van een nieuw bordje tot je eerste bericht op de mesh. Je hebt een LoRa-bordje nodig, een computer met Chrome of Edge, en een telefoon of laptop voor de app.
description: Flash MeshCore vanuit je browser, koppel de app, kies het radiopreset van je omgeving, stuur je eerste bericht en word lid van je lokale kanaal.
eyebrow: 6 stappen · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-10-31'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Deze stappen gaan uit van MeshCore-firmware v1.18.0 en de officiële tools van
oktober 2026. Menunamen in de app kunnen per versie iets verschillen.

## 1. Kies een apparaat {#device}

Elk bordje op de [apparatenpagina](/devices/) waarbij companion staat, werkt. Kies
voor je eerste node een *companion*: de radio waarmee je berichten stuurt. Je
koppelt hem via Bluetooth of USB aan je telefoon of laptop. Of je kiest er een
met eigen scherm en toetsenbord, die zelfstandig werkt.

Neem de 868 MHz-versie. De meegeleverde antenne volstaat. In de
[antennegids](/guides/antenna/) lees je hoe je een antenne controleert.

{{< callout type="warning" >}}
Sluit de antenne aan voordat je de radio aanzet. Een LoRa-radio die zonder
antenne zendt, kan zijn eigen chip beschadigen.
{{< /callout >}}

## 2. Flash de firmware {#flash}

1. Sluit het apparaat met een USB-datakabel aan op je computer.
2. Open de webflasher op [flasher.meshcore.io](https://flasher.meshcore.io)
   in Chrome of Edge. De flasher gebruikt Web Serial, en dat hebben andere browsers niet.
3. Kies je apparaat en daarna de **Companion**-firmware voor **Bluetooth** (of
   USB, als je hem alleen met een kabel aan een computer gebruikt).
4. Flash. Sommige bordjes moeten eerst in updatemodus; de flasher legt uit
   hoe dat moet.

Gebruik *erase* alleen als je helemaal opnieuw wilt beginnen. Met wissen
verlies je de identiteit van het apparaat en je contacten. Flash latere
updates zonder te wissen. Wil je je identiteit na het wissen houden? Exporteer
dan eerst de private key van je companion in de app en importeer hem daarna.

## 3. Installeer de app {#app}

De officiële MeshCore-app bestaat voor Android, iOS, Windows en macOS. Op
[meshcore.io](https://meshcore.io) vind je links naar elke versie. Er is ook
een webapp op [app.meshcore.nz](https://app.meshcore.nz), die op een computer
in Chrome of Edge draait.

## 4. Koppel je node {#pair}

Zet je node aan, open de app en maak via Bluetooth verbinding. Vraagt de app
om een pincode:

- een node **met** scherm toont een pincode; typ die in;
- een node **zonder** scherm gebruikt `123456`.

Mislukt de koppeling? Verwijder het apparaat dan uit de Bluetooth-instellingen
van je telefoon en probeer het opnieuw. Geef je node daarna een naam. Anderen
zien die naam, dus gebruik niet je volledige naam of adres, tenzij je dat wilt.

## 5. Kies het radiopreset van je omgeving {#preset}

Alle radio's in een omgeving gebruiken dezelfde frequentie en instellingen.
Anders horen ze elkaar niet. Kies in de radio-instellingen van de app het
preset dat je omgeving gebruikt. Buiten de gebieden hieronder gebruikt Europa
**EU/UK (Narrow)**. Nederland, Tsjechië, Hongarije, Slowakije, Portugal en
Zwitserland hebben een eigen preset, en Limburg in Nederland heeft een variant:

{{< presets >}}

Biedt je apparaat het preset van je omgeving niet aan? Vul dan de 4 waarden
uit de tabel zelf in bij de radio-instellingen van de app: frequentie,
bandbreedte, spreading factor en coding rate. Een node met andere waarden hoort
de mesh niet.

Twijfel je? Je [lokale groep](/community/) weet welk preset je omgeving
gebruikt. De app haalt deze lijst op bij het MeshCore-project. Voor een nieuw
preset hoeft de app dus niet bijgewerkt te worden.

## 6. Zeg hallo {#hello}

1. **Maak jezelf bekend.** Stuur vanuit de app een *advertentie*. Een
   flood-advertentie gaat via de repeaters (nodes die berichten doorgeven) de
   hele mesh rond, zodat iedereen je kan toevoegen.
   Een companion maakt zich nooit vanzelf bekend.
2. **Vind anderen.** Mensen verschijnen in je contacten zodra hun advertenties
   je bereiken. Repeaters sturen standaard elke 47 uur een flood-advertentie.
   Het kan dus 2 dagen duren voordat je lijst gevuld is.
3. **Stuur een bericht.** Open een contact en schrijf. Het eerste bericht gaat
   als flood door het netwerk. De ontvanger meldt terug welke route het nam, en
   latere berichten volgen die route.
4. **Word lid van kanalen.** Het kanaal **Public** staat al klaar. Alles wat je
   daar schrijft, bereikt iedereen op de mesh. Voeg het *hashtagkanaal* van je
   regio toe (een naam die met `#` begint) door de naam in te typen. Je
   [lokale groep](/community/) vertelt je welke kanalen actief zijn.

## Als iets niet werkt {#troubleshooting}

**De app vindt mijn apparaat niet via Bluetooth.**
Waarschijnlijk heb je de USB-companion geflasht. Flash opnieuw en kies de
Bluetooth-versie. Op de Heltec V3 heeft de kleine ingebouwde Bluetooth-antenne
een kort bereik. Houd je telefoon dichtbij.

**De koppeling mislukt steeds.**
Verwijder het apparaat uit de Bluetooth-instellingen van je telefoon, herstart
Bluetooth en koppel opnieuw met de pincode op het scherm of `123456`.

**Er verschijnt niemand in mijn contacten.**
Controleer of je preset bij je omgeving past. Stuur een flood-advertentie. Is
er geen repeater binnen bereik, dan hoor je alleen radio's vlak in de buurt. Op
de [kaartpagina](/map/) zie je waar repeaters staan.

**Een contact toont 'laatst gezien' van dagen geleden, terwijl die wel actief is.**
Een van de twee nodes heeft de verkeerde tijd. Een companion neemt de tijd over
van je telefoon. Bij repeaters en room servers (nodes die berichten voor een
groep bewaren) moet de eigenaar de tijd instellen.

**Een direct bericht komt nooit aan.**
Jij en de ander moeten elkaar allebei als contact hebben. Een node gooit een bericht van
een onbekende weg, zonder dat de afzender het merkt. Stuur een
flood-advertentie en vraag de ander om dat ook te doen. Controleer in de app of
die nieuwe contacten automatisch toevoegt. De app voegt alleen nodes toe binnen
de hoplimiet.

**Oude contacten werken, nieuwe krijgen nooit verbinding.**
Een eerste bericht gaat als flood, en een repeater geeft het alleen door als
hij de regio van het bericht heeft ingesteld. Latere berichten volgen een
geleerde route, en daar houdt geen regiocontrole ze tegen. Vraag je
[lokale groep](/community/) welke regio's de repeaters bij jou in de buurt
hebben, en bekijk [de instellingen voor je omgeving](/guides/settings/#traffic).

**De app maakt geen verbinding meer met je companion.**
Sommige bordjes hebben een gebruikersknop, zoals een aantal RAK-bordjes en de
Heltec T114. Houd die ingedrukt in de eerste 8 seconden nadat het bordje
opstart. De companion opent dan een herstelconsole via USB. In de console op
[flasher.meshcore.io](https://flasher.meshcore.io) stel je met `set pin <pin>`
een nieuwe Bluetooth-pincode in, en met `erase` wis je het apparaat.

**De flasher kan de seriële poort onder Linux niet openen.**
Je gebruiker heeft toegang tot de poort nodig, bijvoorbeeld met
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, of lidmaatschap van de groep
`dialout`.

**Iets anders.** De
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
behandelt nog veel meer problemen.
