---
title: MQTT na tvém observeru
lead: Nech svůj repeater hlásit přes Wi-Fi do MeshCore Analyzeru, co slyší. Zprávy předává dál jako dřív.
description: Udělej z repeateru na ESP32 observer MeshCore s observer firmwarem DMC. Nahraj firmware, nastav Wi-Fi a kód letiště, vyber brokery a ověř, že hlásí do MeshCore Analyzeru.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-26'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
---

Observer je uzel, který navíc přes Wi-Fi hlásí po MQTT, co slyší. Každý
observer ukáže o kousek víc z meshe v
[MeshCore Analyzeru](https://meshcore-analyzer.eu/) a na
[mapách pokrytí](/map/). Tento návod udělá observer z repeateru (uzlu, který
předává zprávy dál). Repeater opakuje dál a hlášení jde jen jedním směrem:
do meshe se nic nevrací.

{{< callout type="warning" >}}
Tento návod platí pro **observer firmware DMC**, observer sestavení
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), postavené na
MeshCore 1.18.0. Standardní MeshCore žádné MQTT nemá. Každý příkaz níže
pochází ze zdrojového kódu firmwaru v sestavení `32dd8ad` z 19. října 2026.
{{< /callout >}}

## Co potřebuješ {#need}

- Desku ESP32 s Wi-Fi, třeba Heltec V3 nebo V4, LilyGo T3S3 nebo
  Xiao S3. [Release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  uvádí každou desku. Desky nRF52, třeba RAK4631, Wi-Fi nemají.
- Síť Wi-Fi 2.4 GHz tam, kde deska stojí.
- Datový kabel USB a na počítači Chrome, Edge nebo Opera.
- Kód letiště nejblíž k tvému uzlu, 3 písmena, třeba `AMS` nebo `BRU`.
  Říká brokerům (serverům, které přijímají tvá hlášení), v jaké oblasti
  tvůj observer stojí.

Tam, kde stojí tvůj repeater, není Wi-Fi, ale vedle něj je počítač?
[Postav místo toho konfiguraci bridge](/guides/mctomqtt/).

## Nahraj firmware {#flash}

[Flasher](/firmware/flasher/) na tomto webu nabízí jen standardní MeshCore.
Observer firmware najdeš ve flasheru v
[DutchMeshCore Toolboxu](https://toolbox.dutchmeshcore.nl/):

1. Vyber svou desku a pak **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Poprvé zvol **Full flash**: přepíše na desce všechno včetně tabulky
   oddílů. Aktualizace aplikace zachová, co na desce je, a hodí se na pozdější
   aktualizace.
3. Nastav repeater jako obvykle: název, rádiový preset a heslo správce, jak
   popisuje [návod k repeateru](/repeater-guide/#config).

Tento firmware je sestavení **dev** a po zadání `ota update` se aktualizuje
z kanálu dev. Stabilní kanál zatím nese 1.17.1, takže pro tento návod zůstaň
na dev.

## Nastavení {#settings}

Otevři [sériovou konzoli](/firmware/console/) na tomto webu a připoj desku.
Doplň vlastní síť Wi-Fi, heslo a kód letiště a pak vlož tyto řádky jeden po
druhém:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Po restartu se deska připojí k tvé Wi-Fi a nastaví si hodiny z internetu.
Brokeři tyto hodiny potřebují, aby ověřili, kdo tvůj observer je. Bez kódu
letiště se nic nehlásí.

Radši klikáš, než píšeš? `start webconfig` spustí na desce stránku s
nastavením, na adrese, kterou konzole ukáže. Přihlas se heslem správce.

## Sloty pro brokery {#brokers}

Slot drží jednoho brokera. Firmware začíná s těmito vyplněnými sloty:

| Slot | Broker | Provozuje |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Deska bez přídavné paměti (PSRAM), třeba Heltec V3, má 3 sloty. Připojuje
se ke 2 z nich najednou, takže Analyzer ve slotu 3 se nikdy nepřipojí.
Přesuň ho do slotu 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Deska s PSRAM, třeba Heltec V4, má 6 slotů a připojuje se k 5 najednou.
Ta žádnou změnu nepotřebuje.

Tvůj uzel se ke každému brokerovi přihlašuje vlastním klíčem, takže účet
nepotřebuješ. `get mqtt.presets` vypíše ostatní komunitní brokery, které
firmware zná.

### Vlastní broker {#own}

Vlastního brokera dej do volného slotu. Doplň jeho adresu, port, uživatelské
jméno a heslo. Na desce s PSRAM je volný slot 4:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Na desce bez PSRAM použij místo toho slot 2: nahraď `mqtt4` za `mqtt2`.
Tvůj broker pak nahradí `dutchmeshcore-2`.

Port `8883` se připojuje šifrovaně (TLS), port `443` šifrovaně přes webové
spojení (websocket) a jakýkoli jiný port nešifrovaně. Můžeš zadat i celou
adresu, třeba `wss://mqtt.example.org:9002/mqtt`; pak pravidlo o portech
neplatí.

## Ověř, že to funguje {#check}

Zadej `get mqtt.status`. Každý slot ukáže svůj stav:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: připojeno.
- `wait`: slotu chybí nějaké nastavení, třeba kód letiště.
- `disc`: zatím nepřipojeno. Zkontroluj Wi-Fi příkazem `get wifi.status`.
- `fail`: slot selhal 7krát za sebou během zhruba 20 minut a teď to zkouší
  jednou za 30 minut. Zkontroluj adresu brokera a přihlašovací údaje.
- `inactive`: deska na tento slot nemá místo. Viz
  [Sloty pro brokery](#brokers).

Pak hledej název svého repeateru na
[stránce observerů v Analyzeru](https://meshcore-analyzer.eu/#observers).
Objeví se do 5 minut, spolu s tím, co slyšel.
