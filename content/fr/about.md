---
title: Qu'est-ce que MeshCore ?
lead: MeshCore envoie des messages texte par radio, de nœud en nœud. Il fonctionne sans internet et sans abonnement.
description: 'Ce que MeshCore est et n''est pas : le maillage, les compagnons, les répéteurs et les serveurs de salon, le routage, le chiffrement et la bande 868 MHz en Europe.'
eyebrow: MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '33e571f0'
  seeded: '2026-10-26'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['a3a6c1ff', '007314d2', 'f1f23981', '493b444f', '429f699c', 'f8008f48', '655373a9']
---

MeshCore est un logiciel libre pour petites radios LoRa. LoRa est une technique radio
qui transmet peu de données sur une longue distance, avec très peu d'énergie. Une radio équipée de MeshCore
s'appelle un *nœud*. Associé à l'appli sur ton téléphone ou ton ordinateur portable, ou doté de son propre
écran et clavier, il envoie du texte à des gens situés à des kilomètres. Aucune antenne-relais, aucun routeur, aucun opérateur ne s'intercale.

MeshCore n'envoie que de courts messages texte : ni voix, ni photos, ni trafic
internet.
Un message peut prendre quelques secondes, et son arrivée dépend des
répéteurs autour de toi. Il ne remplace pas les services d'urgence : en cas
d'urgence, appelle le 112.

Le logiciel est open source, développé sur
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) sous licence
MIT.

## Le maillage en une minute {#mesh}

Une radio LoRa porte à quelques kilomètres en ville, et bien plus loin depuis une
colline ou un toit. Pour aller plus loin, les radios se relaient les messages : c'est
ce qu'on appelle un *maillage*. Dans MeshCore, ce relais est assuré par des radios appelées *répéteurs*. Un
répéteur qui entend un message le renvoie, et le message peut ainsi traverser toute une région.

Le maillage n'appartient à personne. Chaque nœud et chaque répéteur appartient à quelqu'un de la
communauté. Le maillage vaut ce que valent les répéteurs que les gens installent.

## Les 3 types de nœud {#roles}

Tu choisis le type d'un nœud quand tu flashes son micrologiciel. Ton premier nœud est un compagnon.

**Compagnon.** Ta propre radio. Il s'appaire avec l'appli MeshCore sur ton téléphone ou
ton ordinateur portable, via Bluetooth ou USB ; certains ont leur propre écran et clavier. C'est dans l'appli
que tu lis et que tu écris. Le compagnon conserve tes contacts et tes canaux,
ainsi que les messages arrivés pendant que l'appli n'était pas connectée. Un compagnon ne relaie pas les messages des autres.

**Répéteur.** Une radio placée en hauteur qui relaie les messages de tout le monde. La plupart
fonctionnent à l'énergie solaire. Tu n'as besoin du tien que là où le maillage n'arrive pas
encore. Il n'a pas d'appli à lui. Tu le configures par USB, ou
tu te connectes avec un mot de passe et tu le gères par radio. Le
[guide du répéteur](/repeater-guide/) explique comment faire.

**Serveur de salon.** Un petit tableau de messages sur le maillage. Quand tu te connectes, tu reçois
les messages que tu as manqués hors de portée, jusqu'aux 32 derniers. Un groupe local
s'en sert pour ses annonces.

## Comment un message trouve son chemin {#routing}

Chaque nœud possède une clé secrète et une clé publique. La clé publique est son identité. Un nœud
se signale par une *annonce* : un paquet signé avec son nom et, si tu le
souhaites, sa position. Quelqu'un apparaît dans tes contacts après qu'une de ses
annonces t'est parvenue, ou quand tu scannes son code QR. L'appli a un bouton pour envoyer la tienne.

Ton premier message à un contact part en *diffusion*. Chaque répéteur qui
l'entend le relaie une fois, et y ajoute au passage son propre identifiant court. La réponse
ramène cette liste d'identifiants. À partir de là, tes messages à ce contact
suivent le chemin enregistré, et seuls les répéteurs sur ce chemin émettent. Quand le chemin
se rompt, l'appli repasse en diffusion.

Les messages destinés à un canal n'ont pas d'adresse unique, ils partent donc toujours en diffusion.
Les répéteurs se souviennent de ce qu'ils ont relayé récemment et écartent les copies qui arrivent
de nouveau par un autre chemin. Un message peut traverser jusqu'à 64 répéteurs, ou 32 quand le préréglage utilise des identifiants
sur 2 octets.

## Chiffrement et vie privée {#encryption}

Tes messages directs sont chiffrés de bout en bout : seuls toi et ton correspondant
pouvez les lire. Un répéteur ne voit le destinataire d'un paquet que sous forme d'un indice de 1 octet.

Les canaux sont chiffrés avec une clé partagée, donc leur lecture dépend de qui
détient cette clé :

- **Public** est configuré sur chaque compagnon. Sa clé est publiée, donc n'importe qui
  peut le lire.
- Les **canaux hashtag**, comme `#utrecht`, tirent leur clé de leur nom.
  Quiconque connaît le nom peut les rejoindre, considère-les donc aussi comme publics.
- Les **canaux privés** utilisent une clé aléatoire que tu partages toi-même, par exemple
  sous forme de code QR.

Les annonces sont signées mais pas chiffrées. Le nom de ton nœud, et sa position si
tu la partages, sont visibles par tous ceux à portée. Choisis un nom qui n'en dit pas plus
que tu ne le veux.

## La bande 868 MHz en Europe {#band}

En Europe, MeshCore utilise une petite partie de la bande 868 MHz que chacun peut utiliser
sans licence. Son préréglage radio européen, EU/UK (Narrow), se situe à
869.618 MHz sur un canal de 62.5 kHz. C'est à l'intérieur de la sous-bande
869.40-869.65 MHz, qui autorise jusqu'à 500 mW e.r.p. Un appareil ne peut y émettre qu'au plus 10 %
du temps. La
[section juridique du guide du répéteur](/repeater-guide/#legal) donne les détails
et les limites par pays.

Tout le monde dans une zone utilise le même préréglage, sinon les radios ne peuvent pas s'entendre
entre elles. Certains pays et certaines régions utilisent une variante : ton
[groupe local](/community/) sait laquelle.

## À quoi les gens s'en servent {#uses}

- Rester en contact en randonnée, en mer et dans les festivals où le réseau mobile
  est saturé ou absent.
- Un canal de secours pour la famille ou les voisins quand le courant ou les réseaux mobiles
  tombent en panne.
- Discuter localement sur des radios que les gens possèdent eux-mêmes.
- Expérimenter avec la radio, les antennes, l'énergie solaire et le logiciel open source.
