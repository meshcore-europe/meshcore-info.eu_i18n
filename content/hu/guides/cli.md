---
title: CLI-parancsok
layout: cli
lead: Az átjátszód, a room servered, a szenzorod vagy a companionöd összes parancsa, aszerint csoportosítva, hogy mit szeretnél csinálni. Elolvasod, mit csinál, és milyen értékkel indul, beírod a sajátodat, és kimásolod.
description: 'A MeshCore 1.18.0-s firmware összes parancsa átjátszókhoz, room serverekhez, szenzorokhoz és companionökhöz, feladat szerint csoportosítva: mit csinál, milyen értékkel indul a firmware-ben, és melyik csomópontokon érhető el.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-31'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Ezek a parancsok a MeshCore 1.18.0-s firmware-t követik, a firmware forráskódja alapján. Az újabb verzióban megjelent parancsoknál ott áll, melyik verzió kell hozzájuk. Az átjátszó továbbítja az üzeneteket, a room server egy csoport bejegyzéseit tárolja, a szenzor méréseket küld. A room serverek, a szenzorok és a companionök sok parancsot közösen használnak. Minden parancsnál ott áll, melyik csomópontokon érhető el. A „Melyik csomópont?” résznél csak a te csomópontod parancsait látod.

Átjátszón, room serveren vagy szenzoron USB-n keresztül írod be őket a számítógépedről, például az oldal [soros konzoljában](/firmware/console/). A MeshCore app a mesh hálózaton keresztül küldi el őket. Az [átjátszó-útmutató](/repeater-guide/#config) mindkét módot bemutatja.

Az 1.18 óta a companionnek is van parancssora. A companion az a csomópont, amelyről üzenetet küldesz: a telefonodhoz vagy a laptopodhoz párosítod, vagy saját kijelzője van. A MeshCore app 1.50-es vagy újabb verziójában a beállításoknál nyisd meg a Command Line menüpontot. Ha egy kapcsolatnak Remote CLI jogosultsága van, ugyanezeket a parancsokat küldheti a companionödnek a mesh hálózaton keresztül. Ebbe a WiFi- és a PIN-parancsok is beletartoznak.

A parancsoknál megadott kezdőérték az átjátszó értéke. A room server, a szenzor vagy a companion más értékről is indulhat. A csak companionön elérhető parancsok a saját kezdőértéküket mutatják.
