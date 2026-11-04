---
title: Repeater-guide
lead: En repeater højt oppe sender beskeder videre for alle omkring den, over en hel by eller dal. Find et sted, forsyn den med solenergi, sæt den op, og hold dig inden for loven.
description: 'Planlæg, forsyn, konfigurer og drift en MeshCore-repeater lovligt i Europa: valg af sted, dimensionering af solceller, CLI-indstillinger, effekt på 868 MHz og grænser for duty cycle.'
eyebrow: 868 MHz · op til 500 mW · uden licens
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '3e38a8c6'
  seeded: '2026-11-04'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '824ab38e', '662ea23c', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', 'bbea9a0c', '2b9fab3b', 'b13d1947', 'c2bad16f', '636edc86', 'c2d6bcd1', '957ae975', '98874949', '96d1ebad', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Repeatere bærer meshet. Companions, de radioer du skriver beskeder fra, sender ikke beskeder videre. Uden repeatere når du derfor kun folk inden for direkte rækkevidde. En repeater på det rigtige sted udvider meshet for alle omkring den. Denne guide følger MeshCore-firmware v1.18.0.

Tal med din [lokale gruppe](/community/), før du går i gang. De ved, hvor dækningen mangler, [hvilket preset der bruges i dit område](/guides/settings/), og hvordan repeatere skal navngives. Se på [dækningskortene](/map/), om der er repeatere nær dig, og sig hej på de offentlige eller lokale [kanaler](/guides/channels/).

## Har du brug for en? {#need}

En repeater sender alle flood-beskeder videre, som den hører, og alle repeatere inden for rækkevidde deler den samme sendetid. Hvor meshet allerede når dig, giver endnu en repeater mere trafik, ikke mere dækning. En companion placeret højt, i et loftsvindue eller på en altan, kan være alt, du behøver.

Sæt en repeater op, hvor dækningen mangler:

- [dækningskortene](/map/) viser ingen repeater nær dig, eller kun nogle, din companion ikke hører;
- din lokale gruppe siger, at området har brug for en.

## Vælg et sted {#site}

Højde slår effekt. LoRa på 868 MHz når længst med frit udsyn. Bakker, bygninger og tætte træer koster langt mere rækkevidde, end nogle få ekstra milliwatt henter ind igen.

- **Gå højt op.** Et tag, en mast, en høj bygning eller en bakke dækker langt mere end en vindueskarm. Selv nogle få meter over de omkringliggende tage hjælper.
- **Hold antennen fri.** Monter den over tagkanterne, væk fra metal, tagrender og andre antenner.
- **Tjek udsynet.** Værktøjer som [HeyWhatsThat](https://www.heywhatsthat.com/) viser, hvad man kan se fra et sted. MeshCore-appen [beregner, hvad en repeater dér kan nå](#check-site).
- **Sørg for frirum.** En radiosti kræver fri plads omkring den direkte linje, ikke kun selve linjen. Ved 868 MHz er den plads cirka 20 m omkring midten af en sti på 5 km. På 20 km er den cirka 40 m.
- **Spørg om lov.** Få ejerens samtykke til taget eller masten, og aftal, hvordan du kommer til repeateren for at vedligeholde den.

### Tjek et sted i appen {#check-site}

Version 1.33 eller nyere af MeshCore-appen har disse værktøjer under **Tools** i
menuen. De virker uden tilsluttet radio.

- **Line of Sight** tegner terrænet mellem 2 punkter og den plads over det, som
  signalet har brug for. Tryk længe på 2 punkter på kortet, eller tryk på repeatere.
- **Antenna Coverage** viser på kortet, hvad en antenne i 1 punkt kan nå.
  Tryk længe på et punkt, eller tryk på en repeater. Tilføj flere punkter for at
  sammenligne steder.

På en computer vælger du **Add Point** i værktøjets menu og skriver koordinaterne.

Begge værktøjer starter med antennen på dit sted i 5 m højde, så indstil den højde, du
planlægger, i værktøjets indstillinger. Antenna Coverage starter med en modtageantenne
i 1 m højde. Uden en tilsluttet radio starter Line of Sight på 915 MHz: indstil
frekvensen for din [forudindstilling](/guides/settings/) i værktøjets indstillinger.

Værktøjerne regner ud fra højdedata og tester ikke din radio. Tjek selv træer og
nye bygninger, og tag så en companion med ud på stedet og se, hvilke
repeatere den hører.

![Line of Sight i MeshCore-appen: terrænet mellem 2 punkter og den plads over det, som signalet har brug for](/media/guides/line-of-sight.webp)

![Antenna Coverage i MeshCore-appen: det område, en antenne på en bakke kan nå, vist på et kort](/media/guides/antenna-coverage.webp)

## Hardware {#hardware}

- **Board.** Vælg et strømbesparende nRF52-board som [Heltec T114](/devices/), RAK WisBlock eller SenseCAP Solar Node. ESP32-boards bruger mere strøm (på enhedssiden står de som High), og det gør drift på solenergi svær.
- **Antenne.** Brug en antenne lavet til 868 MHz, og montér den lodret. I [antenneguiden](/guides/antenna/) kan du læse om typer, stik, kabel og montering. Antennens forstærkning tæller med i den lovlige effektgrænse: se [Lovlige grænser](#legal).
- **Kabel.** Hold koaksialkablet kort, eller brug kabel med lavt tab. På 868 MHz kan nogle få meter tyndt kabel koste halvdelen af din effekt.
- **Kabinet.** En vejrbestandig kasse (IP65 eller bedre) med kabelforskruning, et udluftnings- eller drænhul mod kondens og en lys farve eller solskærm. Batterier tager skade af varme, og du kan ikke oplade dem under frysepunktet.
- **Lyn.** En antenne på et tag er et mål for lynet. Følg de lokale regler for jording, eller montér antennen, hvor et nedslag ikke når bygningens el-installation.

## Strøm og dimensionering af solceller {#power}

En repeater på solenergi skal klare vinterens mørkeste uger. Dimensionér den efter dem:

1. **Mål forbruget.** Kør den konfigurerede repeater gennem en USB-strømmåler i et døgn. Aflæs energiforbruget i watttimer (Wh). Trafikken i dit område påvirker tallet, så mål på stedet, hvis du kan.
2. **Læg en reserve oveni.** Planlæg batterikapacitet til mindst 5 til 7 dage uden brugbar sol.
3. **Find din vintersol.** EU's gratis [PVGIS-værktøj](https://re.jrc.ec.europa.eu/pvg_tools/en/) viser for ethvert sted, hvor meget energi et panel producerer pr. måned. Brug måneden med mindst sol.
4. **Dimensionér panelet.** Panelet skal dække hver dags forbrug i den værste måned, med plads til ladetab.

Et regneeksempel med antagede tal: en repeater, der bruger 1 Wh pr. dag, kræver et batteri på mindst 7 Wh til en uges reserve. Det svarer til omkring 2 Ah brugbar kapacitet ved 3.7 V. Hvis PVGIS siger, at et panel på 1 W på dit sted giver 0.5 Wh pr. dag i december, skal du bruge et panel på mindst 2 W. Med 3 til 5 W har du margin til skyer, sne og ældning.

## Sæt den op {#config}

**Flash.** Brug [web-flasheren](https://flasher.meshcore.io), og vælg **Repeater**-firmwaren til dit board. I
[Kom i gang](/get-started/#flash) kan du se, hvordan du flasher.

**Konfigurér via USB.** Lad repeateren være tilsluttet din computer, og åbn
[config.meshcore.io](https://config.meshcore.io) eller flasherens konsol. Du kan også bruge en hvilken som helst seriel terminal ved 115200 baud. De vigtigste kommandoer:

| Hvad | Kommando |
|---|---|
| Skift admin-adgangskoden | `password <new password>` |
| Giv den et navn | `set name <name>` |
| Radiopreset: frekvens, båndbredde, SF, CR (genstart for at aktivere det) | `set radio 869.618,62.5,8,8` |
| Grænse for duty cycle, i procent | `set dutycycle 10` |
| Radiochippens sendeeffekt, i dBm | `set tx <dBm>` |
| Position, så den vises på kort | `set lat <degrees>` og `set lon <degrees>` |
| Kontaktoplysninger til andre operatører | `set owner.info <text>` |
| Timer mellem flood-adverts, dem hele meshet hører | `set flood.advert.interval <hours>` |
| Annoncér den nu | `advert` |
| Genstart | `reboot` |

Standardadgangskoden til admin er `password`, og alle, der logger ind med den, bliver admin. Skift den, før repeateren går i luften.

Eksemplet med `set radio` ovenfor er EU/UK (Narrow). Brug i stedet værdierne fra dit områdes preset: [Anbefalede indstillinger](/guides/settings/) viser dem for hvert land.

**Indstil uret.** Uden et urmodul (RTC) mister en repeater tiden ved hvert strømsvigt og starter igen i maj 2024. Mens den kører, driver uret også: det løber længere og længere foran eller bagud. Indstil derfor uret en gang imellem: log ind på afstand fra appen, og brug `clock sync`, eller indstil tiden via USB. Med et RTC-modul behøver du sjældent at gøre det: det holder styr på tiden under strømsvigt og driver langt mindre.

**Administrér den på afstand.** Når den er på meshet, logger du ind fra MeshCore-appen med admin-adgangskoden. Der aflæser du dens status og bruger de samme kommandoer over radioen. Nogle kommandoer virker kun via USB, for eksempel `set freq` og fabriksnulstillingen `erase`.

**Behold dens identitet.** Før en sletning skriver du `get prv.key` via USB og gemmer den viste private nøgle et sikkert sted. Efter sletningen giver `set prv.key <key>` og et `reboot` repeateren dens gamle identitet tilbage, så noder, der kender den, finder den under det samme præfiks.

Den fulde kommandoliste står i
[MeshCore CLI-referencen](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Opdater den trådløst {#update}

Når repeateren først sidder højt oppe, opdaterer du den fra jorden. Log ind fra MeshCore-appen med admin-adgangskoden, åbn dens kommandolinje, og skriv `start ota`. Hvad der derefter sker, afhænger af boardet. Andre boards svarer `Error`, og dem opdaterer du via USB.

**nRF52-boards**, for eksempel RAK, Heltec T114, Seeed XIAO og SenseCAP Solar:

1. Hent **ZIP**-filen med den nye firmware til dit board fra [web-flasheren](https://flasher.meshcore.io).
2. Skriv `start ota`. Repeateren svarer `OK` og dukker op via Bluetooth som `<board>_OTA`, for eksempel `RAK4631_OTA`.
3. Åbn appen nRF Device Firmware Update på din telefon, vælg ZIP-filen og repeateren, og upload. Det tager nogle få minutter.

Installer [OTAFIX-bootloaderen](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX) på et nRF52-board, før det kommer op at sidde. Med den oprindelige bootloader kan du kun reparere en mislykket opdatering via USB. Med OTAFIX går boardet tilbage til opdateringstilstand, og du prøver igen via Bluetooth.

**ESP32-boards**, for eksempel Heltec V3 og V4:

1. Hent den **ikke-sammenflettede** `.bin` til dit board fra web-flasheren: filen uden "merged" i navnet.
2. Skriv `start ota`. Repeateren åbner et WiFi-netværk ved navn `MeshCore-OTA` og svarer med adressen på sin uploadside.
3. Gå inden for WiFi-rækkevidde, forbind din telefon eller bærbare computer til netværket, åbn adressen, og upload filen.

## Lovlige grænser {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
MeshCores europæiske presets ligger i delbåndet **869.40-869.65 MHz**. I EU, Storbritannien, Schweiz og Norge må kortrækkende enheder bruge det uden licens, inden for disse grænser:

- højst **500 mW e.r.p.** udstrålet effekt;
- højst **10% duty cycle**: højst 360 sekunders sendetid i en given time, pr. enhed. Alternativt må en enhed bruge listen-before-talk med adaptive frequency agility som defineret i ETSI EN 300 220-2;
- hele signalet, højst 250 kHz bredt, skal holde sig inden for delbåndet.

Båndet er delt: du må ikke forstyrre licenserede tjenester, og andre kan forstyrre dig.
Radioen skal være CE-mærket (i Storbritannien CE- eller UKCA-mærket).
{{< /callout >}}

Kilder: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845), bilag 1, bånd h1.7;
[Kommissionens beslutning 2006/771/EF](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) og dens ændringer;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), bånd O.

### Effekt: e.r.p. og din antenne {#erp}

Grænsen gælder den *udstrålede* effekt, målt i forhold til en simpel dipolantenne (e.r.p.). Antenneforstærkning tæller med, og kabeltab trækkes fra. Producenter angiver antenneforstærkning i dBi, hvor tallet er 2.15 dB højere end den samme forstærkning i dBd (i forhold til en dipol). Hold denne sum på højst 27 dBm (500 mW):

> sendeeffekt (dBm) + antenneforstærkning (dBi) − kabeltab (dB) − 2.15 ≤ 27

- Et board sender med 22 dBm ind i en antenne på 5 dBi gennem 1 dB kabeltab: 22 + 5 − 1 − 2.15 = 23.85 dBm, omkring 240 mW e.r.p. Det er inden for grænsen.
- Et board med en forstærker på 30 dBm (1 W) sender ind i en antenne på 3 dBi: 30 + 3 − 2.15 = 30.85 dBm, omkring 1.2 W e.r.p. Det er over grænsen, så skru ned for sendeeffekten.

Med `set tx` indstiller du LoRa-chippens udgangseffekt, i dBm. Selve SX1262-chippen når højst 22 dBm, og firmwaren tjekker ikke det tal, du indtaster. Boards med en ekstra forstærker, for eksempel Heltec V4 eller Station G2, sender med langt mere end det tal, du indstiller. Tjek producentens tabel, før du indstiller det, og start lavt.

### Duty cycle {#duty-cycle}

En repeater sender for alle omkring den, så den bruger sin sendetid hurtigere end en companion. MeshCores begrænser for duty cycle står som standard på 50%, og det er mere, end dette bånd tillader. Sæt den til 10% på alle repeatere:

```text
set dutycycle 10
```

### Frekvensnøjagtighed {#frequency}

EU/UK (Narrow)-kanalen, 869.618 MHz med 62.5 kHz båndbredde, når op til 869.649 MHz: mindre end 1 kHz under toppen af delbåndet. Signalet skal holde sig inden for båndet ved enhver temperatur. Det kræver en temperaturkompenseret krystal (TCXO). Næsten alle nuværende boards har en. Ældre boards uden TCXO, for eksempel Heltec V2, driver for meget til at virke pålideligt ved 62.5 kHz.

### Noter om de enkelte lande {#countries}

- **EU-medlemslande** skal stille dette delbånd til rådighed på disse vilkår (beslutning 2006/771/EF, artikel 3).
- **Storbritannien:** samme grænser, i Ofcom [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Schweiz og Liechtenstein:** samme grænser, i OFCOM [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norge:** samme grænser, i [forskriften om generelle tilladelser](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Disse noter er ikke juridisk rådgivning. Reglerne ændrer sig. Er du i tvivl, så tjek hos din nationale myndighed på området.

## Tjekliste til opsætning {#checklist}

- [ ] Ejeren af stedet har sagt ja, og du kan komme til repeateren for at vedligeholde den.
- [ ] Boardet kører **Repeater**-firmwaren, og antennen sad på før første opstart.
- [ ] Admin-adgangskoden er skiftet.
- [ ] Radioen passer til [dit områdes preset](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` er indstillet.
- [ ] Sendeeffekt plus antenneforstærkning holder sig inden for 500 mW e.r.p.
- [ ] Navn, position og `owner.info` er indstillet, så andre ved, hvem der driver den.
- [ ] Uret er indstillet (`clock`).
- [ ] Kabinettet er tæt, med et dræn- eller udluftningshul, og kablet har en drypsløjfe.
- [ ] Batteri og panel er dimensioneret til den værste vintermåned.
- [ ] Du har testet den på afstand med appen, før du forlader stedet.
- [ ] Din lokale gruppe ved, at den er oppe at køre.
