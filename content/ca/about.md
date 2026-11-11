---
title: Què és MeshCore?
lead: MeshCore envia missatges de text per ràdio, de node a node. Funciona sense internet i sense cap subscripció.
description: 'Què és MeshCore i què no és: tipus de node, encaminament, xifratge i la banda de 868 MHz.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '70b86ac3'
  seeded: '2026-11-11'
  fields: {title: '06eda66b', lead: 'c0174569', description: 'c2255f49', eyebrow: '8610c822'}
  sections: ['aa768ac3', '9e1e2d85', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', 'd516c212', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b7b981e6', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '5d796ffb', '1a490368', 'f0dd237f', '053d85bc', '02f1fe2f', 'e6b5b258']
---

MeshCore és programari lliure per a ràdios LoRa petites. LoRa és una tècnica de ràdio que envia poques dades molt lluny amb molt poca energia. Una ràdio amb MeshCore s'anomena *node*. Connectat a l'app del teu mòbil o ordinador, o amb pantalla i teclat propis, envia text a persones que són a quilòmetres de distància. Entremig no hi ha cap torre, cap encaminador ni cap proveïdor.

El programari és de codi obert i es desenvolupa a
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore), amb llicència MIT.

## Què no és MeshCore {#not}

Comences amb la ràdio? Això és el que la gent espera més sovint de MeshCore i que no fa.

- **No és internet ni un telèfon.** MeshCore envia missatges de text curts,
  de la llargada aproximada d'un SMS del teu mòbil. No hi ha veu, fotos, vídeo
  ni webs, i no pots trucar ni escriure a un número de telèfon normal.
- **No és un servei d'emergències.** Cap servei d'emergències es compromet a
  escoltar la malla. Sabem que la malla pot funcionar. Ningú sap si funciona
  en una emergència.
- **No és instantani ni arriba a tot arreu.** Un missatge salta de ràdio en
  ràdio i pot trigar uns segons, o no arribar mai. Que arribi depèn dels
  repetidors del teu voltant, de l'altura, dels edificis i de la teva antena.
  Una ràdio petita dins de casa sovint no arriba a ningú. Un repetidor en un
  terrat arriba a quilòmetres de distància.
- **No és un servei que algú gestiona per a tu.** No hi ha cap proveïdor, cap
  servei d'ajuda ni cap promesa de cobertura. La malla existeix allà on gent de
  la comunitat ha instal·lat repetidors.
- **No tot el que hi circula és privat.** Els missatges directes van xifrats,
  però qualsevol pot llegir Public i els canals amb etiqueta (hashtag). A més,
  tothom qui és dins l'abast veu el nom del teu node i la posició que comparteixes.
  Els [observadors](/network/) envien el que senten a mapes públics. La
  [secció sobre el xifratge](#encryption) explica què es manté privat.
- **No és il·limitat.** A cada zona, tothom comparteix un sol canal de ràdio, i
  les normes de la [banda de 868 MHz](#band) limiten quant de temps pot emetre
  cada ràdio. Cada missatge treu temps d'emissió a tots els altres. Per això els
  bots, els anuncis freqüents i els missatges de prova alenteixen la malla per a
  tothom.
- **No és Meshtastic.** Meshtastic és un sistema diferent que funciona en
  plaques molt semblants. Els dos sistemes no es poden comunicar entre si.

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

- Mantenir el contacte en excursions, al mar i en festivals on la xarxa mòbil
  està saturada o no hi és.
- Un canal de reserva per a la família o els veïns quan falla el corrent o la
  xarxa mòbil.
- Una reserva per a les autoritats locals quan les seves xarxes habituals fallen.
- Xat local amb ràdios que són de la mateixa gent.
- Mantenir en contacte un equip de cerca i rescat on no hi ha xarxa mòbil.
  MeshCore SAR, una app de la comunitat que trobaràs a [Projectes](/projects/),
  hi afegeix mapes i posicions compartides.
- Comprovar un lloc remot des de casa. Quan ho demanes, els repetidors i els
  nodes sensors informen del voltatge de la bateria i d'altres lectures.
- Vigilar un sensor. Un node sensor fa servir el firmware de MeshCore per mesurar
  coses. Guarda un historial del voltatge de la seva bateria. Si hi entres com a
  administrador, t'avisa quan queda poca bateria. Els avisos per a altres
  lectures els afegeixes tu amb el teu propi codi.
- Accionar alguna cosa a distància, com ara una bomba. Això ho afegeixes al
  firmware del sensor amb el teu propi codi.
- Experimentar amb la ràdio, les antenes, l'energia solar i el programari de codi
  obert.

Algunes autoritats estan construint o provant un sistema de reserva basat en MeshCore. Vam comprovar aquests exemples el novembre de 2026.

- El cicló Gabrielle va tallar totes les comunicacions a Tairāwhiti, a Nova Zelanda.
  El setembre de 2025, el servei d'emergències de la regió va citar MeshCore
  [com una de les almenys 6 vies de reserva per comunicar-se](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  També construïa repetidors solars com a columna vertebral de la xarxa.
- El districte alemany de Bad Kissingen
  [construeix una xarxa de text amb MeshCore](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  per a les autoritats, els serveis d'emergència i les instal·lacions crítiques. Els parcs
  de bombers es connecten primer.
- El consell municipal de Hilversum, als Països Baixos,
  [va votar per 34 a 1 a favor d'una prova](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  amb un repetidor a la torre de l'ajuntament. El municipi
  [l'avaluarà la tardor de 2027](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Dues regions de seguretat neerlandeses, que organitzen la resposta a una crisi,
  experimenten amb MeshCore:
  [Limburg del Sud](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  i [Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Drenthe diu que encara és massa aviat per saber com o quan el podria fer servir.
- A Dalfsen, també als Països Baixos, uns voluntaris
  [fan una prova pilot juntament amb els municipis](https://noodnetoverijssel.nl/).
  Primer fan servir la ràdio de veu, i MeshCore com a segona capa per al text.

Ningú sap si la malla del teu voltant funciona en una emergència.

## D'on surten les dades {#data}

El cercador de la pàgina de [grups locals](/community/) troba un lloc amb una còpia de les llistes lliures de llocs i codis postals de [GeoNames](https://www.geonames.org/), amb llicència
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). La còpia és en aquest web. La teva cerca no surt mai del teu dispositiu, i no s'envia cap petició a GeoNames.
