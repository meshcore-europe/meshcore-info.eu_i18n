---
title: Izveido tilta konfigurāciju
lead: 'Sūti to, ko dzird tavs retranslators, uz jebkuru MQTT brokeri: savu vai Analyzer. Datus sūta dators, kas atrodas blakus retranslatoram.'
description: Palaid meshcoretomqtt uz Raspberry Pi vai cita datora un sūti to, ko MeshCore retranslators dzird, pa USB uz savu MQTT brokeri, MeshCore Analyzer vai abiem.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Retranslators ir mezgls, kas pārsūta ziņas tālāk. Tu vēlies, lai tā datplūsma nonāk MQTT
brokerī: tavā, ja vajag paneli vai datubāzi, vai
[MeshCore Analyzer](https://meshcore-analyzer.eu/) brokerī. Vai arī tavam
retranslatoram nav sava Wi-Fi, bet blakus tam ir Raspberry Pi vai serveris.
Kopienas rīks [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) ir tilts:
tas sūta datplūsmu no šī datora. Retranslators turpina pārsūtīt ziņas, jo tilts
tikai nolasa to, ko retranslators pa USB raksta žurnālā.

## Kas tev vajadzīgs {#need}

- Retranslators, kura programmaparatūra būvēta ar pakešu žurnalēšanu (skaidrojums zemāk).
- Raspberry Pi Zero, 2, 3 vai 4 vai jebkurš Linux vai macOS dators ar Python
  3.11 vai jaunāku versiju.
- USB datu kabelis starp abām ierīcēm.

Standarta retranslatora programmaparatūra no flasher rīka pakešu žurnālu neraksta.
Uzbūvē retranslatora programmaparatūru pats no
[MeshCore pirmkoda](https://github.com/meshcore-dev/MeshCore) un pievieno savas
plates būvējumam šo karodziņu:

```text
-D MESH_PACKET_LOGGING=1
```

## Instalēšana {#install}

Pieslēdz retranslatoru datoram un pēc tam palaid šajā datorā meshcoretomqtt
instalēšanas skriptu:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skripts instalē tiltu kā pakalpojumu, kas sāk darboties līdz ar datoru, un jautā, uz
kuriem brokeriem sūtīt datus. Analyzer šajā sarakstā nav: to tu pievieno tālāk
aprakstītajā konfigurācijas failā. Tavi iestatījumi atrodas failā
`/etc/mctomqtt/config.d/99-user.toml`, un atjauninājums to nekad nepārraksta.

## Brokeri {#brokers}

Katram brokerim ir savs `[[broker]]` bloks, tāpēc viens retranslators var sūtīt
datus vairākiem brokeriem vienlaikus. Savam brokerim tu norādi lietotājvārdu un
paroli vai vispār iztiec bez pieteikšanās (`method = "none"`).
MeshCore Analyzer tā vietā prasa marķieri, ko paraksta tava retranslatora atslēga:

- adrese `mqtt.meshcore-analyzer.eu`, ports `443`, pa drošu websocket savienojumu;
- marķiera auditorija ir tā pati adrese.

## Tavs konfigurācijas fails {#config}

Aizstāj faila `/etc/mctomqtt/config.d/99-user.toml` saturu ar šo tekstu. Ieraksti
retranslatoram tuvākās lidostas kodu (piemēram, `AMS`) un USB portu, kuram
retranslators ir pieslēgts. Pēc tam pievieno savu brokeri. Bloku, kas tev nav
vajadzīgs, izlaid.

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

Pēc izmaiņām restartē pakalpojumu (Linux sistēmā `sudo systemctl restart mctomqtt`).
Tad tavs retranslators parādās Analyzer rīkā kā novērotājs (mezgls, kas
augšupielādē dzirdēto) ar paša retranslatora nosaukumu. Visi pārējie iestatījumi
ir aprakstīti failā [meshcoretomqtt README](https://github.com/Cisien/meshcoretomqtt).
