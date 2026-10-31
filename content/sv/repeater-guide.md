---
title: Guide för repeatrar
lead: En högt placerad repeater skickar vidare meddelanden åt alla runt omkring, över en hel stad eller dal. Välj en plats, driv den med solenergi, ställ in den och håll dig inom lagen.
description: 'Planera, driv, konfigurera och använd en MeshCore-repeater lagligt i Europa: val av plats, dimensionering av solpanel, CLI-inställningar, effekt och sändningstid på 868 MHz.'
eyebrow: 868 MHz · upp till 500 mW · licensfritt
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-10-31'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Repeatrar bär upp meshen. Companions, radiorna du skickar meddelanden från, skickar inte
vidare meddelanden. Utan repeatrar når du därför bara dem som är inom direkt räckvidd.
En repeater på rätt plats utökar meshen för alla runt omkring. Guiden utgår från
MeshCore firmware v1.18.0.

Prata med din [lokala grupp](/community/) innan du börjar. De vet var
täckning saknas, vilken [preset ditt område använder](/guides/settings/) och hur repeatrar ska namnges. Leta efter repeatrar nära dig på
[täckningskartorna](/map/), och säg hej i de publika
eller lokala [kanalerna](/guides/channels/).

## Behöver du en? {#need}

En repeater skickar vidare varje flood-meddelande den hör. Alla repeatrar inom
räckvidd delar på samma sändningstid. Där meshen redan når dig ger ytterligare en
repeater mer trafik och ingen ny täckning. Ofta räcker en högt placerad companion,
i ett vindsfönster eller på en balkong.

Sätt upp en repeater där täckning saknas:

- [täckningskartorna](/map/) visar ingen repeater nära dig, eller bara sådana som din
  companion inte hör;
- din lokala grupp säger att området behöver en.

## Välj plats {#site}

Höjd slår effekt. LoRa på 868 MHz når längst med fri sikt.
Kullar, byggnader och tät skog tar mycket mer räckvidd än några extra
milliwatt ger tillbaka.

- **Gå högt.** Ett tak, en mast, en hög byggnad eller en kulle täcker mycket mer
  än en fönsterbräda. Redan några meter över omgivande tak hjälper.
- **Håll antennen fri.** Montera den ovanför takkanter, på avstånd från
  metall, hängrännor och andra antenner.
- **Kontrollera sikten.** Med verktyg som [HeyWhatsThat](https://www.heywhatsthat.com/)
  ser du vad som syns från en plats. Kan du se en punkt, så når du en repeater
  där.
- **Lämna fritt utrymme.** En radioväg behöver lite fritt utrymme runt den raka
  linjen, inte bara själva linjen. Över långa avstånd bör mitten av vägen
  gå flera meter över hindren.
- **Be om lov.** Skaffa ägarens samtycke till taket eller masten, och kom överens om
  hur du kommer åt repeatern för underhåll.

## Hårdvara {#hardware}

- **Kort.** Välj ett strömsnålt nRF52-kort, till exempel
  [Heltec T114](/devices/), RAK WisBlock eller SenseCAP Solar Node. ESP32-kort
  drar mer ström (enhetssidan märker dem med High), och då blir solcellsdrift svår.
- **Antenn.** Använd en antenn avsedd för 868 MHz och montera den lodrätt.
  [Antennguiden](/guides/antenna/) tar upp typer, kontakter, kabel och
  montering. Antennförstärkningen räknas in i den lagliga effektgränsen, se
  [Lagliga gränser](#legal).
- **Kabel.** Håll koaxialkabeln kort, eller använd kabel med låg förlust. På 868 MHz kan några
  meter tunn kabel kosta hälften av effekten.
- **Kapsling.** En väderskyddad låda (IP65 eller bättre) med kabelgenomföring, ett
  ventilations- eller dräneringshål mot kondens och ljus färg eller solskydd.
  Batterier tar skada av värme och kan inte laddas under fryspunkten.
- **Åska.** En antenn på ett tak är ett mål. Följ lokala regler för
  jordning, eller montera den där ett nedslag inte når byggnadens
  elinstallation.

## Ström och dimensionering av solpanel {#power}

En solcellsdriven repeater måste klara vinterns mörkaste veckor. Dimensionera den
efter dem:

1. **Mät förbrukningen.** Kör den konfigurerade repeatern genom en USB-effektmätare
   i ett dygn. Läs av energin i wattimmar (Wh). Trafiken i
   ditt område påverkar värdet, så mät på plats om du kan.
2. **Lägg till reserv.** Planera batterikapacitet för minst 5 till 7 dagar
   utan användbar sol.
3. **Ta reda på vintersolen.** EU:s kostnadsfria
   [PVGIS-verktyg](https://re.jrc.ec.europa.eu/pvg_tools/en/) visar för valfri
   plats hur mycket energi en panel ger per månad. Utgå från månaden med
   minst sol.
4. **Dimensionera panelen.** Panelen måste ersätta varje dags förbrukning under den sämsta
   månaden, med marginal för laddningsförluster.

Ett räkneexempel med antagna värden: en repeater som förbrukar 1 Wh per dygn
behöver ett batteri på minst 7 Wh för en veckas reserv, ungefär 2 Ah
användbar kapacitet vid 3.7 V. Om PVGIS visar att en 1 W-panel på din plats ger
0.5 Wh per dygn i december, behöver du minst en 2 W-panel. Med 3 till 5 W
får du marginal för moln, snö och åldrande.

## Ställ in den {#config}

**Flasha.** Använd [webbflashern](https://flasher.meshcore.io) och välj
firmwaren **Repeater** för ditt kort. Stegen för flashning hittar du i
[Kom igång](/get-started/#flash).

**Konfigurera via USB.** Låt repeatern vara ansluten till datorn och
öppna [config.meshcore.io](https://config.meshcore.io) eller flasherns
konsol. Du kan också använda valfri seriell terminal på 115200 baud. De
viktigaste kommandona:

| Vad | Kommando |
|---|---|
| Byt adminlösenord | `password <new password>` |
| Ge den ett namn | `set name <name>` |
| Radiopreset: frekvens, bandbredd, SF, CR (gäller efter omstart) | `set radio 869.618,62.5,8,8` |
| Gräns för sändningstid, i procent | `set dutycycle 10` |
| Radiochipets sändeffekt, i dBm | `set tx <dBm>` |
| Position, så att den syns på kartor | `set lat <degrees>` och `set lon <degrees>` |
| Kontaktuppgifter för andra operatörer | `set owner.info <text>` |
| Timmar mellan flood-adverts, de som hela meshen hör | `set flood.advert.interval <hours>` |
| Annonsera den nu | `advert` |
| Starta om | `reboot` |

Standardlösenordet för admin är `password`, och den som loggar in med det
blir admin. Byt det innan repeatern börjar sända.

Exemplet med `set radio` ovan är EU/UK (Narrow). Använd i stället värdena för ditt
områdes preset: [Rekommenderade inställningar](/guides/settings/) listar dem
per land.

**Ställ klockan.** Utan klockmodul (RTC) tappar en repeater tiden vid
varje strömavbrott och startar om i maj 2024. Medan den är igång driver
klockan dessutom: den går allt mer före eller efter. Ställ därför klockan då och då. Logga
in på distans från appen och använd `clock sync`, eller ställ tiden via USB. Med
en RTC-modul behöver du sällan göra det: den behåller tiden vid strömavbrott och
driver mycket mindre.

**Hantera den på distans.** När den finns på meshen loggar du in från MeshCore-appen
med adminlösenordet. Där läser du av dess status och använder samma kommandon
via radio. Vissa kommandon fungerar bara via USB, till exempel `set freq` och
fabriksåterställningen `erase`.

**Behåll identiteten.** Skriv `get prv.key` via USB före en erase, och spara
den privata nyckel som visas på ett säkert ställe. Efter erase ger `set prv.key <key>`
och en `reboot` repeatern tillbaka dess gamla identitet. Noder som känner till
den hittar den då under samma prefix.

Hela kommandolistan finns i
[MeshCore CLI-referensen](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Uppdatera den trådlöst {#update}

När repeatern sitter högt upp uppdaterar du den från marken. Logga in från
MeshCore-appen med adminlösenordet, öppna dess kommandorad och skriv
`start ota`. Vad som händer sedan beror på kortet. Andra kort svarar `Error`,
och dem uppdaterar du via USB.

**nRF52-kort**, till exempel RAK, Heltec T114, Seeed XIAO och SenseCAP Solar:

1. Ladda ner **ZIP**-filen med den nya firmwaren för ditt kort från
   [webbflashern](https://flasher.meshcore.io).
2. Skriv `start ota`. Repeatern svarar `OK` och syns via Bluetooth
   som `<board>_OTA`, till exempel `RAK4631_OTA`.
3. Öppna appen nRF Device Firmware Update i telefonen, välj ZIP-filen och
   repeatern, och ladda upp. Det tar några minuter.

Installera [OTAFIX-bootloadern](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
på ett nRF52-kort innan du sätter upp det. Med den ursprungliga bootloadern kan en misslyckad
uppdatering bara lagas via USB. Med OTAFIX går kortet tillbaka till
uppdateringsläge, och du försöker igen via Bluetooth.

**ESP32-kort**, till exempel Heltec V3 och V4:

1. Ladda ner den **icke sammanslagna** `.bin`-filen för ditt kort från webbflashern:
   filen utan "merged" i namnet.
2. Skriv `start ota`. Repeatern öppnar ett WiFi-nätverk som heter `MeshCore-OTA`
   och svarar med adressen till sin uppladdningssida.
3. Inom WiFi-räckvidd ansluter du telefonen eller datorn till nätverket, öppnar
   adressen och laddar upp filen.

## Lagliga gränser {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
MeshCores europeiska presets ligger i delbandet **869.40-869.65 MHz**. I
EU, Storbritannien, Schweiz och Norge får kortdistansenheter använda det utan
licens, inom dessa gränser:

- högst **500 mW e.r.p.** utstrålad effekt;
- högst **10% duty cycle**: högst 360 sekunders sändning per
  timme och enhet. Alternativt får en enhet använda listen-before-talk
  med adaptive frequency agility enligt ETSI EN 300 220-2;
- hela signalen, högst 250 kHz bred, måste hålla sig inom delbandet.

Bandet är delat: du får inte störa licensierade tjänster, och andra får
störa dig.
Radion måste vara CE-märkt (i Storbritannien CE eller UKCA).
{{< /callout >}}

Källor: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
bilaga 1, band h1.7;
[kommissionens beslut 2006/771/EG](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
och dess ändringar;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
band O.

### Effekt: e.r.p. och din antenn {#erp}

Gränsen gäller den *utstrålade* effekten, mätt mot en enkel dipolantenn
(e.r.p.). Antennförstärkning räknas med, kabelförlust dras av. Tillverkare anger
antennförstärkning i dBi, vilket är 2.15 dB mer än samma förstärkning i dBd
(relativt en dipol). Håll den här summan på högst 27 dBm (500 mW):

> sändeffekt (dBm) + antennförstärkning (dBi) − kabelförlust (dB) − 2.15 ≤ 27

- Ett kort som sänder 22 dBm till en 5 dBi-antenn genom 1 dB kabel:
  22 + 5 − 1 − 2.15 = 23.85 dBm, ungefär 240 mW e.r.p. Inom gränsen.
- Ett kort med en förstärkare på 30 dBm (1 W) till en 3 dBi-antenn:
  30 + 3 − 2.15 = 30.85 dBm, ungefär 1.2 W e.r.p. Över gränsen. Sänk
  sändeffekten.

`set tx` ställer in LoRa-chipets uteffekt, i dBm. SX1262-chipet ger själv
högst 22 dBm, och firmwaren kontrollerar inte värdet du anger. Kort med en extra
förstärkare, till exempel Heltec V4 eller Station G2, sänder mycket mer än
värdet du ställer in. Kontrollera tillverkarens tabell innan du ställer in det, och
börja lågt.

### Duty cycle {#duty-cycle}

En repeater sänder åt alla runt omkring, så den förbrukar sin sändningstid snabbare
än en companion. MeshCores begränsare för duty cycle står som standard på 50%, vilket är
mer än bandet tillåter. Ställ in 10% på varje repeater:

```text
set dutycycle 10
```

### Frekvensnoggrannhet {#frequency}

Kanalen EU/UK (Narrow), 869.618 MHz med 62.5 kHz bandbredd, når upp
till 869.649 MHz: mindre än 1 kHz under delbandets övre gräns. Signalen
måste hålla sig inom bandet vid alla temperaturer. Det kräver en
temperaturkompenserad kristall (TCXO). Nästan alla aktuella kort har en.
Äldre kort utan, som Heltec V2, driver för mycket för att fungera pålitligt
på 62.5 kHz.

### Om enskilda länder {#countries}

- **EU:s medlemsstater** måste göra delbandet tillgängligt på dessa villkor
  (beslut 2006/771/EG, artikel 3).
- **Storbritannien:** samma gränser, i Ofcoms
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Schweiz och Liechtenstein:** samma gränser, i OFCOM:s
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norge:** samma gränser, i
  [föreskriften om allmänna tillstånd](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

De här noteringarna är ingen juridisk rådgivning. Regler ändras. Fråga din
nationella tillsynsmyndighet om du är osäker.

## Checklista för uppsättning {#checklist}

- [ ] Platsens ägare har sagt ja, och du kommer åt repeatern för underhåll.
- [ ] Kortet kör firmwaren **Repeater**, och antennen var ansluten
      före första start.
- [ ] Adminlösenordet är bytt.
- [ ] Radion stämmer med [ditt områdes preset](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` är inställt.
- [ ] Sändeffekt plus antennförstärkning håller sig inom 500 mW e.r.p.
- [ ] Namn, position och `owner.info` är inställda, så att andra vet vem som driver den.
- [ ] Klockan är ställd (`clock`).
- [ ] Kapslingen är tätad, med dränerings- eller ventilationshål, och kabeln har en
      droppslinga.
- [ ] Batteri och panel är dimensionerade för den sämsta vintermånaden.
- [ ] Du har testat den på avstånd med appen innan du lämnade platsen.
- [ ] Din lokala grupp vet att den är igång.
