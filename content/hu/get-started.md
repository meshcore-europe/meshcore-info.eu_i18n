---
title: Kezdő lépések
lead: Egy új kártyától az első üzenetedig a mesh-en. Kell egy LoRa kártya, egy számítógép Chrome vagy Edge böngészővel, és egy telefon vagy laptop az alkalmazáshoz.
description: Töltsd fel a MeshCore firmware-t a böngésződből, párosítsd az alkalmazást, válaszd ki a térségedben használt rádió-előbeállítást, küldd el az első üzenetedet és csatlakozz a helyi csatornához.
eyebrow: 6 lépés · MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '68c89544'
  seeded: '2026-10-26'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', '36a3eba3', '6da9fd7a', 'cb5fb72e', '89626504', 'a419ce79', 'aa273b20']
---

Ezek a lépések a MeshCore firmware v1.18.0 verzióját és a 2026 októberi
hivatalos eszközöket követik. Az alkalmazás menüpontjainak neve verziónként kissé eltérhet.

## 1. Válassz eszközt {#device}

Az [eszközök oldalon](/devices/) minden kártya megfelel, amelynél szerepel a companion.
Az első csomópontodnak válassz *companion*-t: ez az a rádió, amelyről üzenetet küldesz.
Párosítsd a telefonoddal vagy laptopoddal Bluetooth-on vagy USB-n, vagy válassz
olyat, amelynek saját kijelzője és billentyűzete van, és önállóan is működik.

A 868 MHz-es változatot vedd meg. A mellékelt antenna megteszi; az
[antenna útmutató](/guides/antenna/) megmutatja, hogyan ellenőrizd.

{{< callout type="warning" >}}
Csatlakoztasd az antennát, mielőtt bekapcsolod a rádiót. Ha egy LoRa rádió
antenna nélkül ad, kárt tehet a saját chipjében.
{{< /callout >}}

## 2. Töltsd fel a firmware-t {#flash}

1. Kösd az eszközt a számítógépedhez egy USB adatkábellel.
2. Nyisd meg a webes flashert a [flasher.meshcore.io](https://flasher.meshcore.io)
   címen Chrome vagy Edge böngészőben. Web Serialt használ, ami más böngészőkből hiányzik.
3. Válaszd ki az eszközödet, majd a **Companion** firmware-t **Bluetooth**-ra (vagy
   USB-re, ha csak számítógépes kábellel fogod használni).
4. Töltsd fel. Néhány kártya először frissítési módba lép; a flasher megmondja,
   hogyan.

Az *erase* (törlés) opciót csak tiszta újrakezdéshez használd: a törlés eltávolítja az eszköz
identitását és a kapcsolataidat. Későbbi frissítésekhez törlés nélkül tölts fel.

## 3. Telepítsd az alkalmazást {#app}

A hivatalos MeshCore alkalmazás elérhető Androidra, iOS-re, Windowsra és macOS-re;
a [meshcore.io](https://meshcore.io) minden változatra ad linket. Van egy
webes alkalmazás is az [app.meshcore.nz](https://app.meshcore.nz) címen, amely számítógépen
Chrome vagy Edge böngészőben fut.

## 4. Párosítsd a csomópontodat {#pair}

Kapcsold be a csomópontodat, nyisd meg az alkalmazást és csatlakozz hozzá Bluetooth-on.
Amikor PIN-kódot kér:

- a kijelző**vel** rendelkező csomópont mutat egy PIN-kódot; azt írd be;
- a kijelző **nélküli** csomópont a `123456` kódot használja.

Ha a párosítás nem sikerül, töröld az eszközt a telefonod Bluetooth beállításaiból,
és próbáld újra. Ezután adj nevet a csomópontodnak. Ezt a nevet mások is látják, ezért
ne használd a teljes nevedet vagy a címedet, hacsak nem akarod.

## 5. Válaszd ki a térséged rádió-előbeállítását {#preset}

Egy térségben minden rádió ugyanazt a frekvenciát és beállításokat használja, különben
nem hallják egymást. Az alkalmazás rádióbeállításaiban válaszd ki azt az előbeállítást, amelyet a térséged használ.
Az alábbi térségeken kívül Európa az **EU/UK (Narrow)** előbeállítást használja. Hollandia,
Csehország, Magyarország, Szlovákia, Portugália és Svájc sajátot használ, a hollandiai
Limburgnak pedig van egy változata:

{{< presets >}}

Nem vagy biztos benne? A [helyi csoportod](/community/) tudja, melyik előbeállítást használja a térséged.
Az alkalmazás ezt a listát a MeshCore projekttől tölti le, így egy új előbeállításhoz
nem kell alkalmazásfrissítés.

## 6. Köszönj be {#hello}

1. **Jelentsd be magad.** Küldj egy *advert*-et az alkalmazásból. A "flood" advert
   végigmegy az átjátszókon (ezek az üzeneteket továbbító csomópontok), így a mesh-en
   mindenki felvehet téged.
   A companionok soha nem jelentik be magukat automatikusan.
2. **Találj másokat.** Az emberek akkor jelennek meg a kapcsolataid között, amikor az advertjük eljut
   hozzád. Az átjátszók alapértelmezés szerint 47 óránként küldenek flood advertet, így a listád
   feltöltődése 2 napig is tarthat.
3. **Küldj üzenetet.** Nyiss meg egy kapcsolatot és írj. Az első üzenet flood módon
   terjed a hálózaton; a fogadó visszajelzi a megtett útvonalat, és a későbbi
   üzenetek azt az útvonalat követik.
4. **Csatlakozz csatornákhoz.** A **Public** csatorna már be van állítva; bármit
   írsz oda, a mesh-en mindenkihez eljut. Add hozzá a régiód *hashtag
   csatornáját* (`#`-tel kezdődő név) a nevének beírásával. A
   [helyi csoportod](/community/) megmondja, mely csatornák aktívak.

## Ha valami nem működik {#troubleshooting}

**Az alkalmazás nem találja az eszközömet Bluetooth-on.**
Valószínűleg az USB companiont töltötted fel. Töltsd fel újra, és válaszd a
Bluetooth változatot. A Heltec V3 kis beépített Bluetooth antennájának
rövid a hatótávolsága; tartsd közel a telefont.

**A párosítás folyton sikertelen.**
Töröld az eszközt a telefonod Bluetooth beállításaiból, indítsd újra a Bluetooth-t,
és párosíts újra a kijelzőn látható PIN-kóddal vagy a `123456` kóddal.

**Senki nem jelenik meg a kapcsolataim között.**
Ellenőrizd, hogy az előbeállításod megfelel a térségednek. Küldj flood advertet. Ha nincs
átjátszó hatótávolságon belül, csak a közeli rádiókat hallod; a
[térkép oldal](/map/) mutatja, hol vannak átjátszók.

**Egy kapcsolatnál napokkal ezelőtti "utoljára látva" idő szerepel, pedig aktív.**
A két csomópont közül az egyiken rossz az idő. A companion a telefonodtól veszi az
időt; az átjátszóknál és a room servereknél (ezek egy csoport üzeneteit tároló csomópontok)
a tulajdonosnak kell beállítania.

**A flasher nem tudja megnyitni a soros portot Linuxon.**
A felhasználódnak hozzáférés kell a porthoz, például
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, vagy tagság a `dialout`
csoportban.

**Valami más.** A
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
még sok további problémára kitér.
