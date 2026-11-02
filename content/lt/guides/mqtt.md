---
title: MQTT tavo stebėtojui
lead: Tegul tavo retransliatorius per Wi-Fi praneša MeshCore Analyzer, ką girdi. Žinutes jis perduoda toliau kaip anksčiau.
description: Paversk ESP32 retransliatorių MeshCore stebėtoju su DMC observer programine įranga. Įrašyk ją į plokštę, nustatyk Wi-Fi ir oro uosto kodą, pasirink brokerius ir patikrink, ar pranešimai pasiekia MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-11-02'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Stebėtojas (observer) yra mazgas, kuris per Wi-Fi ir MQTT dar praneša, ką girdi.
Su kiekvienu stebėtoju [MeshCore Analyzer](https://meshcore-analyzer.eu/) svetainėje ir
[aprėpties žemėlapiuose](/map/) matyti šiek tiek daugiau tinklo. Šiame vadove retransliatorių (mazgą, kuris
perduoda žinutes toliau) paversi stebėtoju. Jis toliau retransliuoja žinutes, o
pranešimai keliauja tik viena kryptimi: į tinklą niekas negrįžta.

{{< callout type="warning" >}}
Šis vadovas skirtas **DMC observer programinei įrangai**. Tai
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) stebėtojo versija,
sukurta MeshCore 1.18.0 pagrindu. Standartinis MeshCore neturi MQTT. Visas
toliau pateiktas komandas paėmėme iš programinės įrangos šaltinio kodo (versija
`32dd8ad`, 2026 m. spalio 19 d.).
{{< /callout >}}

## Ko tau reikia {#need}

- ESP32 plokštės su Wi-Fi, pavyzdžiui, Heltec V3 ar V4, LilyGo T3S3 arba
  Xiao S3. [Laidos puslapyje](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  išvardytos visos plokštės. nRF52 plokštės, pavyzdžiui, RAK4631, neturi Wi-Fi.
- 2.4 GHz Wi-Fi tinklo toje vietoje, kur stovi plokštė.
- USB duomenų kabelio ir Chrome, Edge arba Opera naršyklės kompiuteryje.
- Tavo mazgui artimiausio oro uosto 3 raidžių kodo, pavyzdžiui, `AMS` arba `BRU`.
  Pagal jį brokeriai (serveriai, kurie gauna tavo pranešimus) žino, kurioje
  vietovėje yra tavo stebėtojas.

Prie retransliatoriaus nėra Wi-Fi, bet šalia yra kompiuteris?
Tada [susikurk tilto konfigūraciją](/guides/mctomqtt/).

## Programinės įrangos įrašymas {#flash}

Šios svetainės [įrašymo įrankyje](/firmware/flasher/) yra tik standartinis MeshCore.
Stebėtojo programinę įrangą rasi
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/) įrašymo įrankyje:

1. Pasirink savo plokštę, tada **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Pirmą kartą rinkis **Full flash**: taip pakeisi viską plokštėje, įskaitant
   skaidinių lentelę. Programos atnaujinimas palieka tai, kas jau yra, ir skirtas
   vėlesniems atnaujinimams.
3. Retransliatorių nustatyk kaip įprasta: pavadinimą, radijo profilį ir
   administratoriaus slaptažodį, kaip aprašyta [retransliatoriaus vadove](/repeater-guide/#config).

Tai **dev** versija. Kai įvedi `ota update`, ji atsinaujina iš dev kanalo.
Stabiliame kanale vis dar yra 1.17.1, todėl šiam vadovui lik dev kanale.

## Nustatymai {#settings}

Atidaryk šios svetainės [nuosekliąją konsolę](/firmware/console/) ir prijunk
plokštę. Įrašyk savo Wi-Fi tinklo pavadinimą, slaptažodį ir oro uosto kodą, tada įklijuok
šias eilutes po vieną:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Po paleidimo iš naujo plokštė prisijungia prie tavo Wi-Fi ir nustato laikrodį
pagal internetą. Šio laikrodžio brokeriams reikia, kad patikrintų, kas yra tavo stebėtojas. Be oro
uosto kodo plokštė nieko nepraneša.

Nori spustelėti, o ne rašyti? Komanda `start webconfig` atidaro plokštės
nustatymų puslapį tuo adresu, kurį rodo konsolė. Prisijunk administratoriaus
slaptažodžiu.

## Brokerių lizdai {#brokers}

Viename lizde telpa vienas brokeris. Programinėje įrangoje iš pradžių užpildyti šie lizdai:

| Lizdas | Brokeris | Kas prižiūri |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Plokštė be papildomos atminties (PSRAM), pavyzdžiui, Heltec V3, turi 3 lizdus.
Vienu metu ji jungiasi prie 2 iš jų, todėl Analyzer 3 lizde niekada neprisijungia.
Perkelk jį į 1 lizdą:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Plokštė su PSRAM, pavyzdžiui, Heltec V4, turi 6 lizdus ir vienu metu jungiasi
prie 5. Jai nieko keisti nereikia.

Tavo mazgas prie kiekvieno brokerio jungiasi savo raktu, todėl paskyros tau
nereikia. Komanda `get mqtt.presets` išvardija kitus bendruomenės brokerius, kuriuos
žino programinė įranga.

### Nuosavas brokeris {#own}

Įrašyk savo brokerį į laisvą lizdą. Nurodyk jo adresą, prievadą, naudotojo vardą
ir slaptažodį. Plokštėje su PSRAM laisvas 4 lizdas:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Plokštėje be PSRAM naudok 2 lizdą: `mqtt4` pakeisk į `mqtt2`.
Tada tavo brokeris užims `dutchmeshcore-2` vietą.

Per prievadą `8883` ryšys šifruojamas (TLS), per prievadą `443` jis šifruojamas
per žiniatinklio ryšį (websocket), o per bet kurį kitą prievadą nešifruojamas.
Gali nurodyti ir visą adresą, pavyzdžiui, `wss://mqtt.example.org:9002/mqtt`:
tada prievadų taisyklė negalioja.

## Patikrink, ar veikia {#check}

Įvesk `get mqtt.status`. Prie kiekvieno lizdo matysi jo būseną:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: prisijungta.
- `wait`: lizdui trūksta nustatymo, pavyzdžiui, oro uosto kodo.
- `disc`: dar neprisijungta. Patikrink Wi-Fi komanda `get wifi.status`.
- `fail`: lizdui nepavyko prisijungti 7 kartus iš eilės per maždaug 20 minučių
  ir dabar jis bando kartą per 30 minučių. Patikrink brokerio adresą ir
  prisijungimo duomenis.
- `inactive`: plokštėje šiam lizdui nėra vietos. Žr.
  [Brokerių lizdai](#brokers).

Tada ieškok savo retransliatoriaus pavadinimo
[Analyzer stebėtojų puslapyje](https://meshcore-analyzer.eu/#observers).
Per 5 minutes jis ten atsiras, ir matysi, ką jis girdėjo.
