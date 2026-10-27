---
title: MQTT pe observatorul tău
lead: Lasă repetorul tău să raporteze ce aude către MeshCore Analyzer, prin Wi-Fi. El transmite mesajele mai departe ca și până acum.
description: Transformă un repetor ESP32 într-un observator MeshCore cu firmware-ul de observator DMC. Instalează-l, setează Wi-Fi și codul tău de aeroport, alege brokerii și verifică dacă raportează către MeshCore Analyzer.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-26'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
---

Un observator este un nod care raportează în plus ce aude, prin MQTT, pe
Wi-Fi. Fiecare observator arată o parte în plus din mesh pe
[MeshCore Analyzer](https://meshcore-analyzer.eu/) și pe
[hărțile de acoperire](/map/). Acest ghid transformă un repetor (un nod care
transmite mesajele mai departe) într-un observator. El continuă să repete, iar
raportarea merge într-o singură direcție: nimic nu se întoarce în mesh.

{{< callout type="warning" >}}
Acest ghid este pentru **firmware-ul de observator DMC**, varianta de observator
a [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), bazată pe
MeshCore 1.18.0. MeshCore standard nu are MQTT. Fiecare comandă de mai jos este
luată din codul sursă al firmware-ului, build `32dd8ad` din 19 octombrie 2026.
{{< /callout >}}

## De ce ai nevoie {#need}

- O placă ESP32 cu Wi-Fi, cum ar fi Heltec V3 sau V4, LilyGo T3S3 sau
  Xiao S3. [Release-ul](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  listează fiecare placă. Plăcile nRF52, cum ar fi RAK4631, nu au Wi-Fi.
- O rețea Wi-Fi de 2.4 GHz acolo unde stă placa.
- Un cablu USB de date și Chrome, Edge sau Opera pe calculatorul tău.
- Codul aeroportului cel mai apropiat de nodul tău, 3 litere, cum ar fi `AMS` sau `BRU`.
  El spune brokerilor (serverele care primesc rapoartele tale) în ce zonă
  se află observatorul tău.

Nu ai Wi-Fi acolo unde stă repetorul, dar ai un calculator lângă el?
[Construiește în schimb o configurație de punte](/guides/mctomqtt/).

## Instalează firmware-ul {#flash}

[Flasher-ul](/firmware/flasher/) de pe acest site conține doar MeshCore
standard. Firmware-ul de observator îl iei din flasher-ul din
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Alege placa ta, apoi **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Prima dată alege **Full flash**: înlocuiește tot ce e pe placă, inclusiv
   tabela de partiții. Actualizarea aplicației păstrează ce există deja și e
   pentru actualizările ulterioare.
3. Configurează repetorul ca de obicei: nume, preset radio și parola de
   administrator, ca în [ghidul pentru repetor](/repeater-guide/#config).

Acest firmware este build-ul **dev** și se actualizează singur din canalul dev
când tastezi `ota update`. Canalul stabil are încă 1.17.1, așa că rămâi pe dev
pentru acest ghid.

## Setări {#settings}

Deschide [consola serială](/firmware/console/) de pe acest site și conectează
placa. Completează rețeaua ta Wi-Fi, parola și codul de aeroport, apoi lipește
aceste linii una câte una:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

După repornire, placa se conectează la Wi-Fi-ul tău și își setează ceasul de
pe internet. Brokerii au nevoie de acest ceas ca să verifice cine este
observatorul tău. Fără cod de aeroport, nu se raportează nimic.

Preferi să dai clic în loc să tastezi? `start webconfig` deschide o pagină de
setări pe placă, la adresa pe care o arată consola. Autentifică-te cu parola
de administrator.

## Sloturi pentru brokeri {#brokers}

Un slot conține un broker. Firmware-ul pornește cu aceste sloturi completate:

| Slot | Broker | Operat de |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

O placă fără memorie suplimentară (PSRAM), cum ar fi Heltec V3, are 3 sloturi.
Se conectează la 2 dintre ele simultan, așa că Analyzer-ul din slotul 3 nu se
conectează niciodată. Mută-l în slotul 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

O placă cu PSRAM, cum ar fi Heltec V4, are 6 sloturi și se conectează la 5
simultan. Ea nu are nevoie de nicio modificare.

Nodul tău se autentifică la fiecare broker cu propria sa cheie, deci nu ai
nevoie de cont. `get mqtt.presets` listează ceilalți brokeri ai comunității pe
care firmware-ul îi cunoaște.

### Brokerul tău propriu {#own}

Pune brokerul tău într-un slot liber. Completează adresa, portul, numele de
utilizator și parola lui. Pe o placă cu PSRAM, slotul 4 este liber:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Pe o placă fără PSRAM, folosește în schimb slotul 2: înlocuiește `mqtt4` cu
`mqtt2`. Brokerul tău ia atunci locul lui `dutchmeshcore-2`.

Portul `8883` se conectează criptat (TLS), portul `443` criptat printr-o
conexiune web (websocket), iar orice alt port necriptat. Poți da și adresa
completă, cum ar fi `wss://mqtt.example.org:9002/mqtt`; atunci regula portului
nu se mai aplică.

## Verifică dacă funcționează {#check}

Tastează `get mqtt.status`. Fiecare slot își arată starea:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: conectat.
- `wait`: slotului îi lipsește o setare, cum ar fi codul de aeroport.
- `disc`: încă neconectat. Verifică Wi-Fi-ul cu `get wifi.status`.
- `fail`: slotul a eșuat de 7 ori la rând, în aproximativ 20 de minute, și
  acum încearcă o dată la 30 de minute. Verifică adresa brokerului și datele
  de autentificare.
- `inactive`: placa nu are loc pentru acest slot. Vezi
  [Sloturi pentru brokeri](#brokers).

Apoi caută numele repetorului tău pe
[pagina de observatori a Analyzer-ului](https://meshcore-analyzer.eu/#observers).
Apare în 5 minute, împreună cu ce a auzit.
