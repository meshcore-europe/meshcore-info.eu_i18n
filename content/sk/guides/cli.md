---
title: Príkazy CLI
layout: cli
lead: Všetky príkazy tvojho repeatera, room servera, senzora alebo companionu, zoradené podľa toho, čo chceš urobiť. Prečítaj si, čo príkaz robí a akú má počiatočnú hodnotu, doplň vlastnú a skopíruj ho.
description: 'Všetky príkazy firmvéru MeshCore 1.18.0 pre repeatery, room servery, senzory a companiony, zoradené podľa úlohy: čo robia, s akou hodnotou firmvér začína a ktoré uzly ich majú.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-11-02'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Tieto príkazy zodpovedajú firmvéru MeshCore 1.18.0 a vychádzajú z jeho zdrojového kódu. Pri príkaze pridanom v nedávnej verzii je uvedené, ktorú verziu potrebuje. Repeater preposiela správy ďalej, room server ukladá príspevky pre skupinu a senzor odosiela namerané hodnoty. Room servery, senzory a companiony majú veľa príkazov spoločných. Pri každom príkaze je uvedené, ktoré uzly ho majú. Cez „Ktorý uzol?“ si zobrazíš iba príkazy svojho uzla.

Na repeateri, room serveri alebo senzore ich zadávaš z počítača cez USB, napríklad v [sériovej konzole](/firmware/console/) na tomto webe. Aplikácia MeshCore ich posiela cez sieť mesh. V [príručke k repeateru](/repeater-guide/#config) nájdeš oba spôsoby.

Od verzie 1.18 má príkazový riadok aj companion (uzol, z ktorého posielaš správy, spárovaný s telefónom alebo notebookom, prípadne s vlastným displejom). Otvor Command Line v nastaveniach aplikácie MeshCore, verzie 1.50 alebo novšej. Kontakt s oprávnením Remote CLI môže tvojmu companionu posielať tie isté príkazy cez sieť mesh. Patria k nim aj príkazy pre WiFi a PIN.

Uvedená počiatočná hodnota príkazu platí pre repeater. Room server, senzor alebo companion môže začínať s inou hodnotou. Pri príkaze, ktorý má iba companion, je uvedená jeho vlastná hodnota.
