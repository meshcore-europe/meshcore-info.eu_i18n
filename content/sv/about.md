---
title: Vad är MeshCore?
lead: MeshCore skickar textmeddelanden via radio, från nod till nod. Det fungerar utan internet och utan abonnemang.
description: 'Vad MeshCore är och inte är: typer av noder, routing, skillnaden mot Meshtastic, kryptering och 868 MHz-bandet.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '279b56a4'
  seeded: '2026-11-02'
  fields: {title: '06eda66b', lead: 'c0174569', description: '15e6d2a7', eyebrow: '8610c822'}
  sections: ['aa768ac3', '16fde264', '0a55792c', 'c3de803d', '493b444f', 'a8b2b9b4', '429f699c', 'f8008f48', '88af2bd3', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'fab378a5', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', 'fc8f3129', '8dec428a', '07cbac35', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '95e18f18', '02f1fe2f', 'e6b5b258']
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

- **Det är varken internet eller en telefon.** MeshCore skickar korta textmeddelanden,
  ungefär lika långa som ett sms på din telefon. Ingen röst, inga foton, ingen video
  och inga webbsidor, och du kan inte nå ett vanligt telefonnummer.
- **Det är ingen larmtjänst.** Ingen larmtjänst lyssnar på meshen,
  och ingen lovar att någon läser ditt meddelande. I en nödsituation
  ringer du 112.
- **Det är inte omedelbart, och det finns inte överallt.** Ett meddelande hoppar från radio till
  radio och kan ta några sekunder, eller aldrig komma fram. Om det kommer fram beror på
  repeatrarna omkring dig, på höjd, byggnader och din
  antenn. En liten radio inomhus når ofta ingen; en repeater på ett tak
  når flera kilometer.
- **Det är ingen tjänst som någon driver åt dig.** Det finns ingen leverantör, ingen
  kundtjänst och inget löfte om täckning. Meshen finns där folk i
  communityt har satt upp repeatrar, och ingen annanstans.
- **Allt på meshen är inte privat.** Direktmeddelanden är krypterade, men
  alla kan läsa Public och hashtagkanalerna, och din nods
  namn och delade position syns för alla inom räckhåll.
  [Observers](/network/) rapporterar det de hör till offentliga kartor.
  [Avsnittet om kryptering](#encryption) förklarar vad som förblir privat.
- **Det är inte obegränsat.** Alla i ett område delar på samma radiokanal, och
  reglerna för [868 MHz-bandet](#band) begränsar hur länge varje radio får sända.
  Varje meddelande tar sändningstid från alla andra, så bottar, täta adverts
  och testmeddelanden gör meshen långsammare för alla.
- **Det är inte Meshtastic.** Meshtastic är ett annat system som körs på
  ungefär samma kort. Systemen kan inte prata med varandra.
  [Från Meshtastic](#meshtastic) listar vad som fungerar annorlunda.

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

## Från Meshtastic {#meshtastic}

Många kort kan köra antingen MeshCore eller Meshtastic, och du flashar det du vill ha. Här är skillnaderna du märker först. De utgår från MeshCore
v1.18.0 och Meshtastics dokumentation från november 2026.

- **Vem som för meddelanden vidare.** I MeshCore gör bara repeatrar det, din companion
  gör det aldrig. I Meshtastic för även standardrollen client meddelanden vidare,
  om inte en annan nod redan har gjort det.
- **Hur långt ett meddelande når.** Ett meddelande i MeshCore kan passera upp till 64
  repeatrar. Meshtastic stannar som standard efter 3 hopp och som mest efter 7.
- **Mätvärden från andra noder.** Repeatrar och sensornoder i MeshCore skickar
  mätvärden som batterispänning när du ber om dem. De skickar dem inte till hela meshen.
- **Internet.** MeshCores firmware har ingen länk mellan mesher via
  internet. [Observers](/network/) rapporterar det de hör till kartor, bara
  i en riktning. Meshtastic har en inbyggd MQTT-modul
  som kan föra över meddelanden mellan mesher via internet.

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
- En reservkanal för familj eller grannar när strömmen eller mobilnäten
  ligger nere.
- Lokal chatt på radioapparater som folk äger själva.
- Kolla läget på en avlägsen plats hemifrån. Repeatrar och sensornoder rapporterar sin
  batterispänning och andra mätvärden när du frågar.
- Hålla koll på en sensor. En sensornod kör MeshCores firmware för mätningar.
  Den sparar historik över sina mätvärden. Om du prenumererar varnar den
  dig, till exempel när batteriet börjar ta slut.
- Styra något på långt håll, till exempel en pump. Du lägger till det i sensorns
  firmware med egen kod.
- Experimentera med radio, antenner, solenergi och programvara med öppen källkod.

## Var datan kommer ifrån {#data}

Sökningen på sidan [lokala grupper](/community/) hittar en plats med hjälp av
en kopia av de fria ort- och postnummerlistorna från
[GeoNames](https://www.geonames.org/), licensierade under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopian finns på
den här webbplatsen. Din sökning lämnar aldrig din enhet, och ingen förfrågan
går till GeoNames.
