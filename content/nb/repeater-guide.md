---
title: Repeater-guide
lead: En repeater som står høyt sender meldinger videre for alle rundt seg, over en hel by eller dal. Velg et sted, driv den med sol, sett den opp, og hold deg innenfor loven.
description: 'Planlegg, driv, konfigurer og bruk en MeshCore-repeater lovlig i Europa: valg av sted, dimensjonering av solceller, CLI-innstillinger, grenser for sendeeffekt og duty cycle på 868 MHz.'
eyebrow: 868 MHz · inntil 500 mW · lisensfritt
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '4a0fe39f'
  seeded: '2026-10-26'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['1de4a4f7', '766086be', '70faf508', '8bc641aa', '2018aa04', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
---

Repeatere bærer meshet. Companions, radioene du sender meldinger fra, sender ikke meldinger videre. Uten repeatere når du derfor bare folk innenfor direkte rekkevidde. Hver repeater du setter opp utvider meshet for alle rundt den. Denne guiden følger MeshCore firmware v1.18.0.

Snakk med din [lokale gruppe](/community/) før du begynner. De vet hvor dekningen mangler, hvilken [forhåndsinnstilling området ditt bruker](/guides/settings/) og hvordan repeatere skal navngis. Sjekk [dekningskartene](/map/) for repeatere i nærheten, og si hei i de offentlige eller lokale [kanalene](/guides/channels/).

## Velg et sted {#site}

Høyde slår effekt. LoRa på 868 MHz går best langs en fri siktlinje. Åser, bygninger og tett skog koster langt mer rekkevidde enn noen ekstra milliwatt vinner tilbake.

- **Gå høyt.** Et tak, en mast, en høy bygning eller en ås dekker langt mer enn en vinduskarm. Selv noen få meter over takene rundt hjelper.
- **Hold antennen fri.** Monter den over takkanter, unna metall, takrenner og andre antenner.
- **Sjekk utsikten.** Verktøy som [HeyWhatsThat](https://www.heywhatsthat.com/) viser hva du kan se fra et sted. Kan du se et punkt, er en repeater der innen rekkevidde.
- **Gi plass rundt siktlinjen.** En radiosti trenger fritt rom rundt den direkte linjen, ikke bare selve linjen. Over lange avstander bør midten av stien gå flere meter klar av hindringer.
- **Be om lov.** Få eierens samtykke til å bruke taket eller masten, og avtal hvordan du kommer til repeateren for vedlikehold.

## Maskinvare {#hardware}

- **Kort.** Velg et nRF52-kort med lavt forbruk, som [Heltec T114](/devices/), RAK WisBlock eller SenseCAP Solar Node. ESP32-kort trekker mer strøm (enhetssiden merker dem som Høy), og det gjør soldrift vanskelig.
- **Antenne.** Bruk en antenne laget for 868 MHz, montert vertikalt. [Antenneguiden](/guides/antenna/) dekker typer, kontakter, kabel og montering. Antenneforsterkningen teller med i den lovlige effektgrensen, se [Lovlige grenser](#legal).
- **Kabel.** Hold koaksialkabelen kort, eller bruk kabel med lavt tap. På 868 MHz kan noen meter tynn kabel spise halve effekten din.
- **Kapsling.** En værbestandig boks (IP65 eller bedre) med kabelgjennomføring, et lufte- eller dreneringshull mot kondens, og lys farge eller solskjerm. Batterier lider i varme og kan ikke lades under frysepunktet.
- **Lyn.** En antenne på et tak er et mål. Følg lokale regler for jording, eller monter den der et nedslag ikke når bygningens ledningsnett.

## Strøm og dimensjonering av solceller {#power}

En solcelledrevet repeater må overleve de mørkeste ukene om vinteren. Dimensjoner den for dem:

1. **Mål forbruket.** Kjør den ferdig konfigurerte repeateren gjennom en USB-effektmåler i ett døgn. Les av energien som er brukt i wattimer (Wh). Trafikken i området ditt påvirker tallet, så mål på stedet om du kan.
2. **Legg til reserve.** Planlegg batterikapasitet for minst 5 til 7 dager uten nyttig sol.
3. **Finn vintersolen din.** EUs gratis [PVGIS-verktøy](https://re.jrc.ec.europa.eu/pvg_tools/en/) viser hvor mye energi et panel produserer per måned på et hvilket som helst sted. Bruk måneden med minst sol.
4. **Dimensjoner panelet.** Panelet må erstatte hver dags forbruk i den verste måneden, med rom for ladetap.

Et regneeksempel med antatte tall: en repeater som bruker 1 Wh per dag trenger et batteri på minst 7 Wh for en ukes reserve, omtrent 2 Ah brukbar kapasitet ved 3,7 V. Sier PVGIS at et 1 W-panel på stedet ditt gir 0,5 Wh per dag i desember, trenger du minst et 2 W-panel. 3 til 5 W gir margin for skyer, snø og aldring.

## Sett den opp {#config}

**Flash.** Bruk [web-flasheren](https://flasher.meshcore.io) og velg **Repeater**-firmwaren for kortet ditt. Se [Kom i gang](/get-started/#flash) for trinnene i flashingen.

**Konfigurer over USB.** Mens repeateren fortsatt er koblet til datamaskinen, åpner du [config.meshcore.io](https://config.meshcore.io) eller konsollen i flasheren. Du kan også bruke en hvilken som helst seriell terminal på 115200 baud. De viktigste kommandoene:

| Hva | Kommando |
|---|---|
| Endre admin-passordet | `password <new password>` |
| Gi den et navn | `set name <name>` |
| Radioforhåndsinnstilling: frekvens, båndbredde, SF, CR (start på nytt for å ta i bruk) | `set radio 869.618,62.5,8,8` |
| Grense for duty cycle, i prosent | `set dutycycle 10` |
| Sendeeffekt fra radiobrikken, i dBm | `set tx <dBm>` |
| Posisjon, slik at den vises på kart | `set lat <degrees>` og `set lon <degrees>` |
| Kontaktinformasjon for andre operatører | `set owner.info <text>` |
| Timer mellom flood-adverts, de som hele meshet hører | `set flood.advert.interval <hours>` |
| Kunngjør den nå | `advert` |
| Start på nytt | `reboot` |

Standard admin-passord er `password`, og alle som logger inn med det blir admin. Endre det før repeateren går på lufta.

Eksempelet med `set radio` over er EU/UK (Narrow). Bruk verdiene fra forhåndsinnstillingen for ditt område i stedet: [Anbefalte innstillinger](/guides/settings/) lister dem per land.

**Still klokka.** Uten en klokkemodul (RTC) mister en repeater tiden ved hvert strømbrudd og starter opp igjen i mai 2024. Mens den kjører, driver klokka. Logg inn eksternt fra appen og bruk `clock sync`, eller still tiden over USB. En RTC-modul er et nyttig tillegg for en repeater: den holder tiden gjennom strømbrudd og driver langt mindre.

**Administrer den eksternt.** Når den er på meshet, logger du inn fra MeshCore-appen med admin-passordet. Der leser du statusen og bruker de samme kommandoene over radio. Noen kommandoer virker bare over USB, som `set freq` og fabrikktilbakestillingen `erase`.

Den fulle kommandolisten finner du i [MeshCore CLI-referansen](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Lovlige grenser {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
MeshCores europeiske forhåndsinnstillinger ligger i delbåndet **869.40-869.65 MHz**. I EU, Storbritannia, Sveits og Norge er det åpent for kortdistanseutstyr uten lisens, innenfor disse grensene:

- høyst **500 mW e.r.p.** utstrålt effekt;
- høyst **10 % duty cycle**: ikke mer enn 360 sekunder sending i løpet av en time, per enhet. Alternativt kan en enhet bruke lytt-før-send med adaptiv frekvensagilitet slik ETSI EN 300 220-2 definerer det;
- hele signalet, høyst 250 kHz bredt, må holde seg innenfor delbåndet.

Båndet er delt: du må ikke forstyrre lisensierte tjenester, og andre kan forstyrre deg.
Radioen må være CE-merket (i Storbritannia, CE eller UKCA).
{{< /callout >}}

Kilder: [CEPT ERC-rekommandasjon 70-03](https://docdb.cept.org/document/845),
vedlegg 1, bånd h1.7;
[Kommisjonsbeslutning 2006/771/EF](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
med endringer;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
bånd O.

### Effekt: e.r.p. og antennen din {#erp}

Grensen gjelder den *utstrålte* effekten, målt mot en enkel dipolantenne (e.r.p.). Antenneforsterkning teller med; kabeltap trekkes fra. Produsenter oppgir antenneforsterkning i dBi, som er 2.15 dB mer enn samme forsterkning i dBd (relativt til en dipol). Hold denne summen på eller under 27 dBm (500 mW):

> sendeeffekt (dBm) + antenneforsterkning (dBi) − kabeltap (dB) − 2.15 ≤ 27

- Et kort som sender 22 dBm inn i en 5 dBi-antenne gjennom 1 dB kabel:
  22 + 5 − 1 − 2.15 = 23.85 dBm, omtrent 240 mW e.r.p. Innenfor grensen.
- Et kort med en 30 dBm (1 W) forsterker inn i en 3 dBi-antenne:
  30 + 3 − 2.15 = 30.85 dBm, omtrent 1.2 W e.r.p. Over grensen; senk sendeeffekten.

`set tx` setter utgangseffekten fra LoRa-brikken, i dBm. Selve SX1262-brikken stopper på 22 dBm; firmwaren sjekker ikke tallet du skriver inn. Kort med en ekstra forsterker, som Heltec V4 eller Station G2, sender langt mer enn tallet du setter. Sjekk produsentens tabell før du setter det, og start lavt.

### Duty cycle {#duty-cycle}

En repeater sender for alle rundt seg, så den bruker opp sendetiden sin raskere enn en companion. MeshCores duty cycle-begrenser står som standard på 50 %, og det er over det dette båndet tillater. Sett den til 10 % på hver repeater:

```text
set dutycycle 10
```

### Frekvensnøyaktighet {#frequency}

Kanalen EU/UK (Narrow), 869.618 MHz med 62.5 kHz båndbredde, strekker seg opp til 869.649 MHz: under 1 kHz fra toppen av delbåndet. Signalet må holde seg innenfor båndet ved alle temperaturer. Det krever en temperaturkompensert krystall (TCXO). Nesten alle nyere kort har en; eldre kort uten, som Heltec V2, driver for mye til å virke pålitelig ved 62.5 kHz.

### Merknader per land {#countries}

- **EU-medlemsland** må gjøre dette delbåndet tilgjengelig på disse vilkårene (vedtak 2006/771/EF, artikkel 3).
- **Storbritannia:** de samme grensene, i Ofcoms [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Sveits og Liechtenstein:** de samme grensene, i OFCOMs [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norge:** de samme grensene, i [forskrift om generelle tillatelser](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Disse merknadene er ikke juridisk rådgivning. Regler endrer seg. Er du i tvil, sjekk med den nasjonale myndigheten din.

## Sjekkliste for utplassering {#checklist}

- [ ] Eieren av stedet har sagt ja, og du kommer til repeateren for vedlikehold.
- [ ] Kortet kjører **Repeater**-firmwaren, og antennen var koblet til før første oppstart.
- [ ] Admin-passordet er endret.
- [ ] Radioen stemmer med [forhåndsinnstillingen for ditt område](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` er satt.
- [ ] Sendeeffekt pluss antenneforsterkning holder seg innenfor 500 mW e.r.p.
- [ ] Navn, posisjon og `owner.info` er satt, så andre vet hvem som driver den.
- [ ] Klokka er stilt (`clock`).
- [ ] Kapslingen er tett, med drenerings- eller luftehull, og kabelen har en dryppsløyfe.
- [ ] Batteri og panel er dimensjonert for den verste vintermåneden.
- [ ] Du testet den på avstand med appen før du forlot stedet.
- [ ] Den lokale gruppen din vet at den er oppe.
