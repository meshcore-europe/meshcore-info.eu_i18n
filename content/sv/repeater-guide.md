---
title: Repeaterguide
lead: En repeater som sitter högt för meddelanden vidare åt alla runt omkring, över en hel stad eller dal. Välj en plats, driv den med solenergi, ställ in den och håll dig inom lagen.
description: 'Planera, strömförsörj, konfigurera och driv en MeshCore-repeater lagligt i Europa: platsval, dimensionering av solceller, CLI-inställningar, effekt- och duty cycle-gränser på 868 MHz.'
eyebrow: 868 MHz · upp till 500 mW · licensfri
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '4a0fe39f'
  seeded: '2026-10-26'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['1de4a4f7', '766086be', '70faf508', '8bc641aa', '2018aa04', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
---

Repeatrar bär upp meshen. Companions, radiorna du skickar meddelanden från, för
inte meddelanden vidare, så utan
repeatrar når du bara dem som är inom direkt räckvidd. Varje repeater du sätter
upp utökar meshen för alla runt omkring. Den här guiden följer MeshCore
firmware v1.18.0.

Prata med din [lokala grupp](/community/) innan du börjar. De vet var
täckning saknas, vilket [preset ditt område använder](/guides/settings/) och hur repeatrar ska namnges. Titta på
[täckningskartorna](/map/) efter repeatrar nära dig, och säg hej i de publika
eller lokala [kanalerna](/guides/channels/).

## Välj en plats {#site}

Höjd slår effekt. LoRa på 868 MHz går bäst längs fri sikt.
Kullar, byggnader och tät skog kostar mycket mer räckvidd än några extra
milliwatt vinner tillbaka.

- **Sikta högt.** Ett tak, en mast, en hög byggnad eller en kulle täcker mycket mer
  än en fönsterbräda. Till och med några meter över taken runt omkring hjälper.
- **Håll antennen fri.** Montera den ovanför takkanter, på avstånd från
  metall, hängrännor och andra antenner.
- **Kontrollera utsikten.** Verktyg som [HeyWhatsThat](https://www.heywhatsthat.com/)
  visar vad som syns från en plats. Kan du se en punkt, så är en repeater
  där inom räckhåll.
- **Lämna fritt utrymme.** En radioväg behöver lite fritt utrymme runt den direkta
  linjen, inte bara själva linjen. Över långa avstånd bör mitten av vägen
  gå flera meter fritt från hinder.
- **Be om lov.** Få ägarens tillstånd för taket eller masten, och kom överens
  om hur du når repeatern för underhåll.

## Hårdvara {#hardware}

- **Kort.** Välj ett strömsnålt nRF52-kort som
  [Heltec T114](/devices/), RAK WisBlock eller SenseCAP Solar Node. ESP32-kort
  drar mer ström (enhetssidan markerar dem som Hög), vilket gör
  soldrift svår.
- **Antenn.** Använd en antenn gjord för 868 MHz, monterad vertikalt;
  [antennguiden](/guides/antenna/) tar upp typer, kontakter, kabel och
  montering. Antennförstärkningen räknas in i den lagliga effektgränsen; se
  [Lagliga gränser](#legal).
- **Kabel.** Håll koaxialkabeln kort, eller använd kabel med låg förlust. På 868 MHz kan några
  meter tunn kabel äta upp halva effekten.
- **Kapsling.** En väderskyddad låda (IP65 eller bättre) med kabelgenomföring, ett
  ventilations- eller dräneringshål mot kondens, och ljus färg eller solskydd.
  Batterier far illa i värme och kan inte laddas under nollan.
- **Blixt.** En antenn på ett tak är ett mål. Följ lokala regler för
  jordning, eller montera den där ett nedslag inte når byggnadens
  elinstallation.

## Ström och dimensionering av solceller {#power}

En solcellsdriven repeater måste klara vinterns mörkaste veckor. Dimensionera den
för dem:

1. **Mät förbrukningen.** Kör den konfigurerade repeatern genom en USB-effektmätare
   under ett dygn. Läs av förbrukad energi i wattimmar (Wh). Trafiken i
   ditt område påverkar siffran, så mät på plats om du kan.
2. **Lägg till reserv.** Planera batterikapacitet för minst 5 till 7 dygn
   utan användbar sol.
3. **Ta reda på din vintersol.** EU:s kostnadsfria
   [PVGIS-verktyg](https://re.jrc.ec.europa.eu/pvg_tools/en/) visar, för vilken
   plats som helst, hur mycket energi en panel ger per månad. Använd månaden med
   minst sol.
4. **Dimensionera panelen.** Panelen måste ersätta varje dygns förbrukning i den sämsta
   månaden, med marginal för laddningsförluster.

Ett räkneexempel, med antagna siffror: en repeater som förbrukar 1 Wh per dygn
behöver ett batteri på minst 7 Wh för en veckas reserv, ungefär 2 Ah
användbar kapacitet vid 3,7 V. Om PVGIS säger att en panel på 1 W på din plats ger
0,5 Wh per dygn i december, behöver du minst en panel på 2 W, och 3 till 5 W
ger marginal för moln, snö och åldrande.

## Ställ in den {#config}

**Flasha.** Använd [webbflashern](https://flasher.meshcore.io) och välj
**Repeater**-firmware för ditt kort. Se
[Kom igång](/get-started/#flash) för stegen vid flashning.

**Konfigurera via USB.** Med repeatern fortfarande ansluten till datorn
öppnar du [config.meshcore.io](https://config.meshcore.io) eller flasherns
konsol. Du kan också använda vilken seriell terminal som helst på 115200 baud. De
viktigaste kommandona:

| Vad | Kommando |
|---|---|
| Byt adminlösenord | `password <new password>` |
| Ge den ett namn | `set name <name>` |
| Radiopreset: frekvens, bandbredd, SF, CR (starta om för att aktivera) | `set radio 869.618,62.5,8,8` |
| Duty cycle-gräns, i procent | `set dutycycle 10` |
| Radiochippets sändeffekt, i dBm | `set tx <dBm>` |
| Position, så att den syns på kartor | `set lat <degrees>` och `set lon <degrees>` |
| Kontaktuppgifter för andra operatörer | `set owner.info <text>` |
| Timmar mellan flood-adverts, de som hela meshen hör | `set flood.advert.interval <hours>` |
| Annonsera den nu | `advert` |
| Starta om | `reboot` |

Standardlösenordet för admin är `password`, och den som loggar in med det
blir admin. Byt det innan repeatern går i luften.

Exemplet `set radio` ovan är EU/UK (Narrow). Använd i stället värdena från ditt
områdes preset: [Rekommenderade inställningar](/guides/settings/) listar dem
per land.

**Ställ klockan.** Utan klockmodul (RTC) tappar en repeater tiden vid
varje strömavbrott och startar om i maj 2024, och medan den kör driver klockan.
Logga in på distans från appen och använd `clock sync`, eller ställ tiden via USB.
En RTC-modul är ett bra tillägg för en repeater: den håller tiden
genom strömavbrott och driver betydligt mindre.

**Sköt den på distans.** När den väl är med i meshen loggar du in från MeshCore-appen
med adminlösenordet. Där läser du av dess status och använder samma kommandon
över radion. Vissa kommandon fungerar bara via USB, till exempel `set freq` och
fabriksåterställningen `erase`.

Hela kommandolistan finns i
[MeshCore CLI-referensen](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Lagliga gränser {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
MeshCores europeiska presets ligger i delbandet **869.40-869.65 MHz**. I
EU, Storbritannien, Schweiz och Norge är det öppet för kortdistansradio utan
tillstånd, inom dessa gränser:

- högst **500 mW e.r.p.** utstrålad effekt;
- högst **10 % duty cycle**: inte mer än 360 sekunders sändning under
  en timme, per enhet. Alternativt får en enhet använda listen-before-talk
  med adaptiv frekvensagilitet enligt ETSI EN 300 220-2;
- hela signalen, högst 250 kHz bred, måste hålla sig inom delbandet.

Bandet är delat: du får inte störa tillståndspliktiga tjänster, och andra kan
störa dig.
Radion måste vara CE-märkt (i Storbritannien, CE eller UKCA).
{{< /callout >}}

Källor: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
bilaga 1, band h1.7;
[kommissionens beslut 2006/771/EG](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
med ändringar;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
band O.

### Effekt: e.r.p. och din antenn {#erp}

Gränsen gäller den *utstrålade* effekten, mätt mot en enkel dipolantenn
(e.r.p.). Antennförstärkningen räknas med; kabelförlusten dras av. Tillverkare anger
antennförstärkning i dBi, vilket är 2.15 dB mer än samma förstärkning i dBd
(relativt en dipol). Håll den här summan på eller under 27 dBm (500 mW):

> sändeffekt (dBm) + antennförstärkning (dBi) − kabelförlust (dB) − 2.15 ≤ 27

- Ett kort som sänder 22 dBm in i en antenn på 5 dBi genom 1 dB kabel:
  22 + 5 − 1 − 2.15 = 23.85 dBm, ungefär 240 mW e.r.p. Inom gränsen.
- Ett kort med en förstärkare på 30 dBm (1 W) in i en antenn på 3 dBi:
  30 + 3 − 2.15 = 30.85 dBm, ungefär 1.2 W e.r.p. Över gränsen; sänk
  sändeffekten.

`set tx` ställer in LoRa-chippets uteffekt, i dBm. Själva SX1262-chippet
når som mest 22 dBm; firmware kontrollerar inte siffran du anger. Kort med en extra
förstärkare, som Heltec V4 eller Station G2, sänder mycket mer än
siffran du ställer in. Kontrollera tillverkarens tabell innan du ställer in den, och
börja lågt.

### Duty cycle {#duty-cycle}

En repeater sänder för alla runt omkring, så den förbrukar sin sändtid snabbare
än en companion. MeshCores duty cycle-begränsare har 50 % som standard, vilket är
mer än bandet tillåter. Ställ in den på 10 % på varje repeater:

```text
set dutycycle 10
```

### Frekvensnoggrannhet {#frequency}

Kanalen EU/UK (Narrow), 869.618 MHz med 62.5 kHz bandbredd, når upp till
869.649 MHz: mindre än 1 kHz under delbandets överkant. Signalen måste
hålla sig inom bandet vid varje temperatur. Det kräver en
temperaturkompenserad kristall (TCXO). Nästan alla aktuella kort har en;
äldre kort utan, som Heltec V2, driver för mycket för att fungera tillförlitligt
vid 62.5 kHz.

### Landsnoteringar {#countries}

- **EU:s medlemsstater** måste göra det här delbandet tillgängligt på dessa villkor
  (beslut 2006/771/EG, artikel 3).
- **Storbritannien:** samma gränser, i Ofcoms
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Schweiz och Liechtenstein:** samma gränser, i OFCOM:s
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norge:** samma gränser, i
  [föreskriften om allmänna tillstånd](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

De här noteringarna är inte juridisk rådgivning. Regler ändras; kontrollera med
din nationella myndighet om du är osäker.

## Checklista för driftsättning {#checklist}

- [ ] Platsens ägare har gett sitt tillstånd, och du når repeatern för underhåll.
- [ ] Kortet kör **Repeater**-firmware, och antennen sattes på
      innan första uppstarten.
- [ ] Adminlösenordet är bytt.
- [ ] Radion matchar [ditt områdes preset](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` är inställt.
- [ ] Sändeffekt plus antennförstärkning håller sig inom 500 mW e.r.p.
- [ ] Namn, position och `owner.info` är inställda, så att andra vet vem som driver den.
- [ ] Klockan är ställd (`clock`).
- [ ] Kapslingen är tät, med dränerings- eller ventilationshål, och kabeln har en
      droppslinga.
- [ ] Batteri och panel är dimensionerade för den sämsta vintermånaden.
- [ ] Du testade den på avstånd med appen innan du lämnade platsen.
- [ ] Din lokala grupp vet att den är uppe.
