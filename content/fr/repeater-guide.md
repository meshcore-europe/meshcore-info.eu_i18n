---
title: Guide du répéteur
lead: Un répéteur placé en hauteur relaie les messages pour tout le monde autour de lui, sur toute une ville ou une vallée. Choisis un emplacement, alimente-le au soleil, configure-le et reste dans la légalité.
description: 'Planifier, alimenter, configurer et exploiter légalement un répéteur MeshCore en Europe : choix du site, dimensionnement solaire, réglages CLI, puissance et limites de rapport cyclique à 868 MHz.'
eyebrow: 868 MHz · jusqu'à 500 mW · sans licence
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '4a0fe39f'
  seeded: '2026-10-26'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['1de4a4f7', '766086be', '70faf508', '8bc641aa', '2018aa04', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
---

Les répéteurs portent le maillage. Les compagnons, les radios depuis lesquelles tu envoies des messages, ne relaient pas les messages. Sans répéteurs, tu n'atteins donc que les personnes à portée directe. Chaque répéteur que tu installes étend le maillage pour tout le monde autour de lui. Ce guide suit le micrologiciel MeshCore v1.18.0.

Avant de commencer, parle avec ton [groupe local](/community/). Ses membres savent où la couverture manque, quel [préréglage ta région utilise](/guides/settings/) et comment nommer les répéteurs. Regarde sur les [cartes de couverture](/map/) les répéteurs près de chez toi, et dis bonjour sur les [canaux](/guides/channels/) publics ou locaux.

## Choisir un emplacement {#site}

La hauteur compte plus que la puissance. Le LoRa à 868 MHz porte le mieux en ligne de vue dégagée. Les collines, les bâtiments et les arbres denses coûtent bien plus de portée que quelques milliwatts de plus n'en rapportent.

- **Monte haut.** Un toit, un mât, un immeuble élevé ou une colline couvre bien plus qu'un rebord de fenêtre. Même quelques mètres au-dessus des toits voisins font la différence.
- **Dégage l'antenne.** Monte-la au-dessus des bords du toit, loin du métal, des gouttières et des autres antennes.
- **Vérifie la vue.** Des outils comme [HeyWhatsThat](https://www.heywhatsthat.com/) montrent ce que l'on voit depuis un emplacement. Si tu vois un endroit, un répéteur placé là est à portée.
- **Garde de la marge.** Un trajet radio a besoin d'espace libre autour de la ligne directe, pas seulement de la ligne elle-même. Sur de longues distances, le milieu du trajet doit passer plusieurs mètres au-dessus des obstacles.
- **Demande la permission.** Obtiens l'accord du propriétaire pour le toit ou le mât, et convenez de la façon dont tu accéderas au répéteur pour l'entretien.

## Matériel {#hardware}

- **Carte.** Choisis une carte nRF52 à faible consommation comme la [Heltec T114](/devices/), la RAK WisBlock ou la SenseCAP Solar Node. Les cartes ESP32 consomment davantage (la page des appareils les marque « élevée »), ce qui complique le fonctionnement solaire.
- **Antenne.** Utilise une antenne conçue pour 868 MHz, montée verticalement. Le [guide des antennes](/guides/antenna/) traite des types, des connecteurs, du câble et du montage. Le gain d'antenne compte dans la limite légale de puissance, voir [Limites légales](#legal).
- **Câble.** Garde le câble coaxial court, ou utilise un câble à faibles pertes. À 868 MHz, quelques mètres de câble fin peuvent faire perdre la moitié de ta puissance.
- **Boîtier.** Un boîtier étanche (IP65 ou mieux) avec un presse-étoupe, un trou d'aération ou de drainage contre la condensation, et une couleur claire ou un pare-soleil. Les batteries souffrent de la chaleur et ne se chargent pas en dessous de zéro.
- **Foudre.** Une antenne sur un toit est une cible. Suis les règles locales de mise à la terre, ou monte-la là où un impact n'atteindrait pas le câblage du bâtiment.

## Alimentation et dimensionnement solaire {#power}

Un répéteur solaire doit survivre aux semaines les plus sombres de l'hiver. Dimensionne-le pour elles :

1. **Mesure la consommation.** Fais tourner le répéteur configuré pendant une journée à travers un wattmètre USB. Lis l'énergie consommée en wattheures (Wh). Le trafic de ta région change le chiffre, mesure donc sur place si tu peux.
2. **Ajoute une réserve.** Prévois une capacité de batterie pour au moins 5 à 7 jours sans soleil utile.
3. **Trouve ton soleil d'hiver.** L'outil gratuit [PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) de l'UE montre, pour n'importe quel lieu, combien d'énergie un panneau produit par mois. Prends le mois le moins ensoleillé.
4. **Dimensionne le panneau.** Le panneau doit compenser la consommation de chaque jour dans ce pire mois, avec de la marge pour les pertes de charge.

Un exemple chiffré, avec des valeurs supposées : un répéteur qui consomme 1 Wh par jour a besoin d'une batterie d'au moins 7 Wh pour une semaine de réserve, environ 2 Ah de capacité utile à 3,7 V. Si PVGIS indique qu'un panneau de 1 W produit chez toi 0,5 Wh par jour en décembre, il te faut au moins un panneau de 2 W, et 3 à 5 W laissent de la marge pour les nuages, la neige et le vieillissement.

## Le configurer {#config}

**Flasher.** Utilise le [flasheur web](https://flasher.meshcore.io) et choisis le micrologiciel **Repeater** pour ta carte. Les étapes du flashage sont dans [Premiers pas](/get-started/#flash).

**Configurer par USB.** Avec le répéteur encore branché à ton ordinateur, ouvre [config.meshcore.io](https://config.meshcore.io) ou la console du flasheur. Tu peux aussi utiliser n'importe quel terminal série à 115200 bauds. Les commandes les plus importantes :

| Quoi | Commande |
|---|---|
| Changer le mot de passe administrateur | `password <new password>` |
| Le nommer | `set name <name>` |
| Préréglage radio : fréquence, bande passante, SF, CR (redémarre pour appliquer) | `set radio 869.618,62.5,8,8` |
| Limite de rapport cyclique, en pour cent | `set dutycycle 10` |
| Puissance d'émission de la puce radio, en dBm | `set tx <dBm>` |
| Position, pour qu'il apparaisse sur les cartes | `set lat <degrees>` et `set lon <degrees>` |
| Coordonnées pour les autres opérateurs | `set owner.info <text>` |
| Heures entre les annonces en diffusion, celles que tout le maillage entend | `set flood.advert.interval <hours>` |
| L'annoncer maintenant | `advert` |
| Redémarrer | `reboot` |

Le mot de passe administrateur par défaut est `password`, et quiconque se connecte avec devient administrateur. Change-le avant que le répéteur passe à l'antenne.

L'exemple `set radio` ci-dessus correspond à EU/UK (Narrow). Utilise plutôt les valeurs du préréglage de ta région : [Réglages recommandés](/guides/settings/) les liste par pays.

**Régler l'horloge.** Sans module d'horloge (RTC), un répéteur perd l'heure à chaque coupure de courant et redémarre en mai 2024, et son horloge dérive pendant qu'il tourne. Connecte-toi à distance depuis l'application et utilise `clock sync`, ou règle l'heure par USB. Un module RTC est un ajout utile pour un répéteur : il garde l'heure pendant les coupures et dérive beaucoup moins.

**Le gérer à distance.** Une fois qu'il est sur le maillage, connecte-toi depuis l'application MeshCore avec le mot de passe administrateur. Tu y lis son état et tu utilises les mêmes commandes par radio. Certaines commandes ne fonctionnent que par USB, comme `set freq` et la remise à zéro d'usine `erase`.

La liste complète des commandes se trouve dans la [référence CLI de MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Limites légales {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Les préréglages européens de MeshCore se situent dans la sous-bande **869.40-869.65 MHz**. Dans l'UE, au Royaume-Uni, en Suisse et en Norvège, elle est ouverte sans licence aux appareils à courte portée, dans ces limites :

- au plus **500 mW e.r.p.** de puissance rayonnée ;
- au plus **10 % de rapport cyclique** : pas plus de 360 secondes d'émission par heure, par appareil. Un appareil peut aussi utiliser l'écoute avant émission avec agilité de fréquence adaptative, telle que définie dans ETSI EN 300 220-2 ;
- le signal entier, large de 250 kHz au plus, doit rester dans la sous-bande.

La bande est partagée : tu ne dois pas perturber les services sous licence, et d'autres peuvent te perturber.
La radio doit porter le marquage CE (en Grande-Bretagne, CE ou UKCA).
{{< /callout >}}

Sources : [Recommandation CEPT ERC 70-03](https://docdb.cept.org/document/845), annexe 1, bande h1.7 ;
[Décision de la Commission 2006/771/CE](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) et ses modifications ;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), bande O.

### Puissance : e.r.p. et ton antenne {#erp}

La limite s'applique à la puissance *rayonnée*, mesurée par rapport à une simple antenne dipôle (e.r.p.). Le gain d'antenne compte ; les pertes de câble se soustraient. Les fabricants indiquent le gain d'antenne en dBi, soit 2.15 dB de plus que le même gain en dBd (par rapport à un dipôle). Garde cette somme à 27 dBm (500 mW) ou moins :

> puissance d'émission (dBm) + gain d'antenne (dBi) − pertes de câble (dB) − 2.15 ≤ 27

- Une carte qui émet 22 dBm dans une antenne de 5 dBi à travers 1 dB de câble :
  22 + 5 − 1 − 2.15 = 23.85 dBm, environ 240 mW e.r.p. Dans la limite.
- Une carte avec un amplificateur de 30 dBm (1 W) dans une antenne de 3 dBi :
  30 + 3 − 2.15 = 30.85 dBm, environ 1.2 W e.r.p. Au-dessus de la limite ; baisse la puissance d'émission.

`set tx` règle la sortie de la puce LoRa, en dBm. La puce SX1262 elle-même plafonne à 22 dBm ; le micrologiciel ne vérifie pas le nombre que tu saisis. Les cartes avec un amplificateur supplémentaire, comme la Heltec V4 ou la Station G2, émettent bien plus que le nombre que tu règles. Consulte le tableau du fabricant avant de le régler, et commence bas.

### Rapport cyclique {#duty-cycle}

Un répéteur émet pour tout le monde autour de lui, il épuise donc son temps d'antenne plus vite qu'un compagnon. Le limiteur de rapport cyclique de MeshCore est à 50 % par défaut, ce qui dépasse ce que cette bande autorise. Règle-le à 10 % sur chaque répéteur :

```text
set dutycycle 10
```

### Précision de fréquence {#frequency}

Le canal EU/UK (Narrow), 869.618 MHz avec 62.5 kHz de bande passante, monte jusqu'à 869.649 MHz : moins de 1 kHz sous le haut de la sous-bande. Le signal doit rester dans la bande à toute température. Il faut pour cela un quartz compensé en température (TCXO). Presque toutes les cartes actuelles en ont un ; les cartes plus anciennes qui n'en ont pas, comme la Heltec V2, dérivent trop pour fonctionner de façon fiable à 62.5 kHz.

### Notes par pays {#countries}

- **Les États membres de l'UE** doivent rendre cette sous-bande disponible à ces conditions (Décision 2006/771/CE, article 3).
- **Royaume-Uni :** les mêmes limites, dans l'[IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices) de l'Ofcom.
- **Suisse et Liechtenstein :** les mêmes limites, dans le [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09) de l'OFCOM.
- **Norvège :** les mêmes limites, dans le [règlement sur les autorisations générales](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Ces notes ne sont pas un avis juridique. Les règles changent. En cas de doute, renseigne-toi auprès de ton régulateur national.

## Liste de contrôle pour le déploiement {#checklist}

- [ ] Le propriétaire du site a donné son accord, et tu peux accéder au répéteur pour l'entretien.
- [ ] La carte tourne avec le micrologiciel **Repeater**, et l'antenne était branchée avant la première mise sous tension.
- [ ] Le mot de passe administrateur est changé.
- [ ] La radio correspond au [préréglage de ta région](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` est réglé.
- [ ] La puissance d'émission plus le gain d'antenne reste dans les 500 mW e.r.p.
- [ ] Le nom, la position et `owner.info` sont renseignés, pour que les autres sachent qui l'exploite.
- [ ] L'horloge est réglée (`clock`).
- [ ] Le boîtier est étanche, avec un trou de drainage ou d'aération, et le câble forme une boucle d'égouttement.
- [ ] La batterie et le panneau sont dimensionnés pour le pire mois d'hiver.
- [ ] Tu l'as testé à distance avec l'application avant de quitter le site.
- [ ] Ton groupe local sait qu'il est en service.
