---
title: Guide til repeatere
lead: En repeater, der står højt, sender beskeder videre for alle omkring den, over en hel by eller dal. Find et sted, giv den strøm fra solen, sæt den op, og hold dig inden for loven.
description: 'Planlæg, forsyn, konfigurer og drift en MeshCore-repeater lovligt i Europa: valg af sted, dimensionering af solcelle, CLI-indstillinger, effekt og duty cycle-grænser på 868 MHz.'
eyebrow: 868 MHz · op til 500 mW · uden licens
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-10-31'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Repeatere bærer meshet. Companions, de radioer du skriver beskeder fra, sender ikke
beskeder videre. Uden repeatere når du derfor kun de folk, der er inden for
direkte rækkevidde. En repeater på det rigtige sted udvider meshet for alle
omkring den. Denne guide følger MeshCore-firmware v1.18.0.

Før du går i gang, så tal med din [lokale gruppe](/community/). De ved, hvor
der mangler dækning, hvilken [preset dit område bruger](/guides/settings/), og hvordan repeatere skal navngives. Se på
[dækningskortene](/map/), om der er repeatere nær dig, og sig hej på de offentlige
eller lokale [kanaler](/guides/channels/).

## Har du brug for en? {#need}

En repeater sender hver flood-besked videre, som den hører. Alle repeatere inden for
rækkevidde deler den samme sendetid. Hvor meshet allerede når dig, giver en repeater
mere ekstra trafik og ingen ekstra dækning. En companion, der står højt i et
kvistvindue eller på en altan, kan være alt, du behøver.

Sæt en repeater op, hvor der mangler dækning:

- [dækningskortene](/map/) viser ingen repeater nær dig, eller kun nogle, som din
  companion ikke hører;
- din lokale gruppe siger, at området har brug for en.

## Vælg et sted {#site}

Højde slår effekt. LoRa på 868 MHz rækker længst, når der er fri sigtelinje.
Bakker, bygninger og tæt skov koster langt mere rækkevidde, end nogle få ekstra
milliwatt vinder tilbage.

- **Gå højt op.** Et tag, en mast, en høj bygning eller en bakke dækker langt mere
  end en vindueskarm. Allerede nogle få meter over de omkringliggende tage hjælper.
- **Giv antennen frit udsyn.** Monter den over tagkanten, væk fra metal,
  tagrender og andre antenner.
- **Tjek udsynet.** Med værktøjer som [HeyWhatsThat](https://www.heywhatsthat.com/)
  kan du se, hvad der er synligt fra et sted. Kan du se et punkt, kan en repeater
  der også nås.
- **Hold området frit.** En radiosti kræver noget fri plads omkring den direkte
  linje, ikke kun selve linjen. Over lange afstande skal midten af stien
  gå flere meter over forhindringer.
- **Spørg om lov.** Få ejerens samtykke til taget eller masten, og aftal,
  hvordan du kommer til repeateren, når den skal vedligeholdes.

## Hardware {#hardware}

- **Board.** Vælg et strømbesparende nRF52-board som
  [Heltec T114](/devices/), RAK WisBlock eller SenseCAP Solar Node. ESP32-boards
  bruger mere strøm (enhedssiden markerer dem med High), og det gør drift på
  solcelle svær.
- **Antenne.** Brug en antenne lavet til 868 MHz, monteret lodret.
  [Antenneguiden](/guides/antenna/) gennemgår typer, stik, kabel og
  montering. Antennens forstærkning tæller med i den lovlige effektgrænse. Se
  [Lovlige grænser](#legal).
- **Kabel.** Hold koaksialkablet kort, eller brug kabel med lavt tab. På 868 MHz kan
  nogle få meter tyndt kabel æde halvdelen af din effekt.
- **Kabinet.** Brug en vejrtæt boks (IP65 eller bedre) med kabelforskruning,
  et ventilations- eller drænhul mod kondens og en lys farve eller solskærm.
  Batterier har det dårligt i varme og kan ikke lades under frysepunktet.
- **Lyn.** En antenne på et tag er et mål. Følg de lokale regler for
  jording, eller monter den, hvor et lynnedslag ikke når bygningens
  elinstallation.

## Strøm og dimensionering af solcelle {#power}

En solcelledrevet repeater skal klare vinterens mørkeste uger. Dimensioner den
efter dem:

1. **Mål forbruget.** Kør den konfigurerede repeater gennem en USB-strømmåler
   i et døgn. Aflæs energiforbruget i watt-timer (Wh). Trafikken i dit område
   påvirker tallet, så mål på stedet, hvis du kan.
2. **Læg reserve til.** Planlæg batterikapacitet til mindst 5 til 7 dage
   uden brugbar sol.
3. **Find din vintersol.** Med EU's gratis
   [PVGIS-værktøj](https://re.jrc.ec.europa.eu/pvg_tools/en/) kan du se, hvor meget
   energi et panel producerer pr. måned på et givet sted. Brug måneden med
   mindst sol.
4. **Dimensioner panelet.** Panelet skal dække hver dags forbrug i den værste
   måned, med plads til tab under opladning.

Et regneeksempel med antagne tal: En repeater, der bruger 1 Wh pr. dag,
skal have et batteri på mindst 7 Wh for en uges reserve, cirka 2 Ah
brugbar kapacitet ved 3,7 V. Hvis PVGIS siger, at et panel på 1 W på dit sted giver
0,5 Wh pr. dag i december, skal du bruge mindst et panel på 2 W. Med 3 til 5 W
har du margin til skyer, sne og ældning.

## Sæt den op {#config}

**Flash.** Brug [webflasheren](https://flasher.meshcore.io), og vælg
**Repeater**-firmwaren til dit board. Trinene til at flashe står i
[Kom i gang](/get-started/#flash).

**Konfigurer over USB.** Mens repeateren stadig er sluttet til din computer,
åbner du [config.meshcore.io](https://config.meshcore.io) eller flasherens
konsol. Du kan også bruge en hvilken som helst seriel terminal på 115200 baud. De vigtigste
kommandoer:

| Hvad | Kommando |
|---|---|
| Skift admin-adgangskoden | `password <new password>` |
| Giv den et navn | `set name <name>` |
| Radio-preset: frekvens, båndbredde, SF, CR (genstart for at anvende) | `set radio 869.618,62.5,8,8` |
| Duty cycle-grænse, i procent | `set dutycycle 10` |
| Sendeeffekt fra radiochippen, i dBm | `set tx <dBm>` |
| Position, så den vises på kort | `set lat <degrees>` og `set lon <degrees>` |
| Kontaktoplysninger til andre operatører | `set owner.info <text>` |
| Timer mellem flood-adverts, dem hele meshet hører | `set flood.advert.interval <hours>` |
| Annoncer den nu | `advert` |
| Genstart | `reboot` |

Standardadgangskoden til admin er `password`, og alle, der logger ind med den,
bliver admin. Skift den, før repeateren går i luften.

Eksemplet med `set radio` ovenfor er EU/UK (Narrow). Brug i stedet værdierne fra dit
områdes preset: [Anbefalede indstillinger](/guides/settings/) viser dem
for hvert land.

**Stil uret.** Uden et urmodul (RTC) mister en repeater tiden ved
hvert strømsvigt og starter igen i maj 2024. Mens den kører, driver uret også:
det går mere og mere foran eller bagud. Stil derfor uret en gang imellem: Log
ind på afstand fra appen og brug `clock sync`, eller stil tiden over USB. Med
et RTC-modul skal du sjældent gøre det: Det holder tiden gennem strømsvigt og
driver langt mindre.

**Styr den på afstand.** Når den er på meshet, logger du ind fra MeshCore-appen
med admin-adgangskoden. Der kan du læse dens status og bruge de samme kommandoer
over radioen. Nogle kommandoer virker kun over USB, for eksempel `set freq` og
fabriksnulstillingen `erase`.

**Bevar dens identitet.** Før en erase skriver du `get prv.key` over USB og gemmer
den private nøgle, den viser, et sikkert sted. Efter din erase giver `set prv.key <key>`
og en `reboot` repeateren dens gamle identitet tilbage. Så finder noder, der kender
den, den under samme præfiks.

Den fulde liste over kommandoer står i
[MeshCore CLI-referencen](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Opdater den trådløst {#update}

Når repeateren sidder højt oppe, opdaterer du den fra jorden. Log ind fra
MeshCore-appen med admin-adgangskoden, åbn dens kommandolinje, og skriv
`start ota`. Hvad der derefter sker, afhænger af boardet. Andre boards svarer `Error`,
og dem opdaterer du over USB.

**nRF52-boards**, som RAK, Heltec T114, Seeed XIAO og SenseCAP Solar:

1. Hent **ZIP**-filen med den nye firmware til dit board fra
   [webflasheren](https://flasher.meshcore.io).
2. Skriv `start ota`. Repeateren svarer `OK` og dukker op over Bluetooth
   som `<board>_OTA`, for eksempel `RAK4631_OTA`.
3. Åbn appen nRF Device Firmware Update på din telefon, vælg ZIP-filen og
   repeateren, og upload. Det tager nogle minutter.

Installer [OTAFIX-bootloaderen](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
på et nRF52-board, før det kommer op. Med den oprindelige bootloader kan en mislykket
opdatering kun repareres over USB. Med OTAFIX går boardet tilbage til
opdateringstilstand, og du prøver igen over Bluetooth.

**ESP32-boards**, som Heltec V3 og V4:

1. Hent den **ikke-sammenflettede** `.bin`-fil til dit board fra webflasheren:
   filen uden "merged" i navnet.
2. Skriv `start ota`. Repeateren åbner et WiFi-netværk med navnet `MeshCore-OTA`
   og svarer med adressen på sin upload-side.
3. Når du er inden for WiFi-rækkevidde, forbinder du din telefon eller bærbare til netværket,
   åbner adressen og uploader filen.

## Lovlige grænser {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
MeshCores europæiske presets ligger i underbåndet **869.40-869.65 MHz**. I
EU, Storbritannien, Schweiz og Norge er det åbent for kortdistanceudstyr uden
licens, inden for disse grænser:

- højst **500 mW e.r.p.** udstrålet effekt;
- højst **10% duty cycle**: ikke mere end 360 sekunders sending i
  løbet af en time, pr. enhed. Alternativt må en enhed bruge listen-before-talk
  med adaptive frequency agility som defineret i ETSI EN 300 220-2;
- hele signalet, højst 250 kHz bredt, skal holde sig inden for underbåndet.

Båndet er delt: Du må ikke forstyrre licenserede tjenester, og andre kan
forstyrre dig.
Radioen skal være CE-mærket (i Storbritannien CE eller UKCA).
{{< /callout >}}

Kilder: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
Annex 1, bånd h1.7;
[Kommissionens beslutning 2006/771/EF](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
og dens ændringer;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
bånd O.

### Power: e.r.p. and your antenna {#erp}

The limit applies to the *radiated* power, measured against a simple dipole
antenna (e.r.p.). Antenna gain counts; cable loss subtracts. Makers state
antenna gain in dBi, which is 2.15 dB more than the same gain in dBd
(relative to a dipole). Keep this sum at or below 27 dBm (500 mW):

> transmit power (dBm) + antenna gain (dBi) − cable loss (dB) − 2.15 ≤ 27

- A board transmitting 22 dBm into a 5 dBi antenna through 1 dB of cable:
  22 + 5 − 1 − 2.15 = 23.85 dBm, about 240 mW e.r.p. Within the limit.
- A board with a 30 dBm (1 W) amplifier into a 3 dBi antenna:
  30 + 3 − 2.15 = 30.85 dBm, about 1.2 W e.r.p. Over the limit; lower the
  transmit power.

`set tx` sets the output of the LoRa chip, in dBm. The SX1262 chip itself
tops out at 22 dBm; the firmware does not check the number you enter. Boards with an extra
amplifier, such as the Heltec V4 or the Station G2, transmit much more than
the number you set. Check the manufacturer's table before you set it, and
start low.

### Duty cycle {#duty-cycle}

En repeater sender for alle omkring den, så den bruger sin sendetid hurtigere
op end en companion. MeshCores duty cycle-begrænser står som standard på 50%, og det er
mere, end dette bånd tillader. Sæt den til 10% på hver repeater:

```text
set dutycycle 10
```

### Frekvensnøjagtighed {#frequency}

EU/UK (Narrow)-kanalen, 869.618 MHz med 62.5 kHz båndbredde, rækker op til 869.649 MHz: mindre end 1 kHz under toppen af underbåndet. Signalet skal holde sig inden for båndet ved enhver temperatur. Det kræver en temperaturkompenseret krystal (TCXO). Næsten alle nuværende boards har en. Ældre boards uden, som Heltec V2, driver for meget til at virke pålideligt på 62.5 kHz.

### Noter om lande {#countries}

- **EU-medlemslande** skal stille dette underbånd til rådighed på disse vilkår
  (beslutning 2006/771/EF, artikel 3).
- **Storbritannien:** de samme grænser, i Ofcom
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Schweiz og Liechtenstein:** de samme grænser, i OFCOM
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norge:** de samme grænser, i
  [forskriften om generelle tilladelser](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Disse noter er ikke juridisk rådgivning. Reglerne ændrer sig. Er du i tvivl, så spørg
din nationale myndighed.

## Tjekliste til opsætning {#checklist}

- [ ] Ejeren af stedet har sagt ja, og du kan komme til repeateren for vedligeholdelse.
- [ ] Boardet kører **Repeater**-firmwaren, og antennen sad på
      før første opstart.
- [ ] Admin-adgangskoden er skiftet.
- [ ] Radioen passer til [dit områdes preset](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` er sat.
- [ ] Sendeeffekt plus antenneforstærkning holder sig inden for 500 mW e.r.p.
- [ ] Navn, position og `owner.info` er sat, så andre ved, hvem der driver den.
- [ ] Uret er stillet (`clock`).
- [ ] Kabinettet er tæt, med et dræn- eller ventilationshul, og kablet har en
      dryppesløjfe.
- [ ] Batteri og panel er dimensioneret til den værste vintermåned.
- [ ] Du har testet den på afstand med appen, før du forlod stedet.
- [ ] Din lokale gruppe ved, at den er oppe.
