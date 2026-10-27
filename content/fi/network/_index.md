---
title: Verkko
layout: network
lead: Katso, miltä mesh näyttää Euroopassa, ja auta sitä näkymään paremmin. Tarkkailijat kuuntelevat meshiä ja raportoivat siitä, ja jokainen uusi tarkkailija näyttää vähän enemmän.
description: 'Näin MeshCore-mesh Euroopassa tulee näkyväksi: tarkkailijat raportoivat kuulemansa MeshCore Analyzerille. Reaaliaikaiset luvut ja ohjeet oman tarkkailijan lisäämiseen.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '05fa5ea3'
  seeded: '2026-10-26'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['05fa5ea3']
---

Mesh itse ei tallenna mitään: viesti kulkee solmulta solmulle ja katoaa.
Se, mitä näet [peittokartoilla](/map/) ja tilastoissa, tulee tarkkailijoilta.
Tarkkailija on solmu, joka raportoi kuulemansa myös MQTT:n kautta, WiFi-yhteydellä
tai internetin yli. Raportti kulkee vain yhteen suuntaan: meshiin ei palaa mitään.
Toistin (solmu, joka välittää viestejä eteenpäin) jatkaa välittämistä
tarkkailijalaiteohjelmistollakin aivan kuten ennen.

Tarkkailijat eri puolilla Eurooppaa raportoivat [MeshCore Analyzerille](https://meshcore-analyzer.eu/)
osoitteeseen mqtt.meshcore-analyzer.eu. Analyzer lukee myös muita välittäjiä, joten
niihin raportoiva tarkkailija lasketaan sekin mukaan. Näistä raporteista Analyzer kokoaa
tämän sivuston kartat, tilastot ja [kanavaluettelon](/guides/channels/).

{{< callout type="tip" >}}
Mesh ei tarvitse mitään tästä. Tarkkailijoiden raportit, Analyzer sekä nämä kartat
ja työkalut kulkevat internetin yli. Sähkökatkon aikana tai internetin ollessa poikki ne pysähtyvät.
Mesh välittää viestejä radiolla edelleen jokaisen toistimen kautta, jolla on
yhä virtaa, kuten aurinkosähköllä toimivien. Työkalut ovat olemassa meshin näkemistä ja
suunnittelua varten, eivät sen pyörittämistä varten.
{{< /callout >}}
