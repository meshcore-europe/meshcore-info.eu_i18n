---
title: MQTT na tvém observeru
lead: Tvůj repeater bude přes Wi-Fi hlásit MeshCore Analyzeru, co slyší. Zprávy přitom předává dál jako dosud.
description: Udělej z ESP32 repeateru MeshCore observer s DMC observer firmwarem. Nahraj ho, nastav Wi-Fi a kód letiště, vyber brokery a ověř, že hlásí do MeshCore Analyzeru.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-31'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Observer je uzel, který navíc přes Wi-Fi hlásí po MQTT, co slyší. Každý
observer ukáže na [MeshCore Analyzeru](https://meshcore-analyzer.eu/) a na
[mapách pokrytí](/map/) zase kousek mesh sítě navíc. Podle tohoto návodu
uděláš observer z repeateru (uzlu, který předává zprávy dál). Repeater dál
předává zprávy. Hlášení jde jen jedním směrem: do mesh sítě se nic nevrací.

{{< callout type="warning" >}}
Tento návod platí pro **DMC observer firmware**, observer verzi
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) postavenou na
MeshCore 1.18.0. Běžný MeshCore MQTT nemá. Všechny příkazy níže pocházejí ze
zdrojového kódu firmwaru, build `32dd8ad` z 19. října 2026.
{{< /callout >}}

## Co potřebuješ {#need}

- Desku ESP32 s Wi-Fi, třeba Heltec V3 nebo V4, LilyGo T3S3 nebo Xiao S3.
  Všechny desky najdeš ve
  [vydání](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev).
  Desky nRF52, třeba RAK4631, Wi-Fi nemají.
- Wi-Fi síť 2.4 GHz v místě, kde deska stojí.
- Datový USB kabel a v počítači Chrome, Edge nebo Opera.
- Kód letiště nejblíž tvému uzlu, 3 písmena jako `AMS` nebo `BRU`.
  Podle něj brokery (servery, které přijímají tvá hlášení) poznají, v jaké
  oblasti tvůj observer je.

U repeateru nemáš Wi-Fi, ale stojí vedle něj počítač?
Místo toho si [sestav konfiguraci mostu](/guides/mctomqtt/).

## Nahraj firmware {#flash}

[Flasher](/firmware/flasher/) na tomto webu nabízí jen běžný MeshCore.
Observer firmware nahraješ flasherem v
[DutchMeshCore Toolboxu](https://toolbox.dutchmeshcore.nl/):

1. Vyber svou desku a pak **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Poprvé zvol **Full flash**: přepíše na desce všechno, i tabulku oddílů.
   Aktualizace aplikace zachová, co na desce je, a slouží pro pozdější
   aktualizace.
3. Nastav repeater jako obvykle: jméno, rádiový preset a heslo správce, podle
   [návodu k repeateru](/repeater-guide/#config).

Tento firmware je **dev** build. Když napíšeš `ota update`, aktualizuje se
z kanálu dev. Stabilní kanál má pořád 1.17.1, proto pro tento návod zůstaň
na dev.

## Nastavení {#settings}

Otevři na tomto webu [sériovou konzoli](/firmware/console/) a připoj desku.
Doplň svou Wi-Fi síť, heslo a kód letiště a vlož tyto řádky jeden po druhém:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Po restartu se deska připojí k tvé Wi-Fi a nastaví si hodiny z internetu.
Podle těchto hodin brokery ověřují, kdo tvůj observer je. Bez kódu letiště
se nic nehlásí.

Raději klikáš než píšeš? Příkaz `start webconfig` otevře na desce stránku
s nastavením, na adrese, kterou ukáže konzole. Přihlas se heslem správce.

## Sloty pro brokery {#brokers}

Do jednoho slotu patří jeden broker. Firmware má od začátku vyplněné tyto
sloty:

| Slot | Broker | Provozuje |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Deska bez přídavné paměti (PSRAM), třeba Heltec V3, má 3 sloty. Připojí se
najednou ke 2 z nich, takže Analyzer ve slotu 3 se nikdy nepřipojí.
Přesuň ho do slotu 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Deska s PSRAM, třeba Heltec V4, má 6 slotů a připojí se najednou k 5.
Nic měnit nemusíš.

Tvůj uzel se ke každému brokeru přihlašuje vlastním klíčem, takže účet
nepotřebuješ. Příkaz `get mqtt.presets` vypíše další komunitní brokery, které
firmware zná.

### Vlastní broker {#own}

Vlastní broker dej do volného slotu. Vyplň jeho adresu, port, uživatelské
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

Port `8883` se připojí šifrovaně (TLS), port `443` šifrovaně přes webové
spojení (websocket) a každý jiný port nešifrovaně. Můžeš zadat i celou
adresu, třeba `wss://mqtt.example.org:9002/mqtt`. Pravidlo pro porty pak
neplatí.

## Ověř, že to funguje {#check}

Napiš `get mqtt.status`. U každého slotu uvidíš jeho stav:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: připojeno.
- `wait`: slotu chybí nějaké nastavení, třeba kód letiště.
- `disc`: zatím nepřipojeno. Zkontroluj Wi-Fi příkazem `get wifi.status`.
- `fail`: slot selhal 7krát za sebou, zhruba během 20 minut, a teď to zkouší
  jednou za 30 minut. Zkontroluj adresu brokeru a přihlašovací údaje.
- `inactive`: deska nemá pro tento slot místo. Viz
  [Sloty pro brokery](#brokers).

Pak najdi jméno svého repeateru na
[stránce observerů v Analyzeru](https://meshcore-analyzer.eu/#observers).
Objeví se do 5 minut i s tím, co slyšel.
