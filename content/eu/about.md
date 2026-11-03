---
title: Zer da MeshCore?
lead: MeshCore-k testu-mezuak irratiz bidaltzen ditu, nodotik nodora. Ez du internetik edo harpidetzarik behar.
description: 'MeshCore zer den eta zer ez den: nodo motak, bideratzea, Meshtastic-etik zertan bereizten den, enkriptatzea eta 868 MHz-eko banda.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '279b56a4'
  seeded: '2026-11-03'
  fields: {title: '06eda66b', lead: 'c0174569', description: '15e6d2a7', eyebrow: '8610c822'}
  sections: ['aa768ac3', '16fde264', '0a55792c', 'c3de803d', '493b444f', 'a8b2b9b4', '429f699c', 'f8008f48', '88af2bd3', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'fab378a5', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', 'fc8f3129', '8dec428a', '07cbac35', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '95e18f18', '02f1fe2f', 'e6b5b258']
---

MeshCore LoRa irrati txikietarako software librea da. LoRa irrati-teknika bat da: datu gutxi urrutira bidaltzen ditu, oso energia gutxirekin. MeshCore duen irrati bati *nodo* esaten zaio. Zure telefonoko edo eramangarriko aplikazioarekin parekatuta, edo bere pantaila eta teklatuarekin, testua bidaltzen die kilometroetara dagoen jendeari. Tartean ez dago dorrerik, bideratzailerik edo hornitzailerik.

Softwarea kode irekikoa da. [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) proiektuan garatzen dute, MIT lizentziapean.

## Zer ez den MeshCore {#not}

Irratien munduan berria zara? Hauek dira jendeak MeshCore-ri gehien eskatzen dizkion gauzak, eta MeshCore-k egiten ez dituenak.

- **Ez da internet, ezta telefonoa ere.** MeshCore-k testu-mezu laburrak bidaltzen ditu,
  gutxi gorabehera zure telefonoko testu-mezu baten luzerakoak. Ez dago ahotsik, argazkirik, bideorik
  edo webgunerik, eta ezin duzu telefono-zenbaki arruntekin harremanetan jarri.
- **Ez da larrialdi-zerbitzu bat.** Ez dago mesh sarea entzuten duen larrialdi-zerbitzurik,
  eta inork ez du bermatzen norbaitek zure mezua irakurriko duenik. Larrialdi
  batean, deitu 112ra.
- **Ez da berehalakoa, eta ez dago leku guztietan.** Mezua irratiz irrati doa jauzika.
  Segundo batzuk behar ditzake, edo agian ez da iritsiko. Iritsiko den ala ez zure inguruko errepikagailuen,
  altueraren, eraikinen eta zure antenaren araberakoa da. Eraikin barruan, irrati txiki bat askotan
  ez da inorengana iristen; teilatuko errepikagailu bat kilometroetara iristen da.
- **Ez da norbaitek zuretzat kudeatzen duen zerbitzu bat.** Ez dago hornitzailerik,
  laguntza-zerbitzurik, ezta estaldura-bermerik ere. Mesh sarea komunitateko jendeak errepikagailuak
  jarri dituen lekuetan dago, eta ez beste inon.
- **Ez da dena pribatua.** Mezu zuzenak zifratuta daude, baina
  edonork irakur ditzake Public eta hashtag kanalak. Irismen barruko guztiek ikusten dituzte
  zure nodoaren izena eta partekatutako kokapena.
  [Behatzaileek](/network/) entzuten dutenaren berri ematen dute mapa publikoetan.
  [Zifratzeari buruzko atalak](#encryption) azaltzen du zer geratzen den pribatu.
- **Ez da mugagabea.** Eremu bateko guztiek irrati-kanal bakarra partekatzen dute, eta
  [868 MHz-eko bandaren](#band) arauek mugatzen dute irrati bakoitzak zenbat denbora igor dezakeen.
  Mezu bakoitzak aire-denbora kentzen die beste guztiei. Horregatik, botek, maiz bidalitako iragarkiek
  eta proba-mezuek mesh sarea moteltzen dute guztientzat.
- **Ez da Meshtastic.** Meshtastic beste sistema bat da, eta plaka ia berberetan dabil.
  Bi sistemek ezin dute elkarrekin hitz egin.
  [Meshtastic-etik zatoz](#meshtastic) atalak zerrendatzen du zer dabilen desberdin.

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

## Meshtastic-etik bazatoz {#meshtastic}

Plaka askok MeshCore edo Meshtastic exekuta dezakete, eta nahi duzuna grabatzen duzu. Hauek dira lehenik nabarituko dituzun desberdintasunak. MeshCore v1.18.0 eta Meshtastic-en 2026ko azaroko dokumentazioari jarraitzen diete.

- **Nork birbidaltzen dituen mezuak.** MeshCore-n errepikagailuek bakarrik birbidaltzen dituzte; zure companionak inoiz ez.
  Meshtastic-en, client rol lehenetsiak ere birbidaltzen ditu mezuak,
  beste nodo batek lehendik birbidali ez baditu.
- **Zein urrun iristen den mezu bat.** MeshCore-n mezu batek gehienez 64
  errepikagailu zeharka ditzake. Meshtastic-en mezua 3 jauziren ondoren gelditzen da lehenespenez, eta gehienez 7ren ondoren.
- **Beste nodoen neurketak.** MeshCore-n errepikagailuek eta sentsore-nodoek
  neurketak bidaltzen dituzte, adibidez bateriaren tentsioa, zuk eskatzen dizkiezunean. Ez dizkiote
  mesh sare osoari bidaltzen.
- **Internet.** MeshCore firmwareak ez du internet bidezko loturarik mesh sareen artean.
  [Behatzaileek](/network/) entzuten dutenaren berri ematen diete mapei, norabide bakarrean.
  Meshtastic-ek MQTT modulu integratu bat du,
  eta modulu horrek mezuak internet bidez eraman ditzake mesh sareen artean.

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

- Harremanetan egotea mendi-ibilaldietan, itsasoan eta sare mugikorra gainezka dagoen
  edo falta den jaialdietan.
- Ordezko kanal bat familiarentzat edo auzokoentzat, argindarra edo sare mugikorrak
  erortzen direnean.
- Tokiko berriketa, jendeak berak dituen irratietan.
- Urruneko leku bat etxetik kontrolatzea. Errepikagailuek eta sentsore-nodoek bateriaren
  tentsioa eta beste neurketa batzuk bidaltzen dizkizute, eskatzen dituzunean.
- Sentsore bat zaintzea. Sentsore-nodo batek MeshCore-ren neurketetarako firmwarea darabil.
  Neurketen historia gordetzen du. Harpidetzen bazara, abisua bidaltzen dizu,
  adibidez bateria agortzen ari zaionean.
- Urrun dagoen zerbait piztea edo itzaltzea, ponpa bat adibidez. Hori zeure kodearekin
  gehitzen diozu sentsore-firmwareari.
- Esperimentuak egitea irratiarekin, antenekin, eguzki-energiarekin eta kode irekiko softwarearekin.

## Nondik datozen datuak {#data}

[Tokiko taldeen](/community/) orriko bilatzaileak toki bat aurkitzen du [GeoNames](https://www.geonames.org/) zerbitzuaren toki- eta posta-kode zerrenda libreen kopia batekin. Zerrenda horiek [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) lizentzia dute. Kopia webgune honetan dago. Zure bilaketa ez da inoiz zure gailutik ateratzen, eta ez da eskaerarik bidaltzen GeoNames-era.
