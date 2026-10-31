---
title: Rețeaua
layout: network
lead: Vezi mesh-ul din Europa și ajută-l să vadă mai mult. Observatorii ascultă mesh-ul și raportează ce aud, iar fiecare observator nou arată ceva mai mult.
description: 'Cum devine vizibil mesh-ul MeshCore din Europa: observatorii trimit ce aud către MeshCore Analyzer. Cifre live și cum îți adaugi propriul observator.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-10-31'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Mesh-ul nu păstrează nicio evidență: un mesaj trece din nod în nod și
dispare. Ce vezi pe [hărțile de acoperire](/map/) și în statistici vine de la
observatori. Un observator este un nod care raportează în plus ce aude prin MQTT,
prin Wi-Fi sau internet. Raportul merge într-o singură direcție: nimic nu se
întoarce în mesh. Un repetor (un nod care transmite mesajele mai departe) cu
firmware de observator repetă mesajele în continuare, ca înainte.

Observatorii din toată Europa raportează către [MeshCore Analyzer](https://meshcore-analyzer.eu/)
la mqtt.meshcore-analyzer.eu. Analyzer citește și alți brokeri, deci un
observator conectat acolo contează și el. Din aceste rapoarte, Analyzer construiește
hărțile, statisticile și [lista de canale](/guides/channels/) de pe acest site.

{{< callout type="tip" >}}
Mesh-ul nu are nevoie de nimic din toate acestea; instrumentele te ajută doar să-l vezi și să-l planifici. Rapoartele observatorilor, Analyzer, aceste hărți
și instrumente funcționează prin internet. La o pană de curent sau când cade internetul, ele se opresc. Mesh-ul
transmite în continuare mesajele prin radio, prin fiecare repetor care mai are
curent, de exemplu cele alimentate solar.
{{< /callout >}}
