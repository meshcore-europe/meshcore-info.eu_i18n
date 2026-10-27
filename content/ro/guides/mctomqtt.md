---
title: Construiește o configurație de punte
lead: 'Trimite ce aude repetorul tău către orice broker MQTT: al tău sau cel al Analyzer-ului. Un calculator de lângă repetor face trimiterea.'
description: Rulează meshcoretomqtt pe un Raspberry Pi sau pe alt calculator ca să trimiți ce aude un repetor MeshCore prin USB către propriul tău broker MQTT, către MeshCore Analyzer sau către ambele.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-26'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
---

Un repetor este un nod care transmite mesajele mai departe. Vrei traficul lui
pe un broker MQTT: al tău, pentru un panou de bord sau o bază de date, sau cel
al [MeshCore Analyzer](https://meshcore-analyzer.eu/). Sau repetorul tău nu
are Wi-Fi propriu, dar lângă el stă un Raspberry Pi sau un server.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), un instrument al
comunității, este puntea: trimite traficul de pe acel calculator. Repetorul
tău repetă în continuare, pentru că puntea doar citește ce înregistrează el
prin USB.

## De ce ai nevoie {#need}

- Un repetor construit cu înregistrarea pachetelor (vezi mai jos).
- Un Raspberry Pi Zero, 2, 3 sau 4, ori orice calculator cu Linux sau macOS,
  cu Python 3.11 sau mai nou.
- Un cablu USB de date între cele două.

Firmware-ul standard de repetor din flasher nu înregistrează pachetele.
Construiește singur firmware-ul de repetor din
[sursa MeshCore](https://github.com/meshcore-dev/MeshCore), cu acest flag
adăugat la build-ul plăcii tale:

```text
-D MESH_PACKET_LOGGING=1
```

## Instalare {#install}

Conectează repetorul la calculator, apoi rulează pe acel calculator scriptul
de instalare al meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Scriptul instalează puntea ca serviciu care pornește odată cu calculatorul și
te întreabă către ce brokeri să trimită. Analyzer-ul nu se află în acea
listă; îl adaugi în fișierul de configurare de mai jos. Setările tale stau în
`/etc/mctomqtt/config.d/99-user.toml`; o actualizare nu suprascrie niciodată
acest fișier.

## Brokeri {#brokers}

Fiecare broker primește propriul bloc `[[broker]]`, așa că un singur repetor
poate alimenta mai mulți deodată. Brokerul tău acceptă un nume de utilizator
și o parolă, sau nicio autentificare (`method = "none"`).
MeshCore Analyzer acceptă în schimb un token, pe care îl semnează cheia
repetorului tău:

- adresa `mqtt.meshcore-analyzer.eu`, portul `443`, printr-un websocket securizat;
- audiența token-ului este aceeași adresă.

## Fișierul tău de configurare {#config}

Înlocuiește conținutul din `/etc/mctomqtt/config.d/99-user.toml` cu ce
urmează. Completează codul aeroportului cel mai apropiat de repetorul tău
(de exemplu `AMS`) și portul USB la care este conectat repetorul. Apoi adaugă
propriul tău broker. Lasă deoparte un bloc de care nu ai nevoie.

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

Repornește serviciul după o modificare (`sudo systemctl restart mctomqtt` pe
Linux). Repetorul tău apare apoi pe Analyzer ca observator, adică un nod care
încarcă ce aude, sub numele propriu al repetorului. Toate celelalte setări le
găsești în [README-ul meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt).
