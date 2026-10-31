---
title: A hálózat
layout: network
lead: Nézd meg a mesh-t Európa-szerte, és segíts, hogy többet lásson. A megfigyelők hallják a mesh-t, és jelentik, amit hallanak. Minden új megfigyelő egy kicsit többet mutat meg.
description: 'Így válik láthatóvá a MeshCore mesh Európában: a megfigyelők jelentik a MeshCore Analyzernek, amit hallanak. Élő számok, és hogyan adhatod hozzá a saját megfigyelődet.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-10-31'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

A mesh maga semmit nem rögzít: az üzenet csomópontról csomópontra halad, aztán
eltűnik. Amit a [lefedettségi térképeken](/map/) és a statisztikákban látsz, az
a megfigyelőktől származik. A megfigyelő (observer) olyan csomópont, amely azt is
jelenti MQTT-n, amit hall. Ezt Wi-Fin vagy az interneten keresztül küldi. A
jelentés egy irányba megy: semmi nem jut vissza a mesh-re. Az átjátszó (olyan
csomópont, amely továbbadja az üzeneteket) megfigyelő firmware-rel is ugyanúgy
továbbít, mint korábban.

Az Európa-szerte működő megfigyelők a [MeshCore Analyzernek](https://meshcore-analyzer.eu/) jelentenek,
az mqtt.meshcore-analyzer.eu címen. Az Analyzer más brokereket is olvas, így az
ott jelentő megfigyelők is számítanak. Ezekből a jelentésekből készíti el a
térképeket, a statisztikákat és az oldal [csatornalistáját](/guides/channels/).

{{< callout type="tip" >}}
A mesh-nek ezekre nincs szüksége. Az eszközök csak abban segítenek, hogy lásd és megtervezd a mesh-t. A megfigyelők jelentései, az Analyzer, ezek a térképek
és eszközök az interneten át működnek. Áramszünetben vagy internetkimaradáskor leállnak. A
mesh rádión továbbra is továbbítja az üzeneteket minden olyan átjátszón keresztül, amelynek
még van áramellátása, például a napelemeseken.
{{< /callout >}}
