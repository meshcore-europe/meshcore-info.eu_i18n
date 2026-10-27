---
title: CLI-parancsok
layout: cli
lead: Az átjátszód, szobaszervered, szenzorod vagy companionod minden parancsa, aszerint csoportosítva, mit akarsz elérni. Olvasd el, mit csinál és milyen értékkel indul, írd be a sajátodat és másold ki.
description: 'A MeshCore 1.18.0 firmware minden parancsa átjátszókhoz, szobaszerverekhez, szenzorokhoz és companionokhoz, feladat szerint csoportosítva: mit csinál, milyen értékkel indul a firmware, és melyik csomópontokon van meg.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-26'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
---

Ezek a parancsok a MeshCore 1.18.0 firmware-t követik, a firmware forráskódjából
kiolvasva. Az újabb verzióban hozzáadott parancsnál ott áll, melyik verzió kell hozzá.
Az átjátszó továbbadja az üzeneteket, a szobaszerver egy csoport bejegyzéseit tárolja,
a szenzor méréseket jelent. A szobaszerverek, szenzorok és companionok sok parancson
osztoznak. Minden parancsnál ott áll, melyik csomópontokon van meg. A „Melyik csomópont?”
csak a te csomópontod parancsait mutatja.

Átjátszón, szobaszerveren vagy szenzoron USB-n keresztül gépeled be őket a számítógépedről,
például ezen az oldalon a [soros konzolban](/firmware/console/). A MeshCore app a mesh-en
küldi el őket. Az [átjátszó-útmutató](/repeater-guide/#config) mindkettőt bemutatja.

Az 1.18 óta a companionnak (a csomópont, amelyről üzenetet küldesz, a telefonoddal vagy
laptopoddal párosítva, vagy saját kijelzővel) is van parancssora. Nyisd meg a Command Line
menüpontot a MeshCore app beállításaiban, 1.50-es vagy újabb verzióban. Egy Remote CLI
jogosultsággal rendelkező kapcsolat ugyanezeket a parancsokat a mesh-en keresztül is
elküldheti a companionodnak. Ebbe a WiFi- és PIN-parancsok is beletartoznak.

Az érték, amellyel egy parancs indul, az átjátszóé. A szobaszerver, szenzor vagy companion
más értékkel indulhat. Az a parancs, amely csak companionon van meg, a saját értékét mutatja.
