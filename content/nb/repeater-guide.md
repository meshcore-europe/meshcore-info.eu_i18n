---
title: Repeaterguide
lead: En repeater som står høyt, sender meldinger videre for alle rundt seg, over en hel by eller dal. Velg et sted, gi den strøm fra sola, sett den opp og hold deg innenfor loven.
description: 'Planlegg, driv, konfigurer og bruk en MeshCore-repeater lovlig i Europa: valg av sted, dimensjonering av solcelleanlegg, CLI-innstillinger, effekt- og duty cycle-grenser på 868 MHz.'
eyebrow: 868 MHz · opptil 500 mW · lisensfritt
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-10-31'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Repeaterne bærer meshet. Companions, radioene du sender meldinger fra, sender ikke
meldinger videre. Uten
repeatere når du derfor bare folk innenfor direkte rekkevidde. En repeater på riktig
sted utvider meshet for alle rundt den. Denne guiden følger MeshCore
firmware v1.18.0.

Før du begynner, bør du snakke med den [lokale gruppen din](/community/). De vet hvor
dekningen mangler, hvilket [preset området ditt bruker](/guides/settings/) og hvordan repeatere skal navngis. Sjekk
[dekningskartene](/map/) for repeatere nær deg, og si hei i de offentlige
eller lokale [kanalene](/guides/channels/).

## Trenger du en? {#need}

En repeater sender videre hver flood-melding den hører. Alle repeatere innenfor
rekkevidde deler den samme sendetiden. Der meshet allerede når deg, gir én repeater til
mer trafikk og ingen ekstra dekning. En companion som står høyt, i et loftsvindu
eller på en balkong, kan være alt du trenger.

Sett opp en repeater der dekningen mangler:

- [dekningskartene](/map/) viser ingen repeater nær deg, eller bare repeatere som
  companionen din ikke hører;
- den lokale gruppen din sier at området trenger en.

## Velg et sted {#site}

Høyde slår effekt. LoRa på 868 MHz går best med fri sikt.
Åser, bygninger og tett skog koster langt mer rekkevidde enn noen få ekstra
milliwatt vinner tilbake.

- **Gå høyt.** Et tak, en mast, en høy bygning eller en ås dekker langt mer
  enn en vinduskarm. Selv noen få meter over takene rundt hjelper.
- **Hold antennen fri.** Monter den over takkantene, unna
  metall, takrenner og andre antenner.
- **Sjekk utsikten.** Verktøy som [HeyWhatsThat](https://www.heywhatsthat.com/)
  viser hva du kan se fra et sted. Kan du se et punkt, er en repeater
  der innenfor rekkevidde.
- **Sørg for klaring.** En radiosti trenger litt fri plass rundt den direkte
  linjen, ikke bare selve linjen. Over lange avstander bør midten av stien
  gå flere meter over hindringer.
- **Spør om lov.** Få eierens samtykke for taket eller masten, og avtal
  hvordan du kommer til repeateren for vedlikehold.

## Maskinvare {#hardware}

- **Kort.** Velg et nRF52-kort med lavt strømforbruk, som
  [Heltec T114](/devices/), RAK WisBlock eller SenseCAP Solar Node. ESP32-kort
  bruker mer strøm (enhetssiden merker dem med High), og det gjør
  solcelledrift vanskelig.
- **Antenne.** Bruk en antenne laget for 868 MHz, montert loddrett.
  [Antenneguiden](/guides/antenna/) tar for seg typer, kontakter, kabel og
  montering. Antenneforsterkningen teller med i den lovlige effektgrensen. Se
  [Lovlige grenser](#legal).
- **Kabel.** Hold koaksialkabelen kort, eller bruk lavtapskabel. På 868 MHz kan noen
  få meter tynn kabel koste deg halve effekten.
- **Kapsling.** Bruk en værbestandig boks (IP65 eller bedre) med kabelnippel, et
  luftehull eller dreneringshull mot kondens, og en lys farge eller solskjerm.
  Batterier tåler varme dårlig og kan ikke lades under frysepunktet.
- **Lyn.** En antenne på et tak er et mål. Følg lokale regler for
  jording, eller monter den der et nedslag ikke når det elektriske anlegget
  i bygningen.

## Strøm og dimensjonering av solcelleanlegg {#power}

En solcelledrevet repeater må klare de mørkeste vinterukene. Dimensjoner den
for dem:

1. **Mål forbruket.** Kjør den ferdig konfigurerte repeateren gjennom en USB-strømmåler
   i et døgn. Les av energiforbruket i wattimer (Wh). Trafikken i
   området ditt endrer tallet, så mål på stedet hvis du kan.
2. **Legg inn reserve.** Planlegg batterikapasitet for minst 5 til 7 dager
   uten nyttig sol.
3. **Finn vintersola di.** Med EUs gratis
   [PVGIS-verktøy](https://re.jrc.ec.europa.eu/pvg_tools/en/) ser du hvor mye energi
   et panel produserer per måned, for et hvilket som helst sted. Bruk måneden med
   minst sol.
4. **Dimensjoner panelet.** Panelet må erstatte forbruket hver dag i den verste
   måneden, med margin for ladetap.

Et regneeksempel med antatte tall: En repeater som bruker 1 Wh per dag,
trenger et batteri på minst 7 Wh for en ukes reserve. Det er omtrent 2 Ah
brukbar kapasitet ved 3,7 V. Hvis PVGIS sier at et 1 W-panel på stedet ditt gir
0,5 Wh per dag i desember, trenger du minst et 2 W-panel. Med 3 til 5 W
har du margin for skyer, snø og aldring.

## Sett den opp {#config}

**Flash.** Bruk [nettflasheren](https://flasher.meshcore.io) og velg
**Repeater**-firmwaren for kortet ditt. Se
[Kom i gang](/get-started/#flash) for stegene.

**Konfigurer over USB.** Mens repeateren fortsatt er koblet til datamaskinen,
åpner du [config.meshcore.io](https://config.meshcore.io) eller konsollen i flasheren.
Du kan også bruke en hvilken som helst seriell terminal på 115200 baud. De viktigste
kommandoene:

| Hva | Kommando |
|---|---|
| Endre admin-passordet | `password <new password>` |
| Gi den et navn | `set name <name>` |
| Radio-preset: frekvens, båndbredde, SF, CR (start på nytt for å ta i bruk) | `set radio 869.618,62.5,8,8` |
| Duty cycle-grense, i prosent | `set dutycycle 10` |
| Sendeeffekt for radiobrikken, i dBm | `set tx <dBm>` |
| Posisjon, slik at den vises på kart | `set lat <degrees>` og `set lon <degrees>` |
| Kontaktinformasjon for andre operatører | `set owner.info <text>` |
| Timer mellom flood-adverts, de som hele meshet hører | `set flood.advert.interval <hours>` |
| Annonser den nå | `advert` |
| Start på nytt | `reboot` |

Standard admin-passord er `password`, og alle som logger inn med det,
blir admin. Endre det før repeateren går på lufta.

`set radio`-eksempelet over er EU/UK (Narrow). Bruk verdiene for presetet i
området ditt i stedet: [Anbefalte innstillinger](/guides/settings/) viser dem
per land.

**Still klokka.** Uten klokkemodul (RTC) mister en repeater tiden ved
hvert strømbrudd og starter på nytt i mai 2024. Mens den går, driver klokka
også: Den går stadig mer for fort eller for sakte. Still derfor klokka av og til: Logg
inn eksternt fra appen og bruk `clock sync`, eller still tiden over USB. Med
en RTC-modul trenger du sjelden det: Den holder tiden gjennom strømbrudd og
driver langt mindre.

**Administrer den eksternt.** Når den er på meshet, logger du inn fra MeshCore-appen
med admin-passordet. Der leser du statusen og bruker de samme kommandoene
over radio. Noen kommandoer fungerer bare over USB, som `set freq` og
fabrikktilbakestillingen `erase`.

**Behold identiteten.** Før du kjører erase, skriver du `get prv.key` over USB og lagrer
den private nøkkelen som vises, på et trygt sted. Etter erase gir `set prv.key <key>`
og en `reboot` repeateren den gamle identiteten tilbake. Noder som kjenner
den, finner den da under samme prefiks.

Den fullstendige kommandolisten finner du i
[MeshCore CLI-referansen](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Oppdater den trådløst {#update}

Når repeateren står høyt oppe, oppdaterer du den fra bakken. Logg inn fra
MeshCore-appen med admin-passordet, åpne kommandolinjen og skriv
`start ota`. Hva som skjer videre, avhenger av kortet. Andre kort svarer `Error`,
og dem oppdaterer du over USB.

**nRF52-kort**, som RAK, Heltec T114, Seeed XIAO og SenseCAP Solar:

1. Last ned **ZIP**-filen med den nye firmwaren for kortet ditt fra
   [nettflasheren](https://flasher.meshcore.io).
2. Skriv `start ota`. Repeateren svarer `OK` og dukker opp over Bluetooth
   som `<board>_OTA`, for eksempel `RAK4631_OTA`.
3. Åpne appen nRF Device Firmware Update på telefonen, velg ZIP-filen og
   repeateren, og last opp. Det tar noen minutter.

Installer [OTAFIX-bootloaderen](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
på et nRF52-kort før det kommer opp. Med standard-bootloaderen kan en mislykket
oppdatering bare repareres over USB. Med OTAFIX går kortet tilbake til
oppdateringsmodus, og du prøver på nytt over Bluetooth.

**ESP32-kort**, som Heltec V3 og V4:

1. Last ned **ikke-sammenslått** `.bin` for kortet ditt fra nettflasheren:
   filen uten «merged» i navnet.
2. Skriv `start ota`. Repeateren åpner et WiFi-nettverk som heter `MeshCore-OTA`,
   og svarer med adressen til opplastingssiden sin.
3. Innenfor WiFi-rekkevidde kobler du telefonen eller den bærbare til det nettverket, åpner
   adressen og laster opp filen.

## Lovlige grenser {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
De europeiske presetene i MeshCore ligger i delbåndet **869.40-869.65 MHz**. I
EU, Storbritannia, Sveits og Norge er det åpent for kortholdsutstyr uten
lisens, innenfor disse grensene:

- høyst **500 mW e.r.p.** utstrålt effekt;
- høyst **10% duty cycle**: ikke mer enn 360 sekunder sending i
  løpet av en time, per enhet. En enhet kan i stedet bruke listen-before-talk
  med adaptive frequency agility slik det er definert i ETSI EN 300 220-2;
- hele signalet, høyst 250 kHz bredt, må holde seg innenfor delbåndet.

Båndet er delt: Du må ikke forstyrre lisensierte tjenester, og andre kan
forstyrre deg.
Radioen må være CE-merket (i Storbritannia CE eller UKCA).
{{< /callout >}}

Kilder: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
Annex 1, bånd h1.7;
[Kommisjonsbeslutning 2006/771/EF](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
med endringer;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
bånd O.

### Effekt: e.r.p. og antennen din {#erp}

Grensen gjelder den *utstrålte* effekten, målt mot en enkel dipolantenne
(e.r.p.). Antenneforsterkningen legges til, kabeltapet trekkes fra. Produsentene oppgir
antenneforsterkning i dBi, som er 2.15 dB mer enn samme forsterkning i dBd
(i forhold til en dipol). Hold denne summen på eller under 27 dBm (500 mW):

> sendeeffekt (dBm) + antenneforsterkning (dBi) − kabeltap (dB) − 2.15 ≤ 27

- Et kort som sender 22 dBm inn i en 5 dBi-antenne gjennom 1 dB kabeltap:
  22 + 5 − 1 − 2.15 = 23.85 dBm, omtrent 240 mW e.r.p. Innenfor grensen.
- Et kort med en 30 dBm (1 W) forsterker inn i en 3 dBi-antenne:
  30 + 3 − 2.15 = 30.85 dBm, omtrent 1.2 W e.r.p. Over grensen. Senk
  sendeeffekten.

`set tx` stiller utgangseffekten til LoRa-brikken, i dBm. Selve SX1262-brikken
går ikke høyere enn 22 dBm. Firmwaren sjekker ikke tallet du skriver inn. Kort med en ekstra
forsterker, som Heltec V4 eller Station G2, sender med langt mer enn
tallet du stiller inn. Sjekk tabellen fra produsenten før du stiller det inn, og
start lavt.

### Duty cycle {#duty-cycle}

En repeater sender for alle rundt seg. Den bruker derfor opp sendetiden sin raskere
enn en companion. Duty cycle-begrenseren i MeshCore står som standard på 50%, og det er
mer enn dette båndet tillater. Still den til 10% på hver repeater:

```text
set dutycycle 10
```

### Frekvensnøyaktighet {#frequency}

EU/UK (Narrow)-kanalen, 869.618 MHz med 62.5 kHz båndbredde, når opp
til 869.649 MHz: mindre enn 1 kHz under toppen av delbåndet. Signalet
må holde seg innenfor båndet ved enhver temperatur. Det krever en
temperaturkompensert krystall (TCXO). Nesten alle dagens kort har en.
Eldre kort uten, som Heltec V2, driver for langt til å fungere pålitelig
på 62.5 kHz.

### Merknader per land {#countries}

- **EUs medlemsland** må gjøre dette delbåndet tilgjengelig på disse vilkårene
  (beslutning 2006/771/EF, artikkel 3).
- **Storbritannia:** de samme grensene, i Ofcom
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Sveits og Liechtenstein:** de samme grensene, i OFCOM
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norge:** de samme grensene, i
  [forskrift om generelle tillatelser](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Disse merknadene er ikke juridisk rådgivning. Reglene endrer seg. Er du i tvil, sjekk med
den nasjonale myndigheten i landet ditt.

## Sjekkliste for utplassering {#checklist}

- [ ] Eieren av stedet har sagt ja, og du kommer til repeateren for vedlikehold.
- [ ] Kortet kjører **Repeater**-firmwaren, og antennen var koblet til
      før første oppstart.
- [ ] Admin-passordet er endret.
- [ ] Radioen samsvarer med [presetet i området ditt](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` er satt.
- [ ] Sendeeffekt pluss antenneforsterkning holder seg innenfor 500 mW e.r.p.
- [ ] Navn, posisjon og `owner.info` er satt, så andre vet hvem som driver den.
- [ ] Klokka er stilt (`clock`).
- [ ] Kapslingen er tett, med et dreneringshull eller luftehull, og kabelen har en
      dryppsløyfe.
- [ ] Batteri og panel er dimensjonert for den verste vintermåneden.
- [ ] Du har testet den på avstand med appen før du forlot stedet.
- [ ] Den lokale gruppen din vet at den er i drift.
