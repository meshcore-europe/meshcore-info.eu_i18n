---
title: Mi a MeshCore?
lead: A MeshCore rádión küld szöveges üzeneteket, csomópontról csomópontra. Nem kell hozzá internet vagy előfizetés.
description: 'Mi a MeshCore, és mi nem: a mesh, a companionök, az átjátszók és a room serverek, az útvonalválasztás, a titkosítás és a 868 MHz-es sáv Európában.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '78bc31e8'
  seeded: '2026-10-31'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['aa768ac3', 'c9b24089', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '655373a9', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b9fc8810', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '0eb54b47', '02f1fe2f', 'e6b5b258']
---

A MeshCore ingyenes szoftver kis LoRa rádiókhoz. A LoRa olyan rádiós technika,
amely kevés adatot visz messzire, nagyon kis energiával. A MeshCore-t futtató
rádió neve *csomópont*. Párosítod a telefonodon vagy laptopodon futó appal,
vagy a saját kijelzőjével és billentyűzetével használod. Így szöveget küldhetsz
több kilométerre lévő embereknek. Nincs köztetek torony, router vagy szolgáltató.

A szoftver nyílt forráskódú. A fejlesztés a
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) oldalon folyik, MIT
licenc alatt.

## Mi nem a MeshCore {#not}

Új vagy a rádiózásban? Ezeket várják az emberek a leggyakrabban a MeshCore-tól,
pedig nem képes rájuk.

- **Nem internet és nem telefon.** A MeshCore rövid szöveges üzeneteket küld,
  nagyjából akkorákat, mint egy SMS a telefonodon. Hangot, fotót, videót
  vagy weboldalt nem visz, és normál telefonszámot sem tudsz elérni vele.
- **Nem segélyhívó szolgáltatás.** A mesht egyetlen segélyszolgálat sem
  figyeli, és senki sem ígéri, hogy valaki elolvassa az üzenetedet. Vészhelyzetben
  hívd a 112-t.
- **Nem azonnali, és nem működik mindenhol.** Az üzenet rádióról rádióra ugrik.
  Ez eltarthat néhány másodpercig, de az is lehet, hogy meg sem érkezik. Az, hogy
  átjut-e, a környékbeli átjátszókon múlik, valamint a magasságon, az épületeken
  és az antennádon. Egy kis rádió beltérben gyakran senkit sem ér el; egy tetőn
  álló átjátszó kilométerekre ellát.
- **Nem szolgáltatás, amit valaki üzemeltet neked.** Nincs szolgáltató, nincs
  ügyfélszolgálat, és senki sem ígér lefedettséget. A mesh ott létezik, ahol a
  közösség tagjai átjátszókat telepítettek, máshol nem.
- **Nem minden privát rajta.** A közvetlen üzenetek titkosítottak. A Public és a
  hashtages csatornákat viszont bárki olvashatja, és a csomópontod nevét meg a
  megosztott pozíciódat mindenki látja a hatótávon belül.
  Az [observerek](/network/) nyilvános térképekre továbbítják, amit hallanak. A
  [titkosításról szóló részből](#encryption) megtudod, mi marad privát.
- **Nem korlátlan.** Egy környéken mindenki egyetlen rádiócsatornán osztozik, és
  a [868 MHz-es sáv](#band) szabályai korlátozzák, mennyi ideig adhat egy rádió.
  Minden üzenet adásidőt vesz el a többiektől. A botok, a gyakori advertek
  és a tesztüzenetek ezért mindenkinek lelassítják a mesht.
- **Nem Meshtastic.** A Meshtastic egy másik rendszer, amely nagyjából
  ugyanazokon a paneleken fut. A kettő nem tud egymással kommunikálni.

## A mesh egy percben {#mesh}

Egy LoRa rádió városban néhány kilométerre ér el, dombról vagy tetőről sokkal
messzebbre. Hogy az üzenet messzebbre jusson, a rádiók továbbadják egymás üzeneteit: ez
a *mesh*. A MeshCore-ban ezt az *átjátszóknak* nevezett rádiók végzik. Ha egy
átjátszó meghall egy üzenetet, újra elküldi, így az egy egész régión átjuthat.

A mesh senkié. Minden csomópont és minden átjátszó a közösség valamelyik tagjáé.
A mesh addig ér, ameddig az ő átjátszóik.

## A csomópontok 3 fajtája {#roles}

A csomópont fajtáját a firmware felírásakor választod ki. Az első csomópontod companion lesz.

**Companion.** A saját rádiód. Bluetooth-on vagy USB-n párosítod a telefonodon
vagy laptopodon futó MeshCore appal; némelyiknek saját kijelzője és billentyűzete van.
Az appban olvasol és gépelsz. A companion tárolja a kapcsolataidat és a csatornáidat,
valamint azokat az üzeneteket, amelyek akkor érkeztek, amikor az app nem csatlakozott. A companion nem adja tovább mások üzeneteit.

**Átjátszó.** Magasra telepített rádió, amely mindenki üzeneteit továbbadja. A
legtöbb napelemről működik. Sajátra csak ott van szükséged, ahová a mesh még nem
ér el. Nincs saját appja. USB-n állítod be, vagy jelszóval belépsz, és rádión
keresztül kezeled. Az [átjátszó-útmutató](/repeater-guide/) megmutatja, hogyan.

**Room server.** Kis üzenőfal a meshen. Amikor belépsz, megkapod azokat a
bejegyzéseket, amelyekről hatótávon kívül lemaradtál, legfeljebb az utolsó 32-t.
Csak a memóriában tárolja őket, ezért újraindításkor vagy áramszünetkor elvesznek.
Egy helyi csoport bejelentésekre használhat egyet.

## Hogyan találja meg az útját egy üzenet {#routing}

Minden csomópontnak van egy privát kulcsa és egy nyilvános kulcsa. A nyilvános kulcs az identitása.
A csomópont egy *adverttel* jelenti be magát: ez egy aláírt csomag a nevével és,
ha úgy döntesz, a pozíciójával. Valaki akkor jelenik meg a kapcsolataid között,
ha eljutott hozzád valamelyik advertje, vagy ha beolvasod a QR-kódját. Az appban egy gombbal elküldheted a sajátodat.

Egy kapcsolatnak küldött első üzeneted *floodként* megy ki. Minden átjátszó, amely
meghallja, egyszer továbbadja, és közben hozzáfűzi a saját rövid azonosítóját. A
válasz visszaviszi ezt az azonosítólistát. Ettől kezdve a kapcsolatnak küldött
üzeneteid a rögzített útvonalon haladnak, és csak az azon lévő átjátszók adnak.
Ha az útvonal megszakad, az app újra floodot küld.

A csatornaüzeneteknek nincs egyetlen címzettje, ezért mindig floodként mennek.
Az átjátszók megjegyzik, mit adtak tovább nemrég, és eldobják a másolatokat, amelyek
más útvonalon újra beérkeznek. Egy üzenet legfeljebb 64 átjátszón juthat át, vagy
32-n, ha a preset 2 bájtos azonosítókat használ.

## Titkosítás és adatvédelem {#encryption}

A közvetlen üzeneteid végponttól végpontig titkosítottak: csak te és a másik fél
olvashatjátok őket. Egy átjátszó csak egy 1 bájtos jelzésből látja, kinek szól egy csomag.

A csatornákat közös kulcs titkosítja. Hogy ki olvashatja őket, azon múlik, kinél
van meg ez a kulcs:

- A **Public** minden companionön be van állítva. A kulcsa nyilvános, így bárki
  olvashatja.
- A **hashtages csatornák**, például a `#utrecht`, a nevükből kapják a kulcsukat.
  Aki ismeri a nevet, csatlakozhat, ezért ezeket is kezeld nyilvánosként.
- A **privát csatornák** véletlen kulcsot használnak, amelyet te magad osztasz meg,
  például QR-kódként.

Az advertek alá vannak írva, de nincsenek titkosítva. A csomópontod nevét, és a
pozícióját, ha megosztod, mindenki látja a hatótávon belül. Olyan nevet válassz,
amely nem árul el többet, mint amennyit szeretnél.

## A 868 MHz-es sáv Európában {#band}

Európában a MeshCore a 868 MHz-es sáv egy kis részét használja, amelyet bárki
licenc nélkül használhat. Az európai rádiós preset, az EU/UK (Narrow),
869.618 MHz-en, 62.5 kHz-es csatornán működik. Ez a 869.40-869.65 MHz-es
alsávon belül van, ahol legfeljebb 500 mW e.r.p. megengedett. Egy eszköz ott az
idő legfeljebb 10%-ában adhat. A részleteket és az országonkénti korlátokat az
[átjátszó-útmutató jogi részében](/repeater-guide/#legal) találod.

Egy környéken mindenki ugyanazt a presetet használja, különben a rádiók nem hallják
egymást. Néhány ország és régió egy változatot használ: a
[helyi csoportod](/community/) tudja, melyiket.

## Mire használják az emberek {#uses}

- Kapcsolattartásra túrán, a tengeren és fesztiválokon, ahol a mobilhálózat
  túlterhelt vagy nincs.
- Tartalék csatornaként a családnak vagy a szomszédoknak, ha kiesik az áram
  vagy a mobilhálózat.
- Helyi csevegésre olyan rádiókon, amelyek az emberek saját tulajdonában vannak.
- Kísérletezésre rádióval, antennákkal, napenergiával és nyílt forráskódú szoftverrel.

## Honnan származnak az adatok {#data}

A [helyi csoportok](/community/) oldal keresője a [GeoNames](https://www.geonames.org/)
ingyenes település- és irányítószám-listáinak egy másolatával találja meg a helyeket.
A listák licence
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). A másolatot ez az oldal
tárolja. A keresésed nem hagyja el az eszközödet, és a GeoNames felé semmilyen kérés nem megy.
