---
title: Repeater-gids
lead: Een hoog geplaatste repeater geeft berichten door voor iedereen in de omgeving, over een hele stad of een heel dal. Kies een plek, voed hem met zonne-energie, stel hem in en blijf binnen de wet.
description: 'Plan, voed, configureer en gebruik een MeshCore-repeater legaal in Europa: plekkeuze, zonnepaneel berekenen, CLI-instellingen, vermogens- en duty-cycle-limieten op 868 MHz.'
eyebrow: 868 MHz · tot 500 mW · zonder vergunning
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '4a0fe39f'
  seeded: '2026-10-26'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['1de4a4f7', '766086be', '70faf508', '8bc641aa', '2018aa04', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
---

Repeaters dragen de mesh. Companions, de radio's waarmee je berichten stuurt, geven berichten niet door. Zonder repeaters bereik je dus alleen mensen binnen direct bereik. Elke repeater die je plaatst, vergroot de mesh voor iedereen in de omgeving. Deze gids volgt MeshCore-firmware v1.18.0.

Praat eerst met je [lokale groep](/community/) voordat je begint. Zij weten waar dekking ontbreekt, welke [preset jouw regio gebruikt](/guides/settings/) en hoe je repeaters een naam geeft. Bekijk op de [dekkingskaarten](/map/) welke repeaters bij jou in de buurt staan. Zeg hallo op de openbare of lokale [kanalen](/guides/channels/).

## Kies een plek {#site}

Hoogte wint het van vermogen. LoRa op 868 MHz reist het best langs een vrije zichtlijn. Heuvels, gebouwen en dicht bos kosten veel meer bereik dan een paar extra milliwatt terugwinnen.

- **Ga hoog.** Een dak, een mast, een hoog gebouw of een heuvel dekt veel meer dan een vensterbank. Zelfs een paar meter boven de omliggende daken helpt al.
- **Houd de antenne vrij.** Monteer hem boven dakranden, weg van metaal, dakgoten en andere antennes.
- **Controleer het uitzicht.** Met tools zoals [HeyWhatsThat](https://www.heywhatsthat.com/) zie je wat vanaf een locatie zichtbaar is. Kun je een plek zien, dan is een repeater daar bereikbaar.
- **Houd ruimte vrij.** Een radiopad heeft wat vrije ruimte rond de rechte lijn nodig, niet alleen de lijn zelf. Over lange afstanden moet het midden van het pad obstakels met enkele meters vrijhouden.
- **Vraag toestemming.** Vraag de eigenaar van het dak of de mast om toestemming. Spreek af hoe je bij de repeater komt voor onderhoud.

## Hardware {#hardware}

- **Board.** Kies een zuinig nRF52-board zoals de [Heltec T114](/devices/), RAK WisBlock of de SenseCAP Solar Node. ESP32-boards verbruiken meer stroom (de apparatenpagina markeert ze als Hoog), wat werken op zonne-energie lastig maakt.
- **Antenne.** Gebruik een antenne voor 868 MHz en monteer hem verticaal. De [antennegids](/guides/antenna/) behandelt types, connectors, kabel en montage. Antennewinst telt mee voor de wettelijke vermogenslimiet; zie [Wettelijke limieten](#legal).
- **Kabel.** Houd coaxkabel kort of gebruik kabel met lage demping. Op 868 MHz kan een paar meter dunne kabel de helft van je vermogen verliezen.
- **Behuizing.** Een weerbestendige kast (IP65 of beter) met een kabelwartel, een ventilatie- of afvoergat tegen condens, en een lichte kleur of zonnescherm. Accu's lijden onder hitte en laden niet onder het vriespunt.
- **Bliksem.** Een antenne op een dak is een doelwit. Volg de lokale regels voor aarding, of monteer hem waar een inslag de bedrading van het gebouw niet bereikt.

## Voeding en zonnepaneel berekenen {#power}

Een repeater op zonne-energie moet de donkerste winterweken overleven. Reken daarop:

1. **Meet het verbruik.** Laat de geconfigureerde repeater een dag via een USB-vermogensmeter draaien. Lees de gebruikte energie af in wattuur (Wh). Het verkeer in jouw regio beïnvloedt dit getal, dus meet als het kan ter plekke.
2. **Voeg reserve toe.** Plan accucapaciteit voor minstens 5 tot 7 dagen zonder bruikbare zon.
3. **Zoek je winterzon op.** De gratis [PVGIS-tool](https://re.jrc.ec.europa.eu/pvg_tools/en/) van de EU toont voor elke locatie hoeveel energie een paneel per maand opwekt. Gebruik de maand met de minste zon.
4. **Bereken het paneel.** Het paneel moet in die slechtste maand het dagelijkse verbruik aanvullen, met marge voor laadverliezen.

Een rekenvoorbeeld met aangenomen getallen: een repeater die 1 Wh per dag verbruikt, heeft een accu van minstens 7 Wh nodig voor een week reserve, ongeveer 2 Ah bruikbare capaciteit bij 3,7 V. Zegt PVGIS dat een paneel van 1 W op jouw plek in december 0,5 Wh per dag levert, dan heb je minstens een paneel van 2 W nodig. Met 3 tot 5 W houd je marge voor wolken, sneeuw en veroudering.

## Stel hem in {#config}

**Flashen.** Gebruik de [webflasher](https://flasher.meshcore.io) en kies de **Repeater**-firmware voor jouw board. Zie [Aan de slag](/get-started/#flash) voor de stappen van het flashen.

**Configureren via USB.** Open, met de repeater nog aan je computer, [config.meshcore.io](https://config.meshcore.io) of de console van de flasher. Je kunt ook elke seriële terminal op 115200 baud gebruiken. De belangrijkste commando's:

| Wat | Commando |
|---|---|
| Het admin-wachtwoord wijzigen | `password <new password>` |
| Een naam geven | `set name <name>` |
| Radio-preset: frequentie, bandbreedte, SF, CR (herstart om toe te passen) | `set radio 869.618,62.5,8,8` |
| Duty-cycle-limiet, in procent | `set dutycycle 10` |
| Zendvermogen van de radiochip, in dBm | `set tx <dBm>` |
| Positie, zodat hij op kaarten verschijnt | `set lat <degrees>` en `set lon <degrees>` |
| Contactgegevens voor andere beheerders | `set owner.info <text>` |
| Uren tussen flood-advertenties, die de hele mesh hoort | `set flood.advert.interval <hours>` |
| Nu aankondigen | `advert` |
| Herstarten | `reboot` |

Het standaard admin-wachtwoord is `password`, en iedereen die daarmee inlogt wordt admin. Wijzig het voordat de repeater in de lucht gaat.

Het voorbeeld van `set radio` hierboven is EU/UK (Narrow). Gebruik in plaats daarvan de waarden van de preset van jouw regio: [Aanbevolen instellingen](/guides/settings/) somt ze per land op.

**Stel de klok in.** Zonder klokmodule (RTC) verliest een repeater bij elke stroomuitval de tijd en start hij opnieuw in mei 2024. Terwijl hij draait, loopt zijn klok af. Log op afstand in vanuit de app en gebruik `clock sync`, of stel de tijd in via USB. Een RTC-module is een nuttige uitbreiding voor een repeater: hij houdt de tijd bij tijdens stroomuitval en loopt veel minder af.

**Beheer hem op afstand.** Zodra hij in de mesh zit, log je in vanuit de MeshCore-app met het admin-wachtwoord. Daar lees je zijn status en gebruik je dezelfde commando's via de radio. Sommige commando's werken alleen via USB, zoals `set freq` en de fabrieksreset `erase`.

De volledige lijst met commando's staat in de [MeshCore CLI-referentie](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Wettelijke limieten {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
De Europese presets van MeshCore liggen in de subband **869.40-869.65 MHz**. In de
EU, het VK, Zwitserland en Noorwegen is die zonder vergunning open voor
apparaten met kort bereik, binnen deze limieten:

- hoogstens **500 mW e.r.p.** uitgestraald vermogen;
- hoogstens **10% duty cycle**: niet meer dan 360 seconden zenden in
  elk uur, per apparaat. Een apparaat mag ook listen-before-talk gebruiken
  met adaptive frequency agility zoals gedefinieerd in ETSI EN 300 220-2;
- het hele signaal, hoogstens 250 kHz breed, moet binnen de subband blijven.

De band is gedeeld: je mag vergunde diensten niet storen, en anderen mogen
jou storen.
De radio moet CE-gemarkeerd zijn (in Groot-Brittannië CE of UKCA).
{{< /callout >}}

Bronnen: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
Annex 1, band h1.7;
[Beschikking 2006/771/EG van de Commissie](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
en de wijzigingen daarvan;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
band O.

### Vermogen: e.r.p. en je antenne {#erp}

De limiet geldt voor het *uitgestraalde* vermogen, gemeten ten opzichte van een eenvoudige dipoolantenne (e.r.p.). Antennewinst telt mee; kabeldemping trek je af. Fabrikanten geven antennewinst op in dBi, en dat is 2.15 dB meer dan dezelfde winst in dBd (ten opzichte van een dipool). Houd deze som op of onder 27 dBm (500 mW):

> zendvermogen (dBm) + antennewinst (dBi) − kabeldemping (dB) − 2.15 ≤ 27

- Een board dat 22 dBm zendt in een antenne van 5 dBi via 1 dB kabel: 22 + 5 − 1 − 2.15 = 23.85 dBm, ongeveer 240 mW e.r.p. Binnen de limiet.
- Een board met een versterker van 30 dBm (1 W) in een antenne van 3 dBi: 30 + 3 − 2.15 = 30.85 dBm, ongeveer 1.2 W e.r.p. Boven de limiet; verlaag het zendvermogen.

`set tx` stelt het uitgangsvermogen van de LoRa-chip in, in dBm. De SX1262-chip zelf komt niet hoger dan 22 dBm; de firmware controleert het getal dat je invoert niet. Boards met een extra versterker, zoals de Heltec V4 of de Station G2, zenden veel meer dan het getal dat je instelt. Bekijk de tabel van de fabrikant voordat je het instelt, en begin laag.

### Duty cycle {#duty-cycle}

Een repeater zendt voor iedereen in de omgeving en verbruikt zijn zendtijd dus sneller dan een companion. De duty-cycle-begrenzer van MeshCore staat standaard op 50%, en dat is meer dan deze band toestaat. Zet hem op elke repeater op 10%:

```text
set dutycycle 10
```

### Frequentienauwkeurigheid {#frequency}

Het kanaal EU/UK (Narrow), 869.618 MHz met 62.5 kHz bandbreedte, reikt tot 869.649 MHz: minder dan 1 kHz onder de bovengrens van de subband. Het signaal moet bij elke temperatuur binnen de band blijven. Daarvoor is een temperatuurgecompenseerd kristal (TCXO) nodig. Bijna elk huidig board heeft er een. Oudere boards zonder, zoals de Heltec V2, drijven te ver af om betrouwbaar op 62.5 kHz te werken.

### Opmerkingen per land {#countries}

- **EU-lidstaten** moeten deze subband onder deze voorwaarden beschikbaar stellen (Beschikking 2006/771/EG, artikel 3).
- **Verenigd Koninkrijk:** dezelfde limieten, in Ofcom [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Zwitserland en Liechtenstein:** dezelfde limieten, in OFCOM [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Noorwegen:** dezelfde limieten, in de [verordening over algemene machtigingen](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Deze opmerkingen zijn geen juridisch advies. Regels veranderen; raadpleeg bij twijfel je nationale toezichthouder.

## Checklist voor plaatsing {#checklist}

- [ ] De eigenaar van de plek is akkoord, en je kunt bij de repeater voor onderhoud.
- [ ] Het board draait de **Repeater**-firmware, en de antenne zat erop voordat je hem voor het eerst inschakelde.
- [ ] Het admin-wachtwoord is gewijzigd.
- [ ] De radio komt overeen met [de preset van jouw regio](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` is ingesteld.
- [ ] Zendvermogen plus antennewinst blijft binnen 500 mW e.r.p.
- [ ] De naam, positie en `owner.info` zijn ingesteld, zodat anderen weten wie hem beheert.
- [ ] De klok is ingesteld (`clock`).
- [ ] De behuizing is afgedicht, met een afvoer- of ventilatiegat, en de kabel heeft een druiplus.
- [ ] Accu en paneel zijn berekend op de slechtste wintermaand.
- [ ] Je hebt hem met de app vanaf afstand getest voordat je de plek verliet.
- [ ] Je lokale groep weet dat hij in de lucht is.
