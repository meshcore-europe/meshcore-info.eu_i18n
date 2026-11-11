---
title: Mis on MeshCore?
lead: MeshCore saadab tekstisõnumeid raadio teel, sõlmest sõlme. Selleks ei ole vaja internetti ega lepingut.
description: 'Mis MeshCore on ja mis see ei ole: sõlmede liigid, marsruutimine, krüpteerimine ja 868 MHz sagedusala.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '70b86ac3'
  seeded: '2026-11-11'
  fields: {title: '06eda66b', lead: 'c0174569', description: 'c2255f49', eyebrow: '8610c822'}
  sections: ['aa768ac3', '9e1e2d85', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', 'd516c212', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b7b981e6', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '5d796ffb', '1a490368', 'f0dd237f', '053d85bc', '02f1fe2f', 'e6b5b258']
---

MeshCore on tasuta tarkvara väikestele LoRa-raadiotele. LoRa on raadiotehnika, mis saadab vähe andmeid kaugele ja kulutab väga vähe energiat. MeshCore'iga raadiot nimetatakse *sõlmeks*. Kui seod sõlme telefoni või sülearvuti rakendusega või kasutad selle enda ekraani ja klaviatuuri, saad saata teksti inimestele kilomeetrite kaugusele. Vahele ei jää ühtegi masti, ruuterit ega teenusepakkujat.

Tarkvara on avatud lähtekoodiga. Seda arendatakse hoidlas [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) MIT-litsentsi all.

## Mis MeshCore ei ole {#not}

Kas raadio on sulle uus? Siin on asjad, mida inimesed MeshCore'ilt kõige sagedamini ootavad, kuid mida see ei tee.

- **See ei ole internet ega telefon.** MeshCore saadab lühikesi tekstisõnumeid,
  umbes sama pikki kui SMS sinu telefonis. Häält, fotosid, videot
  ega veebilehti pole ning tavalist telefoninumbrit sa sellega kätte ei saa.
- **See ei ole hädaabiteenus.** Ükski hädaabiteenus ei luba võrku
  jälgida. Me teame, et võrk suudab toimida. Kas see toimib ka hädaolukorras,
  ei tea keegi.
- **See ei toimi koheselt ega kõikjal.** Sõnum liigub hüpetena raadiolt
  raadiole ja võib kohale jõuda mõne sekundiga või üldse mitte. Kas see
  läbi jõuab, sõltub ümbruskonna repiiteritest, kõrgusest, hoonetest ja sinu
  antennist. Toas olev väike raadio ei jõua sageli kellenigi. Katusel olev repiiter
  ulatub kilomeetrite kaugusele.
- **See ei ole teenus, mida keegi sinu eest haldab.** Teenusepakkujat,
  kasutajatuge ega levigarantiid pole. Võrk on olemas seal, kus kogukonna
  inimesed on repiitereid püsti pannud.
- **Kõik võrgus ei ole privaatne.** Otsesõnumid on krüpteeritud, kuid
  Public ja räsimärgiga kanaleid saab lugeda igaüks ning sinu sõlme
  nime ja jagatud asukohta näevad kõik, kes on levialas.
  [Vaatlejad](/network/) saadavad kuuldu avalikele kaartidele.
  [Krüpteerimise jaotis](#encryption) selgitab, mis jääb privaatseks.
- **See ei ole piiramatu.** Kõik piirkonna kasutajad jagavad ühte raadiokanalit ja
  [868 MHz sagedusala](#band) reeglid piiravad, kui kaua iga raadio tohib saata.
  Iga sõnum võtab eetriaega kõigilt teistelt, nii et botid, sagedased kuulutused
  ja testsõnumid aeglustavad võrku kõigi jaoks.
- **See ei ole Meshtastic.** Meshtastic on teine süsteem, mis töötab
  suuresti samadel plaatidel. Need kaks ei saa omavahel suhelda.

## Mesh-võrk ühe minutiga {#mesh}

Üks LoRa-raadio ulatub linnas mõne kilomeetri kaugusele, künkalt või katuselt palju kaugemale. Et jõuda kaugemale, edastavad raadiod üksteise sõnumeid: see ongi *mesh-võrk*. MeshCore'is edastavad sõnumeid raadiod, mida nimetatakse *repiiteriteks*. Repiiter saadab kuuldud sõnumi uuesti välja, nii et sõnum võib läbida terve piirkonna.

Mesh-võrk ei kuulu kellelegi. Iga sõlm ja iga repiiter kuulub kellelegi kogukonnast. Mesh-võrk ulatub nii kaugele kui nende repiiterid.

## Sõlmede 3 liiki {#roles}

Sõlme liigi valid püsivara paigaldamisel. Sinu esimene sõlm on kaasseade.

**Kaasseade.** Sinu oma raadio. See ühendub sinu telefoni või sülearvuti MeshCore'i rakendusega Bluetoothi või USB kaudu; mõnel on ka oma ekraan ja klaviatuur. Rakenduses loed ja kirjutad sõnumeid. Kaasseade hoiab alles sinu kontaktid ja kanalid ning sõnumid, mis saabusid ajal, kui rakendus polnud ühendatud. Kaasseade ei edasta teiste sõnumeid.

**Repiiter.** Kõrgele paigutatud raadio, mis edastab sõnumeid kõigi jaoks. Enamik töötab päikeseenergial. Oma repiiterit vajad ainult seal, kuhu mesh-võrk veel ei ulatu. Sellel ei ole oma rakendust. Seadistad selle USB kaudu või logid parooliga sisse ja haldad seda raadio kaudu. [Repiiteri juhend](/repeater-guide/) näitab, kuidas seda teha.

**Jututoaserver.** Väike teadetetahvel mesh-võrgus. Sisselogimisel saad postitused, mis jäid sul levist väljas olles nägemata, kuni viimased 32. Server hoiab neid ainult mälus, nii et taaskäivitus või voolukatkestus kustutab need. Kohalik rühm kasutab seda teadete jaoks.

## Kuidas sõnum tee leiab {#routing}

Igal sõlmel on salajane võti ja avalik võti. Avalik võti on sõlme identiteet. Sõlm annab endast märku *teadaandega*: see on allkirjastatud pakett sõlme nime ja soovi korral ka asukohaga. Inimene ilmub sinu kontaktidesse, kui mõni tema teadaanne on sinuni jõudnud või kui skannid tema QR-koodi. Rakenduses on nupp, millega saadad enda teadaande.

Sinu esimene sõnum kontaktile läheb teele *üleujutusena*. Iga repiiter, mis selle kuuleb, edastab sõnumi ühe korra ja lisab teel oma lühikese ID. Vastus toob selle ID-de loendi tagasi. Edaspidi liiguvad sinu sõnumid sellele kontaktile salvestatud marsruuti mööda ja saadavad ainult sellel marsruudil olevad repiiterid. Kui marsruut katkeb, kasutab rakendus uuesti üleujutust.

Kanalisõnumitel ei ole ühte kindlat aadressi, seega levivad need alati üleujutusena. Repiiterid mäletavad, mida nad hiljuti edastasid, ja viskavad ära koopiad, mis saabuvad uuesti mööda teist teed. Sõnum võib läbida kuni 64 repiiterit või 32, kui eelseadistus kasutab 2-baidiseid ID-sid.

## Krüpteerimine ja privaatsus {#encryption}

Sinu otsesõnumid on otspunktkrüpteeritud: peale sinu ja teise inimese ei saa neid lugeda keegi. Repiiter näeb paketi saajat ainult 1-baidise vihjena.

Kanalid on krüpteeritud jagatud võtmega, seega sõltub lugejate ring sellest, kellel see võti on:

- **Public** on seadistatud igas kaasseadmes. Selle võti on avaldatud, nii et lugeda saab igaüks.
- **Räsimärgiga kanalid**, näiteks `#utrecht`, saavad võtme oma nimest. Liituda saab igaüks, kes nime teab, seega pea ka neid avalikeks.
- **Privaatsed kanalid** kasutavad juhuslikku võtit, mida jagad ise, näiteks QR-koodina.

Teadaanded on allkirjastatud, kuid krüpteerimata. Sinu sõlme nime ja jagamise korral ka asukohta näevad kõik levialas olijad. Vali nimi, mis ei ütle rohkem, kui soovid.

## 868 MHz sagedusala Euroopas {#band}

Euroopas kasutab MeshCore väikest osa 868 MHz sagedusalast, mida tohib igaüks kasutada ilma litsentsita. Selle Euroopa raadioeelseadistus EU/UK (Narrow) asub sagedusel 869.618 MHz ja kasutab 62.5 kHz kanalit. See jääb 869.40-869.65 MHz alamsagedusala sisse, kus on lubatud kuni 500 mW e.r.p. Seade tohib seal saata kõige rohkem 10% ajast. Üksikasjad ja piirangud riigiti leiad [repiiteri juhendi õigusjaotisest](/repeater-guide/#legal).

Kõik ühe piirkonna inimesed kasutavad sama eelseadistust, muidu ei kuule nende raadiod üksteist. Mõned riigid ja piirkonnad kasutavad varianti: sinu [kohalik rühm](/community/) teab, millist.

## Milleks inimesed seda kasutavad {#uses}

- Ühenduses püsimine matkadel, merel ja festivalidel, kus mobiilivõrk on ülekoormatud või puudub.
- Varukanal perele või naabritele, kui elekter või mobiilivõrgud kaovad.
- Varulahendus kohalikele omavalitsustele, kui nende tavalised võrgud ei tööta.
- Kohalik vestlus raadiotega, mis on inimeste endi omad.
- Otsingu- ja päästemeeskonna omavaheline ühendus seal, kus mobiilivõrku pole. Kogukonna rakendus MeshCore SAR lehel [Projektid](/projects/) lisab kaardid ja jagatud asukohad.
- Kaugel asuva paiga kontrollimine kodust. Kui sa küsid, teatavad repiitrid ja andurisõlmed oma aku pinge ja muud näidud.
- Anduri jälgimine. Andurisõlmes töötab MeshCore'i mõõtmispüsivara. See salvestab oma aku pinge ajaloo. Logi sisse administraatorina ja see hoiatab sind, kui aku hakkab tühjenema. Teiste näitude jaoks lisad hoiatused oma koodiga.
- Kaugel asuva seadme, näiteks pumba lülitamine. Selle lisad andurisõlme püsivarasse oma koodiga.
- Katsetamine raadioside, antennide, päikeseenergia ja avatud lähtekoodiga tarkvaraga.

Mõned ametiasutused ehitavad või katsetavad MeshCore'i põhjal varulahendust. Kontrollisime neid näiteid 2026. aasta novembris.

- Tsüklon Gabrielle katkestas Uus-Meremaal Tairāwhitis kogu side. 2025. aasta
  septembris nimetas piirkonna hädaolukorrateenistus MeshCore'i
  [üheks vähemalt 6 varusidevahendist](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Teenistus ehitas ka võrgu selgrooks päikeseenergial töötavaid repiitereid.
- Saksamaal ehitab Bad Kissingeni maakond
  [MeshCore'il põhinevat tekstivõrku](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  ametiasutustele, päästeteenistustele ja elutähtsatele objektidele. Esimesena
  liituvad tuletõrjedepood.
- Hollandis kiitis Hilversumi volikogu
  [34 poolt- ja 1 vastuhäälega heaks katse](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien),
  mille repiiter asub raekoja tornis. Omavalitsus
  [hindab katset 2027. aasta sügisel](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Kaks Hollandi turvalisuspiirkonda, mis korraldavad kriisile reageerimist,
  katsetavad MeshCore'i:
  [Lõuna-Limburg](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  ja [Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Drenthe sõnul on veel vara öelda, kuidas või millal piirkond seda kasutada saaks.
- Dalfsenis, samuti Hollandis,
  [korraldavad vabatahtlikud koos omavalitsustega pilootprojekti](https://noodnetoverijssel.nl/).
  Nad kasutavad esmalt häälraadiot ja teise kihina MeshCore'i tekstisõnumite jaoks.

Kas sinu lähedal olev võrk hädaolukorras toimib, seda ei tea keegi.

## Kust andmed pärinevad {#data}

Lehe [kohalikud rühmad](/community/) otsing leiab koha [GeoNamesi](https://www.geonames.org/) tasuta kohanimede ja postiindeksite loendite koopiast, mille litsents on [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Koopia asub sellel saidil. Sinu otsing jääb sinu seadmesse ja GeoNamesile ei lähe ühtegi päringut.
