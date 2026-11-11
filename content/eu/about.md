---
title: Zer da MeshCore?
lead: MeshCore-k testu-mezuak irratiz bidaltzen ditu, nodotik nodora. Ez du internetik edo harpidetzarik behar.
description: 'MeshCore zer den eta zer ez den: nodo motak, bideratzea, enkriptatzea eta 868 MHz-eko banda.'
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

MeshCore LoRa irrati txikietarako software librea da. LoRa irrati-teknika bat da: datu gutxi urrutira bidaltzen ditu, oso energia gutxirekin. MeshCore duen irrati bati *nodo* esaten zaio. Zure telefonoko edo eramangarriko aplikazioarekin parekatuta, edo bere pantaila eta teklatuarekin, testua bidaltzen die kilometroetara dagoen jendeari. Tartean ez dago dorrerik, bideratzailerik edo hornitzailerik.

Softwarea kode irekikoa da. [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) proiektuan garatzen dute, MIT lizentziapean.

## Zer ez den MeshCore {#not}

Irratien munduan berria zara? Hauek dira jendeak MeshCore-ri gehien eskatzen dizkion gauzak, eta MeshCore-k egiten ez dituenak.

- **Ez da internet, ezta telefono bat ere.** MeshCore-k testu-mezu laburrak bidaltzen ditu, telefonoko SMS baten luzera gutxi gorabehera. Ez dago ahotsik, argazkirik, bideorik edo webgunerik. Ezin duzu telefono-zenbaki arrunt batera deitu edo idatzi.
- **Ez da larrialdi-zerbitzu bat.** Larrialdi-zerbitzu batek ere ez du hitzematen mesh sarean entzungo duenik. Badakigu mesh sareak funtziona dezakeela. Larrialdi batean funtzionatzen duen, inork ez daki.
- **Ez da berehalakoa, eta ez dago leku guztietan.** Mezu bat irratiz irrati jauzika doa, eta segundo batzuk behar ditzake, edo baliteke ez iristea ere. Iristen den ala ez, zure inguruko errepikagailuen araberakoa da, baita altueraren, eraikinen eta zure antenaren araberakoa ere. Etxe barruko irrati txiki bat askotan ez da inorengana iristen. Teilatu bateko errepikagailu bat kilometroetara iristen da.
- **Ez da norbaitek zuretzat kudeatzen duen zerbitzu bat.** Ez dago hornitzailerik, laguntza-zerbitzurik edo estaldura-bermerik. Mesh sarea komunitateko jendeak errepikagailuak jarri dituen lekuetan dago.
- **Bertan dagoen guztia ez da pribatua.** Mezu zuzenak enkriptatuta daude. Hala ere, edonork irakur ditzake Public eta traola-kanalak, eta zure nodoaren izena eta partekatutako kokapena irismenean dagoen edonork ikusten ditu. [Behatzaileek](/network/) entzuten dutena mapa publikoetara bidaltzen dute. [Enkriptazioari buruzko atalak](#encryption) azaltzen du zer geratzen den pribatu.
- **Ez da mugagabea.** Eremu bateko guztiek irrati-kanal bakarra partekatzen dute, eta [868 MHz bandako](#band) arauek mugatzen dute irrati bakoitzak zenbat denbora igor dezakeen. Mezu bakoitzak besteen emisio-denbora kentzen du. Horregatik, botek, maiz bidalitako iragarkiek eta proba-mezuek mesh sarea moteltzen dute guztientzat.
- **Ez da Meshtastic.** Meshtastic beste sistema bat da, eta plaka ia berdinetan dabil. Bi sistemek ezin dute elkarren artean hitz egin.

## Mesh sarea minutu batean {#mesh}

LoRa irrati bat kilometro gutxi batzuetara iristen da herri batean, eta askoz urrunago muino edo teilatu batetik. Urrunago iristeko, irratiek elkarri pasatzen dizkiote mezuak: hori da *mesh* sarea. MeshCore-n, *errepikagailu* izeneko irratiek pasatzen dituzte mezuak. Errepikagailu batek mezu bat entzutean, berriro bidaltzen du, eta horrela mezuak eskualde oso bat zeharka dezake.

Mesh sarea ez da inorena. Nodo eta errepikagailu bakoitza komunitateko norbaitena da. Mesh sarea haien errepikagailuak iristen diren lekuraino iristen da.

## 3 nodo motak {#roles}

Nodoaren mota firmwarea grabatzean aukeratzen duzu. Zure lehen nodoa companion bat da.

**Companion.** Zeure irratia. Telefonoko edo eramangarriko MeshCore aplikazioarekin parekatzen duzu, Bluetooth edo USB bidez; batzuek beren pantaila eta teklatua dituzte. Aplikazioan irakurtzen eta idazten duzu. Companionak zure kontaktuak eta kanalak gordetzen ditu, baita aplikazioa konektatu gabe zegoela iritsitako mezuak ere. Companion batek ez ditu besteen mezuak pasatzen.

**Errepikagailua.** Leku altuan jarritako irratia, guztien mezuak pasatzen dituena. Gehienek eguzki-energiarekin funtzionatzen dute. Zeurea mesh sarea oraindik iristen ez den tokian baino ez duzu behar. Ez du bere aplikaziorik. USB bidez konfiguratzen duzu, edo pasahitzarekin saioa hasi eta irratiz kudeatzen duzu. [Errepikagailuen gidan](/repeater-guide/) azaltzen da nola egin.

**Gela-zerbitzaria.** Mesh sareko mezu-taula txiki bat. Saioa hastean, irismenetik kanpo zinela galdu dituzun argitalpenak jasotzen dituzu, gehienez azken 32ak. Memorian bakarrik gordetzen ditu, beraz berrabiarazte batek edo argindar-etete batek ezabatu egiten ditu. Tokiko talde batek iragarpenetarako erabiltzen du.

## Nola aurkitzen duen mezuak bidea {#routing}

Nodo bakoitzak gako sekretu bat eta gako publiko bat ditu. Gako publikoa nodoaren nortasuna da. Nodoak *iragarki* baten bidez aurkezten du bere burua: izena eta, zuk nahi baduzu, kokapena dituen pakete sinatu bat. Norbait zure kontaktuetan agertzen da haren iragarki bat zuregana iritsi ondoren, edo haren QR kodea eskaneatzen duzunean. Aplikazioak botoi bat du zurea bidaltzeko.

Kontaktu bati bidaltzen diozun lehen mezua *uholde* gisa ateratzen da. Mezua entzuten duen errepikagailu bakoitzak behin pasatzen du, eta bidean bere ID laburra gehitzen dio. Erantzunak ID zerrenda hori dakar atzera. Hortik aurrera, kontaktu horri bidaltzen dizkiozun mezuek erregistratutako bideari jarraitzen diote, eta bide horretako errepikagailuek bakarrik igortzen dute. Bidea hausten denean, aplikazioak berriro bidaltzen du uholdez.

Kanaletako mezuek ez dute helbide bakarra, beraz beti uholdez doaz. Errepikagailuek gogoratzen dute zer pasatu duten duela gutxi, eta beste bide batetik berriro iristen diren kopiak baztertzen dituzte. Mezu batek gehienez 64 errepikagailu zeharka ditzake, edo 32, aurrezarpenak 2 byteko IDak erabiltzen dituen tokietan.

## Zifratzea eta pribatutasuna {#encryption}

Zure mezu zuzenak muturretik muturrera zifratuta doaz: zutaz eta beste pertsonaz gain, inork ezin ditu irakurri. Errepikagailu batek 1 byteko aztarna gisa bakarrik ikusten du nori doakion paketea.

Kanalak gako partekatu batekin zifratuta daude, beraz gako hori nork duen, horren araberakoa da nork irakur ditzakeen:

- **Public** companion guztietan dago konfiguratuta. Haren gakoa argitaratuta dago, beraz edonork irakur dezake.
- **Traolen kanalek**, `#utrecht` adibidez, izenetik hartzen dute gakoa. Izena dakien edonor sar daiteke, beraz hartu horiek ere publikotzat.
- **Kanal pribatuek** ausazko gako bat erabiltzen dute, eta zuk zeuk partekatzen duzu, adibidez QR kode gisa.

Iragarkiak sinatuta daude, baina ez zifratuta. Irismen barruan dagoen edonork ikus ditzake zure nodoaren izena eta, partekatzen baduzu, haren kokapena. Aukeratu nahi duzuna baino gehiago esaten ez duen izen bat.

## 868 MHz-eko banda Europan {#band}

Europan, MeshCore-k 868 MHz-eko bandaren zati txiki bat erabiltzen du, edonork lizentziarik gabe erabil dezakeena. Haren Europako irrati-aurrezarpena, EU/UK (Narrow), 869.618 MHz-etan dago, 62.5 kHz-eko kanal batean. Hori 869.40-869.65 MHz azpibandaren barruan dago, eta azpibanda horrek gehienez 500 mW e.r.p. onartzen ditu. Gailu batek denboraren % 10ean igor dezake gehienez han. [Errepikagailuen gidako lege-atalean](/repeater-guide/#legal) dituzu xehetasunak eta herrialde bakoitzeko mugak.

Eremu bateko guztiek aurrezarpen bera erabiltzen dute, bestela irratiek ezin dute elkar entzun. Herrialde eta eskualde batzuek aldaera bat erabiltzen dute: zure [tokiko taldeak](/community/) badaki zein.

## Zertarako erabiltzen duen jendeak {#uses}

- Harremanetan jarraitzea mendi-ibilaldietan, itsasoan eta jaialdietan, sare mugikorra
  gainezka dagoenean edo sarerik ez dagoenean.
- Ordezko kanal bat familiarentzat edo auzokoentzat, argindarrak edo sare mugikorrek
  huts egiten dutenean.
- Ordezko bitarteko bat tokiko agintarientzat, ohiko sareek huts egiten dutenean.
- Tokiko txata, jendeak berak dituen irratietan.
- Bilaketa eta erreskate talde bat harremanetan mantentzea, sare mugikorrik ez dagoen tokian.
  [Proiektuak](/projects/) orrian dagoen MeshCore SAR komunitate-aplikazioak mapak eta
  partekatutako kokapenak gehitzen ditu.
- Urruneko leku bat etxetik kontrolatzea. Errepikagailuek eta sentsore-nodoek beren
  bateriaren tentsioa eta beste neurketa batzuk bidaltzen dituzte, zuk eskatzen diezunean.
- Sentsore bat zaintzea. Sentsore-nodo batek neurketetarako MeshCore firmwarea darabil.
  Bere bateriaren tentsioaren historia gordetzen du. Hasi saioa admin gisa, eta
  bateria gutxi dagoenean abisatuko dizu. Beste neurketetarako abisuak zeure kodearekin
  gehitzen dituzu.
- Urrun dagoen zerbait piztea edo itzaltzea, ponpa bat adibidez. Hori sentsore-firmwarean
  gehitzen duzu, zeure kodearekin.
- Irratiarekin, antenekin, eguzki-energiarekin eta kode irekiko softwarearekin esperimentatzea.

Agintari batzuk MeshCore-n oinarritutako ordezko sistema bat eraikitzen edo probatzen ari dira. Adibide hauek 2026ko azaroan egiaztatu ditugu.

- Zikloi Gabrielek komunikazio guztiak eten zituen Tairāwhitin, Zeelanda Berrian.
  2025eko irailean, eskualdeko larrialdi-kudeaketak MeshCore sartu zuen
  [komunikatzeko gutxienez 6 ordezko moduen artean](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Eguzki-energiako errepikagailuak ere eraikitzen ari zen, sarearen bizkarrezur izateko.
- Alemaniako Bad Kissingen barrutia
  [MeshCore-n oinarritutako testu-sare bat eraikitzen ari da](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  agintarientzat, larrialdi-zerbitzuentzat eta gune kritikoentzat. Suhiltzaile-etxeak
  dira lehenak konektatzen.
- Herbehereetako Hilversumgo udalbatzak
  [proba bat onartu zuen, 34 aldeko eta 1 kontrako botorekin](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien).
  Proban errepikagailu bat dago udaletxeko dorrean. Udalak
  [2027ko udazkenean ebaluatuko du](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Herbehereetako bi segurtasun-eskualde MeshCore-rekin esperimentatzen ari dira.
  Segurtasun-eskualdeek krisi baten aurrean erantzuna antolatzen dute. Hauek dira:
  [Hego Limburg](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  eta [Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Drenthek dio goizegi dela esateko nola edo noiz erabil lezakeen.
- Dalfsenen, hau ere Herbehereetan, boluntarioak
  [proiektu pilotu bat egiten ari dira udalekin batera](https://noodnetoverijssel.nl/).
  Ahots-irratia erabiltzen dute lehenik, eta MeshCore testurako bigarren geruza gisa.

Zure inguruko mesh sareak larrialdi batean funtzionatzen duen, inork ez daki.

## Nondik datozen datuak {#data}

[Tokiko taldeen](/community/) orriko bilatzaileak toki bat aurkitzen du [GeoNames](https://www.geonames.org/) zerbitzuaren toki- eta posta-kode zerrenda libreen kopia batekin. Zerrenda horiek [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) lizentzia dute. Kopia webgune honetan dago. Zure bilaketa ez da inoiz zure gailutik ateratzen, eta ez da eskaerarik bidaltzen GeoNames-era.
