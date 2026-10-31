---
title: Toistinopas
lead: Korkealle sijoitettu toistin välittää viestejä kaikille ympärillään, koko kaupungin tai laakson alueella. Valitse paikka, anna aurinkopaneelin tuottaa virta, tee asetukset ja pysy lain rajoissa.
description: 'Näin suunnittelet, hoidat virran, määrität ja käytät laillisesti MeshCore-toistinta Euroopassa: paikan valinta, aurinkovirran mitoitus, CLI-asetukset sekä 868 MHz:n teho- ja käyttöasteen rajat.'
eyebrow: 868 MHz · enintään 500 mW · ilman lupaa
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-10-31'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Mesh toimii toistimien varassa. Companionit eli radiot, joilla lähetät viestejä, eivät
välitä viestejä eteenpäin. Ilman
toistimia tavoitat siis vain suoralla kantamalla olevat ihmiset. Oikeaan
paikkaan sijoitettu toistin laajentaa meshiä kaikille lähistöllä oleville. Tämä opas perustuu MeshCore-laiteohjelmiston
versioon v1.18.0.

Ennen kuin aloitat, ota yhteyttä [paikalliseen ryhmääsi](/community/). Ryhmä tietää, missä
kuuluvuus puuttuu, [mitä esiasetusta alueellasi käytetään](/guides/settings/) ja miten toistimet nimetään. Katso
[kuuluvuuskartoilta](/map/) lähelläsi olevat toistimet ja tervehdi muita julkisilla
tai paikallisilla [kanavilla](/guides/channels/).

## Tarvitsetko toistimen? {#need}

Toistin lähettää eteenpäin jokaisen kuulemansa flood-viestin. Kaikki kantaman sisällä olevat
toistimet jakavat saman lähetysajan. Jos mesh jo tavoittaa sinut, uusi
toistin lisää liikennettä eikä kuuluvuutta. Korkealle sijoitettu companion, esimerkiksi ullakon
ikkunassa tai parvekkeella, voi riittää sinulle.

Pystytä toistin sinne, missä kuuluvuus puuttuu:

- [kuuluvuuskartoilla](/map/) ei näy toistinta lähelläsi, tai näkyy vain sellaisia, joita
  companionisi ei kuule;
- paikallinen ryhmäsi sanoo, että alue tarvitsee toistimen.

## Valitse paikka {#site}

Korkeus on tärkeämpää kuin teho. LoRa kulkee 868 MHz:llä parhaiten esteettömällä
näköyhteydellä. Mäet, rakennukset ja tiheä metsä syövät kantamaa paljon enemmän
kuin muutama lisämilliwatti voittaa takaisin.

- **Mene korkealle.** Katto, masto, korkea rakennus tai mäki kattaa paljon
  enemmän kuin ikkunalauta. Jo muutama metri ympäröivien kattojen yläpuolella auttaa.
- **Pidä antenni vapaana.** Asenna se räystäiden yläpuolelle, kauas
  metallista, ränneistä ja muista antenneista.
- **Tarkista näkymä.** [HeyWhatsThatin](https://www.heywhatsthat.com/) kaltaisilla työkaluilla
  näet, mitä paikasta näkyy. Jos näet jonkin kohdan, sinne sijoitettu toistin on kantaman sisällä.
- **Jätä tilaa.** Radioreitti tarvitsee vapaata tilaa myös suoran
  linjan ympärille. Pitkillä matkoilla reitin keskikohdan
  pitää kulkea useita metrejä esteiden yläpuolella.
- **Pyydä lupa.** Hanki katon tai maston omistajan suostumus ja sovi,
  miten pääset toistimelle huoltoa varten.

## Laitteisto {#hardware}

- **Piirilevy.** Valitse vähävirtainen nRF52-levy, kuten
  [Heltec T114](/devices/), RAK WisBlock tai SenseCAP Solar Node. ESP32-levyt
  kuluttavat enemmän virtaa (laitesivulla niissä on merkintä High). Siksi niitä
  on vaikea käyttää aurinkovirralla.
- **Antenni.** Käytä 868 MHz:lle tehtyä antennia pystyasennossa.
  [Antenniopas](/guides/antenna/) kertoo tyypeistä, liittimistä, kaapelista ja
  asennuksesta. Antennin vahvistus lasketaan mukaan sallittuun tehorajaan, katso
  [Lailliset rajat](#legal).
- **Kaapeli.** Pidä koaksiaalikaapeli lyhyenä tai käytä pienihäviöistä kaapelia. 868 MHz:llä
  muutama metri ohutta kaapelia voi hukata puolet tehostasi.
- **Kotelo.** Sääsuojattu kotelo (IP65 tai parempi), jossa on kaapeliläpivienti,
  tuuletus- tai vedenpoistoreikä kosteuden tiivistymistä vastaan sekä vaalea väri tai aurinkosuoja.
  Akut kärsivät kuumuudesta, eikä niitä voi ladata pakkasella.
- **Salama.** Katolla oleva antenni on salaman kohde. Noudata paikallisia
  maadoitusmääräyksiä tai asenna antenni paikkaan, josta isku ei ulotu rakennuksen
  sähköjohtoihin.

## Virta ja aurinkovirran mitoitus {#power}

Aurinkovirralla toimivan toistimen on selvittävä talven pimeimmistä viikoista. Mitoita se
niiden mukaan:

1. **Mittaa kuorma.** Kytke valmiiksi määritetty toistin vuorokaudeksi USB-tehomittarin
   kautta. Lue kulutettu energia wattitunteina (Wh). Alueesi liikenne
   vaikuttaa lukuun, joten mittaa paikan päällä, jos voit.
2. **Lisää varaa.** Mitoita akun kapasiteetti vähintään 5–7 päiväksi
   ilman hyödyllistä auringonvaloa.
3. **Selvitä talven auringonvalo.** EU:n maksuton
   [PVGIS-työkalu](https://re.jrc.ec.europa.eu/pvg_tools/en/) näyttää mille tahansa
   paikalle, paljonko energiaa paneeli tuottaa kuukaudessa. Käytä kuukautta, jolloin
   aurinkoa on vähiten.
4. **Mitoita paneeli.** Paneelin on korvattava jokaisen päivän kulutus tuona huonoimpana
   kuukautena, ja lataushäviöille on jäätävä varaa.

Laskuesimerkki oletetuilla luvuilla: toistin, joka kuluttaa 1 Wh päivässä,
tarvitsee viikon varaa varten vähintään 7 Wh:n akun. Se on noin 2 Ah
käytettävää kapasiteettia 3,7 V:n jännitteellä. Jos PVGIS kertoo, että 1 W:n paneeli tuottaa paikallasi
0,5 Wh päivässä joulukuussa, tarvitset vähintään 2 W:n paneelin. 3–5 W:n paneeli
jättää varaa pilville, lumelle ja vanhenemiselle.

## Asetukset {#config}

**Asenna laiteohjelmisto.** Käytä [verkkoflasheria](https://flasher.meshcore.io) ja valitse
levyllesi **Repeater**-laiteohjelmisto. Asennuksen vaiheet löydät sivulta
[Aloita tästä](/get-started/#flash).

**Määritä USB:n kautta.** Pidä toistin yhä kytkettynä tietokoneeseen ja
avaa [config.meshcore.io](https://config.meshcore.io) tai flasherin
konsoli. Voit käyttää myös mitä tahansa sarjapääteohjelmaa nopeudella 115200 baudia. Tärkeimmät
komennot:

| Mitä | Komento |
|---|---|
| Vaihda ylläpitäjän salasana | `password <new password>` |
| Anna nimi | `set name <name>` |
| Radion esiasetus: taajuus, kaistanleveys, SF, CR (voimaan uudelleenkäynnistyksen jälkeen) | `set radio 869.618,62.5,8,8` |
| Käyttöasteen raja prosentteina | `set dutycycle 10` |
| Radiopiirin lähetysteho dBm:inä | `set tx <dBm>` |
| Sijainti, jotta toistin näkyy kartoilla | `set lat <degrees>` ja `set lon <degrees>` |
| Yhteystiedot muille ylläpitäjille | `set owner.info <text>` |
| Tunnit flood-ilmoitusten välillä (koko mesh kuulee ne) | `set flood.advert.interval <hours>` |
| Ilmoita toistimesta heti | `advert` |
| Käynnistä uudelleen | `reboot` |

Ylläpitäjän oletussalasana on `password`, ja jokainen sillä kirjautuva
saa ylläpitäjän oikeudet. Vaihda se, ennen kuin toistin alkaa lähettää.

Yllä oleva `set radio` -esimerkki on EU/UK (Narrow). Käytä sen sijaan alueesi
esiasetuksen arvoja: [Suositellut asetukset](/guides/settings/) listaa ne
maittain.

**Aseta kello.** Ilman kellomoduulia (RTC) toistin kadottaa ajan
jokaisessa sähkökatkossa ja käynnistyy toukokuun 2024 päivämäärällä. Käynnissä ollessaan sen kello myös
ryömii: se edistää tai jätättää yhä enemmän. Aseta siis kello silloin tällöin: kirjaudu
etänä sovelluksesta ja käytä komentoa `clock sync`, tai aseta aika USB:n kautta. Jos
toistimessa on RTC-moduuli, sinun tarvitsee tehdä tätä harvoin: moduuli pitää ajan sähkökatkojen yli ja
ryömii paljon vähemmän.

**Hallitse etänä.** Kun toistin on meshissä, kirjaudu sille MeshCore-sovelluksesta
ylläpitäjän salasanalla. Sovelluksessa näet sen tilan ja voit antaa samat komennot
radion kautta. Jotkin komennot toimivat vain USB:n kautta, kuten `set freq` ja
tehdasasetusten palautus `erase`.

**Säilytä identiteetti.** Kirjoita ennen tyhjennystä USB:n kautta `get prv.key` ja tallenna
sen näyttämä yksityinen avain turvalliseen paikkaan. Tyhjennyksen jälkeen `set prv.key <key>`
ja `reboot` palauttavat toistimelle sen vanhan identiteetin. Silloin sen tuntevat solmut
löytävät sen saman etuliitteen alta.

Koko komentoluettelo on
[MeshCoren CLI-ohjeessa](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Päivitä langattomasti {#update}

Kun toistin on paikallaan korkealla, päivität sen maasta käsin. Kirjaudu
MeshCore-sovelluksesta ylläpitäjän salasanalla, avaa toistimen komentorivi ja kirjoita
`start ota`. Jatko riippuu levystä. Muut levyt vastaavat `Error`,
ja ne päivität USB:n kautta.

**nRF52-levyt**, kuten RAK, Heltec T114, Seeed XIAO ja SenseCAP Solar:

1. Lataa levysi uuden laiteohjelmiston **ZIP**-tiedosto
   [verkkoflasherista](https://flasher.meshcore.io).
2. Kirjoita `start ota`. Toistin vastaa `OK` ja näkyy Bluetoothissa
   nimellä `<board>_OTA`, esimerkiksi `RAK4631_OTA`.
3. Avaa puhelimessa nRF Device Firmware Update -sovellus, valitse ZIP-tiedosto ja
   toistin ja lähetä päivitys. Se kestää muutaman minuutin.

Asenna nRF52-levylle [OTAFIX-käynnistyslatain](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX),
ennen kuin viet levyn ylös. Alkuperäisellä käynnistyslataimella epäonnistuneen
päivityksen voi korjata vain USB:n kautta. OTAFIXin kanssa levy palaa
päivitystilaan, ja voit yrittää uudelleen Bluetoothin kautta.

**ESP32-levyt**, kuten Heltec V3 ja V4:

1. Lataa verkkoflasherista levysi **non-merged** `.bin` -tiedosto:
   se tiedosto, jonka nimessä ei ole sanaa "merged".
2. Kirjoita `start ota`. Toistin avaa WiFi-verkon nimeltä `MeshCore-OTA`
   ja vastaa lataussivunsa osoitteella.
3. Yhdistä WiFi-kantaman sisällä puhelimesi tai kannettavasi tähän verkkoon, avaa
   osoite ja lähetä tiedosto.

## Lailliset rajat {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
MeshCoren eurooppalaiset esiasetukset sijaitsevat alikaistalla **869.40-869.65 MHz**. EU:ssa,
Isossa-Britanniassa, Sveitsissä ja Norjassa lyhyen kantaman laitteet saavat käyttää sitä ilman
lupaa näissä rajoissa:

- säteilyteho enintään **500 mW e.r.p.**;
- käyttöaste (duty cycle) enintään **10 %**: enintään 360 sekuntia lähetystä
  tunnissa laitetta kohden. Vaihtoehtoisesti laite voi käyttää kuuntele ennen lähetystä -menettelyä
  ja mukautuvaa taajuusketteryyttä standardin ETSI EN 300 220-2 mukaisesti;
- koko signaalin, enintään 250 kHz leveän, on pysyttävä alikaistan sisällä.

Kaista on jaettu: et saa häiritä luvanvaraisia palveluja, ja muut voivat
häiritä sinua.
Radiossa on oltava CE-merkintä (Isossa-Britanniassa CE tai UKCA).
{{< /callout >}}

Lähteet: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
liite 1, kaista h1.7;
[Komission päätös 2006/771/EY](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
ja sen muutokset;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
kaista O.

### Teho: e.r.p. ja antennisi {#erp}

Raja koskee *säteilytehoa*, joka mitataan suhteessa yksinkertaiseen dipoliantenniin
(e.r.p.). Antennin vahvistus lasketaan mukaan, kaapelihäviö vähennetään. Valmistajat
ilmoittavat antennin vahvistuksen dBi:nä. Se on 2.15 dB enemmän kuin sama vahvistus dBd:nä
(suhteessa dipoliin). Pidä tämä summa enintään 27 dBm:ssä (500 mW):

> lähetysteho (dBm) + antennin vahvistus (dBi) − kaapelihäviö (dB) − 2.15 ≤ 27

- Levy lähettää 22 dBm 5 dBi:n antenniin 1 dB:n kaapelihäviön kautta:
  22 + 5 − 1 − 2.15 = 23.85 dBm, noin 240 mW e.r.p. Rajan sisällä.
- Levyssä on 30 dBm:n (1 W) vahvistin ja 3 dBi:n antenni:
  30 + 3 − 2.15 = 30.85 dBm, noin 1.2 W e.r.p. Yli rajan. Laske
  lähetystehoa.

`set tx` asettaa LoRa-piirin lähtötehon dBm:inä. SX1262-piiri itse
yltää enintään 22 dBm:iin. Laiteohjelmisto ei tarkista antamaasi lukua. Levyt, joissa on lisävahvistin,
kuten Heltec V4 tai Station G2, lähettävät paljon enemmän kuin
asettamasi luku. Tarkista valmistajan taulukko, ennen kuin asetat arvon, ja
aloita pienestä.

### Käyttöaste {#duty-cycle}

Toistin lähettää kaikille ympärillään, joten se kuluttaa lähetysaikansa nopeammin
kuin companion. MeshCoren käyttöasteen rajoitin on oletuksena 50 %, mikä on
enemmän kuin tällä kaistalla saa. Aseta se 10 %:iin jokaisessa toistimessa:

```text
set dutycycle 10
```

### Taajuuden tarkkuus {#frequency}

EU/UK (Narrow) -kanava, 869.618 MHz ja kaistanleveys 62.5 kHz, ulottuu 869.649 MHz:iin asti. Se on alle 1 kHz alikaistan ylärajan alapuolella. Signaalin on pysyttävä kaistan sisällä kaikissa lämpötiloissa. Siihen tarvitaan lämpötilakompensoitu kide (TCXO). Lähes jokaisessa nykyisessä levyssä on sellainen. Vanhemmat levyt ilman sitä, kuten Heltec V2, ryömivät liian kauas. Ne eivät toimi luotettavasti 62.5 kHz:n kaistanleveydellä.

### Maakohtaiset huomiot {#countries}

- **EU:n jäsenvaltioiden** on asetettava tämä alikaista saataville näillä ehdoilla
  (päätös 2006/771/EY, 3 artikla).
- **Iso-Britannia:** samat rajat, Ofcomin määräyksessä
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Sveitsi ja Liechtenstein:** samat rajat, OFCOMin määräyksessä
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norja:** samat rajat,
  [yleisluvista annetussa asetuksessa](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Nämä huomiot eivät ole oikeudellista neuvontaa. Säännöt muuttuvat. Jos olet epävarma, tarkista asia
kansalliselta viranomaiselta.

## Käyttöönoton tarkistuslista {#checklist}

- [ ] Paikan omistaja on suostunut, ja pääset toistimelle huoltoa varten.
- [ ] Levyllä on **Repeater**-laiteohjelmisto, ja antenni kytkettiin
      ennen ensimmäistä käynnistystä.
- [ ] Ylläpitäjän salasana on vaihdettu.
- [ ] Radio vastaa [alueesi esiasetusta](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` on asetettu.
- [ ] Lähetysteho ja antennin vahvistus pysyvät yhdessä 500 mW e.r.p. -rajan sisällä.
- [ ] Nimi, sijainti ja `owner.info` on asetettu, jotta muut tietävät, kuka toistinta ylläpitää.
- [ ] Kello on asetettu (`clock`).
- [ ] Kotelo on tiivis, siinä on vedenpoisto- tai tuuletusreikä, ja kaapelissa on
      tippalenkki.
- [ ] Akku ja paneeli on mitoitettu talven huonoimman kuukauden mukaan.
- [ ] Testasit toistimen sovelluksella kauempaa ennen kuin lähdit paikalta.
- [ ] Paikallinen ryhmäsi tietää, että toistin on toiminnassa.
