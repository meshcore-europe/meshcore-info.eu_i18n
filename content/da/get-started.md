---
title: Kom i gang
lead: Fra et nyt board til din første besked på mesh-netværket. Du skal bruge et LoRa-board, en computer med Chrome eller Edge og en telefon eller bærbar til appen.
description: Flash MeshCore fra din browser, par appen, vælg den radioindstilling dit område bruger, send din første besked og kom med i din lokale kanal.
eyebrow: 6 trin · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-10-31'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Trinene følger MeshCore-firmware v1.18.0 og de officielle værktøjer fra
oktober 2026. Menunavnene i appen kan variere lidt mellem versionerne.

## 1. Vælg en enhed {#device}

Alle boards på [siden med enheder](/devices/), der har companion på listen, kan bruges.
Til din første node vælger du en *companion*: den radio, du sender beskeder fra.
Du parrer den med din telefon eller bærbare via Bluetooth eller USB. Du kan også
vælge en med egen skærm og eget tastatur, som virker på egen hånd.

Køb 868 MHz-versionen. Den medfølgende antenne er god nok. I
[antenneguiden](/guides/antenna/) kan du se, hvordan du tjekker en antenne.

{{< callout type="warning" >}}
Sæt antennen på, før du tænder radioen. En LoRa-radio, der sender uden
antenne, kan ødelægge sin egen chip.
{{< /callout >}}

## 2. Flash firmwaren {#flash}

1. Forbind enheden til din computer med et USB-datakabel.
2. Åbn webflasheren på [flasher.meshcore.io](https://flasher.meshcore.io)
   i Chrome eller Edge. Den bruger Web Serial, som andre browsere ikke har.
3. Vælg din enhed og derefter **Companion**-firmwaren til **Bluetooth** (eller
   USB, hvis du kun vil bruge den med et kabel til en computer).
4. Flash. Nogle boards skal først i opdateringstilstand. Flasheren fortæller dig
   hvordan.

Brug kun *erase*, når du vil starte helt forfra: sletningen fjerner enhedens identitet
og dine kontakter. Ved senere opdateringer flasher du uden at slette. Vil du beholde
din identitet efter en sletning, eksporterer du først din companions private nøgle
fra appen og importerer den bagefter.

## 3. Installer appen {#app}

Den officielle MeshCore-app findes til Android, iOS, Windows og macOS.
På [meshcore.io](https://meshcore.io) finder du links til alle versioner. Der er også en
webapp på [app.meshcore.nz](https://app.meshcore.nz), som kører i Chrome eller
Edge på en computer.

## 4. Par din node {#pair}

Tænd din node, åbn appen og forbind til noden via Bluetooth. Når appen
beder om en PIN-kode:

- en node **med** skærm viser en PIN-kode, og den indtaster du;
- en node **uden** skærm bruger `123456`.

Mislykkes parringen, så fjern enheden i telefonens Bluetooth-indstillinger og
prøv igen. Giv derefter din node et navn. Andre kan se navnet, så brug ikke
dit fulde navn eller din adresse, medmindre du vil.

## 5. Vælg dit områdes radioindstilling {#preset}

Alle radioer i et område bruger samme frekvens og indstillinger, ellers kan de
ikke høre hinanden. Vælg den indstilling, dit område bruger, i appens radioindstillinger.
Uden for områderne nedenfor bruger Europa **EU/UK (Narrow)**. Holland,
Tjekkiet, Ungarn, Slovakiet, Portugal og Schweiz har deres egne, og
Limburg i Holland har en variant:

{{< presets >}}

Tilbyder din enhed ikke dit områdes indstilling? Så indtaster du de 4 værdier fra
tabellen manuelt i appens radioindstillinger: frekvens, båndbredde, spreading
factor og coding rate. En node med andre værdier hører ikke mesh-netværket.

Er du i tvivl? Din [lokale gruppe](/community/) ved, hvilken indstilling dit område bruger.
Appen henter listen fra MeshCore-projektet, så en ny indstilling kræver
ingen opdatering af appen.

## 6. Sig hej {#hello}

1. **Annoncér dig selv.** Send en *advert* fra appen. En "flood"-advert
   går videre gennem repeaterne (noder, der sender beskeder videre), så alle
   på mesh-netværket kan tilføje dig.
   Companions annoncerer sig aldrig selv automatisk.
2. **Find andre.** Folk dukker op i dine kontakter, når deres adverts når
   frem til dig. Repeatere sender som standard en flood-advert hver 47. time, så det
   kan tage 2 dage, før din liste fyldes op.
3. **Send en besked.** Åbn en kontakt og skriv. Den første besked sendes som flood
   gennem netværket. Modtageren melder den sti tilbage, beskeden tog, og senere
   beskeder følger den sti.
4. **Tilmeld dig kanaler.** Kanalen **Public** er allerede sat op. Alt, hvad du
   skriver der, når ud til alle på mesh-netværket. Tilføj din regions *hashtag-kanal*
   (et navn, der starter med `#`), ved at skrive dens navn. Din
   [lokale gruppe](/community/) kan fortælle dig, hvilke kanaler der er aktive.

## Når noget ikke virker {#troubleshooting}

**Appen finder ikke min enhed via Bluetooth.**
Du har sandsynligvis flashet USB-versionen af companion. Flash igen, og vælg
Bluetooth-versionen. På Heltec V3 har den lille indbyggede Bluetooth-antenne
kort rækkevidde. Hold telefonen tæt på.

**Parringen mislykkes igen og igen.**
Fjern enheden i telefonens Bluetooth-indstillinger, genstart Bluetooth,
og par igen med PIN-koden på skærmen eller `123456`.

**Der dukker ingen op i mine kontakter.**
Tjek, at din indstilling passer til dit område. Send en flood-advert. Er der ingen
repeater inden for rækkevidde, hører du kun radioer tæt på. På
[kortsiden](/map/) kan du se, hvor der står repeatere.

**En kontakt står som "sidst set" for flere dage siden, selvom personen er aktiv.**
En af de to noder har forkert tid. En companion henter tiden fra
din telefon. Repeatere og room servers (noder, der gemmer beskeder for en
gruppe) skal have tiden sat af deres ejer.

**En direkte besked kommer aldrig frem.**
I skal begge have hinanden som kontakt. En node smider en besked fra en ukendt
afsender væk uden at give afsenderen besked. Send en flood-advert, og bed
den anden person sende en også. Tjek i appen, at den tilføjer nye
kontakter automatisk. Den tilføjer kun noder inden for sin hop-grænse.

**Gamle kontakter virker, men nye får aldrig forbindelse.**
En første besked sendes som flood, og en repeater sender den kun videre, når den har
beskedens region. Senere beskeder følger en lært sti, som intet regionstjek stopper.
Spørg din [lokale gruppe](/community/), hvilke regioner repeaterne
omkring dig har, og tjek [indstillingerne for dit område](/guides/settings/#traffic).

**Appen kan ikke længere forbinde til din companion.**
Nogle boards har en brugerknap, for eksempel nogle RAK-boards og Heltec T114.
Hold den inde i de første 8 sekunder, efter boardet starter. Så åbner din companion
en nødkonsol via USB. I konsollen på
[flasher.meshcore.io](https://flasher.meshcore.io) sætter du en ny Bluetooth-PIN med
`set pin <pin>`, og med `erase` sletter du enheden.

**Flasheren kan ikke åbne den serielle port på Linux.**
Din bruger skal have adgang til porten, for eksempel med
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, eller være medlem af gruppen
`dialout`.

**Noget andet.** I
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
finder du svar på mange flere problemer.
