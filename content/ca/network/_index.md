---
title: La xarxa
layout: network
lead: Mira la malla arreu d'Europa i ajuda a fer-ne visible una part més gran. Els observadors escolten la malla i n'informen, i cada observador nou en mostra una mica més.
description: 'Com es fa visible la malla de MeshCore a Europa: els observadors envien el que senten al MeshCore Analyzer. Xifres en directe i com pots afegir el teu observador.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-11-02'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

La malla no guarda cap registre: un missatge passa de node en node i
desapareix. El que veus als [mapes de cobertura](/map/) i a les estadístiques ve dels
observadors. Un observador és un node que, a més, informa per MQTT del que sent,
a través de Wi-Fi o d'internet. L'informe va en un sol sentit: res no torna a
la malla. Un repetidor (un node que retransmet missatges) amb firmware d'observador
continua retransmetent com abans.

Els observadors d'arreu d'Europa envien els informes al [MeshCore Analyzer](https://meshcore-analyzer.eu/)
a mqtt.meshcore-analyzer.eu. L'Analyzer també llegeix altres brokers, així que un
observador connectat a un d'ells també compta. A partir d'aquests informes, l'Analyzer crea els mapes, les
estadístiques i la [llista de canals](/guides/channels/) d'aquest lloc web.

{{< callout type="tip" >}}
La malla no necessita res de tot això: les eines només t'ajuden a veure-la i planificar-la. Els informes dels observadors, l'Analyzer, aquests mapes
i aquestes eines passen per internet. Si hi ha un tall de llum o cau internet, s'aturen. La
malla continua transmetent missatges per ràdio, a través de tots els repetidors que encara tenen
corrent, com els que funcionen amb energia solar.
{{< /callout >}}
