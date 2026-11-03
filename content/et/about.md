---
title: Mis on MeshCore?
lead: MeshCore saadab tekstisõnumeid raadio teel, sõlmest sõlme. Selleks ei ole vaja internetti ega lepingut.
description: 'Mis on MeshCore ja mis see ei ole: sõlmede tüübid, marsruutimine, erinevused Meshtasticust, krüpteerimine ja 868 MHz sagedusala.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '279b56a4'
  seeded: '2026-11-02'
  fields: {title: '06eda66b', lead: 'c0174569', description: '15e6d2a7', eyebrow: '8610c822'}
  sections: ['aa768ac3', '16fde264', '0a55792c', 'c3de803d', '493b444f', 'a8b2b9b4', '429f699c', 'f8008f48', '88af2bd3', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'fab378a5', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', 'fc8f3129', '8dec428a', '07cbac35', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '95e18f18', '02f1fe2f', 'e6b5b258']
---

MeshCore on tasuta tarkvara väikestele LoRa-raadiotele. LoRa on raadiotehnika, mis saadab vähe andmeid kaugele ja kulutab väga vähe energiat. MeshCore'iga raadiot nimetatakse *sõlmeks*. Kui seod sõlme telefoni või sülearvuti rakendusega või kasutad selle enda ekraani ja klaviatuuri, saad saata teksti inimestele kilomeetrite kaugusele. Vahele ei jää ühtegi masti, ruuterit ega teenusepakkujat.

Tarkvara on avatud lähtekoodiga. Seda arendatakse hoidlas [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) MIT-litsentsi all.

## Mis MeshCore ei ole {#not}

Kas raadio on sulle uus? Siin on asjad, mida inimesed MeshCore'ilt kõige sagedamini ootavad, kuid mida see ei tee.

- **See ei ole internet ega telefon.** MeshCore saadab lühikesi tekstisõnumeid,
  umbes sama pikki kui SMS sinu telefonis. Kõnesid, fotosid, videot ega veebisaite
  siin ei ole ja tavalist telefoninumbrit sa sellega kätte ei saa.
- **See ei ole hädaabiteenus.** Ükski hädaabiteenus ei kuula seda võrku ja keegi
  ei luba, et sinu sõnumit loetakse. Hädaolukorras helista numbrile 112.
- **See ei toimi kohe ega kõikjal.** Sõnum liigub raadiolt raadiole ja võib
  kohale jõuda mõne sekundiga või üldse mitte. Kas see kohale jõuab, sõltub sinu
  ümber olevatest repiiteritest, kõrgusest, hoonetest ja sinu antennist. Väike
  raadio toas ei ulatu sageli kellenigi; repiiter katusel ulatub kilomeetrite
  kaugusele.
- **See ei ole teenus, mida keegi sinu eest haldab.** Pole teenusepakkujat,
  kasutajatuge ega lubadust, et levi on olemas. Võrk on olemas seal, kuhu
  kogukonna inimesed on repiitereid üles pannud, ja mitte kusagil mujal.
- **Kõik ei ole siin privaatne.** Otsesõnumid on krüpteeritud, kuid kanalit
  Public ja räsimärgiga kanaleid saab lugeda igaüks ning sinu sõlme nime ja
  jagatud asukohta näevad kõik levialas olijad.
  [Vaatlejad](/network/) edastavad kuuldu avalikele kaartidele.
  [Krüpteerimise jaotis](#encryption) selgitab, mis jääb privaatseks.
- **See ei ole piiramatu.** Kõik piirkonna kasutajad jagavad üht raadiokanalit ja
  [868 MHz sagedusala](#band) reeglid piiravad, kui kaua iga raadio tohib saata.
  Iga sõnum võtab eetriaega kõigilt teistelt, nii et botid, sagedased kuulutused
  ja testsõnumid aeglustavad võrku kõigi jaoks.
- **See ei ole Meshtastic.** Meshtastic on teine süsteem, mis töötab suures osas
  samadel plaatidel. Need kaks süsteemi ei saa omavahel suhelda.
  Jaotis [Kui tuled Meshtasticust](#meshtastic) loetleb, mis töötab teisiti.

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

## Kui tuled Meshtasticu juurest {#meshtastic}

Paljud plaadid töötavad kas MeshCore'i või Meshtasticuga ja paigaldad neist selle, mida soovid. Need on erinevused, mida märkad kõigepealt. Nende aluseks on MeshCore'i versioon v1.18.0 ja Meshtasticu dokumentatsioon 2026. aasta novembrist.

- **Kes sõnumeid edasi saadab.** MeshCore'is teevad seda ainult repiiterid; sinu
  kaasseade ei tee seda kunagi. Meshtasticus saadab sõnumeid edasi ka vaikimisi
  kliendiroll, kui mõni teine sõlm pole seda juba teinud.
- **Kui kaugele sõnum jõuab.** MeshCore'i sõnum võib läbida kuni 64 repiiterit.
  Meshtasticus peatub sõnum vaikimisi pärast 3 hüpet ja hiljemalt pärast 7 hüpet.
- **Teiste sõlmede näidud.** MeshCore'i repiiterid ja andurisõlmed saadavad näite,
  nagu aku pinget, siis, kui sa neid küsid. Kogu mesh-võrgule nad neid ei saada.
- **Internet.** MeshCore'i püsivara ei ühenda mesh-võrke interneti kaudu.
  [Vaatlejad](/network/) edastavad kuuldu kaartidele ainult ühes suunas.
  Meshtasticul on sisseehitatud MQTT-moodul, mis saab sõnumeid interneti kaudu
  mesh-võrkude vahel edastada.

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

- Ühenduses püsimine matkal, merel ja festivalidel, kus mobiilivõrk on ülekoormatud
  või puudub.
- Varukanal perele või naabritele, kui elekter või mobiilivõrgud kaovad.
- Kohalik vestlus raadiotega, mis kuuluvad inimestele endile.
- Kauge koha kontrollimine kodust. Kui küsid, teatavad repiiterid ja andurisõlmed oma
  aku pinge ja muud näidud.
- Anduri jälgimine. Andurisõlmes töötab MeshCore'i mõõtmiseks mõeldud püsivara.
  See säilitab oma näitude ajalugu. Kui tellid teavitused, hoiatab see sind,
  näiteks siis, kui selle aku hakkab tühjaks saama.
- Kaugel asuva asja, näiteks pumba, lülitamine. Selle võimaluse lisad anduri püsivarale oma koodiga.
- Katsetamine raadio, antennide, päikeseenergia ja avatud lähtekoodiga tarkvaraga.

## Kust andmed pärinevad {#data}

Lehe [kohalikud rühmad](/community/) otsing leiab koha [GeoNamesi](https://www.geonames.org/) tasuta kohanimede ja postiindeksite loendite koopiast, mille litsents on [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Koopia asub sellel saidil. Sinu otsing jääb sinu seadmesse ja GeoNamesile ei lähe ühtegi päringut.
