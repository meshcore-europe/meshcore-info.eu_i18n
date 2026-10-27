---
title: Rețeaua
layout: network
lead: Vezi mesh-ul din toată Europa și ajută-l să vadă mai mult. Observatorii ascultă mesh-ul și raportează ce aud, iar fiecare observator nou arată puțin mai mult.
description: 'Cum devine vizibil mesh-ul MeshCore din Europa: observatorii raportează ce aud către MeshCore Analyzer. Cifre în timp real și cum adaugi propriul observator.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '05fa5ea3'
  seeded: '2026-10-26'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['05fa5ea3']
---

Mesh-ul în sine nu păstrează nimic: un mesaj trece de la nod la nod și apoi
dispare. Ce vezi pe [hărțile de acoperire](/map/) și în statistici vine de la
observatori. Un observator este un nod care raportează în plus ce aude, prin MQTT,
pe WiFi sau prin internet. Raportul merge într-o singură direcție: nimic nu se
întoarce în mesh. Un repetor (un nod care transmite mesajele mai departe) cu
firmware de observator repetă în continuare, ca înainte.

Observatorii din toată Europa raportează către [MeshCore Analyzer](https://meshcore-analyzer.eu/)
la mqtt.meshcore-analyzer.eu. Analyzer citește și alte brokere, așa că un
observator de acolo contează la fel. Din aceste rapoarte construiește hărțile,
statisticile și [lista de canale](/guides/channels/) de pe acest site.

{{< callout type="tip" >}}
Mesh-ul nu are nevoie de nimic din toate acestea. Rapoartele observatorilor, Analyzer,
aceste hărți și instrumente trec prin internet. La o pană de curent sau când pică
internetul, ele se opresc. Mesh-ul transmite mesajele mai departe prin radio, prin
fiecare repetor care mai are curent, cum sunt cele pe energie solară. Instrumentele
există ca să vezi și să planifici mesh-ul, nu ca să îl facă să funcționeze.
{{< /callout >}}
