---
title: MQTT na tvom observeru
lead: Neka tvoj repetitor preko Wi-Fi mreže javlja MeshCore Analyzeru što čuje. Poruke i dalje prosljeđuje kao i prije.
description: Pretvori ESP32 repetitor u MeshCore observer s DMC observer firmwareom. Flashaj ga, postavi Wi-Fi i kôd zračne luke, odaberi brokere i provjeri javlja li se MeshCore Analyzeru.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-11-02'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Observer je čvor koji uz to preko Wi-Fi mreže i MQTT-a javlja što čuje. Svaki
observer otkriva malo više mesh mreže na
[MeshCore Analyzeru](https://meshcore-analyzer.eu/) i na
[kartama pokrivenosti](/map/). U ovom vodiču od repetitora (čvora koji
prosljeđuje poruke) napravit ćeš observer. Repetitor nastavlja prosljeđivati
poruke, a izvještaji idu samo u jednom smjeru: ništa se ne vraća u mesh mrežu.

{{< callout type="warning" >}}
Ovaj vodič vrijedi za **DMC observer firmware**, observer inačicu projekta
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), temeljenu na
MeshCore 1.18.0. Standardni MeshCore nema MQTT. Sve naredbe u nastavku potječu
iz izvornog koda firmwarea, build `32dd8ad` od 19. listopada 2026.
{{< /callout >}}

## Što ti treba {#need}

- ESP32 pločica s Wi-Fi vezom, na primjer Heltec V3 ili V4, LilyGo T3S3 ili
  Xiao S3. [Izdanje](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  navodi sve pločice. nRF52 pločice poput RAK4631 nemaju Wi-Fi.
- Wi-Fi mreža na 2.4 GHz na mjestu gdje pločica stoji.
- USB podatkovni kabel te Chrome, Edge ili Opera na računalu.
- Kôd zračne luke najbliže tvom čvoru, 3 slova poput `AMS` ili `BRU`.
  Iz njega brokeri (poslužitelji koji primaju tvoje izvještaje) znaju u kojem
  je području tvoj observer.

Nemaš Wi-Fi na mjestu gdje repetitor stoji, ali pokraj njega imaš računalo?
Umjesto toga [složi konfiguraciju za most](/guides/mctomqtt/).

## Flashaj firmware {#flash}

[Flasher](/firmware/flasher/) na ovoj stranici nudi samo standardni MeshCore.
Observer firmware dobivaš preko flashera u
[DutchMeshCore Toolboxu](https://toolbox.dutchmeshcore.nl/):

1. Odaberi svoju pločicu, a zatim **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Prvi put odaberi **Full flash**: tako zamjenjuješ sve na pločici, uključujući
   particijsku tablicu. Ažuriranje aplikacije zadržava postojeći sadržaj i
   služi za kasnija ažuriranja.
3. Postavi repetitor kao i inače: ime, radijski preset i administratorsku
   lozinku, kao u [vodiču za repetitor](/repeater-guide/#config).

Ovaj je firmware **dev** inačica. Kad upišeš `ota update`, ažurira se s dev
kanala. Na stabilnom kanalu još je 1.17.1, zato za ovaj vodič ostani na dev
kanalu.

## Postavke {#settings}

Otvori [serijsku konzolu](/firmware/console/) na ovoj stranici i spoji pločicu.
Upiši svoju Wi-Fi mrežu, lozinku i kôd zračne luke, a zatim zalijepi ove retke
jedan po jedan:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Nakon ponovnog pokretanja pločica se spaja na tvoju Wi-Fi mrežu i namješta sat
preko interneta. Taj sat brokerima treba da provjere tko je tvoj observer. Bez
koda zračne luke pločica ne javlja ništa.

Radije klikaš nego tipkaš? Naredba `start webconfig` otvara stranicu s
postavkama na pločici, na adresi koju prikazuje konzola. Prijavi se svojom
administratorskom lozinkom.

## Utori za brokere {#brokers}

Jedan utor sadrži jedan broker. Firmware na početku ima popunjene ove utore:

| Utor | Broker | Vodi ga |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Pločica bez dodatne memorije (PSRAM), poput Heltec V3, ima 3 utora. Istodobno se
spaja na 2 utora, pa se Analyzer u utoru 3 nikad ne spoji. Premjesti ga u utor 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Pločica s PSRAM-om, poput Heltec V4, ima 6 utora i istodobno se spaja na 5.
Na njoj ne trebaš ništa mijenjati.

Tvoj se čvor na svaki broker prijavljuje vlastitim ključem, pa ti ne treba
korisnički račun. Naredba `get mqtt.presets` ispisuje ostale brokere zajednice
koje firmware poznaje.

### Vlastiti broker {#own}

Stavi svoj broker u slobodan utor. Upiši njegovu adresu, port, korisničko ime i
lozinku. Na pločici s PSRAM-om slobodan je utor 4:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Na pločici bez PSRAM-a umjesto toga koristi utor 2: zamijeni `mqtt4` s `mqtt2`.
Tvoj broker tada zauzima mjesto brokera `dutchmeshcore-2`.

Port `8883` spaja se šifrirano (TLS), port `443` šifrirano preko web veze
(websocket), a svaki drugi port nešifrirano. Možeš upisati i punu adresu, poput
`wss://mqtt.example.org:9002/mqtt`; tada pravilo o portovima ne vrijedi.

## Provjeri radi li {#check}

Upiši `get mqtt.status`. Uz svaki utor vidjet ćeš njegovo stanje:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: spojeno.
- `wait`: utoru nedostaje neka postavka, na primjer kôd zračne luke.
- `disc`: još nije spojeno. Provjeri Wi-Fi naredbom `get wifi.status`.
- `fail`: utor nije uspio 7 puta zaredom, u otprilike 20 minuta, i sada pokušava
  jednom svakih 30 minuta. Provjeri adresu brokera i podatke za prijavu.
- `inactive`: pločica nema mjesta za ovaj utor. Pogledaj odjeljak
  [Utori za brokere](#brokers).

Zatim potraži ime svog repetitora na
[stranici s observerima na Analyzeru](https://meshcore-analyzer.eu/#observers).
Pojavit će se u roku od 5 minuta, zajedno s onim što je čuo.
