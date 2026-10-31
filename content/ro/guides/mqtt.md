---
title: MQTT pe observer-ul tău
lead: Repetorul tău raportează prin Wi-Fi ce aude, către MeshCore Analyzer. Continuă să transmită mesajele mai departe, ca înainte.
description: Transformă un repetor ESP32 într-un observer MeshCore cu firmware-ul DMC observer. Îl flash-uiești, setezi Wi-Fi-ul și codul de aeroport, alegi brokerii și verifici că raportează către MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-31'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Un observer este un nod care raportează și ce aude, prin MQTT, folosind
Wi-Fi. Fiecare observer arată o parte în plus din mesh pe
[MeshCore Analyzer](https://meshcore-analyzer.eu/) și pe
[hărțile de acoperire](/map/). Cu acest ghid transformi un repetor (un nod
care transmite mesajele mai departe) într-un observer. Repetorul continuă să
retransmită, iar raportul merge într-un singur sens: nimic nu se întoarce în mesh.

{{< callout type="warning" >}}
Acest ghid este pentru **firmware-ul DMC observer**, versiunea de observer a
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), bazată pe
MeshCore 1.18.0. MeshCore standard nu are MQTT. Am preluat fiecare comandă de
mai jos din codul sursă al firmware-ului, la build-ul `32dd8ad` din 19 octombrie 2026.
{{< /callout >}}

## De ce ai nevoie {#need}

- O placă ESP32 cu Wi-Fi, de exemplu un Heltec V3 sau V4, un LilyGo T3S3 sau
  un Xiao S3. În [release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  găsești toate plăcile. Plăcile nRF52, cum ar fi RAK4631, nu au Wi-Fi.
- O rețea Wi-Fi de 2.4 GHz acolo unde stă placa.
- Un cablu USB de date și Chrome, Edge sau Opera pe calculator.
- Codul aeroportului cel mai apropiat de nodul tău, din 3 litere, ca `AMS`
  sau `BRU`. Din el, brokerii (serverele care primesc rapoartele tale) află
  în ce zonă se află observer-ul tău.

Nu ai Wi-Fi acolo unde stă repetorul, dar ai un calculator lângă el?
Atunci [creează o configurație de bridge](/guides/mctomqtt/).

## Flash-uiește firmware-ul {#flash}

[Flasher-ul](/firmware/flasher/) de pe acest site are doar MeshCore standard.
Firmware-ul de observer îl iei din flasher-ul din
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Alege placa, apoi **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Prima dată alege **Full flash**: înlocuiește tot ce e pe placă, inclusiv
   tabela de partiții. Actualizarea aplicației păstrează ce există și e
   pentru actualizările ulterioare.
3. Configurează repetorul ca de obicei: nume, preset radio și parolă de
   admin, ca în [ghidul pentru repetor](/repeater-guide/#config).

Acest firmware este build-ul **dev** și se actualizează singur de pe canalul
dev când tastezi `ota update`. Canalul stabil are încă 1.17.1, așa că rămâi
pe dev pentru acest ghid.

## Setări {#settings}

Deschide [consola serială](/firmware/console/) de pe acest site și conectează
placa. Completează rețeaua Wi-Fi, parola și codul de aeroport, apoi lipește
aceste rânduri unul câte unul:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

După repornire, placa se conectează la Wi-Fi și își ia ora de pe internet.
Brokerii au nevoie de această oră ca să verifice identitatea observer-ului
tău. Fără cod de aeroport, nu se raportează nimic.

Preferi să dai click în loc să tastezi? Comanda `start webconfig` deschide o
pagină de setări pe placă, la adresa afișată în consolă. Te autentifici cu
parola de admin.

## Sloturi pentru brokeri {#brokers}

Un slot conține un broker. Firmware-ul vine cu aceste sloturi completate:

| Slot | Broker | Administrat de |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

O placă fără memorie suplimentară (PSRAM), cum e Heltec V3, are 3 sloturi.
Se conectează la 2 dintre ele simultan, așa că Analyzer-ul din slotul 3 nu se
conectează niciodată. Mută-l în slotul 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

O placă cu PSRAM, cum e Heltec V4, are 6 sloturi și se conectează la 5
simultan. Acolo nu trebuie să schimbi nimic.

Nodul tău se autentifică la fiecare broker cu propria cheie, deci nu ai
nevoie de cont. Cu `get mqtt.presets` vezi ceilalți brokeri ai comunității pe
care îi cunoaște firmware-ul.

### Brokerul tău {#own}

Pune propriul broker într-un slot liber. Completează adresa, portul, numele
de utilizator și parola. Pe o placă cu PSRAM, slotul 4 este liber:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Pe o placă fără PSRAM, folosește în schimb slotul 2: înlocuiește `mqtt4` cu
`mqtt2`. Brokerul tău ia atunci locul lui `dutchmeshcore-2`.

Pe portul `8883` conexiunea este criptată (TLS). Pe portul `443` este criptată
printr-o conexiune web (websocket). Pe orice alt port este necriptată. Poți da
și adresa completă, de exemplu `wss://mqtt.example.org:9002/mqtt`. În acest
caz regula porturilor nu se aplică.

## Verifică dacă funcționează {#check}

Tastează `get mqtt.status`. Fiecare slot își arată starea:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: conectat.
- `wait`: slotului îi lipsește o setare, de exemplu codul de aeroport.
- `disc`: nu e conectat încă. Verifică Wi-Fi-ul cu `get wifi.status`.
- `fail`: slotul a eșuat de 7 ori la rând, în aproximativ 20 de minute, iar
  acum încearcă o dată la 30 de minute. Verifică adresa și datele de
  autentificare ale brokerului.
- `inactive`: placa nu are loc pentru acest slot. Vezi
  [Sloturi pentru brokeri](#brokers).

Apoi caută numele repetorului tău pe
[pagina de observeri din Analyzer](https://meshcore-analyzer.eu/#observers).
Apare în cel mult 5 minute, cu ce a auzit.
