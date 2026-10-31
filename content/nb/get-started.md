---
title: Kom i gang
lead: Fra et nytt kort til din første melding på meshen. Du trenger et LoRa-kort, en datamaskin med Chrome eller Edge og en telefon eller bærbar PC til appen.
description: Flash MeshCore fra nettleseren, par appen, velg radioforhåndsvalget området ditt bruker, send din første melding og bli med i den lokale kanalen.
eyebrow: 6 steg · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-10-31'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Disse stegene følger MeshCore-firmware v1.18.0 og de offisielle verktøyene fra
oktober 2026. Menynavnene i appen kan variere litt mellom versjonene.

## 1. Velg en enhet {#device}

Alle kort på [enhetssiden](/devices/) som står oppført med companion, fungerer.
Til din første node velger du en *companion*: radioen du sender meldinger fra.
Du parer den med telefonen eller den bærbare PC-en over Bluetooth eller USB.
Du kan også velge en med egen skjerm og eget tastatur, som fungerer alene.

Velg 868 MHz-versjonen. Antennen som følger med, holder fint.
[Antenneguiden](/guides/antenna/) viser hvordan du sjekker en antenne.

{{< callout type="warning" >}}
Fest antennen før du slår på radioen. En LoRa-radio som sender uten
antenne, kan skade sin egen brikke.
{{< /callout >}}

## 2. Flash firmwaren {#flash}

1. Koble enheten til datamaskinen med en USB-kabel som overfører data.
2. Åpne nettflasheren på [flasher.meshcore.io](https://flasher.meshcore.io)
   i Chrome eller Edge. Den bruker Web Serial, som andre nettlesere ikke har.
3. Velg enheten din, og deretter **Companion**-firmwaren for **Bluetooth** (eller
   USB, hvis du bare skal bruke den med kabel til en datamaskin).
4. Flash. Noen kort må først settes i oppdateringsmodus. Flasheren forteller deg
   hvordan.

Bruk bare *erase* når du vil starte helt på nytt. Sletting fjerner enhetens identitet
og kontaktene dine. Ved senere oppdateringer flasher du uten å slette. Skal du beholde
identiteten gjennom en sletting, eksporterer du først companionens private nøkkel fra appen
og importerer den etterpå.

## 3. Installer appen {#app}

Den offisielle MeshCore-appen finnes for Android, iOS, Windows og macOS.
På [meshcore.io](https://meshcore.io) finner du lenker til alle versjonene. Det finnes også en
nettapp på [app.meshcore.nz](https://app.meshcore.nz) som kjører i Chrome eller
Edge på en datamaskin.

## 4. Par noden din {#pair}

Slå på noden, åpne appen og koble til noden over Bluetooth. Når appen
ber om en PIN-kode:

- en node **med** skjerm viser en PIN-kode, og den skriver du inn;
- en node **uten** skjerm bruker `123456`.

Hvis paringen mislykkes, fjerner du enheten fra Bluetooth-innstillingene på telefonen og
prøver igjen. Gi deretter noden et navn. Andre ser dette navnet. Bruk derfor ikke
fullt navn eller adresse med mindre du ønsker det.

## 5. Velg radioforhåndsvalget for området ditt {#preset}

Alle radioer i et område bruker samme frekvens og innstillinger. Ellers hører de ikke
hverandre. I radioinnstillingene i appen velger du forhåndsvalget området ditt bruker.
Utenfor områdene nedenfor bruker Europa **EU/UK (Narrow)**. Nederland,
Tsjekkia, Ungarn, Slovakia, Portugal og Sveits har egne forhåndsvalg, og
Limburg i Nederland har en variant:

{{< presets >}}

Tilbyr ikke enheten din forhåndsvalget for området ditt? Da skriver du inn de 4 verdiene fra
tabellen manuelt i radioinnstillingene i appen: frekvens, båndbredde, spreading
factor og coding rate. En node med andre verdier hører ikke meshen.

Usikker? Den [lokale gruppen din](/community/) vet hvilket forhåndsvalg området ditt bruker.
Appen henter denne listen fra MeshCore-prosjektet. Et nytt forhåndsvalg krever
derfor ingen oppdatering av appen.

## 6. Si hei {#hello}

1. **Presenter deg.** Send en *advert* fra appen. En «flood»-advert
   går gjennom repeaterne (noder som sender meldinger videre), slik at alle
   på meshen kan legge deg til.
   En companion sender aldri advert av seg selv.
2. **Finn andre.** Folk dukker opp i kontaktene dine når advertene deres når
   deg. Repeatere sender som standard en flood-advert hver 47. time. Det kan derfor
   ta 2 dager før listen fylles opp.
3. **Send en melding.** Åpne en kontakt og skriv. Den første meldingen sendes som flood
   gjennom nettverket. Mottakeren melder tilbake ruten meldingen tok, og senere
   meldinger følger den ruten.
4. **Bli med i kanaler.** Kanalen **Public** er allerede satt opp. Alt du
   skriver der, når alle på meshen. Legg til regionens *hashtag-kanal*
   (et navn som begynner med `#`) ved å skrive inn navnet. Den
   [lokale gruppen din](/community/) forteller deg hvilke kanaler som er aktive.

## Når noe ikke fungerer {#troubleshooting}

**Appen finner ikke enheten min over Bluetooth.**
Sannsynligvis har du flashet USB-companionen. Flash på nytt og velg
Bluetooth-versjonen. På Heltec V3 har den lille innebygde Bluetooth-antennen
kort rekkevidde. Hold telefonen i nærheten.

**Paringen mislykkes hele tiden.**
Fjern enheten fra Bluetooth-innstillingene på telefonen, start Bluetooth på nytt
og par igjen med PIN-koden på skjermen eller `123456`.

**Ingen dukker opp i kontaktene mine.**
Sjekk at forhåndsvalget ditt stemmer med området ditt. Send en flood-advert. Er det ingen
repeater innen rekkevidde, hører du bare radioer i nærheten.
[Kartsiden](/map/) viser hvor repeaterne står.

**En kontakt vises som «sist sett» for flere dager siden, selv om personen er aktiv.**
En av de to nodene har feil klokkeslett. En companion henter klokkeslettet fra
telefonen din. Eieren av en repeater eller en room server (en node som lagrer meldinger for en
gruppe) må stille klokken på den selv.

**En direktemelding kommer aldri fram.**
Du og den andre må ha hverandre som kontakt. En node forkaster en melding fra noen
den ikke kjenner, uten å si fra til avsenderen. Send en flood-advert og be
den andre personen sende en også. Sjekk i appen at den legger til nye
kontakter automatisk. Den legger bare til noder innenfor hoppgrensen sin.

**Gamle kontakter fungerer, nye får aldri kontakt.**
En første melding sendes som flood, og en repeater sender den bare videre når den har
meldingens region. Senere meldinger følger en innlært rute, som ingen regionsjekk
stopper. Spør den [lokale gruppen din](/community/) hvilke regioner repeaterne
rundt deg har, og sjekk [innstillingene for området ditt](/guides/settings/#traffic).

**Appen får ikke lenger kontakt med companionen din.**
Noen kort har en brukerknapp, for eksempel noen RAK-kort og Heltec T114.
Hold den inne de første 8 sekundene etter at kortet starter. Companionen åpner
da en redningskonsoll over USB. I konsollen på
[flasher.meshcore.io](https://flasher.meshcore.io) setter `set pin <pin>` en
ny Bluetooth-PIN, og `erase` sletter enheten.

**Flasheren får ikke åpnet serieporten på Linux.**
Brukeren din trenger tilgang til porten, for eksempel med
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, eller medlemskap i gruppen `dialout`.

**Noe annet.**
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
dekker mange flere problemer.
