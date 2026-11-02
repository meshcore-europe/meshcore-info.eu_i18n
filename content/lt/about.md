---
title: Kas yra MeshCore?
lead: MeshCore perduoda tekstines žinutes radijo bangomis, nuo mazgo iki mazgo. Jam nereikia nei interneto, nei abonemento.
description: 'Kas yra MeshCore ir kas juo nėra: mesh tinklas, kompanionai, retransliatoriai ir kambario serveriai, maršrutai, šifravimas ir 868 MHz juosta Europoje.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '78bc31e8'
  seeded: '2026-11-02'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['aa768ac3', 'c9b24089', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '655373a9', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b9fc8810', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '0eb54b47', '02f1fe2f', 'e6b5b258']
---

MeshCore yra nemokama programinė įranga mažiems LoRa radijo įrenginiams. LoRa yra radijo technologija: ji perduoda nedaug duomenų toli ir naudoja labai mažai energijos. Radijo įrenginys su MeshCore vadinamas *mazgu*. Susiek jį su programėle telefone ar nešiojamajame kompiuteryje arba naudok jo paties ekraną ir klaviatūrą. Taip galėsi siųsti tekstą žmonėms, esantiems už kilometrų. Tarp tavęs ir jų nėra jokio bokšto, maršrutizatoriaus ar paslaugų teikėjo.

Programinės įrangos kodas yra atviras. Ji kuriama saugykloje [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) pagal MIT licenciją.

## Kas MeshCore nėra {#not}

Radijo ryšys tau naujas? Štai ko žmonės dažniausiai tikisi iš MeshCore, o jis to nedaro.

- **Tai nėra internetas ar telefonas.** MeshCore perduoda trumpas tekstines žinutes, maždaug tokio ilgio kaip SMS telefone. Balso, nuotraukų, vaizdo įrašų ir svetainių čia nėra, o į įprastą telefono numerį neprisiskambinsi ir neparašysi.
- **Tai nėra skubios pagalbos tarnyba.** Mesh tinklo neklauso jokia skubios pagalbos tarnyba, ir niekas nežada, kad tavo žinutę kas nors perskaitys. Ištikus nelaimei skambink 112.
- **Tai veikia ne akimirksniu ir ne visur.** Žinutė keliauja nuo vieno radijo įrenginio prie kito. Tai gali užtrukti kelias sekundes, o žinutė gali ir visai nepasiekti gavėjo. Ar ji jį pasieks, lemia aplink tave esantys retransliatoriai, aukštis, pastatai ir tavo antena. Mažas radijo įrenginys patalpoje dažnai nepasiekia nieko, o retransliatorius ant stogo siekia kilometrus.
- **Tai nėra paslauga, kurią kas nors tau teikia.** Nėra nei paslaugų teikėjo, nei pagalbos linijos, nei aprėpties pažado. Mesh tinklas yra tik ten, kur bendruomenės žmonės pastatė retransliatorius.
- **Ne viskas čia privatu.** Asmeninės žinutės yra šifruojamos, bet Public ir grotažymių kanalus gali skaityti bet kas. Tavo mazgo pavadinimą ir bendrinamą vietą mato visi, esantys ryšio zonoje. [Stebėtojai](/network/) tai, ką girdi, perduoda į viešus žemėlapius. [Šifravimo skyriuje](#encryption) paaiškinta, kas lieka privatu.
- **Tai nėra neribotas ryšys.** Visi vienos vietovės žmonės dalijasi vienu radijo kanalu, o [868 MHz juostos](#band) taisyklės riboja, kiek laiko kiekvienas radijo įrenginys gali siųsti. Kiekviena žinutė atima eterio laiką iš visų kitų, todėl botai, dažni skelbimai ir bandomosios žinutės lėtina mesh tinklą visiems.
- **Tai nėra Meshtastic.** Meshtastic yra kita sistema, veikianti beveik tose pačiose plokštėse. Šios dvi sistemos negali susikalbėti.

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

- Ryšiui žygiuose, jūroje ir festivaliuose, kur mobilusis tinklas perkrautas arba jo nėra.
- Atsarginiam ryšio kanalui su šeima ar kaimynais, kai dingsta elektra arba mobilieji tinklai.
- Vietos pokalbiams radijo įrenginiais, kurie priklauso patiems žmonėms.
- Eksperimentams su radiju, antenomis, saulės energija ir atvirojo kodo programine įranga.

## Iš kur gaunami duomenys {#data}

Paieška [vietos grupių](/community/) puslapyje randa vietą pagal nemokamų [GeoNames](https://www.geonames.org/) vietovių ir pašto kodų sąrašų kopiją. Šiems sąrašams taikoma [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) licencija. Kopija laikoma šioje svetainėje. Tavo paieška lieka tavo įrenginyje, o į GeoNames nekeliauja jokia užklausa.
