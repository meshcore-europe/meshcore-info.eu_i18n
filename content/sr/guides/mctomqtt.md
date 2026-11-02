---
title: Napravi konfiguraciju za most
lead: 'Šalji ono što tvoj repetitor čuje na bilo koji MQTT broker: svoj ili Analyzerov. Slanje obavlja računar pored repetitora.'
description: Pokreni meshcoretomqtt na Raspberry Pi-ju ili drugom računaru i šalji ono što MeshCore repetitor čuje preko USB-a na svoj MQTT broker, na MeshCore Analyzer ili na oba.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Repetitor je čvor koji prosleđuje poruke. Želiš da se njegov saobraćaj nađe na
MQTT brokeru: na svom, za kontrolnu tablu ili bazu podataka, ili na brokeru
servisa [MeshCore Analyzer](https://meshcore-analyzer.eu/). Ili tvoj repetitor
nema svoj Wi-Fi, ali pored njega stoji Raspberry Pi ili server.
Most je [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), alat iz
zajednice: on šalje saobraćaj s tog računara. Tvoj repetitor nastavlja da
prosleđuje poruke, jer most samo čita ono što repetitor beleži preko USB-a.

## Šta ti treba {#need}

- Repetitor čiji je firmver kompajliran s beleženjem paketa (vidi ispod).
- Raspberry Pi Zero, 2, 3 ili 4, ili bilo koji Linux ili macOS računar, s
  Pythonom 3.11 ili novijim.
- USB kabl za prenos podataka između ta dva uređaja.

Standardni firmver za repetitor iz flešera ne beleži pakete. Sam kompajliraj
firmver za repetitor iz
[izvornog koda projekta MeshCore](https://github.com/meshcore-dev/MeshCore) i u
build za svoju ploču dodaj ovu zastavicu:

```text
-D MESH_PACKET_LOGGING=1
```

## Instalacija {#install}

Priključi repetitor na računar, a zatim na tom računaru pokreni instalacionu
skriptu alata meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skripta instalira most kao servis koji se pokreće zajedno s računarom i pita te
na koje brokere da šalje. Analyzer nije na tom spisku, pa ga dodaješ u
konfiguracionom fajlu ispod. Tvoja podešavanja nalaze se u
`/etc/mctomqtt/config.d/99-user.toml`, a ažuriranje nikad ne prepisuje taj fajl.

## Brokeri {#brokers}

Svaki broker dobija svoj blok `[[broker]]`, pa jedan repetitor može istovremeno
da šalje podatke na više njih. Za svoj broker koristiš korisničko ime i lozinku
ili se uopšte ne prijavljuješ (`method = "none"`).
MeshCore Analyzer umesto toga traži token, koji potpisuje ključ tvog repetitora:

- adresa `mqtt.meshcore-analyzer.eu`, port `443`, preko bezbednog websocketa;
- audience tokena je ta ista adresa.

## Tvoj konfiguracioni fajl {#config}

Zameni sadržaj fajla `/etc/mctomqtt/config.d/99-user.toml` ovim tekstom. Upiši
kod aerodroma najbližeg svom repetitoru (na primer `AMS`) i USB port na kom je
repetitor. Zatim dodaj svoj broker. Izostavi blok koji ti ne treba.

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

Posle svake izmene ponovo pokreni servis (`sudo systemctl restart mctomqtt` na
Linuxu). Tvoj repetitor se tada pojavljuje na Analyzeru kao posmatrač (observer),
čvor koji otprema ono što čuje, i to pod svojim imenom. Sva ostala
podešavanja naći ćeš u fajlu
[meshcoretomqtt README](https://github.com/Cisien/meshcoretomqtt).
