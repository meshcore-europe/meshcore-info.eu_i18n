---
title: Le réseau
layout: network
lead: Vois le maillage à travers l'Europe, et aide-le à voir plus loin. Les observateurs écoutent le maillage et le rapportent, et chaque nouvel observateur en montre un peu plus.
description: 'Comment le maillage MeshCore devient visible en Europe : des observateurs rapportent ce qu''ils entendent au MeshCore Analyzer. Chiffres en direct, et comment ajouter ton propre observateur.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '05fa5ea3'
  seeded: '2026-10-26'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['05fa5ea3']
---

Le maillage lui-même ne garde aucune trace : un message passe de nœud en nœud, puis disparaît. Ce que tu vois sur les [cartes de couverture](/map/) et dans les statistiques vient des observateurs. Un observateur est un nœud qui signale aussi ce qu'il entend via MQTT, par Wi-Fi ou par internet. Le signalement va dans un seul sens : rien ne revient sur le maillage. Un répéteur (un nœud qui transmet les messages) avec un micrologiciel d'observateur continue de répéter comme avant.

Les observateurs de toute l'Europe envoient leurs signalements au [MeshCore Analyzer](https://meshcore-analyzer.eu/) sur mqtt.meshcore-analyzer.eu. L'Analyzer lit aussi d'autres brokers, donc un observateur qui s'y trouve compte aussi. À partir de ces signalements, il construit les cartes, les statistiques et la [liste des canaux](/guides/channels/) de ce site.

{{< callout type="tip" >}}
Le maillage n'a besoin de rien de tout cela. Les signalements des observateurs, l'Analyzer, ces cartes et ces outils passent par internet. En cas de coupure de courant ou de panne d'internet, ils s'arrêtent. Le maillage continue de transmettre les messages par radio, à travers chaque répéteur encore alimenté, comme ceux sur panneau solaire. Les outils servent à voir et à planifier le maillage, pas à le faire fonctionner.
{{< /callout >}}
