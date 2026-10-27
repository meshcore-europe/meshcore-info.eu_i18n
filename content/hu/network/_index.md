---
title: A hálózat
layout: network
lead: Nézd meg a mesh-t Európa-szerte, és segíts, hogy többet lásson. A megfigyelők hallják a mesh-t és jelentik, és minden új megfigyelő egy kicsit többet mutat.
description: 'Így válik láthatóvá a MeshCore mesh Európában: a megfigyelők jelentik, amit hallanak, a MeshCore Analyzernek. Élő számok, és hogyan adhatod hozzá a saját megfigyelődet.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '05fa5ea3'
  seeded: '2026-10-26'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['05fa5ea3']
---

A mesh maga nem tárol semmit: egy üzenet csomópontról csomópontra halad, majd eltűnik. Amit a [lefedettségi térképeken](/map/) és a statisztikákban látsz, az megfigyelőktől származik. A megfigyelő olyan csomópont, amely MQTT-n keresztül, WiFi-n vagy az interneten át jelenti is, amit hall. A jelentés egyirányú: semmi nem kerül vissza a meshbe. Egy megfigyelő firmware-t futtató átjátszó (üzeneteket továbbadó csomópont) ugyanúgy átjátszik, mint eddig.

Európa-szerte a megfigyelők a [MeshCore Analyzer](https://meshcore-analyzer.eu/) felé jelentenek, az mqtt.meshcore-analyzer.eu címen. Az Analyzer más brokereket is olvas, így az ottani megfigyelők is számítanak. Ezekből a jelentésekből építi fel a térképeket, a statisztikákat és ennek az oldalnak a [csatornalistáját](/guides/channels/).

{{< callout type="tip" >}}
A meshnek ezekből semmire nincs szüksége. A megfigyelők jelentései, az Analyzer, ezek a térképek és eszközök az interneten mennek. Áramszünetkor vagy ha az internet kiesik, leállnak. A mesh továbbra is rádión adja tovább az üzeneteket, minden olyan átjátszón át, amelynek még van árama, például a napelemeseken. Az eszközök arra valók, hogy lásd és tervezd a mesht, nem arra, hogy működtesd.
{{< /callout >}}
