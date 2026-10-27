---
title: Aan de slag
lead: Van een nieuw bordje naar je eerste bericht op de mesh. Je hebt een LoRa-bordje nodig, een computer met Chrome of Edge, en een telefoon of laptop voor de app.
description: Flash MeshCore vanuit je browser, koppel de app, kies de radiopreset van jouw omgeving, verstuur je eerste bericht en doe mee in je lokale kanaal.
eyebrow: 6 stappen · MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '68c89544'
  seeded: '2026-10-26'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', '36a3eba3', '6da9fd7a', 'cb5fb72e', '89626504', 'a419ce79', 'aa273b20']
---

Deze stappen gaan uit van MeshCore firmware v1.18.0 en de officiële tools van
oktober 2026. Menunamen in de app kunnen per versie iets verschillen.

## 1. Kies een apparaat {#device}

Elk bordje op de [apparatenpagina](/devices/) waar companion bij staat, werkt.
Kies voor je eerste node een *companion*: de radio waarmee je berichten stuurt.
Je koppelt die via Bluetooth of USB aan je telefoon of laptop. Of je kiest er
een met eigen scherm en toetsenbord, die zelfstandig werkt.

Neem de 868 MHz-versie. De meegeleverde antenne voldoet; in de
[antennegids](/guides/antenna/) lees je hoe je er een controleert.

{{< callout type="warning" >}}
Sluit de antenne aan voordat je de radio aanzet. Een LoRa-radio die zonder
antenne zendt, kan zijn eigen chip beschadigen.
{{< /callout >}}

## 2. Flash de firmware {#flash}

1. Sluit het apparaat met een USB-datakabel aan op je computer.
2. Open de webflasher op [flasher.meshcore.io](https://flasher.meshcore.io)
   in Chrome of Edge. Die gebruikt Web Serial, wat andere browsers niet hebben.
3. Kies je apparaat en daarna de **Companion**-firmware voor **Bluetooth** (of
   USB, als je hem alleen met een kabel aan een computer gebruikt).
4. Flash. Sommige bordjes moeten eerst in updatemodus; de flasher legt uit
   hoe.

Gebruik *erase* alleen voor een schone start: wissen verwijdert de identiteit
van het apparaat en je contacten. Bij latere updates flash je zonder wissen.

## 3. Installeer de app {#app}

De officiële MeshCore-app is er voor Android, iOS, Windows en macOS;
[meshcore.io](https://meshcore.io) linkt naar elke versie. Er is ook een
webapp op [app.meshcore.nz](https://app.meshcore.nz), die in Chrome of Edge
op een computer draait.

## 4. Koppel je node {#pair}

Zet je node aan, open de app en maak via Bluetooth verbinding. Als de app om
een pincode vraagt:

- een node **met** scherm toont een pincode; typ die in;
- een node **zonder** scherm gebruikt `123456`.

Mislukt de koppeling? Verwijder het apparaat uit de Bluetooth-instellingen van
je telefoon en probeer het opnieuw. Geef je node daarna een naam. Anderen zien
die naam, dus gebruik je volledige naam of adres alleen als je dat zelf wilt.

## 5. Kies de radiopreset van jouw omgeving {#preset}

Alle radio's in een gebied gebruiken dezelfde frequentie en instellingen,
anders horen ze elkaar niet. Kies in de radio-instellingen van de app de preset
die jouw omgeving gebruikt. Buiten de gebieden hieronder gebruikt Europa
**EU/UK (Narrow)**. Nederland, Tsjechië, Hongarije, Slowakije, Portugal en
Zwitserland hebben een eigen preset, en Limburg in Nederland heeft een variant:

{{< presets >}}

Twijfel je? Je [lokale groep](/community/) weet welke preset jouw omgeving
gebruikt. De app haalt deze lijst op bij het MeshCore-project, dus voor een
nieuwe preset is geen app-update nodig.

## 6. Zeg hallo {#hello}

1. **Maak jezelf bekend.** Verstuur een *advertentie* vanuit de app. Een
   "flood"-advertentie reist via de repeaters (nodes die berichten doorgeven),
   zodat iedereen op de mesh je kan toevoegen.
   Companions maken zichzelf nooit automatisch bekend.
2. **Vind anderen.** Mensen verschijnen in je contacten zodra hun advertenties
   jou bereiken. Repeaters sturen standaard elke 47 uur een flood-advertentie,
   dus het kan 2 dagen duren voordat je lijst vol is.
3. **Stuur een bericht.** Open een contact en schrijf. Het eerste bericht
   floodt door het netwerk; de ontvanger meldt terug welke route het nam, en
   latere berichten volgen die route.
4. **Doe mee in kanalen.** Het kanaal **Public** staat al ingesteld; alles wat
   je daar schrijft, bereikt iedereen op de mesh. Voeg het *hashtagkanaal* van
   je regio toe (een naam die met `#` begint) door de naam in te typen. Je
   [lokale groep](/community/) vertelt je welke kanalen actief zijn.

## Als iets niet werkt {#troubleshooting}

**De app vindt mijn apparaat niet via Bluetooth.**
Waarschijnlijk heb je de USB-companion geflasht. Flash opnieuw en kies de
Bluetooth-versie. Op de Heltec V3 heeft de kleine ingebouwde Bluetooth-antenne
een kort bereik; houd je telefoon dichtbij.

**Koppelen blijft mislukken.**
Verwijder het apparaat uit de Bluetooth-instellingen van je telefoon, herstart
Bluetooth en koppel opnieuw met de pincode op het scherm of `123456`.

**Er verschijnt niemand in mijn contacten.**
Controleer of je preset bij jouw omgeving past. Verstuur een flood-advertentie.
Als er geen repeater binnen bereik is, hoor je alleen radio's dichtbij; de
[kaartpagina](/map/) laat zien waar repeaters staan.

**Bij een contact staat "laatst gezien" dagen geleden, terwijl die actief is.**
Een van de twee nodes heeft de verkeerde tijd. Een companion neemt de tijd over
van je telefoon; bij repeaters en roomservers (nodes die berichten voor een
groep bewaren) moet de eigenaar de tijd zelf instellen.

**De flasher kan de seriële poort op Linux niet openen.**
Je gebruiker heeft toegang tot de poort nodig, bijvoorbeeld met
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, of via lidmaatschap van de groep
`dialout`.

**Iets anders.** De
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
behandelt nog veel meer problemen.
