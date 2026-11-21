---
title: Liste de contrôle du répéteur
lead: Vérifie ton répéteur avant de l'installer en hauteur. Chaque ligne indique ce que tu vérifies, la commande qui l'affiche et le guide qui l'explique.
description: 'Une liste de contrôle pour un répéteur MeshCore avant sa pose sur un toit ou un mât : ce que tu vérifies en USB, comment tu le fixes et le test avant de partir.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Un répéteur sur un toit est difficile d'accès : vérifie-le donc tant qu'il est
encore sur ton bureau. Le [guide du répéteur](/repeater-guide/) explique chaque
étape. Les valeurs, comme le préréglage et les limites de sauts, viennent des
[réglages de ta zone](/guides/settings/). Tape les commandes en USB, par
exemple dans la [console série](/firmware/console/). Cette liste suit le
micrologiciel MeshCore v1.18.0.

## Avant de commencer {#start}

- [ ] Les [cartes de couverture](/map/) ou ton [groupe local](/community/)
      indiquent que la zone a besoin d'un répéteur. Voir
      [En as-tu besoin ?](/repeater-guide/#need)
- [ ] Le propriétaire du site est d'accord, et tu peux accéder au répéteur
      pour l'entretien.
- [ ] Tu as dimensionné la batterie et le panneau pour le pire mois d'hiver.
      Voir [Alimentation et dimensionnement solaire](/repeater-guide/#power).

## À ton bureau, en USB {#usb}

- [ ] La carte fait tourner le micrologiciel **Repeater** : `ver` affiche sa
      version. Voir [Le configurer](/repeater-guide/#config).
- [ ] Sur une carte nRF52, la réponse à `get bootloader.ver` contient
      `OTAFIX`. Voir [Le mettre à jour sans fil](/repeater-guide/#update).
- [ ] `get radio` affiche le préréglage de ta zone.
- [ ] `get dutycycle` affiche 10. Voir [Rapport cyclique](/repeater-guide/#duty-cycle).
- [ ] `get tx` plus le gain de ton antenne reste dans la limite de 500 mW
      e.r.p. Voir [Puissance : e.r.p. et ton antenne](/repeater-guide/#erp).
- [ ] Le mot de passe admin n'est plus `password`.
- [ ] `get guest.password` affiche un mot de passe.
- [ ] `get name` affiche le nom que ton groupe local utilise pour ses répéteurs.
- [ ] `get lat` et `get lon` affichent la position du site.
- [ ] `get owner.info` indique comment les autres opérateurs peuvent te joindre.
- [ ] `region` affiche les régions de ta zone. `get flood.max.advert` et
      `get flood.max.unscoped` affichent ses limites de sauts. Voir
      [Limiter le trafic](/guides/settings/#traffic).
- [ ] Tu as rangé en lieu sûr la clé privée obtenue avec `get prv.key`.
- [ ] `clock` affiche l'heure actuelle, en UTC.
- [ ] Sur une installation solaire, `powersaving` affiche `on`.

## Sur le toit {#roof}

- [ ] Tu as fixé l'antenne avant de mettre le répéteur sous tension.
- [ ] L'antenne est verticale, en haut du mât, loin du métal. Voir
      [Fixation](/guides/antenna/#mounting).
- [ ] Chaque connecteur extérieur est étanche, et le câble forme une boucle
      d'égouttement.
- [ ] Le boîtier est fermé, avec un évent ou un trou d'évacuation. Voir
      [Matériel](/repeater-guide/#hardware).

## Avant de partir {#leave}

- [ ] À distance, ton companion atteint le répéteur dans l'application.
- [ ] Tu as envoyé `advert` pour que les nœuds de tout le maillage connaissent le répéteur.
- [ ] Ton [groupe local](/community/) sait qu'il est en service.
