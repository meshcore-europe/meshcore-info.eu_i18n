---
title: Rakenna sillan asetukset
lead: 'Lähetä toistimesi kuulema liikenne mihin tahansa MQTT-välittäjään: omaasi tai Analyzeriin. Lähettämisen hoitaa toistimen vieressä oleva tietokone.'
description: Aja meshcoretomqtt-työkalua Raspberry Pi:llä tai muulla tietokoneella. Se lähettää USB:n kautta sen, minkä MeshCore-toistin kuulee, omaan MQTT-välittäjääsi, MeshCore Analyzeriin tai molempiin.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-31'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Toistin on solmu, joka välittää viestejä eteenpäin. Haluat sen liikenteen MQTT-välittäjään:
omaasi koontinäkymää tai tietokantaa varten, tai
[MeshCore Analyzerin](https://meshcore-analyzer.eu/) välittäjään. Tai toistimessasi ei
ole omaa Wi-Fi-yhteyttä, mutta sen vieressä on Raspberry Pi tai palvelin.
Yhteisön työkalu [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt)
on silta: se lähettää liikenteen tuolta tietokoneelta. Toistimesi jatkaa
toistamista, koska silta ainoastaan lukee sen, mitä toistin kirjaa USB:n kautta.

## Mitä tarvitset {#need}

- Toistimen, jossa on pakettien kirjaus käytössä (katso alta).
- Raspberry Pi Zeron, 2:n, 3:n tai 4:n tai minkä tahansa Linux- tai macOS-tietokoneen,
  jossa on Python 3.11 tai uudempi.
- USB-datakaapelin näiden kahden välille.

Flasherin tavallinen toistimen laiteohjelmisto ei kirjaa paketteja. Käännä
toistimen laiteohjelmisto itse
[MeshCoren lähdekoodista](https://github.com/meshcore-dev/MeshCore). Lisää
tämä lippu laitteesi käännösasetuksiin:

```text
-D MESH_PACKET_LOGGING=1
```

## Asennus {#install}

Kytke toistin tietokoneeseen. Aja sitten meshcoretomqtt-työkalun asennusskripti
samalla tietokoneella:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skripti asentaa sillan palveluksi, joka käynnistyy tietokoneen mukana. Se myös kysyy,
mihin välittäjiin liikenne lähetetään. Analyzer ei ole tällä listalla: lisäät sen
alla olevaan asetustiedostoon. Omat asetuksesi ovat tiedostossa
`/etc/mctomqtt/config.d/99-user.toml`. Päivitys ei koskaan korvaa tätä tiedostoa.

## Välittäjät {#brokers}

Jokainen välittäjä saa oman `[[broker]]`-lohkonsa, joten yksi toistin voi syöttää
useaan välittäjään samaan aikaan. Omaan välittäjääsi kirjaudut käyttäjätunnuksella ja salasanalla,
tai kirjautumista ei tarvita lainkaan (`method = "none"`).
MeshCore Analyzer käyttää sen sijaan tunnistetta, jonka toistimesi avain allekirjoittaa:

- osoite `mqtt.meshcore-analyzer.eu`, portti `443`, suojatun websocket-yhteyden kautta;
- tunnisteen yleisö (audience) on sama osoite.

## Asetustiedostosi {#config}

Korvaa tiedoston `/etc/mctomqtt/config.d/99-user.toml` sisältö tällä. Kirjoita
siihen toistintasi lähimmän lentokentän koodi (esimerkiksi `AMS`) ja USB-portti, jossa
toistimesi on. Lisää sitten oma välittäjäsi. Jätä pois lohko, jota et
tarvitse.

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

Käynnistä palvelu uudelleen muutoksen jälkeen (Linuxissa `sudo systemctl restart mctomqtt`).
Sen jälkeen toistimesi näkyy Analyzerissa omalla nimellään tarkkailijana
(observer). Tarkkailija on solmu, joka lataa kuulemansa liikenteen palvelimelle.
[meshcoretomqtt-työkalun README-tiedostossa](https://github.com/Cisien/meshcoretomqtt)
ovat kaikki muut asetukset.
