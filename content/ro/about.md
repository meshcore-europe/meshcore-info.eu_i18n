---
title: Ce este MeshCore?
lead: MeshCore trimite mesaje text prin radio, de la un nod la altul. Funcționează fără internet și fără abonament.
description: 'Ce este și ce nu este MeshCore: rețeaua mesh, companionii, repetoarele și serverele de cameră, rutarea, criptarea și banda de 868 MHz în Europa.'
eyebrow: MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '33e571f0'
  seeded: '2026-10-26'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['a3a6c1ff', '007314d2', 'f1f23981', '493b444f', '429f699c', 'f8008f48', '655373a9']
---

MeshCore este un software gratuit pentru radiouri LoRa mici. LoRa este o tehnică radio
care transmite puține date la distanță mare, cu foarte puțină energie. Un radio cu MeshCore
se numește *nod*. Asociat cu aplicația de pe telefon sau laptop, sau cu propriul
ecran și propria tastatură, trimite text unor oameni aflați la kilometri distanță. Între ele nu există niciun turn, router sau operator.

MeshCore trimite doar mesaje text scurte: fără voce, fotografii sau trafic
de internet.
Un mesaj poate dura câteva secunde, iar dacă ajunge depinde de
repetoarele din jurul tău. Nu înlocuiește serviciile de urgență: în caz de
urgență, sună la 112.

Software-ul este open source și este dezvoltat la
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) sub licența
MIT.

## Rețeaua mesh într-un minut {#mesh}

Un radio LoRa acoperă câțiva kilometri într-un oraș și mult mai mult de pe un
deal sau de pe un acoperiș. Ca să ajungă mai departe, radiourile își transmit mesajele unul altuia: asta
este o rețea *mesh*. În MeshCore, retransmiterea o fac radiouri numite *repetoare*. Un
repetor care aude un mesaj îl trimite din nou, astfel încât mesajul poate traversa o regiune întreagă.

Nimeni nu deține rețeaua mesh. Fiecare nod și fiecare repetor aparține cuiva din
comunitate. Rețeaua mesh este atât de bună cât sunt repetoarele instalate de oameni.

## Cele 3 tipuri de nod {#roles}

Tipul unui nod îl alegi atunci când îl flashezi. Primul tău nod este un companion.

**Companion.** Radioul tău personal. Se asociază cu aplicația MeshCore de pe telefon sau
laptop prin Bluetooth sau USB; unele au propriul ecran și propria tastatură. În aplicație
citești și scrii. Companionul păstrează contactele și canalele tale,
precum și mesajele sosite cât timp aplicația nu era conectată. Un companion nu retransmite mesaje pentru alții.

**Repetor.** Un radio montat la înălțime, care retransmite mesaje pentru toată lumea. Cele mai multe
funcționează cu energie solară. Ai nevoie de unul propriu doar acolo unde rețeaua mesh nu ajunge
încă. Nu are o aplicație proprie. Îl configurezi prin USB sau
te autentifici cu o parolă și îl administrezi prin radio.
[Ghidul pentru repetoare](/repeater-guide/) îți arată cum.

**Server de cameră.** Un mic avizier pe rețeaua mesh. Când te autentifici, primești
postările ratate cât timp ai fost în afara razei, cel mult ultimele 32. Un grup local
folosește unul pentru anunțuri.

## Cum își găsește drumul un mesaj {#routing}

Fiecare nod are o cheie secretă și o cheie publică. Cheia publică este identitatea lui. Un nod
se anunță printr-un *anunț*: un pachet semnat, cu numele său și, dacă
alegi, cu poziția sa. Cineva apare în contactele tale după ce unul dintre
anunțurile lui a ajuns la tine, sau când îi scanezi codul QR. Aplicația are un buton pentru a trimite propriul anunț.

Primul tău mesaj către un contact pleacă prin *flood*. Fiecare repetor care îl
aude îl retransmite o singură dată și adaugă pe drum propriul ID scurt. Răspunsul
aduce înapoi acea listă de ID-uri. De atunci, mesajele tale către acel contact
urmează ruta înregistrată, iar doar repetoarele de pe ea transmit. Când ruta
se rupe, aplicația face din nou flood.

Mesajele către un canal nu au o singură adresă, așa că merg întotdeauna prin flood.
Repetoarele țin minte ce au retransmis de curând și ignoră copiile care sosesc
din nou pe altă rută. Un mesaj poate traversa cel mult 64 de repetoare, sau 32 acolo unde presetarea folosește ID-uri
de 2 octeți.

## Criptare și confidențialitate {#encryption}

Mesajele tale directe sunt criptate de la un capăt la altul: doar tu și cealaltă persoană
le puteți citi. Un repetor vede cui îi este destinat un pachet doar ca un indiciu de 1 octet.

Canalele sunt criptate cu o cheie comună, așa că cine le poate citi depinde de cine
are acea cheie:

- **Public** este configurat pe fiecare companion. Cheia lui este publicată, deci oricine
  îl poate citi.
- **Canalele hashtag**, cum ar fi `#utrecht`, își iau cheia din propriul nume.
  Oricine știe numele se poate alătura, așa că tratează-le tot ca pe unele publice.
- **Canalele private** folosesc o cheie aleatorie, pe care o distribui chiar tu, de exemplu
  sub forma unui cod QR.

Anunțurile sunt semnate, dar nu criptate. Numele nodului tău, și poziția lui dacă
o partajezi, sunt vizibile pentru toți cei din rază. Alege un nume care nu spune mai mult
decât vrei tu.

## Banda de 868 MHz în Europa {#band}

În Europa, MeshCore folosește o mică parte din banda de 868 MHz, pe care oricine o poate folosi
fără licență. Presetarea radio europeană, EU/UK (Narrow), este la
869.618 MHz, pe un canal de 62.5 kHz. Aceasta se află în sub-banda
869.40-869.65 MHz, care permite până la 500 mW e.r.p. Un dispozitiv poate transmite acolo cel mult 10%
din timp.
[Secțiunea legală din ghidul pentru repetoare](/repeater-guide/#legal) conține detaliile
și limitele pentru fiecare țară.

Toată lumea dintr-o zonă folosește aceeași presetare, altfel radiourile nu se pot auzi
între ele. Unele țări și regiuni folosesc o variantă: 
[grupul tău local](/community/) știe care.

## La ce îl folosesc oamenii {#uses}

- Pentru a rămâne în legătură pe trasee montane, pe mare și la festivaluri, unde rețeaua mobilă
  este supraîncărcată sau lipsește.
- Ca un canal de rezervă pentru familie sau vecini, când cad curentul sau rețelele
  mobile.
- Pentru chat local pe radiouri pe care oamenii le dețin ei înșiși.
- Pentru a experimenta cu radio, antene, energie solară și software open source.
