---
title: CLI-komennot
layout: cli
lead: Kaikki toistimen, room serverin, sensorin tai companionin komennot ryhmiteltyinä sen mukaan, mitä haluat tehdä. Lue, mitä komento tekee ja mikä sen oletusarvo on. Täytä oma arvosi ja kopioi komento.
description: 'Kaikki MeshCore-laiteohjelmiston 1.18.0 komennot toistimille, room servereille, sensoreille ja companioneille tehtävittäin: mitä komento tekee, mikä arvo laiteohjelmistossa on oletuksena ja missä solmuissa komento on.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-31'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Nämä komennot perustuvat MeshCore-laiteohjelmiston versioon 1.18.0, ja ne on poimittu laiteohjelmiston lähdekoodista. Jos komento on lisätty hiljattain, kerromme, minkä version se vaatii. Toistin välittää viestejä eteenpäin, room server tallentaa ryhmän julkaisut ja sensori ilmoittaa mittauslukemia. Room serverillä, sensorilla ja companionilla on paljon yhteisiä komentoja. Jokaisen komennon kohdalla kerrotaan, missä solmuissa se on. "Mikä solmu?" -valinnalla näet vain oman solmusi komennot.

Toistimelle, room serverille tai sensorille kirjoitat komennot tietokoneelta USB:n kautta, esimerkiksi tämän sivuston [sarjakonsolissa](/firmware/console/). MeshCore-sovellus lähettää ne meshin kautta. [Toistinoppaassa](/repeater-guide/#config) näytetään molemmat tavat.

Versiosta 1.18 alkaen myös companionissa on komentorivi. Companion on solmu, josta lähetät viestejä. Se on pariliitetty puhelimeesi tai kannettavaasi, tai siinä on oma näyttö. Avaa Command Line MeshCore-sovelluksen asetuksista. Sovelluksen pitää olla versio 1.50 tai uudempi. Yhteystieto, jolla on Remote CLI -oikeus, voi lähettää companionillesi samat komennot meshin kautta. Tämä koskee myös WiFi- ja PIN-komentoja.

Komennon oletusarvo on toistimen arvo. Room serverin, sensorin tai companionin oletusarvo voi olla eri. Jos komento on vain companionissa, sen kohdalla näkyy companionin oma oletusarvo.
