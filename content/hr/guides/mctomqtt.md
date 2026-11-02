---
title: Napravi konfiguraciju mosta
lead: 'Šalji ono što tvoj repeater čuje na bilo koji MQTT broker: svoj ili Analyzerov. Slanje obavlja računalo pokraj repeatera.'
description: Pokreni meshcoretomqtt na Raspberry Piju ili drugom računalu i šalji ono što MeshCore repeater čuje preko USB-a na svoj MQTT broker, na MeshCore Analyzer ili na oba.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Repeater je čvor koji prosljeđuje poruke. Želiš da njegov promet stiže na MQTT broker: na svoj, za nadzornu ploču ili bazu podataka, ili na broker
[MeshCore Analyzera](https://meshcore-analyzer.eu/). Ili tvoj repeater nema vlastiti Wi-Fi, ali pokraj njega stoji Raspberry Pi ili poslužitelj.
Most je [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), alat iz zajednice: šalje promet s tog računala.
Tvoj repeater i dalje prosljeđuje poruke, jer most samo čita ono što repeater bilježi preko USB-a.

## Što ti treba {#need}

- Repeater čiji je firmware izgrađen s bilježenjem paketa (vidi niže).
- Raspberry Pi Zero, 2, 3 ili 4, ili bilo koje računalo s Linuxom ili macOS-om, uz Python 3.11 ili noviji.
- USB podatkovni kabel između ta dva uređaja.

Standardni firmware za repeater iz flashera ne bilježi pakete. Sam izgradi firmware za repeater iz
[izvornog koda MeshCorea](https://github.com/meshcore-dev/MeshCore). U build svoje pločice dodaj ovu zastavicu:

```text
-D MESH_PACKET_LOGGING=1
```

## Instalacija {#install}

Priključi repeater na računalo, a zatim na tom računalu pokreni instalacijsku skriptu meshcoretomqtta:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skripta instalira most kao servis koji se pokreće zajedno s računalom, a pita te i na koje brokere želiš slati promet. Analyzera nema na tom popisu: dodaješ ga u konfiguracijskoj datoteci u nastavku. Tvoje postavke nalaze se u
`/etc/mctomqtt/config.d/99-user.toml`. Nijedno ažuriranje ne prepisuje tu datoteku.

## Brokeri {#brokers}

Svaki broker dobiva vlastiti blok `[[broker]]`, pa jedan repeater može slati na više njih istodobno. Na svojem brokeru koristiš korisničko ime i lozinku ili se uopće ne prijavljuješ
(`method = "none"`).
MeshCore Analyzer umjesto toga traži token, a potpisuje ga ključ tvojeg repeatera:

- adresa `mqtt.meshcore-analyzer.eu`, port `443`, preko sigurnog websocketa;
- audience tokena je ta ista adresa.

## Tvoja konfiguracijska datoteka {#config}

Zamijeni sadržaj datoteke `/etc/mctomqtt/config.d/99-user.toml` ovim tekstom. Upiši kod zračne luke najbliže svojem repeateru (na primjer `AMS`) i USB port na kojem je repeater. Zatim dodaj svoj broker. Izostavi blok koji ti ne treba.

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

Nakon svake promjene ponovno pokreni servis (`sudo systemctl restart mctomqtt` na Linuxu). Tvoj se repeater tada na Analyzeru pojavljuje kao observer, čvor koji šalje ono što čuje, pod vlastitim imenom. Sve ostale postavke naći ćeš u
[README-u meshcoretomqtta](https://github.com/Cisien/meshcoretomqtt).
