---
title: Sieť
layout: network
lead: Pozri si mesh naprieč Európou a pomôž mu vidieť viac. Observery počúvajú mesh a podávajú o ňom správy. Každý nový ukáže o kúsok viac.
description: 'Ako sa mesh MeshCore v Európe stáva viditeľným: observery posielajú to, čo počujú, do MeshCore Analyzer. Živé čísla a postup, ako pridáš vlastný observer.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-11-02'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Samotný mesh nič nezaznamenáva: správa prejde z uzla na uzol a zmizne.
To, čo vidíš na [mapách pokrytia](/map/) a v štatistikách, pochádza od observerov.
Observer je uzol, ktorý navyše cez MQTT hlási, čo počuje, a to cez Wi-Fi alebo internet.
Hlásenie ide jedným smerom: do meshu sa nič nevracia.
Repeater (uzol, ktorý posúva správy ďalej) s firmvérom observera ďalej opakuje správy ako predtým.

Observery z celej Európy posielajú hlásenia do [MeshCore Analyzera](https://meshcore-analyzer.eu/)
na adrese mqtt.meshcore-analyzer.eu. Analyzer číta aj iné brokery, takže sa počíta aj observer pripojený k nim.
Z týchto hlásení zostavuje mapy, štatistiky a [zoznam kanálov](/guides/channels/) na tomto webe.

{{< callout type="tip" >}}
Mesh nič z toho nepotrebuje: nástroje ti len pomáhajú mesh vidieť a plánovať. Hlásenia observerov, Analyzer, tieto mapy
a nástroje bežia cez internet. Pri výpadku prúdu alebo internetu prestanú fungovať. Mesh
ďalej posúva správy rádiom cez každý repeater, ktorý má stále napájanie, napríklad repeatery na solárnych paneloch.
{{< /callout >}}
