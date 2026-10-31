---
title: Hvad er MeshCore?
lead: MeshCore sender tekstbeskeder via radio, fra node til node. Det virker uden internet og uden abonnement.
description: 'Hvad MeshCore er, og hvad det ikke er: mesh-nettet, companions, repeatere og room servers, routing, kryptering og 868 MHz-båndet i Europa.'
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

MeshCore er gratis software til små LoRa-radioer. LoRa er en radioteknik,
der sender små mængder data langt med meget lidt strøm. En radio med MeshCore
kaldes en *node*. Du parrer den med appen på din telefon eller bærbare, eller
bruger dens egen skærm og tastatur. Så kan du sende tekst til folk, der er
kilometer væk. Der er ingen mast, router eller udbyder imellem.

Softwaren er open source. Den udvikles på
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) under
MIT-licensen.

## Hvad MeshCore ikke er {#not}

Er du ny inden for radio? Her er det, folk oftest forventer af MeshCore,
og som det ikke kan.

- **Det er ikke internettet eller en telefon.** MeshCore sender korte
  tekstbeskeder, cirka så lange som en sms på din telefon. Der er ingen tale,
  billeder, video eller hjemmesider, og du kan ikke ringe til et almindeligt
  telefonnummer.
- **Det er ikke en nødtjeneste.** Ingen nødtjeneste lytter med på mesh-nettet,
  og ingen lover, at nogen læser din besked. Ring 112, hvis det er en nødsituation.
- **Det er ikke øjeblikkeligt, og det virker ikke overalt.** En besked hopper
  fra radio til radio. Det kan tage nogle sekunder, eller den kommer slet ikke
  frem. Om den når frem, afhænger af repeaterne omkring dig, af højde, bygninger
  og din antenne. En lille radio indendørs når ofte ingen. En repeater på et tag
  når flere kilometer.
- **Det er ikke en tjeneste, som nogen driver for dig.** Der er ingen udbyder,
  ingen helpdesk og ingen garanti for dækning. Mesh-nettet findes der, hvor folk
  i fællesskabet har sat repeatere op, og ingen andre steder.
- **Ikke alt er privat.** Direkte beskeder er krypterede. Men alle kan læse
  Public og hashtag-kanalerne, og alle inden for rækkevidde kan se din nodes
  navn og den position, du deler. [Observers](/network/) sender det, de hører,
  videre til offentlige kort. [Afsnittet om kryptering](#encryption) forklarer,
  hvad der forbliver privat.
- **Det er ikke ubegrænset.** Alle i et område deler én radiokanal. Reglerne for
  [868 MHz-båndet](#band) begrænser, hvor længe hver radio må sende. Hver besked
  tager sendetid fra alle andre. Bots, hyppige adverts og testbeskeder gør derfor
  mesh-nettet langsommere for alle.
- **Det er ikke Meshtastic.** Meshtastic er et andet system, der kører på stort
  set de samme boards. De to kan ikke tale sammen.

## Mesh-nettet på et minut {#mesh}

En LoRa-radio når nogle få kilometer i en by og meget længere fra en bakke
eller et tag. For at nå længere sender radioerne beskeder videre for hinanden.
Det kaldes et *mesh*. I MeshCore er det radioer kaldet *repeatere*, der sender
videre. Når en repeater hører en besked, sender den den igen. Så kan beskeden
krydse en hel region.

Ingen ejer mesh-nettet. Hver node og hver repeater tilhører en person i
fællesskabet. Mesh-nettet rækker så langt, som deres repeatere gør.

## De 3 slags noder {#roles}

Du vælger nodens type, når du flasher den. Din første node er en companion.

**Companion.** Din egen radio. Du parrer den med MeshCore-appen på din telefon
eller bærbare via Bluetooth eller USB. Nogle har deres egen skærm og tastatur.
I appen læser og skriver du. Companionen gemmer dine kontakter og kanaler og
de beskeder, der kom, mens appen ikke var forbundet. En companion sender ikke
beskeder videre for andre.

**Repeater.** En radio, der står højt og sender beskeder videre for alle. De
fleste kører på solenergi. Du behøver kun din egen, hvor mesh-nettet ikke når
ud endnu. Den har ingen app. Du sætter den op via USB, eller du logger ind med
en adgangskode og styrer den over radioen. [Repeater-guiden](/repeater-guide/)
viser hvordan.

**Room server.** En lille opslagstavle på mesh-nettet. Når du logger ind, får du
de indlæg, du gik glip af uden for rækkevidde, op til de seneste 32. Den gemmer
dem kun i hukommelsen, så en genstart eller et strømsvigt sletter dem. En lokal
gruppe bruger en room server til meddelelser.

## Sådan finder en besked vej {#routing}

Hver node har en hemmelig nøgle og en offentlig nøgle. Den offentlige nøgle er
nodens identitet. En node gør opmærksom på sig selv med en *advert*: en signeret
pakke med dens navn og, hvis du vil, dens position. En person dukker op i dine
kontakter, når en af deres adverts har nået dig, eller når du scanner deres
QR-kode. I appen er der en knap, så du kan sende din egen.

Din første besked til en kontakt sendes som et *flood*. Hver repeater, der hører
den, sender den videre én gang og tilføjer sit eget korte ID undervejs. Svaret
bringer listen med ID'er tilbage. Herefter følger dine beskeder til den kontakt
den registrerede sti, og kun repeaterne på den sender. Hvis stien bryder
sammen, sender appen et flood igen.

Beskeder til en kanal har ikke én bestemt adresse, så de sendes altid som flood.
Repeatere husker, hvad de for nylig har sendt videre, og smider kopier væk, der
kommer igen ad en anden sti. En besked kan krydse op til 64 repeatere, eller 32,
hvor presettet bruger ID'er på 2 bytes.

## Kryptering og privatliv {#encryption}

Dine direkte beskeder er krypteret end-to-end: kun du og den anden person kan
læse dem. En repeater ser kun modtageren af en pakke som et hint på 1 byte.

Kanaler er krypteret med en delt nøgle. Hvem der kan læse dem, afhænger derfor
af, hvem der har nøglen:

- **Public** er sat op på alle companions. Nøglen er offentliggjort, så alle
  kan læse kanalen.
- **Hashtag-kanaler**, som `#utrecht`, får deres nøgle fra navnet. Alle, der
  kender navnet, kan deltage, så betragt dem også som offentlige.
- **Private kanaler** bruger en tilfældig nøgle, som du selv deler, for
  eksempel som en QR-kode.

Adverts er signerede, men ikke krypterede. Alle inden for rækkevidde kan se din
nodes navn og dens position, hvis du deler den. Vælg et navn, der ikke siger
mere, end du ønsker.

## 868 MHz-båndet i Europa {#band}

I Europa bruger MeshCore en lille del af 868 MHz-båndet, som alle må bruge
uden licens. Det europæiske radiopreset, EU/UK (Narrow), ligger på
869.618 MHz med en kanal på 62.5 kHz. Det ligger inden for underbåndet
869.40-869.65 MHz, som tillader op til 500 mW e.r.p. En enhed må højst sende
10% af tiden der. [Det juridiske afsnit i repeater-guiden](/repeater-guide/#legal)
har detaljerne og grænserne for hvert land.

Alle i et område bruger det samme preset, ellers kan deres radioer ikke høre
hinanden. Nogle lande og regioner bruger en variant. Din
[lokale gruppe](/community/) ved hvilken.

## Hvad folk bruger det til {#uses}

- At holde kontakten på vandreture, til søs og på festivaler, hvor mobilnettet
  er overbelastet eller mangler.
- En reservekanal for familie eller naboer, når strøm eller mobilnet svigter.
- Lokal chat på radioer, som folk selv ejer.
- Eksperimenter med radio, antenner, solenergi og open source-software.

## Hvor dataene kommer fra {#data}

Søgningen på siden med [lokale grupper](/community/) finder et sted ud fra en
kopi af de gratis lister over steder og postnumre fra
[GeoNames](https://www.geonames.org/), under licensen
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopien ligger på
denne hjemmeside. Din søgning forlader aldrig din enhed, og der går ingen
forespørgsel til GeoNames.
