---
title: Antennijuhend
lead: Õige ja hästi paigaldatud antenniga jõuad kaugemale kui suurema võimsusega. Kontrolli oma companion-seadme antenni, seejärel vali repiiterile antenn, ühenda see ja paigalda.
description: 'Vali ja paigalda MeshCore''i antenn 868 MHz jaoks: companion-seadme piitsantenni kontroll, antennitüübid ja võimendus, liitmikud, kaabli kadu meetri kohta, filtrid, paigaldus ja võimenduse arvestamine seadusliku piiri juures.'
eyebrow: Companion-seade ja repiiter · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-11-02'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Kõrgus, häälestatud antenn ja lühike kaabel annavad rohkem levi kui ükski lisamillivatt. See juhend algab companion-seadmest, raadiost, millega sõnumeid saadad. Seejärel tuleb juttu repiiteri antennist. Repiiter on katusel või mastis asuv sõlm, mis annab sõnumeid edasi.

## Sinu companion-seade {#companion}

{{< callout type="warning" >}}
Ühenda antenn enne raadio sisselülitamist. Kui LoRa-raadio saadab ilma antennita, võib see oma kiibi ära rikkuda.
{{< /callout >}}

Plaadiga kaasas olnud antennist piisab. Ühenda see, hoia sõlme püsti ja hakka sõnumeid saatma. Parem antenn annab companion-seadmele vähe juurde, levialas olev repiiter aga palju.

Osta eraldi piitsantenn ainult siis, kui kaasasolev on katki või puudub. Kõik 868 MHz jaoks müüdavad piitsantennid ei ole sellele sagedusele häälestatud. [Kontrolli seda NanoVNA-ga](#nanovna), taskusuuruse antennianalüsaatoriga, enne kui seda usaldad, või laena antenn töötavalt plaadilt.

Tugeva saatja kõrval kuuleb sõlm halvemini, kui peaks. Väike [SAW-filter (pinnaakustilise laine filter)](#filters) raadio ja antenni vahel hoiab selle saatja signaali vastuvõtjast eemal. Kontrolli esmalt filtri andmelehte:

- **Suurim sisendvõimsus.** Filter on ka sinu enda saadetava signaali teel. Kui plaat saadab 22 dBm (160 mW) 15 dBm jaoks ette nähtud filtrisse, läheb filter katki.
- **Pääsuriba.** See peab hõlmama sinu eelseadistuse sagedust. Vahemiku 868.65 kuni 869.25 MHz filter ei lase läbi EU/UK (Narrow) kanalit sagedusel 869.618 MHz.

## Repiiteri antennitüübid {#types}

Kõik võrgu antennid seisavad püsti. Vali tüüp selle järgi, kus asuvad sõlmed, milleni tahad jõuda:

- **Klaaskiust kollineaarantenn.** Valge toru mastis, mille võimendus katab kogu horisondi. Tavaline valik linna teenindavale repiiterile.
- **Dipool.** Lühem, väiksema võimenduse ja kõrge kiirega. Allpool ja ülalpool asuvate sõlmedeni jõuab see paremini kui kollineaarantenn, näiteks oru kohal olevalt mäelt.
- **Yagi.** Ristelementidega poom, mille suunad ühte kohta. Sellega jõuad üksiku kauge repiiterini ja vähe millegi muuni. Paigalda see elemendid püsti, sest selle polarisatsioon järgib elementide suunda.

## Võimendus ja kiir {#gain}

Võimendus ei lisa võimsust. See võtab signaali, mis läheks üles ja alla, ning saadab selle piki horisonti. See on nagu taskulamp, mille valgust koondad: patarei on sama, kiir pikem ja kitsam. Seda näitavad sama tootja dipool ja kollineaarantenn:

| Antenn | Võimendus | Kiire vertikaalne laius |
|---|---|---|
| Dipool (Sirio SO 868-915-2) | 2.2 dBi | 88 kraadi |
| Klaaskiust kollineaarantenn (Sirio SPO 868-915-6) | 5.8 dBi | 23 kraadi |

{{< gain >}}

Joonisel on lõige läbi masti, küljelt vaadatuna. Pööra seda ümber masti ja saad kogu kiire: dipoolil on see sõõriku, kollineaarantennil lameda ketta kujuline. Püstine antenn saadab signaali igas suunas enda ümber ühtemoodi. Väljaspool joonistatud kiirt signaal ei kao. See on nõrgem, kuid lähedal asuva sõlme jaoks ikka piisav.

Katusel vajad just lamedat kiirt. Sõlmedest kõrgel oleval mäel läheb 23-kraadine kiir neil üle pea, dipool aga katab need. Yagi läheb veel kaugemale: 16.6 dBi kiires, mis on 23 kraadi kõrge ja 25 kraadi lai (Amphenol Procom 7176870), ning külgedele ei lähe midagi.

Võimendust mõõdetakse võrdlusantenni suhtes. dBi võrdleb ideaalse antenniga, mis saadab signaali igas suunas võrdselt. dBd võrdleb poollainedipooliga, millel endal on 2.15 dBi: isegi kõige lihtsam antenn ei saada midagi otse üles ega alla. Pikem dipool, 1.25 lainepikkust, jõuab 5.2 dBi-ni. Kollineaarantenn laob selle asemel poollaine-elemendid üksteise kohale: mida rohkem elemente, seda suurem võimendus. Kui surud sama signaali poole väiksemasse ruumi, on see seal kaks korda tugevam: 3 dB. Kui veerandisse, siis 4 korda tugevam: 6 dB. Tootjad annavad võimenduse dBi-des, seaduslik piir on arvestatud dBd-des, vaata jaotist [Seadusliku piiri sees](#legal).

### Milline võimendus sobib sinu asukohale {#choose-gain}

- **Mäed, orud või tihe linn: umbes 3 dBi.** Kõrge kiir jõuab sinust ülal ja all asuvate sõlmedeni ning ümber ette jäävate nõlvade ja hoonete. See toimib ka vastupidi: orust läheb lame kiir kohal oleval mäel asuvast repiiterist alt läbi. Üks selline antenn on RAKwireless RAKARG12, 36 cm pikkune klaaskiudtoru.
- **Eeslinn või madalate katustega linn: 5 kuni 6 dBi.** Tavaline klaaskiust kollineaarantenn.
- **Tasane ja lage maa: 8 kuni 10 dBi.** Kõige lamedam kiir jõuab piki horisonti kõige kaugemale. Kõrgele paigaldatuna läheb see lähedal asuvatest sõlmedest üle.

Nimes toodud võimendus on parim näit antenni kogu sagedusalas. RAKARG12-l, mida müüakse 3 dBi antennina, on sagedustel 865 kuni 870 MHz võimendus 2.8 dBi. Vaata andmelehe võimendustabelist väärtust oma eelseadistuse sagedusel.

Üle 7 dBi antenniga ületab 22 dBm plaat seadusliku piiri, kui kaabli ja filtri kadu vahet ei korva. Vähenda saatevõimsust vastavalt.

Suur võimendus aitab ainult siis, kui tead, kus sõlmed asuvad: repiiteri ümber piki horisonti või Yagi puhul ühe kauge repiiteri juures. Käes hoitav companion-seade on suunatud igale poole, seega sobib sellele kõige paremini kaasas olnud väikese võimendusega antenn.

## Miks vertikaalselt {#vertical}

Antennid kuulevad üksteist kõige paremini, kui need on samas suunas. Kadu kasvab koos nendevahelise nurgaga: 45 kraadi juures kaotad 3 dB, poole oma signaalist. 90 kraadi juures, kui lamav antenn on püstise vastas, ei jõua teoreetiliselt kohale midagi. Võrgu antennid seisavad püsti, seega peab ka sinu antenn püsti seisma. See kehtib ka laual oleva companion-seadme kohta: kui paned selle pikali, kuulevad kõik sõlmed sinu ümber sind halvemini.

## Liitmikud {#connectors}

Telli antenn sama liitmikuga, mis on sinu plaadil. Iga adapter on üks ühenduskoht rohkem, mida tihendada, ja lisab signaalikadu.

- **SMA.** Keermega liitmik, umbes 6 mm lai. Enamikul plaatidel on pesa keskel auk ja antennil tihvt. Seda tüüpi liitmikus kaob sagedusel 868 MHz umbes 0.03 dB.
- **RP-SMA.** Korpus ja keere on samad mis SMA-l, kuid tihvt ja auk on vahetatud. See näeb välja nagu SMA, kuid sellega kokku ei sobi. Enne tellimist kontrolli, kumb sinu plaadil on.
- **U.FL (IPEX).** Pisike pealesurutav pesa otse plaadil. Sellest viib lühike pigtail-kaabel korpuses asuva SMA-pesani. See on ette nähtud 30 ühenduskorra jaoks, seega ühenda see üks kord ja jäta paika.
- **N.** Suur keermega liitmik klaaskiust antennidel ja jämedal kaablil. Selles kaob kõige rohkem 0.05 dB. Repiiter vajab üht adapterit või pigtail-kaablit N-liitmikult plaadi SMA-le.

## Kaabli kadu {#cable}

Kaabel võtab signaali enne, kui see antennist välja jõuab, ja seda mõlemas suunas. 3 dB on pool sinu võimsusest. Tootjate andmed meetri kohta sagedustel 868 kuni 900 MHz:

| Kaabel | Kadu meetri kohta | Kadu 5 m kohta |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 meetrit RG174-kaablit, õhukest pigtail-kaablit, mis on paljude plaatidega kaasas, võtab poole sinu võimsusest. Paigalda plaat lühikese pigtail-kaabliga antenni juurde või vea antennini jäme kaabel. Liida kogukaole iga adapter ja filter signaali teel.

## Filtrid {#filters}

Filter asub raadio ja antenni vahel. See laseb läbi sinu sagedusala ja blokeerib ülejäänu, nii et tugev lähedal asuv saatja ei ummista vastuvõtjat. Filtrit vajad siis, kui sõlm kuuleb teiste saatjate lähedal halvemini, kui peaks. Selline sõlm on repiiter mastis, kus on ka mobiilside tugijaamad. Filter võtab signaali mõlemas suunas: arvesta selle kadu samamoodi nagu kaabli oma.

| | SAW-filter | Õõnsusfilter |
|---|---|---|
| Suurus | Mõni millimeeter, väikesel plaadil | Metallplokk või -toru |
| Hea filtri kadu | alla 2 dB | alla 1 dB |
| Hea filtri suurim sisendvõimsus | 500 mW | mitu vatti |

Näiteks sysmocom cf866.5-kt30 on õõnsusfilter vahemikule 863 kuni 870 MHz, mille kadu on kõige rohkem 1.0 dB ja mis talub 30 W. See on mõeldud siseruumidesse, seega pane see mastis tihendatud karpi.

Filtrid on väga erinevad, seega kontrolli enne ostmist andmelehte. Filtri nimisisendvõimsus peab ületama sinu saatevõimsust ja pääsuriba peab hõlmama sinu eelseadistuse sagedust.

## Paigaldus {#mounting}

- **Katuseservast kõrgemale.** Antenn vajab vaba vaatevälja igas suunas, mida see teenindab. Isegi mõni meeter ümbritsevatest katustest kõrgemal aitab. Repiiteri juhendi jaotis [Vali asukoht](/repeater-guide/#site) näitab, kuidas vaatevälja kontrollida.
- **Metallist eemale.** Antenni kõrval olevad vihmaveerennid, mastid, teised antennid ja metallkatused muudavad selle kiirgusmustrit ja häälestust. Paigalda see masti tippu, mitte selle kõrvale.
- **Püsti.** Kasuta vesiloodi, vaata jaotist [Miks vertikaalselt](#vertical).
- **Tilgasilmus.** Lase kaablil enne üles või sisse suundumist liitmikust allapoole rippuda. Nii tilgub vesi maha ega valgu ühenduskohta.
- **Tihenda iga välisliitmik.** Vesi liitmikus suurendab kadu ja söövitab tihvti. Tihenda liitmik vihma vastu ja kontrolli tihendust igal aastal.
- **Välk.** Katusel olev antenn on märklaud. Kaablisse paigaldatud gaaslahenduspiirik rakendub liigpinge korral ja juhib selle maasse. Maanduse puhul järgi repiiteri juhendi jaotist [Riistvara](/repeater-guide/#hardware) ja kohalikke nõudeid.

## Seadusliku piiri sees {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
Euroopas kasutab MeshCore alamriba 869.40-869.65 MHz, kus efektiivne kiirgusvõimsus (e.r.p.) on kõige rohkem **500 mW**. Piir arvestab seda, mis antennist välja läheb: antenni võimendus lisandub, kaabli ja filtri kadu lahutatakse. dBi-des antud võimendus läheb arvesse 2.15 dB võrra väiksemana, sest piiri mõõdetakse dipooli suhtes.
{{< /callout >}}

5.8 dBi kollineaarantenn jääb 22 dBm plaadil piiri sisse. Sama antenn võimendiga plaadil ei jää, kuni sa saatevõimsust ei vähenda. Repiiteri juhendi jaotises [Võimsus: e.r.p. ja sinu antenn](/repeater-guide/#erp) on arvutus ja 2 läbi arvutatud näidet.

## Kontrolli antenni NanoVNA-ga {#nanovna}

NanoVNA on taskusuurune vektorvõrguanalüsaator. See näitab, millisele sagedusele antenn on häälestatud, nii et tead seda juba enne paigaldamist. NanoVNA-H mõõdab kuni 1.5 GHz, mis hõlmab ka 868 MHz.

1. Kalibreeri see vahemikule 800 kuni 950 MHz komplekti kuuluvate open-, short- ja load-otsikutega.
2. Ühenda antenn sama adapteriga, mida see sõlmel kasutama hakkab. Hoia antenni püsti ning oma kehast ja lauast eemal.
3. Vaata SWR-kõverat (seisulainesuhe): see näitab, kui palju signaali antenn tagasi saadab. Kõvera madalaim koht peab olema sinu eelseadistuse sagedusel, EU/UK (Narrow) puhul 869.618 MHz. Kui madalaim koht on sadade MHz kaugusel, on antenn tehtud teise sagedusala jaoks.

Veerandlaine sagedusel 868 MHz on 86 mm (lainepikkus on 345 mm). Ainult pikkuse järgi sagedusala ei tuvasta, sest tootjad voldivad ja koormavad piitsantenne. NanoVNA näitab selle ära.

## Allikad {#sources}

- Kaabli kadu: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  Huber+Suhner RG316 andmeleht,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  Times Microwave LMR-240 ja LMR-400 andmelehed,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antennid: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  Sirio SO 868-915-2 andmeleht,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Võimendus kui väiksemasse ruumi surutud signaal: [RF Cafe, sissejuhatus antennidesse](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Liitmikud: Rosenberger 32S102 (SMA) ja 53S101 (N) andmelehed, Hirose U.FL kataloog.
- Filtrid: sysmocom cf866.5-kt30 tootelehekülg,
  [Citeli gaaslahenduspiirikud](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarisatsioonikadu: [Toronto Ülikool, Friisi efektid](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipooli võimendus pikkuse järgi: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Lainepikkus: valguse kiirus [NIST-ist](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Seaduslik piir: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  lisa 1, riba h1.7; ülejäänud allikad on loetletud [repiiteri juhendis](/repeater-guide/#legal).
