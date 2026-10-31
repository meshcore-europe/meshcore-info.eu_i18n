---
title: Maak de mesh weerbaar
lead: Is de mesh bij jou in de buurt traag of vol rommel? Zoek uit waar het door komt, zet op je repeater de instelling aan die het stopt en laat het je lokale groep weten.
description: 'Floods en spam op een MeshCore-mesh: hoe je elke soort herkent, welke repeaterinstelling helpt, hoe je een flood ziet en hoe je de bron vindt.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-10-31'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Komen berichten laat of helemaal niet aan? Loopt Public vol met rommel? Dan
is er een flood: meer verkeer dan de mesh aankan, per ongeluk of met opzet
verstuurd. Zoek in de tabellen hieronder op wat je ziet. Elke rij noemt de
instelling die het stopt. Zet die aan op je repeater, de node die berichten
doorgeeft. Laat het daarna je [lokale groep](/community/) weten, zodat de
repeaters om je heen hetzelfde doen. Elke repeater die een flood laat vallen,
houdt zendtijd vrij voor alle anderen.

## Floods per ongeluk {#mistake}

Een flood per ongeluk komt van een node waarvan de eigenaar niet weet dat
die er een veroorzaakt. Zodra de eigenaar het weet, stopt de flood. Een
advertentie in de tabellen hieronder is de groet die een node uitzendt,
zodat anderen hem kunnen vinden.

De instellingen in de tabellen volgen uit wat de firmware doet. Niet elke
instelling heeft al een flood op een echte mesh gestopt.

{{< callout type="warning" >}}
Sommige instellingen op deze pagina vragen om de DMC-firmware. Standaard
**MeshCore** 1.18.0 heeft regio's, de hoplimieten `flood.max.*`,
lusdetectie en de duty cycle. Het pakketfilter, de regels waarmee je
repeater rommel laat vallen, zit in de **DMC-firmware** van
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Dat geldt ook
voor duty-cycle gating en het companionfilter. Deze pagina volgt de DMC
1.18.0 dev-build `ecfb2d4` van 19 oktober 2026. Op de pagina over het
[pakketfilter](/guides/filter/#firmware) lees je waar je die haalt.
{{< /callout >}}

| Wat je ziet | Wat het is | Wat helpt |
| --- | --- | --- |
| Dag en nacht verzoeken van één node aan repeaters, en een mesh die dagenlang traag blijft | Een domotica-systeem of een bot die repeaters te vaak om hun status vraagt | `filter on`. Het pakketfilter laat dan 5 verzoeken per minuut door. Laat het de eigenaar weten. |
| Elke minuut hetzelfde soort bericht op een kanaal | Een bot die te vaak post | [Blokkeer het kanaal](/guides/filter/#channel) of [rem de afzender af](/guides/filter/#sender). Laat het de eigenaar weten. |
| Onleesbare berichten op Public en andere kanalen | Een node met kapotte firmware of verkeerde radio-instellingen | `filter malformed on` laat ze op Public vallen. Laat het de eigenaar weten. |
| Om de paar minuten een advertentie van dezelfde node | Een node die te vaak adverteert | `filter advert 24` laat van elke node één advertentie per dag door. `set flood.max.advert 3` houdt advertenties binnen 3 hops. |
| Berichten van ver weg, met regio's die hier niet horen | Een brug die meshes via internet koppelt | `set flood.max.unscoped 1`, en zet je repeater alleen in de [regio's die hij bedient](/guides/settings/#traffic). |
| Hetzelfde bericht komt steeds opnieuw langs, met de ID van je repeater meer dan eens in het pad | Een repeater die pakketten aanpast en doorgeeft, waardoor ze rondzingen | Lusdetectie staat standaard op `minimal`. Met `set loop.detect moderate` valt een lus eerder weg. |

## Floods met opzet {#purpose}

Sommige floods zijn spam: rommel die iemand met opzet verstuurt om de mesh
te laten dichtslibben. De afzender wisselt van naam, sleutel en pad. Daarom
stopt geen enkele regel de flood op zichzelf.

| Wat je ziet | Wat het is | Wat helpt |
| --- | --- | --- |
| Veel nieuwe nodes met willekeurige namen, elk met een nieuwe sleutel | Nepadvertenties | `filter rate 04 5 60` laat 5 advertenties per minuut door. `filter advert` helpt niet: elke advertentie komt van een [nieuwe sleutel](#forged). |
| Berichten met onleesbare tekst van verzonnen afzenders, vaak met een datum van meer dan een jaar geleden | Kanaalspam | `filter malformed on` laat ze op Public vallen. `filter age 60` laat de oud gedateerde vallen op Public en op [bewaakte kanalen](/guides/filter/#settings). |
| Tot 200 directe berichten per minuut aan nodes die niet bestaan, en geen ontvangstbevestigingen terug | Een flood van directe berichten | `filter rate 02 5 60`. Je app toont deze berichten niet, een observer wel. |
| Salvo's verzoeken van één node aan tientallen andere | Verzoekspam | Met `filter on` laat het pakketfilter 5 verzoeken per minuut door. |
| Een bericht komt 10 tot 20 minuten later terug, met bijna hetzelfde pad | Replay: een kopie die opnieuw verstuurd is | Een repeater onthoudt de laatste 160 pakketten die hij zag. Op een drukke mesh komt een latere kopie dus weer door. `filter age` laat een groepsbericht vallen dat ouder is dan jij toestaat. |
| Berichten uit Public, opnieuw verstuurd onder een verzonnen afzender, soms met een oude datum | Echospam | `filter age 60`. `filter malformed on` laat ook een datum vallen die er meer dan een week naast zit. |
| Om de paar seconden een bericht op meerdere kanalen, elk van een nieuwe naam, met gewone vragen | Een botgolf | `filter rate 05 10 60`, en [blokkeer de kanalen](/guides/filter/#channel) die jouw omgeving niet gebruikt. Elke naam is nieuw, dus de [afzenderregels](#forged) missen hem. |

## Wat gewerkt heeft {#worked}

Lokale groepen hebben floods met deze stappen gestopt:

1. **Laat het de eigenaar weten.** Een flood per ongeluk stopt zodra de
   eigenaar het weet. Stuur een vriendelijk bericht.
2. **Reageer niet op de mesh.** Met een antwoord laat je een spammer zien dat
   de spam werkt.
3. **Vraag om observers.** Een observer is een node die elk pakket dat hij
   hoort via MQTT doorgeeft. Hoe meer observers om je heen, hoe eerder je
   ziet waar een flood binnenkomt. Maak van je eigen repeater een observer
   met [MQTT op je observer](/guides/mqtt/).
4. **Zoek de bron.** Observers plaatsen de afzender in een gebied. Voor de
   laatste kilometer moeten mensen te voet op pad met een radio. Zie
   [Zoek de bron](#source).
5. **Zet je lokale groep in beweging.** Eén repeater met de juiste
   instellingen helpt. Alle repeaters in de omgeving samen stoppen een flood.
   Je [lokale groep](/community/) zorgt dat elke eigenaar de instelling
   aanzet.

## Verzonnen afzenders en paden {#forged}

Deze delen van een pakket schrijft de afzender zelf, en niets controleert ze:

- **De naam van de afzender.** In een kanaalbericht hoort de naam bij de
  tekst. Iedereen met de kanaalsleutel kan elke naam invullen.
- **Het begin van het pad.** Elke repeater zet zijn eigen ID achter aan het
  pad. Niets controleert de ID's die er al stonden. Een afzender kan het pad
  dus met verzonnen ID's laten beginnen. Het einde van het pad is echt.

{{< forged-path >}}

`filter sender` en `filter path` houden een afzender dus alleen tegen tot
die zijn naam of pad verandert. Een [padblokkade](/guides/filter/#path) laat
ook het echte verkeer vallen van de repeater wiens ID erin staat.
Snelheidslimieten, hoplimieten, de controles op leeftijd en misvorming,
kanaalblokkades, regio's en de duty cycle blijven werken.

## Instellingen voor elke flood {#always}

Deze werken, welke flood de mesh ook treft:

- **Duty cycle op 10%.** Je repeater zendt dan nooit meer dan de wet toestaat,
  wat er ook binnenkomt. De [repeatergids](/repeater-guide/#duty-cycle) legt
  het uit.
- **Regio's en hoplimieten.** Een regio is het gebied waarin een bericht
  blijft. Een repeater geeft alleen berichten door in de regio's die hij
  heeft, en `flood.max.*` houdt verkeer dichtbij. Beide staan in
  [Houd het verkeer laag](/guides/settings/#traffic).
- **Het pakketfilter voor een drukke repeater.** De
  [kant-en-klare instellingen](/guides/filter/#busy) halveren groepsberichten
  en advertenties. Probeer ze eerst in [dry-run](/guides/filter/#dryrun): dan
  telt het filter alleen wat het zou laten vallen.
- **Het companionfilter, in de DMC-firmware.** Je companion, de node waarmee
  je berichten stuurt, houdt rommel uit je app. Hij verbergt kapotte en oude
  berichten, en berichten van een repeater, een afzender of een woord dat je
  blokkeert. Een regel voor een afzender of woord
  verbergt het bericht alleen voor jou. Anderen ontvangen het nog wel.

### Duty-cycle gating {#gate}

Met de DMC-firmware kan je repeater voorrang geven aan zijn eigen regio als
het druk wordt. Heeft hij in de laatste minuut meer dan 35% van de tijd
gezonden, dan geeft hij geen berichten zonder regio meer door. Blijft het
druk, dan laat hij daarna de breedste regio vallen, één niveau tegelijk.
Zijn eigen regio komt altijd door. Het werkt alleen als je regio's op je
repeater hebt ingesteld. Zet het aan en controleer het:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Wat hiermee wegvalt, zie je niet in `filter stats`. Wordt de repeater weer
rustig, dan komen de regio's terug, de binnenste eerst.

## Een flood zien {#see}

Je app toont alleen wat jou bereikt. Een flood van directe berichten aan
nodes die niet bestaan, hoort alleen een observer. Elke observer stuurt zijn
meldingen naar de [MeshCore Analyzer](https://meshcore-analyzer.eu/), waar
iedereen ze kan zien. Maak van je repeater een observer met
[MQTT op je observer](/guides/mqtt/).

Bekijk in de Analyzer elke kopie van één pakket. Meestal zie je aan het pad
waar het vandaan kwam. Een flooder kan het pad met
[verzonnen ID's](#forged) laten beginnen, dus de eerste ID's zeggen je niets.
Maar elke kopie heeft hetzelfde verzonnen begin. De kopie met het kortste
pad ging langs de minste echte repeaters. Die is dus het dichtst bij de
afzender gehoord.

{{< copies >}}

Op je eigen repeater zie je met `filter stats` wat het pakketfilter liet
vallen. `filter stats top` toont de eerste byte van de node-ID's achter de
meeste weggevallen pakketten. Veel nodes delen die byte. Je zoekgebied wordt
dus kleiner, maar de afzender heb je er nog niet mee.

## Zoek de bron {#source}

Als een flood steeds terugkomt:

1. **Volg de paden.** Lees een pad van achteren: de laatste ID's zijn de
   repeaters waar de flood langskwam. De vroegste echte zit dicht bij de
   bron. De ID's daarvoor kunnen [verzonnen](#forged) zijn.
2. **Beperk het gebied.** Als meerdere observers hetzelfde pakket horen,
   plaatsen ze de afzender in een gebied. De
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) rekent het uit
   met de repeaters die het hoorden.
3. **Loop de laatste kilometer.** De repeaters horen de bron alleen aan de
   rand van hun bereik. Voor het laatste stuk moeten mensen dus te voet op
   pad. [Mesh-Hunter](https://mesh-hunter.eu/) maakt een koppeling met je
   companion en legt elk pakket dat hij hoort vast met je GPS-positie. Lopen
   er meerdere mensen tegelijk, dan vind je de bron sneller.
4. **Laat het je [lokale groep](/community/) weten.** Die ziet meer van de
   mesh, beslist wat er daarna gebeurt en neemt contact op met wie met opzet
   floodt.

## Vul aan wat je zag {#add}

Kreeg je te maken met een flood die niet
in deze tabellen staat? Heeft een instelling er een gestopt? Vertel het ons
op [Discord](https://discord.meshcore-info.eu/): wat je zag en wat je
aanzette. We zetten het op de pagina.
