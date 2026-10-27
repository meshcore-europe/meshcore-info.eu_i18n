---
title: Réglages recommandés
layout: settings
lead: Le préréglage radio utilisé dans ta zone, et les réglages que tes voisins ont modifiés. Choisis ton pays, applique le préréglage et copie les commandes.
description: Le préréglage radio MeshCore par zone en Europe, ainsi que les réglages de répéteur et de compagnon que les groupes locaux ont modifiés par rapport aux valeurs par défaut, avec les commandes.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '9547ba62'
  seeded: '2026-10-26'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', '43cde8b4']
---

Chaque zone ci-dessous utilise son propre préréglage radio, ou modifie quelques
valeurs par défaut de MeshCore. Tout ce qui n'est pas listé reste à la valeur par
défaut : tu ne modifies donc que ce que ta zone a modifié. Un répéteur relaie les
messages pour tout le monde. Un compagnon est le nœud depuis lequel tu envoies
tes messages, appairé à ton téléphone ou ton ordinateur portable via Bluetooth ou
USB, ou doté de son propre écran.

Le [guide du répéteur](/repeater-guide/#config) explique comment accéder à la
ligne de commande de ton répéteur. La [console série](/firmware/console/) de ce
site te permet de saisir les commandes toi-même. Sous chaque zone, tu peux aussi
envoyer ses réglages via USB. Le guide indique aussi les
[limites légales](/repeater-guide/#legal) sur 868 MHz.

## Limiter le trafic {#traffic}

Ces réglages s'appliquent à toutes les zones. Chaque répéteur relaie tous les
messages en diffusion qu'il entend. Un message envoyé par toi coûte une
transmission, plus une pour chaque répéteur qui l'entend. Avec le cycle de
service de 10 %, un répéteur peut envoyer environ 680 paquets par heure, et tout
le monde autour de lui se partage ce nombre. Un message qui voyage plus loin que
nécessaire en consomme une partie.

**Envoie à la plus petite région qui atteint les personnes à qui tu écris.**
Les régions s'emboîtent : un pays, une province, un groupe local, chacun avec
son propre code, comme `nl`, `nl-ov` et `nl-ov-zwo`. Un message pour `nl-ov-zwo`
reste sur les répéteurs de ce groupe. Place chaque répéteur uniquement dans les
régions qu'il dessert. Ton [groupe local](/community/) sait lesquelles.

**Limite ce que ton répéteur relaie.** Deux réglages gardent près de chez toi le
trafic qui n'a pas besoin d'aller loin :

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3` : les annonces, qui signalent un nœud au maillage,
  parcourent au plus 3 sauts.
- `flood.max.unscoped 1` : un message sans région passe par un seul répéteur
  au maximum.
