---
title: Estaldura-mapak
layout: map
lead: Ikusi sarea non iristen den, nodoak non dauden eta mezuek nola egiten duten bidea. Europa osoko komunitateek kudeatzen dituzte mapa hauek.
description: MeshCore-ren zuzeneko mapak, estaldura-mapak eta pakete-analizatzaileak, Europa osorako eta herrialde bakoitzerako.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '351071aa'
  seeded: '2026-11-02'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['351071aa']
  blocks: ['dd5f039e', '9d4a2ad8', '70c417f2', '9fef7e16']
---

Nodo bat mapa hauetan agertzen da jabeak argitaratzen duenean, edo *observer* batek entzuten duenean. Observer-a entzuten duena MQTT bidez birbidaltzen duen nodoa da. Beraz, ez dago mapa osorik. Analizatzaileek beren observer-ek jasotzen duten trafikoa erakusten dute: paketeak, ibilbideak eta kanalen jarduera. Mezu zuzenak zifratuta daude, beraz analizatzaile batek ere ez du erakusten zer dioten.

Nodo bat jabeak jarri duen tokian ageri da mapan, eta toki hori okerra edo zaharkitua izan daiteke. Flood mezu batek hainbat bide egiten ditu aldi berean. Mapako ibilbidea lehenengo iritsi den kopiaren bidea da; besteen bideak ez dira erregistratzen.

Mapa hauek internet behar dute; mesh sareak ez. [Zergatik](/network/)

Errepikagailu bat (mezuak aurrera bidaltzen dituen nodoa) duzu martxan? Ezarri haren kokapena `set lat` eta `set lon` komandoekin, eta mapek kokatu ahal izango dute. [Errepikagailuen gidan](/repeater-guide/#config) ikusiko duzu nola egin.
