---
title: Mikä MeshCore on?
lead: MeshCore lähettää tekstiviestejä radiolla solmusta solmuun. Se toimii ilman internetiä ja ilman liittymää.
description: 'Mitä MeshCore on ja mitä se ei ole: mesh, companion-laitteet, toistimet ja huonepalvelimet, reititys, salaus ja 868 MHz:n taajuusalue Euroopassa.'
eyebrow: MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '33e571f0'
  seeded: '2026-10-26'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['a3a6c1ff', '007314d2', 'f1f23981', '493b444f', '429f699c', 'f8008f48', '655373a9']
---

MeshCore on ilmainen ohjelmisto pieniin LoRa-radioihin. LoRa on radiotekniikka,
joka lähettää pieniä määriä dataa kauas hyvin pienellä teholla. Radiota, jossa
MeshCore on, kutsutaan *solmuksi*. Kun yhdistät sen puhelimesi tai tietokoneesi
sovellukseen, tai kun siinä on oma näyttö ja näppäimistö, voit lähettää tekstiä
kilometrien päähän. Välissä ei ole tukiasemaa, reititintä eikä operaattoria.

MeshCore lähettää vain lyhyitä tekstiviestejä: ei puhetta, kuvia eikä
internetliikennettä.
Viestin kulkuun voi mennä muutama sekunti, ja sen perillemeno riippuu
ympärilläsi olevista toistimista. Se ei korvaa hätäpalveluja: hätätilanteessa
soita numeroon 112.

Ohjelmisto on avointa lähdekoodia. Sitä kehitetään osoitteessa
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) MIT-lisenssillä.

## Mesh minuutissa {#mesh}

Yksi LoRa-radio kantaa kaupungissa muutaman kilometrin, ja mäeltä tai katolta
paljon pidemmälle. Kantamaa saa lisää, kun radiot välittävät viestejä toisilleen:
sitä kutsutaan *meshiksi*. MeshCoressa välittämisen hoitavat radiot, joita
kutsutaan *toistimiksi*. Toistin, joka kuulee viestin, lähettää sen uudelleen, ja
niin viesti voi kulkea kokonaisen alueen halki.

Mesh ei ole kenenkään omaisuutta. Jokainen solmu ja jokainen toistin kuuluu
jollekulle yhteisön jäsenelle. Mesh on juuri niin hyvä kuin toistimet, joita
ihmiset pystyttävät.

## 3 solmutyyppiä {#roles}

Valitset solmun tyypin, kun flashaat sen. Ensimmäinen solmusi on companion.

**Companion.** Oma radiosi. Se muodostaa pariliitoksen puhelimesi tai
tietokoneesi MeshCore-sovellukseen Bluetoothilla tai USB:llä; joissakin on oma
näyttö ja näppäimistö. Sovelluksessa luet ja kirjoitat viestit. Companion
säilyttää yhteystietosi ja kanavasi sekä viestit, jotka saapuivat, kun sovellus ei
ollut yhdistettynä. Companion ei välitä viestejä muille.

**Toistin.** Korkealle sijoitettu radio, joka välittää viestejä kaikille. Useimmat
toimivat aurinkosähköllä. Tarvitset oman toistimen vain siellä, minne mesh ei
vielä ulotu. Sillä ei ole omaa sovellusta. Teet asetukset USB:n kautta, tai
kirjaudut sisään salasanalla ja hallitset sitä radion yli.
[Toistinopas](/repeater-guide/) näyttää, miten se tehdään.

**Huonepalvelin.** Pieni ilmoitustaulu meshissä. Kun kirjaudut sisään, saat
viestit, jotka jäivät sinulta väliin kantaman ulkopuolella, enintään 32 viimeistä.
Paikallinen ryhmä käyttää sitä tiedotuksiin.

## Miten viesti löytää perille {#routing}

Jokaisella solmulla on salainen avain ja julkinen avain. Julkinen avain on sen
identiteetti. Solmu ilmoittaa itsestään *ilmoituksella*: allekirjoitetulla
paketilla, jossa on sen nimi ja halutessasi sen sijainti. Joku ilmestyy
yhteystietoihisi, kun yksi hänen ilmoituksistaan on saapunut sinulle tai kun
skannaat hänen QR-koodinsa. Sovelluksessa on painike oman ilmoituksen
lähettämiseen.

Ensimmäinen viestisi yhteystiedolle lähtee *floodina*. Jokainen toistin, joka
kuulee sen, välittää sen kerran eteenpäin ja lisää matkalla oman lyhyen
tunnuksensa. Vastaus tuo tuon tunnusluettelon takaisin. Siitä lähtien viestisi
tälle yhteystiedolle kulkevat tallennettua reittiä, ja vain sen varrella olevat
toistimet lähettävät. Kun reitti katkeaa, sovellus floodaa uudelleen.

Kanavalle lähetetyillä viesteillä ei ole yhtä osoitetta, joten ne floodataan aina.
Toistimet muistavat, mitä ne ovat äskettäin välittäneet, ja hylkäävät kopiot,
jotka saapuvat uudelleen toista reittiä. Viesti voi kulkea enintään 64 toistimen
kautta, tai 32, jos esiasetus käyttää 2 tavun tunnuksia.

## Salaus ja yksityisyys {#encryption}

Yksityisviestisi on salattu päästä päähän: vain sinä ja vastaanottaja voitte
lukea ne. Toistin näkee paketin vastaanottajasta vain 1 tavun vihjeen.

Kanavat salataan jaetulla avaimella, joten niitä voi lukea se, jolla avain on:

- **Public** on asennettu jokaiseen companioniin. Sen avain on julkaistu, joten
  kuka tahansa voi lukea sitä.
- **Hashtag-kanavat**, kuten `#utrecht`, saavat avaimensa nimestään. Kuka
  tahansa nimen tietävä voi liittyä, joten pidä niitäkin julkisina.
- **Yksityiset kanavat** käyttävät satunnaista avainta, jonka jaat itse,
  esimerkiksi QR-koodina.

Ilmoitukset allekirjoitetaan, mutta niitä ei salata. Solmusi nimi, ja sen
sijainti jos jaat sen, näkyvät kaikille kantaman sisällä. Valitse nimi, joka
kertoo vain sen, minkä haluat.

## 868 MHz:n taajuusalue Euroopassa {#band}

Euroopassa MeshCore käyttää pientä osaa 868 MHz:n taajuusalueesta, jota kuka
tahansa saa käyttää ilman lupaa. Sen eurooppalainen radioesiasetus, EU/UK
(Narrow), sijaitsee taajuudella 869.618 MHz 62.5 kHz:n kanavalla. Se on
869.40-869.65 MHz:n osa-alueella, jolla sallitaan enintään 500 mW e.r.p. Laite
saa lähettää siellä enintään 10% ajasta.
[Toistinoppaan lakiosiosta](/repeater-guide/#legal) löydät yksityiskohdat ja
maakohtaiset rajat.

Kaikki saman alueen käyttäjät käyttävät samaa esiasetusta, muuten radiot eivät
kuule toisiaan. Joissakin maissa ja alueilla käytetään muunnelmaa:
[paikallinen ryhmäsi](/community/) tietää, mikä se on.

## Mihin ihmiset käyttävät sitä {#uses}

- Yhteydenpitoon vaelluksilla, merellä ja festivaaleilla, joissa matkapuhelinverkko
  on ylikuormittunut tai sitä ei ole.
- Varakanavaksi perheelle tai naapureille, kun sähkö tai matkapuhelinverkot
  katkeavat.
- Paikalliseen keskusteluun radioilla, jotka ihmiset omistavat itse.
- Kokeiluihin radion, antennien, aurinkosähkön ja avoimen lähdekoodin
  ohjelmistojen kanssa.
