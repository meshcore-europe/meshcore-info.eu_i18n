---
title: Το δίκτυο
layout: network
lead: Δες το mesh σε όλη την Ευρώπη και βοήθησε να φαίνεται περισσότερο. Οι observers ακούν το mesh και το αναφέρουν, και κάθε νέος δείχνει λίγο περισσότερο.
description: 'Πώς γίνεται ορατό το MeshCore mesh στην Ευρώπη: οι observers αναφέρουν ό,τι ακούν στο MeshCore Analyzer. Ζωντανά νούμερα, και πώς προσθέτεις τον δικό σου observer.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-10-31'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Το ίδιο το mesh δεν κρατά κανένα αρχείο: ένα μήνυμα περνά από κόμβο σε κόμβο
και χάνεται. Ό,τι βλέπεις στους [χάρτες κάλυψης](/map/) και στα στατιστικά
προέρχεται από observers. Observer είναι ένας κόμβος που αναφέρει επιπλέον ό,τι
ακούει μέσω MQTT, μέσω Wi-Fi ή του internet. Η αναφορά πηγαίνει μόνο προς μία
κατεύθυνση: τίποτα δεν επιστρέφει στο mesh. Ένας αναμεταδότης (ένας κόμβος που
προωθεί τα μηνύματα) με υλικολογισμικό observer συνεχίζει να αναμεταδίδει όπως πριν.

Observers σε όλη την Ευρώπη στέλνουν αναφορές στο [MeshCore Analyzer](https://meshcore-analyzer.eu/)
στη διεύθυνση mqtt.meshcore-analyzer.eu. Το Analyzer διαβάζει και άλλους brokers,
οπότε μετράει και ένας observer που στέλνει εκεί. Από αυτές τις αναφορές φτιάχνει
τους χάρτες, τα στατιστικά και τη [λίστα καναλιών](/guides/channels/) αυτού του site.

{{< callout type="tip" >}}
Το mesh δεν χρειάζεται τίποτα από αυτά. Τα εργαλεία σε βοηθούν μόνο να το βλέπεις και να το σχεδιάζεις. Οι αναφορές των observers, το Analyzer, αυτοί οι χάρτες
και τα εργαλεία περνούν μέσα από το internet. Σε διακοπή ρεύματος ή όταν πέσει το internet, σταματούν. Το
mesh συνεχίζει να μεταφέρει μηνύματα ασύρματα, μέσα από κάθε αναμεταδότη που έχει ακόμα
ρεύμα, όπως αυτούς με ηλιακά πάνελ.
{{< /callout >}}
