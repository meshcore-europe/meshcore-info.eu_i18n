---
title: Vad är MeshCore?
lead: MeshCore skickar textmeddelanden via radio, från nod till nod. Det fungerar utan internet och utan abonnemang.
description: 'Vad MeshCore är och inte är: nodtyper, routing, kryptering och 868 MHz-bandet.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '2a40da22'
  seeded: '2026-11-04'
  fields: {title: '06eda66b', lead: 'c0174569', description: 'c2255f49', eyebrow: '8610c822'}
  sections: ['aa768ac3', '92fc3ea7', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '203a07ef', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'ac039316', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '5d796ffb', '1a490368', 'f0dd237f', '3182d5c8', '02f1fe2f', 'e6b5b258']
---

MeshCore är fri programvara för små LoRa-radioapparater. LoRa är en radioteknik
som skickar små mängder data långt, med mycket lite ström. En radio med MeshCore
kallas en *nod*. Du kopplar den till appen i din telefon eller dator, eller
använder dess egen skärm och tangentbord. Då kan du skicka text till folk flera kilometer bort. Det finns ingen mast, router eller operatör emellan.

Programvaran har öppen källkod och utvecklas på
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) under
MIT-licensen.

## Vad MeshCore inte är {#not}

Är du ny inom radio? Här är det folk oftast förväntar sig av MeshCore,
men som det inte gör.

- **Det är inte internet eller en telefon.** MeshCore skickar korta textmeddelanden,
  ungefär lika långa som ett sms på din telefon. Inga röstsamtal, bilder, video
  eller webbsidor, och du kan inte nå ett vanligt telefonnummer.
- **Det är ingen nödtjänst.** Ingen nödtjänst lovar att lyssna på meshen,
  och ingen lovar att någon läser ditt meddelande.
- **Det är inte omedelbart, och det finns inte överallt.** Ett meddelande hoppar
  från radio till radio och kan ta några sekunder, eller aldrig komma fram. Om det
  går fram beror på repeatrarna runt dig, på höjd, byggnader och din antenn.
  En liten radio inomhus når ofta ingen. En repeater på ett tak når flera kilometer.
- **Det är ingen tjänst som någon driver åt dig.** Det finns ingen leverantör,
  ingen support och inget löfte om täckning. Meshen finns där folk i
  gemenskapen har satt upp repeatrar.
- **Inte allt i meshen är privat.** Direktmeddelanden är krypterade, men alla kan
  läsa Public och hashtag-kanalerna. Alla inom räckhåll ser din nods namn och
  den position du delar. [Observers](/network/) rapporterar det de hör till
  offentliga kartor. [Avsnittet om kryptering](#encryption) förklarar vad som
  förblir privat.
- **Det är inte obegränsat.** Alla i ett område delar en radiokanal, och
  reglerna för [868 MHz-bandet](#band) begränsar hur länge varje radio får sända.
  Varje meddelande tar sändningstid från alla andra. Därför gör bottar, täta adverts
  och testmeddelanden meshen långsammare för alla.
- **Det är inte Meshtastic.** Meshtastic är ett annat system som körs på
  ungefär samma kort. De två kan inte prata med varandra.

## Meshen på en minut {#mesh}

En LoRa-radio når några kilometer i en stad, och mycket längre från en kulle
eller ett tak. För att nå längre skickar radioapparaterna meddelanden vidare åt
varandra: det är en *mesh*. I MeshCore är det radioapparater som kallas
*repeatrar* som skickar vidare. En repeater som hör ett meddelande skickar det igen. Så kan
meddelandet korsa en hel region.

Ingen äger meshen. Varje nod och varje repeater tillhör någon i gemenskapen.
Meshen når så långt som deras repeatrar når.

## 3 typer av noder {#roles}

Du väljer nodens typ när du flashar den. Din första nod är en companion.

**Companion.** Din egen radio. Du parkopplar den med MeshCore-appen i
telefonen eller datorn via Bluetooth eller USB. Vissa har egen skärm och eget
tangentbord. I appen läser och skriver du. Companion-noden sparar dina kontakter och
kanaler, och de meddelanden som kom medan appen inte var ansluten. En companion skickar inte vidare meddelanden åt andra.

**Repeater.** En radio som står högt och skickar vidare meddelanden åt alla.
De flesta drivs med solkraft. Du behöver bara en egen där meshen inte når
ännu. Den har ingen egen app. Du ställer in den via USB, eller
loggar in med ett lösenord och sköter den via radion. I
[repeaterguiden](/repeater-guide/) ser du hur.

**Room server.** En liten anslagstavla på meshen. När du loggar in får du
inläggen du missade medan du var utom räckhåll, upp till de senaste 32. Den
sparar dem bara i minnet, så en omstart eller ett strömavbrott raderar dem.
En lokal grupp använder en sådan för tillkännagivanden.

## Så hittar ett meddelande fram {#routing}

Varje nod har en hemlig nyckel och en offentlig nyckel. Den offentliga nyckeln är dess identitet. En nod
presenterar sig med en *advert*: ett signerat paket med dess namn och, om du
vill, dess position. Någon dyker upp bland dina kontakter när en av deras
adverts har nått dig, eller när du skannar deras QR-kod. I appen finns en knapp för att skicka din egen.

Ditt första meddelande till en kontakt går ut som *flood*. Varje repeater som
hör det skickar det vidare en gång och lägger till sitt eget korta ID på vägen.
Svaret tar med sig listan med ID:n tillbaka. Därefter följer dina meddelanden
till den kontakten den sparade vägen, och bara repeatrarna längs den sänder.
När vägen bryts skickar appen som flood igen.

Meddelanden till en kanal har ingen enskild adress, så de skickas alltid som flood.
Repeatrar minns vad de nyligen skickat vidare och kastar kopior som kommer
igen via en annan väg. Ett meddelande kan passera upp till 64 repeatrar, eller 32 där förinställningen använder ID:n på 2 byte.

## Kryptering och integritet {#encryption}

Dina direktmeddelanden är krypterade från ände till ände: bara du och den
andra personen kan läsa dem. Av mottagaren ser en repeater bara en ledtråd
på 1 byte.

Kanaler krypteras med en delad nyckel. Vem som kan läsa dem beror alltså på
vem som har nyckeln:

- **Public** finns på varje companion. Nyckeln är publicerad, så vem som
  helst kan läsa kanalen.
- **Hashtag-kanaler**, som `#utrecht`, får sin nyckel från sitt namn. Alla
  som känner till namnet kan gå med, så se dem också som offentliga.
- **Privata kanaler** använder en slumpmässig nyckel som du delar själv,
  till exempel som en QR-kod.

Adverts är signerade men inte krypterade. Alla inom räckhåll ser din nods
namn, och dess position om du delar den. Välj ett namn som inte avslöjar mer
än du vill.

## 868 MHz-bandet i Europa {#band}

I Europa använder MeshCore en liten del av 868 MHz-bandet, som vem som helst
får använda utan licens. Den europeiska radioförinställningen, EU/UK (Narrow),
ligger på 869.618 MHz med en kanal på 62.5 kHz. Det ligger inom delbandet
869.40-869.65 MHz, som tillåter upp till 500 mW e.r.p. En enhet får sända där
högst 10% av tiden. I
[den juridiska delen av repeaterguiden](/repeater-guide/#legal) hittar du
detaljerna och gränserna per land.

Alla i ett område använder samma förinställning, annars kan deras radioapparater
inte höra varandra. Vissa länder och regioner använder en variant: din
[lokala grupp](/community/) vet vilken.

## Vad folk använder det till {#uses}

- Hålla kontakten på vandringar, till sjöss och på festivaler där mobilnätet
  är överbelastat eller saknas.
- En reservkanal för familj eller grannar när ström eller mobilnät
  slutar fungera.
- En reserv för lokala myndigheter när deras vanliga nät slutar fungera.
- Lokal chatt på radioapparater som folk äger själva.
- Hålla ett sök- och räddningsteam i kontakt där det inte finns något mobilnät.
  MeshCore SAR, en app från communityn under [Projekt](/projects/), lägger till kartor och
  delade positioner.
- Kontrollera en avlägsen plats hemifrån. Repeatrar och sensornoder rapporterar sin
  batterispänning och andra mätvärden när du frågar.
- Övervaka en sensor. En sensornod kör MeshCores firmware för att mäta
  saker. Den sparar en historik över sin batterispänning. Logga in som admin så
  varnar den dig när batteriet börjar ta slut. Varningar för andra mätvärden lägger
  du till med egen kod.
- Slå på eller av något långt bort, till exempel en pump. Det lägger du till i
  sensorns firmware med egen kod.
- Experimentera med radio, antenner, solkraft och programvara med öppen källkod.

Vissa myndigheter bygger eller testar en reservlösning på MeshCore. Vi kontrollerade
de här exemplen i november 2026.

- Cyklonen Gabrielle slog ut all kommunikation i Tairāwhiti, Nya Zeeland. I
  september 2025 pekade regionens krisberedskap ut MeshCore som
  [ett av minst 6 reservalternativ för kommunikation](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Krisberedskapen höll också på att bygga solcellsdrivna repeatrar som stomme.
- Det tyska distriktet Bad Kissingen
  [bygger ett textnät på MeshCore](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  för myndigheter, räddningstjänst och samhällsviktiga platser. Brandstationerna
  ansluts först.
- Kommunfullmäktige i Hilversum, i Nederländerna,
  [röstade 34 mot 1 för ett försök](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  med en repeater i stadshustornet. Kommunen
  [utvärderar försöket hösten 2027](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Två nederländska säkerhetsregioner, som organiserar insatsen vid en kris,
  testar MeshCore:
  [Södra Limburg](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  och [Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Enligt Drenthe är det för tidigt att säga hur eller när regionen kan använda det.
- I Dalfsen, också i Nederländerna,
  [driver frivilliga ett pilotprojekt tillsammans med kommunerna](https://noodnetoverijssel.nl/).
  De använder röstradio i första hand och MeshCore som ett andra lager för text.

Ingen lovar att någon i meshen nära dig läser ditt meddelande.

## Var datan kommer ifrån {#data}

Sökningen på sidan [lokala grupper](/community/) hittar en plats med hjälp av
en kopia av de fria ort- och postnummerlistorna från
[GeoNames](https://www.geonames.org/), licensierade under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopian finns på
den här webbplatsen. Din sökning lämnar aldrig din enhet, och ingen förfrågan
går till GeoNames.
