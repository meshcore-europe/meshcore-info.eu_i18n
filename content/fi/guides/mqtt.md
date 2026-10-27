---
title: MQTT havainnoijassasi
lead: Anna toistimesi raportoida kuulemansa MeshCore Analyzerille Wi-Fin kautta. Se välittää viestejä edelleen kuten ennenkin.
description: Muuta ESP32-toistin MeshCore-havainnoijaksi DMC:n havainnoijalaiteohjelmistolla. Flashaa se, aseta Wi-Fi ja lentokenttäkoodisi, valitse välittäjät ja tarkista, että se raportoi MeshCore Analyzerille.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-26'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
---

Havainnoija on solmu, joka myös raportoi kuulemansa MQTT:llä Wi-Fin
kautta. Jokainen havainnoija näyttää hieman enemmän meshistä
[MeshCore Analyzerissa](https://meshcore-analyzer.eu/) ja
[kuuluvuuskartoilla](/map/). Tämä opas muuttaa toistimen (solmun, joka
välittää viestejä eteenpäin) havainnoijaksi. Se jatkaa toistamista, ja
raportti kulkee vain yhteen suuntaan: meshiin ei palaa mitään.

{{< callout type="warning" >}}
Tämä opas koskee **DMC:n havainnoijalaiteohjelmistoa**, eli
[Dutch-MeshCoren](https://github.com/Dutch-MeshCore/MeshCore) havainnoijaversiota,
joka perustuu MeshCore 1.18.0:aan. Vakio-MeshCoressa ei ole MQTT:tä. Jokainen
alla oleva komento on luettu laiteohjelmiston lähdekoodista, koontiversiosta
`32dd8ad` 19. lokakuuta 2026.
{{< /callout >}}

## Mitä tarvitset {#need}

- ESP32-levyn, jossa on Wi-Fi, kuten Heltec V3 tai V4, LilyGo T3S3 tai
  Xiao S3. [Julkaisu](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  luettelee kaikki levyt. nRF52-levyissä, kuten RAK4631:ssä, ei ole Wi-Fiä.
- 2.4 GHz:n Wi-Fi-verkon siellä, missä levy sijaitsee.
- USB-datakaapelin sekä Chromen, Edgen tai Operan tietokoneellasi.
- Solmuasi lähimmän lentokentän koodin, 3 kirjainta, kuten `AMS` tai `BRU`.
  Se kertoo välittäjille (palvelimille, jotka vastaanottavat raporttisi),
  millä alueella havainnoijasi on.

Eikö toistimesi sijainnissa ole Wi-Fiä, mutta sen vieressä on tietokone?
[Rakenna sen sijaan siltakokoonpano](/guides/mctomqtt/).

## Flashaa laiteohjelmisto {#flash}

Tämän sivuston [flashaustyökalu](/firmware/flasher/) sisältää vain vakio-MeshCoren.
Havainnoijalaiteohjelmiston saat
[DutchMeshCore Toolboxin](https://toolbox.dutchmeshcore.nl/) flashaustyökalusta:

1. Valitse levysi ja sitten **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Valitse ensimmäisellä kerralla **Full flash**: se korvaa kaiken levyllä,
   myös osiotaulun. Sovelluspäivitys säilyttää levyn sisällön ja on
   tarkoitettu myöhempiin päivityksiin.
3. Määritä toistimesi tavalliseen tapaan: nimi, radioesiasetus ja
   ylläpitäjän salasana, kuten [toistinoppaassa](/repeater-guide/#config).

Tämä laiteohjelmisto on **dev**-koontiversio ja päivittää itsensä
dev-kanavalta, kun kirjoitat `ota update`. Vakaa kanava tarjoaa yhä
versiota 1.17.1, joten pysy tätä opasta varten dev-kanavalla.

## Asetukset {#settings}

Avaa tämän sivuston [sarjakonsoli](/firmware/console/) ja yhdistä levysi.
Täytä oma Wi-Fi-verkkosi, salasanasi ja lentokenttäkoodisi ja liitä sitten
nämä rivit yksi kerrallaan:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Uudelleenkäynnistyksen jälkeen levy liittyy Wi-Fiisi ja asettaa kellonsa
internetistä. Välittäjät tarvitsevat tuon kellon tarkistaakseen, kuka
havainnoijasi on. Ilman lentokenttäkoodia mitään ei raportoida.

Klikkaatko mieluummin kuin kirjoitat? `start webconfig` avaa asetussivun
levyllä, osoitteessa, jonka konsoli näyttää. Kirjaudu sisään ylläpitäjän
salasanallasi.

## Välittäjäpaikat {#brokers}

Yksi paikka sisältää yhden välittäjän. Laiteohjelmistossa nämä paikat ovat
valmiiksi täytettyinä:

| Paikka | Välittäjä | Ylläpitäjä |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Levyllä ilman lisämuistia (PSRAM), kuten Heltec V3:lla, on 3 paikkaa. Se
yhdistää niistä 2:een kerralla, joten paikassa 3 oleva Analyzer ei koskaan
yhdisty. Siirrä se paikkaan 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Levyllä, jossa on PSRAM, kuten Heltec V4:llä, on 6 paikkaa, ja se yhdistää
5:een kerralla. Siihen ei tarvita muutosta.

Solmusi kirjautuu jokaiseen välittäjään omalla avaimellaan, joten et tarvitse
tiliä. `get mqtt.presets` luettelee muut laiteohjelmiston tuntemat yhteisön
välittäjät.

### Oma välittäjäsi {#own}

Laita oma välittäjäsi vapaaseen paikkaan. Täytä sen osoite, portti,
käyttäjätunnus ja salasana. Levyllä, jossa on PSRAM, paikka 4 on vapaa:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Levyllä ilman PSRAM-muistia käytä sen sijaan paikkaa 2: korvaa `mqtt4`
arvolla `mqtt2`. Välittäjäsi tulee silloin `dutchmeshcore-2`:n tilalle.

Portti `8883` yhdistää salattuna (TLS), portti `443` salattuna
web-yhteyden kautta (websocket) ja mikä tahansa muu portti salaamattomana.
Voit antaa myös koko osoitteen, esimerkiksi `wss://mqtt.example.org:9002/mqtt`;
silloin porttisääntö ei päde.

## Tarkista, että se toimii {#check}

Kirjoita `get mqtt.status`. Jokainen paikka näyttää tilansa:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: yhdistetty.
- `wait`: paikasta puuttuu asetus, esimerkiksi lentokenttäkoodi.
- `disc`: ei vielä yhdistetty. Tarkista Wi-Fisi komennolla `get wifi.status`.
- `fail`: paikka epäonnistui 7 kertaa peräkkäin noin 20 minuutin aikana ja
  yrittää nyt kerran 30 minuutissa. Tarkista välittäjän osoite ja
  kirjautumistiedot.
- `inactive`: levyllä ei ole tilaa tälle paikalle. Katso
  [Välittäjäpaikat](#brokers).

Etsi sitten toistimesi nimi
[Analyzerin havainnoijasivulta](https://meshcore-analyzer.eu/#observers).
Se ilmestyy sinne 5 minuutin kuluessa yhdessä kuulemansa kanssa.
