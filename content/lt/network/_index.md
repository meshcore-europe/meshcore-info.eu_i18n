---
title: Tinklas
layout: network
lead: Pažiūrėk, kaip mesh tinklas atrodo visoje Europoje, ir padėk jį pamatyti plačiau. Stebėtojai girdi tinklą ir apie jį praneša, o kiekvienas naujas parodo šiek tiek daugiau.
description: 'Kaip MeshCore mesh tinklas Europoje tampa matomas: stebėtojai praneša MeshCore Analyzer, ką girdi. Skaičiai realiuoju laiku ir kaip pridėti savo stebėtoją.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-11-02'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Pats mesh tinklas jokių įrašų nesaugo: žinutė keliauja nuo mazgo prie mazgo ir dingsta.
Tai, ką matai [aprėpties žemėlapiuose](/map/) ir statistikoje, gaunama iš
stebėtojų. Stebėtojas yra mazgas, kuris dar ir praneša, ką girdi: duomenis jis
siunčia per MQTT, naudodamas Wi-Fi arba internetą. Pranešimai keliauja tik viena
kryptimi: į tinklą niekas negrįžta. Kartotuvas (mazgas, kuris perduoda žinutes toliau)
su stebėtojo programine įranga ir toliau kartoja žinutes kaip anksčiau.

Stebėtojai visoje Europoje siunčia pranešimus į [MeshCore Analyzer](https://meshcore-analyzer.eu/)
adresu mqtt.meshcore-analyzer.eu. Analyzer skaito ir kitus brokerius, todėl ten
pranešantis stebėtojas irgi įskaičiuojamas. Iš šių pranešimų Analyzer sudaro šios
svetainės žemėlapius, statistiką ir [kanalų sąrašą](/guides/channels/).

{{< callout type="tip" >}}
Tinklui viso to nereikia: šie įrankiai tik padeda tau jį matyti ir planuoti. Stebėtojų pranešimai, Analyzer, šie žemėlapiai
ir įrankiai veikia per internetą. Dingus elektrai arba nutrūkus internetui, jie nustoja veikti.
Tinklas ir toliau perduoda žinutes radijo ryšiu per kiekvieną kartotuvą, kuris dar gauna
maitinimą, pavyzdžiui, per kartotuvus su saulės baterijomis.
{{< /callout >}}
