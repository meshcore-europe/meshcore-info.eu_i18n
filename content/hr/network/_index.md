---
title: Mreža
layout: network
lead: Pogledaj mesh mrežu diljem Europe i pomozi da se vidi još više. Observeri slušaju mesh i javljaju što čuju, a svaki novi otkriva malo više.
description: 'Kako mesh mreža MeshCore u Europi postaje vidljiva: observeri javljaju što čuju MeshCore Analyzeru. Brojke uživo i upute kako dodati vlastiti observer.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-11-02'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Sam mesh ne čuva nikakav zapis: poruka prelazi s čvora na čvor i nestaje.
Ono što vidiš na [kartama pokrivenosti](/map/) i u statistikama dolazi od
observera. Observer je čvor koji uz to preko MQTT-a javlja što čuje,
putem Wi-Fi-ja ili interneta. Izvješće ide samo u jednom smjeru: ništa se ne vraća
u mesh. Repeater (čvor koji prosljeđuje poruke) s observer firmwareom
nastavlja prosljeđivati poruke kao i prije.

Observeri diljem Europe šalju izvješća [MeshCore Analyzeru](https://meshcore-analyzer.eu/)
na adresu mqtt.meshcore-analyzer.eu. Analyzer čita i druge brokere, pa se računa i
observer koji javlja njima. Iz tih izvješća Analyzer izrađuje karte,
statistike i [popis kanala](/guides/channels/) na ovim stranicama.

{{< callout type="tip" >}}
Meshu ništa od ovoga ne treba: alati ti samo pomažu da ga vidiš i planiraš. Izvješća observera, Analyzer, ove karte
i alati idu preko interneta. Kad nestane struje ili interneta, sve to prestaje raditi. Mesh
i dalje prenosi poruke radiom, preko svakog repeatera koji još ima
struju, primjerice onih na solarni pogon.
{{< /callout >}}
