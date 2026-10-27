---
title: CLI-komennot
layout: cli
lead: Kaikki toistimesi, huonepalvelimesi, anturisi tai companion-solmusi komennot ryhmiteltynä sen mukaan, mitä haluat tehdä. Lue, mitä komento tekee ja millä arvolla se alkaa, täytä oma arvosi ja kopioi se.
description: 'Kaikki MeshCore-laiteohjelmiston 1.18.0 komennot toistimille, huonepalvelimille, antureille ja companion-solmuille ryhmiteltynä tehtävän mukaan: mitä komento tekee, millä arvolla laiteohjelmisto alkaa ja missä solmuissa komento on.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-26'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
---

Nämä komennot noudattavat MeshCore-laiteohjelmiston versiota 1.18.0 ja on luettu laiteohjelmiston lähdekoodista. Tuoreessa versiossa lisätty komento kertoo, minkä version se vaatii. Toistin välittää viestejä eteenpäin, huonepalvelin tallentaa ryhmän viestit ja anturi raportoi mittauslukemia. Huonepalvelimilla, antureilla ja companion-solmuilla on monia yhteisiä komentoja. Jokainen komento kertoo, missä solmuissa se on. "Mikä solmu?" näyttää vain omien solmujesi komennot.

Toistimelle, huonepalvelimelle tai anturille kirjoitat komennot tietokoneeltasi USB:n kautta, esimerkiksi tämän sivuston [sarjakonsolissa](/firmware/console/). MeshCore-sovellus lähettää ne meshin kautta. [Toistinopas](/repeater-guide/#config) näyttää molemmat tavat.

Versiosta 1.18 alkaen myös companion-solmulla on komentorivi. Companion on solmu, josta lähetät viestejä, ja se on pariliitetty puhelimeesi tai kannettavaasi tai sillä on oma näyttö. Avaa Command Line MeshCore-sovelluksen asetuksista, versio 1.50 tai uudempi. Yhteystieto, jolla on Remote CLI -oikeus, voi lähettää companion-solmullesi samat komennot meshin kautta. Tämä koskee myös WiFi- ja PIN-komentoja.

Komennon alkuarvo on toistimen arvo. Huonepalvelimen, anturin tai companion-solmun alkuarvo voi olla toinen. Komento, joka on vain companion-solmulla, näyttää oman arvonsa.
