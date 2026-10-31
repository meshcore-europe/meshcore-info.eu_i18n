---
title: Aloita tästä
lead: Uudesta laitteesta ensimmäiseen viestiisi meshissä. Tarvitset LoRa-laitteen, tietokoneen, jossa on Chrome tai Edge, sekä puhelimen tai kannettavan sovellusta varten.
description: Asenna MeshCore selaimella, yhdistä sovellus, valitse alueesi käyttämä radioasetus, lähetä ensimmäinen viestisi ja liity paikalliseen kanavaan.
eyebrow: 6 vaihetta · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-10-31'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Nämä ohjeet perustuvat MeshCore-laiteohjelmistoon v1.18.0 ja lokakuun 2026
virallisiin työkaluihin. Sovelluksen valikoiden nimet voivat vaihdella hieman
versioiden välillä.

## 1. Valitse laite {#device}

Mikä tahansa [laitesivun](/devices/) laite, jonka kohdalla lukee companion,
käy. Valitse ensimmäiseksi solmuksesi *companion*: radio, jolla lähetät
viestejä. Yhdistä se puhelimeesi tai kannettavaasi Bluetoothilla tai USB:llä.
Voit myös valita mallin, jossa on oma näyttö ja näppäimistö ja joka toimii
itsenäisesti.

Hanki 868 MHz:n versio. Mukana tuleva antenni riittää.
[Antenniohjeesta](/guides/antenna/) näet, miten antennin voi tarkistaa.

{{< callout type="warning" >}}
Kiinnitä antenni ennen kuin kytket radion päälle. Jos LoRa-radio lähettää
ilman antennia, sen piiri voi vaurioitua.
{{< /callout >}}

## 2. Asenna laiteohjelmisto {#flash}

1. Kytke laite tietokoneeseen USB-datakaapelilla.
2. Avaa verkkoasennin osoitteessa [flasher.meshcore.io](https://flasher.meshcore.io)
   Chromella tai Edgellä. Asennin käyttää Web Serialia, jota muut selaimet eivät tue.
3. Valitse laitteesi ja sitten **Companion**-laiteohjelmisto **Bluetoothille**
   (tai USB:lle, jos käytät laitetta vain tietokoneen kaapelilla).
4. Aloita asennus. Osa laitteista pitää ensin siirtää päivitystilaan.
   Asennin kertoo, miten se tehdään.

Käytä *erase*-toimintoa vain, kun haluat aloittaa alusta. Tyhjennys poistaa
laitteen identiteetin ja yhteystietosi. Myöhemmät päivitykset asennat ilman
tyhjennystä. Jos haluat säilyttää identiteettisi tyhjennyksen yli, vie
companionin yksityinen avain ensin sovelluksesta ja tuo se takaisin
tyhjennyksen jälkeen.

## 3. Asenna sovellus {#app}

Virallinen MeshCore-sovellus on saatavilla Androidille, iOS:lle, Windowsille
ja macOS:lle. Linkit kaikkiin versioihin löydät sivulta
[meshcore.io](https://meshcore.io). Lisäksi osoitteessa
[app.meshcore.nz](https://app.meshcore.nz) on verkkosovellus, joka toimii
tietokoneen Chromessa tai Edgessä.

## 4. Muodosta pariliitos solmuun {#pair}

Kytke solmu päälle, avaa sovellus ja yhdistä solmuun Bluetoothilla. Kun
sovellus kysyy PIN-koodia:

- jos solmussa **on** näyttö, se näyttää PIN-koodin; kirjoita se;
- jos solmussa **ei ole** näyttöä, koodi on `123456`.

Jos pariliitos epäonnistuu, poista laite puhelimen Bluetooth-asetuksista ja
yritä uudelleen. Anna sitten solmullesi nimi. Muut näkevät nimen, joten älä
käytä koko nimeäsi tai osoitettasi, ellet halua.

## 5. Valitse alueesi radioasetus {#preset}

Kaikki saman alueen radiot käyttävät samaa taajuutta ja samoja asetuksia.
Muuten ne eivät kuule toisiaan. Valitse sovelluksen radioasetuksista alueesi
käyttämä esiasetus. Alla lueteltujen alueiden ulkopuolella Euroopassa
käytetään asetusta **EU/UK (Narrow)**. Alankomailla, Tšekillä, Unkarilla,
Slovakialla, Portugalilla ja Sveitsillä on omansa, ja Alankomaiden
Limburgissa on oma muunnelmansa:

{{< presets >}}

Eikö laitteessasi ole alueesi esiasetusta? Syötä taulukon 4 arvoa käsin
sovelluksen radioasetuksiin: taajuus, kaistanleveys, levityskerroin
(spreading factor) ja koodaussuhde (coding rate). Solmu, jolla on eri arvot,
ei kuule meshiä.

Etkö ole varma? [Paikallinen ryhmäsi](/community/) tietää, mitä esiasetusta
alueellasi käytetään. Sovellus lataa tämän listan MeshCore-projektilta, joten
uusi esiasetus ei vaadi sovelluspäivitystä.

## 6. Tervehdi muita {#hello}

1. **Ilmoita itsestäsi.** Lähetä sovelluksesta *ilmoitus*. Flood-ilmoitus
   kulkee toistimien (solmujen, jotka välittävät viestejä eteenpäin) kautta,
   joten kaikki meshissä voivat lisätä sinut.
   Companionit eivät koskaan ilmoita itsestään automaattisesti.
2. **Löydä muita.** Muut ilmestyvät yhteystietoihisi, kun heidän ilmoituksensa
   tavoittavat sinut. Toistimet lähettävät oletuksena flood-ilmoituksen 47
   tunnin välein, joten listasi täyttymiseen voi mennä 2 päivää.
3. **Lähetä viesti.** Avaa yhteystieto ja kirjoita. Ensimmäinen viesti
   leviää koko verkkoon flood-tilassa. Vastaanottaja ilmoittaa takaisin
   reitin, jota viesti kulki, ja myöhemmät viestit kulkevat sitä reittiä.
4. **Liity kanaville.** **Public**-kanava on valmiiksi käytössä. Kaikki, mitä
   kirjoitat sinne, tavoittaa jokaisen meshissä. Lisää alueesi
   *hashtag-kanava* (nimi alkaa merkillä `#`) kirjoittamalla sen nimi.
   [Paikallinen ryhmäsi](/community/) kertoo, mitkä kanavat ovat aktiivisia.

## Kun jokin ei toimi {#troubleshooting}

**Sovellus ei löydä laitettani Bluetoothilla.**
Asensit todennäköisesti USB-companionin. Asenna uudelleen ja valitse
Bluetooth-versio. Heltec V3:ssa pienen sisäänrakennetun Bluetooth-antennin
kantama on lyhyt, joten pidä puhelin lähellä.

**Pariliitos epäonnistuu yhä uudelleen.**
Poista laite puhelimen Bluetooth-asetuksista, käynnistä Bluetooth uudelleen
ja muodosta pariliitos taas näytön PIN-koodilla tai koodilla `123456`.

**Yhteystietoihini ei ilmesty ketään.**
Tarkista, että esiasetuksesi vastaa aluettasi. Lähetä flood-ilmoitus. Jos
kantaman sisällä ei ole toistinta, kuulet vain lähellä olevat radiot.
[Karttasivulta](/map/) näet, missä toistimia on.

**Yhteystiedon kohdalla lukee "viimeksi nähty" päiviä sitten, vaikka hän on aktiivinen.**
Jommankumman solmun kellonaika on väärin. Companion hakee ajan puhelimestasi.
Toistimien ja room servereiden (solmujen, jotka tallentavat viestejä
ryhmälle) ajan asettaa niiden omistaja.

**Yksityisviesti ei koskaan tule perille.**
Kummankin täytyy olla toisen yhteystiedoissa. Solmu hylkää viestin
tuntemattomalta lähettäjältä kertomatta siitä lähettäjälle. Lähetä
flood-ilmoitus ja pyydä toista lähettämään samoin. Tarkista sovelluksesta,
että se lisää uudet yhteystiedot automaattisesti. Sovellus lisää vain solmut,
jotka ovat sen hyppyrajan sisällä.

**Vanhat yhteystiedot toimivat, uusiin ei synny yhteyttä.**
Ensimmäinen viesti lähtee flood-tilassa, ja toistin välittää sen vain, jos
sillä on viestin alue. Myöhemmät viestit kulkevat opittua reittiä, eikä
aluetarkistus pysäytä niitä. Kysy [paikalliselta ryhmältäsi](/community/),
mitkä alueet lähistön toistimilla on, ja tarkista
[alueesi asetukset](/guides/settings/#traffic).

**Sovellus ei enää yhdisty companioniisi.**
Joissakin laitteissa on käyttäjäpainike, esimerkiksi osassa RAK-laitteita ja
Heltec T114:ssä. Pidä sitä painettuna 8 ensimmäisen sekunnin aikana laitteen
käynnistyttyä. Companion avaa tällöin pelastuskonsolin USB:n kautta.
Osoitteen [flasher.meshcore.io](https://flasher.meshcore.io) konsolissa
`set pin <pin>` asettaa uuden Bluetooth-PIN-koodin ja `erase` tyhjentää
laitteen.

**Asennin ei saa sarjaporttia auki Linuxissa.**
Käyttäjätunnuksellasi pitää olla pääsy porttiin, esimerkiksi komennolla
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, tai sen pitää kuulua `dialout`-ryhmään.

**Jokin muu ongelma.**
[MeshCoren usein kysytyt kysymykset](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
käsittelevät monia muita ongelmia.
