---
title: Tee võrk vastupidavaks
lead: Kas võrk sinu lähedal on aeglane või täis rämpsu? Uuri välja põhjus, lülita sisse kordaja seade, mis selle peatab, ja anna oma kohalikule grupile teada.
description: 'Üleujutused ja spämm MeshCore võrgus: kuidas iga liiki ära tunda, milline kordaja seade aitab, kuidas üleujutust näha ja selle allikat leida.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-11-02'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Kas sõnumid jõuavad kohale hilja või ei jõua üldse? Kas Public täitub
rämpsuga? See on üleujutus: liiklust on rohkem, kui võrk kanda jõuab, ja see
on saadetud kogemata või meelega. Otsi allolevatest tabelitest üles see, mida
näed. Igas reas on seade, mis selle peatab. Lülita see sisse oma kordajal, see
tähendab sõlmel, mis sõnumeid edasi saadab. Seejärel anna teada oma
[kohalikule grupile](/community/), et ümberkaudsed kordajad teeksid sama.
Iga kordaja, mis üleujutuse ära viskab, jätab teistele eetriaega.

## Kogemata tekkinud üleujutused {#mistake}

Kogemata tekkinud üleujutuse põhjustab sõlm, mille omanik sellest ei tea.
See lõpeb, kui omanik teada saab. Kuulutus on allolevates tabelites
tervitus, mille sõlm saadab, et teised selle üles leiaksid.

Tabelite seaded põhinevad sellel, mida püsivara teeb. Kõik neist pole veel
päris võrgus üleujutust peatanud.

{{< callout type="warning" >}}
Mõne selle lehe seade jaoks on vaja DMC püsivara. Tavalises **MeshCore** 1.18.0
versioonis on piirkonnad, hüpete piirangud `flood.max.*`, silmuste tuvastamine
ja töötsükkel. Pakettfilter (reeglid, millega su kordaja rämpsu ära viskab)
tuleb **DMC püsivaraga**, mille leiad
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) lehelt. Sama
kehtib töötsüklipõhise piiramise ja kaasseadme filtri kohta. See leht järgib
DMC 1.18.0 arendusjärku `ecfb2d4`, mis on 19. oktoobrist 2026. Lehel
[pakettfilter](/guides/filter/#firmware) on kirjas, kust selle saad.
{{< /callout >}}

| Mida näed | Mis see on | Mis aitab |
| --- | --- | --- |
| Ühelt sõlmelt tuleb kordajatele päringuid päeval ja öösel ning võrk püsib päevi aeglane | Koduautomaatika või bott küsib kordajatelt olekut liiga tihti | `filter on`. Seejärel laseb pakettfilter läbi 5 päringut minutis. Anna omanikule teada. |
| Kanalil ilmub iga minut sama tüüpi sõnum | Bott postitab liiga tihti | [Blokeeri kanal](/guides/filter/#channel) või [aeglusta saatjat](/guides/filter/#sender). Anna omanikule teada. |
| Publicus ja teistes kanalites on loetamatud sõnumid | Sõlmel on katkine püsivara või valed raadioseaded | `filter malformed on` viskab need Publicus ära. Anna omanikule teada. |
| Ühe sõlme kuulutus tuleb iga paari minuti järel | Sõlm on seatud liiga tihti kuulutama | `filter advert 24` laseb iga sõlme kuulutuse läbi kord päevas. `set flood.max.advert 3` hoiab kuulutused 3 hüppe piires. |
| Kaugelt tulevad sõnumid piirkondadega, mis siia ei kuulu | Sild ühendab võrke interneti kaudu | `set flood.max.unscoped 1` ja pane oma kordaja ainult nendesse [piirkondadesse, mida see teenindab](/guides/settings/#traffic). |
| Sama sõnum läheb ikka ja jälle läbi ning su kordaja ID on selle teekonnas mitu korda | Kordaja muudab pakette ja saadab need edasi, nii et need liiguvad silmuses | Silmuste tuvastamine töötab vaikimisi tasemel `minimal`. `set loop.detect moderate` viskab silmuse varem ära. |

## Meelega tekitatud üleujutused {#purpose}

Mõni üleujutus on spämm: rämps, mille keegi saadab meelega võrgu
ummistamiseks. Saatja vahetab nimesid, võtmeid ja teekondi, nii et ükski
üksik reegel üleujutust ei peata.

| Mida näed | Mis see on | Mis aitab |
| --- | --- | --- |
| Palju uusi juhuslike nimedega sõlmi, igaühel uus võti | Võltskuulutused | `filter rate 04 5 60` laseb läbi 5 kuulutust minutis. `filter advert` ei aita: iga kuulutus tuleb [uuelt võtmelt](#forged). |
| Väljamõeldud saatjatelt tulevad loetamatu tekstiga sõnumid, sageli üle aasta vana kuupäevaga | Kanalispämm | `filter malformed on` viskab need Publicus ära. `filter age 60` viskab vana kuupäevaga sõnumid ära Publicus ja [jälgitavatel kanalitel](/guides/filter/#settings). |
| Kuni 200 otsesõnumit minutis sõlmedele, mida pole olemas, ja kinnitusi tagasi ei tule | Otsesõnumite üleujutus | `filter rate 02 5 60`. Sinu rakendus neid sõnumeid ei näita, vaatleja näitab. |
| Ühelt sõlmelt lähevad päringupursked kümnetele teistele | Päringuspämm | Kui `filter on` on sees, laseb pakettfilter läbi 5 päringut minutis. |
| Sõnum tuleb 10 kuni 20 minutit hiljem tagasi peaaegu sama teekonnaga | Taasesitus: uuesti saadetud koopia | Kordaja mäletab viimast 160 paketti, mida ta nägi, nii et hõivatud võrgus läheb hilisem koopia uuesti läbi. `filter age` viskab ära grupisõnumi, mis on vanem, kui lubad. |
| Publicu sõnumid saadetakse uuesti väljamõeldud saatja nimel, mõnikord vana kuupäevaga | Kajaspämm | `filter age 60`. `filter malformed on` viskab ära ka sõnumi, mille kuupäev on üle nädala vale. |
| Mitmel kanalil tuleb iga paari sekundi järel sõnum, iga kord uue nimega, ja selles küsitakse tavalisi asju | Bottide laine | `filter rate 05 10 60` ja [blokeeri kanalid](/guides/filter/#channel), mida su piirkonnas ei kasutata. Iga nimi on uus, nii et [saatjareeglid](#forged) seda ei taba. |

## Mis on toiminud {#worked}

Kohalikud grupid peatasid üleujutusi nende sammudega:

1. **Anna omanikule teada.** Kogemata tekkinud üleujutus lõpeb, kui omanik
   sellest teada saab. Saada talle sõbralik sõnum.
2. **Ära reageeri võrgus.** Vastus näitab spämmijale, et spämm toimib.
3. **Palu lisada vaatlejaid.** Vaatleja on sõlm, mis annab MQTT kaudu teada igast
   kuuldud paketist. Mida rohkem on su ümber vaatlejaid, seda varem näed, kust
   üleujutus sisse tuleb. Tee oma kordajast vaatleja juhendiga
   [MQTT sinu vaatlejal](/guides/mqtt/).
4. **Leia allikas.** Vaatlejad paigutavad saatja mingisse piirkonda. Viimase
   kilomeetri läbivad inimesed jalgsi, raadio käes. Vaata jaotist
   [Leia allikas](#source).
5. **Pane oma kohalik grupp tegutsema.** Üks õigete seadetega kordaja aitab.
   Kõik piirkonna kordajad koos peatavad üleujutuse. Sinu
   [kohalik grupp](/community/) veenab iga omanikku seadet sisse lülitama.

## Väljamõeldud saatjad ja teekonnad {#forged}

Need paketi osad kirjutab saatja ja miski neid ei kontrolli:

- **Saatja nimi.** Kanalisõnumis on nimi osa tekstist. Igaüks, kellel on
  kanali võti, saab kirjutada mis tahes nime.
- **Teekonna algus.** Iga kordaja lisab oma ID teekonna lõppu. Miski ei
  kontrolli varem seal olnud ID-sid, nii et saatja võib alustada teekonda
  väljamõeldud ID-dega. Teekonna lõpp on ehtne.

{{< forged-path >}}

Seega peatavad `filter sender` ja `filter path` saatja ainult seni, kuni ta oma
nime või teekonda muudab. [Teekonna blokeering](/guides/filter/#path) viskab
ära ka selle kordaja ehtsa liikluse, mille ID selles on. Kiiruspiirangud,
hüpete piirangud, vanuse ja vigase vormingu kontrollid, kanalite blokeeringud,
piirkonnad ja töötsükkel töötavad edasi.

## Seaded iga üleujutuse jaoks {#always}

Need kehtivad, ükskõik mis võrku üle ujutab:

- **Töötsükkel 10%.** Nii ei saada su kordaja kunagi rohkem, kui seadus lubab,
  ükskõik mis sisse tuleb. Sellest räägib
  [kordaja juhend](/repeater-guide/#duty-cycle).
- **Piirkonnad ja hüpete piirangud.** Piirkond on ala, mille sisse sõnum jääb.
  Kordaja saadab edasi ainult nende piirkondade sõnumeid, mis tal on, ja
  `flood.max.*` hoiab liikluse lähedal. Mõlemad on kirjas jaotises
  [Hoia liiklus madalal](/guides/settings/#traffic).
- **Pakettfilter hõivatud kordajale.**
  [Valmisseaded](/guides/filter/#busy) vähendavad grupisõnumite ja kuulutuste
  hulka poole võrra. Proovi neid esmalt [dry-run-režiimis](/guides/filter/#dryrun):
  see ainult loendab, mida ta ära viskaks.
- **Kaasseadme filter DMC püsivaras.** Sinu kaasseade (sõlm, millelt sõnumeid
  saadad) hoiab rämpsu su rakendusest eemal. See peidab katkised ja
  vanad sõnumid ning sõnumid kordajalt, saatjalt või sõnaga, mille blokeerid.
  Saatja- või sõnareegel peidab sõnumi ainult sinu eest: teised saavad selle
  ikkagi kätte.

### Töötsüklipõhine piiramine {#gate}

DMC püsivaras saad lasta kordajal hõivatud ajal eelistada oma piirkonda. Kui
kordaja on viimasest minutist üle 35% saatnud, ei saada see enam piirkonnata
sõnumeid edasi. Kui hõivatus püsib, viskab kordaja järgmisena ära kõige laiema
piirkonna, üks tase korraga. Oma piirkonna sõnumid lähevad alati edasi. See
töötab ainult siis, kui oled kordajale piirkonnad määranud. Lülita see sisse ja
kontrolli:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Seda, mida see ära viskab, `filter stats` ei näita. Kui kordajal on jälle
vaikne, tulevad piirkonnad tagasi, alates kõige sisemisest.

## Kuidas üleujutust näha {#see}

Sinu rakendus näitab ainult seda, mis sinuni jõuab. Otsesõnumite üleujutust
sõlmedele, mida pole olemas, kuuleb ainult vaatleja. Iga vaatleja annab teada
[MeshCore Analyzerile](https://meshcore-analyzer.eu/), kus kõik seda näha
saavad. Tee oma kordajast vaatleja juhendiga
[MQTT sinu vaatlejal](/guides/mqtt/).

Vaata Analyzeris ühe paketi kõiki koopiaid. Tavaliselt näitab teekond, kust
pakett tuli. Üleujutaja võib alustada teekonda [väljamõeldud ID-dega](#forged),
nii et esimesed ID-d ei ütle sulle midagi. Kuid igal koopial on sama
väljamõeldud algus. Lühima teekonnaga koopia läbis kõige vähem ehtsaid
kordajaid, seega kuuldi seda saatjale kõige lähemal.

{{< copies >}}

Oma kordajal näed käsuga `filter stats`, mida pakettfilter ära viskas.
`filter stats top` näitab nende sõlme-ID-de esimest baiti, mille taga on enamik
ära visatud pakette. Sama bait on paljudel sõlmedel, nii et see
kitsendab otsingut, kuid ei nimeta saatjat.

## Leia allikas {#source}

Kui üleujutus aina tagasi tuleb:

1. **Järgi teekondi.** Loe teekonda lõpust: viimased ID-d on kordajad, mida
   üleujutus läbis. Kõige varasem ehtne ID on allika lähedal. Sellele eelnevad
   ID-d võivad olla [väljamõeldud](#forged).
2. **Kitsenda piirkonda.** Kui mitu vaatlejat kuuleb sama paketti, paigutavad
   nad saatja mingisse piirkonda.
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) arvutab selle
   välja kordajate põhjal, mis paketti kuulsid.
3. **Käi viimane kilomeeter jalgsi.** Kordajad kuulevad allikat ainult oma ulatuse
   servas, nii et viimase osa läbivad inimesed jalgsi.
   [Mesh-Hunter](https://mesh-hunter.eu/) ühendub su kaasseadmega ja logib
   iga kuuldud paketi koos sinu GPS-asukohaga. Kui mitu inimest kõnnib
   korraga, leiavad nad allika kiiremini.
4. **Anna teada oma [kohalikule grupile](/community/).** Grupp näeb võrgust
   rohkem, otsustab, mis edasi saab, ja võtab ühendust sellega, kes meelega
   võrku üle ujutab.

## Lisa, mida nägid {#add}

Kas sind tabas üleujutus, mida nendes tabelites pole? Kas mõni seade peatas
üleujutuse? Kirjuta meile [Discordis](https://discord.meshcore-info.eu/): mida
nägid ja mida sisse lülitasid. Lisame selle lehele.
