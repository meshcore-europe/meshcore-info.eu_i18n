---
title: Repeatergids
lead: Een hoog geplaatste repeater geeft berichten door voor iedereen in de omgeving, over een hele stad of vallei. Kies een locatie, laat de zon de repeater voeden, stel hem in en blijf binnen de wet.
description: 'Plan, voed, configureer en gebruik een MeshCore-repeater legaal in Europa: locatiekeuze, zonnepaneel en accu berekenen, CLI-instellingen, 868 MHz-grenzen voor vermogen en duty cycle.'
eyebrow: 868 MHz · tot 500 mW · licentievrij
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '3e38a8c6'
  seeded: '2026-11-04'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '824ab38e', '662ea23c', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', 'bbea9a0c', '2b9fab3b', 'b13d1947', 'c2bad16f', '636edc86', 'c2d6bcd1', '957ae975', '98874949', '96d1ebad', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

De mesh draait op repeaters. Companions, de radio's waarmee je berichten stuurt, geven berichten niet door. Zonder repeaters kom je dus alleen bij mensen in je directe bereik. Een repeater op de juiste plek vergroot de mesh voor iedereen in de omgeving. Deze gids gaat uit van MeshCore-firmware v1.18.0.

Overleg eerst met je [lokale groep](/community/). Die weet waar dekking ontbreekt, [welke preset jouw gebied gebruikt](/guides/settings/) en hoe je repeaters een naam geeft. Zoek op de [dekkingskaarten](/map/) naar repeaters bij jou in de buurt, en zeg hallo op de openbare of lokale [kanalen](/guides/channels/).

## Heb je er een nodig? {#need}

Een repeater zendt elk flood-bericht dat hij hoort opnieuw uit, en alle repeaters binnen bereik delen dezelfde zendtijd. Waar de mesh je al bereikt, levert nog een repeater meer verkeer op, geen extra dekking. Een hoog geplaatste companion, bij een zolderraam of op een balkon, kan al genoeg zijn.

Plaats een repeater waar dekking ontbreekt:

- je ziet op de [dekkingskaarten](/map/) geen repeater bij jou in de buurt, of alleen repeaters die je companion niet hoort;
- je lokale groep zegt dat het gebied er een nodig heeft.

## Kies een locatie {#site}

Hoogte weegt zwaarder dan vermogen. LoRa op 868 MHz komt het verst langs een vrije zichtlijn. Heuvels, gebouwen en dichte bomen kosten veel meer bereik dan een paar extra milliwatt kunnen goedmaken.

- **Ga hoog.** Een dak, een mast, een hoog gebouw of een heuvel bestrijkt veel meer
  dan een vensterbank. Zelfs een paar meter boven de omliggende daken helpt al.
- **Houd de antenne vrij.** Monteer hem boven de dakrand, uit de buurt van
  metaal, dakgoten en andere antennes.
- **Bekijk het uitzicht.** Tools zoals [HeyWhatsThat](https://www.heywhatsthat.com/)
  laten zien wat je vanaf een plek kunt zien. De MeshCore-app
  [berekent wat een repeater daar kan bereiken](#check-site).
- **Zorg voor vrije ruimte.** Een radiopad heeft vrije ruimte rond de directe lijn nodig,
  niet alleen de lijn zelf. Op 868 MHz is die ruimte ongeveer 20 m rond het
  midden van een pad van 5 km. Bij 20 km is dat ongeveer 40 m.
- **Vraag toestemming.** Vraag de eigenaar toestemming voor het dak of de mast,
  en spreek af hoe je de repeater bereikt voor onderhoud.

### Een locatie controleren in de app {#check-site}

In versie 1.33 of later van de MeshCore-app staan deze tools in het menu onder
**Tools**. Ze werken zonder verbonden radio.

- **Line of Sight** tekent het terrein tussen 2 punten en de ruimte die het
  signaal daarboven nodig heeft. Druk lang op 2 punten op de kaart, of tik op repeaters.
- **Antenna Coverage** laat op de kaart zien wat een antenne op 1 punt kan bereiken.
  Druk lang op een punt of tik op een repeater. Voeg meer punten toe om locaties te vergelijken.

Op een computer kies je **Add Point** in het menu van de tool en typ je de coördinaten in.

Beide tools gaan uit van een antenne op jouw locatie op 5 m. Stel daarom in
de instellingen van de tool de hoogte in die je wilt gebruiken. Antenna
Coverage gaat uit van een ontvangende antenne op 1 m. Zonder aangesloten radio
gaat Line of Sight uit van 915 MHz: stel in de instellingen de frequentie van
je [preset](/guides/settings/) in.

De tools rekenen met hoogtegegevens en testen je radio niet. Controleer zelf bomen en
nieuwe gebouwen. Neem daarna een companion mee naar de plek en kijk welke
repeaters hij hoort.

![Line of Sight in de MeshCore-app: het terrein tussen 2 punten en de ruimte die het signaal daarboven nodig heeft](/media/guides/line-of-sight.webp)

![Antenna Coverage in de MeshCore-app: het gebied dat een antenne op een heuvel kan bereiken, op een kaart](/media/guides/antenna-coverage.webp)

## Hardware {#hardware}

- **Board.** Kies een zuinig nRF52-board zoals de [Heltec T114](/devices/), RAK WisBlock of de SenseCAP Solar Node. ESP32-boards verbruiken meer stroom (op de apparatenpagina staan ze als High), en dat maakt werken op zonne-energie lastig.
- **Antenne.** Gebruik een antenne die voor 868 MHz is gemaakt en monteer hem verticaal. De [antennegids](/guides/antenna/) behandelt typen, connectoren, kabel en montage. Antennewinst telt mee voor de wettelijke vermogensgrens, zie [Wettelijke grenzen](#legal).
- **Kabel.** Houd coaxkabel kort, of gebruik kabel met weinig verlies. Op 868 MHz kan een paar meter dunne kabel de helft van je vermogen kosten.
- **Behuizing.** Gebruik een weerbestendige kast (IP65 of beter) met een kabelwartel, een ventilatie- of afvoergaatje tegen condens, en een lichte kleur of zonnekap. Accu's lijden onder hitte en kun je onder het vriespunt niet opladen.
- **Bliksem.** Een antenne op een dak is een doelwit. Volg de lokale regels voor aarding, of monteer de antenne op een plek waar een inslag de bedrading van het gebouw niet bereikt.

## Stroom en zonnepaneel berekenen {#power}

Een repeater op zonne-energie moet de donkerste winterweken doorstaan. Bereken je opstelling op die weken:

1. **Meet het verbruik.** Sluit de geconfigureerde repeater een dag lang aan op een USB-stroommeter. Lees het energieverbruik af in wattuur (Wh). Het verkeer in je gebied beïnvloedt dit getal, dus meet zo mogelijk ter plekke.
2. **Neem reserve.** Reken op accucapaciteit voor minstens 5 tot 7 dagen zonder bruikbare zon.
3. **Zoek je winterzon op.** De gratis [PVGIS-tool](https://re.jrc.ec.europa.eu/pvg_tools/en/) van de EU toont voor elke locatie hoeveel energie een paneel per maand opwekt. Gebruik de maand met de minste zon.
4. **Bepaal de grootte van het paneel.** Het paneel moet in die slechtste maand het verbruik van elke dag opwekken, met ruimte voor laadverliezen.

Een uitgewerkt voorbeeld, met aangenomen getallen: een repeater die 1 Wh per dag verbruikt, heeft voor een week reserve een accu van minstens 7 Wh nodig. Dat is ongeveer 2 Ah bruikbare capaciteit bij 3.7 V. Als PVGIS aangeeft dat een paneel van 1 W op jouw locatie in december 0.5 Wh per dag oplevert, heb je minstens een paneel van 2 W nodig. Met 3 tot 5 W houd je marge voor wolken, sneeuw en veroudering.

## Stel hem in {#config}

**Flashen.** Gebruik de [webflasher](https://flasher.meshcore.io) en kies de **Repeater**-firmware voor je board. De stappen voor het flashen vind je bij [Aan de slag](/get-started/#flash).

**Configureren via USB.** Open [config.meshcore.io](https://config.meshcore.io) of de console van de flasher terwijl de repeater nog op je computer is aangesloten. Je kunt ook elke seriële terminal op 115200 baud gebruiken. De belangrijkste commando's:

| Wat | Commando |
|---|---|
| Het beheerderswachtwoord wijzigen | `password <new password>` |
| Een naam geven | `set name <name>` |
| Radiopreset: frequentie, bandbreedte, SF, CR (herstart om toe te passen) | `set radio 869.618,62.5,8,8` |
| Duty-cycle-limiet, in procent | `set dutycycle 10` |
| Zendvermogen van de radiochip, in dBm | `set tx <dBm>` |
| Positie, zodat de repeater op kaarten verschijnt | `set lat <degrees>` en `set lon <degrees>` |
| Contactgegevens voor andere beheerders | `set owner.info <text>` |
| Uren tussen flood-adverts, de adverts die de hele mesh hoort | `set flood.advert.interval <hours>` |
| Nu aankondigen | `advert` |
| Herstarten | `reboot` |

Het standaard beheerderswachtwoord is `password`, en iedereen die daarmee inlogt, wordt beheerder. Wijzig het voordat de repeater de lucht in gaat.

Het voorbeeld van `set radio` hierboven is EU/UK (Narrow). Gebruik in plaats daarvan de waarden van de preset van je gebied: je vindt ze per land bij [Aanbevolen instellingen](/guides/settings/).

**De klok instellen.** Zonder klokmodule (RTC) raakt een repeater bij elke stroomuitval de tijd kwijt en start hij opnieuw in mei 2024. Terwijl hij draait, loopt zijn klok ook weg: die loopt steeds verder voor of achter. Stel de klok daarom af en toe in: log op afstand in vanuit de app en gebruik `clock sync`, of stel de tijd in via USB. Met een RTC-module hoeft dat zelden: die houdt de tijd bij tijdens stroomuitval en loopt veel minder weg.

**Op afstand beheren.** Zodra de repeater op de mesh zit, log je vanuit de MeshCore-app in met het beheerderswachtwoord. Daar lees je zijn status af en gebruik je dezelfde commando's via de radio. Sommige commando's werken alleen via USB, zoals `set freq` en de fabrieksreset `erase`.

**De identiteit bewaren.** Typ vóór een erase `get prv.key` via USB en bewaar de getoonde privésleutel op een veilige plek. Na de erase geef je de repeater zijn oude identiteit terug met `set prv.key <key>` en een `reboot`. Nodes die hem kennen, vinden hem dan onder hetzelfde prefix.

De volledige lijst met commando's staat in de [MeshCore CLI-referentie](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Update hem draadloos {#update}

Zodra de repeater hoog hangt, update je hem vanaf de grond. Log vanuit de MeshCore-app in met het beheerderswachtwoord, open de opdrachtregel en typ `start ota`. Wat er daarna gebeurt, hangt af van het board. Andere boards antwoorden `Error`, en die update je via USB.

**nRF52-boards**, zoals RAK, Heltec T114, Seeed XIAO en SenseCAP Solar:

1. Download via de [webflasher](https://flasher.meshcore.io) de **ZIP** van de nieuwe firmware voor je board.
2. Typ `start ota`. De repeater antwoordt `OK` en verschijnt via Bluetooth als `<board>_OTA`, bijvoorbeeld `RAK4631_OTA`.
3. Open de app nRF Device Firmware Update op je telefoon, kies de ZIP en de repeater, en start het uploaden. Dat duurt een paar minuten.

Installeer de [OTAFIX-bootloader](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX) op een nRF52-board voordat je het ophangt. Met de standaardbootloader kun je een mislukte update alleen via USB herstellen. Met OTAFIX valt het board terug op de updatemodus, en probeer je het opnieuw via Bluetooth.

**ESP32-boards**, zoals de Heltec V3 en V4:

1. Download via de webflasher de **niet-samengevoegde** `.bin` voor je board: het bestand zonder "merged" in de naam.
2. Typ `start ota`. De repeater opent een WiFi-netwerk met de naam `MeshCore-OTA` en antwoordt met het adres van zijn uploadpagina.
3. Verbind binnen WiFi-bereik je telefoon of laptop met dat netwerk, open het adres en upload het bestand.

## Wettelijke grenzen {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
De Europese presets van MeshCore liggen in de subband **869.40-869.65 MHz**. In de EU, het Verenigd Koninkrijk, Zwitserland en Noorwegen mogen apparaten met een kort bereik deze subband zonder licentie gebruiken, binnen deze grenzen:

- maximaal **500 mW e.r.p.** uitgestraald vermogen;
- maximaal **10% duty cycle**: per apparaat niet meer dan 360 seconden zenden in elk uur. Een apparaat mag in plaats daarvan listen-before-talk met adaptive frequency agility gebruiken, zoals gedefinieerd in ETSI EN 300 220-2;
- het hele signaal, maximaal 250 kHz breed, moet binnen de subband blijven.

Je deelt de band met anderen: je mag vergunde diensten niet storen, en anderen mogen jou storen.
De radio moet een CE-markering hebben (in Groot-Brittannië CE of UKCA).
{{< /callout >}}

Bronnen: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845), bijlage 1, band h1.7; [Beschikking 2006/771/EG van de Commissie](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) en de wijzigingen daarvan; [ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), band O.

### Vermogen: e.r.p. en je antenne {#erp}

De grens geldt voor het *uitgestraalde* vermogen, gemeten ten opzichte van een eenvoudige dipoolantenne (e.r.p.). Antennewinst telt mee, kabelverlies trek je ervan af. Fabrikanten geven antennewinst op in dBi, en dat is 2.15 dB meer dan dezelfde winst in dBd (ten opzichte van een dipool). Houd de uitkomst van deze som op maximaal 27 dBm (500 mW):

> zendvermogen (dBm) + antennewinst (dBi) − kabelverlies (dB) − 2.15 ≤ 27

- Een board zendt 22 dBm via 1 dB kabelverlies naar een antenne van 5 dBi: 22 + 5 − 1 − 2.15 = 23.85 dBm, ongeveer 240 mW e.r.p. Dat blijft binnen de grens.
- Een board met een versterker van 30 dBm (1 W) zendt naar een antenne van 3 dBi: 30 + 3 − 2.15 = 30.85 dBm, ongeveer 1.2 W e.r.p. Dat gaat over de grens, dus verlaag het zendvermogen.

Met `set tx` stel je het uitgangsvermogen van de LoRa-chip in, in dBm. De SX1262-chip zelf haalt maximaal 22 dBm, en de firmware controleert het ingevoerde getal niet. Boards met een extra versterker, zoals de Heltec V4 of de Station G2, zenden veel meer dan het getal dat je instelt. Bekijk de tabel van de fabrikant voordat je het instelt, en begin laag.

### Duty cycle {#duty-cycle}

Een repeater zendt voor iedereen in de omgeving, dus hij verbruikt zijn zendtijd sneller dan een companion. De duty-cycle-limiter van MeshCore staat standaard op 50%, en dat is meer dan deze band toestaat. Stel hem op elke repeater in op 10%:

```text
set dutycycle 10
```

### Frequentienauwkeurigheid {#frequency}

Het kanaal EU/UK (Narrow), 869.618 MHz met 62.5 kHz bandbreedte, loopt door tot 869.649 MHz: minder dan 1 kHz onder de bovenkant van de subband. Het signaal moet bij elke temperatuur binnen de band blijven. Daarvoor is een temperatuurgecompenseerd kristal (TCXO) nodig. Bijna elk huidig board heeft er een. Oudere boards zonder TCXO, zoals de Heltec V2, lopen in frequentie te ver weg om betrouwbaar op 62.5 kHz te werken.

### Opmerkingen per land {#countries}

- **EU-lidstaten** moeten deze subband onder deze voorwaarden beschikbaar stellen (Beschikking 2006/771/EG, artikel 3).
- **Verenigd Koninkrijk:** dezelfde grenzen, in Ofcom [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Zwitserland en Liechtenstein:** dezelfde grenzen, in OFCOM [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Noorwegen:** dezelfde grenzen, in de [regeling voor algemene machtigingen](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Deze opmerkingen zijn geen juridisch advies. Regels veranderen. Vraag bij twijfel je nationale toezichthouder om uitsluitsel.

## Checklist voor de plaatsing {#checklist}

- [ ] De eigenaar van de locatie heeft ingestemd, en je kunt voor onderhoud bij de repeater komen.
- [ ] Op het board draait de **Repeater**-firmware, en je hebt de antenne aangesloten vóór de eerste keer inschakelen.
- [ ] Je hebt het beheerderswachtwoord gewijzigd.
- [ ] De radio komt overeen met [de preset van je gebied](/guides/settings/) (`get radio`).
- [ ] Je hebt `set dutycycle 10` ingesteld.
- [ ] Zendvermogen plus antennewinst blijft binnen 500 mW e.r.p.
- [ ] Je hebt de naam, positie en `owner.info` ingesteld, zodat anderen weten wie de repeater beheert.
- [ ] Je hebt de klok ingesteld (`clock`).
- [ ] De behuizing is afgedicht, met een afvoer- of ventilatiegaatje, en de kabel heeft een druppellus.
- [ ] Accu en paneel zijn berekend op de slechtste wintermaand.
- [ ] Je hebt de repeater op afstand getest met de app voordat je de locatie verliet.
- [ ] Je lokale groep weet dat de repeater actief is.
