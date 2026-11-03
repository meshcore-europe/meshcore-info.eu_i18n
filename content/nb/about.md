---
title: Hva er MeshCore?
lead: MeshCore sender tekstmeldinger via radio, fra node til node. Det fungerer uten internett og uten abonnement.
description: 'Hva MeshCore er og ikke er: nodetyper, ruting, forskjellen fra Meshtastic, kryptering og 868 MHz-båndet.'
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

MeshCore er gratis programvare for små LoRa-radioer. LoRa er en radioteknikk
som sender små datamengder langt, med svært lite strøm. En radio med MeshCore
kalles en *node*. Du kobler den til appen på telefonen eller den bærbare,
eller bruker nodens egen skjerm og tastatur. Da kan du sende tekst til folk
flere kilometer unna. Ingen mast, ruter eller leverandør står imellom.

Programvaren er åpen kildekode. Den utvikles på
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) under
MIT-lisensen.

## Hva MeshCore ikke er {#not}

Er du ny innen radio? Her er det folk oftest forventer av MeshCore, men som
det ikke gjør.

- **Det er verken internett eller en telefon.** MeshCore sender korte tekstmeldinger,
  omtrent like lange som en tekstmelding på telefonen. Du får ikke tale, bilder,
  video eller nettsider, og du kan ikke nå et vanlig telefonnummer.
- **Det er ikke en nødtjeneste.** Ingen nødtjeneste lytter på meshet, og ingen
  lover at noen leser meldingen din. Ring 112 i en nødsituasjon.
- **Det går ikke umiddelbart, og det finnes ikke overalt.** En melding hopper fra
  radio til radio og kan ta noen sekunder, eller ikke komme fram i det hele tatt.
  Om den kommer fram, avhenger av repeaterne rundt deg, av høyde, bygninger og
  antennen din. En liten radio innendørs når ofte ingen. En repeater på et tak
  når flere kilometer.
- **Det er ikke en tjeneste noen drifter for deg.** Det finnes ingen leverandør,
  ingen brukerstøtte og ingen dekningsgaranti. Meshet finnes der folk i miljøet
  har satt opp repeatere, og ingen andre steder.
- **Ikke alt på meshet er privat.** Direktemeldinger er kryptert, men alle kan lese
  Public og hashtag-kanalene, og alle innen rekkevidde ser navnet på noden din og
  posisjonen du deler. [Observatører](/network/) rapporterer det de hører, til
  offentlige kart. [Delen om kryptering](#encryption) forklarer hva som forblir privat.
- **Det er ikke ubegrenset.** Alle i et område deler én radiokanal, og reglene for
  [868 MHz-båndet](#band) begrenser hvor lenge hver radio får sende. Hver melding
  tar sendetid fra alle andre, så boter, hyppige adverts og testmeldinger gjør
  meshet tregere for alle.
- **Det er ikke Meshtastic.** Meshtastic er et annet system som kjører på omtrent
  de samme kortene. De to systemene kan ikke snakke sammen.
  [Kommer du fra Meshtastic](#meshtastic) viser hva som fungerer annerledes.

## Meshen på ett minutt {#mesh}

Én LoRa-radio når noen få kilometer i en by, og mye lenger fra en ås eller et
tak. For å nå lenger sender radioene meldinger videre for hverandre: det er en
*mesh*. I MeshCore er det radioer kalt *repeatere* som sender videre. En
repeater som hører en melding, sender den på nytt. Slik kan meldingen krysse
en hel region.

Ingen eier meshen. Hver node og hver repeater tilhører noen i miljøet. Meshen
rekker så langt som repeaterne deres gjør.

## De 3 nodetypene {#roles}

Du velger nodetype når du flasher noden. Din første node er en companion.

**Companion.** Din egen radio. Du parer den med MeshCore-appen på telefonen
eller den bærbare via Bluetooth eller USB. Noen har egen skjerm og tastatur.
I appen leser og skriver du. Companion-noden lagrer kontaktene og kanalene
dine, og meldingene som kom mens appen ikke var tilkoblet. En companion sender
ikke meldinger videre for andre.

**Repeater.** En radio som står høyt og sender meldinger videre for alle. De
fleste går på solstrøm. Du trenger bare din egen der meshen ikke når ennå. Den
har ingen egen app. Du setter den opp via USB, eller logger inn med passord og
administrerer den over radio.
[Repeaterguiden](/repeater-guide/) viser hvordan.

**Room server.** En liten oppslagstavle på meshen. Når du logger inn, får du
innleggene du gikk glipp av mens du var utenfor rekkevidde, opptil de 32
siste. Serveren holder dem bare i minnet, så en omstart eller et strømbrudd
sletter dem. En lokal gruppe bruker en room server til kunngjøringer.

## Slik finner en melding fram {#routing}

Hver node har en hemmelig nøkkel og en offentlig nøkkel. Den offentlige
nøkkelen er nodens identitet. En node kunngjør seg selv med en *advert*: en
signert pakke med navnet og, hvis du vil, posisjonen. Noen dukker opp blant
kontaktene dine når en av deres adverts har nådd deg, eller når du skanner
QR-koden deres. I appen finnes en knapp for å sende din egen.

Den første meldingen din til en kontakt går ut som *flood*. Hver repeater som
hører den, sender den videre én gang og legger til sin egen korte ID underveis.
Svaret tar med seg denne ID-listen tilbake. Fra da av følger meldingene dine
til den kontakten den registrerte stien, og bare repeaterne på stien sender.
Når stien brytes, sender appen en ny flood.

Meldinger til en kanal har ingen enkeltadresse, så de går alltid som flood.
Repeatere husker hva de nylig har sendt videre, og forkaster kopier som kommer
inn på nytt via en annen sti. En melding kan krysse opptil 64 repeatere, eller
32 der forhåndsinnstillingen bruker 2-byte-ID-er.

## For deg som kommer fra Meshtastic {#meshtastic}

Mange kort kjører enten MeshCore eller Meshtastic, og du flasher det du vil ha. Dette er forskjellene du merker først. De bygger på MeshCore v1.18.0 og Meshtastic-dokumentasjonen fra november 2026.

- **Hvem som sender meldinger videre.** I MeshCore gjør bare repeatere det; companion-noden din
  gjør det aldri. I Meshtastic sender også standardrollen client meldinger videre,
  med mindre en annen node allerede har gjort det.
- **Hvor langt en melding kommer.** En MeshCore-melding kan gå gjennom opptil 64
  repeatere. Meshtastic stopper som standard etter 3 hopp, og senest etter 7.
- **Målinger fra andre noder.** Repeatere og sensornoder i MeshCore sender målinger
  som batterispenning når du ber om dem. De sender dem ikke til hele meshen.
- **Internett.** MeshCore-firmwaren har ingen kobling mellom mesher over
  internett. [Observatører](/network/) rapporterer det de hører til kart, bare
  én vei. Meshtastic har en innebygd MQTT-modul
  som kan overføre meldinger mellom mesher over internett.

## Kryptering og personvern {#encryption}

Direktemeldingene dine er ende-til-ende-kryptert: bare du og mottakeren kan
lese dem. En repeater ser mottakeren av en pakke bare som et hint på 1 byte.

Kanaler krypteres med en delt nøkkel. Hvem som kan lese dem, avhenger derfor
av hvem som har nøkkelen:

- **Public** er satt opp på alle companions. Nøkkelen er publisert, så alle
  kan lese kanalen.
- **Hashtag-kanaler**, som `#utrecht`, får nøkkelen fra navnet sitt. Alle som
  kjenner navnet, kan bli med, så regn dem også som offentlige.
- **Private kanaler** bruker en tilfeldig nøkkel som du deler selv, for
  eksempel som QR-kode.

Adverts er signert, men ikke kryptert. Alle innen rekkevidde ser nodenavnet
ditt, og posisjonen hvis du deler den. Velg et navn som ikke sier mer enn du
vil.

## 868 MHz-båndet i Europa {#band}

I Europa bruker MeshCore en liten del av 868 MHz-båndet, som alle kan bruke
uten lisens. Den europeiske radioinnstillingen, EU/UK (Narrow), ligger på
869.618 MHz med en kanal på 62.5 kHz. Det er innenfor delbåndet
869.40-869.65 MHz, som tillater opptil 500 mW e.r.p. En enhet kan sende der
høyst 10% av tiden.
[Den juridiske delen av repeaterguiden](/repeater-guide/#legal) har detaljene
og grensene per land.

Alle i et område bruker samme forhåndsinnstilling, ellers kan ikke radioene
høre hverandre. Noen land og regioner bruker en variant: den
[lokale gruppen din](/community/) vet hvilken.

## Hva folk bruker det til {#uses}

- Holde kontakten på fjellturer, på sjøen og på festivaler der mobilnettet
  er overbelastet eller mangler.
- En reservekanal for familie eller naboer når strøm eller mobilnett svikter.
- Lokal chat på radioer folk eier selv.
- Sjekke et sted langt unna hjemmefra. Repeatere og sensornoder rapporterer
  batterispenning og andre målinger når du ber om det.
- Følge med på en sensor. En sensornode kjører MeshCores firmware for å måle
  ting. Den lagrer en historikk over målingene sine. Abonnerer du, varsler
  den deg, for eksempel når batteriet begynner å bli lavt.
- Slå på eller av noe langt unna, for eksempel en pumpe. Det legger du til i
  sensorfirmwaren med din egen kode.
- Eksperimentere med radio, antenner, solenergi og programvare med åpen kildekode.

## Hvor dataene kommer fra {#data}

Søket på siden om [lokale grupper](/community/) finner steder i en kopi av de
gratis steds- og postnummerlistene fra [GeoNames](https://www.geonames.org/),
lisensiert under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopien ligger på
dette nettstedet. Søket ditt forlater aldri enheten din, og ingen
forespørsel går til GeoNames.
