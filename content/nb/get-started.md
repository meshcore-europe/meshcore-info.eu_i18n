---
title: Kom i gang
lead: Fra et nytt kort til din første melding på meshen. Du trenger et LoRa-kort, en datamaskin med Chrome eller Edge, og en telefon eller bærbar til appen.
description: Flash MeshCore fra nettleseren, par appen, velg radioforvalget området ditt bruker, send din første melding og bli med i din lokale kanal.
eyebrow: 6 trinn · MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '68c89544'
  seeded: '2026-10-26'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', '36a3eba3', '6da9fd7a', 'cb5fb72e', '89626504', 'a419ce79', 'aa273b20']
---

Disse trinnene følger MeshCore firmware v1.18.0 og de offisielle verktøyene fra
oktober 2026. Menynavn i appen kan variere litt mellom versjoner.

## 1. Velg en enhet {#device}

Alle kort på [enhetssiden](/devices/) som er merket companion fungerer. Til
din første node velger du en *companion*: radioen du sender meldinger fra. Du
parer den med telefonen eller den bærbare over Bluetooth eller USB, eller du
velger en med egen skjerm og eget tastatur som klarer seg selv.

Kjøp 868 MHz-versjonen. Antennen som følger med gjør jobben, og
[antenneguiden](/guides/antenna/) viser hvordan du sjekker en.

{{< callout type="warning" >}}
Sett på antennen før du slår på radioen. En LoRa-radio som sender uten
antenne kan ødelegge sin egen brikke.
{{< /callout >}}

## 2. Flash firmwaren {#flash}

1. Koble enheten til datamaskinen med en USB-datakabel.
2. Åpne web-flasheren på [flasher.meshcore.io](https://flasher.meshcore.io)
   i Chrome eller Edge. Den bruker Web Serial, som andre nettlesere mangler.
3. Velg enheten din, deretter **Companion**-firmwaren for **Bluetooth** (eller
   USB, hvis du bare skal bruke den med kabel til en datamaskin).
4. Flash. Noen kort må først settes i oppdateringsmodus; flasheren forklarer
   hvordan.

Bruk *erase* bare når du vil starte helt på nytt: sletting fjerner enhetens
identitet og kontaktene dine. Ved senere oppdateringer flasher du uten å slette.

## 3. Installer appen {#app}

Den offisielle MeshCore-appen finnes for Android, iOS, Windows og macOS;
[meshcore.io](https://meshcore.io) lenker til alle versjonene. Det finnes også en
nettapp på [app.meshcore.nz](https://app.meshcore.nz) som kjører i Chrome eller
Edge på en datamaskin.

## 4. Par noden din {#pair}

Slå på noden, åpne appen og koble til den over Bluetooth. Når du blir bedt om
en PIN-kode:

- en node **med** skjerm viser en PIN-kode; skriv inn den;
- en node **uten** skjerm bruker `123456`.

Hvis paringen mislykkes, fjerner du enheten fra Bluetooth-innstillingene på
telefonen og prøver igjen. Gi deretter noden et navn. Andre ser dette navnet,
så ikke bruk fullt navn eller adresse med mindre du vil det.

## 5. Velg radioforvalget for området ditt {#preset}

Alle radioer i et område bruker samme frekvens og innstillinger, ellers hører
de ikke hverandre. I radioinnstillingene i appen velger du forvalget området
ditt bruker. Utenfor områdene nedenfor bruker Europa **EU/UK (Narrow)**.
Nederland, Tsjekkia, Ungarn, Slovakia, Portugal og Sveits bruker sine egne, og
Limburg i Nederland har en variant:

{{< presets >}}

Usikker? Din [lokale gruppe](/community/) vet hvilket forvalg området ditt
bruker. Appen laster ned denne listen fra MeshCore-prosjektet, så et nytt
forvalg krever ingen appoppdatering.

## 6. Si hei {#hello}

1. **Gjør deg kjent.** Send en *advert* fra appen. En «flood»-advert går
   gjennom repeaterne (noder som sender meldinger videre), slik at alle på
   meshen kan legge deg til.
   Companions annonserer seg aldri automatisk.
2. **Finn andre.** Folk dukker opp i kontaktene dine når advertene deres når
   deg. Repeatere sender en flood-advert hver 47. time som standard, så listen
   din kan trenge 2 dager på å fylle seg.
3. **Send en melding.** Åpne en kontakt og skriv. Den første meldingen floodes
   gjennom nettverket; mottakeren melder tilbake hvilken rute den tok, og
   senere meldinger følger den ruten.
4. **Bli med i kanaler.** Kanalen **Public** er allerede satt opp; alt du
   skriver der når alle på meshen. Legg til regionens *hashtag-kanal* (et navn
   som starter med `#`) ved å skrive inn navnet. Din
   [lokale gruppe](/community/) forteller deg hvilke kanaler som er aktive.

## Når noe ikke fungerer {#troubleshooting}

**Appen finner ikke enheten min over Bluetooth.**
Du har sannsynligvis flashet USB-companionen. Flash på nytt og velg
Bluetooth-versjonen. På Heltec V3 har den lille innebygde Bluetooth-antennen
kort rekkevidde; hold telefonen nær.

**Paringen mislykkes gang på gang.**
Fjern enheten fra Bluetooth-innstillingene på telefonen, start Bluetooth på
nytt, og par igjen med PIN-koden på skjermen eller `123456`.

**Ingen dukker opp i kontaktene mine.**
Sjekk at forvalget ditt stemmer med området ditt. Send en flood-advert. Hvis
ingen repeater er innen rekkevidde, hører du bare radioer i nærheten;
[kartsiden](/map/) viser hvor repeaterne står.

**En kontakt viser «sist sett» for flere dager siden selv om de er aktive.**
En av de to nodene har feil klokke. En companion henter tiden fra telefonen
din; repeatere og romservere (noder som lagrer meldinger for en gruppe) må få
tiden satt av eieren sin.

**Flasheren får ikke åpnet serieporten på Linux.**
Brukeren din trenger tilgang til porten, for eksempel med
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, eller medlemskap i gruppen
`dialout`.

**Noe annet.**
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
dekker mange flere problemer.
