---
title: Kas ir MeshCore?
lead: MeshCore pa radio sūta īsziņas no mezgla uz mezglu. Tam nav vajadzīgs ne internets, ne abonements.
description: 'Kas MeshCore ir un kas tas nav: mezglu veidi, maršrutēšana, šifrēšana un 868 MHz josla.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '2a40da22'
  seeded: '2026-11-04'
  fields: {title: '06eda66b', lead: 'c0174569', description: 'c2255f49', eyebrow: '8610c822'}
  sections: ['aa768ac3', '92fc3ea7', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '203a07ef', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'ac039316', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '5d796ffb', '1a490368', 'f0dd237f', '3182d5c8', '02f1fe2f', 'e6b5b258']
---

MeshCore ir bezmaksas programmatūra mazām LoRa radioierīcēm. LoRa ir radio tehnika, kas ar ļoti mazu jaudu aizsūta nelielu datu apjomu tālu. Radioierīci ar MeshCore sauc par *mezglu*. Tu to savieno ar lietotni telefonā vai klēpjdatorā vai izmanto paša mezgla ekrānu un tastatūru. Tā tu sūti tekstu cilvēkiem, kas ir kilometriem tālu. Pa vidu nav ne torņa, ne maršrutētāja, ne pakalpojumu sniedzēja.

Programmatūra ir atvērtā koda, un to izstrādā repozitorijā [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) ar MIT licenci.

## Kas MeshCore nav {#not}

Radio tev ir kaut kas jauns? Šīs ir lietas, ko cilvēki no MeshCore gaida visbiežāk, bet ko tas nedara.

- **Tas nav internets vai telefons.** MeshCore sūta īsas teksta ziņas,
  apmēram tik garas kā īsziņa tavā telefonā. Nav balss, foto, video
  vai tīmekļa vietņu, un parastu telefona numuru tu nesasniegsi.
- **Tas nav ārkārtas dienests.** Neviens ārkārtas dienests nesola
  klausīties mesh tīklā, un neviens nesola, ka kāds tavu ziņu izlasīs.
- **Tas nav acumirklīgs un nav visur.** Ziņa lēc no radio uz radio
  un var ceļot dažas sekundes vai nepienākt nemaz. Vai tā nonāk galā, ir
  atkarīgs no retranslatoriem tev apkārt, no augstuma, ēkām un tavas antenas.
  Mazs radio iekštelpās bieži nesasniedz nevienu. Retranslators uz jumta
  sasniedz kilometrus.
- **Tas nav pakalpojums, ko kāds uztur tev.** Nav pakalpojumu
  sniedzēja, nav atbalsta dienesta un nav pārklājuma solījuma. Mesh tīkls ir
  tur, kur kopienas cilvēki ir uzstādījuši retranslatorus.
- **Ne viss tajā ir privāts.** Tiešās ziņas ir šifrētas, bet Public un
  hashtag kanālus var lasīt jebkurš. Tava mezgla nosaukumu un kopīgoto
  atrašanās vietu redz visi uztveršanas zonā.
  [Novērotāji](/network/) nodod publiskām kartēm to, ko dzird.
  [Šifrēšanas sadaļa](#encryption) skaidro, kas paliek privāts.
- **Tas nav neierobežots.** Visi apgabalā lieto vienu kopīgu radio kanālu, un
  [868 MHz joslas](#band) noteikumi ierobežo, cik ilgi katrs radio drīkst sūtīt.
  Katra ziņa atņem ētera laiku visiem citiem. Tāpēc boti, bieži adverti
  un testa ziņas palēnina mesh tīklu visiem.
- **Tas nav Meshtastic.** Meshtastic ir cita sistēma, kas darbojas uz
  gandrīz tām pašām platēm. Abas sistēmas nevar sazināties savā starpā.

## Mesh tīkls vienā minūtē {#mesh}

Viena LoRa radioierīce pilsētā aizsniedz dažus kilometrus, bet no pakalna vai jumta daudz tālāk. Lai aizsniegtu vēl tālāk, radioierīces nodod ziņas cita citai: to sauc par *mesh* tīklu. MeshCore tīklā ziņas tālāk nodod radioierīces, ko sauc par *retranslatoriem*. Retranslators sadzirdēto ziņu raida vēlreiz, tāpēc tā var šķērsot veselu reģionu.

Mesh tīkls nepieder nevienam. Katrs mezgls un katrs retranslators pieder kādam kopienas dalībniekam. Mesh tīkls sniedzas tik tālu, cik tālu sniedzas viņu retranslatori.

## 3 mezglu veidi {#roles}

Mezgla veidu tu izvēlies, kad ieraksti tajā programmaparatūru. Tavs pirmais mezgls ir companion.

**Companion.** Tava personīgā radioierīce. Tu to savieno ar MeshCore lietotni telefonā vai klēpjdatorā pa Bluetooth vai USB. Dažām ierīcēm ir savs ekrāns un tastatūra. Lietotnē tu lasi un raksti. Companion mezgls glabā tavus kontaktus un kanālus, kā arī ziņas, kas pienāca, kamēr lietotne nebija savienota. Companion mezgls citu ziņas tālāk nenodod.

**Retranslators.** Augstu novietota radioierīce, kas tālāk nodod visu ziņas. Lielākā daļa retranslatoru darbojas ar saules enerģiju. Savs retranslators tev vajadzīgs tikai tur, kur mesh tīkls vēl nesniedzas. Tam nav savas lietotnes. Tu to iestati pa USB vai piesakies ar paroli un pārvaldi to pa radio. Kā to izdarīt, rāda [retranslatoru ceļvedis](/repeater-guide/).

**Istabas serveris (room server).** Neliels ziņojumu dēlis mesh tīklā. Kad piesakies, tu saņem ierakstus, ko palaidi garām, kamēr biji ārpus darbības rādiusa, ne vairāk kā pēdējos 32. Serveris tos glabā tikai atmiņā, tāpēc restartēšana vai elektrības pārrāvums tos izdzēš. Vietējā grupa istabas serveri izmanto paziņojumiem.

## Kā ziņa atrod ceļu {#routing}

Katram mezglam ir slepenā atslēga un publiskā atslēga. Publiskā atslēga ir mezgla identitāte. Mezgls par sevi paziņo ar *advert*: tā ir parakstīta pakete ar mezgla nosaukumu un, ja vēlies, atrašanās vietu. Kāds parādās tavos kontaktos, kad tevi sasniedz viņa advert vai kad tu noskenē viņa QR kodu. Lietotnē ir poga, ar kuru vari nosūtīt savu advert.

Tava pirmā ziņa kontaktam aiziet kā *flood*. Katrs retranslators, kas to dzird, nodod to tālāk vienu reizi un pa ceļam pievieno savu īso ID. Atbilde šo ID sarakstu atnes atpakaļ. Pēc tam tavas ziņas šim kontaktam iet pa saglabāto maršrutu, un raida tikai šī maršruta retranslatori. Kad maršruts pārtrūkst, lietotne atkal izmanto flood.

Kanāla ziņām nav vienas adreses, tāpēc tās vienmēr iet kā flood. Retranslatori atceras, ko nesen nodevuši tālāk, un atmet kopijas, kas vēlreiz pienāk pa citu maršrutu. Ziņa var šķērsot līdz 64 retranslatoriem vai līdz 32, ja iestatījumu komplekts izmanto 2 baitu ID.

## Šifrēšana un privātums {#encryption}

Tavas tiešās ziņas ir šifrētas no gala līdz galam: tās var izlasīt tikai tu un otrs cilvēks. Par to, kam pakete paredzēta, retranslators redz tikai 1 baita norādi.

Kanāli ir šifrēti ar kopīgu atslēgu, tāpēc lasīt tos var tie, kam šī atslēga ir:

- **Public** ir iestatīts katrā companion mezglā. Tā atslēga ir publicēta, tāpēc to var lasīt jebkurš.
- **Tēmturu kanāli**, piemēram, `#utrecht`, atslēgu iegūst no sava nosaukuma. Pievienoties var jebkurš, kas zina nosaukumu, tāpēc arī tos uzskati par publiskiem.
- **Privātie kanāli** izmanto nejaušu atslēgu, ko kopīgo tu, piemēram, kā QR kodu.

Adverti ir parakstīti, bet nav šifrēti. Tava mezgla nosaukumu un atrašanās vietu, ja to kopīgo, redz visi, kas ir darbības rādiusā. Izvēlies nosaukumu, kas neatklāj vairāk, nekā vēlies.

## 868 MHz josla Eiropā {#band}

Eiropā MeshCore izmanto nelielu 868 MHz joslas daļu, ko jebkurš drīkst lietot bez licences. Eiropas radio iestatījumu komplekts EU/UK (Narrow) darbojas uz 869.618 MHz ar 62.5 kHz kanālu. Tas ietilpst 869.40-869.65 MHz apakšjoslā, kur atļauts līdz 500 mW e.r.p. Ierīce tur drīkst raidīt ne vairāk kā 10% laika. Sīkāka informācija un ierobežojumi pa valstīm ir [retranslatoru ceļveža juridiskajā sadaļā](/repeater-guide/#legal).

Visi vienā apvidū izmanto vienu un to pašu iestatījumu komplektu, citādi viņu radioierīces cita citu nedzird. Dažas valstis un reģioni izmanto citu variantu: kuru tieši, zina tava [vietējā grupa](/community/).

## Kam cilvēki to izmanto {#uses}

- Lai sazinātos pārgājienos, jūrā un festivālos, kur mobilais tīkls ir
  pārslogots vai tā nav nemaz.
- Rezerves kanāls ģimenei vai kaimiņiem, kad pazūd elektrība vai mobilie
  tīkli.
- Rezerve vietējām iestādēm, kad to ierastie tīkli nedarbojas.
- Vietēja sarakste pa radioierīcēm, kas pieder pašiem cilvēkiem.
- Lai meklēšanas un glābšanas komanda uzturētu saziņu, kur nav mobilā tīkla.
  MeshCore SAR, kopienas lietotne lapā [Projekti](/projects/), pievieno
  kartes un kopīgotas atrašanās vietas.
- Lai no mājām pārbaudītu attālu vietu. Retranslatori un sensoru mezgli
  pēc tava pieprasījuma ziņo akumulatora spriegumu un citus rādījumus.
- Lai uzraudzītu sensoru. Sensora mezglā darbojas MeshCore programmaparatūra,
  kas paredzēta mērījumiem. Tas glabā sava akumulatora sprieguma vēsturi.
  Piesakies kā administrators, un tas tevi brīdinās, kad akumulators būs
  gandrīz izlādējies. Brīdinājumus par citiem rādījumiem tu pievieno ar savu
  kodu.
- Lai pārslēgtu kaut ko tālumā, piemēram, sūkni. Šo funkciju tu pievieno
  sensora programmaparatūrai ar savu kodu.
- Lai eksperimentētu ar radio, antenām, saules enerģiju un atvērtā koda
  programmatūru.

Dažas iestādes veido vai testē rezerves sakarus uz MeshCore bāzes. Šos piemērus mēs pārbaudījām 2026. gada novembrī.

- Ciklons Gabriela pārrāva visus sakarus Tairāvhiti reģionā Jaunzēlandē. 2025. gada
  septembrī reģiona ārkārtas situāciju pārvaldība nosauca MeshCore par
  [vienu no vismaz 6 rezerves saziņas veidiem](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Tīkla mugurkaulam tā arī būvēja retranslatorus ar saules barošanu.
- Vācijas Bādkisingenes apriņķis
  [būvē MeshCore teksta tīklu](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  iestādēm, glābšanas dienestiem un kritiski svarīgiem objektiem. Pirmie
  pieslēdzas ugunsdzēsēju depo.
- Hilversumas pilsētas dome Nīderlandē
  [ar 34 balsīm pret 1 nobalsoja par izmēģinājumu](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  ar retranslatoru rātsnama tornī. Pašvaldība
  [to izvērtēs 2027. gada rudenī](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Ar MeshCore eksperimentē divi Nīderlandes drošības reģioni, kas organizē reaģēšanu uz krīzēm:
  [Dienvidlimburga](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  un [Drente](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Drente uzskata, ka vēl ir par agru teikt, kā vai kad tā to varētu izmantot.
- Dalfsenā, arī Nīderlandē, brīvprātīgie
  [kopā ar pašvaldībām īsteno izmēģinājumu](https://noodnetoverijssel.nl/).
  Viņi vispirms izmanto balss radio, bet MeshCore ir otrais slānis teksta ziņām.

Neviens nesola, ka tavu ziņu mesh tīklā tavā tuvumā kāds izlasīs.

## No kurienes nāk dati {#data}

Meklēšana lapā [vietējās grupas](/community/) atrod vietu, izmantojot [GeoNames](https://www.geonames.org/) bezmaksas vietu un pasta indeksu sarakstu kopiju ar licenci [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopija atrodas šajā vietnē. Tavs meklējums nekad neiziet ārpus tavas ierīces, un GeoNames nesaņem nevienu pieprasījumu.
