---
title: Kmandi tas-CLI
layout: cli
lead: Kull kmand tar-repeater, tar-room server, tas-sensor jew tal-companion tiegħek, miġbur skont dak li trid tagħmel. Aqra x'jagħmel u l-valur li jibda bih, daħħal il-valur tiegħek u kkupjah.
description: 'Kull kmand tal-firmware MeshCore 1.18.0 għal repeaters, room servers, sensors u companions, miġbur skont il-kompitu: x''jagħmel, il-valur li bih jibda l-firmware u liema nodes għandhom il-kmand.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-11-02'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Dawn il-kmandi huma dawk tal-firmware MeshCore 1.18.0, meħuda mill-kodiċi tas-sors
tal-firmware. Kmand miżjud f'verżjoni riċenti jgħidlek liema verżjoni jeħtieġ. Repeater
jgħaddi l-messaġġi 'l quddiem, room server jaħżen il-posts għal grupp, sensor jirrapporta
l-qari tiegħu. Ir-room servers, is-sensors u l-companions għandhom ħafna kmandi komuni.
Kull kmand jgħidlek f'liema nodes jinsab. "Liema node?" juri biss il-kmandi tan-node
tiegħek.

Fuq repeater, room server jew sensor, tittajpjahom mill-kompjuter tiegħek bl-USB,
pereżempju fil-[console serjali](/firmware/console/) ta' dan is-sit. L-app MeshCore tibgħathom minn fuq il-mesh. Il-[gwida
tar-repeater](/repeater-guide/#config) turi ż-żewġ modi.

Mill-1.18 'il quddiem, companion (in-node li minnu tibgħat il-messaġġi, imqabbad mat-telefon jew mal-laptop tiegħek, jew bl-iskrin tiegħu stess) għandu wkoll linja
tal-kmand. Iftaħ Command Line fis-settings tal-app MeshCore, verżjoni 1.50 jew aktar
riċenti. Kuntatt bil-permess Remote CLI jista' jibgħat lill-companion tiegħek l-istess
kmandi minn fuq il-mesh. Dan jinkludi l-kmandi tal-WiFi u tal-PIN.

Il-valur li bih jibda kmand huwa dak tar-repeater. Room server, sensor jew
companion jista' jibda b'valur ieħor. Kmand li jeżisti biss fuq companion juri l-valur tiegħu stess.
