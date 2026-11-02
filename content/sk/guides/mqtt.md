---
title: MQTT na tvojom observeri
lead: Nechaj svoj repeater hlásiť cez Wi-Fi do MeshCore Analyzer, čo počuje. Správy bude posielať ďalej rovnako ako doteraz.
description: Urob z repeatera s ESP32 MeshCore observer pomocou firmvéru DMC observer. Nahraj firmvér, nastav Wi-Fi a kód letiska, vyber brokerov a over, či sa hlásenia dostávajú do MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-11-02'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Observer je uzol, ktorý navyše cez Wi-Fi a MQTT hlási, čo počuje. Každý
observer ukáže o kúsok viac zo siete v
[MeshCore Analyzeri](https://meshcore-analyzer.eu/) a na
[mapách pokrytia](/map/). Podľa tohto návodu z repeatera (uzla, ktorý posiela
správy ďalej) urobíš observer. Repeater bude správy preposielať aj potom.
Hlásenia idú iba jedným smerom: do siete sa nič nevracia.

{{< callout type="warning" >}}
Tento návod platí pre **firmvér DMC observer**, teda verziu
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) pre observery,
postavenú na MeshCore 1.18.0. Štandardný MeshCore MQTT nemá. Všetky príkazy
nižšie pochádzajú zo zdrojového kódu firmvéru, zo zostavy `32dd8ad` z
19. októbra 2026.
{{< /callout >}}

## Čo potrebuješ {#need}

- Dosku ESP32 s Wi-Fi, napríklad Heltec V3 alebo V4, LilyGo T3S3 alebo
  Xiao S3. Všetky dosky nájdeš vo [vydaní](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev).
  Dosky nRF52, napríklad RAK4631, Wi-Fi nemajú.
- Sieť Wi-Fi 2.4 GHz tam, kde doska stojí.
- Dátový kábel USB a na počítači Chrome, Edge alebo Opera.
- Kód letiska najbližšieho k tvojmu uzlu: 3 písmená, napríklad `AMS` alebo `BRU`.
  Podľa neho brokeri (servery, ktoré prijímajú tvoje hlásenia) vedia, v ktorej
  oblasti je tvoj observer.

Tam, kde stojí tvoj repeater, nemáš Wi-Fi, ale máš vedľa neho počítač?
Namiesto toho si [zostav bridge config](/guides/mctomqtt/).

## Nahraj firmvér {#flash}

[Flasher](/firmware/flasher/) na tomto webe obsahuje iba štandardný MeshCore.
Firmvér pre observer nahráš pomocou flashera v
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Vyber svoju dosku a potom **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Pri prvom nahrávaní zvoľ **Full flash**: prepíše všetko na doske vrátane
   tabuľky oddielov. Aktualizácia aplikácie ponechá, čo na doske je, a použiješ
   ju pri ďalších aktualizáciách.
3. Nastav repeater ako obvykle: názov, predvoľbu rádia a heslo správcu, ako
   v [návode na repeater](/repeater-guide/#config).

Tento firmvér je zostava **dev**. Keď zadáš `ota update`, aktualizuje sa
z kanála dev. Stabilný kanál má stále verziu 1.17.1, preto pri tomto návode
zostaň na kanáli dev.

## Nastavenia {#settings}

Otvor [sériovú konzolu](/firmware/console/) na tomto webe a pripoj dosku.
Doplň názov a heslo svojej Wi-Fi siete a kód letiska. Potom vkladaj tieto
riadky jeden po druhom:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Po reštarte sa doska pripojí k tvojej Wi-Fi a nastaví si hodiny z internetu.
Brokeri tieto hodiny potrebujú, aby overili, kto je tvoj observer. Bez kódu
letiska sa nič nehlási.

Radšej klikáš, než píšeš? Príkaz `start webconfig` otvorí na doske stránku
s nastaveniami, na adrese, ktorú ukáže konzola. Prihlás sa heslom správcu.

## Sloty pre brokerov {#brokers}

Do jedného slotu patrí jeden broker. Firmvér má na začiatku vyplnené tieto
sloty:

| Slot | Broker | Prevádzkuje |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Doska bez dodatočnej pamäte (PSRAM), napríklad Heltec V3, má 3 sloty. Naraz sa
pripojí k 2 z nich, takže Analyzer v slote 3 sa nikdy nepripojí. Presuň ho do
slotu 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Doska s PSRAM, napríklad Heltec V4, má 6 slotov a naraz sa pripojí k 5 z nich.
Tu nemusíš nič meniť.

Tvoj uzol sa ku každému brokerovi prihlasuje vlastným kľúčom, takže účet
nepotrebuješ. Príkaz `get mqtt.presets` vypíše ďalších komunitných brokerov,
ktorých firmvér pozná.

### Vlastný broker {#own}

Vlastného brokera zadaj do voľného slotu. Vyplň jeho adresu, port, používateľské
meno a heslo. Na doske s PSRAM je voľný slot 4:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Na doske bez PSRAM použi namiesto neho slot 2: `mqtt4` zmeň na `mqtt2`.
Tvoj broker potom nahradí `dutchmeshcore-2`.

Port `8883` znamená šifrované pripojenie (TLS), port `443` šifrované pripojenie
cez web (websocket) a každý iný port nešifrované pripojenie. Môžeš zadať aj celú
adresu, napríklad `wss://mqtt.example.org:9002/mqtt`. Pravidlo o portoch potom
neplatí.

## Over, či to funguje {#check}

Zadaj `get mqtt.status`. Pri každom slote uvidíš jeho stav:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: pripojený.
- `wait`: slotu chýba nastavenie, napríklad kód letiska.
- `disc`: zatiaľ nepripojený. Skontroluj Wi-Fi príkazom `get wifi.status`.
- `fail`: slot zlyhal 7-krát za sebou, počas približne 20 minút, a teraz to
  skúša raz za 30 minút. Skontroluj adresu brokera a prihlasovacie údaje.
- `inactive`: doska nemá miesto pre tento slot. Pozri
  [Sloty pre brokerov](#brokers).

Potom pohľadaj názov svojho repeatera na
[stránke observerov v Analyzeri](https://meshcore-analyzer.eu/#observers).
Do 5 minút sa tam objaví aj s tým, čo počul.
