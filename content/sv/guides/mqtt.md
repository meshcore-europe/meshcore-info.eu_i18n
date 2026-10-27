---
title: MQTT på din observer
lead: Låt din repeater rapportera vad den hör till MeshCore Analyzer via Wi-Fi. Den fortsätter skicka meddelanden vidare som förut.
description: Gör en ESP32-repeater till en MeshCore-observer med DMC:s observer-firmware. Flasha den, ställ in Wi-Fi och din flygplatskod, välj brokers och kontrollera att den rapporterar till MeshCore Analyzer.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-26'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
---

En observer är en nod som dessutom rapporterar vad den hör över MQTT, via
Wi-Fi. Varje observer visar lite mer av meshen på
[MeshCore Analyzer](https://meshcore-analyzer.eu/) och på
[täckningskartorna](/map/). Den här guiden gör en repeater (en nod som skickar
meddelanden vidare) till en observer. Den fortsätter repeatera, och rapporten går
bara åt ett håll: ingenting kommer tillbaka in i meshen.

{{< callout type="warning" >}}
Den här guiden gäller **DMC:s observer-firmware**, observer-bygget av
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), baserat på
MeshCore 1.18.0. Vanlig MeshCore har ingen MQTT. Alla kommandon nedan kommer från
firmwarens källkod vid bygge `32dd8ad` från den 19 oktober 2026.
{{< /callout >}}

## Det du behöver {#need}

- Ett ESP32-kort med Wi-Fi, till exempel ett Heltec V3 eller V4, ett LilyGo T3S3
  eller ett Xiao S3. [Releasen](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  listar alla kort. nRF52-kort som RAK4631 har inget Wi-Fi.
- Ett 2.4 GHz Wi-Fi-nät där kortet står.
- En USB-datakabel, och Chrome, Edge eller Opera på din dator.
- Flygplatskoden närmast din nod, 3 bokstäver som `AMS` eller `BRU`.
  Den talar om för brokrarna (servrarna som tar emot dina rapporter) i vilket
  område din observer finns.

Inget Wi-Fi där din repeater står, men en dator bredvid?
[Bygg en bridge-konfiguration](/guides/mctomqtt/) i stället.

## Flasha firmwaren {#flash}

[Flashern](/firmware/flasher/) på den här sajten har bara vanlig MeshCore.
Observer-firmwaren hämtar du med flashern i
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Välj ditt kort och sedan **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Välj **Full flash** första gången: då ersätts allt på kortet, inklusive
   partitionstabellen. App-uppdateringen behåller det som finns och är till för
   senare uppdateringar.
3. Ställ in din repeater som vanligt: namn, radioförinställning och adminlösenord,
   som i [repeaterguiden](/repeater-guide/#config).

Den här firmwaren är **dev**-bygget och uppdaterar sig själv från dev-kanalen
när du skriver `ota update`. Den stabila kanalen har fortfarande 1.17.1, så stanna
på dev för den här guiden.

## Inställningar {#settings}

Öppna [seriekonsolen](/firmware/console/) på den här sajten och anslut ditt
kort. Fyll i ditt eget Wi-Fi-nätverk, lösenord och flygplatskod, och klistra sedan
in raderna en i taget:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Efter omstarten ansluter kortet till ditt Wi-Fi och ställer klockan från
internet. Brokers behöver den klockan för att kontrollera vem din observer är. Utan
flygplatskod rapporteras ingenting.

Vill du hellre klicka än skriva? `start webconfig` öppnar en inställningssida på
kortet, på adressen som konsolen visar. Logga in med ditt adminlösenord.

## Brokerplatser {#brokers}

En plats rymmer en broker. Firmwaren levereras med de här platserna ifyllda:

| Plats | Broker | Drivs av |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Ett kort utan extra minne (PSRAM), som Heltec V3, har 3 platser. Det
ansluter till 2 av dem samtidigt, så Analyzer på plats 3 ansluter aldrig.
Flytta den till plats 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Ett kort med PSRAM, som Heltec V4, har 6 platser och ansluter till 5
samtidigt. Det behöver ingen ändring.

Din nod loggar in på varje broker med sin egen nyckel, så du behöver inget konto.
`get mqtt.presets` listar de andra community-brokers som firmwaren känner till.

### Din egen broker {#own}

Lägg din egen broker på en ledig plats. Fyll i dess adress, port, användarnamn och
lösenord. På ett kort med PSRAM är plats 4 ledig:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

På ett kort utan PSRAM använder du plats 2 i stället: byt ut `mqtt4` mot `mqtt2`.
Din broker tar då platsen för `dutchmeshcore-2`.

Port `8883` ansluter krypterat (TLS), port `443` krypterat över en
webbanslutning (websocket), och alla andra portar okrypterat. Du kan också ange
hela adressen, till exempel `wss://mqtt.example.org:9002/mqtt`; då gäller inte
portregeln.

## Kontrollera att det fungerar {#check}

Skriv `get mqtt.status`. Varje plats visar sitt läge:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: ansluten.
- `wait`: platsen saknar en inställning, till exempel flygplatskoden.
- `disc`: inte ansluten ännu. Kontrollera ditt Wi-Fi med `get wifi.status`.
- `fail`: platsen misslyckades 7 gånger i rad, under ungefär 20 minuter, och
  försöker nu en gång var 30:e minut. Kontrollera brokerns adress och inloggning.
- `inactive`: kortet har inte plats för den här platsen. Se
  [Brokerplatser](#brokers).

Leta sedan efter din repeaters namn på
[observersidan i Analyzer](https://meshcore-analyzer.eu/#observers).
Den dyker upp inom 5 minuter, med det den hört.
