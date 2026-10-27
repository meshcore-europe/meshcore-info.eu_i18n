---
title: Hva er MeshCore?
lead: MeshCore sender tekstmeldinger over radio, fra node til node. Det fungerer uten internett og uten abonnement.
description: 'Hva MeshCore er og ikke er: mesh, companions, repeatere og room-servere, ruting, kryptering og 868 MHz-båndet i Europa.'
eyebrow: MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '33e571f0'
  seeded: '2026-10-26'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['a3a6c1ff', '007314d2', 'f1f23981', '493b444f', '429f699c', 'f8008f48', '655373a9']
---

MeshCore er gratis programvare for små LoRa-radioer. LoRa er en radioteknikk
som sender lite data langt, med svært lite strøm. En radio med MeshCore
kalles en *node*. Koblet til appen på telefonen eller den bærbare, eller med
egen skjerm og eget tastatur, sender den tekst til folk kilometervis unna. Ingen mast, ruter eller operatør står imellom.

MeshCore sender bare korte tekstmeldinger: ingen tale, bilder eller
internettrafikk.
En melding kan ta noen sekunder, og om den kommer fram, avhenger av
repeaterne rundt deg. Det erstatter ikke nødetatene: i en nødsituasjon
ringer du 112.

Programvaren er åpen kildekode og utvikles på
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) under
MIT-lisensen.

## Mesh på ett minutt {#mesh}

Én LoRa-radio rekker noen kilometer i en by, og mye lenger fra en ås eller
et tak. For å nå lenger sender radioene meldinger videre for hverandre: det
er et *mesh*. I MeshCore er det radioer som kalles *repeatere* som sender
videre. En repeater som hører en melding, sender den på nytt, så den kan
krysse en hel region.

Ingen eier meshet. Hver node og hver repeater tilhører noen i fellesskapet.
Meshet er like godt som repeaterne folk setter opp.

## De 3 typene node {#roles}

Du velger typen node når du flasher den. Din første node er en companion.

**Companion.** Din egen radio. Den pares med MeshCore-appen på telefonen
eller den bærbare over Bluetooth eller USB; noen har egen skjerm og eget
tastatur. I appen leser og skriver du. Companionen tar vare på kontaktene og
kanalene dine, og meldingene som kom inn mens appen ikke var tilkoblet. En companion sender ikke meldinger videre for andre.

**Repeater.** En radio plassert høyt som sender meldinger videre for alle. De
fleste går på solceller. Du trenger bare en egen der meshet ikke rekker
ennå. Den har ingen egen app. Du setter den opp over USB, eller
logger inn med passord og styrer den over radio.
[Repeater-guiden](/repeater-guide/) viser hvordan.

**Room-server.** En liten oppslagstavle på meshet. Når du logger inn, får du
innleggene du gikk glipp av mens du var utenfor rekkevidde, opptil de siste
32. En lokal gruppe bruker en til kunngjøringer.

## Hvordan en melding finner veien {#routing}

Hver node har en privat nøkkel og en offentlig nøkkel. Den offentlige nøkkelen er dens identitet. En node
gjør seg kjent med en *advert*: en signert pakke med navnet og, hvis du
velger det, posisjonen. Noen dukker opp i kontaktene dine etter at en av
advertene deres har nådd deg, eller når du skanner QR-koden deres. Appen har en knapp for å sende din egen.

Den første meldingen din til en kontakt går ut som en *flood*. Hver repeater
som hører den, sender den videre én gang og legger til sin egen korte ID
underveis. Svaret tar den listen med ID-er med tilbake. Fra da av følger
meldingene dine til den kontakten den registrerte ruten, og bare repeaterne
på den sender. Når ruten brytes, flooder appen på nytt.

Meldinger til en kanal har ingen enkelt adresse, så de flooder alltid.
Repeatere husker hva de nylig har sendt videre og forkaster kopier som kommer
igjen via en annen rute. En melding kan krysse opptil 64 repeatere, eller 32 der forhåndsinnstillingen bruker 2-byte
ID-er.

## Kryptering og personvern {#encryption}

Direktemeldingene dine er ende-til-ende-kryptert: bare du og den andre kan
lese dem. En repeater ser hvem en pakke er til bare som et hint på 1 byte.

Kanaler krypteres med en delt nøkkel, så hvem som kan lese dem, avhenger av
hvem som har den nøkkelen:

- **Public** er satt opp på hver companion. Nøkkelen er offentliggjort, så
  hvem som helst kan lese den.
- **Hashtag-kanaler**, som `#utrecht`, får nøkkelen fra navnet sitt. Alle
  som kjenner navnet, kan bli med, så behandle dem som offentlige også.
- **Private kanaler** bruker en tilfeldig nøkkel som du deler selv, for
  eksempel som QR-kode.

Adverts er signert, men ikke kryptert. Navnet på noden din, og posisjonen
hvis du deler den, er synlig for alle innen rekkevidde. Velg et navn som ikke
sier mer enn du vil.

## 868 MHz-båndet i Europa {#band}

I Europa bruker MeshCore en liten del av 868 MHz-båndet som alle kan bruke
uten lisens. Den europeiske radioforhåndsinnstillingen, EU/UK (Narrow),
ligger på 869.618 MHz i en kanal på 62.5 kHz. Det er innenfor delbåndet
869.40-869.65 MHz, som tillater opptil 500 mW e.r.p. En enhet kan sende der
høyst 10% av tiden.
[Juss-delen i repeater-guiden](/repeater-guide/#legal) har detaljene og
grensene per land.

Alle i et område bruker samme forhåndsinnstilling, ellers kan ikke radioene
høre hverandre. Noen land og regioner bruker en variant: den
[lokale gruppen din](/community/) vet hvilken.

## Hva folk bruker det til {#uses}

- Å holde kontakten på turer, til sjøs og på festivaler der mobilnettet er
  overbelastet eller fraværende.
- En reservekanal for familie eller naboer når strømmen eller mobilnettet
  svikter.
- Lokal prat på radioer som folk eier selv.
- Å eksperimentere med radio, antenner, solceller og programvare med åpen
  kildekode.
