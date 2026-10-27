---
title: Repeater-guide
lead: En repeater placeret højt sender beskeder videre for alle omkring den, på tværs af en hel by eller dal. Vælg et sted, driv den med solenergi, sæt den op, og hold dig inden for loven.
description: 'Planlæg, forsyn, konfigurer og driv lovligt en MeshCore-repeater i Europa: valg af sted, dimensionering af solceller, CLI-indstillinger, sendeeffekt og duty cycle-grænser på 868 MHz.'
eyebrow: 868 MHz · op til 500 mW · licensfri
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '4a0fe39f'
  seeded: '2026-10-26'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['1de4a4f7', '766086be', '70faf508', '8bc641aa', '2018aa04', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
---

Repeatere bærer meshet. Companions, de radioer du sender beskeder fra, sender ikke beskeder videre. Uden repeatere når du derfor kun de folk, der er i direkte rækkevidde. Hver repeater, du sætter op, udvider meshet for alle omkring den. Denne guide følger MeshCore firmware v1.18.0.

Tal med din [lokale gruppe](/community/), før du går i gang. De ved, hvor der mangler dækning, hvilken [preset dit område bruger](/guides/settings/), og hvordan repeatere navngives. Tjek [dækningskortene](/map/) for repeatere i nærheden af dig, og sig hej på de offentlige eller lokale [kanaler](/guides/channels/).

## Vælg et sted {#site}

Højde slår effekt. LoRa på 868 MHz rækker bedst langs en fri sigtelinje. Bakker, bygninger og tæt bevoksning koster langt mere rækkevidde, end et par ekstra milliwatt vinder tilbage.

- **Kom højt op.** Et tag, en mast, en høj bygning eller en bakke dækker langt mere end en vindueskarm. Selv få meter over de omkringliggende tage hjælper.
- **Hold antennen fri.** Monter den over tagkanter, væk fra metal, tagrender og andre antenner.
- **Tjek udsigten.** Værktøjer som [HeyWhatsThat](https://www.heywhatsthat.com/) viser, hvad man kan se fra et sted. Hvis du kan se et sted, er en repeater der inden for rækkevidde.
- **Giv plads.** En radiosti har brug for noget fri plads omkring den direkte linje, ikke kun selve linjen. Over lange afstande bør midten af stien gå fri af forhindringer med flere meter.
- **Spørg om lov.** Få ejerens tilladelse til taget eller masten, og aftal, hvordan du kan komme til repeateren for vedligehold.

## Hardware {#hardware}

- **Board.** Vælg et strømbesparende nRF52-board som [Heltec T114](/devices/), RAK WisBlock eller SenseCAP Solar Node. ESP32-boards bruger mere strøm (enhedssiden markerer dem som High), og det gør soldrift svær.
- **Antenne.** Brug en antenne lavet til 868 MHz, monteret lodret. [Antenne-guiden](/guides/antenna/) gennemgår typer, stik, kabel og montering. Antennens forstærkning tæller med i den lovlige effektgrænse, se [Lovlige grænser](#legal).
- **Kabel.** Hold koaksialkablet kort, eller brug kabel med lavt tab. På 868 MHz kan få meter tyndt kabel tabe halvdelen af din effekt.
- **Kabinet.** En vejrbestandig boks (IP65 eller bedre) med kabelgennemføring, et ventilations- eller drænhul mod kondens og en lys farve eller solafskærmning. Batterier lider under varme og kan ikke lades under frysepunktet.
- **Lyn.** En antenne på et tag er et mål. Følg de lokale regler for jording, eller monter den, hvor et lynnedslag ikke når bygningens ledningsnet.

## Strøm og dimensionering af solceller {#power}

En solcelledrevet repeater skal overleve vinterens mørkeste uger. Dimensioner den til dem:

1. **Mål forbruget.** Kør den konfigurerede repeater gennem en USB-effektmåler i et døgn. Aflæs det brugte energiforbrug i watt-timer (Wh). Trafikken i dit område ændrer tallet, så mål på stedet, hvis du kan.
2. **Læg reserve til.** Planlæg batterikapacitet til mindst 5 til 7 dage uden brugbar sol.
3. **Find din vintersol.** EU's gratis [PVGIS-værktøj](https://re.jrc.ec.europa.eu/pvg_tools/en/) viser for ethvert sted, hvor meget energi et panel producerer per måned. Brug måneden med mindst sol.
4. **Dimensioner panelet.** Panelet skal erstatte hver dags forbrug i den værste måned, med plads til ladetab.

Et regneeksempel med antagne tal: en repeater, der bruger 1 Wh om dagen, har brug for et batteri på mindst 7 Wh til en uges reserve, omkring 2 Ah brugbar kapacitet ved 3,7 V. Hvis PVGIS siger, at et 1 W panel på dit sted giver 0,5 Wh om dagen i december, skal du bruge mindst et 2 W panel, og 3 til 5 W giver margin til skyer, sne og ældning.

## Sæt den op {#config}

**Flash.** Brug [web-flasheren](https://flasher.meshcore.io), og vælg **Repeater**-firmwaren til dit board. Se [Kom i gang](/get-started/#flash) for trinnene til flashing.

**Konfigurer over USB.** Mens repeateren stadig er tilsluttet din computer, åbner du [config.meshcore.io](https://config.meshcore.io) eller flasherens konsol. Du kan også bruge en hvilken som helst seriel terminal på 115200 baud. De vigtigste kommandoer:

| Hvad | Kommando |
|---|---|
| Skift admin-adgangskoden | `password <new password>` |
| Giv den et navn | `set name <name>` |
| Radio-preset: frekvens, båndbredde, SF, CR (genstart for at anvende) | `set radio 869.618,62.5,8,8` |
| Duty cycle-grænse, i procent | `set dutycycle 10` |
| Radiochippens sendeeffekt, i dBm | `set tx <dBm>` |
| Position, så den vises på kort | `set lat <degrees>` og `set lon <degrees>` |
| Kontaktoplysninger til andre operatører | `set owner.info <text>` |
| Timer mellem flood-adverts, dem hele meshet hører | `set flood.advert.interval <hours>` |
| Annoncer den nu | `advert` |
| Genstart | `reboot` |

Standard-adgangskoden for admin er `password`, og enhver, der logger ind med den, bliver admin. Skift den, før repeateren går i luften.

Eksemplet med `set radio` ovenfor er EU/UK (Narrow). Brug i stedet værdierne fra dit områdes preset: [Anbefalede indstillinger](/guides/settings/) lister dem per land.

**Sæt uret.** Uden et urmodul (RTC) mister en repeater tiden ved hvert strømsvigt og genstarter i maj 2024, og mens den kører, driver dens ur. Log ind eksternt fra appen, og brug `clock sync`, eller sæt tiden over USB. Et RTC-modul er et nyttigt tilbehør til en repeater: det holder tiden gennem strømsvigt og driver langt mindre.

**Administrer den eksternt.** Når den er på meshet, logger du ind fra MeshCore-appen med admin-adgangskoden. Der aflæser du dens status og bruger de samme kommandoer over radioen. Nogle kommandoer virker kun over USB, for eksempel `set freq` og fabriksnulstillingen `erase`.

Den fulde liste over kommandoer findes i [MeshCore CLI-referencen](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Lovlige grænser {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
MeshCores europæiske presets ligger i delbåndet **869.40-869.65 MHz**. I EU, Storbritannien, Schweiz og Norge er det åbent for kortrækkende udstyr uden licens, inden for disse grænser:

- højst **500 mW e.r.p.** udstrålet effekt;
- højst **10% duty cycle**: ikke mere end 360 sekunders sending i en hvilken som helst time, per enhed. Alternativt må en enhed bruge listen-before-talk med adaptiv frekvensagilitet som defineret i ETSI EN 300 220-2;
- hele signalet, højst 250 kHz bredt, skal holde sig inden for delbåndet.

Båndet er delt: du må ikke forstyrre licenserede tjenester, og andre må forstyrre dig.
Radioen skal være CE-mærket (i Storbritannien CE eller UKCA).
{{< /callout >}}

Kilder: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845), bilag 1, bånd h1.7;
[Kommissionens beslutning 2006/771/EF](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) og dens ændringer;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), bånd O.

### Effekt: e.r.p. og din antenne {#erp}

Grænsen gælder den *udstrålede* effekt, målt i forhold til en simpel dipolantenne (e.r.p.). Antennens forstærkning tæller med; kabeltab trækkes fra. Producenter angiver antenneforstærkning i dBi, som er 2.15 dB mere end samme forstærkning i dBd (i forhold til en dipol). Hold denne sum på eller under 27 dBm (500 mW):

> sendeeffekt (dBm) + antenneforstærkning (dBi) − kabeltab (dB) − 2.15 ≤ 27

- Et board, der sender 22 dBm ind i en 5 dBi antenne gennem 1 dB kabel:
  22 + 5 − 1 − 2.15 = 23.85 dBm, omkring 240 mW e.r.p. Inden for grænsen.
- Et board med en 30 dBm (1 W) forstærker ind i en 3 dBi antenne:
  30 + 3 − 2.15 = 30.85 dBm, omkring 1.2 W e.r.p. Over grænsen; sænk sendeeffekten.

`set tx` sætter LoRa-chippens udgangseffekt, i dBm. SX1262-chippen selv topper ved 22 dBm; firmwaren tjekker ikke det tal, du indtaster. Boards med en ekstra forstærker, som Heltec V4 eller Station G2, sender langt mere end det tal, du sætter. Tjek producentens tabel, før du sætter det, og start lavt.

### Duty cycle {#duty-cycle}

En repeater sender for alle omkring den, så den bruger sin sendetid hurtigere end en companion. MeshCores duty cycle-begrænser står som standard på 50 %, hvilket er over, hvad dette bånd tillader. Sæt den til 10 % på hver repeater:

```text
set dutycycle 10
```

### Frekvensnøjagtighed {#frequency}

Kanalen EU/UK (Narrow), 869.618 MHz med 62.5 kHz båndbredde, rækker op til 869.649 MHz: mindre end 1 kHz under delbåndets øvre grænse. Signalet skal blive inden for båndet ved enhver temperatur. Det kræver en temperaturkompenseret krystal (TCXO). Næsten alle nuværende boards har en. Ældre boards uden, som Heltec V2, driver for langt til at virke pålideligt ved 62.5 kHz.

### Noter per land {#countries}

- **EU's medlemsstater** skal stille dette delbånd til rådighed på disse vilkår (beslutning 2006/771/EF, artikel 3).
- **Storbritannien:** de samme grænser, i Ofcoms [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Schweiz og Liechtenstein:** de samme grænser, i OFCOM's [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norge:** de samme grænser, i [forskriften om generelle tilladelser](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Disse noter er ikke juridisk rådgivning. Regler ændrer sig. Er du i tvivl, så spørg din nationale myndighed.

## Tjekliste til opsætning {#checklist}

- [ ] Ejeren af stedet har givet lov, og du kan komme til repeateren for vedligehold.
- [ ] Boardet kører **Repeater**-firmwaren, og antennen blev sat på, før den blev tændt første gang.
- [ ] Admin-adgangskoden er ændret.
- [ ] Radioen matcher [dit områdes preset](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` er sat.
- [ ] Sendeeffekt plus antenneforstærkning holder sig inden for 500 mW e.r.p.
- [ ] Navn, position og `owner.info` er sat, så andre ved, hvem der driver den.
- [ ] Uret er sat (`clock`).
- [ ] Kabinettet er tæt, med dræn- eller ventilationshul, og kablet har en drypsløjfe.
- [ ] Batteri og panel er dimensioneret til den værste vintermåned.
- [ ] Du har testet den på afstand med appen, før du forlod stedet.
- [ ] Din lokale gruppe ved, at den er oppe.
