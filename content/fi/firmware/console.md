---
title: Sarjakonsoli
layout: console
lead: Kirjoita komentoja toistimellesi selaimesta USB:n kautta.
description: Määritä MeshCore-toistin, room server tai sensori USB:n kautta Chromessa, Edgessä tai Operassa. Sarjakonsoli toimii selaimessa, eikä sinun tarvitse asentaa mitään.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-31'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Toistimella (se välittää viestejä eteenpäin), room serverillä (se tallentaa ryhmän viestit) tai sensorilla (se raportoi mittaustietoja) ei ole sovellusta. Siksi määrität sen kirjoittamalla komentoja USB:n kautta. Kytke solmusi tietokoneeseen. Avaa tämä sivu tietokoneella Chromessa, Edgessä tai Operassa ja valitse solmusi portti. Konsoli lähettää ensin komennot `get role` ja `ver`, jotta se tietää, mikä solmusi on. Kumpikin komento vain lukee tietoja. Sen jälkeen konsoli näyttää, mitä solmusi vastaa. Kirjoita komento, esimerkiksi `get name`, ja paina Enteriä. Kun kirjoitat, konsoli ehdottaa komentoja, jotka solmusi ymmärtää. Tab-näppäin täydentää niistä ensimmäisen.

Companion eli solmu, jolta lähetät viestejä, viestii sen sijaan sovelluksen kanssa USB:n kautta. Sen komentorivi on MeshCore-sovelluksessa, versiossa 1.50 tai uudemmassa.
