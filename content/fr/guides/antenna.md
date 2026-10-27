---
title: Guide des antennes
lead: L'antenne fait la moitié de ton nœud. La bonne antenne, bien montée, porte plus loin que de la puissance en plus. Vérifie l'antenne de ton compagnon, puis choisis, raccorde et monte une antenne pour un répéteur.
description: 'Choisir et monter une antenne MeshCore pour 868 MHz : vérifier le fouet d''un compagnon, types d''antennes et gain, connecteurs, perte de câble par mètre, filtres, montage et comment le gain compte dans la limite légale.'
eyebrow: Compagnon et répéteur · 868 MHz
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '45010ad0'
  seeded: '2026-10-26'
  fields: {title: '3a76cb0e', lead: '98430ade', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', '94c5bae4', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
---

La hauteur, une antenne accordée et un câble court gagnent plus de portée que n'importe quel milliwatt en plus. Ce guide commence par le compagnon, la radio depuis laquelle tu envoies tes messages. Il passe ensuite à l'antenne d'un répéteur, un nœud qui relaie les messages depuis un toit ou un mât.

## Ton compagnon {#companion}

{{< callout type="warning" >}}
Fixe l'antenne avant d'allumer la radio. Une radio LoRa qui émet sans antenne peut endommager sa propre puce.
{{< /callout >}}

L'antenne livrée avec ta carte fait l'affaire. Fixe-la, tiens le nœud à la verticale et commence à envoyer des messages. Une meilleure antenne sur un compagnon gagne peu ; un répéteur à portée gagne beaucoup.

N'achète une antenne fouet séparée que si celle fournie est cassée ou manquante. Toutes les antennes fouet vendues pour 868 MHz ne sont pas accordées sur cette fréquence. [Vérifie-la avec un NanoVNA](#nanovna), un analyseur d'antenne de poche, avant de lui faire confiance, ou emprunte-en une à une carte qui fonctionne.

Un nœud à côté d'un émetteur puissant entend moins qu'il ne le devrait. Un petit [filtre SAW (à ondes acoustiques de surface)](#filters) entre la radio et l'antenne tient cet émetteur à l'écart du récepteur. Lis d'abord sa fiche technique :

- **Puissance d'entrée maximale.** Le filtre se trouve aussi sur le chemin de ta propre émission. Une carte qui émet 22 dBm (160 mW) dans un filtre prévu pour 15 dBm casse le filtre.
- **Bande passante.** Elle doit inclure la fréquence de ton préréglage. Un filtre pour 868.65 à 869.25 MHz ne laisse pas passer le canal EU/UK (Narrow) sur 869.618 MHz.

## Types d'antennes pour un répéteur {#types}

Toutes les antennes du maillage sont à la verticale. Choisis le type selon l'emplacement des nœuds que tu veux atteindre :

- **Colinéaire en fibre de verre.** Un tube blanc sur un mât, avec du gain tout autour de l'horizon. Le choix standard pour un répéteur qui dessert une ville.
- **Dipôle.** Plus court, avec moins de gain et un faisceau haut. Il atteint mieux qu'une colinéaire les nœuds situés au-dessous et au-dessus de toi. Cela compte sur une colline qui domine une vallée.
- **Yagi.** Une perche avec des éléments transversaux, pointée vers un seul endroit. Elle atteint un répéteur lointain et pas grand-chose d'autre. Monte-la avec les éléments à la verticale, car sa polarisation suit les éléments.

## Le gain et le faisceau {#gain}

Le gain n'ajoute pas de puissance. Il prend le signal qui partirait vers le haut et le bas et l'envoie le long de l'horizon. Comme une lampe torche que tu règles : la même pile, un faisceau plus long et plus étroit. Un dipôle et une colinéaire du même fabricant le montrent :

| Antenne | Gain | Ouverture verticale |
|---|---|---|
| Dipôle (Sirio SO 868-915-2) | 2.2 dBi | 88 degrés |
| Colinéaire en fibre de verre (Sirio SPO 868-915-6) | 5.8 dBi | 23 degrés |

{{< gain >}}

Le schéma coupe le mât, vu de côté. Fais-le tourner autour du mât et tu obtiens tout le faisceau : un anneau pour le dipôle, un disque plat pour la colinéaire. Une antenne à la verticale émet de la même façon dans toutes les directions autour d'elle. Hors du faisceau dessiné, le signal ne s'arrête pas ; il est plus faible, encore suffisant pour un nœud proche.

Sur un toit, un faisceau plat est ce que tu veux. Sur une colline bien au-dessus des nœuds, un faisceau de 23 degrés passe par-dessus leurs têtes ; un dipôle les couvre. Une Yagi va plus loin : 16.6 dBi dans un faisceau de 23 degrés de haut et 25 degrés de large (Amphenol Procom 7176870), et rien sur les côtés.

Le gain se compte par rapport à une référence. Le dBi compare à une antenne idéale qui émet autant dans toutes les directions. Le dBd compare à un dipôle demi-onde, qui a lui-même 2.15 dBi : même l'antenne la plus simple n'émet rien droit vers le haut ou le bas. Un dipôle plus long, de 1.25 longueur d'onde, atteint 5.2 dBi. Une colinéaire empile plutôt des éléments demi-onde les uns au-dessus des autres : plus elle en empile, plus le gain est élevé. Concentre le même signal dans la moitié de l'espace et il y est deux fois plus fort : 3 dB. Dans un quart, 4 fois plus fort : 6 dB. Les fabricants indiquent le gain en dBi ; la limite légale se compte en dBd, voir [Dans la limite légale](#legal).

### Quel gain pour ton emplacement {#choose-gain}

- **Collines, vallées ou ville dense : environ 3 dBi.** Le faisceau haut atteint les nœuds au-dessus et au-dessous de toi, et contourne les pentes et les bâtiments sur le chemin. Cela marche aussi dans l'autre sens : depuis une vallée, un faisceau plat passe sous un répéteur sur la colline au-dessus. La RAKwireless RAKARG12 en est une : un tube en fibre de verre de 36 cm.
- **Banlieue ou petite ville aux toits bas : 5 à 6 dBi.** La colinéaire en fibre de verre standard.
- **Terrain plat et dégagé : 8 à 10 dBi.** Le faisceau le plus plat va le plus loin le long de l'horizon. Montée haut, elle passe par-dessus les nœuds proches.

Le gain dans le nom est le meilleur chiffre sur toute la bande de l'antenne. La RAKARG12, vendue comme 3 dBi, a 2.8 dBi de 865 à 870 MHz. Lis le tableau de gain dans la fiche technique à la fréquence de ton préréglage.

Au-dessus de 7 dBi, une carte de 22 dBm dépasse la limite légale, sauf si les pertes du câble et du filtre compensent la différence. Baisse la puissance d'émission pour rester dans la limite.

Un gain élevé n'aide que si tu sais où sont les nœuds : le long de l'horizon autour d'un répéteur, ou vers un seul répéteur lointain pour une Yagi. Un compagnon dans ta main pointe dans tous les sens, donc le faible gain de son antenne d'origine lui convient le mieux.

## Pourquoi à la verticale {#vertical}

Les antennes s'entendent le mieux quand elles pointent dans le même sens. La perte augmente avec l'angle entre elles : 45 degrés coûtent 3 dB, la moitié de ton signal. À 90 degrés, une antenne à plat face à une antenne verticale, rien n'arrive en théorie. Le maillage est à la verticale, donc ton antenne aussi. Cela vaut aussi pour un compagnon sur un bureau : pose-le à plat et tous les nœuds autour de toi entendent moins bien.

## Les connecteurs {#connectors}

Commande l'antenne avec le connecteur de ta carte. Chaque adaptateur est un joint de plus à étanchéifier et du signal perdu en plus.

- **SMA.** Un connecteur fileté d'environ 6 mm de large. La prise sur la plupart des cartes a un trou au centre ; l'antenne porte la broche. Un connecteur de ce type perd environ 0.03 dB à 868 MHz.
- **RP-SMA.** Le même corps et le même filetage que le SMA, avec la broche et le trou inversés. Il ressemble au SMA et ne s'y connecte pas. Vérifie lequel ta carte possède avant de commander.
- **U.FL (IPEX).** Une minuscule prise à enficher sur la carte elle-même. Un court câble pigtail la relie à une prise SMA dans le boîtier. Elle est prévue pour 30 cycles de connexion, donc branche-la une fois et n'y touche plus.
- **N.** Le gros connecteur fileté des antennes en fibre de verre et des câbles épais. Il perd au plus 0.05 dB. Un répéteur a besoin d'un adaptateur ou d'un pigtail de N vers le SMA de la carte.

## Les pertes du câble {#cable}

Le câble coûte du signal avant qu'il quitte l'antenne, dans les deux sens. 3 dB, c'est la moitié de ta puissance. Les chiffres des fabricants par mètre, de 868 à 900 MHz :

| Câble | Perte par mètre | Perte sur 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 mètres de RG174, le pigtail fin livré avec beaucoup de cartes, perdent la moitié de ta puissance. Monte la carte près de l'antenne avec un pigtail court, ou tire un câble épais jusqu'à elle. Ajoute au total chaque adaptateur et chaque filtre sur le chemin.

## Les filtres {#filters}

Un filtre se place entre la radio et l'antenne. Il laisse passer ta bande et bloque le reste, pour qu'un émetteur puissant à proximité ne sature pas le récepteur. Il t'en faut un quand un nœud entend moins qu'il ne le devrait près d'autres émetteurs. Un répéteur sur un mât avec des stations de base de téléphonie mobile est un tel nœud. Un filtre coûte du signal dans les deux sens : compte sa perte comme celle du câble.

| | Filtre SAW | Filtre à cavité |
|---|---|---|
| Taille | Quelques millimètres, sur une petite carte | Un bloc ou un tube en métal |
| Perte d'un bon modèle | moins de 2 dB | moins de 1 dB |
| Puissance d'entrée maximale d'un bon modèle | 500 mW | plusieurs watts |

Le sysmocom cf866.5-kt30, par exemple, est un filtre à cavité pour 863 à 870 MHz qui perd au plus 1.0 dB et supporte 30 W. Il est conçu pour l'intérieur, donc place-le dans un boîtier étanche sur un mât.

Les filtres diffèrent beaucoup, donc lis la fiche technique avant d'acheter. Sa puissance d'entrée nominale doit dépasser ta puissance d'émission, et sa bande passante doit inclure la fréquence de ton préréglage.

## Montage {#mounting}

- **Au-dessus du bord du toit.** L'antenne a besoin d'une vue dégagée dans chaque direction qu'elle dessert. Même quelques mètres au-dessus des toits voisins aident. [Choisir un site](/repeater-guide/#site) dans le guide du répéteur montre comment vérifier la vue.
- **Loin du métal.** Les gouttières, mâts, autres antennes et toits en métal à côté de l'antenne modifient son diagramme et son accord. Monte-la au sommet du mât, pas sur le côté.
- **À la verticale.** Utilise un niveau à bulle ; voir [Pourquoi à la verticale](#vertical).
- **Boucle d'égouttement.** Laisse le câble pendre sous le connecteur avant qu'il ne remonte ou n'entre. L'eau goutte alors au lieu de couler dans le joint.
- **Étanchéifie chaque connecteur extérieur.** L'eau dans un connecteur augmente la perte et corrode la broche. Protège-le de la pluie et vérifie l'étanchéité chaque année.
- **Foudre.** Une antenne sur un toit est une cible. Un parafoudre à gaz dans le câble se déclenche lors d'une surtension et l'envoie à la terre. Suis [Matériel](/repeater-guide/#hardware) dans le guide du répéteur et les règles locales pour la mise à la terre.

## Dans la limite légale {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
En Europe, MeshCore utilise la sous-bande 869.40-869.65 MHz, avec au plus
**500 mW** de puissance apparente rayonnée (p.a.r., e.r.p. en anglais). La limite compte ce qui sort de l'antenne :
le gain de l'antenne s'ajoute, les pertes du câble et du filtre se retranchent. Le gain en dBi compte
2.15 dB de moins, car la limite se mesure par rapport à un dipôle.
{{< /callout >}}

Une colinéaire de 5.8 dBi sur une carte de 22 dBm reste dans la limite. La même
antenne sur une carte avec un amplificateur la dépasse, tant que tu ne baisses pas la puissance
d'émission. [Puissance : p.a.r. et ton antenne](/repeater-guide/#erp) dans le
guide du répéteur donne le calcul et 2 exemples chiffrés.

## Vérifier une antenne avec un NanoVNA {#nanovna}

Un NanoVNA est un analyseur de réseau vectoriel de poche. Il montre sur quelle
fréquence une antenne est accordée, donc tu le sais avant de la monter. Le
NanoVNA-H mesure jusqu'à 1.5 GHz, ce qui couvre 868 MHz.

1. Calibre-le pour 800 à 950 MHz avec les pièces ouvert, court-circuit et charge
   de son kit.
2. Branche l'antenne via l'adaptateur qu'elle utilisera sur le nœud. Tiens-la
   à la verticale, loin de ton corps et de la table.
3. Lis la courbe de ROS (rapport d'ondes stationnaires) : elle montre combien de signal
   l'antenne renvoie. Le creux doit se trouver sur la fréquence de ton préréglage, 869.618
   MHz pour EU/UK (Narrow). Un creux à des centaines de MHz de là signifie que l'antenne est
   faite pour une autre bande.

Un quart d'onde à 868 MHz mesure 86 mm (la longueur d'onde est de 345 mm). La longueur
seule ne t'indique pas la bande, car les fabricants replient et chargent les fouets ; le
NanoVNA, lui, te l'indique.

## Sources {#sources}

- Perte dans le câble : [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf), la fiche technique Huber+Suhner RG316, [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf), [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf), les fiches techniques Times Microwave LMR-240 et LMR-400, [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antennes : [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf), la fiche technique Sirio SO 868-915-2, [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870), [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Le gain comme signal concentré dans moins d'espace : [RF Cafe, introduction aux antennes](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Connecteurs : les fiches techniques Rosenberger 32S102 (SMA) et 53S101 (N), le catalogue Hirose U.FL.
- Filtres : la page produit du sysmocom cf866.5-kt30, [parafoudres à gaz Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Perte de polarisation : [Université de Toronto, effets de Friis](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Gain du dipôle selon la longueur : [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Longueur d'onde : vitesse de la lumière selon le [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA : [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Limite légale : [Recommandation CEPT ERC 70-03](https://docdb.cept.org/document/845), annexe 1, bande h1.7 ; le [guide du répéteur](/repeater-guide/#legal) liste le reste.
