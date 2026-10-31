---
title: Rendre le maillage résistant
lead: Le maillage près de chez toi est lent ou rempli de déchets ? Découvre la cause, active le réglage du répéteur qui l'arrête, et préviens ton groupe local.
description: 'Diffusions massives et spam sur un maillage MeshCore : comment reconnaître chaque type, quel réglage du répéteur aide, comment voir une diffusion massive et comment trouver sa source.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-10-31'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Tes messages arrivent en retard, ou pas du tout ? Public se remplit de
messages indésirables ? C'est une diffusion massive : plus de trafic que le maillage ne
peut en absorber, envoyé par erreur ou exprès. Cherche ce que tu observes dans
les tableaux ci-dessous. Chaque ligne indique le réglage qui l'arrête.
Active-le sur ton répéteur, le nœud qui relaie les messages. Préviens
ensuite ton [groupe local](/community/), pour que les répéteurs autour de
toi fassent pareil. Chaque répéteur qui écarte une diffusion massive libère
du temps d'antenne pour tous les autres.

## Diffusions massives par erreur {#mistake}

Une diffusion massive par erreur vient d'un nœud dont le propriétaire ne
sait pas qu'il la provoque. Elle cesse dès qu'il le sait. Dans les tableaux
ci-dessous, une annonce est le « bonjour » qu'un nœud envoie pour que les
autres le trouvent.

Les réglages des tableaux découlent du fonctionnement du micrologiciel. Ils
n'ont pas encore tous arrêté une diffusion massive sur un vrai maillage.

{{< callout type="warning" >}}
Certains réglages de cette page demandent le micrologiciel DMC. **MeshCore**
1.18.0 standard propose les régions, les limites de sauts `flood.max.*`, la
détection de boucles et le cycle de service. Le filtre de paquets, c'est-à-dire
les règles qui permettent à ton répéteur d'écarter les indésirables, fait partie
du **micrologiciel DMC** de
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). C'est aussi le
cas du blocage selon le cycle de service et du filtre du compagnon. Cette page
suit la version de développement DMC 1.18.0 `ecfb2d4` du 19 octobre 2026 ;
la page [filtre de paquets](/guides/filter/#firmware) explique où la trouver.
{{< /callout >}}

| Ce que tu observes | Ce que c'est | Ce qui aide |
| --- | --- | --- |
| Des requêtes vers les répéteurs depuis un seul nœud, jour et nuit, et un maillage qui reste lent pendant des jours | Un système domotique ou un bot qui demande trop souvent leur état aux répéteurs | `filter on`. Le filtre de paquets laisse alors passer 5 requêtes par minute. Préviens le propriétaire. |
| Le même genre de message sur un canal, chaque minute | Un bot qui publie trop souvent | [Bloque le canal](/guides/filter/#channel) ou [ralentis l'expéditeur](/guides/filter/#sender). Préviens le propriétaire. |
| Des messages illisibles sur Public et d'autres canaux | Un nœud avec un micrologiciel défectueux ou de mauvais réglages radio | `filter malformed on` les écarte sur Public. Préviens le propriétaire. |
| L'annonce d'un même nœud toutes les quelques minutes | Un nœud réglé pour s'annoncer trop souvent | `filter advert 24` laisse passer l'annonce de chaque nœud une fois par jour. `set flood.max.advert 3` limite les annonces à 3 sauts. |
| Des messages venus de loin, avec des régions qui n'ont rien à faire ici | Un pont qui relie des maillages par internet | `set flood.max.unscoped 1`, et place ton répéteur uniquement dans les [régions qu'il dessert](/guides/settings/#traffic). |
| Le même message repasse sans cesse, avec l'ID de ton répéteur plusieurs fois dans son chemin | Un répéteur qui modifie les paquets avant de les relayer, si bien qu'ils tournent en boucle | La détection de boucles est à `minimal` par défaut. `set loop.detect moderate` écarte une boucle plus tôt. |

## Diffusions massives volontaires {#purpose}

Certaines diffusions massives sont du spam : des messages indésirables envoyés exprès pour
engorger le maillage. L'expéditeur change de nom, de clé et de chemin, donc
aucune règle seule ne l'arrête.

| Ce que tu observes | Ce que c'est | Ce qui aide |
| --- | --- | --- |
| Beaucoup de nouveaux nœuds aux noms aléatoires, chacun avec une nouvelle clé | De fausses annonces | `filter rate 04 5 60` laisse passer 5 annonces par minute. `filter advert` n'aide pas : chaque annonce vient d'une [nouvelle clé](#forged). |
| Des messages au texte illisible venant d'expéditeurs inventés, souvent datés de plus d'un an | Du spam de canal | `filter malformed on` les écarte sur Public. `filter age 60` écarte ceux à date ancienne sur Public et sur les [canaux surveillés](/guides/filter/#settings). |
| Jusqu'à 200 messages directs par minute vers des nœuds qui n'existent pas, sans aucun accusé de réception | Une diffusion massive de messages directs | `filter rate 02 5 60`. Ton appli n'affiche pas ces messages ; un observateur, si. |
| Des rafales de requêtes d'un nœud vers des dizaines d'autres | Du spam de requêtes | Avec `filter on`, le filtre de paquets laisse passer 5 requêtes par minute. |
| Un message revient 10 à 20 minutes plus tard, avec presque le même chemin | Un rejeu : une copie renvoyée | Un répéteur retient les 160 derniers paquets qu'il a vus. Sur un maillage chargé, une copie tardive repasse donc. `filter age` écarte un message de groupe plus vieux que ce que tu autorises. |
| Des messages de Public renvoyés sous un expéditeur inventé, parfois avec une date ancienne | Du spam d'écho | `filter age 60`. `filter malformed on` écarte aussi une date décalée de plus d'une semaine. |
| Un message toutes les quelques secondes sur plusieurs canaux, chacun sous un nouveau nom, avec des questions banales | Une vague de bots | `filter rate 05 10 60`, et [bloque les canaux](/guides/filter/#channel) que ta zone n'utilise pas. Chaque nom est nouveau, donc les [règles sur l'expéditeur](#forged) ne l'attrapent pas. |

## Ce qui a marché {#worked}

Des groupes locaux ont arrêté des diffusions massives ainsi :

1. **Préviens le propriétaire.** Une diffusion massive par erreur cesse dès
   que son propriétaire le sait. Envoie-lui un message aimable.
2. **Ne réagis pas sur le maillage.** Une réponse montre au spammeur que son
   spam fonctionne.
3. **Demande des observateurs.** Un observateur est un nœud qui signale par
   MQTT chaque paquet qu'il entend. Plus il y a d'observateurs autour de
   toi, plus vite tu vois par où entre une diffusion massive. Fais de ton
   propre répéteur un observateur avec [MQTT sur ton observateur](/guides/mqtt/).
4. **Trouve la source.** Les observateurs situent l'expéditeur dans une
   zone. Pour le dernier kilomètre, il faut des gens à pied avec une radio. Voir
   [Trouver la source](#source).
5. **Mobilise ton groupe local.** Un répéteur bien réglé aide. Tous les
   répéteurs de la zone ensemble arrêtent une diffusion massive. Ton
   [groupe local](/community/) amène chaque propriétaire à activer le réglage.

## Expéditeurs et chemins inventés {#forged}

L'expéditeur écrit ces parties d'un paquet, et rien ne les vérifie :

- **Le nom de l'expéditeur.** Dans un message de canal, le nom fait partie
  du texte. Quiconque a la clé du canal peut écrire n'importe quel nom.
- **Le début du chemin.** Chaque répéteur ajoute son propre ID à la fin du
  chemin. Rien ne vérifie les ID déjà présents, donc un expéditeur peut
  commencer le chemin par des ID inventés. La fin du chemin est authentique.

{{< forged-path >}}

`filter sender` et `filter path` n'arrêtent donc un expéditeur que jusqu'à
ce qu'il change de nom ou de chemin. Un [blocage de chemin](/guides/filter/#path)
écarte aussi le vrai trafic du répéteur dont l'ID y figure. Les limites de
débit, les limites de sauts, les contrôles d'âge et de format, les blocages
de canaux, les régions et le cycle de service restent efficaces.

## Réglages pour toutes les diffusions massives {#always}

Ces réglages tiennent, quelle que soit la diffusion massive :

- **Cycle de service à 10%.** Ton répéteur n'émet alors jamais plus que ce
  que la loi autorise, quoi qu'il reçoive. Le
  [guide du répéteur](/repeater-guide/#duty-cycle) l'explique.
- **Régions et limites de sauts.** Une région est la zone dans laquelle un
  message reste. Un répéteur ne relaie que les messages des régions qu'il
  détient, et `flood.max.*` garde le trafic proche. Les deux sont décrits
  dans [Limiter le trafic](/guides/settings/#traffic).
- **Le filtre de paquets pour un répéteur chargé.** Les
  [réglages tout prêts](/guides/filter/#busy) divisent par deux les messages
  de groupe et les annonces. Teste-les d'abord en [dry-run](/guides/filter/#dryrun) :
  ce mode compte seulement ce qu'il écarterait.
- **Le filtre du compagnon, dans le micrologiciel DMC.** Ton compagnon, le
  nœud depuis lequel tu envoies tes messages, garde les indésirables hors de ton
  appli. Il masque les messages défectueux et anciens, et ceux d'un
  répéteur, d'un expéditeur ou d'un mot que tu bloques. Une règle sur un
  expéditeur ou un mot masque le message pour toi seul ; les autres le
  reçoivent toujours.

### Blocage selon le cycle de service {#gate}

Avec le micrologiciel DMC, ton répéteur peut donner la priorité à sa propre
région quand il est chargé. Dès qu'il a émis pendant plus de 35% de la dernière
minute, il cesse de relayer les messages sans région. S'il reste chargé, il
écarte ensuite la région la plus large, un niveau à la fois. Sa propre
région passe toujours. Ça ne marche qu'avec des régions configurées sur ton
répéteur. Active-le et vérifie :

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Ce qu'il écarte n'apparaît pas dans `filter stats`. Quand le répéteur
redevient calme, les régions reviennent, de la plus intérieure à la plus
large.

## Voir une diffusion massive {#see}

Ton appli ne montre que ce qui t'arrive. Seul un observateur entend une
diffusion massive de messages directs vers des nœuds qui n'existent pas.
Chaque observateur envoie ses données au
[MeshCore Analyzer](https://meshcore-analyzer.eu/), où tout le monde peut
les voir. Fais de ton répéteur un observateur avec
[MQTT sur ton observateur](/guides/mqtt/).

Sur l'Analyzer, regarde toutes les copies d'un même paquet. Son chemin
montre en général d'où il vient. Un auteur de diffusion massive peut
commencer le chemin par des [ID inventés](#forged), donc les premiers ID ne
t'apprennent rien. Mais chaque copie porte le même début inventé. La copie
au chemin le plus court a traversé le moins de vrais répéteurs : elle a donc
été captée au plus près de l'expéditeur.

{{< copies >}}

Sur ton propre répéteur, `filter stats` montre ce que le filtre de paquets
a écarté. `filter stats top` montre le premier octet des ID de nœuds à
l'origine du plus grand nombre de rejets. Beaucoup de nœuds partagent cet
octet. Il resserre donc la recherche, sans nommer l'expéditeur.

## Trouver la source {#source}

Quand une diffusion massive revient sans cesse :

1. **Suis les chemins.** Lis un chemin en partant de la fin : les derniers
   ID sont les répéteurs que la diffusion massive a traversés. Le premier
   ID authentique est proche de la source ; ceux qui le précèdent peuvent
   être [inventés](#forged).
2. **Resserre la zone.** Plusieurs observateurs qui entendent le même
   paquet situent l'expéditeur dans une zone. Le
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) la calcule à
   partir des répéteurs qui l'ont entendu.
3. **Parcours le dernier kilomètre à pied.** Les répéteurs n'entendent la
   source qu'en limite de portée, donc la dernière partie se fait à pied.
   [Mesh-Hunter](https://mesh-hunter.eu/) s'appaire avec ton compagnon et
   enregistre chaque paquet qu'il entend avec ta position GPS. À plusieurs
   en même temps, on la trouve plus vite.
4. **Préviens ton [groupe local](/community/).** Il voit une plus grande
   partie du maillage, décide de la suite et contacte les auteurs de
   diffusions massives volontaires.

## Ajoute ce que tu as vu {#add}

Tu as subi une diffusion massive absente de ces tableaux ? Un réglage en a
arrêté une ? Dis-le-nous sur
[Discord](https://discord.meshcore-info.eu/) : ce que tu as vu et ce que tu
as activé. Nous l'ajoutons à la page.
