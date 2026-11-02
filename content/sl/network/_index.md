---
title: Omrežje
layout: network
lead: Oglej si omrežje po Evropi in mu pomagaj, da postane bolj vidno. Opazovalci slišijo omrežje in poročajo o njem, vsak novi pa pokaže nekaj več.
description: 'Kako omrežje MeshCore v Evropi postane vidno: opazovalci orodju MeshCore Analyzer sporočajo, kaj slišijo. Številke v živo in navodila, kako dodaš svojega opazovalca.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-11-02'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Omrežje samo ne hrani nobenih zapisov: sporočilo potuje od vozlišča do vozlišča
in izgine. Kar vidiš na [zemljevidih pokritosti](/map/) in v statistiki, prihaja od
opazovalcev. Opazovalec je vozlišče, ki tudi sporoča, kaj sliši, prek MQTT po
Wi-Fi-ju ali internetu. Poročilo potuje samo v eno smer: v omrežje se nič ne vrne.
Repetitor (vozlišče, ki posreduje sporočila naprej) z vdelano programsko opremo za
opazovalce še vedno posreduje sporočila tako kot prej.

Opazovalci po vsej Evropi poročajo orodju [MeshCore Analyzer](https://meshcore-analyzer.eu/)
na naslovu mqtt.meshcore-analyzer.eu. Analyzer bere tudi druge posrednike, zato
šteje tudi opazovalec, ki poroča tja. Iz teh poročil Analyzer sestavi zemljevide,
statistiko in [seznam kanalov](/guides/channels/) na tem spletnem mestu.

{{< callout type="tip" >}}
Omrežje ne potrebuje ničesar od tega: orodja ti le pomagajo, da ga vidiš in načrtuješ. Poročila opazovalcev, Analyzer, ti zemljevidi
in orodja delujejo prek interneta. Ob izpadu elektrike ali interneta prenehajo delovati.
Omrežje še naprej prenaša sporočila po radiu, prek vsakega repetitorja, ki še ima
napajanje, na primer tistih na sončno energijo.
{{< /callout >}}
