---
title: Kom godt i gang
lead: Fra et nyt board til din første besked på meshet. Du skal have et LoRa-board, en computer med Chrome eller Edge og en telefon eller laptop til appen.
description: Flash MeshCore fra din browser, par appen, vælg det radiopreset dit område bruger, send din første besked og kom med i din lokale kanal.
eyebrow: 6 trin · MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '68c89544'
  seeded: '2026-10-26'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', '36a3eba3', '6da9fd7a', 'cb5fb72e', '89626504', 'a419ce79', 'aa273b20']
---

Disse trin følger MeshCore-firmware v1.18.0 og de officielle værktøjer fra
oktober 2026. Menunavne i appen kan variere lidt mellem versioner.

## 1. Vælg en enhed {#device}

Alle boards på [enhedssiden](/devices/), der er markeret som companion, virker. Til
din første node bør du vælge en *companion*: den radio du sender beskeder fra. Du parrer den med
din telefon eller laptop via Bluetooth eller USB. Du kan også vælge en med egen skærm
og eget tastatur, som fungerer alene.

Køb versionen til 868 MHz. Den medfølgende antenne klarer opgaven, og
[antenneguiden](/guides/antenna/) viser, hvordan du tjekker en.

{{< callout type="warning" >}}
Sæt antennen på, før du tænder radioen. En LoRa-radio, der
sender uden antenne, kan beskadige sin egen chip.
{{< /callout >}}

## 2. Flash firmwaren {#flash}

1. Slut enheden til din computer med et USB-datakabel.
2. Åbn webflasheren på [flasher.meshcore.io](https://flasher.meshcore.io)
   i Chrome eller Edge. Den bruger Web Serial, som andre browsere ikke har.
3. Vælg din enhed og derefter **Companion**-firmwaren til **Bluetooth** (eller
   USB, hvis du kun vil bruge den med et kabel til computeren).
4. Flash. Nogle boards skal først i opdateringstilstand; flasheren fortæller dig
   hvordan.

Brug kun *erase* til en helt frisk start: sletning fjerner enhedens identitet
og dine kontakter. Ved senere opdateringer skal du flashe uden at slette.

## 3. Installer appen {#app}

Den officielle MeshCore-app findes til Android, iOS, Windows og macOS;
[meshcore.io](https://meshcore.io) linker til alle versioner. Der findes også en
webapp på [app.meshcore.nz](https://app.meshcore.nz), som kører i Chrome eller
Edge på en computer.

## 4. Par din node {#pair}

Tænd din node, åbn appen og forbind til den via Bluetooth. Når
du bliver bedt om en PIN:

- en node **med** skærm viser en PIN; indtast den;
- en node **uden** skærm bruger `123456`.

Hvis parringen mislykkes, skal du fjerne enheden fra telefonens Bluetooth-indstillinger og
prøve igen. Giv derefter din node et navn. Andre kan se navnet, så brug ikke
dit fulde navn eller din adresse, medmindre du selv vil.

## 5. Vælg dit områdes radiopreset {#preset}

Alle radioer i et område bruger samme frekvens og samme indstillinger, ellers kan de ikke
høre hinanden. Vælg det preset dit område bruger i appens radioindstillinger.
Uden for områderne nedenfor bruger Europa **EU/UK (Narrow)**. Holland,
Tjekkiet, Ungarn, Slovakiet, Portugal og Schweiz bruger deres egne, og
Limburg i Holland har en variant:

{{< presets >}}

Er du i tvivl? Din [lokale gruppe](/community/) ved, hvilket preset dit område bruger.
Appen henter denne liste fra MeshCore-projektet, så et nyt preset kræver
ingen opdatering af appen.

## 6. Sig hej {#hello}

1. **Gør opmærksom på dig selv.** Send en *advert* fra appen. En "flood"-advert
   rejser gennem repeaterne (noder der sender beskeder videre), så alle
   på meshet kan tilføje dig.
   Companions annoncerer aldrig sig selv automatisk.
2. **Find andre.** Folk dukker op i dine kontakter, når deres adverts når
   dig. Repeatere sender som standard en flood-advert hver 47 timer, så det kan
   tage 2 dage, før din liste er fyldt op.
3. **Send en besked.** Åbn en kontakt og skriv. Den første besked flooder
   netværket; modtageren melder tilbage, hvilken rute den tog, og senere
   beskeder følger den rute.
4. **Kom med i kanaler.** Kanalen **Public** er allerede sat op; alt hvad du
   skriver dér, når alle på meshet. Tilføj din regions *hashtag-kanal*
   (et navn der starter med `#`) ved at indtaste navnet. Din
   [lokale gruppe](/community/) fortæller dig, hvilke kanaler der er aktive.

## Når noget ikke virker {#troubleshooting}

**Appen finder ikke min enhed via Bluetooth.**
Du har sikkert flashet USB-companion-versionen. Flash igen og vælg
Bluetooth-versionen. På Heltec V3 har den lille indbyggede Bluetooth-antenne
kort rækkevidde; hold telefonen tæt på.

**Parringen mislykkes hele tiden.**
Fjern enheden fra telefonens Bluetooth-indstillinger, genstart Bluetooth,
og par igen med PIN-koden på skærmen eller `123456`.

**Ingen dukker op i mine kontakter.**
Tjek, at dit preset passer til dit område. Send en flood-advert. Hvis der ikke er nogen
repeater inden for rækkevidde, hører du kun radioer tæt på;
[kortsiden](/map/) viser, hvor repeaterne står.

**En kontakt viser "sidst set" for flere dage siden, selvom vedkommende er aktiv.**
En af de to noder har forkert tid. En companion tager tiden fra
din telefon; repeatere og room servers (noder der gemmer beskeder til en
gruppe) skal have tiden sat af deres ejer.

**Flasheren kan ikke åbne den serielle port på Linux.**
Din bruger skal have adgang til porten, for eksempel med
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, eller ved at være medlem af gruppen `dialout`.

**Noget andet.**
[MeshCore-FAQ'en](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
dækker mange flere problemer.
