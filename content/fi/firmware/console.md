---
title: Sarjakonsoli
layout: console
lead: Kirjoita komentoja toistimellesi selaimesta USB:n kautta.
description: Määritä MeshCore-toistin, huonepalvelin tai anturi USB:n kautta Chromessa, Edgessä tai Operassa selaimen sarjakonsolilla. Mitään ohjelmaa ei tarvitse asentaa.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-26'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: 'a2fe0704'}
  sections: ['c33167ce']
---

Toistimella (se välittää viestejä eteenpäin), huonepalvelimella (se tallentaa ryhmän viestit) ja anturilla (se raportoi mittauksia) ei ole sovellusta. Siksi määrität ne kirjoittamalla komentoja USB:n kautta. Kytke solmusi tietokoneeseen ja avaa tämä sivu tietokoneella Chromessa, Edgessä tai Operassa. Valitse sitten solmusi portti. Konsoli lähettää ensin komennot `get role` ja `ver`, jotta se tietää, mikä solmusi on. Kumpikin vain lukee tietoja. Sen jälkeen konsoli näyttää, mitä solmusi vastaa. Kirjoita komento, kuten `get name`, ja paina Enteriä. Kirjoittaessasi konsoli ehdottaa komentoja, jotka solmusi ymmärtää. Tab-näppäin täydentää niistä ensimmäisen.

Kumppanisolmu, eli solmu, josta lähetät viestejä, keskustelee sen sijaan sovelluksen kanssa USB:n kautta. Sen komentorivi löytyy MeshCore-sovelluksesta, versiosta 1.50 tai uudemmasta.
