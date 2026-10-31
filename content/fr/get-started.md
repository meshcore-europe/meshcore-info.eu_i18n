---
title: Bien démarrer
lead: D'une carte neuve à ton premier message sur le maillage. Il te faut une carte LoRa, un ordinateur avec Chrome ou Edge, et un téléphone ou un portable pour l'application.
description: Installe MeshCore depuis ton navigateur, appaire l'application, choisis le préréglage radio de ta zone, envoie ton premier message et rejoins ton canal local.
eyebrow: 6 étapes · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-10-31'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Ces étapes suivent le micrologiciel MeshCore v1.18.0 et les outils officiels
d'octobre 2026. Les noms des menus de l'application peuvent varier un peu d'une version à l'autre.

## 1. Choisis un appareil {#device}

Toute carte de la [page des appareils](/devices/) marquée companion convient.
Pour ton premier nœud, prends un *companion* : la radio depuis laquelle tu
envoies tes messages. Tu l'appaires avec ton téléphone ou ton portable en
Bluetooth ou en USB. Tu peux aussi en prendre un avec son propre écran et son
propre clavier, qui fonctionne seul.

Prends la version 868 MHz. L'antenne fournie fait l'affaire. Le
[guide des antennes](/guides/antenna/) explique comment en vérifier une.

{{< callout type="warning" >}}
Branche l'antenne avant d'allumer la radio. Une radio LoRa qui émet sans
antenne peut endommager sa propre puce.
{{< /callout >}}

## 2. Installe le micrologiciel {#flash}

1. Relie l'appareil à ton ordinateur avec un câble USB de données.
2. Ouvre l'outil de flashage web sur [flasher.meshcore.io](https://flasher.meshcore.io)
   dans Chrome ou Edge. Il utilise Web Serial, absent des autres navigateurs.
3. Choisis ton appareil, puis le micrologiciel **Companion** pour **Bluetooth** (ou
   USB, si tu ne t'en sers qu'avec un câble relié à l'ordinateur).
4. Lance le flashage. Certaines cartes doivent d'abord passer en mode mise à
   jour. L'outil t'indique comment faire.

N'utilise *erase* que pour repartir de zéro : l'effacement supprime l'identité
de l'appareil et tes contacts. Pour les mises à jour suivantes, flashe sans
effacer. Pour garder ton identité malgré un effacement, exporte d'abord la clé
privée de ton companion depuis l'application, puis importe-la après.

## 3. Installe l'application {#app}

L'application officielle MeshCore existe pour Android, iOS, Windows et macOS.
Tu trouves le lien vers chaque version sur [meshcore.io](https://meshcore.io).
Il existe aussi une application web sur [app.meshcore.nz](https://app.meshcore.nz),
qui tourne dans Chrome ou Edge sur un ordinateur.

## 4. Appaire ton nœud {#pair}

Allume ton nœud, ouvre l'application et connecte-toi à lui en Bluetooth. Quand
l'application te demande un code PIN :

- un nœud **avec** écran affiche un code PIN : saisis celui-là ;
- un nœud **sans** écran utilise `123456`.

Si l'appairage échoue, supprime l'appareil des réglages Bluetooth de ton
téléphone et réessaie. Donne ensuite un nom à ton nœud. Les autres voient ce
nom. N'y mets donc ni ton nom complet ni ton adresse, sauf si tu le veux.

## 5. Choisis le préréglage radio de ta zone {#preset}

Toutes les radios d'une zone utilisent la même fréquence et les mêmes réglages.
Sinon, elles ne s'entendent pas. Dans les réglages radio de l'application,
choisis le préréglage de ta zone. En dehors des zones ci-dessous, l'Europe
utilise **EU/UK (Narrow)**. Les Pays-Bas, la Tchéquie, la Hongrie, la Slovaquie,
le Portugal et la Suisse ont le leur, et le Limbourg néerlandais a une variante :

{{< presets >}}

Ton appareil ne propose pas le préréglage de ta zone ? Saisis à la main les 4
valeurs du tableau dans les réglages radio de l'application : fréquence, bande
passante, facteur d'étalement et taux de codage. Un nœud avec d'autres valeurs
n'entend pas le maillage.

Tu as un doute ? Ton [groupe local](/community/) sait quel préréglage ta zone
utilise. L'application télécharge cette liste depuis le projet MeshCore. Un
nouveau préréglage ne demande donc aucune mise à jour de l'application.

## 6. Dis bonjour {#hello}

1. **Fais-toi connaître.** Envoie une *annonce* depuis l'application. Une annonce
   en « diffusion » passe par les répéteurs (des nœuds qui relaient les
   messages). Tout le monde sur le maillage peut ainsi t'ajouter.
   Un companion ne s'annonce jamais de lui-même.
2. **Trouve les autres.** Les gens apparaissent dans tes contacts dès que leurs
   annonces te parviennent. Par défaut, les répéteurs envoient une annonce en
   diffusion toutes les 47 heures. Ta liste peut donc mettre 2 jours à se remplir.
3. **Envoie un message.** Ouvre un contact et écris. Le premier message part en
   diffusion sur le réseau. Le destinataire renvoie le chemin suivi par le message,
   et les messages suivants empruntent ce chemin.
4. **Rejoins des canaux.** Le canal **Public** est déjà configuré. Tout ce que tu
   y écris parvient à tout le monde sur le maillage. Ajoute le *canal hashtag* de
   ta région (un nom qui commence par `#`) en tapant son nom. Ton
   [groupe local](/community/) te dira quels canaux sont actifs.

## Quand quelque chose ne marche pas {#troubleshooting}

**L'application ne trouve pas mon appareil en Bluetooth.**
Tu as sans doute flashé le companion USB. Flashe à nouveau et choisis la
version Bluetooth. Sur la Heltec V3, la petite antenne Bluetooth intégrée a une
faible portée. Garde le téléphone tout près.

**L'appairage échoue à chaque fois.**
Supprime l'appareil des réglages Bluetooth de ton téléphone, redémarre le
Bluetooth, puis appaire à nouveau avec le code PIN affiché à l'écran ou `123456`.

**Personne n'apparaît dans mes contacts.**
Vérifie que ton préréglage correspond à ta zone. Envoie une annonce en diffusion.
S'il n'y a aucun répéteur à portée, tu n'entendras que les radios proches. La
[page de la carte](/map/) montre où se trouvent les répéteurs.

**Un contact affiche « vu pour la dernière fois » il y a des jours alors qu'il est actif.**
L'un des deux nœuds n'est pas à l'heure. Un companion prend l'heure de ton
téléphone. Pour les répéteurs et les room servers (des nœuds qui stockent les
messages d'un groupe), c'est leur propriétaire qui doit régler l'heure.

**Un message direct n'arrive jamais.**
Tu dois avoir l'autre personne en contact, et elle doit t'avoir aussi. Un nœud
rejette le message d'un inconnu, sans prévenir l'expéditeur. Envoie une annonce
en diffusion et demande à l'autre personne d'en envoyer une aussi. Vérifie dans
l'application qu'elle ajoute automatiquement les nouveaux contacts. Elle n'ajoute
que les nœuds dans sa limite de sauts.

**Les anciens contacts marchent, les nouveaux ne se connectent jamais.**
Un premier message part en diffusion, et un répéteur ne le relaie que s'il gère
la région du message. Les messages suivants empruntent un chemin appris, qu'aucun
contrôle de région n'arrête. Demande à ton [groupe local](/community/) quelles
régions les répéteurs autour de toi gèrent, et vérifie
[les réglages de ta zone](/guides/settings/#traffic).

**L'application ne se connecte plus à ton companion.**
Certaines cartes ont un bouton utilisateur, comme certaines cartes RAK et la
Heltec T114. Maintiens-le enfoncé pendant les 8 premières secondes après le
démarrage de la carte. Le companion ouvre alors une console de secours en USB.
Dans la console sur [flasher.meshcore.io](https://flasher.meshcore.io),
`set pin <pin>` définit un nouveau code PIN Bluetooth et `erase` efface
l'appareil.

**L'outil de flashage n'arrive pas à ouvrir le port série sous Linux.**
Ton utilisateur doit avoir accès au port, par exemple avec
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, ou faire partie du groupe `dialout`.

**Autre chose.** La
[FAQ MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
traite de nombreux autres problèmes.
