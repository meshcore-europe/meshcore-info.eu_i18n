---
title: MQTT på din observer
lead: Låt din repeater rapportera det den hör till MeshCore Analyzer via Wi-Fi. Den fortsätter att skicka vidare meddelanden som förut.
description: Gör en ESP32-repeater till en MeshCore-observer med DMC:s observer-firmware. Flasha den, ställ in Wi-Fi och din flygplatskod, välj brokrar och kontrollera att den rapporterar till MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-31'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

En observer är en nod som också rapporterar det den hör över MQTT, via
Wi-Fi. Varje observer visar lite mer av meshen på
[MeshCore Analyzer](https://meshcore-analyzer.eu/) och på
[täckningskartorna](/map/). Med den här guiden gör du en repeater (en nod som
skickar vidare meddelanden) till en observer. Den fortsätter att repetera.
Rapporten går bara åt ett håll: ingenting kommer tillbaka ut i meshen.

{{< callout type="warning" >}}
Den här guiden gäller **DMC:s observer-firmware**, observer-versionen av
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), byggd på
MeshCore 1.18.0. Vanlig MeshCore har inget MQTT. Alla kommandon nedan kommer
från firmwarens källkod i bygget `32dd8ad` från 19 oktober 2026.
{{< /callout >}}

## Det här behöver du {#need}

- Ett ESP32-kort med Wi-Fi, till exempel Heltec V3 eller V4, LilyGo T3S3 eller
  Xiao S3. [Releasen](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  listar alla kort. nRF52-kort som RAK4631 saknar Wi-Fi.
- Ett Wi-Fi-nät på 2.4 GHz där kortet står.
- En USB-kabel för data, och Chrome, Edge eller Opera på datorn.
- Flygplatskoden närmast din nod, 3 bokstäver som `AMS` eller `BRU`.
  Med den vet brokrarna (servrarna som tar emot dina rapporter) vilket område
  din observer finns i.

Har du inget Wi-Fi där repeatern står, men en dator bredvid den?
[Bygg en bryggkonfiguration](/guides/mctomqtt/) i stället.

## Flasha firmwaren {#flash}

[Flashverktyget](/firmware/flasher/) på den här webbplatsen har bara vanlig
MeshCore. Observer-firmwaren hämtar du med flashverktyget i
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Välj ditt kort och sedan **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Välj **Full flash** första gången: den ersätter allt på kortet, även
   partitionstabellen. Appuppdateringen behåller det som finns och är till för
   senare uppdateringar.
3. Ställ in repeatern som vanligt: namn, radioförval och adminlösenord, som i
   [repeaterguiden](/repeater-guide/#config).

Den här firmwaren är **dev**-bygget. Den uppdaterar sig från dev-kanalen när
du skriver `ota update`. Den stabila kanalen har fortfarande 1.17.1, så stanna
på dev för den här guiden.

## Inställningar {#settings}

Öppna [seriekonsolen](/firmware/console/) på den här webbplatsen och anslut
kortet. Fyll i ditt eget Wi-Fi-nät, lösenord och din flygplatskod. Klistra
sedan in raderna en i taget:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Efter omstarten ansluter kortet till ditt Wi-Fi och ställer klockan via
internet. Brokrarna behöver klockan för att kontrollera vem din observer är.
Utan flygplatskod rapporteras ingenting.

Klickar du hellre än skriver? Med `start webconfig` öppnar du en
inställningssida på kortet, på adressen som konsolen visar. Logga in med ditt
adminlösenord.

## Broker-platser {#brokers}

En plats rymmer en broker. Firmwaren har från början de här platserna ifyllda:

| Plats | Broker | Drivs av |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Ett kort utan extra minne (PSRAM), som Heltec V3, har 3 platser. Det ansluter
till 2 av dem samtidigt, så Analyzer på plats 3 ansluts aldrig.
Flytta den till plats 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Ett kort med PSRAM, som Heltec V4, har 6 platser och ansluter till 5
samtidigt. Där behöver du inte ändra något.

Din nod loggar in hos varje broker med sin egen nyckel, så du behöver inget
konto. Med `get mqtt.presets` ser du de andra community-brokrarna som
firmwaren känner till.

### Din egen broker {#own}

Lägg din egen broker på en ledig plats. Fyll i adress, port, användarnamn och
lösenord. På ett kort med PSRAM är plats 4 ledig:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

På ett kort utan PSRAM använder du plats 2 i stället: byt `mqtt4` mot `mqtt2`.
Din broker tar då platsen från `dutchmeshcore-2`.

Port `8883` ger en krypterad anslutning (TLS), port `443` en krypterad
anslutning via webben (websocket) och alla andra portar en okrypterad. Du kan
också ange hela adressen, till exempel `wss://mqtt.example.org:9002/mqtt`. Då
gäller inte portregeln.

## Kontrollera att det fungerar {#check}

Skriv `get mqtt.status`. Varje plats visar sin status:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: ansluten.
- `wait`: platsen saknar en inställning, till exempel flygplatskoden.
- `disc`: inte ansluten än. Kontrollera ditt Wi-Fi med `get wifi.status`.
- `fail`: platsen misslyckades 7 gånger i rad, under ungefär 20 minuter, och
  försöker nu en gång var 30:e minut. Kontrollera brokerns adress och inloggning.
- `inactive`: kortet har inte plats för den här platsen. Se
  [Broker-platser](#brokers).

Leta sedan efter din repeaters namn på
[Analyzers observer-sida](https://meshcore-analyzer.eu/#observers).
Den dyker upp inom 5 minuter, med det den har hört.
