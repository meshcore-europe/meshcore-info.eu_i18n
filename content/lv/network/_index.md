---
title: Tīkls
layout: network
lead: Apskati mesh tīklu visā Eiropā un palīdzi padarīt redzamu vēl vairāk. Novērotāji uztver tīklu un ziņo par to, un katrs jauns novērotājs parāda nedaudz vairāk.
description: 'Kā MeshCore tīkls Eiropā kļūst redzams: novērotāji ziņo MeshCore Analyzer par to, ko uztver. Aktuālie skaitļi un norādes, kā pievienot savu novērotāju.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-11-02'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Pats tīkls neko neglabā: ziņa pāriet no mezgla uz mezglu un pazūd. To, ko
redzi [pārklājuma kartēs](/map/) un statistikā, sniedz novērotāji. Novērotājs
ir mezgls, kas arī ziņo par uztverto pa MQTT, izmantojot Wi-Fi vai internetu.
Ziņojums iet tikai vienā virzienā: tīklā nekas neatgriežas. Retranslators
(mezgls, kas pārsūta ziņas tālāk) ar novērotāja programmaparatūru turpina
retranslēt tāpat kā līdz šim.

Novērotāji visā Eiropā sūta ziņojumus uz [MeshCore Analyzer](https://meshcore-analyzer.eu/)
adresi mqtt.meshcore-analyzer.eu. Analyzer lasa arī citus brokerus, tāpēc ņem
vērā arī tur pieslēgtu novērotāju. No šiem ziņojumiem Analyzer veido šīs vietnes kartes,
statistiku un [kanālu sarakstu](/guides/channels/).

{{< callout type="tip" >}}
Tīklam nekas no tā nav vajadzīgs: šie rīki tikai palīdz tev to redzēt un plānot. Novērotāju ziņojumi, Analyzer, šīs kartes
un rīki darbojas internetā. Ja pazūd elektrība vai internets, tie pārstāj darboties. Tīkls
turpina pārsūtīt ziņas pa radio caur katru retranslatoru, kuram vēl ir
barošana, piemēram, caur tiem, kas strādā ar saules paneļiem.
{{< /callout >}}
