---
title: Võrk
layout: network
lead: Vaata võrku üle Euroopa ja aita tal näha rohkem. Vaatlejad kuulevad võrku ja annavad sellest teada, ning iga uus vaatleja näitab veidi rohkem.
description: 'Nii muutub MeshCore''i võrk Euroopas nähtavaks: vaatlejad (observer) teatavad MeshCore Analyzerile, mida nad kuulevad. Reaalajas numbrid ja juhis, kuidas lisad oma vaatleja.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-11-02'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Võrk ise midagi ei salvesta: sõnum liigub sõlmest sõlme ja kaob. See, mida näed [levikaartidel](/map/) ja statistikas, pärineb vaatlejatelt. Vaatleja (observer) on sõlm, mis annab kuuldust teada ka MQTT kaudu, üle Wi-Fi või interneti. Teade liigub ühes suunas: võrku ei tule midagi tagasi. Vaatleja püsivaraga repiiter (sõlm, mis annab sõnumeid edasi) edastab sõnumeid samamoodi nagu varem.

Vaatlejad kogu Euroopas saadavad teateid [MeshCore Analyzerile](https://meshcore-analyzer.eu/) aadressil mqtt.meshcore-analyzer.eu. Analyzer loeb ka teisi brokereid, nii et ka neile teatav vaatleja läheb arvesse. Nende teadete põhjal koostab Analyzer selle saidi kaardid, statistika ja [kanalite loendi](/guides/channels/).

{{< callout type="tip" >}}
Võrk ei vaja sellest midagi: tööriistad aitavad sul võrku ainult näha ja planeerida. Vaatlejate teated, Analyzer, need kaardid ja tööriistad töötavad interneti kaudu. Elektrikatkestuse või internetirikke ajal jäävad need seisma. Võrk jätkab sõnumite edastamist raadio teel iga repiiteri kaudu, millel on veel toide, näiteks päikesepaneeliga repiiterite kaudu.
{{< /callout >}}
