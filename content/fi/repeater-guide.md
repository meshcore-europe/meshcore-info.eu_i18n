---
title: Toistinopas
lead: Korkealle sijoitettu toistin välittää viestejä kaikille ympärillään, koko kaupungin tai laakson alueella. Valitse paikka, ota virta auringosta, tee asetukset ja pysy lain rajoissa.
description: 'Suunnittele, syötä virta, määritä asetukset ja käytä MeshCore-toistinta laillisesti Euroopassa: paikan valinta, aurinkopaneelin mitoitus, CLI-asetukset, 868 MHz:n teho- ja lähetysaikarajat.'
eyebrow: 868 MHz · enintään 500 mW · ei vaadi lupaa
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '4a0fe39f'
  seeded: '2026-10-26'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['1de4a4f7', '766086be', '70faf508', '8bc641aa', '2018aa04', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
---

Toistimet kantavat meshiä. Kumppanilaitteet, eli radiot, joilla viestittelet, eivät välitä viestejä eteenpäin. Ilman toistimia tavoitat siis vain ihmiset suorassa kantamassa. Jokainen pystyttämäsi toistin laajentaa meshiä kaikille ympärillään. Tämä opas noudattaa MeshCore-laiteohjelmiston versiota v1.18.0.

Keskustele ennen aloittamista [paikallisen ryhmäsi](/community/) kanssa. He tietävät, mistä kuuluvuus puuttuu, [mitä esiasetusta alueellasi käytetään](/guides/settings/) ja miten toistimet nimetään. Katso [kuuluvuuskartoista](/map/) lähelläsi olevat toistimet ja tervehdi julkisilla tai paikallisilla [kanavilla](/guides/channels/).

## Valitse paikka {#site}

Korkeus voittaa tehon. LoRa kulkee 868 MHz:llä parhaiten esteettömällä näköyhteydellä. Mäet, rakennukset ja tiheä puusto vievät kantamaa paljon enemmän kuin muutama ylimääräinen milliwatti tuo takaisin.

- **Mene korkealle.** Katto, masto, korkea rakennus tai mäki kattaa paljon enemmän kuin ikkunalauta. Jo muutama metri ympäröivien kattojen yläpuolella auttaa.
- **Pidä antenni vapaana.** Asenna se kattojen reunojen yläpuolelle, kauas metallista, kouruista ja muista antenneista.
- **Tarkista näkymä.** Esimerkiksi [HeyWhatsThat](https://www.heywhatsthat.com/) näyttää, mitä paikasta näkyy. Jos näet jonkin kohdan, siellä oleva toistin on tavoitettavissa.
- **Jätä tilaa.** Radioreitti tarvitsee vapaata tilaa suoran linjan ympärille, ei vain linjaa itseään. Pitkillä matkoilla reitin keskikohdan pitää ylittää esteet useilla metreillä.
- **Pyydä lupa.** Hanki katon tai maston omistajan suostumus ja sovi, miten pääset toistimen luo huoltoa varten.

## Laitteisto {#hardware}

- **Piirilevy.** Valitse vähän virtaa kuluttava nRF52-piirilevy, kuten [Heltec T114](/devices/), RAK WisBlock tai SenseCAP Solar Node. ESP32-piirilevyt kuluttavat enemmän virtaa (laitesivu merkitsee ne luokkaan High), mikä tekee aurinkokäytöstä vaikeaa.
- **Antenni.** Käytä 868 MHz:lle tehtyä antennia pystyasennossa. [Antenniopas](/guides/antenna/) kertoo tyypeistä, liittimistä, kaapelista ja asennuksesta. Antennin vahvistus lasketaan mukaan lailliseen tehorajaan, katso [Lain rajat](#legal).
- **Kaapeli.** Pidä koaksiaalikaapeli lyhyenä tai käytä vähähäviöistä kaapelia. 868 MHz:llä muutama metri ohutta kaapelia voi syödä puolet tehosta.
- **Kotelo.** Säänkestävä kotelo (IP65 tai parempi), jossa on kaapeliläpivienti, tuuletus- tai vedenpoistoreikä kondenssia vastaan sekä vaalea väri tai aurinkosuoja. Akut kärsivät kuumuudesta, eikä niitä voi ladata pakkasella.
- **Salama.** Katolla oleva antenni on salaman kohde. Noudata paikallisia maadoitussääntöjä tai asenna antenni paikkaan, josta salamanisku ei pääse rakennuksen johdotukseen.

## Virta ja aurinkopaneelin mitoitus {#power}

Aurinkotoistimen on selvittävä talven pimeimmistä viikoista. Mitoita se niiden mukaan:

1. **Mittaa kulutus.** Pidä valmiiksi asetettua toistinta USB-tehomittarin takana yhden päivän. Lue käytetty energia wattitunteina (Wh). Alueesi liikenne vaikuttaa lukuun, joten mittaa paikan päällä, jos voit.
2. **Lisää varaa.** Mitoita akun kapasiteetti vähintään 5–7 päivälle ilman hyödyllistä aurinkoa.
3. **Selvitä talviaurinkosi.** EU:n ilmainen [PVGIS-työkalu](https://re.jrc.ec.europa.eu/pvg_tools/en/) näyttää mille tahansa paikalle, paljonko energiaa paneeli tuottaa kuukaudessa. Käytä kuukautta, jossa aurinkoa on vähiten.
4. **Mitoita paneeli.** Paneelin on korvattava jokaisen päivän kulutus tuossa huonoimmassa kuukaudessa, ja latauksen häviöille jää varaa.

Laskuesimerkki oletetuilla luvuilla: toistin, joka kuluttaa 1 Wh päivässä, tarvitsee vähintään 7 Wh:n akun viikon varalle, eli noin 2 Ah käyttökelpoista kapasiteettia 3.7 V:n jännitteellä. Jos PVGIS kertoo, että 1 W:n paneeli antaa paikallasi joulukuussa 0.5 Wh päivässä, tarvitset vähintään 2 W:n paneelin, ja 3–5 W jättää varaa pilville, lumelle ja ikääntymiselle.

## Ota käyttöön {#config}

**Flashaa.** Käytä [web-flasheria](https://flasher.meshcore.io) ja valitse piirilevyllesi **Repeater**-laiteohjelmisto. Flashauksen vaiheet löydät kohdasta [Aloita](/get-started/#flash).

**Määritä asetukset USB:n kautta.** Kun toistin on vielä kytkettynä tietokoneeseesi, avaa [config.meshcore.io](https://config.meshcore.io) tai flasherin konsoli. Voit käyttää myös mitä tahansa sarjaterminaalia nopeudella 115200 baudia. Tärkeimmät komennot:

| Mitä | Komento |
|---|---|
| Vaihda ylläpitäjän salasana | `password <new password>` |
| Anna nimi | `set name <name>` |
| Radion esiasetus: taajuus, kaistanleveys, SF, CR (tulee voimaan uudelleenkäynnistyksessä) | `set radio 869.618,62.5,8,8` |
| Lähetysaikaraja prosentteina | `set dutycycle 10` |
| Radiopiirin lähetysteho, dBm | `set tx <dBm>` |
| Sijainti, jotta toistin näkyy kartoilla | `set lat <degrees>` ja `set lon <degrees>` |
| Yhteystiedot muille ylläpitäjille | `set owner.info <text>` |
| Flood-ilmoitusten (koko meshin kuulemien) väli tunteina | `set flood.advert.interval <hours>` |
| Ilmoita heti | `advert` |
| Käynnistä uudelleen | `reboot` |

Ylläpitäjän oletussalasana on `password`, ja jokainen sillä kirjautuva saa ylläpitäjän oikeudet. Vaihda se ennen kuin toistin menee lähetykseen.

Edellä oleva `set radio`-esimerkki on EU/UK (Narrow). Käytä sen sijaan oman alueesi esiasetuksen arvoja: [Suositellut asetukset](/guides/settings/) listaa ne maittain.

**Aseta kello.** Ilman kellomoduulia (RTC) toistin menettää ajan jokaisessa sähkökatkossa ja sen kello palaa käynnistyessä toukokuuhun 2024. Käynnissä sen kello myös ajelehtii. Kirjaudu etänä sovelluksesta ja käytä komentoa `clock sync`, tai aseta aika USB:n kautta. RTC-moduuli on toistimeen kannattava lisä: se pitää ajan sähkökatkojen yli ja ajelehtii paljon vähemmän.

**Hallitse etänä.** Kun toistin on meshissä, kirjaudu MeshCore-sovelluksesta ylläpitäjän salasanalla. Siellä luet sen tilan ja käytät samoja komentoja radion yli. Osa komennoista toimii vain USB:n kautta, esimerkiksi `set freq` ja tehdasasetusten palautus `erase`.

Koko komentolista on [MeshCore CLI -ohjeessa](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Lain rajat {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
MeshCoren eurooppalaiset esiasetukset ovat alakaistalla **869.40–869.65 MHz**. EU:ssa, Britanniassa, Sveitsissä ja Norjassa se on avoin lyhyen kantaman laitteille ilman lupaa näissä rajoissa:

- säteilyteho enintään **500 mW e.r.p.**;
- lähetysaikaraja enintään **10 %**: korkeintaan 360 sekuntia lähetystä missä tahansa tunnissa laitetta kohti. Vaihtoehtoisesti laite voi käyttää kuuntele ennen lähetystä -menettelyä ja mukautuvaa taajuudenvaihtoa ETSI EN 300 220-2 -standardin mukaan;
- koko signaalin, enintään 250 kHz leveän, pitää pysyä alakaistan sisällä.

Kaista on jaettu: et saa häiritä luvanvaraisia palveluja, ja muut saavat häiritä sinua.
Radiossa pitää olla CE-merkintä (Isossa-Britanniassa CE tai UKCA).
{{< /callout >}}

Lähteet: [CEPT ERC -suositus 70-03](https://docdb.cept.org/document/845), liite 1, kaista h1.7;
[komission päätös 2006/771/EY](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) ja sen muutokset;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), kaista O.

### Teho: e.r.p. ja antennisi {#erp}

Raja koskee *säteiltyä* tehoa, joka mitataan suhteessa yksinkertaiseen dipoliantenniin (e.r.p.). Antennin vahvistus lasketaan mukaan, kaapelihäviö vähennetään. Valmistajat ilmoittavat antennin vahvistuksen dBi-yksikössä, joka on 2.15 dB enemmän kuin sama vahvistus dBd-yksikössä (suhteessa dipoliin). Pidä tämä summa enintään 27 dBm:ssä (500 mW):

> lähetysteho (dBm) + antennin vahvistus (dBi) − kaapelihäviö (dB) − 2.15 ≤ 27

- Piirilevy lähettää 22 dBm 5 dBi:n antenniin 1 dB:n kaapelin kautta: 22 + 5 − 1 − 2.15 = 23.85 dBm, noin 240 mW e.r.p. Rajan sisällä.
- Piirilevy, jossa on 30 dBm:n (1 W) vahvistin, 3 dBi:n antenniin: 30 + 3 − 2.15 = 30.85 dBm, noin 1.2 W e.r.p. Rajan yli, laske lähetystehoa.

`set tx` asettaa LoRa-piirin lähtötehon dBm-yksikössä. SX1262-piiri itse yltää enintään 22 dBm:iin, eikä laiteohjelmisto tarkista syöttämääsi lukua. Piirilevyt, joissa on lisävahvistin, kuten Heltec V4 tai Station G2, lähettävät paljon enemmän kuin asettamasi luku. Tarkista valmistajan taulukko ennen asettamista ja aloita pienestä.

### Lähetysaika {#duty-cycle}

Toistin lähettää kaikkien ympärillään puolesta, joten se kuluttaa lähetysaikansa nopeammin kuin kumppanilaite. MeshCoren lähetysaikarajoitin on oletuksena 50 %, mikä on enemmän kuin tämä kaista sallii. Aseta se 10 %:iin jokaisessa toistimessa:

```text
set dutycycle 10
```

### Taajuuden tarkkuus {#frequency}

EU/UK (Narrow) -kanava, 869.618 MHz ja 62.5 kHz:n kaistanleveys, ulottuu 869.649 MHz:iin asti: alle 1 kHz alakaistan yläreunan alapuolelle. Signaalin pitää pysyä kaistan sisällä kaikissa lämpötiloissa. Se vaatii lämpötilakompensoidun kiteen (TCXO). Lähes jokaisessa nykyisessä piirilevyssä on sellainen. Vanhemmat piirilevyt ilman sitä, kuten Heltec V2, ajelehtivat liikaa toimiakseen luotettavasti 62.5 kHz:llä.

### Maakohtaiset huomiot {#countries}

- **EU:n jäsenvaltioiden** on annettava tämä alakaista käyttöön näillä ehdoilla (päätös 2006/771/EY, 3 artikla).
- **Iso-Britannia:** samat rajat, Ofcomin [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Sveitsi ja Liechtenstein:** samat rajat, OFCOMin [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norja:** samat rajat, [yleisiä käyttöoikeuksia koskevassa asetuksessa](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Nämä huomiot eivät ole oikeudellista neuvontaa. Säännöt muuttuvat. Jos olet epävarma, tarkista asia kansalliselta viranomaiseltasi.

## Käyttöönoton tarkistuslista {#checklist}

- [ ] Paikan omistaja on suostunut, ja pääset toistimen luo huoltoa varten.
- [ ] Piirilevyllä on **Repeater**-laiteohjelmisto, ja antenni kiinnitettiin ennen ensimmäistä käynnistystä.
- [ ] Ylläpitäjän salasana on vaihdettu.
- [ ] Radio vastaa [alueesi esiasetusta](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` on asetettu.
- [ ] Lähetysteho ja antennin vahvistus pysyvät yhteensä 500 mW:n e.r.p.-rajassa.
- [ ] Nimi, sijainti ja `owner.info` on asetettu, jotta muut tietävät, kuka toistinta ylläpitää.
- [ ] Kello on asetettu (`clock`).
- [ ] Kotelo on tiivistetty, siinä on vedenpoisto- tai tuuletusreikä, ja kaapelissa on tippalenkki.
- [ ] Akku ja paneeli on mitoitettu huonoimman talvikuukauden mukaan.
- [ ] Testasit toistimen etäältä sovelluksella ennen paikalta lähtöä.
- [ ] Paikallinen ryhmäsi tietää, että toistin on pystyssä.
