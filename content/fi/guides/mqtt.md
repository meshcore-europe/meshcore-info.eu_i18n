---
title: MQTT observer-solmussasi
lead: Toistimesi raportoi kuulemansa MeshCore Analyzeriin Wi-Fin kautta. Se välittää viestejä edelleen kuten ennenkin.
description: Tee ESP32-toistimesta MeshCore-observer DMC observer -laiteohjelmistolla. Flashaa se, aseta Wi-Fi ja lentokenttäkoodisi, valitse brokerit ja tarkista, että se raportoi MeshCore Analyzeriin.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-31'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Observer on solmu, joka myös raportoi kuulemansa MQTT:n kautta Wi-Fin yli.
Jokainen observer näyttää vähän lisää meshistä
[MeshCore Analyzerissa](https://meshcore-analyzer.eu/) ja
[kuuluvuuskartoilla](/map/). Tällä ohjeella teet toistimesta (solmusta, joka
välittää viestejä eteenpäin) observerin. Se toistaa viestejä edelleen.
Raportti kulkee vain yhteen suuntaan: meshiin ei palaa mitään.

{{< callout type="warning" >}}
Tämä ohje koskee **DMC observer -laiteohjelmistoa**. Se on
[Dutch-MeshCoren](https://github.com/Dutch-MeshCore/MeshCore) observer-versio,
joka perustuu MeshCore 1.18.0:aan. Tavallisessa MeshCoressa ei ole MQTT:tä.
Kaikki alla olevat komennot on luettu laiteohjelmiston lähdekoodista, versiosta
`32dd8ad` 19. lokakuuta 2026.
{{< /callout >}}

## Mitä tarvitset {#need}

- ESP32-kortti, jossa on Wi-Fi, esimerkiksi Heltec V3 tai V4, LilyGo T3S3 tai
  Xiao S3. Kaikki kortit löydät [julkaisusta](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev).
  nRF52-korteissa, kuten RAK4631:ssä, ei ole Wi-Fiä.
- 2.4 GHz:n Wi-Fi-verkko kortin sijaintipaikassa.
- USB-datakaapeli sekä Chrome, Edge tai Opera tietokoneellasi.
- Solmuasi lähimmän lentokentän koodi, 3 kirjainta, kuten `AMS` tai `BRU`.
  Koodista brokerit (palvelimet, jotka vastaanottavat raporttisi) näkevät,
  millä alueella observerisi on.

Eikö toistimesi luona ole Wi-Fiä, mutta sen vieressä on tietokone?
[Rakenna silloin siltamääritys](/guides/mctomqtt/).

## Laiteohjelmiston flashaus {#flash}

Tämän sivuston [flasherissa](/firmware/flasher/) on vain tavallinen MeshCore.
Observer-laiteohjelmiston saat [DutchMeshCore Toolboxin](https://toolbox.dutchmeshcore.nl/)
flasherista:

1. Valitse korttisi ja sitten **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Valitse ensimmäisellä kerralla **Full flash**: se korvaa kaiken kortilla,
   myös osiotaulun. App update säilyttää nykyisen sisällön, ja se on
   myöhempiä päivityksiä varten.
3. Määritä toistin tavalliseen tapaan: nimi, radioasetus ja ylläpitäjän
   salasana, kuten [toistinohjeessa](/repeater-guide/#config).

Tämä laiteohjelmisto on **dev**-versio. Kun kirjoitat `ota update`, se
päivittyy dev-kanavalta. Vakaalla kanavalla on yhä 1.17.1, joten pysy tässä
ohjeessa dev-kanavalla.

## Asetukset {#settings}

Avaa tämän sivuston [sarjakonsoli](/firmware/console/) ja yhdistä korttisi.
Täytä oman Wi-Fi-verkkosi nimi, salasana ja lentokenttäkoodi. Liitä sitten
nämä rivit yksi kerrallaan:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Uudelleenkäynnistyksen jälkeen kortti liittyy Wi-Fi-verkkoosi ja hakee
kellonajan internetistä. Brokerit tarvitsevat kellonajan tunnistaakseen
observerisi. Ilman lentokenttäkoodia mitään ei raportoida.

Napsautatko mieluummin kuin kirjoitat? `start webconfig` avaa kortille
asetussivun osoitteessa, jonka konsoli näyttää. Kirjaudu sisään ylläpitäjän
salasanalla.

## Broker-paikat {#brokers}

Yhteen paikkaan mahtuu yksi broker. Laiteohjelmistossa nämä paikat ovat
valmiiksi täytettyinä:

| Paikka | Broker | Ylläpitäjä |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Kortissa ilman lisämuistia (PSRAM), kuten Heltec V3:ssa, on 3 paikkaa. Se
yhdistää 2:een niistä kerrallaan, joten paikan 3 Analyzer ei koskaan
yhdisty. Siirrä se paikkaan 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

PSRAM-kortissa, kuten Heltec V4:ssä, on 6 paikkaa, ja se yhdistää 5:een
kerrallaan. Siihen ei tarvitse tehdä muutoksia.

Solmusi kirjautuu jokaiseen brokeriin omalla avaimellaan, joten et tarvitse
tiliä. `get mqtt.presets` listaa muut yhteisön brokerit, jotka
laiteohjelmisto tuntee.

### Oma broker {#own}

Laita oma brokerisi vapaaseen paikkaan. Täytä sen osoite, portti,
käyttäjätunnus ja salasana. PSRAM-kortissa paikka 4 on vapaa:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Kortissa ilman PSRAMia käytä sen sijaan paikkaa 2: vaihda `mqtt4` tilalle
`mqtt2`. Brokerisi tulee silloin `dutchmeshcore-2`:n paikalle.

Portti `8883` muodostaa salatun yhteyden (TLS). Portti `443` muodostaa salatun
yhteyden verkkoyhteyden (websocket) yli. Muut portit yhdistävät salaamatta.
Voit myös antaa koko osoitteen, kuten `wss://mqtt.example.org:9002/mqtt`.
Silloin porttisääntö ei ole voimassa.

## Tarkista, että se toimii {#check}

Kirjoita `get mqtt.status`. Jokaisen paikan tila näkyy:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: yhdistetty.
- `wait`: paikasta puuttuu asetus, esimerkiksi lentokenttäkoodi.
- `disc`: ei vielä yhdistetty. Tarkista Wi-Fi komennolla `get wifi.status`.
- `fail`: paikka epäonnistui 7 kertaa peräkkäin noin 20 minuutin aikana. Nyt
  se yrittää kerran 30 minuutissa. Tarkista brokerin osoite ja kirjautumistiedot.
- `inactive`: kortilla ei ole tilaa tälle paikalle. Katso
  [Broker-paikat](#brokers).

Etsi sitten toistimesi nimeä
[Analyzerin observer-sivulta](https://meshcore-analyzer.eu/#observers).
Se ilmestyy sinne 5 minuutin kuluessa kuulemiensa viestien kanssa.
