---
title: Le réseau
layout: network
lead: Découvre le maillage à travers l'Europe, et aide-le à en voir davantage. Les observateurs écoutent le maillage et en rendent compte, et chaque nouveau en montre un peu plus.
description: 'Comment le maillage MeshCore devient visible en Europe : les observateurs transmettent ce qu’ils entendent au MeshCore Analyzer. Chiffres en direct, et comment ajouter ton propre observateur.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-10-31'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Le maillage lui-même ne garde aucune trace : un message passe de nœud en nœud,
puis disparaît. Ce que tu vois sur les [cartes de couverture](/map/) et dans les
statistiques vient des observateurs. Un observateur est un nœud qui transmet aussi
ce qu'il entend via MQTT, par le Wi-Fi ou internet. Le rapport va dans un seul
sens : rien ne revient sur le maillage. Un répéteur (un nœud qui relaie les
messages) équipé du micrologiciel d'observateur continue à relayer comme avant.

Des observateurs de toute l'Europe envoient leurs rapports au [MeshCore Analyzer](https://meshcore-analyzer.eu/),
à l'adresse mqtt.meshcore-analyzer.eu. L'Analyzer lit aussi d'autres brokers :
un observateur connecté à l'un d'eux compte donc lui aussi. À partir de ces rapports,
l'Analyzer construit les cartes, les statistiques et la [liste des canaux](/guides/channels/)
de ce site.

{{< callout type="tip" >}}
Le maillage n'a besoin de rien de tout cela : ces outils t'aident seulement à le voir et à le planifier. Les rapports des observateurs, l'Analyzer, ces cartes
et ces outils passent par internet. Lors d'une coupure de courant ou d'internet, ils s'arrêtent. Le
maillage continue à faire passer les messages par radio, via chaque répéteur encore
alimenté, comme ceux qui fonctionnent à l'énergie solaire.
{{< /callout >}}
