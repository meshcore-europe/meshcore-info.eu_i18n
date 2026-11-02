---
title: Kas yra MeshCore?
lead: MeshCore perduoda tekstines žinutes radijo bangomis, nuo mazgo iki mazgo. Jam nereikia nei interneto, nei abonemento.
description: 'Kas yra MeshCore ir kas juo nėra: mazgų tipai, maršrutizavimas, skirtumai nuo Meshtastic, šifravimas ir 868 MHz juosta.'
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

MeshCore yra nemokama programinė įranga mažiems LoRa radijo įrenginiams. LoRa yra radijo technologija: ji perduoda nedaug duomenų toli ir naudoja labai mažai energijos. Radijo įrenginys su MeshCore vadinamas *mazgu*. Susiek jį su programėle telefone ar nešiojamajame kompiuteryje arba naudok jo paties ekraną ir klaviatūrą. Taip galėsi siųsti tekstą žmonėms, esantiems už kilometrų. Tarp tavęs ir jų nėra jokio bokšto, maršrutizatoriaus ar paslaugų teikėjo.

Programinės įrangos kodas yra atviras. Ji kuriama saugykloje [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) pagal MIT licenciją.

## Kas MeshCore nėra {#not}

Radijo ryšys tau naujas? Štai ko žmonės dažniausiai tikisi iš MeshCore, o jis to nedaro.

- **Tai nėra internetas ar telefonas.** MeshCore siunčia trumpas tekstines žinutes,
  maždaug tokio ilgio kaip žinutė tavo telefone. Balso, nuotraukų, vaizdo įrašų
  ar svetainių nėra, o įprasto telefono numerio nepasieksi.
- **Tai nėra skubios pagalbos tarnyba.** Jokia skubios pagalbos tarnyba tinklo neklauso, ir niekas
  nežada, kad kas nors perskaitys tavo žinutę. Nelaimės atveju skambink 112.
- **Tai veikia ne akimirksniu ir ne visur.** Žinutė keliauja nuo vieno radijo įrenginio
  prie kito ir gali užtrukti kelias sekundes arba visai nepasiekti gavėjo.
  Ar ji pasieks gavėją, priklauso nuo aplinkinių retransliatorių, aukščio, pastatų ir
  tavo antenos. Mažas radijo įrenginys patalpoje dažnai nieko nepasiekia;
  retransliatorius ant stogo pasiekia kilometrų atstumu.
- **Tai nėra paslauga, kurią kažkas tau teikia.** Nėra nei teikėjo, nei pagalbos
  linijos, nei aprėpties pažado. Tinklas yra ten, kur bendruomenės žmonės pastatė
  retransliatorius, ir niekur kitur.
- **Ne viskas čia privatu.** Tiesioginės žinutės šifruojamos, bet Public ir
  grotažymių kanalus gali skaityti bet kas, o tavo mazgo pavadinimą ir bendrinamą
  vietą mato visi ryšio zonoje.
  [Stebėtojai](/network/) tai, ką girdi, perduoda į viešus žemėlapius.
  [Šifravimo skyriuje](#encryption) paaiškinta, kas lieka privatu.
- **Tai nėra neribota.** Visi vienoje vietovėje dalijasi vienu radijo kanalu, o
  [868 MHz juostos](#band) taisyklės riboja, kiek laiko kiekvienas radijo įrenginys
  gali siųsti. Kiekviena žinutė atima eterio laiką iš visų kitų, todėl botai, dažni
  skelbimai ir bandomosios žinutės lėtina tinklą visiems.
- **Tai nėra Meshtastic.** Meshtastic yra kita sistema, veikianti beveik tose pačiose
  plokštėse. Šios dvi sistemos tarpusavyje nesusikalba.
  Skyriuje [Jei pereini iš Meshtastic](#meshtastic) rasi, kas veikia kitaip.

## Mesh tinklas per minutę {#mesh}

Vienas LoRa radijo įrenginys mieste pasiekia kelis kilometrus, o nuo kalvos ar stogo gerokai toliau. Kad žinutės nukeliautų toliau, radijo įrenginiai perduoda jas vienas kitam: tai ir yra *mesh* tinklas. MeshCore tinkle žinutes perduoda radijo įrenginiai, vadinami *retransliatoriais*. Išgirdęs žinutę, retransliatorius išsiunčia ją dar kartą, todėl ji gali nukeliauti per visą regioną.

Mesh tinklas niekam nepriklauso. Kiekvienas mazgas ir kiekvienas retransliatorius priklauso kuriam nors bendruomenės nariui. Tinklas siekia tiek, kiek siekia jų retransliatoriai.

## 3 mazgų rūšys {#roles}

Mazgo rūšį pasirenki, kai įrašai jam programinę įrangą. Tavo pirmasis mazgas yra kompanionas.

**Kompanionas.** Tai tavo asmeninis radijo įrenginys. Su MeshCore programėle telefone ar nešiojamajame kompiuteryje jį susieji per Bluetooth arba USB, o kai kurie kompanionai turi savo ekraną ir klaviatūrą. Programėlėje skaitai ir rašai žinutes. Kompanionas saugo tavo kontaktus ir kanalus, taip pat žinutes, atėjusias, kol programėlė nebuvo prijungta. Kitų žinučių kompanionas neperduoda.

**Retransliatorius.** Tai aukštai pastatytas radijo įrenginys, kuris perduoda visų žinutes. Dauguma jų veikia saulės energija. Savo retransliatoriaus tau reikia tik ten, kur mesh tinklas dar nesiekia. Atskiros programėlės jis neturi. Jį nustatai per USB arba prisijungi slaptažodžiu ir valdai radijo ryšiu. Kaip tai padaryti, rasi [retransliatoriaus vadove](/repeater-guide/).

**Kambario serveris.** Tai nedidelė skelbimų lenta mesh tinkle. Prisijungęs gauni įrašus, kuriuos praleidai būdamas už ryšio zonos ribų, iki 32 paskutinių. Serveris laiko juos tik atmintyje, todėl paleidus jį iš naujo ar dingus elektrai jie išsitrina. Vietos grupė naudoja jį pranešimams.

## Kaip žinutė randa kelią {#routing}

Kiekvienas mazgas turi slaptąjį ir viešąjį raktą. Viešasis raktas yra mazgo tapatybė. Mazgas apie save praneša *skelbimu*: tai pasirašytas paketas su jo pavadinimu ir, jei nori, vieta. Žmogus atsiranda tavo kontaktuose, kai tave pasiekia vienas iš jo skelbimų arba kai nuskenuoji jo QR kodą. Programėlėje yra mygtukas, kuriuo išsiunti savo skelbimą.

Pirmoji tavo žinutė kontaktui iškeliauja *užtvindymu*. Kiekvienas ją išgirdęs retransliatorius perduoda ją vieną kartą ir pakeliui prideda savo trumpą ID. Atsakymas parneša šį ID sąrašą atgal. Nuo tada tavo žinutės tam kontaktui keliauja įrašytu maršrutu, o siunčia tik jame esantys retransliatoriai. Kai maršrutas nutrūksta, programėlė vėl siunčia užtvindymu.

Kanalo žinutės neturi vieno adresato, todėl visada keliauja užtvindymu. Retransliatoriai įsimena, ką neseniai perdavė, ir atmeta kopijas, kurios dar kartą atkeliauja kitu maršrutu. Žinutė gali pereiti per iki 64 retransliatorių, o jei profilis naudoja 2 baitų ID, per iki 32.

## Jei pereini iš Meshtastic {#meshtastic}

Daugelis plokščių veikia su MeshCore arba Meshtastic, o tu įrašai tą, kurio nori.
Štai skirtumai, kuriuos pastebėsi pirmiausia. Jie remiasi MeshCore
v1.18.0 ir 2026 m. lapkričio mėn. Meshtastic dokumentacija.

- **Kas perduoda žinutes.** MeshCore tinkle tai daro tik retransliatoriai, tavo kompanionas
  niekada jų neperduoda. Meshtastic tinkle žinutes perduoda ir mazgas su numatytuoju kliento vaidmeniu,
  nebent kitas mazgas tai jau padarė.
- **Kiek toli keliauja žinutė.** MeshCore žinutė gali pereiti daugiausia per 64
  retransliatorius. Meshtastic pagal numatytuosius nustatymus žinutę sustabdo po 3 šuolių, o daugiausia leidžia 7.
- **Kitų mazgų rodmenys.** MeshCore retransliatoriai ir jutiklių mazgai siunčia
  rodmenis, pavyzdžiui, baterijos įtampą, kai jų paprašai. Visam mesh tinklui jie jų
  nesiunčia.
- **Internetas.** MeshCore programinėje įrangoje nėra ryšio tarp mesh tinklų per
  internetą. [Stebėtojai](/network/) tai, ką girdi, praneša žemėlapiams, tik viena
  kryptimi. Meshtastic turi integruotą MQTT modulį,
  kuris gali perduoti žinutes tarp mesh tinklų per internetą.

## Šifravimas ir privatumas {#encryption}

Tavo asmeninės žinutės šifruojamos nuo galo iki galo: jas gali skaityti tik tu ir kitas žmogus. Retransliatorius mato, kam skirtas paketas, tik pagal 1 baito užuominą.

Kanalai šifruojami bendru raktu, todėl tai, kas gali juos skaityti, priklauso nuo to, kas turi tą raktą:

- **Public** yra nustatytas kiekviename kompanione. Jo raktas paskelbtas, todėl šį kanalą gali skaityti bet kas.
- **Grotažymių kanalai**, tokie kaip `#utrecht`, raktą gauna iš savo pavadinimo. Prisijungti gali kiekvienas, kas žino pavadinimą, todėl laikyk juos irgi viešais.
- **Privatūs kanalai** naudoja atsitiktinį raktą, kuriuo dalijiesi pats, pavyzdžiui, QR kodu.

Skelbimai pasirašomi, bet nešifruojami. Tavo mazgo pavadinimą ir vietą, jei ja dalijiesi, mato visi, esantys ryšio zonoje. Rinkis pavadinimą, kuris neatskleidžia daugiau, nei nori.

## 868 MHz juosta Europoje {#band}

Europoje MeshCore naudoja nedidelę 868 MHz juostos dalį, kurią kiekvienas gali naudoti be licencijos. Europos radijo profilis EU/UK (Narrow) veikia 869.618 MHz dažniu, 62.5 kHz pločio kanale. Tai patenka į 869.40-869.65 MHz pajuostę, kurioje leidžiama iki 500 mW e.r.p. Įrenginys joje gali siųsti ne daugiau kaip 10% laiko. Išsamiau apie tai ir apie kiekvienos šalies ribas rasi [retransliatoriaus vadovo teisiniame skyriuje](/repeater-guide/#legal).

Visi vienos vietovės žmonės naudoja tą patį profilį, kitaip jų radijo įrenginiai vienas kito negirdi. Kai kurios šalys ir regionai naudoja kitą variantą: kurį, žino tavo [vietos grupė](/community/).

## Kam žmonės jį naudoja {#uses}

- Ryšio palaikymas žygiuose, jūroje ir festivaliuose, kur mobilusis tinklas
  perkrautas arba jo nėra.
- Atsarginis kanalas šeimai ar kaimynams, kai dingsta elektra ar neveikia
  mobilusis tinklas.
- Vietiniai pokalbiai žmonių nuosavais radijo įrenginiais.
- Tolimos vietos patikra iš namų. Kai paprašai, retransliatoriai ir jutiklių
  mazgai praneša baterijos įtampą ir kitus rodmenis.
- Jutiklio stebėjimas. Jutiklio mazge veikia MeshCore programinė įranga,
  skirta matavimams. Jis saugo savo rodmenų istoriją. Jei užsiprenumeruoji, jis
  tave įspėja, pavyzdžiui, kai senka jo baterija.
- Nuotolinis ko nors perjungimas, pavyzdžiui, siurblio. Tai į jutiklio
  programinę įrangą pridedi savo kodu.
- Eksperimentai su radiju, antenomis, saulės energija ir atvirojo kodo
  programine įranga.

## Iš kur gaunami duomenys {#data}

Paieška [vietos grupių](/community/) puslapyje randa vietą pagal nemokamų [GeoNames](https://www.geonames.org/) vietovių ir pašto kodų sąrašų kopiją. Šiems sąrašams taikoma [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) licencija. Kopija laikoma šioje svetainėje. Tavo paieška lieka tavo įrenginyje, o į GeoNames nekeliauja jokia užklausa.
