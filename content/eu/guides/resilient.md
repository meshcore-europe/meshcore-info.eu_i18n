---
title: Egin mesh sarea sendoago
lead: Zure inguruko mesh sarea motel dabil edo zaborrez beteta dago? Jakin zerk eragiten duen, piztu hori geldiarazten duen errepikagailuaren ezarpena eta esan zure tokiko taldeari.
description: 'Uholdeak eta spama MeshCore mesh sare batean: mota bakoitza nola ezagutu, zein errepikagailu-ezarpenek laguntzen duten, uholdea nola ikusi eta haren iturria nola aurkitu.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-11-02'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Mezuak berandu iristen dira edo ez dira iristen? Public kanala zaborrez betetzen da? Hori uholdea da: mesh sareak eraman dezakeena baino trafiko gehiago, nahi gabe edo nahita bidalia. Bilatu beheko tauletan ikusten duzuna. Lerro bakoitzak aipatzen du hori geldiarazten duen ezarpena. Piztu ezarpen hori zure errepikagailuan, mezuak birbidaltzen dituen nodoan. Gero, esan zure [tokiko taldeari](/community/), inguruko errepikagailuek gauza bera egin dezaten. Uholdea baztertzen duen errepikagailu bakoitzak aire-denbora uzten die gainerako guztiei.

## Nahi gabeko uholdeak {#mistake}

Nahi gabeko uholdea nodo batetik dator, eta jabeak ez daki nodoak uholdea sortzen duenik. Jabeak jakiten duenean, uholdea gelditu egiten da. Beheko tauletan, iragarkia (advert) nodo batek bidaltzen duen agurra da, besteek aurki dezaten.

Tauletako ezarpenak firmwareak egiten duenetik abiatuta daude idatzita. Horietako batzuek oraindik ez dute uholderik geldiarazi benetako mesh sare batean.

{{< callout type="warning" >}}
Orri honetako ezarpen batzuek DMC firmwarea behar dute. **MeshCore** 1.18.0 bertsio estandarrak eskualdeak, `flood.max.*` jauzi-mugak, begizten detekzioa eta duty cycle-a ditu. Pakete-iragazkia, zure errepikagailuari zaborra baztertzen uzten dioten arauak, [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) taldearen **DMC firmwarearekin** dator. Duty cycle bidezko atea eta companion iragazkia ere bai. Orri honek 2026ko urriaren 19ko DMC 1.18.0 dev build `ecfb2d4` hartzen du oinarri; [pakete-iragazkiaren](/guides/filter/#firmware) orrian esaten da non lortu.
{{< /callout >}}

| Zer ikusten duzun | Zer den | Zerk laguntzen duen |
| --- | --- | --- |
| Nodo bakar batetik errepikagailuei egindako eskaerak, gau eta egun, eta egunetan motel dagoen mesh sarea | Errepikagailuei egoera maizegi eskatzen dien etxe-automatizazioa edo bota | `filter on`. Orduan pakete-iragazkiak minutuan 5 eskaera pasatzen uzten ditu. Esan jabeari. |
| Mezu mota bera kanal batean, minuturo | Maizegi argitaratzen duen bota | [Blokeatu kanala](/guides/filter/#channel) edo [moteldu igorlea](/guides/filter/#sender). Esan jabeari. |
| Mezu irakurtezinak Public kanalean eta beste kanaletan | Firmware hondatua edo irrati-ezarpen okerrak dituen nodoa | `filter malformed on` aginduak Public kanalean baztertzen ditu. Esan jabeari. |
| Nodo baten iragarkia minutu gutxitan behin | Maizegi iragartzeko ezarrita dagoen nodoa | `filter advert 24` aginduak nodo bakoitzaren iragarki bat pasatzen uzten du egunean. `set flood.max.advert 3` aginduak iragarkiak 3 jauziren barruan mantentzen ditu. |
| Urrutitik datozen mezuak, hemengoak ez diren eskualdeekin | Mesh sareak internet bidez lotzen dituen zubia | `set flood.max.unscoped 1`, eta jarri zure errepikagailua [zerbitzatzen dituen eskualdeetan](/guides/settings/#traffic) soilik. |
| Mezu bera behin eta berriz pasatzen da, eta zure errepikagailuaren IDa behin baino gehiagotan ageri da bidean | Paketeak aldatu eta birbidaltzen dituen errepikagailua, eta horregatik paketeek begizta egiten dute | Begizten detekzioa `minimal` mailan dabil lehenespenez. `set loop.detect moderate` aginduak begizta lehenago baztertzen du. |

## Nahita egindako uholdeak {#purpose}

Uholde batzuk spama dira: mesh sarea buxatzeko nahita bidalitako zaborra. Igorleak izenak, gakoak eta bideak aldatzen ditu, eta beraz arau bakar batek ere ez du uholdea geldiarazten.

| Zer ikusten duzun | Zer den | Zerk laguntzen duen |
| --- | --- | --- |
| Ausazko izena duten nodo berri asko, bakoitza gako berri batekin | Iragarki faltsuak | `filter rate 04 5 60` aginduak minutuan 5 iragarki pasatzen uzten ditu. `filter advert` aginduak ez du laguntzen: iragarki bakoitza [gako berri](#forged) batetik dator. |
| Testu irakurtezina duten mezuak, igorle asmatuetatik, askotan duela urtebete baino gehiagoko datarekin | Kanaleko spama | `filter malformed on` aginduak Public kanalean baztertzen ditu. `filter age 60` aginduak data zaharrekoak baztertzen ditu Public kanalean eta [zaindutako kanaletan](/guides/filter/#settings). |
| Gehienez 200 mezu zuzen minutuan existitzen ez diren nodoetara, eta berrespenik ez da itzultzen | Mezu zuzenen uholdea | `filter rate 02 5 60`. Zure aplikazioak ez ditu mezu hauek erakusten; behatzaile batek bai. |
| Nodo bakar batetik beste dozenaka nodotara doazen eskaera-boladak | Eskaeren spama | `filter on` aginduarekin, pakete-iragazkiak minutuan 5 eskaera pasatzen uzten ditu. |
| Mezu bat 10 eta 20 minutu artean geroago itzultzen da, ia bide berarekin | Errepikapena (replay): berriro bidalitako kopia | Errepikagailu batek ikusi dituen azken 160 paketeak gogoratzen ditu, eta beraz mesh sare lanpetu batean geroko kopia berriro pasatzen da. `filter age` aginduak zuk onartzen duzuna baino zaharragoa den talde-mezua baztertzen du. |
| Public kanaleko mezuak, igorle asmatu baten izenean berriro bidaliak, batzuetan data zaharrarekin | Oihartzun-spama | `filter age 60`. `filter malformed on` aginduak astebete baino gehiago desbideratutako data ere baztertzen du. |
| Mezu bat segundo gutxitan behin hainbat kanaletan, bakoitza izen berri batetik, galdera arruntak eginez | Boten olatua | `filter rate 05 10 60`, eta [blokeatu](/guides/filter/#channel) zure inguruan erabiltzen ez diren kanalak. Izen guztiak berriak dira, eta beraz [igorle-arauek](#forged) ez dute harrapatzen. |

## Zerk funtzionatu duen {#worked}

Tokiko taldeek urrats hauekin geldiarazi dituzte uholdeak:

1. **Esan jabeari.** Nahi gabeko uholdea gelditu egiten da jabeak jakiten duenean. Bidali mezu atsegin bat.
2. **Ez erantzun mesh sarean.** Erantzun batek spamak funtzionatzen duela erakusten dio spamerrari.
3. **Eskatu behatzaileak.** Behatzailea entzuten duen pakete bakoitzaren berri MQTT bidez ematen duen nodoa da. Zenbat eta behatzaile gehiago inguruan, orduan eta lehenago ikusiko duzu uholdea nondik sartzen den. Bihurtu zure errepikagailua behatzaile [MQTT zure behatzailean](/guides/mqtt/) gidarekin.
4. **Aurkitu iturria.** Behatzaileek igorlea eremu batean kokatzen dute. Azken kilometroa jendeak oinez egin behar du, irrati batekin. Ikus [Aurkitu iturria](#source).
5. **Mugiarazi zure tokiko taldea.** Ezarpen egokiak dituen errepikagailu batek laguntzen du. Eremuko errepikagailu guztiek batera uholdea geldiarazten dute. Zure [tokiko taldeak](/community/) jabe guztiek ezarpena piztea lortzen du.

## Igorle eta bide asmatuak {#forged}

Igorleak pakete baten zati hauek idazten ditu, eta ezerk ez ditu egiaztatzen:

- **Igorlearen izena.** Kanal-mezu batean, izena testuaren parte da. Kanalaren gakoa duen edonork edozein izen idatz dezake.
- **Bidearen hasiera.** Errepikagailu bakoitzak bere IDa gehitzen du bidearen amaieran. Ezerk ez ditu aurretik zeuden IDak egiaztatzen, eta beraz igorleak ID asmatuekin has dezake bidea. Bidearen amaiera benetakoa da.

{{< forged-path >}}

Beraz, `filter sender` eta `filter path` aginduek igorlea izena edo bidea aldatu arte bakarrik geldiarazten dute. [Bide-blokeo](/guides/filter/#path) batek bertan IDa duen errepikagailuaren benetako trafikoa ere baztertzen du. Abiadura-mugek, jauzi-mugek, adinaren eta formatu okerraren egiaztapenek, kanal-blokeoek, eskualdeek eta duty cycle-ak funtzionatzen jarraitzen dute.

## Uholde guztietarako ezarpenak {#always}

Hauek balio dute, mesh sarea edozerk uholdatzen duela ere:

- **Duty cycle-a % 10ean.** Horrela, zure errepikagailuak ez du inoiz legeak onartzen duena baino gehiago igortzen, edozer iristen dela ere. [Errepikagailuaren gidak](/repeater-guide/#duty-cycle) azaltzen du.
- **Eskualdeak eta jauzi-mugak.** Eskualdea mezu bat barruan geratzen den eremua da. Errepikagailu batek bere eskualdeetako mezuak bakarrik birbidaltzen ditu, eta `flood.max.*` ezarpenek trafikoa gertu mantentzen dute. Biak [Mantendu trafikoa baxu](/guides/settings/#traffic) atalean daude.
- **Pakete-iragazkia errepikagailu lanpetu baterako.** [Prest dauden ezarpenek](/guides/filter/#busy) talde-mezuak eta iragarkiak erdira murrizten dituzte. Probatu lehenik [dry-run](/guides/filter/#dryrun) moduan: baztertuko lukeena zenbatzen du soilik.
- **Companion iragazkia, DMC firmwarean.** Zure companion gailuak, mezuak bidaltzeko erabiltzen duzun nodoak, zaborra zure aplikaziotik kanpo uzten du. Mezu hondatuak eta zaharrak ezkutatzen ditu, baita blokeatzen dituzun errepikagailu, igorle edo hitzen mezuak ere. Igorle- edo hitz-arau batek zuri bakarrik ezkutatzen dizu mezua; besteek jasotzen jarraitzen dute.

### Duty cycle bidezko atea {#gate}

DMC firmwarean, zure errepikagailuak bere eskualdeari lehentasuna eman diezaioke lanpetuta dagoenean. Azken minutuaren % 35 baino gehiago igorri duenean, eskualderik gabeko mezuak birbidaltzeari uzten dio. Lanpetuta jarraitzen badu, eskualderik zabalena baztertzen du ondoren, maila bat aldiro. Bere eskualdea beti pasatzen da. Atea zure errepikagailuan eskualdeak ezarrita daudenean bakarrik dabil. Piztu eta egiaztatu honela:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Ateak baztertzen duena ez da `filter stats` aginduan agertzen. Errepikagailua berriro lasai dagoenean, eskualdeak itzuli egiten dira, barnekoenetik hasita.

## Ikusi uholdea {#see}

Zure aplikazioak zuregana iristen dena bakarrik erakusten du. Existitzen ez diren nodoetara doan mezu zuzenen uholdea behatzaile batek bakarrik entzuten du. Behatzaile bakoitzak [MeshCore Analyzer](https://meshcore-analyzer.eu/) tresnari ematen dio informazioa, eta han edonork ikus dezake. Bihurtu zure errepikagailua behatzaile [MQTT zure behatzailean](/guides/mqtt/) gidarekin.

Analyzer-en, begiratu pakete baten kopia guztiak. Bideak normalean erakusten du nondik etorri den. Uholdea sortzen duenak [ID asmatuekin](#forged) has dezake bidea, eta beraz lehen IDek ez dizute ezer esaten. Baina kopia guztiek hasiera asmatu bera dute. Biderik laburrena duen kopiak benetako errepikagailu gutxien igaro ditu, eta beraz igorletik gertuen entzun zen.

{{< copies >}}

Zure errepikagailuan, `filter stats` aginduak erakusten du pakete-iragazkiak zer baztertu duen. `filter stats top` aginduak baztertze gehienen atzean dauden nodo-IDen lehen bytea erakusten du. Nodo askok dute byte hori, eta beraz bilaketa murrizten du, baina ez dizu igorlea izendatzen.

## Aurkitu iturria {#source}

Uholdea behin eta berriz itzultzen denean:

1. **Jarraitu bideei.** Irakurri bidea amaieratik: azken IDak uholdeak igarotako errepikagailuak dira. Benetako lehenengoa iturritik gertu dago; aurreko IDak [asmatuak](#forged) izan daitezke.
2. **Mugatu eremua.** Pakete bera entzuten duten hainbat behatzailek igorlea eremu batean kokatzen dute. [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) tresnak paketea entzun duten errepikagailuetatik kalkulatzen du eremua.
3. **Egin azken kilometroa oinez.** Errepikagailuek iturria beren irismenaren ertzean bakarrik entzuten dute, eta beraz azken zatia jendeak oinez egin behar du. [Mesh-Hunter](https://mesh-hunter.eu/) zure companion gailuarekin parekatzen da, eta entzuten duen pakete bakoitza zure GPS kokapenarekin erregistratzen du. Hainbat lagun aldi berean ibiltzen badira, lehenago aurkitzen dute iturria.
4. **Esan zure [tokiko taldeari](/community/).** Taldeak mesh sarearen zati handiagoa ikusten du, hurrengo urratsa erabakitzen du eta nahita uholdatzen duenarekin harremanetan jartzen da.

## Gehitu ikusi duzuna {#add}

Tauletan ez dagoen uholde batek jo zaitu? Ezarpen batek uholde bat geldiarazi du? Esan iezaguzu [Discord](https://discord.meshcore-info.eu/) bidez: zer ikusi duzun eta zer piztu duzun. Orrira gehituko dugu.
