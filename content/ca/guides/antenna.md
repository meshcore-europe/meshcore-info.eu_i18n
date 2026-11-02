---
title: Guia d'antenes
lead: Una antena adequada i ben muntada arriba més lluny que més potència. Comprova l'antena del teu companion i després tria, connecta i munta'n una per a un repetidor.
description: 'Tria i munta una antena MeshCore per a 868 MHz: comprovar l''antena de fuet d''un companion, tipus d''antena i guany, connectors, pèrdua del cable per metre, filtres, muntatge i com compta el guany per al límit legal.'
eyebrow: Companion i repetidor · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-11-02'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

L'altura, una antena ben sintonitzada i un cable curt et donen més abast que
qualsevol mil·liwatt de més. Aquesta guia comença pel companion, la ràdio
des de la qual envies missatges. Després tracta l'antena d'un repetidor, un
node que retransmet missatges des d'un terrat o un pal.

## El teu companion {#companion}

{{< callout type="warning" >}}
Connecta l'antena abans d'engegar la ràdio. Una ràdio LoRa que transmet sense
antena pot fer malbé el seu propi xip.
{{< /callout >}}

L'antena que venia amb la placa ja et serveix. Connecta-la, aguanta el node
dret i comença a enviar missatges. Una antena millor en un companion aporta
poc; tenir un repetidor a l'abast aporta molt.

Compra una antena de fuet a part només si la que venia amb la placa està
trencada o et falta. No totes les antenes de fuet que es venen per a 868 MHz hi
estan sintonitzades. [Comprova-la amb un NanoVNA](#nanovna), un analitzador
d'antenes de butxaca, abans de refiar-te'n, o manlleva la d'una placa que
funcioni.

Un node al costat d'un transmissor potent sent menys del que hauria.
Si poses un petit [filtre SAW (d'ona acústica superficial)](#filters) entre la
ràdio i l'antena, aquest transmissor no entra al receptor. Abans, mira'n el
full de dades:

- **Potència màxima d'entrada.** El filtre també queda al camí de la teva
  pròpia transmissió. Una placa que envia 22 dBm (160 mW) a un filtre previst
  per a 15 dBm el trenca.
- **Banda de pas.** Ha d'incloure la freqüència del teu preset. Un filtre de
  868.65 a 869.25 MHz no deixa passar el canal EU/UK (Narrow) de
  869.618 MHz.

## Tipus d'antena per a un repetidor {#types}

Totes les antenes de la xarxa mesh estan en vertical. Tria el tipus segons on
siguin els nodes als quals vols arribar:

- **Col·lineal de fibra de vidre.** Un tub blanc en un pal, amb guany a tot
  l'horitzó. És l'opció habitual per a un repetidor que dona servei a una
  població.
- **Dipol.** És més curt, amb menys guany i un feix alt. Arriba millor que una
  col·lineal als nodes que tens a sota i a sobre, per exemple des d'un turó
  sobre una vall.
- **Yagi.** Una barra amb elements transversals, orientada cap a un sol lloc.
  Arriba a un únic repetidor llunyà i a poca cosa més. Munta-la amb els
  elements drets, perquè la polarització segueix els elements.

## El guany i el feix {#gain}

El guany no afegeix potència. Agafa el senyal que aniria amunt i avall i
l'envia al llarg de l'horitzó. És com una llanterna que enfoques: la mateixa
pila, un feix més llarg i més estret. Un dipol i una col·lineal del mateix
fabricant ho mostren:

| Antena | Guany | Amplada vertical del feix |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 graus |
| Col·lineal de fibra de vidre (Sirio SPO 868-915-6) | 5.8 dBi | 23 graus |

{{< gain >}}

El diagrama és un tall que passa pel pal, vist de costat. Fes-lo girar al
voltant del pal i tindràs el feix sencer: un dònut per al dipol, un disc pla
per a la col·lineal. Una antena vertical emet igual en totes les direccions al
seu voltant. Fora del feix dibuixat el senyal no s'atura; és més feble, però
encara n'hi ha prou per a un node proper.

En un terrat, et convé un feix pla. En un turó molt per sobre dels nodes, un
feix de 23 graus els passa per sobre del cap; un dipol els cobreix. Una Yagi
va més enllà: 16.6 dBi en un feix de 23 graus d'alçada i 25 graus d'amplada
(Amphenol Procom 7176870), i res als costats.

El guany es compta respecte a una referència. Els dBi el comparen amb una antena
ideal que emet igual en totes les direccions. Els dBd el comparen amb un dipol de
mitja ona, que ja té 2.15 dBi: fins i tot l'antena més senzilla no emet res
recte amunt ni avall. Un dipol més llarg, d'1.25 longituds d'ona, arriba a
5.2 dBi. Una col·lineal, en canvi, apila elements de mitja ona un sobre l'altre:
com més n'apila, més guany té. Si concentres el mateix senyal en la meitat de
l'espai, allà és el doble de fort: 3 dB. En una quarta part, és 4 vegades més
fort: 6 dB. Els fabricants indiquen el guany en dBi; el límit legal compta en
dBd: mira [Dins del límit legal](#legal).

### Quin guany et cal segons el lloc {#choose-gain}

- **Turons, valls o una ciutat densa: uns 3 dBi.** El feix alt arriba als nodes
  que tens a sobre i a sota, i rodeja els vessants i els edificis que hi ha pel
  mig. També funciona al revés: des d'una vall, un feix pla passa per sota d'un
  repetidor situat al turó de sobre. La RAKwireless RAKARG12 n'és una: un tub de
  fibra de vidre de 36 cm.
- **Zones residencials o una població de teulades baixes: de 5 a 6 dBi.** La
  col·lineal de fibra de vidre habitual.
- **Terreny pla i obert: de 8 a 10 dBi.** El feix més pla és el que arriba més
  lluny al llarg de l'horitzó. Si muntes l'antena alta, el feix passa per sobre
  dels nodes propers.

El guany del nom és la millor xifra de tota la banda de l'antena. La RAKARG12,
que es ven com a 3 dBi, té 2.8 dBi de 865 a 870 MHz. Mira la taula de guany del
full de dades a la freqüència del teu preset.

Per sobre de 7 dBi, una placa de 22 dBm supera el límit legal, tret que la
pèrdua del cable i del filtre compensi la diferència. Abaixa la potència de
transmissió en conseqüència.

Un guany alt només ajuda si saps on són els nodes: al llarg de l'horitzó al
voltant d'un repetidor, o en un repetidor llunyà en el cas d'una Yagi. Un
companion a la mà apunta en totes direccions, així que el guany baix amb què
venia és el que li va millor.

## Per què en vertical {#vertical}

Les antenes se senten millor entre elles quan apunten en la mateixa direcció. La
pèrdua creix amb l'angle entre elles: 45 graus costen 3 dB, la meitat del senyal.
A 90 graus, una antena horitzontal davant d'una de vertical, en teoria no arriba
res. La xarxa mesh està en vertical, així que la teva antena també. Això també val
per a un companion sobre una taula: si l'ajeus, tots els nodes del teu voltant
et senten menys.

## Connectors {#connectors}

Demana l'antena amb el connector que té la teva placa. Cada adaptador és una
unió més per segellar i més senyal perdut.

- **SMA.** Un connector de rosca d'uns 6 mm d'amplada. El sòcol de la majoria
  de plaques té un forat al centre; l'antena té el pin. Un connector d'aquest
  tipus perd uns 0.03 dB a 868 MHz.
- **RP-SMA.** El mateix cos i la mateixa rosca que l'SMA, amb el pin i el forat
  intercanviats. S'assembla a l'SMA i no hi encaixa. Comprova quin té la teva
  placa abans de fer la comanda.
- **U.FL (IPEX).** Un sòcol diminut a pressió a la mateixa placa. Un cable
  pigtail curt en surt fins a un sòcol SMA a la caixa. Està especificat per a
  30 cicles de connexió, així que connecta'l una vegada i deixa'l.
- **N.** El connector gran de rosca de les antenes de fibra de vidre i del cable
  gruixut. Perd com a màxim 0.05 dB. Un repetidor necessita un adaptador o
  pigtail d'N a l'SMA de la placa.

## Pèrdua del cable {#cable}

El cable et costa senyal abans que surti de l'antena, en els dos sentits. 3 dB
són la meitat de la potència. Aquestes són les xifres per metre dels fabricants,
de 868 a 900 MHz:

| Cable | Pèrdua per metre | Pèrdua en 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metres d'RG174, el pigtail prim que porten moltes plaques, perden la meitat
de la potència. Munta la placa a tocar de l'antena amb un pigtail curt, o porta-hi
cable gruixut. Afegeix a la suma cada adaptador i filtre que hi hagi al camí.

## Filtres {#filters}

Un filtre va entre la ràdio i l'antena. Deixa passar la teva banda i bloqueja la
resta, perquè un transmissor potent proper no saturi el receptor. En necessites
un quan un node sent menys del que hauria a prop d'altres transmissors. Un
repetidor en un pal amb estacions base de telefonia mòbil és un node d'aquesta
mena. Un filtre costa senyal en els dos sentits: compta'n la pèrdua igual que la
del cable.

| | Filtre SAW | Filtre de cavitat |
|---|---|---|
| Mida | Uns quants mil·límetres, en una placa petita | Un bloc o tub de metall |
| Pèrdua d'un de bo | menys de 2 dB | menys d'1 dB |
| Potència màxima d'entrada d'un de bo | 500 mW | diversos watts |

El sysmocom cf866.5-kt30, per exemple, és un filtre de cavitat de 863 a
870 MHz que perd 1.0 dB com a màxim i aguanta 30 W. Està fet per a interiors,
així que posa'l en una caixa segellada si va en un pal.

Els filtres varien molt, així que mira el full de dades abans de comprar-ne un.
La potència d'entrada especificada ha de superar la teva potència de transmissió,
i la banda de pas ha d'incloure la freqüència del teu preset.

## Muntatge {#mounting}

- **Per sobre de la vora del terrat.** L'antena necessita vista lliure en cada
  direcció que cobreix. Fins i tot uns quants metres per sobre dels terrats del
  voltant ajuden. A [Tria un lloc](/repeater-guide/#site), a la guia del
  repetidor, veuràs com comprovar la vista.
- **Lluny del metall.** Els canalons, els pals, altres antenes i les teulades
  metàl·liques al costat de l'antena en canvien el patró i la sintonia. Munta-la
  a dalt de tot del pal, no al costat.
- **En vertical.** Fes servir un nivell de bombolla; mira [Per què en
  vertical](#vertical).
- **Bucle de degoteig.** Deixa que el cable pengi per sota del connector abans
  que pugi o entri. Així l'aigua degota i no s'escola dins la unió.
- **Segella tots els connectors exteriors.** L'aigua dins d'un connector augmenta
  la pèrdua i corroeix el pin. Segella'l contra la pluja i revisa el segellat
  cada any.
- **Llamps.** Una antena en un terrat és un blanc. Un descarregador de gas al
  cable salta amb una sobretensió i l'envia a terra. Segueix
  [Maquinari](/repeater-guide/#hardware), a la guia del repetidor, i les normes
  locals per a la connexió a terra.

## Dins del límit legal {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
A Europa, MeshCore fa servir la subbanda 869.40-869.65 MHz, amb un màxim de
**500 mW** de potència radiada efectiva (e.r.p.). El límit compta el que surt de
l'antena: el guany de l'antena suma, la pèrdua del cable i del filtre resta. El
guany en dBi compta 2.15 dB menys, perquè el límit es mesura respecte a un dipol.
{{< /callout >}}

Una col·lineal de 5.8 dBi en una placa de 22 dBm queda dins del límit. La mateixa
antena en una placa amb amplificador no hi queda, fins que abaixes la potència de
transmissió. A [Potència: e.r.p. i la teva antena](/repeater-guide/#erp), a la
guia del repetidor, trobaràs el càlcul i 2 exemples resolts.

## Comprova una antena amb un NanoVNA {#nanovna}

Un NanoVNA és un analitzador de xarxes vectorial de butxaca. Mostra a quina
freqüència està sintonitzada una antena, i així ho saps abans de muntar-la. El
NanoVNA-H mesura fins a 1.5 GHz, i això cobreix els 868 MHz.

1. Calibra'l de 800 a 950 MHz amb les peces open, short i load del seu kit.
2. Connecta l'antena amb l'adaptador que farà servir al node. Aguanta-la dreta i
   lluny del teu cos i de la taula.
3. Llegeix la corba d'SWR (relació d'ona estacionària): mostra quant senyal
   retorna l'antena. El mínim ha de caure a la freqüència del teu preset, 869.618
   MHz per a EU/UK (Narrow). Un mínim a centenars de MHz de distància vol dir que
   l'antena està feta per a una altra banda.

Un quart d'ona a 868 MHz fa 86 mm (la longitud d'ona és de 345 mm). La longitud
per si sola no et diu la banda, perquè els fabricants pleguen i carreguen les
antenes de fuet; el NanoVNA sí que te la diu.

## Fonts {#sources}

- Pèrdua del cable: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  el full de dades de l'RG316 d'Huber+Suhner,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  els fulls de dades de l'LMR-240 i l'LMR-400 de Times Microwave,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antenes: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  el full de dades de la Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- El guany com a senyal concentrat en menys espai: [RF Cafe, introducció a les antenes](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Connectors: els fulls de dades de Rosenberger 32S102 (SMA) i 53S101 (N), el
  catàleg U.FL d'Hirose.
- Filtres: la pàgina de producte del sysmocom cf866.5-kt30,
  [descarregadors de gas de Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Pèrdua per polarització: [Universitat de Toronto, efectes de Friis](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Guany del dipol segons la longitud: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Longitud d'ona: velocitat de la llum segons el [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Límit legal: [Recomanació ERC 70-03 de la CEPT](https://docdb.cept.org/document/845),
  annex 1, banda h1.7; la [guia del repetidor](/repeater-guide/#legal) recull la
  resta.
