---
title: Levialakaardid
layout: map
lead: Vaata, kuhu mesh ulatub, kus sõlmed asuvad ja kuidas sõnumid liiguvad. Neid kaarte haldavad kogukonnad üle Euroopa.
description: MeshCore'i reaalajas kaardid, levialakaardid ja pakettide analüsaatorid Euroopa ja üksikute riikide kohta.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '351071aa'
  seeded: '2026-11-02'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['351071aa']
  blocks: ['dd5f039e', '9d4a2ad8', '70c417f2', '9fef7e16']
---

Sõlm ilmub neile kaartidele siis, kui omanik selle avaldab või kui *observer* seda kuuleb. Observer on sõlm, mis edastab kuuldu MQTT kaudu. Seetõttu ei ole ükski kaart täielik. Analüsaatorid näitavad liiklust, mille nende observerid vastu võtavad: pakette, marsruute ja kanalite tegevust. Otsesõnumid jäävad krüpteerituks, seega ei näita ükski analüsaator nende sisu.

Sõlm asub kaardil seal, kuhu omanik selle paigutas, ja see koht võib olla vale või aegunud. Flood-sõnum liigub korraga mitut teed pidi. Kaardil näidatud marsruut on selle koopia tee, mis jõudis kohale esimesena. Muid marsruute ei salvestata.

Need kaardid vajavad internetti, mesh mitte. [Miks](/network/)

Kas haldad repeaterit ehk sõlme, mis sõnumeid edasi saadab? Määra selle asukoht käskudega `set lat` ja `set lon`, siis saavad kaardid selle paika panna. Kuidas seda teha, näitab [repeateri juhend](/repeater-guide/#config).
