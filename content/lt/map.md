---
title: Aprėpties žemėlapiai
layout: map
lead: Pažiūrėk, kur siekia tinklas, kur yra mazgai ir kaip keliauja žinutės. Šiuos žemėlapius prižiūri bendruomenės visoje Europoje.
description: Tiesioginiai MeshCore žemėlapiai, aprėpties žemėlapiai ir paketų analizatoriai Europai ir atskiroms šalims.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '351071aa'
  seeded: '2026-11-02'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['351071aa']
  blocks: ['dd5f039e', '9d4a2ad8', '70c417f2', '9fef7e16']
---

Mazgas atsiranda šiuose žemėlapiuose, kai jį paskelbia savininkas arba kai jį išgirsta
*observer*: mazgas, kuris per MQTT persiunčia tai, ką girdi. Todėl nė vienas žemėlapis
nėra išsamus. Analizatoriai rodo srautą, kurį gauna jų observer mazgai: paketus,
maršrutus ir kanalų aktyvumą. Tiesioginės žinutės lieka užšifruotos, todėl jų turinio
nerodo joks analizatorius.

Mazgas žemėlapyje yra toje vietoje, kurią nurodė jo savininkas, o ši gali būti klaidinga arba
pasenusi. Flood žinutė vienu metu keliauja keliais maršrutais. Žemėlapyje matomas maršrutas yra
tos kopijos, kuri atkeliavo pirmoji, kelias. Kitų kopijų keliai neįrašomi.

Šiems žemėlapiams reikia interneto, o tinklui jo nereikia. [Kodėl](/network/)

Turi repeater, mazgą, kuris perduoda žinutes toliau? Nustatyk jo padėtį komandomis `set lat` ir `set lon`, tada žemėlapiai
galės jį parodyti. Kaip tai padaryti, rasi [repeater vadove](/repeater-guide/#config).
