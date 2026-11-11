---
title: Qu'est-ce que MeshCore ?
lead: MeshCore envoie des messages texte par radio, de nœud en nœud. Pas besoin d'internet ni d'abonnement.
description: 'Ce qu''est MeshCore et ce qu''il n''est pas : types de nœuds, routage, chiffrement et bande 868 MHz.'
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

MeshCore est un logiciel libre pour de petites radios LoRa. LoRa est une technique radio qui transmet peu de données très loin, avec très peu d'énergie. Une radio équipée de MeshCore s'appelle un *nœud*. Tu l'associes à l'application sur ton téléphone ou ton ordinateur, ou tu utilises son propre écran et son clavier. Tu envoies alors du texte à des personnes situées à des kilomètres. Aucune antenne relais, aucun routeur et aucun opérateur ne se trouve entre toi et eux.

Le logiciel est open source. Son développement se fait sur [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore), sous licence MIT.

## Ce que MeshCore n'est pas {#not}

Tu débutes en radio ? Voici ce que les gens attendent le plus souvent de MeshCore, et qu'il ne fait pas.

- **Ce n'est ni Internet ni un téléphone.** MeshCore envoie de courts messages texte,
  à peu près de la longueur d'un SMS sur ton téléphone. Pas de voix, de photos, de vidéos
  ni de sites web, et tu ne peux pas joindre un numéro de téléphone normal.
- **Ce n'est pas un service d'urgence.** Aucun service d'urgence ne s'engage à écouter
  le maillage. Nous savons que le maillage peut fonctionner. Personne ne sait
  s'il fonctionne lors d'une urgence.
- **Ce n'est ni instantané, ni disponible partout.** Un message saute de radio en
  radio et peut prendre quelques secondes, ou ne jamais arriver. Son acheminement dépend
  des répéteurs autour de toi, de la hauteur, des bâtiments et de ton antenne.
  Une petite radio à l'intérieur n'atteint souvent personne. Un répéteur sur un toit
  porte à des kilomètres.
- **Ce n'est pas un service que quelqu'un gère pour toi.** Il n'y a ni opérateur,
  ni assistance, ni promesse de couverture. Le maillage existe là où des membres
  de la communauté ont installé des répéteurs.
- **Tout n'y est pas privé.** Les messages directs sont chiffrés. Mais tout le monde
  peut lire Public et les canaux hashtag, et toute personne à portée voit le nom de
  ton nœud et la position que tu partages.
  Les [observateurs](/network/) transmettent ce qu'ils entendent à des cartes publiques.
  La [section sur le chiffrement](#encryption) explique ce qui reste privé.
- **Ce n'est pas illimité.** Dans une zone, tout le monde partage un seul canal radio,
  et les règles de la [bande 868 MHz](#band) limitent la durée d'émission de chaque radio.
  Chaque message prend du temps d'antenne à tous les autres. Les bots, les annonces fréquentes
  et les messages de test ralentissent donc le maillage pour tous.
- **Ce n'est pas Meshtastic.** Meshtastic est un autre système qui tourne en grande partie sur
  les mêmes cartes. Les deux ne peuvent pas communiquer entre eux.

## Le maillage en une minute {#mesh}

En ville, une radio LoRa porte à quelques kilomètres, et bien plus loin depuis une colline ou un toit. Pour aller plus loin, les radios se relaient les messages : c'est un *maillage*. Dans MeshCore, ce sont des radios appelées *répéteurs* qui relaient. Quand un répéteur capte un message, il le réémet. Le message peut ainsi traverser toute une région.

Le maillage n'appartient à personne. Chaque nœud et chaque répéteur appartient à un membre de la communauté. Le maillage porte aussi loin que leurs répéteurs.

## Les 3 types de nœud {#roles}

Tu choisis le type d'un nœud quand tu installes son micrologiciel. Ton premier nœud est un compagnon.

**Compagnon.** Ta propre radio. Tu l'appaires à l'application MeshCore sur ton téléphone ou ton ordinateur, en Bluetooth ou en USB. Certains ont leur propre écran et leur clavier. Tu lis et tu écris dans l'application. Le compagnon garde tes contacts et tes canaux. Il garde aussi les messages arrivés pendant que l'application n'était pas connectée. Un compagnon ne relaie pas les messages des autres.

**Répéteur.** Une radio placée en hauteur qui relaie les messages de tout le monde. La plupart fonctionnent à l'énergie solaire. Tu n'as besoin du tien que là où le maillage n'arrive pas encore. Il n'a pas d'application à lui. Tu le configures en USB, ou tu te connectes avec un mot de passe et tu le gères par radio. Le [guide du répéteur](/repeater-guide/) explique comment faire.

**Serveur de salon.** Un petit tableau d'affichage sur le maillage. Quand tu te connectes, tu reçois les messages manqués pendant que tu étais hors de portée, jusqu'aux 32 derniers. Il les garde uniquement en mémoire : un redémarrage ou une coupure de courant les efface. Un groupe local s'en sert pour ses annonces.

## Comment un message trouve son chemin {#routing}

Chaque nœud possède une clé secrète et une clé publique. La clé publique est son identité. Un nœud se fait connaître par une *annonce* : un paquet signé avec son nom et, si tu le souhaites, sa position. Quelqu'un apparaît dans tes contacts dès qu'une de ses annonces t'a atteint, ou quand tu scannes son QR code. L'application a un bouton pour envoyer ta propre annonce.

Ton premier message à un contact part en *diffusion*. Chaque répéteur qui le capte le relaie une fois et y ajoute son court identifiant au passage. La réponse rapporte cette liste d'identifiants. Dès lors, tes messages à ce contact suivent le chemin enregistré, et seuls les répéteurs de ce chemin émettent. Si le chemin est coupé, l'application repasse en diffusion.

Les messages vers un canal n'ont pas d'adresse unique. Ils partent donc toujours en diffusion. Les répéteurs se souviennent de ce qu'ils viennent de relayer. Ils ignorent les copies qui reviennent par un autre chemin. Un message peut traverser jusqu'à 64 répéteurs, ou 32 si le préréglage utilise des identifiants de 2 octets.

## Chiffrement et vie privée {#encryption}

Tes messages directs sont chiffrés de bout en bout : seuls toi et ton correspondant pouvez les lire. Un répéteur ne voit le destinataire d'un paquet que sous forme d'un indice de 1 octet.

Les canaux sont chiffrés avec une clé partagée. Qui peut les lire dépend donc de qui possède cette clé :

- **Public** est configuré sur chaque compagnon. Sa clé est publiée, donc tout le monde peut le lire.
- **Les canaux hashtag**, comme `#utrecht`, tirent leur clé de leur nom. Toute personne qui connaît le nom peut les rejoindre. Considère-les donc aussi comme publics.
- **Les canaux privés** utilisent une clé aléatoire que tu partages toi-même, par exemple sous forme de QR code.

Les annonces sont signées mais pas chiffrées. Le nom de ton nœud, et sa position si tu la partages, sont visibles de tous ceux qui sont à portée. Choisis un nom qui n'en dit pas plus que tu ne le veux.

## La bande 868 MHz en Europe {#band}

En Europe, MeshCore utilise une petite partie de la bande 868 MHz, que chacun peut utiliser sans licence. Son préréglage radio européen, EU/UK (Narrow), se trouve sur 869.618 MHz avec un canal de 62.5 kHz. C'est dans la sous-bande 869.40-869.65 MHz, qui autorise jusqu'à 500 mW e.r.p. Un appareil peut y émettre au maximum 10% du temps. La [section juridique du guide du répéteur](/repeater-guide/#legal) donne les détails et les limites par pays.

Dans une zone, tout le monde utilise le même préréglage, sinon les radios ne s'entendent pas. Certains pays et certaines régions utilisent une variante : ton [groupe local](/community/) sait laquelle.

## À quoi les gens l'utilisent {#uses}

- Garder le contact en randonnée, en mer et dans les festivals où le réseau
  mobile est saturé ou absent.
- Un canal de secours pour la famille ou les voisins quand le courant ou les
  réseaux mobiles tombent.
- Un moyen de secours pour les autorités locales quand leurs réseaux habituels
  tombent.
- Discuter en local sur des radios que les gens possèdent eux-mêmes.
- Garder une équipe de recherche et de sauvetage en contact là où il n'y a pas
  de réseau mobile. MeshCore SAR, une application communautaire présentée dans
  [Projets](/projects/), ajoute des cartes et le partage de positions.
- Vérifier un site éloigné depuis chez toi. Les répéteurs et les nœuds capteurs
  donnent la tension de leur batterie et d'autres mesures quand tu le leur
  demandes.
- Surveiller un capteur. Un nœud capteur fait tourner le micrologiciel MeshCore
  dédié aux mesures. Il garde un historique de la tension de sa batterie.
  Connecte-toi en admin : il t'alerte quand la batterie devient faible. Tu
  ajoutes des alertes pour d'autres mesures avec ton propre code.
- Commander quelque chose à distance, comme une pompe. Tu ajoutes cette fonction
  au micrologiciel du capteur avec ton propre code.
- Expérimenter avec la radio, les antennes, l'énergie solaire et les logiciels
  open source.

Certaines autorités mettent en place ou testent une solution de secours basée sur MeshCore. Nous avons vérifié
ces exemples en novembre 2026.

- Le cyclone Gabrielle a coupé toutes les communications à Tairāwhiti, en Nouvelle-Zélande.
  En septembre 2025, les services de gestion des urgences de la région ont cité MeshCore parmi
  [au moins 6 moyens de communication de secours](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Ils construisaient aussi des répéteurs solaires pour former l'ossature du réseau.
- Le district allemand de Bad Kissingen
  [construit un réseau de messagerie texte sur MeshCore](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  pour les autorités, les services d'urgence et les sites critiques. Les casernes
  de pompiers se raccordent en premier.
- Le conseil municipal de Hilversum, aux Pays-Bas,
  [a voté par 34 voix contre 1 en faveur d'un essai](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  avec un répéteur sur la tour de l'hôtel de ville. La commune
  [en fera le bilan à l'automne 2027](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Deux régions de sécurité néerlandaises, qui organisent la gestion des crises,
  expérimentent MeshCore :
  [le Limbourg-du-Sud](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  et [la Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Selon la Drenthe, il est trop tôt pour dire comment ou quand elle pourrait s'en servir.
- À Dalfsen, également aux Pays-Bas, des bénévoles
  [mènent un projet pilote aux côtés des communes](https://noodnetoverijssel.nl/).
  Ils misent d'abord sur la radio en phonie, puis sur MeshCore comme seconde couche pour les messages texte.

Personne ne sait si le maillage près de chez toi fonctionne en cas d'urgence.

## D'où viennent les données {#data}

La recherche de la page [groupes locaux](/community/) trouve un lieu grâce à une copie des listes libres de lieux et de codes postaux de [GeoNames](https://www.geonames.org/), sous licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Cette copie est hébergée sur ce site. Ta recherche ne quitte jamais ton appareil, et aucune requête ne part vers GeoNames.
