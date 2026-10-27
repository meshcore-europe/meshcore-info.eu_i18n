---
title: Rakenna siltakokoonpano
lead: 'Lähetä se, mitä toistimesi kuulee, mihin tahansa MQTT-välittäjään: omaasi tai Analyzeriin. Lähettämisen hoitaa toistimen vieressä oleva tietokone.'
description: Aja meshcoretomqtt Raspberry Pillä tai muulla tietokoneella ja lähetä se, mitä MeshCore-toistin kuulee USB:n kautta, omaan MQTT-välittäjääsi, MeshCore Analyzeriin tai molempiin.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-26'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
---

Toistin on solmu, joka välittää viestejä eteenpäin. Haluat sen liikenteen MQTT-välittäjään: omaasi koontinäyttöä tai tietokantaa varten, tai [MeshCore Analyzerin](https://meshcore-analyzer.eu/) välittäjään. Tai toistimellasi ei ole omaa Wi-Fiä, mutta sen vieressä on Raspberry Pi tai palvelin. Yhteisön työkalu [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) toimii siltana: se lähettää liikenteen tuolta tietokoneelta. Toistimesi jatkaa toistamista, koska silta vain lukee sen USB:n kautta kirjaamat lokit.

## Mitä tarvitset {#need}

- Toistin, jonka laiteohjelmistoon on käännetty pakettiloki (ohje alla).
- Raspberry Pi Zero, 2, 3 tai 4, tai mikä tahansa Linux- tai macOS-tietokone, jossa on Python 3.11 tai uudempi.
- USB-datakaapeli näiden välille.

Flasherin vakiomuotoinen toistimen laiteohjelmisto ei kirjaa paketteja. Käännä toistimen laiteohjelmisto itse [MeshCoren lähdekoodista](https://github.com/meshcore-dev/MeshCore) ja lisää levysi käännökseen tämä lippu:

```text
-D MESH_PACKET_LOGGING=1
```

## Asennus {#install}

Kytke toistin tietokoneeseen ja aja sitten meshcoretomqtt:n asennusskripti sillä tietokoneella:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skripti asentaa sillan palveluksi, joka käynnistyy tietokoneen mukana, ja kysyy, mihin välittäjiin lähetetään. Analyzer ei ole tuossa listassa; lisäät sen alla olevaan asetustiedostoon. Omat asetuksesi ovat tiedostossa `/etc/mctomqtt/config.d/99-user.toml`; päivitys ei koskaan ylikirjoita sitä.

## Välittäjät {#brokers}

Jokainen välittäjä saa oman `[[broker]]`-lohkonsa, joten yksi toistin voi syöttää useaa välittäjää samaan aikaan. Oma välittäjäsi käyttää käyttäjätunnusta ja salasanaa tai ei kirjautumista lainkaan (`method = "none"`). MeshCore Analyzer käyttää sen sijaan tokenia, jonka toistimesi avain allekirjoittaa:

- osoite `mqtt.meshcore-analyzer.eu`, portti `443`, suojatun websocketin yli;
- tokenin yleisö (audience) on sama osoite.

## Asetustiedostosi {#config}

Korvaa tiedoston `/etc/mctomqtt/config.d/99-user.toml` sisältö tällä. Täytä toistintasi lähimmän lentoaseman koodi (esimerkiksi `AMS`) ja USB-portti, jossa toistimesi on. Lisää sitten oma välittäjäsi. Jätä pois lohko, jota et tarvitse.

```toml
[general]
iata = "AMS"

[serial]
ports = ["/dev/ttyACM0"]

# Your own broker
[[broker]]
name = "my-broker"
enabled = true
server = "mqtt.example.org"
port = 1883

[broker.auth]
method = "password"
username = "my_username"
password = "my_password"

# The MeshCore Analyzer
[[broker]]
name = "meshcore-analyzer"
enabled = true
server = "mqtt.meshcore-analyzer.eu"
port = 443
transport = "websockets"

[broker.tls]
enabled = true
verify = true

[broker.auth]
method = "token"
audience = "mqtt.meshcore-analyzer.eu"
```

Käynnistä palvelu uudelleen muutoksen jälkeen (Linuxissa `sudo systemctl restart mctomqtt`). Toistimesi näkyy sen jälkeen Analyzerissa tarkkailijana, eli solmuna, joka lähettää kuulemansa palveluun, toistimesi omalla nimellä. Kaikki muut asetukset löydät [meshcoretomqtt:n README-tiedostosta](https://github.com/Cisien/meshcoretomqtt).
