---
title: Vad är MeshCore?
lead: MeshCore skickar textmeddelanden via radio, från nod till nod. Det fungerar utan internet eller abonnemang.
description: 'Vad MeshCore är och inte är: meshen, companions, repeaters och room servers, routing, kryptering och 868 MHz-bandet i Europa.'
eyebrow: MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '33e571f0'
  seeded: '2026-10-26'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['a3a6c1ff', '007314d2', 'f1f23981', '493b444f', '429f699c', 'f8008f48', '655373a9']
---

MeshCore är fri programvara för små LoRa-radior. LoRa är en radioteknik
som skickar lite data långt, med mycket låg effekt. En radio med MeshCore
kallas *nod*. Tillsammans med appen i din telefon eller dator, eller med egen
skärm och eget tangentbord, skickar den text till personer kilometer bort. Ingen mast, router eller operatör sitter emellan.

MeshCore skickar bara korta textmeddelanden: ingen röst, inga foton och ingen
internettrafik.
Ett meddelande kan ta några sekunder, och om det kommer fram beror på
repeaterna runt dig. Det ersätter inte räddningstjänsten: i en nödsituation
ringer du 112.

Programvaran är öppen källkod och utvecklas på
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) under
MIT-licensen.

## Meshen på en minut {#mesh}

En LoRa-radio når några kilometer i en tätort, och mycket längre från en
kulle eller ett tak. För att nå längre skickar radiorna meddelanden vidare åt
varandra: det är en *mesh*. I MeshCore är det radior som kallas *repeaters*
som skickar vidare. En repeater som hör ett meddelande sänder det igen, så att
det kan korsa en hel region.

Ingen äger meshen. Varje nod och varje repeater tillhör någon i gemenskapen.
Meshen är inte bättre än de repeaters som folk sätter upp.

## De 3 typerna av nod {#roles}

Du väljer nodens typ när du flashar den. Din första nod är en companion.

**Companion.** Din egen radio. Den parkopplas med MeshCore-appen i din telefon
eller dator via Bluetooth eller USB; vissa har egen skärm och eget tangentbord.
I appen läser och skriver du. Companionen sparar dina kontakter och kanaler,
och de meddelanden som kom medan appen inte var ansluten. En companion skickar
inte vidare meddelanden åt andra.

**Repeater.** En radio som placeras högt och skickar vidare meddelanden åt
alla. De flesta drivs med solceller. Du behöver bara en egen där meshen inte
når ännu. Den har ingen egen app. Du ställer in den via USB, eller loggar in
med lösenord och hanterar den över radion.
[Repeaterguiden](/repeater-guide/) visar hur.

**Room server.** En liten anslagstavla på meshen. När du loggar in får du de
inlägg du missade medan du var utom räckhåll, upp till de senaste 32. En
lokal grupp använder en för meddelanden till alla.

## Hur ett meddelande hittar fram {#routing}

Varje nod har en hemlig nyckel och en offentlig nyckel. Den offentliga nyckeln
är dess identitet. En nod presenterar sig med en *advert*: ett signerat paket
med dess namn och, om du vill, dess position. Någon dyker upp bland dina
kontakter när en av deras adverts har nått dig, eller när du skannar deras
QR-kod. Appen har en knapp för att skicka din egen.

Ditt första meddelande till en kontakt går ut som en *flood*. Varje repeater
som hör det skickar det vidare en gång och lägger till sitt eget korta ID på
vägen. Svaret bär med sig den listan med ID:n tillbaka. Från och med då följer
dina meddelanden till den kontakten den sparade vägen, och bara repeaterna på
den sänder. När vägen bryts floodar appen igen.

Meddelanden till en kanal har ingen enskild adress, så de floodar alltid.
Repeaters kommer ihåg vad de nyligen skickat vidare och slänger kopior som
kommer igen via en annan väg. Ett meddelande kan passera upp till 64
repeaters, eller 32 där förinställningen använder 2-byte-ID:n.

## Kryptering och integritet {#encryption}

Dina direktmeddelanden är krypterade från ände till ände: bara du och den
andra personen kan läsa dem. En repeater ser vem ett paket är till enbart som
en ledtråd på 1 byte.

Kanaler krypteras med en delad nyckel, så vem som kan läsa dem beror på vem
som har nyckeln:

- **Public** finns inställd på varje companion. Dess nyckel är publicerad, så
  vem som helst kan läsa den.
- **Hashtag-kanaler**, som `#utrecht`, får sin nyckel från sitt namn. Alla
  som känner till namnet kan gå med, så betrakta även dem som offentliga.
- **Privata kanaler** använder en slumpmässig nyckel som du själv delar ut,
  till exempel som QR-kod.

Adverts är signerade men inte krypterade. Din nods namn, och dess position om
du delar den, syns för alla inom räckhåll. Välj ett namn som inte säger mer än
du vill.

## 868 MHz-bandet i Europa {#band}

I Europa använder MeshCore en liten del av 868 MHz-bandet som vem som helst
får använda utan tillstånd. Dess europeiska radioförinställning, EU/UK
(Narrow), ligger på 869.618 MHz i en 62.5 kHz bred kanal. Det är inom
delbandet 869.40-869.65 MHz, som tillåter upp till 500 mW e.r.p. En enhet får
sända där högst 10% av tiden.
[Avsnittet om regler i repeaterguiden](/repeater-guide/#legal) har detaljerna
och gränserna per land.

Alla i ett område använder samma förinställning, annars kan deras radior inte
höra varandra. Vissa länder och regioner använder en variant: din
[lokala grupp](/community/) vet vilken.

## Vad folk använder det till {#uses}

- Att hålla kontakten på vandringar, till sjöss och på festivaler där
  mobilnätet är överbelastat eller saknas.
- En reservkanal för familj eller grannar när el eller mobilnät slutar
  fungera.
- Lokal chatt på radior som folk äger själva.
- Att experimentera med radio, antenner, solceller och programvara med öppen
  källkod.
