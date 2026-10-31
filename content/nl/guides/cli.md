---
title: CLI-commando's
layout: cli
lead: Alle commando's van je repeater, room server, sensor of companion, gegroepeerd naar wat je wilt doen. Lees wat een commando doet en met welke waarde het begint, vul je eigen waarde in en kopieer het.
description: 'Alle commando''s van MeshCore-firmware 1.18.0 voor repeaters, room servers, sensors en companions, gegroepeerd per taak: wat een commando doet, met welke waarde de firmware begint en welke nodes het hebben.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-31'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Deze commando's horen bij MeshCore-firmware 1.18.0. We hebben ze uit de broncode
van de firmware gehaald. Bij een commando uit een recente versie staat welke
versie je nodig hebt. Een repeater stuurt berichten door. Een room server
bewaart berichten voor een groep. Een sensor meldt meetwaarden. Room servers,
sensors en companions hebben veel commando's gemeen. Bij elk commando staat
welke nodes het kennen. Met "Welke node?" zie je alleen de commando's van jouw
node.

Op een repeater, room server of sensor typ je de commando's via USB vanaf je
computer, bijvoorbeeld in de [seriële console](/firmware/console/) op deze site. Via de MeshCore-app verstuur je ze over de mesh. In de
[repeatergids](/repeater-guide/#config) zie je beide manieren.

Sinds 1.18 heeft ook een companion een opdrachtregel. Een companion is de node waarmee je berichten verstuurt, gekoppeld aan je telefoon of laptop, of
met een eigen scherm. Open Command Line in de instellingen van de MeshCore-app,
versie 1.50 of nieuwer. Een contact met het recht Remote CLI kan je
companion dezelfde commando's over de mesh sturen. Daar horen ook de WiFi- en
PIN-commando's bij.

De beginwaarde van een commando is die van de repeater. Een room server, sensor
of companion kan met een andere waarde beginnen. Bij een commando dat alleen een
companion heeft, staat zijn eigen beginwaarde.
