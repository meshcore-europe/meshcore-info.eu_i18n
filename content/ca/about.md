---
title: Què és MeshCore?
lead: MeshCore envia missatges de text per ràdio, de node a node. Funciona sense internet i sense cap subscripció.
description: 'Què és MeshCore i què no és: la malla, els companions, els repetidors i els room servers, l''encaminament, el xifratge i la banda de 868 MHz a Europa.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '78bc31e8'
  seeded: '2026-11-02'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['aa768ac3', 'c9b24089', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '655373a9', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b9fc8810', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '0eb54b47', '02f1fe2f', 'e6b5b258']
---

MeshCore és programari lliure per a ràdios LoRa petites. LoRa és una tècnica de ràdio que envia poques dades molt lluny amb molt poca energia. Una ràdio amb MeshCore s'anomena *node*. Connectat a l'app del teu mòbil o ordinador, o amb pantalla i teclat propis, envia text a persones que són a quilòmetres de distància. Entremig no hi ha cap torre, cap encaminador ni cap proveïdor.

El programari és de codi obert i es desenvolupa a
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore), amb llicència MIT.

## Què no és MeshCore {#not}

Comences amb la ràdio? Això és el que la gent espera més sovint de MeshCore i que no fa.

- **No és internet ni un telèfon.** MeshCore envia missatges de text curts, més o menys de la llargada d'un SMS del teu mòbil. Res de veu, fotos, vídeo ni webs, i no pots contactar amb un número de telèfon normal.
- **No és un servei d'emergències.** Cap servei d'emergències escolta la malla, i ningú no garanteix que algú llegeixi el teu missatge. En una emergència, truca al 112.
- **No és instantani ni arriba a tot arreu.** Un missatge salta de ràdio en ràdio i pot trigar uns segons, o no arribar mai. Que arribi o no depèn dels repetidors que tens a prop, de l'alçada, dels edificis i de la teva antena. Una ràdio petita a l'interior sovint no arriba a ningú; un repetidor en un terrat arriba a quilòmetres de distància.
- **No és un servei que algú gestioni per a tu.** No hi ha proveïdor, ni servei d'assistència, ni cap garantia de cobertura. La malla existeix on la gent de la comunitat ha instal·lat repetidors, i enlloc més.
- **No tot és privat.** Els missatges directes van xifrats, però qualsevol pot llegir Public i els canals hashtag. Tothom qui estigui a l'abast veu el nom del teu node i la posició que comparteixes. Els [observadors](/network/) envien a mapes públics el que senten. La [secció de xifratge](#encryption) explica què es manté privat.
- **No és il·limitat.** Tothom d'una mateixa zona comparteix un sol canal de ràdio, i les normes de la [banda de 868 MHz](#band) limiten quant de temps pot emetre cada ràdio. Cada missatge treu temps d'emissió a tots els altres, de manera que els bots, els anuncis freqüents i els missatges de prova alenteixen la malla per a tothom.
- **No és Meshtastic.** Meshtastic és un sistema diferent que funciona en gairebé les mateixes plaques. Els dos sistemes no es poden comunicar entre ells.

## La malla en un minut {#mesh}

Una ràdio LoRa arriba a uns quants quilòmetres dins d'una població, i molt més lluny des d'un turó o un terrat. Per arribar més lluny, les ràdios es passen els missatges les unes a les altres: això és una *malla*. A MeshCore, d'aquesta feina se n'encarreguen unes ràdios anomenades *repetidors*. Quan un repetidor sent un missatge, el torna a enviar, i així el missatge pot travessar tota una regió.

La malla no és de ningú. Cada node i cada repetidor és d'algú de la comunitat. La malla arriba fins on arriben els seus repetidors.

## Els 3 tipus de node {#roles}

Tries el tipus de node quan hi graves el firmware. El teu primer node és un companion.

**Companion.** La teva pròpia ràdio. La connectes a l'app de MeshCore del mòbil o de l'ordinador per Bluetooth o USB; alguns models tenen pantalla i teclat propis. A l'app llegeixes i escrius. El companion guarda els teus contactes i canals, i també els missatges que han arribat mentre l'app no estava connectada. Un companion no retransmet missatges d'altres persones.

**Repetidor.** Una ràdio col·locada en alt que retransmet els missatges de tothom. La majoria funcionen amb energia solar. Només en necessites un de propi on la malla encara no arriba. No té app pròpia. El configures per USB, o hi entres amb una contrasenya i el gestiones per ràdio. La [guia del repetidor](/repeater-guide/) t'explica com fer-ho.

**Room server.** Un petit tauler de missatges a la malla. Quan hi entres, reps les publicacions que t'has perdut mentre eres fora d'abast, fins a les 32 últimes. Només les guarda a la memòria, de manera que un reinici o un tall de corrent les esborra. Un grup local en fa servir un per als avisos.

## Com troba el camí un missatge {#routing}

Cada node té una clau secreta i una clau pública. La clau pública és la seva identitat. Un node es dona a conèixer amb un *anunci*: un paquet signat amb el seu nom i, si vols, la seva posició. Algú apareix als teus contactes quan t'ha arribat un dels seus anuncis, o quan escanes el seu codi QR. L'app té un botó per enviar el teu.

El teu primer missatge a un contacte surt com a *inundació*. Cada repetidor que el sent el retransmet una vegada i hi afegeix el seu identificador curt pel camí. La resposta porta de tornada aquesta llista d'identificadors. A partir d'aleshores, els teus missatges a aquest contacte segueixen la ruta registrada, i només emeten els repetidors d'aquesta ruta. Quan la ruta es trenca, l'app torna a fer una inundació.

Els missatges a un canal no tenen una sola adreça, així que sempre surten com a inundació. Els repetidors recorden què han retransmès fa poc i descarten les còpies que tornen a arribar per una altra ruta. Un missatge pot travessar fins a 64 repetidors, o 32 si el preajust fa servir identificadors de 2 bytes.

## Xifratge i privadesa {#encryption}

Els teus missatges directes van xifrats d'extrem a extrem: només els podeu llegir tu i l'altra persona. D'un paquet, un repetidor només veu una pista d'1 byte sobre el destinatari.

Els canals es xifren amb una clau compartida, així que qui els pot llegir depèn de qui té aquesta clau:

- **Public** ve configurat a tots els companions. La seva clau està publicada, de manera que qualsevol el pot llegir.
- **Els canals hashtag**, com ara `#utrecht`, treuen la clau del seu nom. Qualsevol que en sàpiga el nom s'hi pot unir, així que tracta'ls també com a públics.
- **Els canals privats** fan servir una clau aleatòria que comparteixes tu mateix, per exemple amb un codi QR.

Els anuncis van signats, però no xifrats. Tothom qui estigui a l'abast veu el nom del teu node, i també la seva posició si la comparteixes. Tria un nom que no digui més del que vols.

## La banda de 868 MHz a Europa {#band}

A Europa, MeshCore fa servir una petita part de la banda de 868 MHz, que tothom pot utilitzar sense llicència. El seu preajust de ràdio europeu, EU/UK (Narrow), és a 869.618 MHz, en un canal de 62.5 kHz. Aquesta freqüència és dins de la subbanda de 869.40-869.65 MHz, que permet fins a 500 mW e.r.p. Un dispositiu hi pot emetre com a màxim el 10% del temps. A la [secció legal de la guia del repetidor](/repeater-guide/#legal) trobaràs els detalls i els límits per país.

Tothom d'una mateixa zona fa servir el mateix preajust; si no, les ràdios no es poden sentir entre elles. Alguns països i regions fan servir una variant: el teu [grup local](/community/) sap quina.

## Per a què ho fa servir la gent {#uses}

- Per mantenir el contacte en excursions, al mar i en festivals on la xarxa mòbil està saturada o no hi és.
- Com a canal de reserva per a la família o els veïns quan fallen el corrent o les xarxes mòbils.
- Per xatejar localment amb ràdios que són de la mateixa gent.
- Per experimentar amb la ràdio, les antenes, l'energia solar i el programari de codi obert.

## D'on surten les dades {#data}

El cercador de la pàgina de [grups locals](/community/) troba un lloc amb una còpia de les llistes lliures de llocs i codis postals de [GeoNames](https://www.geonames.org/), amb llicència
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). La còpia és en aquest web. La teva cerca no surt mai del teu dispositiu, i no s'envia cap petició a GeoNames.
