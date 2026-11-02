---
title: Naredi mrežo odporno
lead: Je mreža v tvoji bližini počasna ali polna smeti? Ugotovi vzrok, na repetitorju vklopi nastavitev, ki to ustavi, in obvesti svojo lokalno skupino.
description: 'Poplave in spam v mreži MeshCore: kako prepoznaš posamezno vrsto, katera nastavitev repetitorja pomaga, kako vidiš poplavo in kako najdeš njen vir.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-11-02'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Sporočila prihajajo pozno ali sploh ne prispejo? Se Public polni s smetmi? To je
poplava: več prometa, kot ga mreža zmore prenesti, poslanega po pomoti ali
namerno. V spodnjih tabelah poišči to, kar vidiš. V vsaki vrstici piše,
katera nastavitev to ustavi. Vklopi jo na svojem repetitorju, vozlišču, ki
sporočila posreduje naprej. Nato obvesti svojo [lokalno skupino](/community/),
da enako storijo repetitorji okoli tebe. Vsak repetitor, ki zavrže poplavo,
pusti čas oddajanja vsem drugim.

## Nenamerne poplave {#mistake}

Nenamerno poplavo povzroči vozlišče, katerega lastnik za to ne ve. Ko izve,
se poplava ustavi. Najava (advert) v spodnjih tabelah je pozdrav, ki ga
vozlišče pošlje, da ga druga lahko najdejo.

Nastavitve v tabelah temeljijo na tem, kaj naredi vdelana programska oprema.
Niso še vse ustavile poplave v resnični mreži.

{{< callout type="warning" >}}
Nekatere nastavitve na tej strani zahtevajo vdelano programsko opremo DMC.
Standardni **MeshCore** 1.18.0 ima regije, omejitve skokov `flood.max.*`,
zaznavanje zank in delovni cikel. Paketni filter, torej pravila, s katerimi
tvoj repetitor zavrže smeti, je del **vdelane programske opreme DMC** skupine
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Del nje sta tudi
omejevanje po delovnem ciklu in filter za companion. Ta stran se ravna po
razvojni različici DMC 1.18.0 `ecfb2d4` z dne 19. oktobra 2026. Na strani
[paketni filter](/guides/filter/#firmware) piše, kje jo dobiš.
{{< /callout >}}

| Kaj vidiš | Kaj je to | Kaj pomaga |
| --- | --- | --- |
| Zahteve repetitorjem z enega vozlišča, podnevi in ponoči, ter mreža, ki več dni ostane počasna | Hišna avtomatizacija ali bot, ki repetitorje prepogosto sprašuje po stanju | `filter on`. Paketni filter nato prepusti 5 zahtev na minuto. Obvesti lastnika. |
| Ista vrsta sporočila na kanalu, vsako minuto | Bot, ki objavlja prepogosto | [Blokiraj kanal](/guides/filter/#channel) ali [upočasni pošiljatelja](/guides/filter/#sender). Obvesti lastnika. |
| Neberljiva sporočila na Public in drugih kanalih | Vozlišče s pokvarjeno vdelano programsko opremo ali napačnimi radijskimi nastavitvami | `filter malformed on` jih na Public zavrže. Obvesti lastnika. |
| Najava enega vozlišča vsakih nekaj minut | Vozlišče, ki je nastavljeno na prepogoste najave | `filter advert 24` prepusti najavo vsakega vozlišča enkrat na dan. `set flood.max.advert 3` omeji najave na 3 skoke. |
| Sporočila od daleč, z regijami, ki ne spadajo sem | Most, ki povezuje mreže prek interneta | `set flood.max.unscoped 1`, repetitor pa uvrsti samo v [regije, ki jih pokriva](/guides/settings/#traffic). |
| Isto sporočilo gre skozi vedno znova, ID tvojega repetitorja pa je na njegovi poti večkrat | Repetitor, ki pakete spreminja in posreduje naprej, zato krožijo v zanki | Zaznavanje zank privzeto deluje na ravni `minimal`. `set loop.detect moderate` zanko zavrže prej. |

## Namerne poplave {#purpose}

Nekatere poplave so spam: smeti, ki jih nekdo namerno pošilja, da zamaši mrežo.
Pošiljatelj menja imena, ključe in poti, zato poplave ne ustavi nobeno posamezno
pravilo.

| Kaj vidiš | Kaj je to | Kaj pomaga |
| --- | --- | --- |
| Veliko novih vozlišč z naključnimi imeni, vsako z novim ključem | Lažne najave | `filter rate 04 5 60` prepusti 5 najav na minuto. `filter advert` ne pomaga: vsaka najava pride z [novega ključa](#forged). |
| Sporočila z neberljivim besedilom od izmišljenih pošiljateljev, pogosto z datumom, starejšim od enega leta | Spam na kanalih | `filter malformed on` jih na Public zavrže. `filter age 60` zavrže tista s starim datumom na Public in na [nadzorovanih kanalih](/guides/filter/#settings). |
| Do 200 neposrednih sporočil na minuto vozliščem, ki ne obstajajo, brez povratnih potrditev | Poplava neposrednih sporočil | `filter rate 02 5 60`. Tvoja aplikacija teh sporočil ne prikaže, opazovalec pa jih pokaže. |
| Izbruhi zahtev z enega vozlišča več deset drugim | Spam z zahtevami | Z ukazom `filter on` paketni filter prepusti 5 zahtev na minuto. |
| Sporočilo se vrne 10 do 20 minut pozneje, s skoraj enako potjo | Ponovitev (replay): znova poslana kopija | Repetitor si zapomni zadnjih 160 paketov, ki jih je videl, zato v zasedeni mreži poznejša kopija spet gre skozi. `filter age` zavrže skupinsko sporočilo, ki je starejše, kot dovoliš. |
| Sporočila s Public, znova poslana pod izmišljenim pošiljateljem, včasih s starim datumom | Odmevni spam | `filter age 60`. `filter malformed on` zavrže tudi datum, ki odstopa za več kot en teden. |
| Sporočilo vsakih nekaj sekund na več kanalih, vsako z novim imenom, z vsakdanjimi vprašanji | Val botov | `filter rate 05 10 60`, poleg tega [blokiraj kanale](/guides/filter/#channel), ki jih na tvojem območju ne uporabljate. Vsako ime je novo, zato ga [pravila za pošiljatelje](#forged) ne ujamejo. |

## Kaj je delovalo {#worked}

Lokalne skupine so poplave ustavile s temi koraki:

1. **Obvesti lastnika.** Nenamerna poplava se ustavi, ko njen lastnik izve zanjo.
   Pošlji mu prijazno sporočilo.
2. **Ne odzivaj se v mreži.** Odgovor spamerju pokaže, da spam deluje.
3. **Prosi za opazovalce.** Opazovalec je vozlišče, ki prek MQTT sporoča vsak
   paket, ki ga sliši. Več ko je opazovalcev okoli tebe, prej vidiš, kje poplava
   vstopi. Svoj repetitor spremeni v opazovalca z
   [MQTT na opazovalcu](/guides/mqtt/).
4. **Poišči vir.** Opazovalci pošiljatelja umestijo na neko območje. Zadnji
   kilometer morajo ljudje prehoditi z radiem. Glej
   [Poišči vir](#source).
5. **Aktiviraj svojo lokalno skupino.** En repetitor s pravimi nastavitvami
   pomaga. Vsi repetitorji na območju skupaj poplavo ustavijo. Tvoja
   [lokalna skupina](/community/) poskrbi, da nastavitev vklopi vsak lastnik.

## Izmišljeni pošiljatelji in poti {#forged}

Te dele paketa napiše pošiljatelj in nič jih ne preverja:

- **Ime pošiljatelja.** V sporočilu na kanalu je ime del besedila. Kdor ima
  ključ kanala, lahko napiše katero koli ime.
- **Začetek poti.** Vsak repetitor doda svoj ID na konec poti. Nič ne preverja
  ID-jev, ki so bili tam že prej, zato lahko pošiljatelj pot začne z izmišljenimi.
  Konec poti je resničen.

{{< forged-path >}}

Zato `filter sender` in `filter path` pošiljatelja ustavita samo, dokler ne
zamenja imena ali poti. [Blokada poti](/guides/filter/#path) zavrže tudi resnični
promet repetitorja, katerega ID je v njej. Omejitve hitrosti, omejitve skokov,
preverjanje starosti in pokvarjenih sporočil, blokade kanalov, regije in delovni
cikel še naprej delujejo.

## Nastavitve za vsako poplavo {#always}

Te nastavitve veljajo, ne glede na to, kaj preplavlja mrežo:

- **Delovni cikel na 10%.** Tvoj repetitor potem nikoli ne oddaja več, kot dovoli
  zakon, ne glede na to, kaj prihaja. To pojasnjuje
  [vodnik za repetitorje](/repeater-guide/#duty-cycle).
- **Regije in omejitve skokov.** Regija je območje, v katerem sporočilo ostane.
  Repetitor posreduje samo sporočila v regijah, ki jih ima, `flood.max.*`
  pa promet zadrži v bližini. Oboje je opisano v poglavju
  [Zmanjšaj promet](/guides/settings/#traffic).
- **Paketni filter za zaseden repetitor.** [Pripravljene nastavitve](/guides/filter/#busy)
  prepolovijo skupinska sporočila in najave. Najprej jih preizkusi v načinu
  [dry-run](/guides/filter/#dryrun): ta samo šteje, kaj bi zavrgel.
- **Filter za companion v vdelani programski opremi DMC.** Tvoj companion, vozlišče,
  s katerega pišeš sporočila, ne spusti smeti v tvojo aplikacijo. Skrije pokvarjena
  in stara sporočila ter sporočila z repetitorjem, pošiljateljem ali besedo, ki jih
  blokiraš. Pravilo za pošiljatelja ali besedo sporočilo skrije samo tebi: drugi ga
  še vedno prejmejo.

### Omejevanje po delovnem ciklu {#gate}

V vdelani programski opremi DMC lahko tvoj repetitor, ko je zaseden, da prednost
svoji regiji. Ko je oddajal več kot 35% zadnje minute, neha posredovati sporočila
brez regije. Če ostane zaseden, nato zavrže najširšo regijo, po eno raven naenkrat.
Svojo regijo vedno prepusti. To deluje samo, če so na tvojem repetitorju
nastavljene regije. Vklopi omejevanje in ga preveri:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Kar pri tem zavrže, se v `filter stats` ne pokaže. Ko se repetitor spet umiri, se
regije vrnejo, najprej najbolj notranja.

## Kako vidiš poplavo {#see}

Tvoja aplikacija prikaže samo to, kar pride do tebe. Poplavo neposrednih sporočil
vozliščem, ki ne obstajajo, sliši samo opazovalec. Vsak opazovalec poroča
v [MeshCore Analyzer](https://meshcore-analyzer.eu/), kjer lahko to vidi vsak.
Svoj repetitor spremeni v opazovalca z
[MQTT na opazovalcu](/guides/mqtt/).

V Analyzerju si oglej vse kopije enega paketa. Njegova pot navadno pokaže, od kod
je prišel. Pošiljatelj poplave lahko pot začne z
[izmišljenimi ID-ji](#forged), zato ti prvi ID-ji ne povedo ničesar. Toda vsaka
kopija ima isti izmišljeni začetek. Kopija z najkrajšo potjo je šla skozi najmanj
resničnih repetitorjev, zato so jo slišali najbliže pošiljatelju.

{{< copies >}}

Na tvojem repetitorju `filter stats` pokaže, kaj je paketni filter zavrgel.
`filter stats top` pokaže prvi bajt ID-jev vozlišč, od katerih je največ zavrženih
paketov. Ta bajt ima veliko vozlišč, zato iskanje zoži, pošiljatelja pa ne
razkrije.

## Poišči vir {#source}

Ko se poplava kar naprej vrača:

1. **Sledi potem.** Pot beri od konca: zadnji ID-ji so repetitorji, skozi katere je
   šla poplava. Najzgodnejši resnični je blizu vira. ID-ji pred njim so lahko
   [izmišljeni](#forged).
2. **Zoži območje.** Več opazovalcev, ki slišijo isti paket, umesti pošiljatelja na
   neko območje. [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) to
   izračuna iz repetitorjev, ki so ga slišali.
3. **Prehodi zadnji kilometer.** Repetitorji slišijo vir samo na robu svojega dosega,
   zato morajo ljudje zadnji del prehoditi peš.
   [Mesh-Hunter](https://mesh-hunter.eu/) se poveže s tvojim companionom in vsak
   slišani paket zabeleži s tvojim GPS položajem. Več ljudi, ki hodijo hkrati, vir
   najde prej.
4. **Obvesti svojo [lokalno skupino](/community/).** Člani vidijo večji del mreže,
   odločijo o naslednjih korakih in stopijo v stik s tistim, ki namerno povzroča
   poplavo.

## Dodaj, kar si videl {#add}

Te je zadela poplava, ki je ni v teh tabelah? Je kakšna nastavitev katero ustavila?
Povej nam na [Discordu](https://discord.meshcore-info.eu/): kaj si videl in kaj si
vklopil. To dodamo na stran.
