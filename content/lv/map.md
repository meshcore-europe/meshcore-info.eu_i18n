---
title: Pārklājuma kartes
layout: map
lead: Apskati, kur sniedzas tīkls, kur atrodas mezgli un kā ceļo ziņas. Šīs kartes uztur kopienas visā Eiropā.
description: MeshCore tiešsaistes kartes, pārklājuma kartes un pakešu analizatori Eiropai un atsevišķām valstīm.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '24bfdf6b'
  seeded: '2026-11-04'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['24bfdf6b']
  blocks: ['dd5f039e', '9d4a2ad8', '763fc710', '70c417f2', '9fef7e16']
---

Mezgls parādās šajās kartēs, kad to publisko tā īpašnieks vai kad to uztver
*novērotājs*: mezgls, kas visu uztverto pārsūta pa MQTT. Tāpēc neviena karte
nav pilnīga. Analizatori rāda datplūsmu, ko saņem to novērotāji: paketes,
maršrutus un kanālu aktivitāti. Tiešās ziņas paliek šifrētas, tāpēc neviens
analizators nerāda to saturu.

Kartē mezgls atrodas tur, kur to novietojis īpašnieks, un šī vieta var būt
nepareiza vai novecojusi. Flood ziņa izplatās pa vairākiem ceļiem vienlaikus. Kartē redzamais maršruts ir
tās kopijas ceļš, kas pienāca pirmā; pārējos ceļus neviens nepieraksta.

Vai maršruts kartē šķiet neticams? Pārbaudi 2 tā mezglus ar Line of Sight
MeshCore lietotnē. [Retranslatoru ceļvedī](/repeater-guide/#check-site) ir parādīts, kā to izdarīt.

Šīm kartēm vajag internetu, bet tīklam ne. [Kāpēc](/network/)

Vai tev ir retranslators, mezgls, kas pārsūta ziņas tālāk? Iestati tā atrašanās vietu ar `set lat` un `set lon`, un kartes varēs to parādīt. Kā to izdarīt, lasi [retranslatora ceļvedī](/repeater-guide/#config).
