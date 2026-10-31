---
title: Gjør meshen robust
lead: Er meshen der du bor treg eller full av søppel? Finn ut hva som skjer, slå på repeater-innstillingen som stopper det, og si fra til den lokale gruppen din.
description: 'Flood og spam på et MeshCore-mesh: slik kjenner du igjen hver type, hvilken repeater-innstilling som hjelper, hvordan du ser en flood og hvordan du finner kilden.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-10-31'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Kommer meldinger sent eller ikke i det hele tatt? Fylles Public med søppel? Da
er det en flood: mer trafikk enn meshen klarer å bære. Noen sender den ved
en feil eller med vilje. Finn det du ser i tabellene nedenfor. Hver rad
viser innstillingen som stopper det. Slå den på i repeateren din, noden som
sender meldinger videre. Si så fra til den [lokale gruppen](/community/) din,
slik at repeaterne rundt deg gjør det samme. Hver repeater som stopper en
flood, frigjør sendetid til alle andre.

## Flood ved en feil {#mistake}

En flood ved en feil kommer fra en node der eieren ikke vet om problemet.
Den stopper når eieren får vite det. En advert i tabellene nedenfor er
hilsenen en node sender ut, slik at andre kan finne den.

Innstillingene i tabellene bygger på hva firmwaren gjør. Ikke alle har
stoppet en flood på en ekte mesh ennå.

{{< callout type="warning" >}}
Noen innstillinger på denne siden krever DMC-firmwaren. Standard **MeshCore** 1.18.0
har regioner, hopp-grensene `flood.max.*`, løkkedeteksjon og duty cycle.
Pakkefilteret, reglene som lar repeateren din kaste søppel, følger med
**DMC-firmwaren** fra
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Det samme
gjelder duty-cycle-styring og companion-filteret. Denne siden følger
DMC 1.18.0-utviklingsbygget `ecfb2d4` fra 19. oktober 2026. Siden om
[pakkefilteret](/guides/filter/#firmware) forteller hvor du får det.
{{< /callout >}}

| Hva du ser | Hva det er | Hva som hjelper |
| --- | --- | --- |
| Forespørsler til repeatere fra én node, dag og natt, og en mesh som er treg i flere dager | En hjemmeautomasjon eller en bot som spør repeatere om status for ofte | `filter on`. Pakkefilteret slipper da gjennom 5 forespørsler i minuttet. Si fra til eieren. |
| Samme type melding i en kanal, hvert minutt | En bot som poster for ofte | [Blokker kanalen](/guides/filter/#channel) eller [brems avsenderen](/guides/filter/#sender). Si fra til eieren. |
| Uleselige meldinger i Public og andre kanaler | En node med ødelagt firmware eller feil radioinnstillinger | `filter malformed on` kaster dem i Public. Si fra til eieren. |
| Advert fra én node med noen få minutters mellomrom | En node som er satt til å sende advert for ofte | `filter advert 24` slipper gjennom én advert per node i døgnet. `set flood.max.advert 3` holder adverts innenfor 3 hopp. |
| Meldinger langveisfra, med regioner som ikke hører hjemme her | En bro som kobler mesh sammen over internett | `set flood.max.unscoped 1`, og legg repeateren din bare i [regionene den betjener](/guides/settings/#traffic). |
| Samme melding kommer igjen og igjen, med repeaterens ID flere ganger i stien | En repeater som endrer pakker og sender dem videre, slik at de går i løkke | Løkkedeteksjon står på `minimal` som standard. `set loop.detect moderate` stopper en løkke tidligere. |

## Flood med vilje {#purpose}

Noen flooder er spam: søppel som noen sender med vilje for å tette igjen
meshen. Avsenderen bytter navn, nøkler og stier, så ingen enkelt regel
stopper flooden.

| Hva du ser | Hva det er | Hva som hjelper |
| --- | --- | --- |
| Mange nye noder med tilfeldige navn, hver med ny nøkkel | Falske adverts | `filter rate 04 5 60` slipper gjennom 5 adverts i minuttet. `filter advert` hjelper ikke: hver advert kommer fra en [ny nøkkel](#forged). |
| Meldinger med uleselig tekst fra oppdiktede avsendere, ofte datert mer enn et år tilbake | Kanalspam | `filter malformed on` kaster dem i Public. `filter age 60` kaster de gammeldaterte i Public og i [overvåkede kanaler](/guides/filter/#settings). |
| Opptil 200 direktemeldinger i minuttet til noder som ikke finnes, og ingen kvitteringer tilbake | En flood av direktemeldinger | `filter rate 02 5 60`. Appen din viser ikke disse meldingene. Det gjør en observer. |
| Støt av forespørsler fra én node til dusinvis av andre | Forespørselsspam | Med `filter on` slipper pakkefilteret gjennom 5 forespørsler i minuttet. |
| En melding kommer tilbake 10 til 20 minutter senere, med nesten samme sti | Replay: en kopi som sendes på nytt | En repeater husker de siste 160 pakkene den har sett. På en travel mesh slipper derfor en senere kopi gjennom igjen. `filter age` kaster en gruppemelding som er eldre enn du tillater. |
| Meldinger fra Public sendt på nytt under en oppdiktet avsender, noen ganger med gammel dato | Ekkospam | `filter age 60`. `filter malformed on` kaster også en dato som bommer med mer enn en uke. |
| En melding med noen få sekunders mellomrom i flere kanaler, hver fra et nytt navn, med vanlige spørsmål | En bølge av boter | `filter rate 05 10 60`, og [blokker kanalene](/guides/filter/#channel) som ikke brukes der du bor. Hvert navn er nytt, så [avsenderreglene](#forged) treffer ikke. |

## Dette har virket {#worked}

Lokale grupper har stoppet flooder med disse stegene:

1. **Si fra til eieren.** En flood ved en feil stopper når eieren vet om
   den. Send eieren en vennlig melding.
2. **Ikke reager på meshen.** Et svar viser en spammer at spammen virker.
3. **Be om observere.** En observer er en node som rapporterer hver pakke
   den hører over MQTT. Jo flere observere rundt deg, desto før ser du
   hvor en flood kommer inn. Gjør din egen repeater til en med
   [MQTT på observeren din](/guides/mqtt/).
4. **Finn kilden.** Observere plasserer avsenderen i et område. Den siste
   kilometeren krever folk til fots med en radio. Se
   [Finn kilden](#source).
5. **Få den lokale gruppen i gang.** Én repeater med riktige innstillinger
   hjelper. Alle repeaterne i området sammen stopper en flood. Den
   [lokale gruppen](/community/) din får alle eiere til å slå på
   innstillingen.

## Oppdiktede avsendere og stier {#forged}

Avsenderen skriver disse delene av en pakke selv, og ingenting kontrollerer dem:

- **Avsenderens navn.** I en kanalmelding er navnet en del av teksten.
  Alle som har kanalnøkkelen, kan skrive hvilket som helst navn.
- **Starten på stien.** Hver repeater legger sin egen ID til slutten av
  stien. Ingenting kontrollerer ID-ene som stod der fra før. En avsender
  kan derfor starte stien med oppdiktede ID-er. Slutten av stien er ekte.

{{< forged-path >}}

`filter sender` og `filter path` stopper derfor bare en avsender til
avsenderen bytter navn eller sti. En [stiblokkering](/guides/filter/#path)
kaster også den ekte trafikken fra repeateren som har ID-en i blokkeringen.
Hastighetsgrenser, hopp-grenser, alders- og formatkontrollene,
kanalblokkeringer, regioner og duty cycle fortsetter å virke.

## Innstillinger for alle flooder {#always}

Disse gjelder uansett hva som flooder meshen:

- **Duty cycle på 10%.** Repeateren din sender da aldri mer enn loven
  tillater, uansett hva som kommer inn. Dette står i
  [repeater-guiden](/repeater-guide/#duty-cycle).
- **Regioner og hopp-grenser.** En region er området en melding holder
  seg innenfor. En repeater sender bare videre meldinger i regionene den
  har, og `flood.max.*` holder trafikken i nærheten. Begge står i
  [Hold trafikken nede](/guides/settings/#traffic).
- **Pakkefilteret for en travel repeater.** De
  [ferdige innstillingene](/guides/filter/#busy) halverer gruppemeldinger
  og adverts. Prøv dem først i [dry-run](/guides/filter/#dryrun): da teller
  filteret bare det det ville ha kastet.
- **Companion-filteret, i DMC-firmwaren.** Companion-en din, noden du
  sender meldinger fra, holder søppel unna appen din. Den skjuler ødelagte
  og gamle meldinger, og meldinger fra en repeater, en avsender eller et
  ord du blokkerer. En regel for avsender eller ord
  skjuler bare meldingen for deg. Andre mottar den fortsatt.

### Duty-cycle-styring {#gate}

I DMC-firmwaren kan du la repeateren gi sin egen region forrang når den
får mye å gjøre. Når den har sendt i mer enn 35% av siste minutt, slutter
den å sende videre meldinger uten region. Er den fortsatt travel, kaster
den deretter den videste regionen, ett nivå om gangen. Repeaterens egen
region slipper alltid gjennom. Dette virker bare når du har satt regioner
på repeateren. Slå det på og sjekk det:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Det den kaster, vises ikke i `filter stats`. Når repeateren blir rolig
igjen, kommer regionene tilbake, den innerste først.

## Se en flood {#see}

Appen din viser bare det som når fram til deg. Bare en observer hører en
flood av direktemeldinger til noder som ikke finnes. Hver observer
rapporterer til [MeshCore Analyzer](https://meshcore-analyzer.eu/), der
alle kan se det. Gjør repeateren din til en med
[MQTT på observeren din](/guides/mqtt/).

Se på hver kopi av én pakke i Analyzer. Stien viser som regel hvor den
kom fra. En som flooder, kan starte stien med
[oppdiktede ID-er](#forged), så de første ID-ene sier deg ingenting. Men
hver kopi har den samme oppdiktede starten. Kopien med kortest sti har
passert færrest ekte repeatere. Den ble altså hørt nærmest avsenderen.

{{< copies >}}

På din egen repeater viser `filter stats` hva pakkefilteret har kastet.
`filter stats top` viser første byte i node-ID-ene bak flest kastede
pakker. Mange noder deler den byten. Den snevrer derfor inn søket, men
navngir ikke avsenderen.

## Finn kilden {#source}

Når en flood stadig kommer tilbake:

1. **Følg stiene.** Les en sti bakfra: de siste ID-ene er repeaterne
   flooden passerte. Den tidligste ekte er nær kilden. ID-ene foran den
   kan være [oppdiktet](#forged).
2. **Snevre inn området.** Flere observere som hører samme pakke,
   plasserer avsenderen i et område.
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) regner det ut
   fra repeaterne som hørte pakken.
3. **Gå den siste kilometeren.** Repeaterne hører kilden bare i ytterkanten
   av rekkevidden sin. Den siste biten krever derfor folk til fots.
   [Mesh-Hunter](https://mesh-hunter.eu/) pares med companion-en din og
   logger hver pakke den hører, sammen med GPS-posisjonen din. Flere som
   går samtidig, finner kilden fortere.
4. **Si fra til den [lokale gruppen](/community/) din.** De ser mer av
   meshen, de bestemmer hva som skjer videre, og de kontakter den som
   flooder med vilje.

## Legg til det du så {#add}

Ble du rammet av en flood som ikke
står i disse tabellene? Stoppet en innstilling en flood? Fortell oss på
[Discord](https://discord.meshcore-info.eu/) hva du så og hva du slo
på. Vi legger det til på siden.
