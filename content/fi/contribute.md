---
title: Osallistu
lead: Vapaaehtoiset kirjoittavat, tarkistavat ja kääntävät tämän oppaan. Näin voit auttaa, GitHub-tilin kanssa tai ilman.
description: Lisää yhteisösi, laite tai projekti, tarkista käännös tai paranna opasta meshcore-info.eu-sivustolla.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-31'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Koko sivuston sisältö on julkisessa
[GitHub-repositoriossa](https://github.com/meshcore-europe/meshcore-info.eu). Pienet muutokset
ehdotat GitHubin lomakkeella (issue). Isommat muutokset tehdään pull
requestina: se on muutosehdotus tiedostoihin, ja ylläpitäjä tarkistaa sen.
Ylläpitäjä tarkistaa jokaisen muutoksen ennen kuin se julkaistaan.

Eikö sinulla ole GitHub-tiliä? Kerro meille [Discordissa](https://discord.meshcore-info.eu/):
puuttuva ryhmä, väärä tieto tai oudolta kuulostava käännös. Vapaaehtoinen
hoitaa asian siitä eteenpäin.

## Lisää yhteisösi {#community}

Ylläpidätkö paikallista MeshCore-ryhmää, johon kuka tahansa voi liittyä? Täytä
[yhteisölomake](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
ja kerro ryhmän nimi, alue ja julkiset linkit. Kun ryhmä on lisätty, se näkyy
[Paikalliset ryhmät](/community/) -sivulla kaikilla kielillä.

## Ehdota laitetta tai projektia {#device-project}

[Laitesivun](/devices/) tekniset tiedot ovat valmistajien dokumentaatiosta, eikä sivu koskaan linkitä kauppoihin. Ehdota laitetta
[laitelomakkeella](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Oletko tehnyt MeshCorelle sovelluksen, työkalun, sillan tai laitteistosuunnitelman, jonka lähdekoodi
on julkinen? Lisää se
[projektilomakkeella](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Tarkista käännös {#translate}

Muunkieliset sivut ovat aluksi konekäännöksiä, ja sivun yläosassa kerrotaan
siitä. Käännökset ovat omassa repositoriossaan,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), joten
sinun ei koskaan tarvitse koskea sivuston koodiin. Jos osaat jotakin kielistä
hyvin, voit parantaa käännöstä:

1. Avaa sivu ja valitse "Help improve this translation". Linkki avaa
   tiedoston GitHubissa, jossa voit muokata sitä selaimessa.
2. Korjaa sanamuodot. Jätä linkit, koodi, numerot ja nimet, kuten MeshCore,
   täsmälleen ennalleen.
3. Vaihda yläosan `translation`-lohkossa `status: ai` muotoon
   `status: human` ja ehdota muutosta.

Löysitkö väärän sanan, mutta et ehdi korjata sitä? Ilmoita siitä
[käännöslomakkeella](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Paranna opasta {#guides}

Oppaat kirjoitetaan ensin englanniksi ja käännetään siitä muille kielille. Otamme mielellämme vastaan
korjauksia ja uusia aiheita
[sisältölomakkeella](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
tai pull requestina. Tiedoilla pitää olla lähde: MeshCoren laiteohjelmisto ja sen
dokumentaatio, radiotaajuusviranomainen tai valmistaja. Kirjoita omin sanoin.
Lyhyt lainaus lähteineen on sallittu.

[Osallistujan opas](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
kertoo, miten työstät sivustoa omalla tietokoneellasi.

## Käännösten tila {#coverage}

"Reviewed" tarkoittaa, että ihminen on tarkistanut käännöksen. "Machine" tarkoittaa
konekäännöstä, jota ei ole vielä tarkistettu. "Outdated" tarkoittaa, että
englanninkielinen teksti on muuttunut käännöksen jälkeen. "Missing" tarkoittaa,
ettei sivulla ole vielä käännöstä.

{{< coverage >}}

## Tekijät {#credits}

Sivusto on tehty [Astrolla](https://astro.build/). Sivustolla käytetään
IBM Plex Sans- ja IBM Plex Mono -kirjasimia SIL Open Font License -lisenssillä. Käännökset
noudattavat
[kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n)-projektin käytäntöjä ja
käyttävät sen MeshCore-sanastoja. Itse MeshCorea kehitetään osoitteessa
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Tekstit ja käännökset on lisensoitu CC BY 4.0 -lisenssillä, koodi MIT-lisenssillä.
