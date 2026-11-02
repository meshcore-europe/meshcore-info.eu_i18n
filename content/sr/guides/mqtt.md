---
title: MQTT na tvom observeru
lead: Neka tvoj repetitor preko Wi-Fi mreže javlja MeshCore Analyzeru šta čuje. Poruke će prosleđivati kao i do sada.
description: Pretvori ESP32 repetitor u MeshCore observer pomoću DMC observer firmvera. Fleširaj ga, podesi Wi-Fi i kôd aerodroma, izaberi brokere i proveri da li šalje izveštaje MeshCore Analyzeru.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-11-02'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Observer je čvor koji uz to javlja šta čuje, preko MQTT-a i Wi-Fi mreže. Svaki
observer otkriva još malo mreže na
[MeshCore Analyzeru](https://meshcore-analyzer.eu/) i na
[mapama pokrivenosti](/map/). Uz ovo uputstvo od repetitora (čvora koji
prosleđuje poruke) praviš observer. Čvor i dalje prosleđuje poruke, a izveštaji
idu samo u jednom smeru: ništa se ne vraća u mrežu.

{{< callout type="warning" >}}
Ovo uputstvo važi za **DMC observer firmver**, observer verziju
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) firmvera, zasnovanu
na MeshCore 1.18.0. Standardni MeshCore nema MQTT. Sve komande u nastavku
potiču iz izvornog koda firmvera, build `32dd8ad` od 19. oktobra 2026.
{{< /callout >}}

## Šta ti treba {#need}

- ESP32 ploča sa Wi-Fi vezom, na primer Heltec V3 ili V4, LilyGo T3S3 ili
  Xiao S3. [Izdanje](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  navodi sve ploče. nRF52 ploče, kao što je RAK4631, nemaju Wi-Fi.
- Wi-Fi mreža na 2.4 GHz tamo gde ploča stoji.
- USB kabl za prenos podataka i Chrome, Edge ili Opera na računaru.
- Kôd aerodroma najbližeg tvom čvoru, 3 slova, na primer `AMS` ili `BRU`.
  Po njemu brokeri (serveri koji primaju tvoje izveštaje) znaju u kojoj je
  oblasti tvoj observer.

Tamo gde ti stoji repetitor nemaš Wi-Fi, ali pored njega imaš računar?
Onda umesto toga [napravi konfiguraciju za most](/guides/mctomqtt/).

## Fleširanje firmvera {#flash}

[Fleš alat](/firmware/flasher/) na ovom sajtu sadrži samo standardni MeshCore.
Observer firmver dobijaš preko fleš alata iz
[DutchMeshCore Toolbox-a](https://toolbox.dutchmeshcore.nl/):

1. Izaberi svoju ploču, a zatim **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Prvi put izaberi **Full flash**: ta opcija zamenjuje sve na ploči, pa i tabelu
   particija. Ažuriranje aplikacije zadržava ono što je već na ploči i koristiš
   ga za kasnija ažuriranja.
3. Podesi repetitor kao i obično: ime, radio profil i administratorsku lozinku,
   kao u [uputstvu za repetitor](/repeater-guide/#config).

Ovaj firmver je **dev** verzija. Kada otkucaš `ota update`, sam se ažurira sa
dev kanala. Na stabilnom kanalu je još uvek 1.17.1, zato za ovo uputstvo ostani
na dev kanalu.

## Podešavanja {#settings}

Otvori [serijsku konzolu](/firmware/console/) na ovom sajtu i poveži ploču.
Upiši naziv svoje Wi-Fi mreže, lozinku i kôd aerodroma, pa nalepi ove redove
jedan po jedan:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Posle ponovnog pokretanja ploča se povezuje na tvoju Wi-Fi mrežu i podešava sat
preko interneta. Brokerima taj sat treba da provere ko je tvoj observer. Bez
koda aerodroma ploča ne šalje nikakve izveštaje.

Više voliš da klikćeš nego da kucaš? Komanda `start webconfig` otvara stranicu
sa podešavanjima na ploči, na adresi koju prikazuje konzola. Prijavi se svojom
administratorskom lozinkom.

## Slotovi za brokere {#brokers}

U jedan slot staje jedan broker. Firmver na početku ima popunjene ove slotove:

| Slot | Broker | Vodi ga |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Ploča bez dodatne memorije (PSRAM), kao što je Heltec V3, ima 3 slota. Istovremeno
se povezuje na 2 od njih, pa se Analyzer u slotu 3 nikada ne povezuje.
Premesti ga u slot 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Ploča sa PSRAM memorijom, kao što je Heltec V4, ima 6 slotova i istovremeno se
povezuje na 5. Na njoj ne moraš ništa da menjaš.

Tvoj čvor se kod svakog brokera prijavljuje sopstvenim ključem, pa ti nalog ne
treba. Komanda `get mqtt.presets` prikazuje ostale brokere zajednice koje firmver
poznaje.

### Tvoj broker {#own}

Stavi svog brokera u slobodan slot. Upiši njegovu adresu, port, korisničko ime i
lozinku. Na ploči sa PSRAM memorijom slot 4 je slobodan:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Na ploči bez PSRAM memorije umesto njega koristi slot 2: zameni `mqtt4` sa `mqtt2`.
Tvoj broker tada zauzima mesto brokera `dutchmeshcore-2`.

Port `8883` daje šifrovanu vezu (TLS), port `443` šifrovanu vezu preko veb
konekcije (websocket), a svaki drugi port nešifrovanu vezu. Možeš da upišeš i
celu adresu, na primer `wss://mqtt.example.org:9002/mqtt`. Tada ovo pravilo za
portove ne važi.

## Provera rada {#check}

Otkucaj `get mqtt.status`. Za svaki slot vidiš njegovo stanje:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: povezan je.
- `wait`: slotu nedostaje neko podešavanje, na primer kôd aerodroma.
- `disc`: još nije povezan. Proveri Wi-Fi komandom `get wifi.status`.
- `fail`: slot nije uspeo da se poveže 7 puta zaredom, za oko 20 minuta, i sada
  pokušava jednom na svakih 30 minuta. Proveri adresu brokera i podatke za
  prijavu.
- `inactive`: ploča nema mesta za ovaj slot. Pogledaj
  [Slotovi za brokere](#brokers).

Zatim potraži ime svog repetitora na
[stranici sa observerima u Analyzeru](https://meshcore-analyzer.eu/#observers).
Pojaviće se u roku od 5 minuta, zajedno sa onim što je čuo.
