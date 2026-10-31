---
title: Φτιάξε μια ρύθμιση γέφυρας
lead: 'Στείλε ό,τι ακούει ο αναμεταδότης σου σε οποιονδήποτε MQTT broker: στον δικό σου ή στον Analyzer. Την αποστολή την κάνει ένας υπολογιστής δίπλα στον αναμεταδότη.'
description: Τρέξε το meshcoretomqtt σε ένα Raspberry Pi ή σε άλλον υπολογιστή και στείλε ό,τι ακούει ένας αναμεταδότης MeshCore μέσω USB στον δικό σου MQTT broker, στον MeshCore Analyzer ή και στους δύο.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-31'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Αναμεταδότης είναι ένας κόμβος που προωθεί τα μηνύματα. Θέλεις η κίνησή του να φτάνει σε
έναν MQTT broker: στον δικό σου για ένα dashboard ή μια βάση δεδομένων, ή στον broker του
[MeshCore Analyzer](https://meshcore-analyzer.eu/). Ή ο αναμεταδότης σου δεν έχει
δικό του Wi-Fi, αλλά δίπλα του βρίσκεται ένα Raspberry Pi ή ένας server.
Το [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), ένα εργαλείο της κοινότητας,
είναι η γέφυρα: στέλνει την κίνηση από εκείνον τον υπολογιστή. Ο αναμεταδότης σου συνεχίζει
να αναμεταδίδει, γιατί η γέφυρα διαβάζει μόνο ό,τι καταγράφει εκείνος μέσω USB.

## Τι χρειάζεσαι {#need}

- Έναν αναμεταδότη με build που καταγράφει πακέτα (δες παρακάτω).
- Ένα Raspberry Pi Zero, 2, 3 ή 4, ή οποιονδήποτε υπολογιστή με Linux ή macOS, με Python
  3.11 ή νεότερη.
- Ένα καλώδιο USB δεδομένων ανάμεσα στα δύο.

Το τυπικό υλικολογισμικό αναμεταδότη από τον flasher δεν καταγράφει πακέτα. Κάνε εσύ
το build του υλικολογισμικού αναμεταδότη από τον
[πηγαίο κώδικα του MeshCore](https://github.com/meshcore-dev/MeshCore). Πρόσθεσε αυτό το flag
στο build της πλακέτας σου:

```text
-D MESH_PACKET_LOGGING=1
```

## Εγκατάσταση {#install}

Σύνδεσε τον αναμεταδότη στον υπολογιστή. Μετά τρέξε το script εγκατάστασης του
meshcoretomqtt σε εκείνον τον υπολογιστή:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Το script εγκαθιστά τη γέφυρα ως υπηρεσία που ξεκινά μαζί με τον υπολογιστή. Σε ρωτά επίσης
σε ποιους brokers θα στέλνει. Ο Analyzer δεν είναι σε αυτή τη λίστα· τον προσθέτεις στο
αρχείο ρυθμίσεων παρακάτω. Οι δικές σου ρυθμίσεις βρίσκονται στο
`/etc/mctomqtt/config.d/99-user.toml`· μια ενημέρωση δεν αντικαθιστά ποτέ αυτό το αρχείο.

## Brokers {#brokers}

Κάθε broker έχει το δικό του μπλοκ `[[broker]]`, οπότε ένας αναμεταδότης μπορεί να τροφοδοτεί πολλούς
ταυτόχρονα. Ο δικός σου broker θέλει όνομα χρήστη και κωδικό, ή καθόλου στοιχεία σύνδεσης
(`method = "none"`).
Ο MeshCore Analyzer θέλει αντί γι' αυτό ένα token, που το υπογράφει το κλειδί του αναμεταδότη σου:

- διεύθυνση `mqtt.meshcore-analyzer.eu`, θύρα `443`, μέσω ασφαλούς websocket·
- το audience του token είναι η ίδια διεύθυνση.

## Το αρχείο ρυθμίσεών σου {#config}

Αντικατέστησε το περιεχόμενο του `/etc/mctomqtt/config.d/99-user.toml` με αυτό. Συμπλήρωσε
τον κωδικό του κοντινότερου αεροδρομίου στον αναμεταδότη σου (για παράδειγμα `AMS`) και τη θύρα USB
όπου είναι συνδεδεμένος ο αναμεταδότης σου. Μετά πρόσθεσε τον δικό σου broker. Παράλειψε όποιο μπλοκ
δεν χρειάζεσαι.

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

Μετά από κάθε αλλαγή, κάνε επανεκκίνηση της υπηρεσίας (`sudo systemctl restart mctomqtt` σε
Linux). Τότε ο αναμεταδότης σου εμφανίζεται στον Analyzer ως observer, δηλαδή κόμβος που
ανεβάζει ό,τι ακούει, με το όνομα του ίδιου του αναμεταδότη σου. Στο
[README του meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) βρίσκεις όλες τις
υπόλοιπες ρυθμίσεις.
