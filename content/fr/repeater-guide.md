---
title: Guide du répéteur
lead: Placé en hauteur, un répéteur relaie les messages pour tout le monde autour de lui, à l'échelle d'une ville ou d'une vallée. Choisis un site, alimente-le à l'énergie solaire, configure-le et respecte la loi.
description: 'Planifier, alimenter, configurer et exploiter légalement un répéteur MeshCore en Europe : choix du site, dimensionnement solaire, réglages CLI, limites de puissance et de rapport cyclique à 868 MHz.'
eyebrow: 868 MHz · jusqu'à 500 mW · sans licence
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-11-02'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Les répéteurs font vivre le maillage. Les compagnons, les radios depuis lesquelles tu envoies tes messages, ne relaient rien. Sans répéteurs, tu n'atteins donc que les personnes à portée directe. Un répéteur bien placé étend le maillage pour tout le monde autour de lui. Ce guide correspond au micrologiciel MeshCore v1.18.0.

Avant de commencer, parle avec ton [groupe local](/community/). Ses membres savent où la couverture manque, [quel préréglage ta zone utilise](/guides/settings/) et comment nommer les répéteurs. Cherche les répéteurs proches de chez toi sur les [cartes de couverture](/map/), et passe dire bonjour sur les [canaux](/guides/channels/) publics ou locaux.

## As-tu besoin d'un répéteur ? {#need}

Un répéteur retransmet chaque message en diffusion qu'il capte, et tous les répéteurs à portée se partagent le même temps d'antenne. Là où le maillage t'atteint déjà, un répéteur de plus ajoute du trafic, pas de couverture. Un compagnon placé en hauteur, à une fenêtre des combles ou sur un balcon, peut te suffire.

Installe un répéteur là où la couverture manque :

- les [cartes de couverture](/map/) n'indiquent aucun répéteur près de chez toi, ou seulement des répéteurs que ton compagnon ne capte pas ;
- ton groupe local dit que la zone en a besoin.

## Choisir un site {#site}

La hauteur compte plus que la puissance. À 868 MHz, LoRa se propage le mieux quand la ligne de vue est dégagée. Les collines, les bâtiments et les arbres denses font perdre bien plus de portée que quelques milliwatts de plus n'en font gagner.

- **Vise haut.** Un toit, un mât, un grand bâtiment ou une colline couvre bien plus qu'un rebord de fenêtre. Gagner quelques mètres au-dessus des toits voisins aide déjà.
- **Garde l'antenne dégagée.** Fixe-la au-dessus des bords de toit, loin du métal, des gouttières et des autres antennes.
- **Vérifie la vue.** Des outils comme [HeyWhatsThat](https://www.heywhatsthat.com/) montrent ce qui est visible depuis un lieu. Si tu vois un endroit, un répéteur placé là est à portée.
- **Prévois du dégagement.** Un chemin radio a besoin d'espace libre autour de la ligne directe, pas seulement de la ligne elle-même. Sur de longues distances, le milieu du chemin doit passer plusieurs mètres au-dessus des obstacles.
- **Demande l'autorisation.** Obtiens l'accord du propriétaire du toit ou du mât, et mets-toi d'accord avec lui sur la façon d'accéder au répéteur pour l'entretien.

## Matériel {#hardware}

- **Carte.** Choisis une carte nRF52 à faible consommation, comme la [Heltec T114](/devices/), la RAK WisBlock ou le SenseCAP Solar Node. Les cartes ESP32 consomment davantage (la page des appareils les indique comme High), ce qui rend l'alimentation solaire difficile.
- **Antenne.** Utilise une antenne conçue pour 868 MHz, montée à la verticale. Le [guide des antennes](/guides/antenna/) traite des types, des connecteurs, du câble et du montage. Le gain de l'antenne compte dans la limite légale de puissance : consulte [Limites légales](#legal).
- **Câble.** Utilise un câble coaxial court, ou du câble à faibles pertes. À 868 MHz, quelques mètres de câble fin peuvent te faire perdre la moitié de ta puissance.
- **Boîtier.** Un boîtier étanche (IP65 ou mieux) avec un presse-étoupe, un trou d'aération ou d'écoulement contre la condensation, et une couleur claire ou un pare-soleil. Les batteries souffrent de la chaleur et ne peuvent pas se charger quand il gèle.
- **Foudre.** Une antenne sur un toit est une cible. Respecte les règles locales de mise à la terre, ou fixe-la là où la foudre n'atteindrait pas le câblage du bâtiment.

## Alimentation et dimensionnement solaire {#power}

Un répéteur solaire doit tenir pendant les semaines les plus sombres de l'hiver. Dimensionne-le pour ces semaines :

1. **Mesure la consommation.** Branche le répéteur configuré sur un wattmètre USB et laisse-le tourner une journée. Relève l'énergie consommée en wattheures (Wh). Le trafic de ta zone influe sur ce chiffre, alors mesure sur place si tu peux.
2. **Prévois une réserve.** Calcule la capacité de la batterie pour au moins 5 à 7 jours sans soleil utile.
3. **Évalue ton ensoleillement d'hiver.** L'[outil PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/), gratuit et proposé par l'UE, indique pour n'importe quel lieu l'énergie qu'un panneau produit chaque mois. Retiens le mois le moins ensoleillé.
4. **Dimensionne le panneau.** Le panneau doit compenser la consommation de chaque jour de ce mois le plus défavorable, avec une marge pour les pertes liées à la charge.

Voici un exemple chiffré, avec des valeurs supposées. Un répéteur qui consomme 1 Wh par jour a besoin d'une batterie d'au moins 7 Wh pour une semaine de réserve, soit environ 2 Ah de capacité utile à 3.7 V. Si PVGIS indique qu'un panneau de 1 W produit 0.5 Wh par jour en décembre sur ton site, il te faut au moins un panneau de 2 W. Avec 3 à 5 W, tu gardes une marge pour les nuages, la neige et le vieillissement.

## Le configurer {#config}

**Flashe.** Utilise le [flasheur web](https://flasher.meshcore.io) et choisis le micrologiciel **Repeater** pour ta carte. Les étapes de flashage se trouvent dans [Bien démarrer](/get-started/#flash).

**Configure par USB.** Laisse le répéteur branché à ton ordinateur, puis ouvre [config.meshcore.io](https://config.meshcore.io) ou la console du flasheur. Tu peux aussi utiliser n'importe quel terminal série à 115200 bauds. Les commandes les plus importantes :

| Action | Commande |
|---|---|
| Changer le mot de passe administrateur | `password <new password>` |
| Lui donner un nom | `set name <name>` |
| Préréglage radio : fréquence, largeur de bande, SF, CR (redémarre pour appliquer) | `set radio 869.618,62.5,8,8` |
| Limite de rapport cyclique, en pourcentage | `set dutycycle 10` |
| Puissance d'émission de la puce radio, en dBm | `set tx <dBm>` |
| Position, pour qu'il apparaisse sur les cartes | `set lat <degrees>` et `set lon <degrees>` |
| Coordonnées pour les autres opérateurs | `set owner.info <text>` |
| Heures entre les annonces en diffusion, celles que tout le maillage capte | `set flood.advert.interval <hours>` |
| L'annoncer tout de suite | `advert` |
| Redémarrer | `reboot` |

Le mot de passe administrateur par défaut est `password`, et toute personne qui se connecte avec ce mot de passe devient administrateur. Change-le avant de mettre le répéteur en service.

L'exemple `set radio` ci-dessus correspond à EU/UK (Narrow). Utilise plutôt les valeurs du préréglage de ta zone : la page [Réglages recommandés](/guides/settings/) les indique par pays.

**Règle l'horloge.** Sans module d'horloge (RTC), un répéteur perd l'heure à chaque coupure de courant et repart en mai 2024. Pendant qu'il tourne, son horloge dérive aussi : elle prend de l'avance ou du retard. Règle donc l'horloge de temps en temps : connecte-toi à distance depuis l'application et utilise `clock sync`, ou règle l'heure par USB. Avec un module RTC, tu as rarement besoin de le faire : il garde l'heure pendant les coupures et dérive bien moins.

**Gère-le à distance.** Une fois le répéteur sur le maillage, connecte-toi depuis l'application MeshCore avec le mot de passe administrateur. Tu y consultes son état et tu y utilises les mêmes commandes par radio. Certaines commandes ne fonctionnent que par USB, comme `set freq` et la réinitialisation d'usine `erase`.

**Garde son identité.** Avant un effacement, tape `get prv.key` par USB et conserve en lieu sûr la clé privée affichée. Après l'effacement, `set prv.key <key>` suivi d'un `reboot` rend au répéteur son ancienne identité. Les nœuds qui le connaissent le retrouvent ainsi sous le même préfixe.

La liste complète des commandes se trouve dans la [référence CLI de MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Le mettre à jour à distance {#update}

Une fois le répéteur installé en hauteur, tu le mets à jour depuis le sol. Connecte-toi depuis l'application MeshCore avec le mot de passe administrateur, ouvre sa ligne de commande et tape `start ota`. La suite dépend de la carte. Les autres cartes répondent `Error`, et tu les mets à jour par USB.

**Cartes nRF52**, comme RAK, Heltec T114, Seeed XIAO et SenseCAP Solar :

1. Télécharge le **ZIP** du nouveau micrologiciel pour ta carte depuis le [flasheur web](https://flasher.meshcore.io).
2. Tape `start ota`. Le répéteur répond `OK` et apparaît en Bluetooth sous le nom `<board>_OTA`, par exemple `RAK4631_OTA`.
3. Ouvre l'application nRF Device Firmware Update sur ton téléphone, choisis le ZIP et le répéteur, puis lance l'envoi. L'opération prend quelques minutes.

Installe le [bootloader OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX) sur une carte nRF52 avant de la monter en hauteur. Avec le bootloader d'origine, seule une connexion USB permet de réparer une mise à jour ratée. Avec OTAFIX, la carte revient en mode de mise à jour, et tu réessaies en Bluetooth.

**Cartes ESP32**, comme les Heltec V3 et V4 :

1. Télécharge depuis le flasheur web le `.bin` **non fusionné** pour ta carte : le fichier sans « merged » dans son nom.
2. Tape `start ota`. Le répéteur ouvre un réseau WiFi nommé `MeshCore-OTA` et répond avec l'adresse de sa page d'envoi.
3. À portée WiFi, connecte ton téléphone ou ton ordinateur portable à ce réseau, ouvre l'adresse et envoie le fichier.

## Limites légales {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Les préréglages européens de MeshCore se situent dans la sous-bande **869.40-869.65 MHz**. Dans l'UE, au Royaume-Uni, en Suisse et en Norvège, elle est ouverte sans licence aux appareils à courte portée, dans ces limites :

- au maximum **500 mW e.r.p.** de puissance rayonnée ;
- au maximum **10% de rapport cyclique** : pas plus de 360 secondes d'émission par heure, par appareil. Un appareil peut aussi utiliser l'écoute avant émission (listen-before-talk) avec agilité de fréquence adaptative, telle que définie dans ETSI EN 300 220-2 ;
- le signal entier, large de 250 kHz au maximum, doit rester dans la sous-bande.

La bande est partagée : tu ne dois pas perturber les services sous licence, et d'autres peuvent te perturber.
La radio doit porter le marquage CE (en Grande-Bretagne, CE ou UKCA).
{{< /callout >}}

Sources : [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845), annexe 1, bande h1.7 ; [décision 2006/771/CE de la Commission](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) et ses modifications ; [ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), bande O.

### Puissance : e.r.p. et ton antenne {#erp}

La limite s'applique à la puissance *rayonnée*, mesurée par rapport à une simple antenne dipôle (e.r.p.). Le gain de l'antenne s'ajoute, la perte du câble se soustrait. Les fabricants indiquent le gain d'antenne en dBi, soit 2.15 dB de plus que le même gain en dBd (par rapport à un dipôle). Garde cette somme à 27 dBm (500 mW) ou moins :

> puissance d'émission (dBm) + gain d'antenne (dBi) − perte du câble (dB) − 2.15 ≤ 27

- Une carte émet 22 dBm dans une antenne de 5 dBi, avec 1 dB de perte dans le câble : 22 + 5 − 1 − 2.15 = 23.85 dBm, environ 240 mW e.r.p. Limite respectée.
- Une carte avec un amplificateur de 30 dBm (1 W) émet dans une antenne de 3 dBi : 30 + 3 − 2.15 = 30.85 dBm, environ 1.2 W e.r.p. Limite dépassée : baisse la puissance d'émission.

`set tx` règle la puissance de sortie de la puce LoRa, en dBm. La puce SX1262 elle-même plafonne à 22 dBm, et le micrologiciel ne vérifie pas la valeur que tu saisis. Les cartes dotées d'un amplificateur supplémentaire, comme la Heltec V4 ou la Station G2, émettent bien plus que la valeur réglée. Consulte le tableau du fabricant avant de la régler, et commence par une valeur basse.

### Rapport cyclique {#duty-cycle}

Un répéteur émet pour tout le monde autour de lui, il épuise donc son temps d'antenne plus vite qu'un compagnon. Le limiteur de rapport cyclique de MeshCore est réglé par défaut sur 50%, soit plus que ce que cette bande autorise. Règle-le sur 10% sur chaque répéteur :

```text
set dutycycle 10
```

### Précision de la fréquence {#frequency}

Le canal EU/UK (Narrow), 869.618 MHz avec 62.5 kHz de largeur de bande, monte jusqu'à 869.649 MHz : moins de 1 kHz sous la limite haute de la sous-bande. Le signal doit rester dans la bande à toute température. Il faut pour cela un quartz compensé en température (TCXO). Presque toutes les cartes actuelles en ont un. Les anciennes cartes qui n'en ont pas, comme la Heltec V2, dérivent trop pour fonctionner de façon fiable à 62.5 kHz.

### Notes par pays {#countries}

- **Les États membres de l'UE** doivent mettre cette sous-bande à disposition à ces conditions (décision 2006/771/CE, article 3).
- **Royaume-Uni :** les mêmes limites, dans l'[IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices) de l'Ofcom.
- **Suisse et Liechtenstein :** les mêmes limites, dans la [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09) de l'OFCOM.
- **Norvège :** les mêmes limites, dans le [règlement sur les autorisations générales](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Ces notes ne constituent pas un avis juridique. Les règles changent : en cas de doute, renseigne-toi auprès de ton régulateur national.

## Liste de contrôle du déploiement {#checklist}

- [ ] Le propriétaire du site a donné son accord, et tu peux accéder au répéteur pour l'entretien.
- [ ] La carte fait tourner le micrologiciel **Repeater**, et tu as fixé l'antenne avant la première mise sous tension.
- [ ] Le mot de passe administrateur est changé.
- [ ] La radio correspond au [préréglage de ta zone](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` est appliqué.
- [ ] La puissance d'émission, gain d'antenne compris, reste dans la limite de 500 mW e.r.p.
- [ ] Le nom, la position et `owner.info` sont renseignés, pour que les autres sachent qui gère le répéteur.
- [ ] L'horloge est réglée (`clock`).
- [ ] Le boîtier est scellé, avec un trou d'écoulement ou d'aération, et le câble forme une boucle d'égouttement.
- [ ] La batterie et le panneau sont dimensionnés pour le pire mois d'hiver.
- [ ] Tu l'as testé à distance avec l'application avant de quitter le site.
- [ ] Ton groupe local sait qu'il est en service.
