---
title: Φτιάξε μια ρύθμιση γέφυρας
lead: 'Στείλε όσα ακούει ο αναμεταδότης σου σε οποιονδήποτε MQTT broker: στον δικό σου ή στον Analyzer. Την αποστολή την κάνει ένας υπολογιστής δίπλα στον αναμεταδότη.'
description: Τρέξε το meshcoretomqtt σε ένα Raspberry Pi ή άλλον υπολογιστή για να στέλνεις όσα ακούει ένας αναμεταδότης MeshCore μέσω USB στον δικό σου MQTT broker, στον MeshCore Analyzer ή και στους δύο.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-26'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
---

Ο αναμεταδότης είναι ένας κόμβος που προωθεί μηνύματα. Θέλεις την κίνησή του σε έναν MQTT broker: στον δικό σου, για ένα dashboard ή μια βάση δεδομένων, ή σε αυτόν του [MeshCore Analyzer](https://meshcore-analyzer.eu/). Ή ο αναμεταδότης σου δεν έχει δικό του Wi-Fi, αλλά δίπλα του βρίσκεται ένα Raspberry Pi ή ένας server. Το [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), ένα εργαλείο της κοινότητας, είναι η γέφυρα: στέλνει την κίνηση από αυτόν τον υπολογιστή. Ο αναμεταδότης σου συνεχίζει να αναμεταδίδει, γιατί η γέφυρα διαβάζει μόνο όσα καταγράφει μέσω USB.

## Τι χρειάζεσαι {#need}

- Έναν αναμεταδότη χτισμένο με καταγραφή πακέτων (βλέπε παρακάτω).
- Ένα Raspberry Pi Zero, 2, 3 ή 4, ή οποιονδήποτε υπολογιστή με Linux ή macOS, με Python 3.11 ή νεότερη.
- Ένα καλώδιο δεδομένων USB ανάμεσα στα δύο.

Το τυπικό υλικολογισμικό αναμεταδότη από τον flasher δεν καταγράφει πακέτα. Χτίσε μόνος σου το υλικολογισμικό αναμεταδότη από τον [πηγαίο κώδικα του MeshCore](https://github.com/meshcore-dev/MeshCore), προσθέτοντας αυτή τη σημαία στο build της πλακέτας σου:

```text
-D MESH_PACKET_LOGGING=1
```

## Εγκατάσταση {#install}

Σύνδεσε τον αναμεταδότη στον υπολογιστή και μετά τρέξε σε αυτόν τον υπολογιστή το σενάριο εγκατάστασης του meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Εγκαθιστά τη γέφυρα ως υπηρεσία που ξεκινά μαζί με τον υπολογιστή και σε ρωτά σε ποιους brokers να στέλνει. Ο Analyzer δεν υπάρχει σε αυτή τη λίστα· τον προσθέτεις στο αρχείο ρυθμίσεων παρακάτω. Οι δικές σου ρυθμίσεις βρίσκονται στο `/etc/mctomqtt/config.d/99-user.toml`. Μια ενημέρωση δεν αντικαθιστά ποτέ αυτό το αρχείο.

## Brokers {#brokers}

Κάθε broker παίρνει το δικό του μπλοκ `[[broker]]`, οπότε ένας αναμεταδότης μπορεί να τροφοδοτεί πολλούς ταυτόχρονα. Ο δικός σου broker δέχεται όνομα χρήστη και κωδικό, ή καθόλου σύνδεση (`method = "none"`). Ο MeshCore Analyzer δέχεται αντί γι' αυτά ένα token, το οποίο υπογράφει το κλειδί του αναμεταδότη σου:

- διεύθυνση `mqtt.meshcore-analyzer.eu`, θύρα `443`, μέσω ασφαλούς websocket·
- το audience του token είναι η ίδια διεύθυνση.

## Το αρχείο ρυθμίσεών σου {#config}

Αντικατάστησε το περιεχόμενο του `/etc/mctomqtt/config.d/99-user.toml` με το παρακάτω. Συμπλήρωσε τον κωδικό του πλησιέστερου αεροδρομίου στον αναμεταδότη σου (για παράδειγμα `AMS`) και τη θύρα USB στην οποία είναι συνδεδεμένος ο αναμεταδότης σου. Μετά πρόσθεσε τον δικό σου broker. Παράλειψε όποιο μπλοκ δεν χρειάζεσαι.

```toml
[general]
iata = "AMS"

[serial]
ports = ["/dev/ttyACM0"]

# Your own broker
[[broker]]
name = "my-broker"
enabled = true
server = "mqtt.example.org"
port = 1883

[broker.auth]
method = "password"
username = "my_username"
password = "my_password"

# The MeshCore Analyzer
[[broker]]
name = "meshcore-analyzer"
enabled = true
server = "mqtt.meshcore-analyzer.eu"
port = 443
transport = "websockets"

[broker.tls]
enabled = true
verify = true

[broker.auth]
method = "token"
audience = "mqtt.meshcore-analyzer.eu"
```

Μετά από κάθε αλλαγή κάνε επανεκκίνηση της υπηρεσίας (`sudo systemctl restart mctomqtt` σε Linux). Ο αναμεταδότης σου εμφανίζεται τότε στον Analyzer ως observer, δηλαδή ένας κόμβος που ανεβάζει όσα ακούει, με το όνομα του ίδιου του αναμεταδότη σου. Όλες τις υπόλοιπες ρυθμίσεις θα τις βρεις στο [README του meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt).
