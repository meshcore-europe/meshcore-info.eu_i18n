---
title: Koosta silla seadistus
lead: 'Saada see, mida su repiiter kuuleb, ükskõik millisele MQTT-vahendajale: enda omale või Analyzerile. Saatmise teeb ära repiiteri kõrval olev arvuti.'
description: Käita meshcoretomqtt-i Raspberry Pi-s või muus arvutis ja saada see, mida MeshCore'i repiiter USB kaudu kuuleb, oma MQTT-vahendajale, MeshCore Analyzerile või mõlemale.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Repiiter on sõlm, mis saadab sõnumeid edasi. Tahad selle liiklust saata MQTT-vahendajasse:
enda omasse juhtpaneeli või andmebaasi jaoks või
[MeshCore Analyzeri](https://meshcore-analyzer.eu/) omasse. Või pole su repiiteril
oma Wi-Fi-t, aga selle kõrval on Raspberry Pi või server.
Kogukonna tööriist [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt)
on sild: see saadab liikluse sellest arvutist edasi. Su repiiter jätkab sõnumite edastamist,
sest sild ainult loeb seda, mida repiiter USB kaudu logib.

## Mida sul vaja on {#need}

- Pakettide logimisega ehitatud repiiterit (vaata allpool).
- Raspberry Pi Zero, 2, 3 või 4 või ükskõik millist Linuxi või macOS-i arvutit,
  millel on Python 3.11 või uuem.
- USB-andmekaablit nende kahe vahel.

Püsivara paigaldustööriista tavaline repiiteri püsivara pakette ei logi. Ehita
repiiteri püsivara ise [MeshCore'i lähtekoodist](https://github.com/meshcore-dev/MeshCore)
ja lisa oma plaadi ehitusseadetesse see lipp:

```text
-D MESH_PACKET_LOGGING=1
```

## Paigaldamine {#install}

Ühenda repiiter arvutiga ja käivita selles arvutis meshcoretomqtt-i paigaldusskript:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skript paigaldab silla teenusena, mis käivitub koos arvutiga. Samuti küsib see,
millistele vahendajatele liiklust saata. Analyzerit selles loendis ei ole; selle lisad
allpool olevasse seadistusfaili. Sinu enda seaded on failis
`/etc/mctomqtt/config.d/99-user.toml`; uuendus ei kirjuta seda faili kunagi üle.

## Vahendajad {#brokers}

Igal vahendajal on oma `[[broker]]`-plokk, nii et üks repiiter saab saata liiklust mitmele
korraga. Oma vahendaja jaoks määrad kasutajanime ja parooli või jätad
sisselogimise üldse ära (`method = "none"`).
MeshCore Analyzer nõuab selle asemel tõendit, mille allkirjastab su repiiteri võti:

- aadress `mqtt.meshcore-analyzer.eu`, port `443`, turvalise websocketi kaudu;
- tõendi adressaat on sama aadress.

## Sinu seadistusfail {#config}

Asenda faili `/etc/mctomqtt/config.d/99-user.toml` sisu järgmisega. Kirjuta sinna
repiiterile lähima lennujaama kood (näiteks `AMS`) ja USB-port, mille küljes
repiiter on. Seejärel lisa oma vahendaja. Jäta välja plokk, mida sul vaja pole.

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

Pärast muudatust taaskäivita teenus (Linuxis `sudo systemctl restart mctomqtt`).
Seejärel ilmub su repiiter Analyzeris oma nime all vaatlejana. Vaatleja on sõlm,
mis laadib üles selle, mida ta kuuleb. Kõik ülejäänud seaded leiad
[meshcoretomqtt-i README-st](https://github.com/Cisien/meshcoretomqtt).
