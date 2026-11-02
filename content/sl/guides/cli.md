---
title: Ukazi CLI
layout: cli
lead: Vsi ukazi za tvoj repetitor, sobni strežnik, senzor ali spremljevalno napravo, razvrščeni po tem, kaj želiš narediti. Preberi, kaj ukaz naredi in katera je njegova začetna vrednost, vpiši svojo in ga kopiraj.
description: 'Vsi ukazi vdelane programske opreme MeshCore 1.18.0 za repetitorje, sobne strežnike, senzorje in spremljevalne naprave, razvrščeni po opravilih: kaj ukaz naredi, katera je njegova začetna vrednost v vdelani programski opremi in katera vozlišča ga imajo.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-11-02'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Ti ukazi veljajo za vdelano programsko opremo MeshCore 1.18.0, povzeli pa smo jih iz njene izvorne kode. Pri ukazu iz novejše različice piše, katero različico potrebuješ. Repetitor posreduje sporočila naprej, sobni strežnik hrani objave za skupino, senzor pa sporoča meritve. Sobni strežniki, senzorji in spremljevalne naprave imajo veliko skupnih ukazov. Pri vsakem ukazu piše, katera vozlišča ga imajo. Možnost »Katero vozlišče?« prikaže samo ukaze tvojega vozlišča.

Na repetitorju, sobnem strežniku ali senzorju ukaze vtipkaš z računalnika prek USB, na primer v [serijski konzoli](/firmware/console/) na tej strani. Aplikacija MeshCore jih pošlje prek omrežja mesh. [Vodnik za repetitor](/repeater-guide/#config) prikazuje oba načina.

Od različice 1.18 ima ukazno vrstico tudi spremljevalna naprava (vozlišče, s katerim pošiljaš sporočila: povezano je s telefonom ali prenosnikom ali pa ima svoj zaslon). V nastavitvah aplikacije MeshCore (različica 1.50 ali novejša) odpri Command Line. Stik z dovoljenjem Remote CLI lahko tvoji spremljevalni napravi prek omrežja mesh pošlje iste ukaze. To velja tudi za ukaze za WiFi in PIN.

Navedena začetna vrednost ukaza velja za repetitor. Sobni strežnik, senzor ali spremljevalna naprava ima lahko drugo začetno vrednost. Pri ukazu, ki ga ima samo spremljevalna naprava, je navedena njena lastna vrednost.
