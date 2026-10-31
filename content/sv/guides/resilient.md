---
title: Gör meshen tålig
lead: Är meshen nära dig långsam eller full av skräp? Ta reda på vad som orsakar det, slå på den repeater-inställning som stoppar det och berätta för din lokala grupp.
description: 'Floods och spam i ett MeshCore-mesh: hur du känner igen varje sort, vilken repeater-inställning som hjälper, hur du ser en flood och hur du hittar källan.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-10-31'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Kommer meddelanden fram sent eller inte alls? Fylls Public med skräp? Då är
det en flood: mer trafik än meshen klarar av, skickad av misstag eller med
flit. Leta upp det du ser i tabellerna nedan. Varje rad anger inställningen
som stoppar det. Slå på den i din repeater, noden som skickar meddelanden
vidare. Berätta sedan för din [lokala grupp](/community/), så att
repeatrarna runt dig gör likadant. Varje repeater som kastar en flood
lämnar sändningstid åt alla andra.

## Floods av misstag {#mistake}

En flood av misstag kommer från en nod vars ägare inte vet att den orsakar
en. Den slutar när ägaren får veta. I tabellerna nedan är en advert det
hej som en nod skickar så att andra kan hitta den.

Inställningarna i tabellerna bygger på vad firmwaren gör. Inte alla har
ännu stoppat en flood i ett riktigt mesh.

{{< callout type="warning" >}}
Vissa inställningar på den här sidan kräver DMC-firmwaren. Standardversionen
av **MeshCore** 1.18.0 har regioner, hoppgränserna `flood.max.*`,
loopdetektering och duty cycle. Paketfiltret, reglerna som låter din
repeater kasta skräp, ingår i **DMC-firmwaren** från
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Det gör
också duty-cycle-spärren och companion-filtret. Den här sidan utgår från
DMC 1.18.0-utvecklingsversionen `ecfb2d4` från 19 oktober 2026. På sidan om
[paketfiltret](/guides/filter/#firmware) står var du hämtar den.
{{< /callout >}}

| Det du ser | Vad det är | Det som hjälper |
| --- | --- | --- |
| Förfrågningar till repeatrar från en nod, dag och natt, och ett mesh som är långsamt i flera dagar | En hemautomation eller en bot som frågar repeatrar om deras status för ofta | `filter on`. Paketfiltret släpper då igenom 5 förfrågningar i minuten. Säg till ägaren. |
| Samma sorts meddelande i en kanal, varje minut | En bot som postar för ofta | [Blockera kanalen](/guides/filter/#channel) eller [bromsa avsändaren](/guides/filter/#sender). Säg till ägaren. |
| Oläsliga meddelanden i Public och andra kanaler | En nod med trasig firmware eller fel radioinställningar | `filter malformed on` kastar dem i Public. Säg till ägaren. |
| En nods advert med några minuters mellanrum | En nod som är inställd på att skicka advert för ofta | `filter advert 24` släpper igenom varje nods advert en gång per dygn. `set flood.max.advert 3` håller adverts inom 3 hopp. |
| Meddelanden från långt bort, med regioner som inte hör hemma här | En brygga som kopplar ihop mesh över internet | `set flood.max.unscoped 1`, och lägg din repeater bara i de [regioner den betjänar](/guides/settings/#traffic). |
| Samma meddelande passerar om och om igen, med din repeaters ID mer än en gång i vägen | En repeater som ändrar paket och skickar dem vidare, så att de går i loop | Loopdetekteringen står på `minimal` som standard. `set loop.detect moderate` stoppar en loop tidigare. |

## Floods med flit {#purpose}

Vissa floods är spam: skräp som någon skickar med flit för att täppa till
meshen. Avsändaren byter namn, nycklar och vägar, så ingen enskild regel
stoppar flooden.

| Det du ser | Vad det är | Det som hjälper |
| --- | --- | --- |
| Många nya noder med slumpmässiga namn, var och en med en ny nyckel | Falska adverts | `filter rate 04 5 60` släpper igenom 5 adverts i minuten. `filter advert` hjälper inte: varje advert kommer från en [ny nyckel](#forged). |
| Meddelanden med oläslig text från påhittade avsändare, ofta daterade för mer än ett år sedan | Kanalspam | `filter malformed on` kastar dem i Public. `filter age 60` kastar de gammaldaterade i Public och i [bevakade kanaler](/guides/filter/#settings). |
| Upp till 200 direktmeddelanden i minuten till noder som inte finns, och inga kvittenser tillbaka | En flood av direktmeddelanden | `filter rate 02 5 60`. Din app visar inte de här meddelandena, men en observer gör det. |
| Skurar av förfrågningar från en nod till dussintals andra | Förfrågningsspam | Med `filter on` släpper paketfiltret igenom 5 förfrågningar i minuten. |
| Ett meddelande kommer tillbaka 10 till 20 minuter senare, med nästan samma väg | Replay: en kopia som skickas igen | En repeater minns de senaste 160 paketen den har sett, så i ett livligt mesh passerar en senare kopia igen. `filter age` kastar ett gruppmeddelande som är äldre än du tillåter. |
| Meddelanden från Public som skickas igen under en påhittad avsändare, ibland med ett gammalt datum | Ekospam | `filter age 60`. `filter malformed on` kastar också ett datum som avviker mer än en vecka. |
| Ett meddelande med några sekunders mellanrum i flera kanaler, vart och ett från ett nytt namn, med vanliga frågor | En botvåg | `filter rate 05 10 60`, och [blockera de kanaler](/guides/filter/#channel) som ditt område inte använder. Varje namn är nytt, så [avsändarreglerna](#forged) missar det. |

## Det här har fungerat {#worked}

Lokala grupper har stoppat floods med de här stegen:

1. **Säg till ägaren.** En flood av misstag slutar när ägaren får veta.
   Skicka ett vänligt meddelande.
2. **Reagera inte i meshen.** Ett svar visar en spammare att spammet fungerar.
3. **Be om observers.** En observer är en nod som rapporterar varje paket
   den hör via MQTT. Ju fler observers runt dig, desto snabbare ser du var
   en flood kommer in. Gör din egen repeater till en observer med
   [MQTT på din observer](/guides/mqtt/).
4. **Hitta källan.** Observers placerar avsändaren inom ett område. Den
   sista kilometern kräver folk till fots med en radio. Se
   [Hitta källan](#source).
5. **Få igång din lokala grupp.** En repeater med rätt inställningar
   hjälper. Alla repeatrar i området tillsammans stoppar en flood. Din
   [lokala grupp](/community/) får varje ägare att slå på inställningen.

## Påhittade avsändare och vägar {#forged}

Avsändaren skriver de här delarna av ett paket, och ingen kontrollerar dem:

- **Avsändarens namn.** I ett kanalmeddelande är namnet en del av texten.
  Alla som har kanalnyckeln kan skriva vilket namn som helst.
- **Början av vägen.** Varje repeater lägger till sitt eget ID i slutet av
  vägen. Ingen kontrollerar de ID:n som redan fanns där, så en avsändare kan
  börja vägen med påhittade. Slutet av vägen är äkta.

{{< forged-path >}}

Därför stoppar `filter sender` och `filter path` en avsändare bara tills
den byter namn eller väg. En [vägblockering](/guides/filter/#path) kastar
också den äkta trafiken från den repeater vars ID ingår i den.
Hastighetsgränser, hoppgränser, ålders- och felkontrollerna,
kanalblockeringar, regioner och duty cycle fortsätter att fungera.

## Inställningar för alla floods {#always}

De här håller oavsett vad som floodar meshen:

- **Duty cycle på 10%.** Då sänder din repeater aldrig mer än lagen
  tillåter, oavsett vad som kommer in. Mer om det i
  [repeater-guiden](/repeater-guide/#duty-cycle).
- **Regioner och hoppgränser.** En region är det område ett meddelande
  stannar inom. En repeater skickar bara vidare meddelanden i de regioner
  den har, och `flood.max.*` håller trafiken nära. Båda finns i
  [Håll nere trafiken](/guides/settings/#traffic).
- **Paketfiltret för en livlig repeater.** De
  [färdiga inställningarna](/guides/filter/#busy) halverar gruppmeddelanden
  och adverts. Testa dem först i [dry-run](/guides/filter/#dryrun): då
  räknar filtret bara det som det skulle ha kastat.
- **Companion-filtret, i DMC-firmwaren.** Din companion, noden du skickar
  meddelanden från, håller skräp borta från din app. Den döljer trasiga och
  gamla meddelanden, och meddelanden från en repeater, en avsändare eller
  ett ord som du blockerar. En regel för avsändare eller ord
  döljer bara meddelandet för dig, andra får det fortfarande.

### Duty-cycle-spärr {#gate}

I DMC-firmwaren kan din repeater prioritera sin egen region när det blir
livligt. När den har sänt mer än 35% av den senaste minuten slutar den
skicka vidare meddelanden utan region. Om det fortsätter vara livligt
släpper den sedan den bredaste regionen, en nivå i taget. Dess egen region
går alltid igenom. Det fungerar bara om du har satt regioner på din
repeater. Slå på spärren och kontrollera den:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Det som spärren kastar syns inte i `filter stats`. När repeatern är lugn
igen kommer regionerna tillbaka, den innersta först.

## Se en flood {#see}

Din app visar bara det som når dig. Bara en observer hör en flood av
direktmeddelanden till noder som inte finns. Varje observer rapporterar
till [MeshCore Analyzer](https://meshcore-analyzer.eu/), där alla kan se
det. Gör din repeater till en observer med [MQTT på din observer](/guides/mqtt/).

Titta på varje kopia av ett paket i Analyzer. Vägen visar oftast var det
kom ifrån. Den som floodar kan börja vägen med
[påhittade ID:n](#forged), så de första ID:na säger dig ingenting. Men
varje kopia bär samma påhittade början. Kopian med kortast väg passerade
färst äkta repeatrar, så den hördes närmast avsändaren.

{{< copies >}}

På din egen repeater visar `filter stats` vad paketfiltret har kastat.
`filter stats top` visar den första byten i nod-ID:na bakom flest
kastade paket. Många noder delar den byten, så den begränsar sökningen men
pekar inte ut avsändaren.

## Hitta källan {#source}

När en flood fortsätter att komma tillbaka:

1. **Följ vägarna.** Läs en väg från slutet: de sista ID:na är repeatrarna
   som flooden passerade. Det tidigaste äkta ID:t finns nära källan, och
   ID:na före det kan vara [påhittade](#forged).
2. **Ringa in området.** Flera observers som hör samma paket placerar
   avsändaren inom ett område.
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) räknar ut det
   utifrån repeatrarna som hörde paketet.
3. **Gå den sista kilometern.** Repeatrarna hör källan bara i kanten av sin
   räckvidd, så den sista biten kräver folk till fots.
   [Mesh-Hunter](https://mesh-hunter.eu/) parkopplas med din companion och
   loggar varje paket den hör tillsammans med din GPS-position. Flera
   personer som går samtidigt hittar källan snabbare.
4. **Berätta för din [lokala grupp](/community/).** De ser mer av meshen,
   de bestämmer vad som händer sedan och de kontaktar den som floodar med
   flit.

## Lägg till det du såg {#add}

Har du drabbats av en flood som inte
finns i tabellerna? Har en inställning stoppat en? Berätta för oss på
[Discord](https://discord.meshcore-info.eu/): vad du såg och vad du slog
på. Vi lägger till det på sidan.
