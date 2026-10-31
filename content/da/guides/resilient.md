---
title: Gør meshet robust
lead: Er meshet nær dig langsomt eller fyldt med skrald? Find ud af, hvad der skyldes det, slå den repeater-indstilling til, der stopper det, og sig det til din lokale gruppe.
description: 'Floods og spam på et MeshCore-mesh: sådan genkender du hver slags, hvilken repeater-indstilling der hjælper, hvordan du ser et flood, og hvordan du finder kilden.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-10-31'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Kommer beskeder for sent eller slet ikke frem? Fyldes Public med skrald? Så
er det et flood: mere trafik, end meshet kan bære, sendt ved en fejl eller
med vilje. Find det, du ser, i tabellerne nedenfor. Hver række nævner den
indstilling, der stopper det. Slå den til på din repeater, den node, der
sender beskeder videre. Sig det derefter til din [lokale gruppe](/community/),
så repeaterne omkring dig gør det samme. Hver repeater, der smider et flood
væk, levner sendetid til alle andre.

## Floods ved en fejl {#mistake}

Et flood ved en fejl kommer fra en node, hvis ejer ikke ved, at den skaber
et. Det stopper, så snart ejeren ved det. En advert i tabellerne nedenfor er
den hilsen, en node sender, så andre kan finde den.

Indstillingerne i tabellerne bygger på det, firmwaren gør. Ikke alle har
endnu stoppet et flood på et rigtigt mesh.

{{< callout type="warning" >}}
Nogle indstillinger på denne side kræver DMC-firmwaren. Standard-**MeshCore**
1.18.0 har regioner, hop-grænserne `flood.max.*`, loop-detektion og duty
cycle. Pakkefilteret, de regler, din repeater bruger til at smide skrald
væk, følger med **DMC-firmwaren** fra
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Det gør
duty-cycle gating og companion-filteret også. Denne side følger DMC
1.18.0-dev-buildet `ecfb2d4` fra 19. oktober 2026. Siden om
[pakkefilteret](/guides/filter/#firmware) fortæller, hvor du får den.
{{< /callout >}}

| Hvad du ser | Hvad det er | Hvad der hjælper |
| --- | --- | --- |
| Forespørgsler til repeatere fra én node, dag og nat, og et mesh, der er langsomt i flere dage | En hjemmeautomatisering eller en bot, der beder repeatere om deres status for tit | `filter on`. Pakkefilteret lader så 5 forespørgsler i minuttet passere. Sig det til ejeren. |
| Den samme slags besked på en kanal hvert minut | En bot, der poster for tit | [Bloker kanalen](/guides/filter/#channel) eller [brems afsenderen](/guides/filter/#sender). Sig det til ejeren. |
| Ulæselige beskeder på Public og andre kanaler | En node med defekt firmware eller forkerte radioindstillinger | `filter malformed on` smider dem væk på Public. Sig det til ejeren. |
| Én nodes advert med få minutters mellemrum | En node, der er sat til at sende advert for tit | `filter advert 24` lader hver nodes advert passere én gang i døgnet. `set flood.max.advert 3` holder adverts inden for 3 hop. |
| Beskeder langvejs fra med regioner, der ikke hører til her | En bro, der forbinder mesh over internettet | `set flood.max.unscoped 1`, og læg kun din repeater i de [regioner, den betjener](/guides/settings/#traffic). |
| Den samme besked kommer igen og igen, med din repeaters ID mere end én gang i stien | En repeater, der ændrer pakker og sender dem videre, så de kører i ring | Loop-detektion står som standard på `minimal`. `set loop.detect moderate` smider et loop væk hurtigere. |

## Floods med vilje {#purpose}

Nogle floods er spam: skrald, der sendes med vilje for at tilstoppe meshet.
Afsenderen skifter navne, nøgler og stier, så ingen enkelt regel stopper
floodet.

| Hvad du ser | Hvad det er | Hvad der hjælper |
| --- | --- | --- |
| Mange nye noder med tilfældige navne, hver med en ny nøgle | Falske adverts | `filter rate 04 5 60` lader 5 adverts i minuttet passere. `filter advert` hjælper ikke: hver advert kommer fra en [ny nøgle](#forged). |
| Beskeder med ulæselig tekst fra opdigtede afsendere, ofte dateret mere end et år tilbage | Kanalspam | `filter malformed on` smider dem væk på Public. `filter age 60` smider dem med gammel dato væk på Public og på [overvågede kanaler](/guides/filter/#settings). |
| Op til 200 direkte beskeder i minuttet til noder, der ikke findes, og ingen kvitteringer tilbage | Et flood af direkte beskeder | `filter rate 02 5 60`. Din app viser ikke disse beskeder. Det gør en observer. |
| Byger af forespørgsler fra én node til snesevis af andre | Forespørgselsspam | Med `filter on` lader pakkefilteret 5 forespørgsler i minuttet passere. |
| En besked kommer tilbage 10 til 20 minutter senere med næsten den samme sti | Replay: en kopi, der sendes igen | En repeater husker de sidste 160 pakker, den har set. På et travlt mesh passerer en senere kopi derfor igen. `filter age` smider en gruppebesked væk, hvis den er ældre, end du tillader. |
| Beskeder fra Public sendt igen under en opdigtet afsender, nogle gange med en gammel dato | Ekkospam | `filter age 60`. `filter malformed on` smider også en besked væk, hvis datoen er mere end en uge forkert. |
| En besked med få sekunders mellemrum på flere kanaler, hver fra et nyt navn, med almindelige spørgsmål | En bølge af bots | `filter rate 05 10 60`, og [bloker de kanaler](/guides/filter/#channel), dit område ikke bruger. Hvert navn er nyt, så [afsenderreglerne](#forged) rammer ikke. |

## Det har virket {#worked}

Lokale grupper har stoppet floods med disse skridt:

1. **Sig det til ejeren.** Et flood ved en fejl stopper, så snart ejeren
   ved det. Send ejeren en venlig besked.
2. **Reager ikke på meshet.** Et svar viser en spammer, at spammen virker.
3. **Bed om observere.** En observer er en node, der rapporterer hver pakke,
   den hører, over MQTT. Jo flere observere omkring dig, jo hurtigere ser du,
   hvor et flood kommer ind. Gør din egen repeater til en observer med
   [MQTT på din observer](/guides/mqtt/).
4. **Find kilden.** Observere placerer afsenderen i et område. Den sidste
   kilometer kræver folk til fods med en radio. Se
   [Find kilden](#source).
5. **Få din lokale gruppe i gang.** Én repeater med de rigtige indstillinger
   hjælper. Sammen stopper alle repeatere i området et flood. Din
   [lokale gruppe](/community/) får hver ejer til at slå indstillingen til.

## Opdigtede afsendere og stier {#forged}

Afsenderen skriver selv disse dele af en pakke, og intet kontrollerer dem:

- **Afsenderens navn.** I en kanalbesked er navnet en del af teksten. Alle
  med kanalnøglen kan skrive et hvilket som helst navn.
- **Begyndelsen af stien.** Hver repeater tilføjer sit eget ID sidst i stien.
  Intet kontrollerer de ID'er, der stod der før, så en afsender kan begynde
  stien med opdigtede ID'er. Slutningen af stien er ægte.

{{< forged-path >}}

Derfor stopper `filter sender` og `filter path` kun en afsender, indtil
vedkommende skifter navn eller sti. En [stiblokering](/guides/filter/#path)
smider også den ægte trafik væk fra den repeater, hvis ID står i den.
Hastighedsgrænser, hop-grænser, alders- og malformed-kontrollerne,
kanalblokeringer, regioner og duty cycle virker stadig.

## Indstillinger til alle floods {#always}

Disse virker, uanset hvilket flood der rammer meshet:

- **Duty cycle på 10%.** Din repeater sender så aldrig mere, end loven
  tillader, uanset hvad der kommer ind.
  [Repeater-guiden](/repeater-guide/#duty-cycle) gennemgår det.
- **Regioner og hop-grænser.** En region er det område, en besked bliver i.
  En repeater sender kun beskeder videre i de regioner, den har, og
  `flood.max.*` holder trafikken tæt på. Begge står i
  [Hold trafikken nede](/guides/settings/#traffic).
- **Pakkefilteret til en travl repeater.** De
  [færdige indstillinger](/guides/filter/#busy) halverer gruppebeskeder
  og adverts. Prøv dem først i [dry-run](/guides/filter/#dryrun): den tæller
  kun, hvad den ville smide væk.
- **Companion-filteret i DMC-firmwaren.** Din companion, den node, du sender
  beskeder fra, holder skrald ude af din app. Den skjuler defekte og gamle
  beskeder samt beskeder fra en repeater, en afsender eller et ord, du
  blokerer. En afsender- eller ordregel
  skjuler kun beskeden for dig. Andre modtager den stadig.

### Duty-cycle gating {#gate}

I DMC-firmwaren kan din repeater give sin egen region forrang, når den får
travlt. Når den har sendt i mere end 35% af det sidste minut, holder den op
med at sende beskeder uden region videre. Har den stadig travlt, smider den
derefter den bredeste region væk, ét niveau ad gangen. Dens egen region
passerer altid. Det virker kun, hvis du har sat regioner på din repeater.
Slå det til, og tjek det:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Det, den smider væk, vises ikke i `filter stats`. Når repeateren er rolig
igen, kommer regionerne tilbage, den inderste først.

## Se et flood {#see}

Din app viser kun det, der når frem til dig. Kun en observer hører et flood
af direkte beskeder til noder, der ikke findes. Hver observer rapporterer
til [MeshCore Analyzer](https://meshcore-analyzer.eu/), hvor alle kan se
det. Gør din repeater til en observer med [MQTT på din observer](/guides/mqtt/).

Se på hver kopi af én pakke i Analyzer. Stien viser som regel, hvor den kom
fra. En flooder kan begynde stien med [opdigtede ID'er](#forged), så de
første ID'er siger dig intet. Men hver kopi har den samme opdigtede start.
Kopien med den korteste sti passerede færrest ægte repeatere. Den blev altså
hørt tættest på afsenderen.

{{< copies >}}

På din egen repeater viser `filter stats`, hvad pakkefilteret har smidt
væk. `filter stats top` viser den første byte af de node-ID'er, som de
fleste frasorterede pakker kommer fra. Mange noder deler den byte. Den
indsnævrer søgningen, men den navngiver ikke afsenderen.

## Find kilden {#source}

Når et flood bliver ved med at komme igen:

1. **Følg stierne.** Læs en sti bagfra: de sidste ID'er er de repeatere,
   floodet passerede. Den tidligste ægte er tæt på kilden. ID'erne før den
   kan være [opdigtede](#forged).
2. **Indsnævr området.** Hører flere observere den samme pakke, placerer de
   afsenderen i et område.
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) regner det ud
   fra de repeatere, der hørte den.
3. **Gå den sidste kilometer.** Repeaterne hører kun kilden i kanten af
   deres rækkevidde, så den sidste del kræver folk til fods.
   [Mesh-Hunter](https://mesh-hunter.eu/) parrer med din companion og logger
   hver pakke, den hører, med din GPS-position. Går flere personer på én
   gang, finder de den hurtigere.
4. **Sig det til din [lokale gruppe](/community/).** Gruppen ser mere af
   meshet, beslutter, hvad der skal ske, og kontakter den, der flooder med
   vilje.

## Tilføj det, du så {#add}

Er du blevet ramt af et flood, der ikke
står i tabellerne? Har en indstilling stoppet et? Fortæl os det på
[Discord](https://discord.meshcore-info.eu/): hvad du så, og hvad du slog
til. Vi tilføjer det på siden.
