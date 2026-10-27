---
title: Kattavuuskartat
layout: map
lead: Katso, minne mesh yltää, missä solmut ovat ja miten viestit kulkevat. Yhteisöt eri puolilla Eurooppaa ylläpitävät näitä karttoja.
description: MeshCore-karttoja reaaliajassa, kattavuuskarttoja ja pakettianalysaattoreita Euroopalle ja yksittäisille maille.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '550066cc'
  seeded: '2026-10-26'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['550066cc']
---

Solmu näkyy näillä kartoilla, kun sen omistaja julkaisee sen tai kun
*tarkkailija* kuulee sen. Tarkkailija on solmu, joka välittää kuulemansa
eteenpäin MQTT:n kautta. Yksikään kartta ei siis ole täydellinen.
Analysaattorit näyttävät liikenteen, jonka niiden tarkkailijat vastaanottavat:
paketit, reitit ja kanavien toiminnan. Yksityisviestit pysyvät salattuina,
joten mikään analysaattori ei näytä niiden sisältöä.

Nämä kartat tarvitsevat internetin, mesh ei. [Miksi](/network/)

Ylläpidätkö toistinta eli solmua, joka välittää viestejä eteenpäin? Aseta sen
sijainti komennoilla `set lat` ja `set lon`, niin kartat voivat sijoittaa sen
paikalleen. [Toistinoppaassa](/repeater-guide/#config) kerrotaan, miten se tehdään.
