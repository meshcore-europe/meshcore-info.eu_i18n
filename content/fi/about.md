---
title: Mikä MeshCore on?
lead: MeshCore lähettää tekstiviestejä radiolla solmusta solmuun. Se toimii ilman internetiä ja ilman liittymää.
description: 'Mitä MeshCore on ja mitä se ei ole: solmutyypit, reititys, erot Meshtasticiin, salaus ja 868 MHz:n taajuusalue.'
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

MeshCore on ilmainen ohjelmisto pienille LoRa-radioille. LoRa on radiotekniikka,
joka lähettää vähän dataa pitkälle hyvin vähällä energialla. Radiota, jossa on
MeshCore, kutsutaan *solmuksi*. Kun yhdistät sen puhelimesi tai kannettavasi
sovellukseen tai käytät sen omaa näyttöä ja näppäimistöä, voit lähettää tekstiä kilometrien päähän. Välissä ei ole mastoa, reititintä eikä operaattoria.

Ohjelmisto on avointa lähdekoodia. Sitä kehitetään osoitteessa
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) MIT-lisenssillä.

## Mitä MeshCore ei ole {#not}

Onko radio sinulle uusi asia? Näitä ihmiset odottavat MeshCorelta useimmin,
mutta se ei tee niitä.

- **Se ei ole internet eikä puhelin.** MeshCore lähettää lyhyitä tekstiviestejä,
  suunnilleen puhelimen tekstiviestin pituisia. Ääni, kuvat, video ja verkkosivut
  eivät kulje, etkä tavoita tavallista puhelinnumeroa.
- **Se ei ole hätäpalvelu.** Yksikään hätäpalvelu ei kuuntele meshiä, eikä kukaan
  lupaa, että joku lukee viestisi. Hätätilanteessa soita numeroon 112.
- **Se ei ole välitön, eikä sitä ole kaikkialla.** Viesti hyppii radiolta radiolle.
  Perillepääsy voi kestää muutaman sekunnin, tai viesti ei tule perille lainkaan.
  Se, meneekö viesti perille, riippuu ympärilläsi olevista toistimista, korkeudesta,
  rakennuksista ja antennistasi. Pieni radio ei sisätiloissa useinkaan tavoita ketään,
  kun taas katolla oleva toistin kantaa kilometrien päähän.
- **Se ei ole palvelu, jota joku ylläpitää puolestasi.** Palveluntarjoajaa, tukipalvelua
  tai kuuluvuuslupausta ei ole. Meshiä on siellä, missä yhteisön jäsenet ovat
  pystyttäneet toistimia, eikä missään muualla.
- **Kaikki meshissä ei ole yksityistä.** Yksityisviestit on salattu, mutta kuka tahansa
  voi lukea Public-kanavaa ja hashtag-kanavia. Solmusi nimen ja jakamasi sijainnin
  näkevät kaikki kantaman sisällä. [Tarkkailijat](/network/) raportoivat kuulemansa
  julkisille kartoille. [Salausosio](#encryption) kertoo, mikä pysyy yksityisenä.
- **Se ei ole rajaton.** Kaikki alueen käyttäjät jakavat yhden radiokanavan, ja
  [868 MHz:n taajuusalueen](#band) säännöt rajoittavat, kuinka kauan kukin radio saa
  lähettää. Jokainen viesti vie lähetysaikaa kaikilta muilta, joten botit, tiheät
  ilmoitukset ja testiviestit hidastavat meshiä kaikkien osalta.
- **Se ei ole Meshtastic.** Meshtastic on eri järjestelmä, joka toimii pitkälti
  samoilla piirilevyillä. Järjestelmät eivät voi viestiä keskenään.
  Osio [Meshtasticista siirtyville](#meshtastic) kertoo, mikä toimii eri tavalla.

## Mesh minuutissa {#mesh}

Yksi LoRa-radio kantaa kaupungissa muutaman kilometrin, ja mäeltä tai
katolta paljon pidemmälle. Jotta viestit kulkisivat pidemmälle, radiot välittävät niitä toistensa puolesta:
se on *mesh*. MeshCoressa välittämisen hoitavat radiot, joita kutsutaan *toistimiksi*.
Kun toistin kuulee viestin, se lähettää sen uudelleen. Näin viesti voi kulkea koko alueen halki.

Kukaan ei omista meshiä. Jokainen solmu ja jokainen toistin kuuluu jollekulle
yhteisössä. Mesh ulottuu niin pitkälle kuin heidän toistimensa ulottuvat.

## 3 solmutyyppiä {#roles}

Valitset solmun tyypin, kun asennat siihen laiteohjelmiston. Ensimmäinen solmusi on companion.

**Companion.** Oma radiosi. Yhdistät sen puhelimesi tai kannettavasi
MeshCore-sovellukseen Bluetoothilla tai USB:llä. Joissakin on oma näyttö ja näppäimistö.
Sovelluksessa luet ja kirjoitat viestit. Companion säilyttää yhteystietosi ja kanavasi
sekä viestit, jotka saapuivat, kun sovellus ei ollut yhdistettynä. Companion ei välitä muiden viestejä.

**Toistin.** Korkealle sijoitettu radio, joka välittää viestejä kaikille. Useimmat
toimivat aurinkovoimalla. Omaa toistinta tarvitset vain siellä, minne mesh ei vielä
ulotu. Sillä ei ole omaa sovellusta. Määrität sen USB:n kautta tai
kirjaudut sisään salasanalla ja hallitset sitä radion kautta.
[Toistinopas](/repeater-guide/) neuvoo, miten se tehdään.

**Room server.** Pieni ilmoitustaulu meshissä. Kun kirjaudut sisään, saat
viestit, jotka menetit ollessasi kantaman ulkopuolella, enintään 32 viimeisintä.
Se säilyttää ne vain muistissa, joten uudelleenkäynnistys tai sähkökatko poistaa ne.
Paikallinen ryhmä käyttää sellaista tiedotteisiin.

## Miten viesti löytää perille {#routing}

Jokaisella solmulla on yksityinen avain ja julkinen avain. Julkinen avain on sen identiteetti. Solmu
ilmoittaa itsestään *ilmoituksella*: allekirjoitetulla paketilla, jossa on sen nimi ja,
jos niin valitset, sen sijainti. Henkilö ilmestyy yhteystietoihisi, kun jokin hänen
ilmoituksistaan tavoittaa sinut tai kun skannaat hänen QR-koodinsa. Sovelluksessa on painike, jolla lähetät oman ilmoituksesi.

Ensimmäinen viestisi yhteystiedolle lähtee *floodina*. Jokainen toistin, joka
kuulee sen, välittää sen kerran ja lisää matkalla siihen oman lyhyen tunnuksensa.
Vastaus tuo tämän tunnuslistan takaisin. Siitä eteenpäin viestisi tälle yhteystiedolle
kulkevat tallennettua reittiä, ja vain reitin varrella olevat toistimet lähettävät.
Kun reitti katkeaa, sovellus lähettää taas floodina.

Kanavaviesteillä ei ole yhtä osoitetta, joten ne lähtevät aina floodina.
Toistimet muistavat, mitä ne ovat äskettäin välittäneet, ja hylkäävät kopiot, jotka
saapuvat uudelleen toista reittiä. Viesti voi kulkea enintään 64 toistimen kautta tai 32:n kautta, jos esiasetus käyttää 2-tavuisia
tunnuksia.

## Meshtasticista siirtyville {#meshtastic}

Monilla piirilevyillä toimii joko MeshCore tai Meshtastic, ja asennat niistä haluamasi. Nämä erot huomaat ensimmäisenä. Ne perustuvat MeshCoren versioon v1.18.0 ja Meshtasticin marraskuun 2026 dokumentaatioon.

- **Kuka välittää viestit eteenpäin.** MeshCoressa sen tekevät vain toistimet, oma companionisi ei koskaan.
  Meshtasticissa viestejä välittää myös oletuksena käytössä oleva client-rooli, ellei jokin toinen
  solmu ole jo tehnyt sitä.
- **Kuinka pitkälle viesti kulkee.** MeshCore-viesti voi kulkea enintään 64
  toistimen kautta. Meshtasticissa raja on oletuksena 3 hyppyä ja enintään 7.
- **Muiden solmujen lukemat.** MeshCoressa toistimet ja anturisolmut lähettävät
  lukemia, kuten akun jännitteen, kun pyydät niitä. Ne eivät lähetä lukemia koko meshille.
- **Internet.** MeshCoren laiteohjelmistossa ei ole meshien välistä yhteyttä
  internetin kautta. [Tarkkailijat](/network/) raportoivat kuulemansa kartoille, vain
  yhteen suuntaan. Meshtasticissa on sisäänrakennettu MQTT-moduuli, joka voi välittää
  viestejä meshien välillä internetin kautta.

## Salaus ja yksityisyys {#encryption}

Yksityisviestisi on salattu päästä päähän: vain sinä ja toinen osapuoli
voitte lukea ne. Toistin näkee paketin vastaanottajasta vain 1 tavun vihjeen.

Kanavat on salattu jaetulla avaimella, joten niitä voi lukea se, jolla
avain on:

- **Public** on valmiina jokaisessa companionissa. Sen avain on julkaistu, joten kuka tahansa
  voi lukea sitä.
- **Hashtag-kanavat**, kuten `#utrecht`, saavat avaimensa nimestään.
  Kuka tahansa nimen tietävä voi liittyä, joten pidä niitäkin julkisina.
- **Yksityiset kanavat** käyttävät satunnaista avainta, jonka jaat itse, esimerkiksi
  QR-koodina.

Ilmoitukset on allekirjoitettu, mutta niitä ei ole salattu. Solmusi nimen ja sijainnin, jos
jaat sen, näkevät kaikki kantaman sisällä. Valitse nimi, joka ei kerro enempää
kuin haluat.

## 868 MHz:n kaista Euroopassa {#band}

Euroopassa MeshCore käyttää pientä osaa 868 MHz:n kaistasta. Sitä saa käyttää kuka tahansa
ilman lupaa. MeshCoren eurooppalainen radioesiasetus, EU/UK (Narrow), on taajuudella
869.618 MHz 62.5 kHz:n kanavalla. Se on 869.40-869.65 MHz:n
alikaistalla, joka sallii enintään 500 mW e.r.p. Laite saa lähettää siellä enintään 10%
ajasta.
[Toistinoppaan lakiosiossa](/repeater-guide/#legal) on lisätiedot
ja maakohtaiset rajat.

Kaikki alueen käyttäjät käyttävät samaa esiasetusta, muuten heidän radionsa eivät kuule toisiaan.
Joissakin maissa ja alueilla käytetään muunnelmaa: [paikallinen ryhmäsi](/community/)
tietää, mitä muunnelmaa.

## Mihin sitä käytetään {#uses}

- Yhteydenpito vaelluksilla, merellä ja festivaaleilla, kun matkapuhelinverkko on
  ruuhkautunut tai puuttuu.
- Varakanava perheelle tai naapureille, kun sähköt katkeavat tai matkapuhelinverkot lakkaavat toimimasta.
- Paikallinen keskustelu ihmisten omilla radioilla.
- Etäkohteen tarkistaminen kotoa käsin. Toistimet ja anturisolmut ilmoittavat akkujännitteensä
  ja muita lukemia, kun pyydät niitä.
- Anturin seuranta. Anturisolmussa toimii MeshCoren laiteohjelmisto mittaamiseen.
  Solmu pitää lukemistaan historiaa. Jos tilaat hälytykset, solmu varoittaa sinua
  esimerkiksi silloin, kun sen akku on vähissä.
- Kaukana olevan laitteen, kuten pumpun, kytkeminen. Lisäät tämän toiminnon
  anturisolmun laiteohjelmistoon omalla koodillasi.
- Kokeileminen radiolla, antenneilla, aurinkovoimalla ja avoimen lähdekoodin ohjelmistoilla.

## Mistä tiedot tulevat {#data}

[Paikalliset ryhmät](/community/) -sivun haku löytää paikan
[GeoNamesin](https://www.geonames.org/) ilmaisten paikka- ja postinumeroluetteloiden kopiosta.
Luettelot on julkaistu lisenssillä
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopio on tällä
sivustolla. Hakusi ei koskaan poistu laitteeltasi, eikä GeoNamesiin lähde yhtään pyyntöä.
