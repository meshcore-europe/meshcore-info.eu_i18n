---
title: Padaryk tinklą atsparų
lead: Ar tinklas šalia tavęs lėtas arba pilnas šlamšto? Išsiaiškink priežastį, įjunk tai stabdantį retransliatoriaus nustatymą ir pranešk vietinei grupei.
description: 'Užtvindymai ir šlamštas MeshCore tinkle: kaip atpažinti kiekvieną rūšį, kuris retransliatoriaus nustatymas padeda, kaip pamatyti užtvindymą ir rasti jo šaltinį.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-11-02'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Žinutės ateina pavėluotai arba visai neateina? Public kanalas pilnas šlamšto? Tai
užtvindymas: srauto daugiau, nei tinklas pajėgia perduoti, o kažkas jį siunčia per klaidą arba
tyčia. Susirask tai, ką matai, lentelėse toliau. Kiekvienoje eilutėje
nurodytas nustatymas, kuris tai sustabdo. Įjunk jį savo retransliatoriuje, tai yra
mazge, kuris persiunčia žinutes. Tada pranešk savo [vietinei grupei](/community/),
kad tą patį padarytų ir aplinkiniai retransliatoriai. Kiekvienas retransliatorius, kuris
atmeta užtvindymą, palieka eterio laiko visiems kitiems.

## Užtvindymai per klaidą {#mistake}

Užtvindymą per klaidą sukelia mazgas, kurio savininkas apie tai nežino. Užtvindymas
baigiasi, kai savininkas tai sužino. Lentelėse toliau prisistatymas (advert) yra
pasisveikinimas, kurį mazgas siunčia, kad kiti galėtų jį rasti.

Lentelėse pateikti nustatymai paremti tuo, ką daro programinė įranga. Ne visi
jie jau yra sustabdę užtvindymą tikrame tinkle.

{{< callout type="warning" >}}
Kai kuriems šio puslapio nustatymams reikia DMC programinės įrangos. Standartinėje **MeshCore** 1.18.0
yra regionai, šuolių ribos `flood.max.*`, kilpų aptikimas ir darbo ciklas. Paketų
filtrą, tai yra taisykles, pagal kurias tavo retransliatorius atmeta šlamštą, turi
**DMC programinė įranga** iš
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Ji turi ir darbo
ciklo ribojimą bei companion filtrą. Šis puslapis remiasi DMC
1.18.0 kūrimo versija `ecfb2d4` (2026 m. spalio 19 d.). Kur ją gauti, rasi
puslapyje [paketų filtras](/guides/filter/#firmware).
{{< /callout >}}

| Ką matai | Kas tai yra | Kas padeda |
| --- | --- | --- |
| Vieno mazgo užklausos retransliatoriams dieną naktį ir tinklas, kuris ištisas dienas lieka lėtas | Namų automatikos sistema arba botas, kuris per dažnai klausia retransliatorių jų būsenos | `filter on`. Tada paketų filtras praleidžia 5 užklausas per minutę. Pranešk savininkui. |
| Kas minutę kanale tokio paties pobūdžio žinutė | Botas, kuris rašo per dažnai | [Užblokuok kanalą](/guides/filter/#channel) arba [sulėtink siuntėją](/guides/filter/#sender). Pranešk savininkui. |
| Neįskaitomos žinutės Public ir kituose kanaluose | Mazgas su sugadinta programine įranga arba neteisingais radijo nustatymais | `filter malformed on` atmeta jas Public kanale. Pranešk savininkui. |
| Vieno mazgo prisistatymas kas kelias minutes | Mazgas, nustatytas prisistatyti per dažnai | `filter advert 24` praleidžia kiekvieno mazgo prisistatymą kartą per dieną. `set flood.max.advert 3` išlaiko prisistatymus 3 šuolių ribose. |
| Žinutės iš toli su regionais, kurie čia nepriklauso | Tiltas, kuris jungia tinklus per internetą | `set flood.max.unscoped 1`, o retransliatorių priskirk tik [regionams, kuriuos jis aptarnauja](/guides/settings/#traffic). |
| Ta pati žinutė praeina vėl ir vėl, o jos kelyje tavo retransliatoriaus ID yra daugiau nei kartą | Retransliatorius, kuris keičia paketus ir persiunčia juos toliau, todėl jie sukasi kilpoje | Pagal numatytuosius nustatymus kilpų aptikimas veikia `minimal` lygiu. `set loop.detect moderate` kilpą atmeta greičiau. |

## Tyčiniai užtvindymai {#purpose}

Kai kurie užtvindymai yra šlamštas: šiukšlės, kurias kažkas siunčia tyčia, kad
užkimštų tinklą. Siuntėjas keičia vardus, raktus ir kelius, todėl nė viena taisyklė
viena pati užtvindymo nesustabdo.

| Ką matai | Kas tai yra | Kas padeda |
| --- | --- | --- |
| Daug naujų mazgų atsitiktiniais vardais, kiekvienas su nauju raktu | Netikri prisistatymai | `filter rate 04 5 60` praleidžia 5 prisistatymus per minutę. `filter advert` nepadeda: kiekvienas prisistatymas ateina su [nauju raktu](#forged). |
| Žinutės su neįskaitomu tekstu nuo išgalvotų siuntėjų, dažnai su daugiau nei metų senumo data | Kanalų šlamštas | `filter malformed on` atmeta jas Public kanale. `filter age 60` atmeta žinutes su sena data Public kanale ir [stebimuose kanaluose](/guides/filter/#settings). |
| Iki 200 tiesioginių žinučių per minutę neegzistuojantiems mazgams, o patvirtinimai negrįžta | Tiesioginių žinučių užtvindymas | `filter rate 02 5 60`. Tavo programėlė šių žinučių nerodo, jas rodo stebėtojas. |
| Vieno mazgo užklausų pliūpsniai dešimtims kitų mazgų | Užklausų šlamštas | Su `filter on` paketų filtras praleidžia 5 užklausas per minutę. |
| Žinutė grįžta po 10–20 minučių beveik tuo pačiu keliu | Pakartojimas: dar kartą išsiųsta kopija | Retransliatorius prisimena paskutinius 160 paketų, kuriuos matė, todėl užimtame tinkle vėlesnė kopija vėl praeina. `filter age` atmeta grupinę žinutę, kuri senesnė, nei leidi. |
| Public žinutės, dar kartą išsiųstos išgalvoto siuntėjo vardu, kartais su sena data | Aido šlamštas | `filter age 60`. `filter malformed on` taip pat atmeta žinutę, kurios data skiriasi daugiau nei savaite. |
| Žinutė kas kelias sekundes keliuose kanaluose, kaskart nauju vardu, su įprastais klausimais | Botų banga | `filter rate 05 10 60`, be to, [užblokuok kanalus](/guides/filter/#channel), kurių tavo vietovėje niekas nenaudoja. Kiekvienas vardas naujas, todėl [siuntėjų taisyklės](#forged) jos nesugauna. |

## Kas pasiteisino {#worked}

Vietinės grupės užtvindymus sustabdė šiais žingsniais:

1. **Pranešk savininkui.** Užtvindymas per klaidą baigiasi, kai jo savininkas tai
   sužino. Parašyk jam draugišką žinutę.
2. **Nereaguok tinkle.** Atsakymas parodo šlamšto siuntėjui, kad šlamštas veikia.
3. **Paprašyk stebėtojų.** Stebėtojas yra mazgas, kuris per MQTT praneša apie
   kiekvieną girdimą paketą. Kuo daugiau stebėtojų aplink tave, tuo greičiau pamatysi,
   kur užtvindymas patenka į tinklą. Savo retransliatorių gali paversti stebėtoju
   pagal gidą [MQTT tavo stebėtojui](/guides/mqtt/).
4. **Rask šaltinį.** Stebėtojai nustato siuntėjo vietovę. Paskutiniam kilometrui reikia
   žmonių, kurie eina pėsčiomis su radiju. Skaityk skyrių
   [Rask šaltinį](#source).
5. **Įtrauk vietinę grupę.** Vienas retransliatorius su tinkamais nustatymais padeda.
   Visi vietovės retransliatoriai kartu užtvindymą sustabdo. Tavo
   [vietinė grupė](/community/) pasirūpina, kad nustatymą įjungtų kiekvienas savininkas.

## Išgalvoti siuntėjai ir keliai {#forged}

Šias paketo dalis rašo siuntėjas, ir niekas jų netikrina:

- **Siuntėjo vardas.** Kanalo žinutėje vardas yra teksto dalis. Kas turi kanalo
  raktą, gali parašyti bet kokį vardą.
- **Kelio pradžia.** Kiekvienas retransliatorius prideda savo ID kelio gale. Niekas
  netikrina anksčiau ten buvusių ID, todėl siuntėjas gali pradėti kelią išgalvotais
  ID. Kelio galas yra tikras.

{{< forged-path >}}

Todėl `filter sender` ir `filter path` sustabdo siuntėją tik tol, kol jis nepakeičia
vardo arba kelio. [Kelio blokavimas](/guides/filter/#path) atmeta ir tikrą to
retransliatoriaus srautą, kurio ID jame yra. Greičio ribos, šuolių ribos, amžiaus ir
sugadintų žinučių patikros, kanalų blokavimas, regionai ir darbo ciklas toliau veikia.

## Nustatymai bet kokiam užtvindymui {#always}

Šie nustatymai galioja, kad ir kas užtvindytų tinklą:

- **Darbo ciklas 10%.** Tada tavo retransliatorius niekada nesiunčia daugiau, nei
  leidžia įstatymas, kad ir kas ateitų. Apie tai rašoma
  [retransliatoriaus gide](/repeater-guide/#duty-cycle).
- **Regionai ir šuolių ribos.** Regionas yra sritis, kurioje žinutė lieka.
  Retransliatorius persiunčia tik jam priskirtų regionų žinutes, o
  `flood.max.*` neleidžia srautui nutolti. Abu dalykai aprašyti skyriuje
  [Sumažink srautą](/guides/settings/#traffic).
- **Paketų filtras užimtam retransliatoriui.** [Paruošti nustatymai](/guides/filter/#busy)
  perpus sumažina grupines žinutes ir prisistatymus. Pirmiausia išbandyk juos
  [dry-run](/guides/filter/#dryrun) režimu: jis tik skaičiuoja, ką atmestų.
- **Companion filtras DMC programinėje įrangoje.** Tavo companion, tai yra mazgas, iš
  kurio rašai žinutes, neįleidžia šlamšto į programėlę. Jis slepia sugadintas ir senas
  žinutes, taip pat žinutes iš užblokuoto retransliatoriaus ar siuntėjo ir žinutes su
  užblokuotu žodžiu. Siuntėjo ar žodžio taisyklė
  žinutę paslepia tik nuo tavęs, o kiti ją vis tiek gauna.

### Darbo ciklo ribojimas {#gate}

DMC programinėje įrangoje tavo retransliatorius gali teikti pirmenybę savo regionui,
kai tampa užimtas. Kai paskutinę minutę jis siuntė ilgiau nei 35% laiko, nustoja
persiųsti žinutes be regiono. Jei lieka užimtas, jis toliau atmeta plačiausią regioną,
po vieną lygį. Jo paties regionas visada praeina. Ribojimas veikia tik
tada, kai retransliatoriuje nustatyti regionai. Įjunk jį ir patikrink:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Tai, ką šis ribojimas atmeta, `filter stats` nerodo. Kai retransliatorius vėl aprimsta,
regionai grįžta, pradedant pačiu vidiniu.

## Pamatyk užtvindymą {#see}

Tavo programėlė rodo tik tai, kas pasiekia tave. Tiesioginių žinučių užtvindymą
neegzistuojantiems mazgams girdi tik stebėtojas. Kiekvienas stebėtojas siunčia pranešimus
į [MeshCore Analyzer](https://meshcore-analyzer.eu/), kur juos gali matyti visi. Savo
retransliatorių gali paversti stebėtoju pagal gidą
[MQTT tavo stebėtojui](/guides/mqtt/).

Analyzer svetainėje peržiūrėk visas vieno paketo kopijas. Jo kelias dažniausiai parodo,
iš kur jis atėjo. Užtvindytojas gali pradėti kelią
[išgalvotais ID](#forged), todėl pirmieji ID nieko nepasako. Tačiau kiekviena kopija
turi tą pačią išgalvotą pradžią. Kopija su trumpiausiu keliu praėjo pro mažiausiai tikrų
retransliatorių, todėl ji išgirsta arčiausiai siuntėjo.

{{< copies >}}

Savo retransliatoriuje komanda `filter stats` parodo, ką atmetė paketų filtras.
`filter stats top` parodo pirmąjį baitą tų mazgų ID, dėl kurių atmesta daugiausia paketų.
Tą patį baitą turi daug mazgų, todėl jis susiaurina paiešką, bet siuntėjo neįvardija.

## Rask šaltinį {#source}

Kai užtvindymas vis grįžta:

1. **Sek kelius.** Kelią skaityk nuo galo: paskutiniai ID yra retransliatoriai, pro
   kuriuos užtvindymas praėjo. Ankstyviausias tikras ID yra netoli šaltinio, o prieš jį
   esantys ID gali būti [išgalvoti](#forged).
2. **Susiaurink vietovę.** Keli stebėtojai, kurie girdi tą patį paketą, nustato siuntėjo
   vietovę.
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) ją apskaičiuoja pagal
   retransliatorius, kurie paketą girdėjo.
3. **Paskutinį kilometrą eik pėsčiomis.** Retransliatoriai šaltinį girdi tik savo
   veikimo zonos pakraštyje, todėl paskutinę dalį žmonės eina pėsčiomis.
   [Mesh-Hunter](https://mesh-hunter.eu/) jungiasi prie tavo companion ir kiekvieną
   girdimą paketą įrašo su tavo GPS padėtimi. Kai vienu metu eina keli žmonės, šaltinį
   jie randa greičiau.
4. **Pranešk savo [vietinei grupei](/community/).** Ji mato didesnę tinklo dalį,
   sprendžia, kas bus toliau, ir susisiekia su tais, kurie užtvindo tyčia.

## Pridėk tai, ką matei {#add}

Patyrei užtvindymą, kurio nėra
šiose lentelėse? Kuris nors nustatymas jį sustabdė? Parašyk mums
[Discord](https://discord.meshcore-info.eu/): ką matei ir ką įjungei. Mes tai
įtrauksime į puslapį.
