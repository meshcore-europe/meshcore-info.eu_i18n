---
title: Kas ir MeshCore?
lead: MeshCore pa radio sūta īsziņas no mezgla uz mezglu. Tam nav vajadzīgs ne internets, ne abonements.
description: 'Kas MeshCore ir un kas tas nav: mesh tīkls, companion mezgli, retranslatori un istabu serveri, maršrutēšana, šifrēšana un 868 MHz josla Eiropā.'
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

MeshCore ir bezmaksas programmatūra mazām LoRa radioierīcēm. LoRa ir radio tehnika, kas ar ļoti mazu jaudu aizsūta nelielu datu apjomu tālu. Radioierīci ar MeshCore sauc par *mezglu*. Tu to savieno ar lietotni telefonā vai klēpjdatorā vai izmanto paša mezgla ekrānu un tastatūru. Tā tu sūti tekstu cilvēkiem, kas ir kilometriem tālu. Pa vidu nav ne torņa, ne maršrutētāja, ne pakalpojumu sniedzēja.

Programmatūra ir atvērtā koda, un to izstrādā repozitorijā [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) ar MIT licenci.

## Kas MeshCore nav {#not}

Radio tev ir kaut kas jauns? Šīs ir lietas, ko cilvēki no MeshCore gaida visbiežāk, bet ko tas nedara.

- **Tas nav ne internets, ne telefons.** MeshCore sūta īsus tekstus, aptuveni telefona īsziņas garumā. Nav ne balss, ne fotoattēlu, ne video, ne tīmekļa vietņu, un ar parastu tālruņa numuru tu sazināties nevari.
- **Tas nav operatīvais dienests.** Neviens operatīvais dienests mesh tīklu neklausās, un neviens nesola, ka kāds tavu ziņu izlasīs. Ārkārtas situācijā zvani 112.
- **Tas nedarbojas acumirklī un ne visur.** Ziņa lec no radioierīces uz radioierīci un ceļā var pavadīt dažas sekundes vai nepienākt vispār. Vai tā nonāks galā, atkarīgs no tuvumā esošajiem retranslatoriem, augstuma, ēkām un tavas antenas. Maza radioierīce telpās bieži nesasniedz nevienu, bet retranslators uz jumta sniedzas kilometriem tālu.
- **Tas nav pakalpojums, ko kāds tev nodrošina.** Nav ne pakalpojumu sniedzēja, ne palīdzības dienesta, ne pārklājuma solījuma. Mesh tīkls pastāv tur, kur kopienas dalībnieki ir uzstādījuši retranslatorus, un nekur citur.
- **Ne viss tajā ir privāts.** Tiešās ziņas ir šifrētas, bet kanālu Public un tēmturu kanālus var lasīt jebkurš. Tava mezgla nosaukumu un kopīgoto atrašanās vietu redz visi, kas ir darbības rādiusā. [Novērotāji](/network/) dzirdēto nodod publiskām kartēm. Sadaļā par [šifrēšanu](#encryption) vari izlasīt, kas paliek privāts.
- **Tas nav neierobežots.** Visi vienā apvidū izmanto vienu kopīgu radio kanālu, un [868 MHz joslas](#band) noteikumi ierobežo, cik ilgi katra radioierīce drīkst raidīt. Katra ziņa atņem ēterlaiku visiem pārējiem, tāpēc boti, bieži adverti un testa ziņas bremzē mesh tīklu visiem.
- **Tas nav Meshtastic.** Meshtastic ir cita sistēma, kas darbojas uz gandrīz tām pašām platēm. Abas sistēmas savā starpā sazināties nevar.

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

- Lai uzturētu sakarus pārgājienos, jūrā un festivālos, kur mobilais tīkls ir pārslogots vai tā nav.
- Kā rezerves kanālu ģimenei vai kaimiņiem, kad pazūd elektrība vai mobilie tīkli.
- Vietējām sarunām pa radioierīcēm, kas pieder pašiem cilvēkiem.
- Lai eksperimentētu ar radio, antenām, saules enerģiju un atvērtā koda programmatūru.

## No kurienes nāk dati {#data}

Meklēšana lapā [vietējās grupas](/community/) atrod vietu, izmantojot [GeoNames](https://www.geonames.org/) bezmaksas vietu un pasta indeksu sarakstu kopiju ar licenci [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopija atrodas šajā vietnē. Tavs meklējums nekad neiziet ārpus tavas ierīces, un GeoNames nesaņem nevienu pieprasījumu.
