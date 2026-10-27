---
title: Hvad er MeshCore?
lead: MeshCore sender tekstbeskeder via radio, fra node til node. Det virker uden internet og uden abonnement.
description: 'Hvad MeshCore er og ikke er: mesh, companions, repeatere og room servere, routing, kryptering og 868 MHz-båndet i Europa.'
eyebrow: MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '33e571f0'
  seeded: '2026-10-26'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['a3a6c1ff', '007314d2', 'f1f23981', '493b444f', '429f699c', 'f8008f48', '655373a9']
---

MeshCore er gratis software til små LoRa-radioer. LoRa er en radioteknik,
der sender små mængder data langt på meget lidt strøm. En radio med MeshCore
kaldes en *node*. Parret med appen på din telefon eller laptop, eller med sin
egen skærm og sit eget tastatur, sender den tekst til folk kilometer væk. Der sidder ingen mast, router eller teleudbyder imellem.

MeshCore sender kun korte tekstbeskeder: ingen tale, billeder eller
internettrafik.
En besked kan tage et par sekunder, og om den når frem, afhænger af
repeaterne omkring dig. Det erstatter ikke beredskabet: i en nødsituation
ringer du 112.

Softwaren er open source og udvikles på
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) under
MIT-licensen.

## Mesh på et minut {#mesh}

En LoRa-radio rækker et par kilometer i en by, og meget længere fra en bakke
eller et tag. For at nå længere sender radioerne beskeder videre for
hinanden: det er et *mesh*. I MeshCore er det radioer kaldet *repeatere*, der
sender videre. En repeater, der hører en besked, sender den igen, så den kan
krydse en hel region.

Ingen ejer meshet. Hver node og hver repeater tilhører nogen i fællesskabet.
Meshet er præcis så godt som de repeatere, folk sætter op.

## De 3 slags noder {#roles}

Du vælger nodens type, når du flasher den. Din første node er en companion.

**Companion.** Din egen radio. Du parrer den med MeshCore-appen på din telefon
eller laptop via Bluetooth eller USB; nogle har egen skærm og eget tastatur.
Det er i appen, du læser og skriver. Companionen gemmer dine kontakter og
kanaler samt de beskeder, der kom, mens appen ikke var forbundet. En companion sender ikke beskeder videre for andre.

**Repeater.** En radio, der er placeret højt og sender beskeder videre for
alle. De fleste kører på solceller. Du har kun brug for din egen, hvor meshet
endnu ikke rækker. Den har ingen egen app. Du sætter den op via USB, eller
du logger ind med et kodeord og styrer den over radioen.
[Repeater-guiden](/repeater-guide/) viser hvordan.

**Room server.** En lille opslagstavle på meshet. Når du logger ind, får du
de opslag, du missede uden for dækning, op til de sidste 32. En lokal gruppe
bruger en til meddelelser.

## Sådan finder en besked vej {#routing}

Hver node har en privat nøgle og en offentlig nøgle. Den offentlige nøgle er
dens identitet. En node melder sig med en *advert*: en signeret pakke med
dens navn og, hvis du vælger det, dens position. En person dukker op i dine
kontakter, når en af deres adverts har nået dig, eller når du scanner deres
QR-kode. Appen har en knap til at sende din egen.

Din første besked til en kontakt sendes som et *flood*. Hver repeater, der
hører den, sender den videre én gang og tilføjer sit eget korte ID på vejen.
Svaret bærer den liste af ID'er tilbage. Herefter følger dine beskeder til
den kontakt den registrerede sti, og kun repeaterne på den sender. Når stien
bliver afbrudt, flooder appen igen.

Beskeder til en kanal har ingen enkelt adresse, så de flooder altid.
Repeatere husker, hvad de nyligt har sendt videre, og kasserer kopier, der
kommer igen ad en anden vej. En besked kan krydse op til 64 repeatere, eller
32 hvor presettet bruger 2-byte ID'er.

## Kryptering og privatliv {#encryption}

Dine direkte beskeder er krypteret ende til ende: kun du og den anden kan
læse dem. En repeater ser kun, hvem en pakke er til, som et hint på 1 byte.

Kanaler krypteres med en delt nøgle, så hvem der kan læse dem, afhænger af,
hvem der har nøglen:

- **Public** er sat op på hver companion. Dens nøgle er offentliggjort, så
  alle kan læse den.
- **Hashtag-kanaler**, som `#utrecht`, får deres nøgle fra navnet. Alle, der
  kender navnet, kan være med, så behandl dem også som offentlige.
- **Private kanaler** bruger en tilfældig nøgle, som du selv deler, for
  eksempel som QR-kode.

Adverts er signeret, men ikke krypteret. Din nodes navn, og dens position
hvis du deler den, kan ses af alle inden for rækkevidde. Vælg et navn, der
ikke siger mere, end du vil.

## 868 MHz-båndet i Europa {#band}

I Europa bruger MeshCore en lille del af 868 MHz-båndet, som alle må bruge
uden licens. MeshCores europæiske radiopreset, EU/UK (Narrow), ligger på
869.618 MHz på en 62.5 kHz-kanal. Det er inden for underbåndet
869.40-869.65 MHz, som tillader op til 500 mW e.r.p. En enhed må højst sende
der 10% af tiden.
[Afsnittet om regler i repeater-guiden](/repeater-guide/#legal) har
detaljerne og grænserne for hvert land.

Alle i et område bruger det samme preset, ellers kan deres radioer ikke høre
hinanden. Nogle lande og regioner bruger en variant: din
[lokale gruppe](/community/) ved hvilken.

## Hvad folk bruger det til {#uses}

- At holde kontakt på vandreture, til søs og på festivaler, hvor mobilnettet
  er overbelastet eller mangler.
- En reservekanal for familie eller naboer, når strømmen eller mobilnettet
  svigter.
- Lokal chat på radioer, folk selv ejer.
- At eksperimentere med radio, antenner, solceller og open source-software.
