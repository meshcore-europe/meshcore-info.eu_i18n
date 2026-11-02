---
title: CLI komandas
layout: cli
lead: Visas tava retranslatora, istabas servera, sensora vai kompanjona komandas, sakārtotas pēc tā, ko vēlies izdarīt. Izlasi, ko komanda dara un ar kādu vērtību tā sākas, ieraksti savu vērtību un nokopē komandu.
description: 'Visas MeshCore programmaparatūras 1.18.0 komandas retranslatoriem, istabas serveriem, sensoriem un kompanjoniem, sakārtotas pēc uzdevuma: ko komanda dara, ar kādu vērtību programmaparatūra sākas un kuriem mezgliem šī komanda ir.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-11-02'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Šīs komandas atbilst MeshCore programmaparatūrai 1.18.0, un to saraksts ņemts no programmaparatūras
pirmkoda. Pie komandas, kas pievienota nesenā versijā, norādīta vajadzīgā versija. Retranslators pārsūta
ziņas tālāk, istabas serveris glabā grupas ierakstus, un sensors sūta rādījumus. Istabas serveriem,
sensoriem un kompanjoniem ir daudz kopīgu komandu. Pie katras komandas norādīts, kuriem mezgliem tā ir.
"Kurš mezgls?" parāda tikai tava mezgla komandas.

Retranslatorā, istabas serverī vai sensorā tu komandas ievadi no datora pa USB, piemēram, šīs vietnes [seriālajā konsolē](/firmware/console/). MeshCore lietotne tās nosūta pa mesh tīklu.
[Retranslatora ceļvedī](/repeater-guide/#config) parādīti abi veidi.

Kopš versijas 1.18 komandrinda ir arī kompanjonam (mezglam, no kura tu sūti ziņas: tas ir savienots pārī ar tavu tālruni vai klēpjdatoru,
vai tam ir savs ekrāns). Atver Command Line iestatījumos MeshCore lietotnē, kuras versija ir 1.50 vai
jaunāka. Kontakts ar Remote CLI atļauju var sūtīt tavam kompanjonam tās pašas komandas pa mesh tīklu.
Tas attiecas arī uz WiFi un PIN komandām.

Komandas sākotnējā vērtība ir retranslatora vērtība. Istabas serverim, sensoram vai
kompanjonam tā var būt cita. Komanda, kas ir tikai kompanjonam, rāda savu vērtību.
