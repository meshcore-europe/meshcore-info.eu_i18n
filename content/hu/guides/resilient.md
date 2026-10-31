---
title: Tedd ellenállóvá a mesht
lead: Lassú a mesh a környékeden, vagy tele van szeméttel? Derítsd ki, mi okozza, kapcsold be az átjátszón a beállítást, amely megállítja, és szólj a helyi csoportodnak.
description: 'Floodok és spam egy MeshCore meshen: hogyan ismered fel az egyes fajtákat, melyik átjátszó-beállítás segít, hogyan látod a floodot, és hogyan találod meg a forrását.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-10-31'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Késve érkeznek az üzenetek, vagy meg sem érkeznek? Megtelik a Public szeméttel?
Ez egy flood: több forgalom, mint amennyit a mesh elbír. Valaki tévedésből
vagy szándékosan küldi. Keresd meg a lenti táblázatokban, amit látsz. Minden
sor megnevezi a beállítást, amely megállítja. Kapcsold be az átjátszódon.
Az átjátszó az a csomópont, amely továbbadja az üzeneteket. Aztán szólj a
[helyi csoportodnak](/community/), hogy a környékbeli átjátszók is így
tegyenek. Minden átjátszó, amely eldobja a floodot, adásidőt hagy a többieknek.

## Tévedésből indult floodok {#mistake}

A tévedésből indult flood egy olyan csomóponttól jön, amelynek a gazdája nem
tudja, hogy floodot okoz. Amint megtudja, a flood leáll. A lenti
táblázatokban az advert az a köszöntés, amelyet egy csomópont kiküld, hogy a
többiek megtalálják.

A táblázatok beállításai abból következnek, amit a firmware csinál. Nem
mindegyik állított már meg floodot valódi meshen.

{{< callout type="warning" >}}
Az oldal néhány beállításához a DMC firmware kell. A gyári **MeshCore** 1.18.0
tudja a régiókat, a `flood.max.*` ugráskorlátokat, a hurokfelismerést és a
kitöltési tényezőt. A csomagszűrő olyan szabályok sora, amelyekkel az
átjátszód eldobja a szemetet. Ezt a [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore)
**DMC firmware**-e adja. A kitöltésitényező-alapú kapuzást és a companion
szűrőt is ez adja. Ez az oldal a DMC 1.18.0 `ecfb2d4` fejlesztői buildjét követi,
2026. október 19-ről. A [csomagszűrő](/guides/filter/#firmware) oldalán
megtalálod, honnan töltheted le.
{{< /callout >}}

| Amit látsz | Mi ez | Mi segít |
| --- | --- | --- |
| Egy csomópont éjjel-nappal kéréseket küld az átjátszóknak, és a mesh napokig lassú marad | Egy okosotthon-rendszer vagy bot, amely túl gyakran kéri le az átjátszók állapotát | `filter on`. A csomagszűrő ezután percenként 5 kérést enged át. Szólj a gazdának. |
| Ugyanolyan üzenet egy csatornán, percenként | Egy bot, amely túl gyakran posztol | [Tiltsd le a csatornát](/guides/filter/#channel), vagy [lassítsd le a küldőt](/guides/filter/#sender). Szólj a gazdának. |
| Olvashatatlan üzenetek a Public és más csatornákon | Egy csomópont hibás firmware-rel vagy rossz rádióbeállításokkal | A `filter malformed on` eldobja ezeket a Public csatornán. Szólj a gazdának. |
| Egy csomópont advertje néhány percenként | Egy csomópont, amelyet túl gyakori advertre állítottak | A `filter advert 24` minden csomópont advertjét naponta egyszer engedi át. A `set flood.max.advert 3` 3 ugráson belül tartja az advertöket. |
| Messziről jövő üzenetek, ide nem tartozó régiókkal | Egy híd, amely az interneten keresztül köt össze mesheket | `set flood.max.unscoped 1`, és az átjátszódat csak azokba a [régiókba tedd, amelyeket kiszolgál](/guides/settings/#traffic). |
| Ugyanaz az üzenet újra és újra átmegy, az útvonalában többször is szerepel az átjátszód azonosítója | Egy átjátszó, amely módosítja és továbbadja a csomagokat, így azok hurokba kerülnek | A hurokfelismerés alapból `minimal` szinten fut. A `set loop.detect moderate` hamarabb eldobja a hurkot. |

## Szándékos floodok {#purpose}

Egyes floodok spamek: szándékosan küldött szemét, hogy eldugítsa a mesht. A
küldő váltogatja a neveket, kulcsokat és útvonalakat, ezért egyetlen szabály
sem állítja meg a floodot.

| Amit látsz | Mi ez | Mi segít |
| --- | --- | --- |
| Sok új csomópont véletlenszerű névvel, mindegyik új kulccsal | Hamis advertek | A `filter rate 04 5 60` percenként 5 advertet enged át. A `filter advert` nem segít: minden advert [új kulcstól](#forged) jön. |
| Olvashatatlan szövegű üzenetek kitalált küldőktől, gyakran több mint egy évvel korábbi dátummal | Csatornaspam | A `filter malformed on` eldobja ezeket a Public csatornán. A `filter age 60` eldobja a régi dátumúakat a Public és a [figyelt csatornákon](/guides/filter/#settings). |
| Percenként akár 200 közvetlen üzenet nem létező csomópontoknak, és nem jön vissza nyugta | Közvetlen üzenetek floodja | `filter rate 02 5 60`. Az appod nem mutatja ezeket az üzeneteket, egy observer igen. |
| Kéréssorozatok egy csomóponttól több tucat másiknak | Kérésspam | `filter on` mellett a csomagszűrő percenként 5 kérést enged át. |
| Egy üzenet 10–20 perccel később visszatér, majdnem ugyanazzal az útvonallal | Replay: újra elküldött másolat | Az átjátszó az utolsó 160 látott csomagot jegyzi meg, így forgalmas meshen egy későbbi másolat újra átmegy. A `filter age` eldobja a megengedettnél régebbi csoportüzenetet. |
| A Public üzenetei újra kiküldve, kitalált küldő nevében, néha régi dátummal | Visszhangspam | `filter age 60`. A `filter malformed on` a több mint egy héttel eltérő dátumot is eldobja. |
| Néhány másodpercenként egy üzenet több csatornán, mindig új névvel, hétköznapi kérdésekkel | Bothullám | `filter rate 05 10 60`, és [tiltsd le azokat a csatornákat](/guides/filter/#channel), amelyeket a környéked nem használ. Minden név új, ezért a [küldőszabályok](#forged) nem fogják meg. |

## Ami bevált {#worked}

A helyi csoportok ezekkel a lépésekkel állították meg a floodokat:

1. **Szólj a gazdának.** A tévedésből indult flood leáll, amint a gazdája
   tud róla. Küldj neki egy barátságos üzenetet.
2. **Ne reagálj a meshen.** Egy válaszból a spammer látja, hogy a spam hat.
3. **Kérj observereket.** Az observer olyan csomópont, amely minden hallott
   csomagot jelent MQTT-n. Minél több observer van körülötted, annál
   hamarabb látod, hol jön be a flood. A saját átjátszódat is observerré
   teheted: lásd [MQTT az observereden](/guides/mqtt/).
4. **Keresd meg a forrást.** Az observerek egy területre szűkítik a küldő helyét.
   Az utolsó kilométert emberek járják be gyalog, rádióval. Lásd:
   [A forrás megkeresése](#source).
5. **Mozgósítsd a helyi csoportodat.** Egy jól beállított átjátszó is segít.
   A környék összes átjátszója együtt állítja meg a floodot. A
   [helyi csoportod](/community/) eléri, hogy minden gazda bekapcsolja a
   beállítást.

## Kitalált küldők és útvonalak {#forged}

A csomag alábbi részeit a küldő írja, és semmi sem ellenőrzi őket:

- **A küldő neve.** Csatornaüzenetben a név a szöveg része. Bárki, akinek
  megvan a csatornakulcs, bármilyen nevet írhat.
- **Az útvonal eleje.** Minden átjátszó az útvonal végére fűzi a saját
  azonosítóját. A korábbi azonosítókat semmi sem ellenőrzi, így a küldő
  kitalált azonosítókkal kezdheti az útvonalat. Az útvonal vége valódi.

{{< forged-path >}}

Ezért a `filter sender` és a `filter path` csak addig állítja meg a küldőt,
amíg az meg nem változtatja a nevét vagy az útvonalát. Egy
[útvonaltiltás](/guides/filter/#path) annak az átjátszónak a valódi
forgalmát is eldobja, amelynek az azonosítója benne van. A sebességkorlátok,
az ugráskorlátok, a kor- és hibásformátum-ellenőrzés, a csatornatiltások, a
régiók és a kitöltési tényező továbbra is működnek.

## Beállítások minden floodra {#always}

Ezek érvényesek, bármi árasztja is el a mesht:

- **10% kitöltési tényező.** Így az átjátszód sosem ad többet, mint amennyit
  a törvény enged, bármi jön is be. Az
  [átjátszó-útmutató](/repeater-guide/#duty-cycle) foglalkozik vele.
- **Régiók és ugráskorlátok.** A régió az a terület, amelyen belül egy
  üzenet marad. Az átjátszó csak a nála beállított régiók üzeneteit adja
  tovább, a `flood.max.*` pedig a közelben tartja a forgalmat. Mindkettőt
  megtalálod itt: [A forgalom visszafogása](/guides/settings/#traffic).
- **Csomagszűrő forgalmas átjátszóhoz.** A
  [kész beállítások](/guides/filter/#busy) megfelezik a csoportüzeneteket és
  az advertöket. Előbb próbáld ki őket [dry-run](/guides/filter/#dryrun)
  módban: ekkor a szűrő csak számolja, mit dobna el.
- **A companion szűrő, a DMC firmware-ben.** A companionöd az a csomópont,
  amelyről üzenetet küldesz. Távol tartja a szemetet az appodtól. Elrejti
  a hibás és a régi üzeneteket, valamint azokat, amelyek letiltott átjátszótól
  vagy küldőtől jönnek, vagy letiltott szót tartalmaznak. Egy küldő- vagy szószabály
  csak előled rejti el az üzenetet, mások továbbra is megkapják.

### Kitöltésitényező-alapú kapuzás {#gate}

A DMC firmware-ben az átjátszód elsőbbséget adhat a saját régiójának, ha
leterhelt. Ha az utolsó perc több mint 35%-ában adott, már nem adja tovább a
régió nélküli üzeneteket. Ha továbbra is leterhelt, ezután a legtágabb régiót dobja
el, egyszerre egy szintet. A saját régiója mindig átmegy. Csak akkor működik,
ha az átjátszódon be vannak állítva régiók. Kapcsold be és ellenőrizd:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Amit ez eldob, az nem jelenik meg a `filter stats` kimenetében. Ha az
átjátszó újra csendes, a régiók visszatérnek, a legbelsővel kezdve.

## A flood megtekintése {#see}

Az appod csak azt mutatja, ami eljut hozzád. Nem létező csomópontoknak
küldött közvetlen üzenetek floodját csak egy observer hallja. Minden
observer a [MeshCore Analyzer](https://meshcore-analyzer.eu/) oldalra jelent,
ahol bárki megnézheti. Az átjátszódat observerré teheted:
[MQTT az observereden](/guides/mqtt/).

Az Analyzerben nézd meg egy csomag összes másolatát. Az útvonala általában
megmutatja, honnan jött. A flooder [kitalált azonosítókkal](#forged)
kezdheti az útvonalat, így az első azonosítók semmit sem árulnak el. Viszont
minden másolat ugyanazzal a kitalált kezdettel érkezik. A legrövidebb
útvonalú másolat a legkevesebb valódi átjátszón ment át, így azt hallották
a küldőhöz legközelebb.

{{< copies >}}

A saját átjátszódon a `filter stats` mutatja, mit dobott el a csomagszűrő.
A `filter stats top` a legtöbb eldobás mögötti csomópont-azonosítók első
bájtját mutatja. Ezen a bájton sok csomópont osztozik, így szűkíti a
keresést, de nem nevezi meg a küldőt.

## A forrás megkeresése {#source}

Ha egy flood újra és újra visszatér:

1. **Kövesd az útvonalakat.** Az útvonalat a végéről olvasd: az utolsó
   azonosítók azok az átjátszók, amelyeken a flood átment. A legkorábbi
   valódi a forrás közelében van, az előtte lévők lehetnek
   [kitaláltak](#forged).
2. **Szűkítsd a területet.** Ha több observer hallja ugyanazt a csomagot,
   egy területre szűkítik a küldő helyét. A
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) kiszámolja ezt
   azokból az átjátszókból, amelyek hallották.
3. **Járd be gyalog az utolsó kilométert.** Az átjátszók csak a hatótávuk
   szélén hallják a forrást, ezért az utolsó szakaszt gyalog kell bejárni.
   A [Mesh-Hunter](https://mesh-hunter.eu/) párosítható a companionöddel,
   és minden hallott csomagot a GPS-pozícióddal együtt naplóz. Ha
   többen jártok egyszerre, hamarabb megtaláljátok.
4. **Szólj a [helyi csoportodnak](/community/).** Ők többet látnak a meshből,
   ők döntik el, mi legyen a következő lépés, és ők veszik fel a kapcsolatot
   azzal, aki szándékosan floodol.

## Írd meg, mit láttál {#add}

Olyan flood ért, amely nincs
benne ezekben a táblázatokban? Megállította valamelyik beállítás? Írd meg
nekünk a [Discordon](https://discord.meshcore-info.eu/): mit láttál, és mit
kapcsoltál be. Felvesszük az oldalra.
