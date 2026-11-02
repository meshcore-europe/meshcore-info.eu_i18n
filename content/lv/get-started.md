---
title: Darba sākšana
lead: No jaunas plates līdz pirmajai ziņai tīklā. Tev vajag LoRa plati, datoru ar Chrome vai Edge un tālruni vai klēpjdatoru lietotnei.
description: Ieraksti MeshCore no pārlūka, savieno lietotni, izvēlies sava apgabala radio priekšiestatījumu, nosūti pirmo ziņu un pievienojies vietējam kanālam.
eyebrow: 6 soļi · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-11-02'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Šie soļi atbilst MeshCore programmaparatūrai v1.18.0 un 2026. gada oktobra oficiālajiem rīkiem. Izvēļņu nosaukumi lietotnē dažādās versijās var nedaudz atšķirties.

## 1. Izvēlies ierīci {#device}

Der jebkura plate no [ierīču lapas](/devices/), pie kuras norādīts companion.
Savam pirmajam mezglam izvēlies *companion*: radio, no kura sūti ziņas.
Savieno to ar tālruni vai klēpjdatoru pa Bluetooth vai USB. Vari arī izvēlēties
ierīci ar savu ekrānu un tastatūru, kas darbojas patstāvīgi.

Izvēlies 868 MHz versiju. Komplektā iekļautā antena ir pietiekama. Kā pārbaudīt
antenu, uzzināsi [antenu ceļvedī](/guides/antenna/).

{{< callout type="warning" >}}
Pievieno antenu, pirms ieslēdz radio. LoRa radio, kas raida bez antenas,
var sabojāt pats savu mikroshēmu.
{{< /callout >}}

## 2. Ieraksti programmaparatūru {#flash}

1. Pieslēdz ierīci datoram ar USB datu kabeli.
2. Pārlūkā Chrome vai Edge atver tīmekļa ierakstīšanas rīku
   [flasher.meshcore.io](https://flasher.meshcore.io). Rīks izmanto Web Serial, kura citos pārlūkos nav.
3. Izvēlies savu ierīci un pēc tam **Companion** programmaparatūru **Bluetooth** savienojumam (vai
   USB, ja lietosi ierīci tikai ar kabeli pie datora).
4. Ieraksti programmaparatūru. Dažas plates vispirms jāpārslēdz atjaunināšanas režīmā, un ierakstīšanas rīks
   parāda, kā to izdarīt.

Izmanto *erase* tikai tad, ja sāc no nulles: šī darbība izdzēš ierīces identitāti
un tavus kontaktus. Vēlāk, atjauninot, ieraksti programmaparatūru bez dzēšanas. Ja gribi saglabāt
identitāti arī pēc dzēšanas, vispirms eksportē sava companion privāto atslēgu no lietotnes
un pēc dzēšanas to importē.

## 3. Instalē lietotni {#app}

Oficiālā MeshCore lietotne ir pieejama Android, iOS, Windows un macOS sistēmām.
Saites uz visām versijām atradīsi vietnē [meshcore.io](https://meshcore.io). Ir arī
tīmekļa lietotne [app.meshcore.nz](https://app.meshcore.nz), kas darbojas datorā pārlūkā Chrome vai
Edge.

## 4. Savieno savu mezglu {#pair}

Ieslēdz mezglu, atver lietotni un savienojies ar mezglu pa Bluetooth. Kad
lietotne prasa PIN:

- mezgls **ar** ekrānu parāda PIN, ievadi to;
- mezgls **bez** ekrāna izmanto `123456`.

Ja savienošana neizdodas, noņem ierīci tālruņa Bluetooth iestatījumos un
mēģini vēlreiz. Pēc tam piešķir mezglam nosaukumu. Šo nosaukumu redz citi, tāpēc neizmanto
savu vārdu un uzvārdu vai adresi, ja vien pats to negribi.

## 5. Izvēlies sava apgabala radio priekšiestatījumu {#preset}

Visi radio vienā apgabalā izmanto vienu un to pašu frekvenci un iestatījumus, citādi tie viens otru
nedzird. Lietotnes radio iestatījumos izvēlies sava apgabala priekšiestatījumu.
Ārpus tālāk minētajiem apgabaliem Eiropā izmanto **EU/UK (Narrow)**. Nīderlandē,
Čehijā, Ungārijā, Slovākijā, Portugālē un Šveicē izmanto savus priekšiestatījumus, un
Nīderlandes Limburgai ir savs variants:

{{< presets >}}

Tava ierīce nepiedāvā sava apgabala priekšiestatījumu? Lietotnes radio iestatījumos
manuāli ievadi 4 vērtības no tabulas: frekvenci, joslas platumu, izkliedes
koeficientu un kodēšanas ātrumu. Mezgls ar citām vērtībām tīklu nedzird.

Šaubies? Tava [vietējā grupa](/community/) zina, kuru priekšiestatījumu izmanto tavā apgabalā.
Lietotne lejupielādē šo sarakstu no MeshCore projekta, tāpēc jaunam priekšiestatījumam
lietotnes atjauninājums nav vajadzīgs.

## 6. Sasveicinies {#hello}

1. **Paziņo par sevi.** Nosūti no lietotnes *advert*. "Flood" advert
   iet caur retranslatoriem (mezgliem, kas pārsūta ziņas tālāk), tāpēc ikviens
   tīklā var tevi pievienot.
   Companion ierīces nekad nepaziņo par sevi automātiski.
2. **Atrodi citus.** Cilvēki parādās tavos kontaktos, kad viņu advert tevi
   sasniedz. Retranslatori pēc noklusējuma sūta flood advert ik pēc 47 stundām, tāpēc saraksts
   var aizpildīties 2 dienas.
3. **Nosūti ziņu.** Atver kontaktu un raksti. Pirmā ziņa izplatās pa visu
   tīklu. Saņēmējs atsūta atpakaļ maršrutu, pa kuru tā atnāca, un nākamās
   ziņas iet pa šo maršrutu.
4. **Pievienojies kanāliem.** Kanāls **Public** jau ir iestatīts. Visu, ko tur raksti, saņem
   ikviens tīklā. Pievieno sava reģiona *hashtag kanālu* (kanālu, kura nosaukums sākas ar `#`),
   ierakstot tā nosaukumu. Tava
   [vietējā grupa](/community/) pateiks, kuri kanāli ir aktīvi.

## Ja kaut kas nedarbojas {#troubleshooting}

**Lietotne neatrod manu ierīci pa Bluetooth.**
Visticamāk, tu ierakstīji USB companion versiju. Ieraksti vēlreiz un izvēlies
Bluetooth versiju. Heltec V3 mazajai iebūvētajai Bluetooth antenai ir
neliels darbības rādiuss, tāpēc turi tālruni tuvu.

**Savienošana atkal un atkal neizdodas.**
Noņem ierīci tālruņa Bluetooth iestatījumos, restartē Bluetooth
un savieno vēlreiz ar PIN no ekrāna vai `123456`.

**Manos kontaktos neviens neparādās.**
Pārbaudi, vai tavs priekšiestatījums atbilst tavam apgabalam. Nosūti flood advert. Ja
sasniedzamā attālumā nav retranslatora, tu dzirdēsi tikai tuvumā esošus radio.
[Kartes lapā](/map/) vari redzēt, kur ir retranslatori.

**Kontaktam redzams "last seen" pirms vairākām dienām, lai gan viņš ir aktīvs.**
Vienam no abiem mezgliem ir nepareizs laiks. Companion ņem laiku no
tava tālruņa. Retranslatoriem un room server (mezgliem, kas glabā ziņas
grupai) laiku iestata to īpašnieks.

**Tiešā ziņa nekad nepienāk.**
Tev un otram cilvēkam jābūt vienam otra kontaktos. Mezgls izmet ziņu no nepazīstama sūtītāja
un par to sūtītājam nepaziņo. Nosūti flood advert un palūdz otram cilvēkam
nosūtīt arī savu. Lietotnē pārbaudi, vai tā automātiski pievieno jaunus
kontaktus. Tā pievieno tikai mezglus, kas nepārsniedz tās lēcienu ierobežojumu.

**Vecie kontakti darbojas, bet jaunie nekad nesavienojas.**
Pirmā ziņa izplatās pa visu tīklu, un retranslators to pārsūta tikai tad, ja tam ir
iestatīts ziņas reģions. Nākamās ziņas iet pa noskaidrotu maršrutu, un to neaptur reģiona
pārbaude. Pajautā savai [vietējai grupai](/community/), kādi reģioni iestatīti
retranslatoriem tavā apkārtnē, un pārbaudi [sava apgabala iestatījumus](/guides/settings/#traffic).

**Lietotne vairs nesavienojas ar tavu companion.**
Dažām platēm ir lietotāja poga, piemēram, dažām RAK platēm un Heltec T114.
Turi to nospiestu pirmajās 8 sekundēs pēc plates ieslēgšanās. Companion atver
glābšanas konsoli pa USB. Vietnes
[flasher.meshcore.io](https://flasher.meshcore.io) konsolē ar `set pin <pin>` iestati
jaunu Bluetooth PIN, bet ar `erase` izdzēs ierīces saturu.

**Ierakstīšanas rīks Linux sistēmā nevar atvērt seriālo portu.**
Tavam lietotājam vajadzīga piekļuve portam, piemēram, ar
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, vai dalība grupā `dialout`.

**Kaut kas cits.** Vēl daudzas problēmas apraksta
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md).
