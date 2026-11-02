---
title: Susikurk tilto konfigūraciją
lead: 'Siųsk tai, ką girdi tavo kartotuvas, į bet kurį MQTT brokerį: savo arba Analyzer. Duomenis siunčia šalia kartotuvo esantis kompiuteris.'
description: Paleisk meshcoretomqtt Raspberry Pi ar kitame kompiuteryje ir per USB gautus MeshCore kartotuvo duomenis siųsk į savo MQTT brokerį, MeshCore Analyzer arba į abu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Kartotuvas yra mazgas, kuris perduoda žinutes toliau. Nori matyti jo srautą MQTT
brokeryje: savo, skirtame prietaisų skydeliui ar duomenų bazei, arba
[MeshCore Analyzer](https://meshcore-analyzer.eu/) brokeryje. O gal tavo kartotuvas neturi
savo Wi-Fi, bet šalia jo stovi Raspberry Pi ar serveris.
Bendruomenės įrankis [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) yra tiltas:
jis siunčia srautą iš to kompiuterio. Tavo kartotuvas ir toliau persiunčia žinutes,
nes tiltas tik skaito tai, ką kartotuvas registruoja per USB.

## Ko tau reikia {#need}

- Kartotuvo, sukompiliuoto su paketų registravimu (žr. toliau).
- Raspberry Pi Zero, 2, 3 ar 4 arba bet kurio Linux ar macOS kompiuterio su Python
  3.11 ar naujesne versija.
- USB duomenų kabelio jiems sujungti.

Standartinė kartotuvo programinė įranga iš diegimo įrankio (flasher) paketų neregistruoja.
Kartotuvo programinę įrangą susikompiliuok pats iš
[MeshCore šaltinio kodo](https://github.com/meshcore-dev/MeshCore), o savo plokštės
kompiliavimo nustatymuose pridėk šią vėliavėlę:

```text
-D MESH_PACKET_LOGGING=1
```

## Diegimas {#install}

Prijunk kartotuvą prie kompiuterio ir tame kompiuteryje paleisk meshcoretomqtt
diegimo scenarijų:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Scenarijus įdiegia tiltą kaip paslaugą, kuri pasileidžia kartu su kompiuteriu, ir paklausia,
į kuriuos brokerius siųsti duomenis. Analyzer tame sąraše nėra: jį pridėsi toliau aprašytame
konfigūracijos faile. Tavo nustatymai yra faile
`/etc/mctomqtt/config.d/99-user.toml`. Atnaujinimas šio failo niekada neperrašo.

## Brokeriai {#brokers}

Kiekvienam brokeriui skirtas atskiras `[[broker]]` blokas, todėl vienas kartotuvas gali
vienu metu siųsti duomenis į kelis brokerius. Savo brokeryje naudoji naudotojo vardą ir slaptažodį
arba visai apsieini be prisijungimo
(`method = "none"`).
MeshCore Analyzer vietoj jų naudoja žetoną, kurį pasirašo tavo kartotuvo raktas:

- adresas `mqtt.meshcore-analyzer.eu`, prievadas `443`, per saugų websocket ryšį;
- žetono auditorija (audience) yra tas pats adresas.

## Tavo konfigūracijos failas {#config}

Failo `/etc/mctomqtt/config.d/99-user.toml` turinį pakeisk šiuo tekstu. Įrašyk
arčiausiai kartotuvo esančio oro uosto kodą (pavyzdžiui, `AMS`) ir USB
prievadą, prie kurio prijungtas kartotuvas. Tada pridėk savo brokerį. Nereikalingą
bloką praleisk.

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

Po kiekvieno pakeitimo paleisk paslaugą iš naujo (Linux sistemoje `sudo systemctl restart mctomqtt`).
Tada tavo kartotuvas Analyzer svetainėje pasirodys kaip stebėtojas, t. y. mazgas, kuris
įkelia tai, ką girdi. Jis bus rodomas savo vardu. Visi kiti nustatymai aprašyti
[meshcoretomqtt README](https://github.com/Cisien/meshcoretomqtt) faile.
