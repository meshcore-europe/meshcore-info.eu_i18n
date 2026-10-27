---
title: Osallistu
lead: Vapaaehtoiset kirjoittavat, tarkistavat ja kääntävät tämän oppaan. Näin voit auttaa, GitHub-tilillä tai ilman.
description: Lisää yhteisösi, laite tai projekti, tarkista käännös tai paranna opasta sivustolla meshcore-info.eu.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-26'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
---

Kaikki tämän sivuston sisältö on julkisessa
[GitHub-tietovarastossa](https://github.com/meshcore-europe/meshcore-info.eu). Pienet muutokset
kulkevat GitHubin lomakkeen (issue) kautta. Isommat muutokset tehdään pull
requestina: se on ehdotus tiedostojen muuttamiseksi, jonka ylläpitäjä tarkistaa.
Ylläpitäjä tarkistaa jokaisen muutoksen ennen julkaisua.

Eikö sinulla ole GitHub-tiliä? Kerro asiasta [Discordissa](https://discord.meshcore-info.eu/):
puuttuva ryhmä, virheellinen tieto tai oudolta kuulostava käännös. Vapaaehtoinen
hoitaa loput.

## Lisää yhteisösi {#community}

Vedätkö paikallista MeshCore-ryhmää, johon kuka tahansa voi liittyä? Täytä
[yhteisölomake](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
ja anna nimi, alue ja julkiset linkit. Lisäämisen jälkeen ryhmäsi näkyy
[Paikalliset ryhmät](/community/) -sivulla kaikilla kielillä.

## Ehdota laitetta tai projektia {#device-project}

[Laitesivu](/devices/) listaa valmistajien dokumentaatioon perustuvat tekniset
tiedot eikä koskaan linkitä kauppoihin. Ehdota laitteistoa
[laitelomakkeella](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Oletko tehnyt MeshCorelle sovelluksen, työkalun, sillan tai laitesuunnitelman, jonka
lähdekoodi on julkinen? Lisää se
[projektilomakkeella](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Tarkista käännös {#translate}

Muunkieliset sivut syntyvät ensin konekäännöksinä, ja tämä kerrotaan sivun
yläreunassa. Käännökset ovat omassa tietovarastossaan,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), joten
sinun ei tarvitse koskea sivuston koodiin. Jos osaat jotakin kielistä hyvin,
voit parantaa käännöstä:

1. Avaa sivu ja seuraa linkkiä "Auta parantamaan tätä käännöstä". Se avaa
   tiedoston GitHubissa, jossa voit muokata sitä selaimessa.
2. Korjaa sanamuodot. Säilytä linkit, koodi, numerot ja nimet kuten MeshCore
   täsmälleen ennallaan.
3. Muuta yläreunan `translation`-lohkossa `status: ai` muotoon
   `status: human` ja ehdota muutosta.

Löysitkö väärän sanan, mutta sinulla ei ole aikaa korjata sitä? Ilmoita siitä
[käännöslomakkeella](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Paranna opasta {#guides}

Oppaat kirjoitetaan ensin englanniksi ja käännetään siitä muille kielille. Korjauksia
ja uusia aiheita voi ehdottaa
[sisältölomakkeella](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
tai pull requestilla. Tiedoilla pitää olla lähde: MeshCoren laiteohjelmisto ja sen
dokumentaatio, radioviranomainen tai valmistaja. Kirjoita omin sanoin. Lyhyt
lainaus lähteineen käy hyvin.

[Osallistujan opas](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
kertoo, miten voit työstää sivustoa omalla tietokoneellasi.

## Käännösten tila {#coverage}

"Tarkistettu" tarkoittaa, että ihminen on tarkistanut käännöksen. "Kone"
tarkoittaa konekäännöstä, jota ei ole vielä tarkistettu. "Vanhentunut"
tarkoittaa, että englanninkielinen teksti on muuttunut käännöksen jälkeen.
"Puuttuu" tarkoittaa, ettei sivulla ole vielä käännöstä.

{{< coverage >}}

## Tekijät {#credits}

Sivusto on rakennettu [Astrolla](https://astro.build/). Se käyttää kirjasimia
IBM Plex Sans ja IBM Plex Mono SIL Open Font License -lisenssillä. Käännökset
noudattavat
[kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n)-projektin käytäntöjä ja
käyttävät sen MeshCore-sanastoja. MeshCorea itseään kehitetään osoitteessa
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Tekstit ja käännökset on lisensoitu CC BY 4.0 -lisenssillä, koodi MIT-lisenssillä.
