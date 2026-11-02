---
title: Alustamine
lead: Uuest plaadist esimese sõnumini võrgus. Sul on vaja LoRa plaati, Chrome'i või Edge'iga arvutit ning rakenduse jaoks telefoni või sülearvutit.
description: Laadi MeshCore brauseris seadmesse, seo rakendus seadmega, vali oma piirkonna raadio eelseadistus, saada esimene sõnum ja liitu kohaliku kanaliga.
eyebrow: 6 sammu · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-11-02'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Need sammud põhinevad MeshCore'i püsivara versioonil v1.18.0 ja 2026. aasta oktoobri ametlikel tööriistadel. Rakenduse menüüde nimed võivad versiooniti veidi erineda.

## 1. Vali seade {#device}

Sobib iga plaat, mille juures [seadmete lehel](/devices/) on märgitud companion. Esimeseks sõlmeks vali *companion*: raadio, millelt sõnumeid saadad. Seo see Bluetoothi või USB kaudu oma telefoni või sülearvutiga. Teine võimalus on valida oma ekraani ja klaviatuuriga seade, mis töötab iseseisvalt.

Võta 868 MHz versioon. Kaasasolev antenn sobib. [Antennijuhendist](/guides/antenna/) näed, kuidas antenni kontrollida.

{{< callout type="warning" >}}
Ühenda antenn enne raadio sisselülitamist. LoRa-raadio võib ilma antennita saates oma kiipi kahjustada.
{{< /callout >}}

## 2. Laadi püsivara seadmesse {#flash}

1. Ühenda seade arvutiga USB-andmekaabliga.
2. Ava püsivara veebilaadija [flasher.meshcore.io](https://flasher.meshcore.io) Chrome'is või Edge'is. Laadija kasutab Web Serialit, mida teistel brauseritel pole.
3. Vali oma seade ja seejärel **Companion**-püsivara **Bluetoothi** jaoks (või USB jaoks, kui kasutad seadet ainult arvutiga kaabli kaudu).
4. Käivita laadimine. Mõni plaat tuleb esmalt viia uuendusrežiimi. Laadija ütleb, kuidas.

Kasuta valikut *erase* ainult siis, kui tahad alustada puhtalt lehelt: kustutamine eemaldab seadme identiteedi ja sinu kontaktid. Hiljem uuendades laadi püsivara ilma kustutamata. Kui tahad identiteedi alles hoida, ekspordi enne kustutamist rakendusest oma companioni privaatvõti ja impordi see pärast tagasi.

## 3. Paigalda rakendus {#app}

Ametlik MeshCore'i rakendus on saadaval Androidile, iOS-ile, Windowsile ja macOS-ile. Lingid kõigile versioonidele leiad lehelt [meshcore.io](https://meshcore.io). Lisaks on olemas veebirakendus [app.meshcore.nz](https://app.meshcore.nz), mis töötab arvutis Chrome'is või Edge'is.

## 4. Seo sõlm rakendusega {#pair}

Lülita sõlm sisse, ava rakendus ja ühendu sõlmega Bluetoothi kaudu. Kui rakendus küsib PIN-koodi:

- **ekraaniga** sõlm näitab PIN-koodi, sisesta see;
- **ekraanita** sõlm kasutab koodi `123456`.

Kui sidumine ebaõnnestub, eemalda seade telefoni Bluetoothi seadetest ja proovi uuesti. Seejärel anna sõlmele nimi. Teised näevad seda nime, nii et ära kasuta oma täisnime ega aadressi, kui sa seda ise ei soovi.

## 5. Vali oma piirkonna raadio eelseadistus {#preset}

Kõik ühe piirkonna raadiod kasutavad sama sagedust ja samu seadeid, muidu nad üksteist ei kuule. Vali rakenduse raadioseadetes eelseadistus, mida sinu piirkonnas kasutatakse. Väljaspool allolevaid piirkondi kasutatakse Euroopas eelseadistust **EU/UK (Narrow)**. Madalmaadel, Tšehhil, Ungaril, Slovakkial, Portugalil ja Šveitsil on oma eelseadistused ning Madalmaade Limburgil on oma variant:

{{< presets >}}

Kas sinu seade ei paku sinu piirkonna eelseadistust? Sisesta tabeli 4 väärtust käsitsi rakenduse raadioseadetesse: sagedus, ribalaius, levitustegur (spreading factor) ja kodeerimismäär (coding rate). Teiste väärtustega sõlm ei kuule võrku.

Sa pole kindel? Sinu [kohalik grupp](/community/) teab, millist eelseadistust sinu piirkonnas kasutatakse. Rakendus laadib selle loendi alla MeshCore'i projektilt, seega ei vaja uus eelseadistus rakenduse uuendust.

## 6. Ütle tere {#hello}

1. **Anna endast teada.** Saada rakendusest *advert*. „Flood“-advert liigub repeaterite (sõlmede, mis sõnumeid edasi saadavad) kaudu, nii et kõik võrgus olijad saavad sind lisada.
   Companionid ei anna endast kunagi automaatselt teada.
2. **Leia teised.** Inimesed ilmuvad sinu kontaktidesse siis, kui nende advertid sinuni jõuavad. Repeaterid saadavad vaikimisi flood-adverti iga 47 tunni järel, seega võib loendi täitumine võtta 2 päeva.
3. **Saada sõnum.** Ava kontakt ja kirjuta. Esimene sõnum levib üle kogu võrgu. Saaja teatab tagasi, mis teed sõnum läbis, ja hilisemad sõnumid liiguvad sama teed.
4. **Liitu kanalitega.** Kanal **Public** on juba seadistatud ja kõik, mida sinna kirjutad, jõuab kõigini võrgus. Oma piirkonna *hashtag-kanali* (nimi algab märgiga `#`) lisamiseks sisesta selle nimi. Sinu [kohalik grupp](/community/) ütleb, millised kanalid on aktiivsed.

## Kui miski ei tööta {#troubleshooting}

**Rakendus ei leia minu seadet Bluetoothi kaudu.**
Tõenäoliselt laadisid seadmesse USB-companioni. Laadi püsivara uuesti ja vali Bluetoothi versioon. Heltec V3 väikese sisseehitatud Bluetoothi antenni levi on lühike, seega hoia telefon lähedal.

**Sidumine ebaõnnestub korduvalt.**
Eemalda seade telefoni Bluetoothi seadetest, taaskäivita Bluetooth ja seo uuesti ekraanil oleva PIN-koodiga või koodiga `123456`.

**Minu kontaktidesse ei ilmu kedagi.**
Kontrolli, et eelseadistus vastaks sinu piirkonnale. Saada flood-advert. Kui ühtegi repeaterit pole levialas, kuuled ainult lähedal olevaid raadioid. [Kaardilehelt](/map/) näed, kus repeaterid asuvad.

**Kontakti juures on „last seen“ mitme päeva tagune, kuigi ta on aktiivne.**
Ühel kahest sõlmest on vale kellaaeg. Companion võtab kellaaja sinu telefonist. Repeateritel ja room serveritel (sõlmedel, mis hoiavad sõnumeid grupi jaoks) peab kellaaja seadistama nende omanik.

**Otsesõnum ei jõua kunagi kohale.**
Mõlemal peab teine olema kontaktina lisatud. Sõlm viskab tundmatult saatjalt tulnud sõnumi ära ega teata sellest saatjale. Saada flood-advert ja palu teisel inimesel samuti advert saata. Kontrolli rakenduses, et rakendus lisab uued kontaktid automaatselt. Rakendus lisab ainult need sõlmed, mis jäävad selle hüpete piiri sisse.

**Vanad kontaktid töötavad, uued ei ühendu kunagi.**
Esimene sõnum levib üle võrgu ja repeater edastab selle ainult siis, kui tal on sõnumi piirkond olemas. Hilisemad sõnumid liiguvad mööda õpitud teekonda ja seda ei peata ükski piirkonnakontroll. Küsi oma [kohalikust grupist](/community/), milliseid piirkondi sinu ümbruse repeaterid hoiavad, ja kontrolli [oma piirkonna seadeid](/guides/settings/#traffic).

**Rakendus ei ühendu enam sinu companioniga.**
Mõnel plaadil on kasutajanupp, näiteks mõnel RAK-plaadil ja Heltec T114-l. Hoia seda all esimese 8 sekundi jooksul pärast plaadi käivitumist. Companion avab USB kaudu päästekonsooli. Lehel [flasher.meshcore.io](https://flasher.meshcore.io) olevas konsoolis määrab `set pin <pin>` uue Bluetoothi PIN-koodi ja `erase` tühjendab seadme.

**Laadija ei saa Linuxis jadaporti avada.**
Sinu kasutaja vajab pordile juurdepääsu, näiteks `sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, või peab kuuluma gruppi `dialout`.

**Midagi muud.** [MeshCore'i KKK](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md) käsitleb veel paljusid probleeme.
