---
title: Mi a MeshCore?
lead: A MeshCore rádión küld szöveges üzeneteket, csomópontról csomópontra. Internet és előfizetés nélkül működik.
description: 'Mi a MeshCore, és mi nem: a mesh, a companionok, az átjátszók és a szobaszerverek, az útvonalválasztás, a titkosítás és a 868 MHz-es sáv Európában.'
eyebrow: MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '33e571f0'
  seeded: '2026-10-26'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['a3a6c1ff', '007314d2', 'f1f23981', '493b444f', '429f699c', 'f8008f48', '655373a9']
---

A MeshCore ingyenes szoftver kis LoRa rádiókhoz. A LoRa egy rádiós technika,
amely kevés adatot küld messzire, nagyon kis energiával. A MeshCore-t futtató
rádiót *csomópontnak* hívjuk. A telefonodon vagy laptopodon futó apphoz
párosítva, vagy saját kijelzővel és billentyűzettel, kilométerekre lévő
embereknek küld szöveget. Nincs közben torony, router vagy szolgáltató.

A MeshCore csak rövid szöveges üzeneteket küld: hangot, fotót vagy
internetforgalmat nem.
Egy üzenet néhány másodpercig is tarthat, és az, hogy megérkezik-e, a
környékbeli átjátszóktól függ. Nem helyettesíti a segélyhívó szolgálatokat:
vészhelyzetben hívd a 112-et.

A szoftver nyílt forráskódú, fejlesztése a
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) címen folyik MIT
licenc alatt.

## A mesh egy percben {#mesh}

Egy LoRa rádió városban néhány kilométerre ér el, dombról vagy háztetőről
sokkal messzebbre. A nagyobb távolsághoz a rádiók továbbadják egymásnak az
üzeneteket: ez a *mesh*. A MeshCore-ban a továbbadást az *átjátszónak*
nevezett rádiók végzik. Az átjátszó, amelyik hall egy üzenetet, újra elküldi,
így az egy egész régiót átszelhet.

A mesh nem tulajdona senkinek. Minden csomópont és minden átjátszó a közösség
egy tagjáé. A mesh annyit ér, amennyit az emberek által kihelyezett átjátszók.

## A csomópontok 3 fajtája {#roles}

A csomópont fajtáját flashelésnél választod ki. Az első csomópontod egy companion.

**Companion.** A saját rádiód. Bluetooth-on vagy USB-n párosítod a telefonodon
vagy laptopodon futó MeshCore apphoz; egyeseknek saját kijelzőjük és
billentyűzetük van. Az appban olvasod és írod az üzeneteket. A companion
tárolja a kapcsolataidat és csatornáidat, valamint azokat az üzeneteket,
amelyek akkor érkeztek, amikor az app nem volt csatlakoztatva. A companion
nem továbbít üzeneteket mások számára.

**Átjátszó.** Magasra helyezett rádió, amely mindenki üzeneteit továbbadja.
A legtöbb napenergiáról működik. Sajátra csak ott van szükséged, ahová a mesh
még nem ér el. Nincs saját appja. USB-n állítod be, vagy jelszóval
bejelentkezve rádión keresztül kezeled. Az
[átjátszó-útmutató](/repeater-guide/) megmutatja, hogyan.

**Szobaszerver.** Kis üzenőfal a meshen. Bejelentkezéskor megkapod a
hatótávon kívül kihagyott bejegyzéseket, legfeljebb az utolsó 32-t. Egy helyi
csoport bejelentésekre használja.

## Hogyan talál utat egy üzenet {#routing}

Minden csomópontnak van egy titkos kulcsa és egy nyilvános kulcsa. A nyilvános
kulcs az identitása. A csomópont *adverttel* jelenti be magát: ez egy aláírt
csomag a nevével és, ha úgy döntesz, a pozíciójával. Valaki akkor jelenik meg
a kapcsolataid között, ha egy advertje eljutott hozzád, vagy ha beolvasod a
QR-kódját. Az appban van egy gomb a sajátod elküldésére.

Egy kapcsolatnak küldött első üzeneted *floodként* indul. Minden átjátszó,
amelyik hallja, egyszer továbbadja, és közben hozzáfűzi a saját rövid
azonosítóját. A válasz visszahozza ezt az azonosítólistát. Ettől fogva az
ennek a kapcsolatnak szóló üzeneteid a rögzített útvonalon haladnak, és csak
az azon lévő átjátszók adnak. Ha az útvonal megszakad, az app újra floodol.

A csatornára küldött üzeneteknek nincs egyetlen címzettjük, így mindig
floodolnak. Az átjátszók megjegyzik, mit adtak tovább nemrég, és eldobják a
másik útvonalon újra beérkező másolatokat. Egy üzenet legfeljebb 64 átjátszón
haladhat át, vagy 32-n, ahol a preset 2 bájtos azonosítókat használ.

## Titkosítás és adatvédelem {#encryption}

A közvetlen üzeneteid végpontok között titkosítottak: csak te és a másik fél
olvashatja őket. Az átjátszó csak egy 1 bájtos utalást lát arról, kinek szól a
csomag.

A csatornákat közös kulcs titkosítja, így az olvashatja őket, akinek megvan ez
a kulcs:

- A **Public** minden companionon be van állítva. A kulcsa nyilvános, így
  bárki olvashatja.
- A **hashtag-csatornák**, például a `#utrecht`, a nevükből képzik a
  kulcsukat. Bárki csatlakozhat, aki ismeri a nevet, ezért kezeld ezeket is
  nyilvánosként.
- A **privát csatornák** véletlen kulcsot használnak, amelyet te magad osztasz
  meg, például QR-kódként.

Az advertek aláírtak, de nem titkosítottak. A csomópontod neve, és ha megosztod,
a pozíciója, mindenki számára látható a hatótávon belül. Olyan nevet válassz,
amely nem árul el többet, mint amennyit szeretnél.

## A 868 MHz-es sáv Európában {#band}

Európában a MeshCore a 868 MHz-es sáv egy kis részét használja, amelyet bárki
engedély nélkül használhat. Az európai rádiós presetje, az EU/UK (Narrow),
869.618 MHz-en ül egy 62.5 kHz-es csatornán. Ez a 869.40-869.65 MHz-es
alsávon belül van, amely legfeljebb 500 mW e.r.p. teljesítményt enged. Egy
eszköz ott az idő legfeljebb 10%-ában adhat. Az
[átjátszó-útmutató jogi része](/repeater-guide/#legal) tartalmazza a
részleteket és az országonkénti korlátokat.

Egy területen mindenki ugyanazt a presetet használja, különben a rádióik nem
hallják egymást. Egyes országok és régiók egy változatot használnak: a
[helyi csoportod](/community/) tudja, melyiket.

## Mire használják az emberek {#uses}

- Kapcsolattartásra túrán, tengeren és fesztiválokon, ahol a mobilhálózat
  túlterhelt vagy hiányzik.
- Tartalék csatornaként a családnak vagy a szomszédoknak, ha az áram vagy a
  mobilhálózat kiesik.
- Helyi csevegésre saját tulajdonú rádiókon.
- Kísérletezésre rádióval, antennákkal, napenergiával és nyílt forráskódú
  szoftverrel.
