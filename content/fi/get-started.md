---
title: Aloita tästä
lead: Uudesta piirilevystä ensimmäiseen viestiin meshissä. Tarvitset LoRa-levyn, tietokoneen, jossa on Chrome tai Edge, sekä puhelimen tai kannettavan sovellusta varten.
description: Asenna MeshCore selaimesta, muodosta pariliitos sovelluksen kanssa, valitse alueesi radioasetus, lähetä ensimmäinen viestisi ja liity paikalliseen kanavaan.
eyebrow: 6 vaihetta · MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '68c89544'
  seeded: '2026-10-26'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', '36a3eba3', '6da9fd7a', 'cb5fb72e', '89626504', 'a419ce79', 'aa273b20']
---

Nämä vaiheet perustuvat MeshCore-laiteohjelmiston versioon v1.18.0 ja lokakuun 2026 virallisiin työkaluihin. Sovelluksen valikkojen nimet voivat vaihdella hieman versiosta toiseen.

## 1. Valitse laite {#device}

Mikä tahansa [laitesivun](/devices/) levy, jolle on merkitty companion, käy. Valitse ensimmäiseksi solmuksesi *companion*: radio, jolla lähetät viestejä. Yhdistä se puhelimeesi tai kannettavaasi Bluetoothilla tai USB:llä, tai valitse laite, jossa on oma näyttö ja näppäimistö ja joka toimii itsenäisesti.

Hanki 868 MHz:n versio. Mukana tuleva antenni riittää. [Antenniopas](/guides/antenna/) näyttää, miten tarkistat antennin.

{{< callout type="warning" >}}
Kiinnitä antenni ennen kuin kytket radion päälle. Ilman antennia lähettävä LoRa-radio voi vaurioittaa omaa piiriään.
{{< /callout >}}

## 2. Asenna laiteohjelmisto {#flash}

1. Liitä laite tietokoneeseen USB-datakaapelilla.
2. Avaa selainpohjainen asennusohjelma osoitteessa [flasher.meshcore.io](https://flasher.meshcore.io) Chromella tai Edgellä. Se käyttää Web Serial -rajapintaa, jota muut selaimet eivät tue.
3. Valitse laitteesi ja sitten **Companion**-laiteohjelmisto **Bluetooth**-versiona (tai USB-versiona, jos käytät laitetta vain tietokoneen kaapelilla).
4. Asenna. Jotkin levyt siirtyvät ensin päivitystilaan. Asennusohjelma kertoo, miten se tehdään.

Käytä *erase*-toimintoa vain, kun haluat aloittaa puhtaalta pöydältä: tyhjennys poistaa laitteen identiteetin ja yhteystietosi. Myöhemmät päivitykset kannattaa asentaa tyhjentämättä.

## 3. Asenna sovellus {#app}

Virallinen MeshCore-sovellus on saatavilla Androidille, iOS:lle, Windowsille ja macOS:lle. Linkit kaikkiin versioihin löytyvät osoitteesta [meshcore.io](https://meshcore.io). Lisäksi osoitteessa [app.meshcore.nz](https://app.meshcore.nz) on verkkosovellus, joka toimii tietokoneella Chromessa tai Edgessä.

## 4. Muodosta pariliitos solmuusi {#pair}

Kytke solmu päälle, avaa sovellus ja yhdistä solmuun Bluetoothilla. Kun sovellus kysyy PIN-koodia:

- solmu, jossa **on** näyttö, näyttää PIN-koodin; syötä se;
- solmu, jossa **ei ole** näyttöä, käyttää koodia `123456`.

Jos pariliitos epäonnistuu, poista laite puhelimesi Bluetooth-asetuksista ja yritä uudelleen. Anna sitten solmullesi nimi. Muut näkevät tämän nimen, joten älä käytä koko nimeäsi tai osoitettasi, ellet itse halua.

## 5. Valitse alueesi radioasetus {#preset}

Kaikki alueen radiot käyttävät samaa taajuutta ja samoja asetuksia, muuten ne eivät kuule toisiaan. Valitse sovelluksen radioasetuksista se esiasetus, jota alueesi käyttää. Alla lueteltujen alueiden ulkopuolella Eurooppa käyttää asetusta **EU/UK (Narrow)**. Alankomailla, Tšekillä, Unkarilla, Slovakialla, Portugalilla ja Sveitsillä on omat asetuksensa, ja Alankomaiden Limburgilla on oma muunnelmansa:

{{< presets >}}

Etkö ole varma? [Paikallinen ryhmäsi](/community/) tietää, mitä esiasetusta alueesi käyttää. Sovellus lataa tämän listan MeshCore-projektilta, joten uusi esiasetus ei vaadi sovelluspäivitystä.

## 6. Sano hei {#hello}

1. **Ilmoita itsestäsi.** Lähetä sovelluksesta *ilmoitus*. "flood"-ilmoitus kulkee toistimien (solmujen, jotka välittävät viestejä eteenpäin) kautta, joten kaikki meshissä voivat lisätä sinut.
   Companion-laitteet eivät koskaan ilmoita itsestään automaattisesti.
2. **Löydä muut.** Ihmiset ilmestyvät yhteystietoihisi, kun heidän ilmoituksensa tavoittavat sinut. Toistimet lähettävät flood-ilmoituksen oletuksena 47 tunnin välein, joten listasi täyttyminen voi kestää 2 päivää.
3. **Lähetä viesti.** Avaa yhteystieto ja kirjoita. Ensimmäinen viesti kulkee floodina verkon läpi. Vastaanottaja ilmoittaa takaisin, mitä reittiä viesti kulki, ja myöhemmät viestit seuraavat samaa reittiä.
4. **Liity kanaviin.** **Public**-kanava on jo valmiina. Kaikki, mitä sinne kirjoitat, tavoittaa jokaisen meshissä. Lisää alueesi *hashtag-kanava* (nimi, joka alkaa merkillä `#`) kirjoittamalla sen nimi. [Paikallinen ryhmäsi](/community/) kertoo, mitkä kanavat ovat aktiivisia.

## Kun jokin ei toimi {#troubleshooting}

**Sovellus ei löydä laitettani Bluetoothilla.**
Asensit luultavasti USB-version companion-laiteohjelmistosta. Asenna uudelleen ja valitse Bluetooth-versio. Heltec V3:n pieni sisäänrakennettu Bluetooth-antenni kantaa vain lyhyen matkan. Pidä puhelin lähellä.

**Pariliitos epäonnistuu toistuvasti.**
Poista laite puhelimesi Bluetooth-asetuksista, käynnistä Bluetooth uudelleen ja muodosta pariliitos uudelleen näytön PIN-koodilla tai koodilla `123456`.

**Yhteystietoihini ei ilmesty ketään.**
Tarkista, että esiasetuksesi vastaa aluettasi. Lähetä flood-ilmoitus. Jos kantaman sisällä ei ole toistinta, kuulet vain lähellä olevat radiot. [Karttasivu](/map/) näyttää, missä toistimet ovat.

**Yhteystiedon kohdalla lukee "viimeksi nähty" päiviä sitten, vaikka hän on aktiivinen.**
Toisella solmuista on väärä kellonaika. Companion ottaa ajan puhelimestasi. Toistimien ja huonepalvelimien (solmujen, jotka tallentavat ryhmän viestit) omistajan täytyy asettaa aika itse.

**Asennusohjelma ei saa sarjaporttia auki Linuxissa.**
Käyttäjätunnuksesi tarvitsee pääsyn porttiin, esimerkiksi komennolla `sudo setfacl -m u:$USER:rw /dev/ttyUSB0` tai `dialout`-ryhmän jäsenyydellä.

**Jokin muu.** [MeshCoren FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md) käsittelee monia muita ongelmia.
