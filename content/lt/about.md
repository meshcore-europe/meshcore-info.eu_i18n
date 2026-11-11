---
title: Kas yra MeshCore?
lead: MeshCore perduoda tekstines žinutes radijo bangomis, nuo mazgo iki mazgo. Jam nereikia nei interneto, nei abonemento.
description: 'Kas yra MeshCore ir kas ne: mazgų tipai, maršrutizavimas, šifravimas ir 868 MHz juosta.'
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

MeshCore yra nemokama programinė įranga mažiems LoRa radijo įrenginiams. LoRa yra radijo technologija: ji perduoda nedaug duomenų toli ir naudoja labai mažai energijos. Radijo įrenginys su MeshCore vadinamas *mazgu*. Susiek jį su programėle telefone ar nešiojamajame kompiuteryje arba naudok jo paties ekraną ir klaviatūrą. Taip galėsi siųsti tekstą žmonėms, esantiems už kilometrų. Tarp tavęs ir jų nėra jokio bokšto, maršrutizatoriaus ar paslaugų teikėjo.

Programinės įrangos kodas yra atviras. Ji kuriama saugykloje [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) pagal MIT licenciją.

## Kas MeshCore nėra {#not}

Radijo ryšys tau naujas? Štai ko žmonės dažniausiai tikisi iš MeshCore, o jis to nedaro.

- **Tai nėra internetas ar telefonas.** MeshCore siunčia trumpas tekstines žinutes,
  maždaug tokio ilgio kaip SMS tavo telefone. Jokio balso, nuotraukų, vaizdo įrašų
  ar svetainių, be to, negali susisiekti su įprastu telefono numeriu.
- **Tai nėra skubiosios pagalbos tarnyba.** Jokia skubiosios pagalbos tarnyba nežada klausytis
  mesh tinklo. Žinome, kad mesh tinklas gali veikti. Ar jis veiks
  ekstremalioje situacijoje, niekas nežino.
- **Tai veikia ne akimirksniu ir ne visur.** Žinutė šuoliais keliauja nuo vieno radijo prie
  kito ir gali užtrukti kelias sekundes arba visai nepasiekti adresato.
  Ar ji pasieks tikslą, priklauso nuo retransliatorių aplink tave, aukščio, pastatų ir
  tavo antenos. Mažas radijas patalpoje dažnai nepasiekia nieko. Retransliatorius
  ant stogo siekia kilometrus.
- **Tai nėra paslauga, kurią kažkas tau teikia.** Nėra teikėjo, nėra
  pagalbos linijos ir nėra aprėpties pažado. Mesh tinklas veikia ten, kur
  bendruomenės žmonės įrengė retransliatorius.
- **Ne viskas jame yra privatu.** Tiesioginės žinutės šifruojamos, tačiau
  Public ir grotažymių kanalus gali skaityti bet kas, o tavo mazgo
  pavadinimą ir bendrinamą vietą mato visi, kas yra ryšio zonoje.
  [Stebėtojai](/network/) praneša viešiems žemėlapiams, ką girdi.
  [Šifravimo skyriuje](#encryption) paaiškinta, kas lieka privatu.
- **Ištekliai nėra neriboti.** Visi vienos vietovės naudotojai dalijasi vienu radijo kanalu,
  o [868 MHz juostos](#band) taisyklės riboja, kiek laiko kiekvienas radijas gali siųsti.
  Kiekviena žinutė atima eterio laiko iš visų kitų, todėl botai, dažni skelbimai
  ir bandomosios žinutės sulėtina mesh tinklą visiems.
- **Tai nėra Meshtastic.** Meshtastic yra kita sistema, kuri veikia
  beveik tose pačiose plokštėse. Šios dvi sistemos negali susikalbėti.

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

- Ryšys žygiuose, jūroje ir festivaliuose, kur mobilusis tinklas
  perkrautas arba jo nėra.
- Atsarginis ryšio kanalas šeimai ar kaimynams, kai dingsta elektra ar
  mobilusis ryšys.
- Atsarginis ryšys vietos valdžios institucijoms, kai neveikia jų įprasti tinklai.
- Vietiniai pokalbiai per radijo stotis, kurias žmonės turi patys.
- Ryšys paieškos ir gelbėjimo komandai ten, kur nėra mobiliojo tinklo.
  Bendruomenės programėlė MeshCore SAR (rasi ją [Projektuose](/projects/))
  prideda žemėlapius ir bendrinamas buvimo vietas.
- Nutolusios vietos patikra iš namų. Retransliatoriai ir jutiklių mazgai praneša
  savo baterijos įtampą ir kitus rodmenis, kai jų paprašai.
- Jutiklio stebėjimas. Jutiklio mazge veikia MeshCore matavimų programinė įranga.
  Jis saugo savo baterijos įtampos istoriją. Prisijunk kaip administratorius, ir jis
  įspės tave, kai baterija senka. Įspėjimus apie kitus rodmenis pridedi
  savo kodu.
- Toli esančio įrenginio, pavyzdžiui, siurblio, įjungimas ir išjungimas. Šią
  funkciją prie jutiklio programinės įrangos pridedi savo kodu.
- Eksperimentai su radiju, antenomis, saulės energija ir atvirojo kodo programine įranga.

Kai kurios valdžios institucijos kuria arba bando atsarginį ryšį MeshCore pagrindu. Šiuos pavyzdžius patikrinome 2026 m. lapkritį.

- Ciklonas Gabrielle nutraukė visą ryšį Naujosios Zelandijos Tairāwhiti regione. 2025 m.
  rugsėjį regiono ekstremaliųjų situacijų valdymo tarnyba paskelbė MeshCore
  [vienu iš bent 6 atsarginių ryšio būdų](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Tinklo pagrindui ji taip pat statė saulės energija maitinamus retransliatorius.
- Vokietijos Bad Kisingeno apskritis
  [MeshCore pagrindu kuria tekstinių žinučių tinklą](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  valdžios institucijoms, pagalbos tarnyboms ir svarbiems objektams. Pirmosios
  jungiasi gaisrinės.
- Nyderlandų Hilversumo miesto taryba
  [34 balsais prieš 1 pritarė bandymui](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  su retransliatoriumi ant rotušės bokšto. Savivaldybė
  [bandymą įvertins 2027 m. rudenį](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Du Nyderlandų saugos regionai, atsakingi už reagavimą į krizes,
  išbando MeshCore:
  [Pietų Limburgas](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  ir [Drentė](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Drentės teigimu, dar per anksti sakyti, kaip ar kada ji galėtų jį naudoti.
- Dalfsene, taip pat Nyderlanduose, savanoriai
  [kartu su savivaldybėmis vykdo bandomąjį projektą](https://noodnetoverijssel.nl/).
  Pirmiausia jie naudoja balso radijo ryšį, o MeshCore yra antrasis sluoksnis tekstinėms žinutėms.

Ar mesh tinklas tavo apylinkėse veiks ekstremalioje situacijoje, niekas nežino.

## Iš kur gaunami duomenys {#data}

Paieška [vietos grupių](/community/) puslapyje randa vietą pagal nemokamų [GeoNames](https://www.geonames.org/) vietovių ir pašto kodų sąrašų kopiją. Šiems sąrašams taikoma [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) licencija. Kopija laikoma šioje svetainėje. Tavo paieška lieka tavo įrenginyje, o į GeoNames nekeliauja jokia užklausa.
