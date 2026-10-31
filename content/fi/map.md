---
title: Peittokartat
layout: map
lead: Kartoista näet, mihin mesh ulottuu, missä solmut ovat ja miten viestit kulkevat. Yhteisöt eri puolilla Eurooppaa ylläpitävät näitä karttoja.
description: MeshCore-reaaliaikakartat, peittokartat ja pakettianalysaattorit Euroopalle ja yksittäisille maille.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '351071aa'
  seeded: '2026-10-31'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['351071aa']
  blocks: ['dd5f039e', '9d4a2ad8', '70c417f2', '9fef7e16']
---

Solmu näkyy näillä kartoilla, kun sen omistaja julkaisee sen tai kun *observer* kuulee sen. Observer on solmu, joka välittää kuulemansa eteenpäin MQTT:n kautta. Siksi mikään kartta ei ole täydellinen. Analysaattorit näyttävät liikenteen, jonka niiden observerit vastaanottavat: paketit, reitit ja kanavien aktiivisuuden. Yksityisviestit pysyvät salattuina, joten mikään analysaattori ei näytä niiden sisältöä.

Solmu näkyy kartalla siinä kohdassa, johon omistaja on sen sijoittanut. Sijainti voi olla väärä tai vanhentunut. Flood-viesti kulkee useaa reittiä yhtä aikaa. Kartalla näkyvä reitti on sen kopion reitti, joka saapui ensimmäisenä. Muita reittejä ei tallenneta.

Nämä kartat tarvitsevat internetyhteyden, mesh ei. [Miksi](/network/)

Ylläpidätkö toistinta eli solmua, joka välittää viestejä eteenpäin? Aseta sen sijainti komennoilla `set lat` ja `set lon`, niin kartat osaavat sijoittaa sen. [Toistinoppaasta](/repeater-guide/#config) näet, miten se tehdään.
