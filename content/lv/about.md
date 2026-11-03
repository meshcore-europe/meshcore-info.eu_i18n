---
title: Kas ir MeshCore?
lead: MeshCore pa radio sūta īsziņas no mezgla uz mezglu. Tam nav vajadzīgs ne internets, ne abonements.
description: 'Kas MeshCore ir un kas tas nav: mezglu veidi, maršrutēšana, atšķirības no Meshtastic, šifrēšana un 868 MHz josla.'
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

MeshCore ir bezmaksas programmatūra mazām LoRa radioierīcēm. LoRa ir radio tehnika, kas ar ļoti mazu jaudu aizsūta nelielu datu apjomu tālu. Radioierīci ar MeshCore sauc par *mezglu*. Tu to savieno ar lietotni telefonā vai klēpjdatorā vai izmanto paša mezgla ekrānu un tastatūru. Tā tu sūti tekstu cilvēkiem, kas ir kilometriem tālu. Pa vidu nav ne torņa, ne maršrutētāja, ne pakalpojumu sniedzēja.

Programmatūra ir atvērtā koda, un to izstrādā repozitorijā [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) ar MIT licenci.

## Kas MeshCore nav {#not}

Radio tev ir kaut kas jauns? Šīs ir lietas, ko cilvēki no MeshCore gaida visbiežāk, bet ko tas nedara.

- **Tas nav ne internets, ne telefons.** MeshCore sūta īsas teksta ziņas,
  apmēram tik garas kā īsziņa tavā telefonā. Nav ne balss, ne fotoattēlu, ne video,
  ne tīmekļa vietņu, un parastu tālruņa numuru tu sasniegt nevari.
- **Tas nav operatīvais dienests.** Neviens operatīvais dienests tīklā neklausās,
  un neviens nesola, ka kāds tavu ziņu izlasīs. Ārkārtas situācijā zvani 112.
- **Tas nedarbojas uzreiz un ne visur.** Ziņa pārlec no radioierīces uz
  radioierīci un var ceļot dažas sekundes vai nepienākt nemaz.
  Vai ziņa nonāks galā, ir atkarīgs no retranslatoriem tev apkārt, no augstuma,
  ēkām un tavas antenas. Maza radioierīce telpās bieži nesasniedz nevienu;
  retranslators uz jumta sniedzas kilometriem tālu.
- **Tas nav pakalpojums, ko kāds tev uztur.** Nav ne pakalpojumu sniedzēja,
  ne atbalsta dienesta, ne pārklājuma solījuma. Tīkls pastāv tur, kur
  kopienas cilvēki ir uzstādījuši retranslatorus, un nekur citur.
- **Ne viss tīklā ir privāts.** Tiešās ziņas ir šifrētas, bet Public un
  mirkļbirku kanālus var lasīt jebkurš, un tava mezgla nosaukumu un kopīgoto
  atrašanās vietu redz visi, kas ir darbības zonā.
  [Novērotāji](/network/) dzirdēto nodod publiskajām kartēm.
  [Šifrēšanas sadaļā](#encryption) ir paskaidrots, kas paliek privāts.
- **Tas nav neierobežots.** Visi vienā apvidū izmanto vienu radiokanālu, un
  [868 MHz joslas](#band) noteikumi ierobežo, cik ilgi katra radioierīce drīkst raidīt.
  Katra ziņa atņem ētera laiku visiem pārējiem, tāpēc boti, biežas advert
  pārraides un testa ziņas palēnina tīklu visiem.
- **Tas nav Meshtastic.** Meshtastic ir cita sistēma, kas darbojas uz gandrīz
  tām pašām platēm. Abas sistēmas savā starpā sazināties nevar.
  Sadaļā [Pāreja no Meshtastic](#meshtastic) ir uzskaitīts, kas darbojas citādi.

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

## Pāreja no Meshtastic {#meshtastic}

Daudzās platēs var darboties vai nu MeshCore, vai Meshtastic, un tu ieraksti to, kuru vēlies. Vispirms tu pamanīsi šīs atšķirības. Tās atbilst MeshCore v1.18.0 un Meshtastic 2026. gada novembra dokumentācijai.

- **Kas nodod ziņas tālāk.** MeshCore tīklā to dara tikai retranslatori;
  tavs companion mezgls to nedara nekad. Meshtastic tīklā ziņas tālāk nodod arī
  noklusējuma client loma, ja vien cits mezgls to jau nav izdarījis.
- **Cik tālu ziņa nonāk.** MeshCore ziņa var iziet cauri līdz 64
  retranslatoriem. Meshtastic ziņa pēc noklusējuma apstājas pēc 3 lēcieniem, un maksimums ir 7.
- **Citu mezglu rādījumi.** MeshCore retranslatori un sensoru mezgli sūta
  rādījumus, piemēram, akumulatora spriegumu, kad tu tos pieprasi. Visam mesh
  tīklam tie šos rādījumus nesūta.
- **Internets.** MeshCore programmaparatūrā nav iespējas savienot mesh tīklus pa
  internetu. [Novērotāji](/network/) dzirdēto nodod kartēm, tikai vienā
  virzienā. Meshtastic ir iebūvēts MQTT modulis,
  kas var pārsūtīt ziņas starp mesh tīkliem pa internetu.

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

- Saziņa pārgājienos, jūrā un festivālos, kur mobilais tīkls
  ir pārslogots vai nav pieejams.
- Rezerves kanāls ģimenei vai kaimiņiem, kad pazūd elektrība vai mobilie tīkli.
- Vietējā sarakste pa radioierīcēm, kas cilvēkiem pieder pašiem.
- Attālas vietas pārbaudīšana no mājām. Retranslatori un sensoru mezgli pēc tava
  pieprasījuma ziņo akumulatora spriegumu un citus rādījumus.
- Sensora novērošana. Sensora mezglā darbojas MeshCore mērījumu programmaparatūra.
  Tas glabā rādījumu vēsturi. Ja tu to abonē, tas tevi brīdina,
  piemēram, kad tā akumulators ir gandrīz izlādējies.
- Kādas tālas ierīces, piemēram, sūkņa, pārslēgšana. Šo iespēju tu pievieno sensora
  programmaparatūrai ar savu kodu.
- Eksperimenti ar radio, antenām, saules enerģiju un atvērtā koda programmatūru.

## No kurienes nāk dati {#data}

Meklēšana lapā [vietējās grupas](/community/) atrod vietu, izmantojot [GeoNames](https://www.geonames.org/) bezmaksas vietu un pasta indeksu sarakstu kopiju ar licenci [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopija atrodas šajā vietnē. Tavs meklējums nekad neiziet ārpus tavas ierīces, un GeoNames nesaņem nevienu pieprasījumu.
