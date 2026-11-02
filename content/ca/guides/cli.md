---
title: Ordres de la CLI
layout: cli
lead: Totes les ordres del teu repetidor, room server, sensor o companion, agrupades segons què vulguis fer. Llegeix què fa cada ordre i amb quin valor comença, posa-hi el teu valor i copia-la.
description: 'Totes les ordres del firmware 1.18.0 de MeshCore per a repetidors, room servers, sensors i companions, agrupades per tasca: què fan, amb quin valor comença el firmware i quins nodes les tenen.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-11-02'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Aquestes ordres corresponen al firmware 1.18.0 de MeshCore i surten del seu codi font.
Si una ordre s'ha afegit en una versió recent, s'hi indica quina versió necessita. Un
repetidor retransmet missatges, un room server guarda publicacions per a un grup i un sensor
envia lectures. Els room servers, els sensors i els companions comparteixen moltes ordres.
A cada ordre s'indica quins nodes la tenen. Amb "Quin node?" només veus les ordres
del teu.

En un repetidor, un room server o un sensor, les escrius des de l'ordinador per USB,
per exemple a la [consola sèrie](/firmware/console/) d'aquest lloc. Amb l'app de MeshCore, les envies per la malla. A la
[guia del repetidor](/repeater-guide/#config) trobaràs totes dues maneres.

Des de la versió 1.18, un companion (el node amb què envies missatges, vinculat al telèfon o a l'ordinador portàtil, o
amb pantalla pròpia) també té línia d'ordres. Obre Command Line a la configuració de l'app de MeshCore, versió 1.50 o
posterior. Un contacte amb el permís Remote CLI pot enviar les mateixes ordres al teu companion per la malla.
Això inclou les ordres de WiFi i de PIN.

El valor inicial que veus a cada ordre és el del repetidor. En un room server, un sensor o un
companion, el valor inicial pot ser un altre. Si l'ordre només existeix al companion, s'hi mostra el valor del companion.
