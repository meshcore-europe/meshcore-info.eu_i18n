---
title: Premiers pas
lead: D'une carte neuve à ton premier message sur le maillage. Il te faut une carte LoRa, un ordinateur avec Chrome ou Edge, et un téléphone ou un portable pour l'application.
description: Flashe MeshCore depuis ton navigateur, appaire l'application, choisis le préréglage radio de ta zone, envoie ton premier message et rejoins ton canal local.
eyebrow: 6 étapes · MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '68c89544'
  seeded: '2026-10-26'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', '36a3eba3', '6da9fd7a', 'cb5fb72e', '89626504', 'a419ce79', 'aa273b20']
---

Ces étapes suivent le micrologiciel MeshCore v1.18.0 et les outils officiels
d'octobre 2026. Les noms des menus de l'application peuvent varier un peu selon la version.

## 1. Choisis un appareil {#device}

Toute carte de la [page des appareils](/devices/) marquée companion convient. Pour
ton premier nœud, prends un *companion* : la radio depuis laquelle tu envoies tes messages. Tu l'appaires avec
ton téléphone ou ton portable en Bluetooth ou en USB. Tu peux aussi en prendre une avec son propre écran
et son clavier, qui fonctionne seule.

Prends la version 868 MHz. L'antenne fournie fait l'affaire ; le
[guide des antennes](/guides/antenna/) explique comment en vérifier une.

{{< callout type="warning" >}}
Fixe l'antenne avant d'allumer la radio. Une radio LoRa qui
émet sans antenne peut endommager sa propre puce.
{{< /callout >}}

## 2. Flashe le micrologiciel {#flash}

1. Branche l'appareil à ton ordinateur avec un câble USB de données.
2. Ouvre le flasheur web sur [flasher.meshcore.io](https://flasher.meshcore.io)
   dans Chrome ou Edge. Il utilise Web Serial, que les autres navigateurs n'ont pas.
3. Choisis ton appareil, puis le micrologiciel **Companion** pour **Bluetooth** (ou
   USB, si tu ne l'utiliseras qu'avec un câble relié à un ordinateur).
4. Flashe. Certaines cartes passent d'abord en mode mise à jour ; le flasheur t'explique
   comment faire.

N'utilise *erase* que pour repartir de zéro : l'effacement supprime l'identité de l'appareil
et tes contacts. Pour les mises à jour suivantes, flashe sans effacer.

## 3. Installe l'application {#app}

L'application officielle MeshCore existe pour Android, iOS, Windows et macOS ;
[meshcore.io](https://meshcore.io) renvoie vers chaque version. Il existe aussi une
application web sur [app.meshcore.nz](https://app.meshcore.nz) qui tourne dans Chrome ou
Edge sur un ordinateur.

## 4. Appaire ton nœud {#pair}

Allume ton nœud, ouvre l'application et connecte-toi à lui en Bluetooth. Quand
on te demande un code PIN :

- un nœud **avec** écran affiche un code PIN ; saisis celui-là ;
- un nœud **sans** écran utilise `123456`.

Si l'appairage échoue, retire l'appareil des réglages Bluetooth de ton téléphone et
réessaie. Donne ensuite un nom à ton nœud. Les autres voient ce nom, alors évite
ton nom complet ou ton adresse, sauf si tu le souhaites.

## 5. Choisis le préréglage radio de ta zone {#preset}

Toutes les radios d'une zone utilisent la même fréquence et les mêmes réglages, sinon elles ne
s'entendent pas. Dans les réglages radio de l'application, choisis le préréglage de ta zone.
En dehors des zones ci-dessous, l'Europe utilise **EU/UK (Narrow)**. Les Pays-Bas, la
Tchéquie, la Hongrie, la Slovaquie, le Portugal et la Suisse ont le leur, et
le Limbourg, aux Pays-Bas, a une variante :

{{< presets >}}

Pas sûr ? Ton [groupe local](/community/) sait quel préréglage ta zone utilise.
L'application télécharge cette liste depuis le projet MeshCore, donc un nouveau préréglage ne demande
aucune mise à jour de l'application.

## 6. Dis bonjour {#hello}

1. **Annonce-toi.** Envoie une *annonce* depuis l'application. Une annonce en « diffusion »
   passe par les répéteurs (des nœuds qui relaient les messages), ainsi tout le monde
   sur le maillage peut t'ajouter.
   Un companion ne s'annonce jamais tout seul.
2. **Trouve les autres.** Les gens apparaissent dans tes contacts dès que leurs annonces
   t'atteignent. Par défaut, les répéteurs envoient une annonce en diffusion toutes les 47 heures, donc ta liste
   peut mettre 2 jours à se remplir.
3. **Envoie un message.** Ouvre un contact et écris. Le premier message part en diffusion
   sur le réseau ; le destinataire renvoie le chemin suivi, et les
   messages suivants empruntent ce chemin.
4. **Rejoins des canaux.** Le canal **Public** est déjà configuré ; tout ce que tu
   y écris atteint tout le monde sur le maillage. Ajoute le *canal hashtag* de ta région
   (un nom qui commence par `#`) en saisissant son nom. Ton
   [groupe local](/community/) te dira quels canaux sont actifs.

## Quand quelque chose ne marche pas {#troubleshooting}

**L'application ne trouve pas mon appareil en Bluetooth.**
Tu as sans doute flashé le companion USB. Flashe à nouveau et choisis la
version Bluetooth. Sur le Heltec V3, la petite antenne Bluetooth intégrée
a une portée courte ; garde le téléphone tout près.

**L'appairage échoue à chaque fois.**
Retire l'appareil des réglages Bluetooth de ton téléphone, redémarre le Bluetooth
et appaire à nouveau avec le code PIN de l'écran ou `123456`.

**Personne n'apparaît dans mes contacts.**
Vérifie que ton préréglage correspond à ta zone. Envoie une annonce en diffusion. Sans
répéteur à portée, tu n'entendras que les radios proches ; la
[page de la carte](/map/) montre où se trouvent les répéteurs.

**Un contact affiche « vu pour la dernière fois » il y a des jours alors qu'il est actif.**
L'un des deux nœuds a une mauvaise heure. Un companion prend l'heure de
ton téléphone ; les répéteurs et les serveurs de salon (des nœuds qui stockent les messages d'un
groupe) ont besoin que leur propriétaire règle la leur.

**Le flasheur n'arrive pas à ouvrir le port série sous Linux.**
Ton utilisateur doit avoir accès au port, par exemple avec
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, ou en appartenant au groupe `dialout`.

**Autre chose.** La
[FAQ MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
traite bien d'autres problèmes.
