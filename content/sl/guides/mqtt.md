---
title: MQTT na tvojem opazovalniku
lead: Tvoj repetitor naj prek omrežja Wi-Fi sporoča strani MeshCore Analyzer, kaj sliši. Sporočila bo še naprej posredoval kot doslej.
description: S strojno programsko opremo DMC observer spremeni repetitor ESP32 v opazovalnik MeshCore. Naloži jo, nastavi Wi-Fi in letališko kodo, izberi posrednike in preveri, ali poročila prihajajo na MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-11-02'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Opazovalnik je vozlišče, ki prek omrežja Wi-Fi in protokola MQTT tudi sporoča,
kaj sliši. Vsak opazovalnik pokaže malo več mreže na strani
[MeshCore Analyzer](https://meshcore-analyzer.eu/) in na
[zemljevidih pokritosti](/map/). V tem vodniku iz repetitorja (vozlišča, ki
posreduje sporočila) narediš opazovalnika. Repetitor še naprej posreduje
sporočila, poročila pa potujejo samo v eno smer: v mrežo se nič ne vrne.

{{< callout type="warning" >}}
Ta vodnik velja za **DMC observer firmware**, različico
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) za opazovalnike,
ki temelji na MeshCore 1.18.0. Standardni MeshCore nima podpore za MQTT. Vse
spodnje ukaze smo prebrali iz izvorne kode strojne programske opreme, različica
`32dd8ad` z dne 19. oktobra 2026.
{{< /callout >}}

## Kaj potrebuješ {#need}

- Ploščo ESP32 z Wi-Fi, na primer Heltec V3 ali V4, LilyGo T3S3 ali Xiao S3.
  Vse podprte plošče najdeš v
  [izdaji](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev).
  Plošče nRF52, na primer RAK4631, nimajo Wi-Fi.
- Omrežje Wi-Fi na 2.4 GHz tam, kjer stoji plošča.
- Podatkovni kabel USB ter Chrome, Edge ali Opero na računalniku.
- Kodo letališča, ki je najbližje tvojemu vozlišču: 3 črke, na primer `AMS` ali
  `BRU`. Po njej posredniki (strežniki, ki sprejemajo tvoja poročila) vedo, na
  katerem območju je tvoj opazovalnik.

Če ob repetitorju nimaš omrežja Wi-Fi, imaš pa zraven računalnik,
[raje sestavi konfiguracijo za most](/guides/mctomqtt/).

## Naloži strojno programsko opremo {#flash}

[Orodje za nalaganje](/firmware/flasher/) na tem spletnem mestu ponuja samo
standardni MeshCore. Strojno programsko opremo za opazovalnike naložiš z orodjem v
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Izberi svojo ploščo, nato **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Prvič izberi **Full flash**: ta možnost zamenja vse na plošči, tudi
   particijsko tabelo. Posodobitev aplikacije ohrani, kar je že na plošči, in je
   namenjena poznejšim posodobitvam.
3. Repetitor nastavi kot običajno: ime, radijsko prednastavitev in skrbniško
   geslo, kot piše v [vodniku za repetitor](/repeater-guide/#config).

Ta strojna programska oprema je različica **dev**. Ko vtipkaš `ota update`, se
posodobi s kanala dev. Na stabilnem kanalu je še vedno 1.17.1, zato za ta
vodnik ostani na kanalu dev.

## Nastavitve {#settings}

Odpri [serijsko konzolo](/firmware/console/) na tem spletnem mestu in poveži
ploščo. Vpiši svoje omrežje Wi-Fi, geslo in letališko kodo, nato prilepi te
vrstice eno za drugo:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Po ponovnem zagonu se plošča poveže s tvojim omrežjem Wi-Fi in nastavi uro prek
interneta. Posredniki to uro potrebujejo, da preverijo, kdo je tvoj opazovalnik.
Brez letališke kode plošča ne pošlje nobenega poročila.

Če raje klikaš kot tipkaš, ukaz `start webconfig` na plošči odpre stran z
nastavitvami na naslovu, ki ga pokaže konzola. Prijavi se s skrbniškim geslom.

## Reže za posrednike {#brokers}

V eni reži je en posrednik. Strojna programska oprema ima na začetku izpolnjene
te reže:

| Reža | Posrednik | Upravlja |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Plošča brez dodatnega pomnilnika (PSRAM), na primer Heltec V3, ima 3 reže.
Hkrati se poveže z 2 izmed njih, zato se Analyzer v reži 3 nikoli ne poveže.
Premakni ga v režo 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Plošča s PSRAM, na primer Heltec V4, ima 6 rež in se hkrati poveže s 5 izmed njih.
Pri njej ni treba ničesar spreminjati.

Vozlišče se pri vsakem posredniku prijavi s svojim ključem, zato računa ne
potrebuješ. Ukaz `get mqtt.presets` izpiše druge posrednike skupnosti, ki jih
strojna programska oprema pozna.

### Lasten posrednik {#own}

Svojega posrednika vpiši v prosto režo. Vnesi njegov naslov, vrata, uporabniško
ime in geslo. Na plošči s PSRAM je prosta reža 4:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Na plošči brez PSRAM uporabi režo 2: `mqtt4` zamenjaj z `mqtt2`. Tvoj posrednik
potem nadomesti `dutchmeshcore-2`.

Na vratih `8883` je povezava šifrirana (TLS), na vratih `443` šifrirana prek
spletne povezave (websocket), na vseh drugih vratih pa nešifrirana. Vpišeš lahko
tudi celoten naslov, na primer `wss://mqtt.example.org:9002/mqtt`. V tem primeru
pravilo o vratih ne velja.

## Preveri, ali deluje {#check}

Vtipkaj `get mqtt.status`. Za vsako režo se izpiše njeno stanje:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: povezava je vzpostavljena.
- `wait`: reži manjka nastavitev, na primer letališka koda.
- `disc`: povezava še ni vzpostavljena. Wi-Fi preveri z ukazom `get wifi.status`.
- `fail`: reža se v približno 20 minutah 7-krat zapored ni povezala in zdaj
  poskusi enkrat na 30 minut. Preveri naslov posrednika in prijavne podatke.
- `inactive`: plošča za to režo nima prostora. Oglej si razdelek
  [Reže za posrednike](#brokers).

Nato poišči ime svojega repetitorja na
[strani z opazovalniki v Analyzerju](https://meshcore-analyzer.eu/#observers).
Repetitor se tam pojavi v 5 minutah, skupaj s tem, kar je slišal.
