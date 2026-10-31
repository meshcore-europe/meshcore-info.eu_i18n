---
title: Vad är MeshCore?
lead: MeshCore skickar textmeddelanden via radio, från nod till nod. Det fungerar utan internet och utan abonnemang.
description: 'Vad MeshCore är och inte är: meshen, companions, repeatrar och room servers, routning, kryptering och 868 MHz-bandet i Europa.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '78bc31e8'
  seeded: '2026-10-31'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['aa768ac3', 'c9b24089', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '655373a9', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b9fc8810', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '0eb54b47', '02f1fe2f', 'e6b5b258']
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

- **Det är varken internet eller telefon.** MeshCore skickar korta
  textmeddelanden, ungefär lika långa som ett sms. Du kan inte skicka röst,
  foton, video eller webbsidor, och du når inga vanliga telefonnummer.
- **Det är ingen larmtjänst.** Ingen larmcentral lyssnar på meshen, och
  ingen lovar att någon läser ditt meddelande. Ring 112 vid en nödsituation.
- **Det är inte omedelbart, och det fungerar inte överallt.** Ett meddelande
  hoppar från radio till radio och kan ta några sekunder, eller aldrig komma
  fram. Om det når fram beror på repeatrarna runt dig, på höjd, byggnader och
  din antenn. En liten radio inomhus når ofta ingen. En repeater på ett tak
  når flera kilometer.
- **Det är ingen tjänst som någon driver åt dig.** Det finns ingen operatör,
  ingen kundtjänst och inget löfte om täckning. Meshen finns där folk i
  gemenskapen har satt upp repeatrar, och ingen annanstans.
- **Inte allt på meshen är privat.** Direktmeddelanden är krypterade. Men alla
  kan läsa Public och hashtag-kanalerna, och alla inom räckhåll ser din nods
  namn och den position du delar. [Observers](/network/) rapporterar det de
  hör till offentliga kartor. I [avsnittet om kryptering](#encryption) ser du
  vad som förblir privat.
- **Det är inte obegränsat.** Alla i ett område delar på en radiokanal, och
  reglerna för [868 MHz-bandet](#band) begränsar hur länge varje radio får
  sända. Varje meddelande tar sändningstid från alla andra. Bottar, täta
  adverts och testmeddelanden gör därför meshen långsammare för alla.
- **Det är inte Meshtastic.** Meshtastic är ett annat system som körs på i
  stort sett samma kort. De två kan inte prata med varandra.

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

- Att hålla kontakten på vandringar, till sjöss och på festivaler där
  mobilnätet är överbelastat eller saknas.
- En reservkanal för familj eller grannar när ström eller mobilnät slutar
  fungera.
- Lokal chatt på radioapparater som folk själva äger.
- Att experimentera med radio, antenner, solkraft och programvara med öppen
  källkod.

## Var datan kommer ifrån {#data}

Sökningen på sidan [lokala grupper](/community/) hittar en plats med hjälp av
en kopia av de fria ort- och postnummerlistorna från
[GeoNames](https://www.geonames.org/), licensierade under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopian finns på
den här webbplatsen. Din sökning lämnar aldrig din enhet, och ingen förfrågan
går till GeoNames.
