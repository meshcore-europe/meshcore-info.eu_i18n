---
title: Réglages recommandés
layout: settings
lead: Le préréglage radio de ta zone, et les réglages que tes voisins ont modifiés. Choisis ton pays, applique le préréglage et copie les commandes.
description: Le préréglage radio MeshCore de chaque zone en Europe, et les réglages de répéteur et de companion que les groupes locaux ont modifiés par rapport aux valeurs par défaut, avec les commandes.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-10-31'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Chaque zone ci-dessous utilise son propre préréglage radio, ou modifie quelques
valeurs par défaut de MeshCore. Tout ce qui n'est pas indiqué garde sa valeur par
défaut : tu ne changes donc que ce que ta zone a changé. Un répéteur relaie les
messages pour tout le monde. Un companion est le nœud depuis lequel tu envoies
tes messages. Tu l'appaires avec ton téléphone ou ton ordinateur portable en
Bluetooth ou en USB, ou tu utilises son propre écran.

Le [guide du répéteur](/repeater-guide/#config) t'explique comment accéder à la
ligne de commande de ton répéteur. Avec la [console série](/firmware/console/)
de ce site, tu tapes toi-même les commandes. Sous chaque zone, tu peux aussi
envoyer ses réglages en USB. Le guide indique aussi les [limites légales](/repeater-guide/#legal)
sur 868 MHz.

## Limiter le trafic {#traffic}

Ces réglages valent pour toutes les zones. Chaque répéteur relaie chaque message
en diffusion qu'il capte. Un message que tu envoies coûte une émission, plus une
pour chaque répéteur qui le capte. Avec un rapport cyclique limité à 10 %, un
répéteur peut envoyer environ 680 paquets par heure. Tous ceux qui l'entourent
se partagent ce nombre. Un message qui va plus loin que nécessaire en consomme
une partie.

**Envoie ton message à la plus petite région qui atteint tes destinataires.**
Les régions s'emboîtent : un pays, une province, un groupe local, chacun avec
son propre code, comme `nl`, `nl-ov` et `nl-ov-zwo`. Un message destiné à
`nl-ov-zwo` reste chez les répéteurs de ce groupe. Un répéteur ne relaie que les
régions qu'il a lui-même : s'il a `nl`, il ne relaie pas pour autant `nl-ov`.
Place chaque répéteur dans toutes les régions qu'il dessert, et seulement
celles-là. Ton [groupe local](/community/) sait lesquelles.

**Limite ce que ton répéteur relaie.** Deux réglages gardent près de chez toi le
trafic qui n'a pas besoin d'aller loin :

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3` : les annonces, qui présentent un nœud au maillage,
  parcourent 3 sauts au maximum.
- `flood.max.unscoped 1` : un message sans région passe par un seul répéteur au
  maximum.
