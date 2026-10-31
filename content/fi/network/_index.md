---
title: Verkko
layout: network
lead: Näe mesh koko Euroopassa ja auta sitä näkymään paremmin. Observerit kuulevat meshin ja raportoivat siitä, ja jokainen uusi tuo esiin vähän lisää.
description: 'Näin MeshCore-mesh näkyy Euroopassa: observerit raportoivat kuulemansa MeshCore Analyzeriin. Ajantasaiset luvut ja ohjeet oman observerin lisäämiseen.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-10-31'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Mesh ei itse tallenna mitään: viesti kulkee solmulta solmulle ja katoaa.
Sen, mitä näet [kattavuuskartoilla](/map/) ja tilastoissa, tuottavat
observerit. Observer on solmu, joka myös raportoi kuulemansa MQTT:llä
Wi-Fin tai internetin kautta. Raportti kulkee vain yhteen suuntaan: meshiin ei
palaa mitään. Toistin (solmu, joka välittää viestejä eteenpäin), jossa on
observer-laiteohjelmisto, välittää viestejä edelleen kuten ennenkin.

Observerit eri puolilla Eurooppaa raportoivat [MeshCore Analyzeriin](https://meshcore-analyzer.eu/)
osoitteessa mqtt.meshcore-analyzer.eu. Analyzer lukee myös muita välittäjiä,
joten myös niihin raportoiva observer on mukana. Raporttien pohjalta
Analyzer kokoaa tämän sivuston kartat, tilastot ja [kanavaluettelon](/guides/channels/).

{{< callout type="tip" >}}
Mesh ei tarvitse mitään tästä. Työkalut vain auttavat sinua näkemään ja suunnittelemaan sitä. Observerien raportit, Analyzer, nämä kartat
ja työkalut kulkevat internetin kautta. Sähkökatkon aikana tai kun internet ei toimi, ne lakkaavat toimimasta.
Mesh välittää viestejä edelleen radiolla jokaisen toistimen kautta, jolla on
vielä virtaa, esimerkiksi aurinkosähköllä toimivien.
{{< /callout >}}
