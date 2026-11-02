---
title: Mreža
layout: network
lead: Pogledaj mesh mrežu širom Evrope i pomozi da se vidi još više. Posmatrači (observers) slušaju mrežu i javljaju šta čuju, a svaki novi otkriva još malo.
description: 'Kako MeshCore mreža u Evropi postaje vidljiva: posmatrači javljaju šta čuju servisu MeshCore Analyzer. Brojke uživo i uputstvo kako da dodaš svog posmatrača.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-11-02'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Sama mreža ne čuva nikakav zapis: poruka ide od čvora do čvora i nestaje.
Ono što vidiš na [mapama pokrivenosti](/map/) i u statistikama potiče od
posmatrača. Posmatrač je čvor koji uz to preko protokola MQTT javlja šta čuje,
putem Wi-Fi veze ili interneta. Izveštaj ide samo u jednom smeru: ništa se ne vraća u
mrežu. Repetitor (čvor koji prosleđuje poruke) sa firmverom za posmatrača
nastavlja da prosleđuje poruke kao i ranije.

Posmatrači širom Evrope šalju izveštaje servisu [MeshCore Analyzer](https://meshcore-analyzer.eu/)
na adresi mqtt.meshcore-analyzer.eu. Analyzer čita i druge brokere, pa se računa i
posmatrač koji izveštava preko njih. Od tih izveštaja Analyzer pravi mape, statistike i
[listu kanala](/guides/channels/) na ovom sajtu.

{{< callout type="tip" >}}
Mreži ništa od ovoga nije potrebno: alati ti samo pomažu da je vidiš i planiraš. Izveštaji posmatrača, Analyzer, ove mape
i alati rade preko interneta. Kad nestane struje ili interneta, oni prestaju da rade. Mreža
i dalje prenosi poruke radio-vezom, preko svakog repetitora koji još ima
napajanje, na primer preko onih na solarni pogon.
{{< /callout >}}
