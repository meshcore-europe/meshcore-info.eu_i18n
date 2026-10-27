---
title: Příkazy CLI
layout: cli
lead: Všechny příkazy tvého repeateru, room serveru, senzoru nebo companionu, seřazené podle toho, co chceš udělat. Přečti si, co příkaz dělá a s jakou hodnotou začíná, doplň vlastní a zkopíruj ho.
description: 'Všechny příkazy firmwaru MeshCore 1.18.0 pro repeatery, room servery, senzory a companiony, seřazené podle úkolu: co příkaz dělá, s jakou hodnotou firmware začíná a které uzly ho mají.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-26'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
---

Tyto příkazy odpovídají firmwaru MeshCore 1.18.0 a vycházejí ze zdrojového kódu firmwaru. U příkazu přidaného v nedávné verzi je uvedeno, kterou verzi potřebuje. Repeater předává zprávy dál, room server ukládá příspěvky pro skupinu, senzor hlásí naměřené hodnoty. Room servery, senzory a companiony mají mnoho příkazů společných. U každého příkazu je uvedeno, které uzly ho mají. „Který uzel?“ zobrazí jen příkazy toho tvého.

Na repeateru, room serveru nebo senzoru je zadáváš přes USB z počítače, například v [sériové konzoli](/firmware/console/) na tomto webu. Aplikace MeshCore je posílá přes mesh. [Průvodce repeaterem](/repeater-guide/#config) ukazuje obě možnosti.

Od verze 1.18 má příkazový řádek i companion (uzel, ze kterého píšeš zprávy, spárovaný s telefonem nebo notebookem, případně s vlastní obrazovkou). V nastavení aplikace MeshCore ve verzi 1.50 nebo novější otevři Command Line. Kontakt s oprávněním Remote CLI může tvému companionu posílat stejné příkazy přes mesh. To platí i pro příkazy pro WiFi a PIN.

Hodnota, se kterou příkaz začíná, platí pro repeater. Room server, senzor nebo companion může začínat s jinou hodnotou. U příkazu, který má jen companion, je uvedena jeho vlastní hodnota.
