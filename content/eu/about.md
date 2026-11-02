---
title: Zer da MeshCore?
lead: MeshCore-k testu-mezuak irratiz bidaltzen ditu, nodotik nodora. Ez du internetik edo harpidetzarik behar.
description: 'Zer den MeshCore eta zer ez den: mesh sarea, companionak, errepikagailuak eta gela-zerbitzariak, bideratzea, zifratzea eta Europako 868 MHz-eko banda.'
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

MeshCore LoRa irrati txikietarako software librea da. LoRa irrati-teknika bat da: datu gutxi urrutira bidaltzen ditu, oso energia gutxirekin. MeshCore duen irrati bati *nodo* esaten zaio. Zure telefonoko edo eramangarriko aplikazioarekin parekatuta, edo bere pantaila eta teklatuarekin, testua bidaltzen die kilometroetara dagoen jendeari. Tartean ez dago dorrerik, bideratzailerik edo hornitzailerik.

Softwarea kode irekikoa da. [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) proiektuan garatzen dute, MIT lizentziapean.

## Zer ez den MeshCore {#not}

Irratien munduan berria zara? Hauek dira jendeak MeshCore-ri gehien eskatzen dizkion gauzak, eta MeshCore-k egiten ez dituenak.

- **Ez da internet, ezta telefonoa ere.** MeshCore-k testu-mezu laburrak bidaltzen ditu, telefonoko SMS baten luzera gutxi gorabehera. Ezin duzu ahotsik, argazkirik, bideorik edo webgunerik erabili, eta ezin duzu ohiko telefono-zenbaki batera iritsi.
- **Ez da larrialdi-zerbitzu bat.** Ez dago mesh sarea entzuten duen larrialdi-zerbitzurik, eta inork ez du bermatzen norbaitek zure mezua irakurriko duenik. Larrialdi batean, deitu 112ra.
- **Ez da berehalakoa, eta ez dago edonon.** Mezuak irratiz irrati egiten du jauzi. Segundo batzuk har ditzake, edo ez iritsi ere egin. Mezua iristea inguruko errepikagailuen, altueraren, eraikinen eta zure antenaren araberakoa da. Etxe barruko irrati txiki bat askotan ez da inorengana iristen; teilatuko errepikagailu bat kilometroetara iristen da.
- **Ez da norbaitek zuretzat kudeatzen duen zerbitzu bat.** Ez dago hornitzailerik, laguntza-zerbitzurik edo estaldura-bermerik. Komunitateko jendeak errepikagailuak jarri dituen tokian dago mesh sarea, eta ez beste inon.
- **Dena ez da pribatua.** Mezu zuzenak zifratuta doaz, baina edonork irakur ditzake Public eta traolen kanalak. Irismen barruan dagoen edonork ikus ditzake zure nodoaren izena eta partekatutako kokapena. [Behatzaileek](/network/) entzuten dutena mapa publikoetara bidaltzen dute. [Zifratzeari buruzko atalean](#encryption) irakur dezakezu zer geratzen den pribatu.
- **Ez da mugagabea.** Eremu bateko guztiek irrati-kanal bakarra partekatzen dute, eta [868 MHz-eko bandaren](#band) arauek mugatzen dute irrati bakoitzak zenbat denbora igor dezakeen. Mezu bakoitzak gainerakoei kentzen die igorpen-denbora. Horregatik, botek, maiz bidalitako iragarkiek eta proba-mezuek guztientzat moteltzen dute mesh sarea.
- **Ez da Meshtastic.** Meshtastic beste sistema bat da, eta plaka ia berberetan dabil. Biek ezin dute elkarrekin hitz egin.

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

- Harremanetan jarraitzeko mendi-ibilaldietan, itsasoan eta sare mugikorra gainezka dagoen edo falta den jaialdietan.
- Familiarentzako edo auzokoentzako ordezko kanal gisa, argindarrak edo sare mugikorrek huts egiten dutenean.
- Tokian txateatzeko, jendeak berak dituen irratiekin.
- Irratiekin, antenekin, eguzki-energiarekin eta kode irekiko softwarearekin esperimentatzeko.

## Nondik datozen datuak {#data}

[Tokiko taldeen](/community/) orriko bilatzaileak toki bat aurkitzen du [GeoNames](https://www.geonames.org/) zerbitzuaren toki- eta posta-kode zerrenda libreen kopia batekin. Zerrenda horiek [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) lizentzia dute. Kopia webgune honetan dago. Zure bilaketa ez da inoiz zure gailutik ateratzen, eta ez da eskaerarik bidaltzen GeoNames-era.
