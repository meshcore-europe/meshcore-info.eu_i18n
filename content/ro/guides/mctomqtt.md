---
title: Configurează o punte
lead: 'Trimite ce aude repetorul tău către orice broker MQTT: al tău sau cel al Analyzer. Trimiterea o face un computer aflat lângă repetor.'
description: Rulează meshcoretomqtt pe un Raspberry Pi sau pe alt computer. Așa trimiți ce aude un repetor MeshCore prin USB către brokerul tău MQTT, către MeshCore Analyzer sau către amândouă.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-31'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Un repetor este un nod care transmite mesajele mai departe. Vrei ca traficul lui
să ajungă pe un broker MQTT: pe al tău, pentru un dashboard sau o bază de date, sau pe
cel al [MeshCore Analyzer](https://meshcore-analyzer.eu/). Sau repetorul tău nu
are WiFi propriu, dar lângă el stă un Raspberry Pi sau un server.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), un instrument al
comunității, este puntea: trimite traficul de pe acel computer. Repetorul tău
continuă să retransmită, pentru că puntea doar citește ce scrie el în jurnal prin USB.

## De ce ai nevoie {#need}

- Un repetor compilat cu jurnalizarea pachetelor (vezi mai jos).
- Un Raspberry Pi Zero, 2, 3 sau 4, sau orice computer cu Linux sau macOS,
  cu Python 3.11 sau mai nou.
- Un cablu USB de date între cele două.

Firmware-ul standard de repetor din flasher nu jurnalizează pachetele.
Compilează tu firmware-ul de repetor din
[codul sursă MeshCore](https://github.com/meshcore-dev/MeshCore). Adaugă acest
flag în configurația de build a plăcii tale:

```text
-D MESH_PACKET_LOGGING=1
```

## Instalare {#install}

Conectează repetorul la computer. Apoi rulează pe acel computer scriptul de
instalare al meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Scriptul instalează puntea ca serviciu care pornește odată cu computerul. Apoi
te întreabă către ce brokeri să trimită. Analyzer nu apare în acea listă: îl
adaugi în fișierul de configurare de mai jos. Setările tale stau în
`/etc/mctomqtt/config.d/99-user.toml`. O actualizare nu suprascrie niciodată
acel fișier.

## Brokeri {#brokers}

Fiecare broker are propriul bloc `[[broker]]`. Așa, un repetor poate alimenta
mai mulți brokeri în același timp. Brokerul tău cere un nume de utilizator
și o parolă, sau nu cere deloc autentificare (`method = "none"`).
MeshCore Analyzer cere în schimb un token, pe care îl semnează cheia repetorului tău:

- adresa `mqtt.meshcore-analyzer.eu`, portul `443`, printr-un websocket securizat;
- audiența tokenului este aceeași adresă.

## Fișierul tău de configurare {#config}

Înlocuiește conținutul fișierului `/etc/mctomqtt/config.d/99-user.toml` cu
acesta. Completează codul aeroportului cel mai apropiat de repetorul tău (de
exemplu `AMS`) și portul USB la care e conectat repetorul. Apoi adaugă
brokerul tău. Omite blocurile de care nu ai nevoie.

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

Repornește serviciul după fiecare modificare (`sudo systemctl restart mctomqtt`
pe Linux). Repetorul tău apare apoi în Analyzer ca observer, adică un nod care
încarcă ce aude, sub numele propriu al repetorului. În
[README-ul meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) găsești
toate celelalte setări.
