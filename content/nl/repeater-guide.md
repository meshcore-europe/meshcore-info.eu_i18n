---
title: Gids voor repeaters
lead: Een repeater op een hoge plek stuurt berichten door voor iedereen in de buurt, over een hele stad of vallei. Kies een plek, laat hem op zonne-energie draaien, stel hem in en blijf binnen de wet.
description: 'Een MeshCore-repeater in Europa plannen, van stroom voorzien, instellen en legaal gebruiken: plaatskeuze, zonnepaneel berekenen, CLI-instellingen, vermogen en duty cycle op 868 MHz.'
eyebrow: 868 MHz · tot 500 mW · zonder vergunning
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-10-31'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Repeaters dragen de mesh. Companions, de radio's waarmee je berichten stuurt, sturen
geen berichten door. Zonder repeaters bereik je dus alleen mensen binnen direct
bereik. Een repeater op de juiste plek vergroot de mesh voor iedereen in de buurt.
Deze gids volgt MeshCore-firmware v1.18.0.

Praat eerst met je [lokale groep](/community/). Zij weten waar dekking ontbreekt,
welke [preset je regio gebruikt](/guides/settings/) en hoe je repeaters een naam
geeft. Bekijk op de [dekkingskaarten](/map/) welke repeaters er bij jou in de buurt
staan, en zeg hallo op het openbare of een lokaal [kanaal](/guides/channels/).

## Heb je er een nodig? {#need}

Een repeater stuurt elk flood-bericht door dat hij hoort. Alle repeaters binnen
bereik delen dezelfde zendtijd. Bereikt de mesh je al, dan levert een extra repeater
meer verkeer op en geen extra dekking. Vaak volstaat een companion op een hoge plek,
bij een zolderraam of op een balkon.

Zet een repeater neer waar dekking ontbreekt:

- de [dekkingskaarten](/map/) tonen geen repeater bij jou in de buurt, of alleen
  repeaters die je companion niet hoort;
- je lokale groep zegt dat de regio er een nodig heeft.

## Kies een plek {#site}

Hoogte wint het van vermogen. LoRa op 868 MHz komt het verst bij vrij zicht.
Heuvels, gebouwen en dichte bomen kosten veel meer bereik dan een paar extra
milliwatt terugwinnen.

- **Ga hoog.** Een dak, een mast, een hoog gebouw of een heuvel dekt veel meer dan
  een vensterbank. Al een paar meter boven de omliggende daken helpt.
- **Houd de antenne vrij.** Monteer hem boven de dakrand, uit de buurt van metaal,
  dakgoten en andere antennes.
- **Controleer het zicht.** Met tools als [HeyWhatsThat](https://www.heywhatsthat.com/)
  zie je wat je vanaf een plek kunt zien. Zie je een plek, dan ligt een repeater
  daar binnen bereik.
- **Laat ruimte vrij.** Een radiopad heeft wat vrije ruimte rond de directe lijn
  nodig, niet alleen de lijn zelf. Over lange afstanden moet het midden van het pad
  enkele meters boven obstakels blijven.
- **Vraag toestemming.** Vraag de eigenaar van het dak of de mast om toestemming.
  Spreek af hoe je bij de repeater komt voor onderhoud.

## Hardware {#hardware}

- **Board.** Kies een zuinig nRF52-board, zoals de [Heltec T114](/devices/), RAK
  WisBlock of de SenseCAP Solar Node. ESP32-boards verbruiken meer stroom (op de
  apparatenpagina staan ze als High). Op zonne-energie draaien is daardoor lastig.
- **Antenne.** Gebruik een antenne voor 868 MHz en monteer hem verticaal. De
  [antennegids](/guides/antenna/) behandelt soorten, connectoren, kabel en montage.
  De antennewinst telt mee voor de wettelijke vermogensgrens; zie
  [Wettelijke grenzen](#legal).
- **Kabel.** Houd de coaxkabel kort, of gebruik kabel met weinig verlies. Op 868 MHz
  kost een paar meter dunne kabel je soms de helft van je vermogen.
- **Behuizing.** Gebruik een waterdichte kast (IP65 of beter) met een kabelwartel,
  een ventilatie- of afvoergat tegen condens, en een lichte kleur of zonnekap.
  Accu's hebben last van hitte en laden niet op onder het vriespunt.
- **Bliksem.** Een antenne op een dak is een doelwit. Volg de lokale regels voor
  aarding, of monteer hem waar een inslag de bedrading van het gebouw niet bereikt.

## Stroom en zonnepaneel berekenen {#power}

Een repeater op zonne-energie moet de donkerste winterweken doorstaan. Reken
daarom met die weken:

1. **Meet het verbruik.** Laat de ingestelde repeater een dag lang via een
   USB-stroommeter draaien. Lees het verbruikte energie af in wattuur (Wh). Het
   verkeer in je regio beïnvloedt dit getal, dus meet zo mogelijk ter plekke.
2. **Neem reserve.** Reken de accucapaciteit voor minstens 5 tot 7 dagen zonder
   bruikbare zon.
3. **Zoek je winterzon op.** Met de gratis
   [PVGIS-tool](https://re.jrc.ec.europa.eu/pvg_tools/en/) van de EU zie je voor elke
   plek hoeveel energie een paneel per maand oplevert. Neem de maand met de minste zon.
4. **Bepaal het paneel.** Het paneel moet in die slechtste maand het verbruik van
   elke dag aanvullen, met marge voor laadverliezen.

Een rekenvoorbeeld, met aangenomen getallen: een repeater die 1 Wh per dag
verbruikt, heeft voor een week reserve een accu van minstens 7 Wh nodig. Dat is
ongeveer 2 Ah bruikbare capaciteit bij 3,7 V. Geeft een paneel van 1 W op jouw plek
volgens PVGIS 0,5 Wh per dag in december? Dan heb je minstens een paneel van 2 W
nodig. Met 3 tot 5 W heb je marge voor wolken, sneeuw en veroudering.

## Instellen {#config}

**Flashen.** Gebruik de [webflasher](https://flasher.meshcore.io) en kies de
**Repeater**-firmware voor je board. De stappen voor het flashen staan in
[Aan de slag](/get-started/#flash).

**Instellen via USB.** Laat de repeater aan je computer hangen en open
[config.meshcore.io](https://config.meshcore.io) of de console van de flasher. Je
kunt ook elke seriële terminal op 115200 baud gebruiken. De belangrijkste commando's:

| Wat | Commando |
|---|---|
| Het adminwachtwoord wijzigen | `password <new password>` |
| Een naam geven | `set name <name>` |
| Radiopreset: frequentie, bandbreedte, SF, CR (werkt na herstart) | `set radio 869.618,62.5,8,8` |
| Duty-cyclegrens, in procent | `set dutycycle 10` |
| Zendvermogen van de radiochip, in dBm | `set tx <dBm>` |
| Positie, zodat hij op kaarten verschijnt | `set lat <degrees>` en `set lon <degrees>` |
| Contactgegevens voor andere beheerders | `set owner.info <text>` |
| Uren tussen flood-advertenties, die de hele mesh hoort | `set flood.advert.interval <hours>` |
| Nu aankondigen | `advert` |
| Herstarten | `reboot` |

Het standaard adminwachtwoord is `password`. Wie daarmee inlogt, wordt admin.
Wijzig het voordat de repeater gaat uitzenden.

Het voorbeeld van `set radio` hierboven is EU/UK (Narrow). Gebruik in plaats daarvan
de waarden van de preset in jouw regio: [Aanbevolen instellingen](/guides/settings/)
geeft ze per land.

**Zet de klok gelijk.** Zonder klokmodule (RTC) raakt een repeater bij elke
stroomstoring de tijd kwijt en start hij opnieuw in mei 2024. Terwijl hij draait,
loopt zijn klok ook weg: hij loopt steeds verder voor of achter. Zet de klok daarom
af en toe gelijk. Log op afstand in vanuit de app en gebruik `clock sync`, of stel
de tijd in via USB. Met een RTC-module hoeft dat zelden: die houdt de tijd vast bij
stroomstoringen en loopt veel minder weg.

**Beheer op afstand.** Staat hij eenmaal op de mesh, dan log je in vanuit de
MeshCore-app met het adminwachtwoord. Daar lees je de status en gebruik je dezelfde
commando's via de radio. Sommige commando's werken alleen via USB, zoals `set freq`
en de fabrieksreset `erase`.

**Bewaar de identiteit.** Typ vóór een erase via USB `get prv.key` en bewaar de
privésleutel die verschijnt op een veilige plek. Na de erase geven
`set prv.key <key>` en een `reboot` de repeater zijn oude identiteit terug. Nodes
die hem kennen, vinden hem dan onder hetzelfde prefix.

De volledige lijst met commando's staat in de
[MeshCore CLI-referentie](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Draadloos updaten {#update}

Hangt de repeater eenmaal hoog, dan update je hem vanaf de grond. Log in vanuit de
MeshCore-app met het adminwachtwoord, open de opdrachtregel en typ `start ota`. Wat
er dan gebeurt, hangt af van het board. Andere boards antwoorden `Error`; die update
je via USB.

**nRF52-boards**, zoals RAK, Heltec T114, Seeed XIAO en SenseCAP Solar:

1. Download de **ZIP** van de nieuwe firmware voor je board via de
   [webflasher](https://flasher.meshcore.io).
2. Typ `start ota`. De repeater antwoordt `OK` en verschijnt via Bluetooth als
   `<board>_OTA`, bijvoorbeeld `RAK4631_OTA`.
3. Open de app nRF Device Firmware Update op je telefoon, kies de ZIP en de repeater
   en upload. Dat duurt een paar minuten.

Installeer de [OTAFIX-bootloader](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
op een nRF52-board voordat het de hoogte in gaat. Met de standaard bootloader
herstel je een mislukte update alleen via USB. Met OTAFIX valt het board terug in
de updatemodus en probeer je het opnieuw via Bluetooth.

**ESP32-boards**, zoals de Heltec V3 en V4:

1. Download via de webflasher de **niet-samengevoegde** `.bin` voor je board: het
   bestand zonder "merged" in de naam.
2. Typ `start ota`. De repeater opent een WiFi-netwerk met de naam `MeshCore-OTA`
   en antwoordt met het adres van zijn uploadpagina.
3. Verbind binnen WiFi-bereik je telefoon of laptop met dat netwerk, open het adres
   en upload het bestand.

## Wettelijke grenzen {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
De Europese presets van MeshCore liggen in de subband **869.40-869.65 MHz**. In de
EU, het VK, Zwitserland en Noorwegen mogen apparaten voor korte afstand die zonder
vergunning gebruiken, binnen deze grenzen:

- maximaal **500 mW e.r.p.** uitgestraald vermogen;
- maximaal **10% duty cycle**: per apparaat niet meer dan 360 seconden zenden per
  uur. Een apparaat mag ook listen-before-talk met adaptive frequency agility
  gebruiken, zoals vastgelegd in ETSI EN 300 220-2;
- het hele signaal, maximaal 250 kHz breed, moet binnen de subband blijven.

De band is gedeeld: je mag diensten met vergunning niet storen, en anderen mogen
jou storen.
De radio moet een CE-markering hebben (in Groot-Brittannië CE of UKCA).
{{< /callout >}}

Bronnen: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
bijlage 1, band h1.7;
[Beschikking 2006/771/EG van de Commissie](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
en de wijzigingen daarvan;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
band O.

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

Een repeater zendt voor iedereen in de buurt. Hij verbruikt zijn zendtijd dus
sneller dan een companion. De duty-cyclebegrenzer van MeshCore staat standaard op
50%, meer dan deze band toestaat. Zet hem op elke repeater op 10%:

```text
set dutycycle 10
```

### Frequentienauwkeurigheid {#frequency}

Het kanaal EU/UK (Narrow), 869.618 MHz met 62.5 kHz bandbreedte, reikt tot
869.649 MHz. Dat is minder dan 1 kHz onder de bovenkant van de subband. Het signaal
moet bij elke temperatuur binnen de band blijven. Daarvoor is een
temperatuurgecompenseerd kristal (TCXO) nodig. Bijna elk huidig board heeft er een.
Oudere boards zonder TCXO, zoals de Heltec V2, lopen te ver weg om betrouwbaar
op 62.5 kHz te werken.

### Per land {#countries}

- **EU-lidstaten** moeten deze subband onder deze voorwaarden beschikbaar stellen
  (Beschikking 2006/771/EG, artikel 3).
- **Verenigd Koninkrijk:** dezelfde grenzen, in Ofcom
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Zwitserland en Liechtenstein:** dezelfde grenzen, in OFCOM
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Noorwegen:** dezelfde grenzen, in de
  [regeling voor algemene vergunningen](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Deze notities zijn geen juridisch advies. Regels veranderen. Twijfel je, vraag het
dan na bij je nationale toezichthouder.

## Checklist voor plaatsing {#checklist}

- [ ] De eigenaar van de plek heeft ingestemd, en je kunt bij de repeater voor onderhoud.
- [ ] Het board draait de **Repeater**-firmware, en de antenne zat erop vóór de
      eerste keer aanzetten.
- [ ] Het adminwachtwoord is gewijzigd.
- [ ] De radio komt overeen met [de preset van je regio](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` is ingesteld.
- [ ] Zendvermogen plus antennewinst blijft binnen 500 mW e.r.p.
- [ ] Naam, positie en `owner.info` zijn ingesteld, zodat anderen weten wie hem beheert.
- [ ] De klok is gelijkgezet (`clock`).
- [ ] De behuizing is dicht, met een afvoer- of ventilatiegat, en de kabel heeft een
      druppellus.
- [ ] Accu en paneel zijn berekend op de slechtste wintermaand.
- [ ] Je hebt hem met de app op afstand getest voordat je de plek verliet.
- [ ] Je lokale groep weet dat hij in de lucht is.
