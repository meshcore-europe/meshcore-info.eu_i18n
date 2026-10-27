---
title: CLI-commando's
layout: cli
lead: Elk commando van je repeater, room server, sensor of companion, gegroepeerd naar wat je wilt doen. Lees wat het doet en met welke waarde het begint, vul je eigen waarde in en kopieer het.
description: 'Elk commando van MeshCore firmware 1.18.0 voor repeaters, room servers, sensors en companions, gegroepeerd per taak: wat het doet, de waarde waarmee de firmware begint, en welke nodes het hebben.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-26'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
---

Deze commando's volgen MeshCore firmware 1.18.0, overgenomen uit de
broncode van de firmware. Bij een commando dat in een recente versie is toegevoegd, staat welke versie het nodig heeft. Een
repeater geeft berichten door, een room server bewaart berichten voor een groep, een sensor
rapporteert meetwaarden. Room servers, sensors en companions delen veel commando's.
Bij elk commando staat welke nodes het hebben. "Welke node?" toont alleen de commando's
van de jouwe.

Op een repeater, room server of sensor typ je ze via USB vanaf je
computer, bijvoorbeeld in de [seriële console](/firmware/console/) op deze site. De MeshCore-app stuurt ze over de mesh. De
[repeatergids](/repeater-guide/#config) laat beide zien.

Sinds 1.18 heeft ook een companion (de node waarmee je berichten stuurt, gekoppeld aan je telefoon of laptop, of
met een eigen scherm) een commandoregel. Open Command Line in de instellingen van de MeshCore-app, versie 1.50 of
later. Een contact met de Remote CLI-permissie kan je companion dezelfde
commando's over de mesh sturen. Daaronder vallen ook de WiFi- en PIN-commando's.

De waarde waarmee een commando begint, is die van de repeater. Een room server, sensor of
companion kan met een andere waarde beginnen. Een commando dat alleen een companion heeft, toont zijn eigen waarde.
