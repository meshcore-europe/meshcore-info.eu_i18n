---
title: Első lépések
lead: Az új paneltől az első üzenetedig a mesh-en. Kell hozzá egy LoRa panel, egy számítógép Chrome-mal vagy Edge-dzsel, és egy telefon vagy laptop az apphoz.
description: Telepítsd a MeshCore-t a böngésződből, párosítsd az appot, válaszd ki a környéked rádiós beállítását, küldd el az első üzenetedet, és csatlakozz a helyi csatornához.
eyebrow: 6 lépés · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-10-31'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Ezek a lépések a MeshCore firmware v1.18.0 verzióját és a 2026 októberi hivatalos eszközöket követik. Az app menünevei verziónként kissé eltérhetnek.

## 1. Válassz eszközt {#device}

Az [eszközök oldalán](/devices/) bármelyik panel megfelel, amelynél fel van tüntetve a companion. Az első csomópontodnak válassz egy *companiont*: ez az a rádió, amelyről üzenetet küldesz. Párosítsd a telefonoddal vagy a laptopoddal Bluetooth-on vagy USB-n keresztül. Választhatsz olyat is, amelynek saját kijelzője és billentyűzete van, és önállóan működik.

A 868 MHz-es változatot szerezd be. A mellékelt antenna megfelel; az [antennás útmutatóból](/guides/antenna/) megtudod, hogyan ellenőrizheted.

{{< callout type="warning" >}}
Az antennát a rádió bekapcsolása előtt csatlakoztasd. Ha egy LoRa rádió antenna nélkül ad, károsíthatja a saját chipjét.
{{< /callout >}}

## 2. Telepítsd a firmware-t {#flash}

1. Csatlakoztasd az eszközt a számítógépedhez egy USB adatkábellel.
2. Nyisd meg a webes telepítőt a [flasher.meshcore.io](https://flasher.meshcore.io) címen, Chrome-ban vagy Edge-ben. A telepítő Web Serialt használ, ezt más böngészők nem támogatják.
3. Válaszd ki az eszközödet, majd a **Bluetooth**-os **Companion** firmware-t (vagy az USB-set, ha csak számítógéphez kábellel használod).
4. Indítsd el a telepítést. Egyes paneleket előbb frissítési módba kell tenni; a telepítő megmutatja, hogyan.

Az *erase* opciót csak tiszta újrakezdéshez használd: a törlés eltávolítja az eszköz identitását és a kapcsolataidat. A későbbi frissítéseket törlés nélkül telepítsd. Ha meg akarod tartani az identitásodat egy törlés után is, előbb exportáld a companion privát kulcsát az appból, utána pedig importáld vissza.

## 3. Telepítsd az appot {#app}

A hivatalos MeshCore app Androidra, iOS-re, Windowsra és macOS-re érhető el; a [meshcore.io](https://meshcore.io) oldalon minden verzióhoz találsz linket. Van egy webes app is az [app.meshcore.nz](https://app.meshcore.nz) címen, ez számítógépen fut Chrome-ban vagy Edge-ben.

## 4. Párosítsd a csomópontodat {#pair}

Kapcsold be a csomópontodat, nyisd meg az appot, és csatlakozz hozzá Bluetooth-on. Amikor az app PIN-t kér:

- a kijelzővel **rendelkező** csomópont kiír egy PIN-t; ezt írd be;
- a kijelző **nélküli** csomópont a `123456` kódot használja.

Ha a párosítás nem sikerül, töröld az eszközt a telefonod Bluetooth-beállításaiból, és próbáld újra. Ezután adj nevet a csomópontodnak. Ezt a nevet mások is látják, ezért ne a teljes nevedet vagy a címedet add meg, hacsak nem akarod.

## 5. Válaszd ki a környéked rádiós beállítását {#preset}

Egy környéken minden rádió ugyanazt a frekvenciát és ugyanazokat a beállításokat használja, különben nem hallják egymást. Az app rádiós beállításaiban válaszd ki a környéked előbeállítását. Az alábbi területeken kívül Európa az **EU/UK (Narrow)** beállítást használja. Hollandiának, Csehországnak, Magyarországnak, Szlovákiának, Portugáliának és Svájcnak sajátja van, a hollandiai Limburgnak pedig egy változata:

{{< presets >}}

Az eszközöd nem kínálja fel a környéked előbeállítását? Akkor írd be kézzel a táblázat 4 értékét az app rádiós beállításaiba: frekvencia, sávszélesség, spreading factor és coding rate. Az eltérő értékekkel működő csomópont nem hallja a mesh-t.

Nem vagy biztos benne? A [helyi csoportod](/community/) tudja, melyik előbeállítást használja a környéked. Az app a MeshCore projekttől tölti le ezt a listát, így egy új előbeállításhoz nem kell frissítened az appot.

## 6. Köszönj be {#hello}

1. **Mutatkozz be.** Küldj egy *advertet* az appból. A „flood” advert végigmegy az átjátszókon (ezek a csomópontok továbbítják az üzeneteket), így a mesh-en bárki felvehet téged.
   A companionök sosem mutatkoznak be maguktól.
2. **Találj meg másokat.** Az emberek akkor jelennek meg a kapcsolataid között, amikor az advertjük eljut hozzád. Az átjátszók alapértelmezés szerint 47 óránként küldenek flood advertet, így a listád feltöltődése 2 napig is eltarthat.
3. **Küldj üzenetet.** Nyiss meg egy kapcsolatot, és írj. Az első üzenet flood módon terjed a hálózaton. A címzett visszaküldi, milyen útvonalon érkezett, és a későbbi üzenetek ezt az útvonalat követik.
4. **Csatlakozz csatornákhoz.** A **Public** csatorna már be van állítva; amit oda írsz, az a mesh-en mindenkihez eljut. A régiód *hashtag-csatornáját* (`#` jellel kezdődő nevű csatorna) úgy adod hozzá, hogy beírod a nevét. A [helyi csoportod](/community/) megmondja, mely csatornák aktívak.

## Ha valami nem működik {#troubleshooting}

**Az app nem találja az eszközömet Bluetooth-on.**
Valószínűleg az USB-s companiont telepítetted. Telepítsd újra, és a Bluetooth-os változatot válaszd. A Heltec V3 kis beépített Bluetooth-antennájának rövid a hatótávja; tartsd közel a telefont.

**A párosítás folyton meghiúsul.**
Töröld az eszközt a telefonod Bluetooth-beállításaiból, indítsd újra a Bluetooth-t, és párosíts újra a kijelzőn látható PIN-nel vagy a `123456` kóddal.

**Senki sem jelenik meg a kapcsolataim között.**
Ellenőrizd, hogy az előbeállításod egyezik-e a környékedével. Küldj egy flood advertet. Ha nincs átjátszó a hatótávon belül, csak a közeli rádiókat hallod; a [térkép oldalon](/map/) látod, hol vannak átjátszók.

**Egy kapcsolatnál napokkal ezelőtti „utoljára látva” időpont áll, pedig aktív.**
A két csomópont közül az egyiknek rossz az ideje. A companion a telefonodtól veszi az időt. Az átjátszók és a room serverek (ezek a csomópontok egy csoport üzeneteit tárolják) idejét a tulajdonosuknak kell beállítania.

**Egy közvetlen üzenet sosem érkezik meg.**
Mindkettőtöknek kapcsolatként kell szerepelnie a másiknál. A csomópont eldobja az ismeretlen feladótól érkező üzenetet, és erről a feladót nem értesíti. Küldj egy flood advertet, és kérd meg a másikat is, hogy küldjön egyet. Ellenőrizd az appban, hogy automatikusan felveszi-e az új kapcsolatokat; az app csak az ugráskorláton belüli csomópontokat veszi fel.

**A régi kapcsolatok működnek, az újak sosem kapcsolódnak.**
Az első üzenet flood módon terjed, és az átjátszó csak akkor továbbítja, ha kezeli az üzenet régióját. A későbbi üzenetek egy megtanult útvonalat követnek, ezeket nem állítja meg régióellenőrzés. Kérdezd meg a [helyi csoportodat](/community/), mely régiókat kezelik a környékbeli átjátszók, és nézd meg [a környékedre vonatkozó beállításokat](/guides/settings/#traffic).

**Az app már nem csatlakozik a companionödhöz.**
Egyes paneleken van felhasználói gomb, például néhány RAK panelen és a Heltec T114-en. Tartsd lenyomva a panel indulása utáni első 8 másodpercben. A companion ekkor USB-n keresztül megnyit egy mentőkonzolt. A [flasher.meshcore.io](https://flasher.meshcore.io) konzoljában a `set pin <pin>` új Bluetooth PIN-t állít be, az `erase` pedig törli az eszközt.

**A telepítő nem tudja megnyitni a soros portot Linuxon.**
A felhasználódnak hozzá kell férnie a porthoz, például a
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0` paranccsal, vagy a `dialout` csoport tagjának kell lennie.

**Valami más.** A [MeshCore GYIK](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md) még sok más problémára kitér.
