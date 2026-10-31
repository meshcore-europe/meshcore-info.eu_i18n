---
title: Příkazy CLI
layout: cli
lead: Všechny příkazy tvého repeateru, room serveru, senzoru nebo companionu, seřazené podle toho, co chceš udělat. Přečti si, co příkaz dělá a s jakou hodnotou začíná, doplň svou hodnotu a zkopíruj ho.
description: 'Všechny příkazy firmwaru MeshCore 1.18.0 pro repeatery, room servery, senzory a companiony, seřazené podle úkolu: co příkaz dělá, s jakou hodnotou firmware začíná a které uzly ho mají.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-31'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Tyto příkazy odpovídají firmwaru MeshCore 1.18.0. Vycházejí ze zdrojového kódu
firmwaru. U příkazu z nedávné verze najdeš, jakou verzi potřebuje. Repeater
předává zprávy dál, room server ukládá příspěvky pro skupinu, senzor posílá
naměřené hodnoty. Room servery, senzory a companiony mají mnoho příkazů
společných. U každého příkazu je uvedeno, které uzly ho mají. Volba „Jaký uzel?“
ti ukáže jen příkazy tvého uzlu.

Na repeateru, room serveru nebo senzoru je zadáváš přes USB ze svého
počítače, třeba v [sériové konzoli](/firmware/console/) na tomto webu. Aplikace MeshCore je posílá přes mesh. V
[návodu k repeateru](/repeater-guide/#config) najdeš obojí.

Od verze 1.18 má příkazovou řádku i companion (uzel, ze kterého píšeš zprávy,
spárovaný s telefonem nebo notebookem, případně s vlastním displejem). Otevři
Command Line v nastavení aplikace MeshCore, ve verzi 1.50 nebo
novější. Kontakt s oprávněním Remote CLI může tvému companionu posílat
stejné příkazy přes mesh. Patří k nim i příkazy pro WiFi a PIN.

Výchozí hodnota příkazu je hodnota repeateru. Room server, senzor nebo
companion může začínat s jinou hodnotou. U příkazu, který má jen companion, najdeš jeho vlastní hodnotu.
