---
title: Guide du répéteur
lead: Placé en hauteur, un répéteur relaie les messages pour tous ceux qui l'entourent, à l'échelle d'une ville ou d'une vallée entière. Choisis un site, alimente-le à l'énergie solaire, configure-le et respecte la loi.
description: 'Planifier, alimenter, configurer et exploiter légalement un répéteur MeshCore en Europe : choix du site, dimensionnement solaire, réglages CLI, limites de puissance et de rapport cyclique à 868 MHz.'
eyebrow: 868 MHz · jusqu'à 500 mW · sans licence
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-10-31'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Les répéteurs portent le maillage. Les companions, les radios depuis lesquelles
tu envoies tes messages, ne relaient pas les messages. Sans répéteurs, tu
n'atteins donc que les personnes à portée directe. Un répéteur bien placé
étend le maillage pour tous ceux qui l'entourent. Ce guide suit le
micrologiciel MeshCore v1.18.0.

Avant de commencer, parle à ton [groupe local](/community/). Ses membres savent
où la couverture manque, quel [préréglage ta zone utilise](/guides/settings/) et comment nommer les répéteurs.
Consulte les [cartes de couverture](/map/) pour trouver les répéteurs proches
de chez toi, et dis bonjour sur les [canaux](/guides/channels/) publics ou locaux.

## En as-tu besoin ? {#need}

Un répéteur retransmet chaque message en diffusion qu'il capte, et tous les
répéteurs à portée se partagent le même temps d'antenne. Là où le maillage
t'atteint déjà, un répéteur de plus ajoute du trafic sans ajouter de
couverture. Un companion placé en hauteur, à une lucarne ou sur un balcon,
peut te suffire.

Installe un répéteur là où la couverture manque :

- les [cartes de couverture](/map/) n'indiquent aucun répéteur près de chez
  toi, ou seulement des répéteurs que ton companion n'entend pas ;
- ton groupe local dit que la zone en a besoin.

## Choisir un site {#site}

La hauteur compte plus que la puissance. À 868 MHz, la LoRa porte le mieux en
visibilité directe. Collines, bâtiments et arbres denses coûtent bien plus de
portée que quelques milliwatts de plus n'en regagnent.

- **Monte haut.** Un toit, un mât, un grand immeuble ou une colline couvrent
  bien plus qu'un rebord de fenêtre. Même quelques mètres au-dessus des toits
  voisins aident.
- **Dégage l'antenne.** Fixe-la au-dessus des bords du toit, loin du métal,
  des gouttières et des autres antennes.
- **Vérifie la vue.** Des outils comme [HeyWhatsThat](https://www.heywhatsthat.com/)
  montrent ce qu'on voit depuis un endroit. Si tu vois un point, un répéteur
  placé là est à ta portée.
- **Laisse de la marge.** Un chemin radio a besoin d'espace libre autour de la
  ligne directe, pas seulement de la ligne elle-même. Sur de longues distances,
  le milieu du chemin doit passer plusieurs mètres au-dessus des obstacles.
- **Demande l'autorisation.** Obtiens l'accord du propriétaire du toit ou du
  mât, et convenez de la façon dont tu accéderas au répéteur pour l'entretien.

## Matériel {#hardware}

- **Carte.** Choisis une carte nRF52 basse consommation, comme la
  [Heltec T114](/devices/), la RAK WisBlock ou le SenseCAP Solar Node. Les
  cartes ESP32 consomment davantage (la page des appareils les marque High).
  Les faire tourner à l'énergie solaire devient alors difficile.
- **Antenne.** Utilise une antenne conçue pour 868 MHz, montée verticalement.
  Le [guide des antennes](/guides/antenna/) traite des types, connecteurs,
  câbles et fixations. Le gain d'antenne compte dans la limite légale de
  puissance : voir [Limites légales](#legal).
- **Câble.** Garde le câble coaxial court, ou prends du câble à faibles pertes.
  À 868 MHz, quelques mètres de câble fin peuvent te faire perdre la moitié de
  ta puissance.
- **Boîtier.** Prends un boîtier étanche (IP65 ou mieux) avec presse-étoupe,
  un évent ou un trou d'évacuation contre la condensation, et une couleur
  claire ou un pare-soleil. Les batteries souffrent de la chaleur et ne se
  rechargent pas sous zéro.
- **Foudre.** Une antenne sur un toit est une cible. Respecte les règles
  locales de mise à la terre, ou monte-la là où un impact n'atteindrait pas le
  câblage du bâtiment.

## Alimentation et dimensionnement solaire {#power}

Un répéteur solaire doit tenir pendant les semaines les plus sombres de
l'hiver. Dimensionne-le pour elles :

1. **Mesure la consommation.** Fais tourner le répéteur configuré derrière un
   wattmètre USB pendant une journée. Relève l'énergie consommée en
   wattheures (Wh). Le trafic de ta zone change ce chiffre : mesure sur place
   si tu peux.
2. **Ajoute une réserve.** Prévois une capacité de batterie pour au moins 5 à
   7 jours sans soleil utile.
3. **Trouve ton soleil d'hiver.** L'outil gratuit
   [PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) de l'UE indique, pour
   n'importe quel lieu, l'énergie qu'un panneau produit chaque mois. Prends le
   mois le moins ensoleillé.
4. **Dimensionne le panneau.** Le panneau doit compenser la consommation de
   chaque jour de ce pire mois, avec une marge pour les pertes de charge.

Un exemple chiffré, avec des valeurs supposées : un répéteur qui consomme
1 Wh par jour a besoin d'une batterie d'au moins 7 Wh pour une semaine de
réserve, soit environ 2 Ah de capacité utile à 3,7 V. Si PVGIS indique qu'un
panneau de 1 W donne 0,5 Wh par jour en décembre sur ton site, il te faut au
moins un panneau de 2 W. Avec 3 à 5 W, tu gardes de la marge pour les nuages,
la neige et le vieillissement.

## Configurer {#config}

**Flasher.** Utilise le [flasheur web](https://flasher.meshcore.io) et choisis
le micrologiciel **Repeater** pour ta carte. Les étapes du flashage sont dans
[Bien démarrer](/get-started/#flash).

**Configurer par USB.** Laisse le répéteur branché à ton ordinateur, puis
ouvre [config.meshcore.io](https://config.meshcore.io) ou la console du
flasheur. Tu peux aussi utiliser n'importe quel terminal série à 115200 bauds.
Les commandes les plus importantes :

| Quoi | Commande |
|---|---|
| Changer le mot de passe admin | `password <new password>` |
| Le nommer | `set name <name>` |
| Préréglage radio : fréquence, bande passante, SF, CR (redémarrer pour appliquer) | `set radio 869.618,62.5,8,8` |
| Limite de rapport cyclique, en pourcentage | `set dutycycle 10` |
| Puissance d'émission de la puce radio, en dBm | `set tx <dBm>` |
| Position, pour qu'il apparaisse sur les cartes | `set lat <degrees>` et `set lon <degrees>` |
| Coordonnées pour les autres opérateurs | `set owner.info <text>` |
| Heures entre deux annonces en diffusion, celles que tout le maillage entend | `set flood.advert.interval <hours>` |
| L'annoncer tout de suite | `advert` |
| Redémarrer | `reboot` |

Le mot de passe admin par défaut est `password`. Quiconque se connecte avec
devient admin. Change-le avant de mettre le répéteur en service.

L'exemple `set radio` ci-dessus correspond à EU/UK (Narrow). Utilise plutôt
les valeurs du préréglage de ta zone : la page
[Réglages recommandés](/guides/settings/) les liste par pays.

**Régler l'horloge.** Sans module d'horloge (RTC), un répéteur perd l'heure à
chaque coupure de courant et redémarre en mai 2024. En fonctionnement, son
horloge dérive aussi : elle avance ou retarde de plus en plus. Remets donc
l'heure de temps en temps. Connecte-toi à distance depuis l'appli et utilise
`clock sync`, ou règle l'heure par USB. Avec un module RTC, c'est rarement
nécessaire : il garde l'heure pendant les coupures et dérive beaucoup moins.

**Le gérer à distance.** Une fois le répéteur sur le maillage, connecte-toi
depuis l'appli MeshCore avec le mot de passe admin. Tu y lis son état et tu
utilises les mêmes commandes par radio. Certaines commandes ne marchent que
par USB, comme `set freq` et la réinitialisation d'usine `erase`.

**Garder son identité.** Avant un effacement, tape `get prv.key` par USB et
range la clé privée affichée en lieu sûr. Après l'effacement, `set prv.key <key>`
puis un `reboot` rendent au répéteur son ancienne identité. Les nœuds qui le
connaissent le retrouvent ainsi sous le même préfixe.

La liste complète des commandes se trouve dans la
[référence CLI de MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Mettre à jour par radio {#update}

Une fois le répéteur en hauteur, tu le mets à jour depuis le sol. Connecte-toi
depuis l'appli MeshCore avec le mot de passe admin, ouvre sa ligne de commande
et tape `start ota`. La suite dépend de la carte. Les autres cartes répondent
`Error` : celles-là, tu les mets à jour par USB.

**Cartes nRF52**, comme RAK, Heltec T114, Seeed XIAO et SenseCAP Solar :

1. Télécharge le **ZIP** du nouveau micrologiciel pour ta carte depuis le
   [flasheur web](https://flasher.meshcore.io).
2. Tape `start ota`. Le répéteur répond `OK` et apparaît en Bluetooth sous le
   nom `<board>_OTA`, par exemple `RAK4631_OTA`.
3. Ouvre l'appli nRF Device Firmware Update sur ton téléphone, choisis le ZIP
   et le répéteur, puis lance l'envoi. Cela prend quelques minutes.

Installe le [bootloader OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
sur une carte nRF52 avant de la monter en hauteur. Avec le bootloader
d'origine, une mise à jour ratée ne se répare que par USB. Avec OTAFIX, la
carte repasse en mode mise à jour et tu réessaies en Bluetooth.

**Cartes ESP32**, comme les Heltec V3 et V4 :

1. Télécharge depuis le flasheur web le `.bin` **non fusionné** pour ta
   carte : le fichier sans « merged » dans son nom.
2. Tape `start ota`. Le répéteur ouvre un réseau WiFi nommé `MeshCore-OTA` et
   répond avec l'adresse de sa page d'envoi.
3. À portée du WiFi, connecte ton téléphone ou ton ordinateur portable à ce
   réseau, ouvre l'adresse et envoie le fichier.

## Limites légales {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Les préréglages européens de MeshCore se trouvent dans la sous-bande
**869.40-869.65 MHz**. Dans l'UE, au Royaume-Uni, en Suisse et en Norvège,
elle est ouverte sans licence aux appareils à courte portée, dans ces limites :

- au plus **500 mW e.r.p.** de puissance rayonnée ;
- au plus **10% de rapport cyclique** : pas plus de 360 secondes d'émission
  par heure, par appareil. Un appareil peut aussi utiliser l'écoute avant
  émission avec agilité de fréquence adaptative, telle que définie dans ETSI
  EN 300 220-2 ;
- tout le signal, large de 250 kHz au plus, doit rester dans la sous-bande.

La bande est partagée : tu ne dois pas gêner les services sous licence, et
d'autres peuvent te gêner.
La radio doit porter le marquage CE (en Grande-Bretagne, CE ou UKCA).
{{< /callout >}}

Sources : [Recommandation CEPT ERC 70-03](https://docdb.cept.org/document/845),
annexe 1, bande h1.7 ;
[Décision 2006/771/CE de la Commission](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
et ses modifications ;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
bande O.

### Power: e.r.p. and your antenna {#erp}

The limit applies to the *radiated* power, measured against a simple dipole
antenna (e.r.p.). Antenna gain counts; cable loss subtracts. Makers state
antenna gain in dBi, which is 2.15 dB more than the same gain in dBd
(relative to a dipole). Keep this sum at or below 27 dBm (500 mW):

> transmit power (dBm) + antenna gain (dBi) − cable loss (dB) − 2.15 ≤ 27

- A board transmitting 22 dBm into a 5 dBi antenna through 1 dB of cable:
  22 + 5 − 1 − 2.15 = 23.85 dBm, about 240 mW e.r.p. Within the limit.
- A board with a 30 dBm (1 W) amplifier into a 3 dBi antenna:
  30 + 3 − 2.15 = 30.85 dBm, about 1.2 W e.r.p. Over the limit; lower the
  transmit power.

`set tx` sets the output of the LoRa chip, in dBm. The SX1262 chip itself
tops out at 22 dBm; the firmware does not check the number you enter. Boards with an extra
amplifier, such as the Heltec V4 or the Station G2, transmit much more than
the number you set. Check the manufacturer's table before you set it, and
start low.

### Rapport cyclique {#duty-cycle}

Un répéteur émet pour tous ceux qui l'entourent. Il épuise donc son temps
d'antenne plus vite qu'un companion. Le limiteur de rapport cyclique de
MeshCore est réglé par défaut à 50%, au-dessus de ce que cette bande autorise.
Règle-le à 10% sur chaque répéteur :

```text
set dutycycle 10
```

### Précision de fréquence {#frequency}

Le canal EU/UK (Narrow), 869.618 MHz avec 62.5 kHz de bande passante, monte
jusqu'à 869.649 MHz : moins de 1 kHz sous le haut de la sous-bande. Le signal
doit rester dans la bande à toutes les températures. Il faut pour cela un
quartz compensé en température (TCXO). Presque toutes les cartes actuelles en
ont un. Les cartes plus anciennes sans TCXO, comme la Heltec V2, dérivent trop
pour fonctionner de façon fiable à 62.5 kHz.

### Notes par pays {#countries}

- **Les États membres de l'UE** doivent ouvrir cette sous-bande à ces
  conditions (décision 2006/771/CE, article 3).
- **Royaume-Uni :** les mêmes limites, dans la
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices) de l'Ofcom.
- **Suisse et Liechtenstein :** les mêmes limites, dans la
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09) de l'OFCOM.
- **Norvège :** les mêmes limites, dans le
  [règlement sur les autorisations générales](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Ces notes ne sont pas un avis juridique. Les règles changent. En cas de doute,
renseigne-toi auprès de ton régulateur national.

## Liste de contrôle avant installation {#checklist}

- [ ] Le propriétaire du site a donné son accord, et tu peux accéder au
      répéteur pour l'entretien.
- [ ] La carte tourne sous le micrologiciel **Repeater**, et l'antenne était
      branchée avant la première mise sous tension.
- [ ] Le mot de passe admin est changé.
- [ ] La radio correspond au [préréglage de ta zone](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` est réglé.
- [ ] Puissance d'émission plus gain d'antenne restent dans les 500 mW e.r.p.
- [ ] Le nom, la position et `owner.info` sont réglés, pour que les autres
      sachent qui gère le répéteur.
- [ ] L'horloge est réglée (`clock`).
- [ ] Le boîtier est scellé, avec un trou d'évacuation ou un évent, et le câble
      forme une boucle d'égouttement.
- [ ] La batterie et le panneau sont dimensionnés pour le pire mois d'hiver.
- [ ] Tu l'as testé à distance avec l'appli avant de quitter le site.
- [ ] Ton groupe local sait qu'il est en service.
