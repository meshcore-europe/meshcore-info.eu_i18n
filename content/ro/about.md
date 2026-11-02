---
title: Ce este MeshCore?
lead: MeshCore trimite mesaje text prin radio, de la nod la nod. Funcționează fără internet și fără abonament.
description: 'Ce este MeshCore și ce nu este: tipuri de noduri, rutare, diferențele față de Meshtastic, criptarea și banda de 868 MHz.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '279b56a4'
  seeded: '2026-11-02'
  fields: {title: '06eda66b', lead: 'c0174569', description: '15e6d2a7', eyebrow: '8610c822'}
  sections: ['aa768ac3', '16fde264', '0a55792c', 'c3de803d', '493b444f', 'a8b2b9b4', '429f699c', 'f8008f48', '88af2bd3', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'fab378a5', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', 'fc8f3129', '8dec428a', '07cbac35', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '95e18f18', '02f1fe2f', 'e6b5b258']
---

MeshCore este un software gratuit pentru radiouri LoRa mici. LoRa este o tehnică radio
care trimite puține date la distanțe mari, cu foarte puțină energie. Un radio cu MeshCore
se numește *nod*. Îl asociezi cu aplicația de pe telefon sau laptop, sau îl folosești cu
ecranul și tastatura lui. Așa trimiți text unor oameni aflați la kilometri distanță. Între tine și ei nu stă niciun turn, router sau furnizor.

Software-ul este open source și este dezvoltat la
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore), sub licența
MIT.

## Ce nu este MeshCore {#not}

Ești nou în lumea radio? Acestea sunt lucrurile pe care oamenii le așteaptă cel mai des de la MeshCore,
dar pe care MeshCore nu le face.

- **Nu este internet și nici telefon.** MeshCore trimite mesaje text scurte,
  cam cât un SMS pe telefonul tău. Fără voce, fotografii, video
  sau site-uri web, și nu poți contacta un număr de telefon obișnuit.
- **Nu este un serviciu de urgență.** Niciun serviciu de urgență nu ascultă în
  mesh și nimeni nu îți promite că cineva îți citește mesajul. În caz de
  urgență, sună la 112.
- **Nu este instant și nu merge peste tot.** Un mesaj sare din radio în
  radio și poate dura câteva secunde sau poate să nu ajungă deloc. Dacă ajunge sau nu depinde
  de repetoarele din jurul tău, de înălțime, de clădiri și de antena ta.
  În interior, un radio mic adesea nu ajunge la nimeni; un repetor pe acoperiș
  ajunge la kilometri distanță.
- **Nu este un serviciu pe care cineva îl operează pentru tine.** Nu există furnizor,
  nici helpdesk, nici promisiune de acoperire. Mesh-ul există acolo unde oamenii din
  comunitate au instalat repetoare, și nicăieri altundeva.
- **Nu tot ce circulă în mesh este privat.** Mesajele directe sunt criptate, dar
  oricine poate citi canalul Public și canalele cu hashtag, iar numele nodului tău
  și poziția pe care o partajezi sunt vizibile pentru toți cei aflați în rază.
  [Observatorii](/network/) raportează hărților publice ce aud.
  [Secțiunea despre criptare](#encryption) explică ce rămâne privat.
- **Nu este nelimitat.** Toți cei dintr-o zonă folosesc în comun un singur canal radio, iar
  regulile pentru [banda de 868 MHz](#band) limitează cât timp poate transmite fiecare radio.
  Fiecare mesaj consumă din timpul de emisie al tuturor celorlalți, așa că boții, anunțurile dese
  și mesajele de test încetinesc mesh-ul pentru toți.
- **Nu este Meshtastic.** Meshtastic este un alt sistem, care rulează pe
  aproape aceleași plăci. Cele două nu pot comunica între ele.
  [Dacă vii de la Meshtastic](#meshtastic) arată ce funcționează altfel.

## Mesh-ul într-un minut {#mesh}

Un radio LoRa ajunge la câțiva kilometri într-un oraș și mult mai departe de
pe un deal sau un acoperiș. Ca să ajungă mai departe, radiourile își transmit
mesajele unele altora: asta este un *mesh*. În MeshCore, radiourile numite
*repetoare* se ocupă de retransmitere. Un repetor care aude un mesaj îl
trimite din nou, așa că mesajul poate traversa o regiune întreagă.

Mesh-ul nu aparține nimănui. Fiecare nod și fiecare repetor aparține cuiva din
comunitate. Mesh-ul ajunge până unde ajung repetoarele lor.

## Cele 3 tipuri de nod {#roles}

Tipul unui nod îl alegi când îi încarci firmware-ul. Primul tău nod este un companion.

**Companion.** Radioul tău personal. Îl asociezi cu aplicația MeshCore de pe
telefon sau laptop prin Bluetooth sau USB. Unele au propriul ecran și propria
tastatură. În aplicație citești și scrii. Companionul îți păstrează contactele
și canalele, plus mesajele sosite cât timp aplicația nu era conectată. Un companion nu retransmite mesajele altora.

**Repetor.** Un radio montat la înălțime, care retransmite mesajele tuturor.
Majoritatea funcționează cu energie solară. Ai nevoie de unul propriu doar
acolo unde mesh-ul încă nu ajunge. Nu are aplicație proprie. Îl configurezi
prin USB sau te autentifici cu o parolă și îl administrezi prin radio.
[Ghidul pentru repetoare](/repeater-guide/) îți arată cum.

**Server de cameră.** Un mic avizier în mesh. Când te autentifici, primești
postările pierdute cât ai fost în afara razei, până la ultimele 32. Serverul
le ține doar în memorie, așa că o repornire sau o pană de curent le șterge.
Un grup local folosește un astfel de server pentru anunțuri.

## Cum își găsește un mesaj drumul {#routing}

Fiecare nod are o cheie secretă și o cheie publică. Cheia publică este identitatea lui. Un nod
se face cunoscut printr-un *anunț*: un pachet semnat, cu numele lui și, dacă
vrei, poziția. Cineva apare în contactele tale după ce unul dintre anunțurile
lui a ajuns la tine sau după ce îi scanezi codul QR. Aplicația are un buton pentru a-l trimite pe al tău.

Primul tău mesaj către un contact pleacă prin *flood*. Fiecare repetor care îl
aude îl retransmite o dată și își adaugă pe drum propriul ID scurt. Răspunsul
aduce înapoi lista de ID-uri. Din acel moment, mesajele tale către acel contact
urmează ruta înregistrată și emit doar repetoarele de pe ea. Când ruta se
întrerupe, aplicația trimite din nou prin flood.

Mesajele către un canal nu au o singură adresă, așa că merg mereu prin flood.
Repetoarele își amintesc ce au retransmis recent și aruncă copiile care sosesc
din nou pe altă rută. Un mesaj poate trece prin cel mult 64 de repetoare, sau 32 acolo unde presetarea folosește
ID-uri de 2 octeți.

## Dacă vii de la Meshtastic {#meshtastic}

Multe plăci rulează fie MeshCore, fie Meshtastic, iar tu încarci firmware-ul pe care îl
vrei. Acestea sunt diferențele pe care le observi mai întâi. Se bazează pe MeshCore
v1.18.0 și pe documentația Meshtastic din noiembrie 2026.

- **Cine retransmite mesajele.** În MeshCore o fac doar repetoarele; companionul tău
  nu o face niciodată. În Meshtastic, rolul implicit de client retransmite și el
  mesajele, dacă nu a făcut-o deja alt nod.
- **Cât de departe ajunge un mesaj.** Un mesaj MeshCore poate trece prin cel mult 64
  de repetoare. Meshtastic se oprește implicit după 3 salturi, iar maximul este 7.
- **Valori măsurate de la alte noduri.** Repetoarele și nodurile cu senzori din MeshCore trimit
  valori măsurate, cum ar fi tensiunea bateriei, când le ceri. Nu le trimit în tot mesh-ul.
- **Internetul.** Firmware-ul MeshCore nu are nicio legătură între mesh-uri prin
  internet. [Observatorii](/network/) transmit hărților ce aud, doar într-un singur
  sens. Meshtastic are un modul MQTT integrat, care poate transmite mesaje între
  mesh-uri prin internet.

## Criptare și confidențialitate {#encryption}

Mesajele tale directe sunt criptate cap la cap: doar tu și cealaltă persoană
le puteți citi. Un repetor vede destinatarul unui pachet doar sub forma unui indiciu de 1 octet.

Canalele sunt criptate cu o cheie comună. Cine le poate citi depinde deci de
cine are acea cheie:

- **Public** este configurat pe fiecare companion. Cheia lui este publicată,
  așa că oricine îl poate citi.
- **Canalele cu hashtag**, cum ar fi `#utrecht`, își obțin cheia din nume.
  Oricine știe numele poate intra, așa că tratează-le tot ca publice.
- **Canalele private** folosesc o cheie aleatorie pe care o partajezi tu,
  de exemplu printr-un cod QR.

Anunțurile sunt semnate, dar nu criptate. Numele nodului tău și poziția, dacă
o partajezi, le vede oricine se află în raza de acoperire. Alege un nume care
nu spune mai mult decât vrei.

## Banda de 868 MHz în Europa {#band}

În Europa, MeshCore folosește o mică parte din banda de 868 MHz, pe care o
poate folosi oricine fără licență. Presetarea radio europeană, EU/UK (Narrow),
este pe 869.618 MHz, pe un canal de 62.5 kHz. Aceasta se află în sub-banda
869.40-869.65 MHz, care permite până la 500 mW e.r.p. Acolo, un dispozitiv
poate emite cel mult 10% din timp.
[Secțiunea juridică din ghidul pentru repetoare](/repeater-guide/#legal) are
detaliile și limitele pentru fiecare țară.

Toți cei dintr-o zonă folosesc aceeași presetare, altfel radiourile lor nu se
aud între ele. Unele țări și regiuni folosesc o variantă: [grupul tău
local](/community/) știe care.

## La ce îl folosesc oamenii {#uses}

- Păstrezi legătura în drumeții, pe mare și la festivaluri unde rețeaua mobilă
  este supraîncărcată sau lipsește.
- Un canal de rezervă pentru familie sau vecini când pică curentul sau rețelele
  mobile.
- Chat local pe radiouri pe care oamenii le dețin chiar ei.
- Verifici de acasă un loc îndepărtat. Repetoarele și nodurile cu senzori îți trimit
  tensiunea bateriei și alte valori măsurate când le ceri.
- Urmărești un senzor. Un nod cu senzori rulează firmware-ul MeshCore pentru
  măsurători. Nodul păstrează un istoric al valorilor măsurate. Dacă te abonezi, te
  avertizează, de exemplu când i se descarcă bateria.
- Comuți ceva aflat departe, de exemplu o pompă. Adaugi funcția asta în firmware-ul
  pentru senzori, cu propriul tău cod.
- Faci experimente cu radio, antene, energie solară și software open source.

## De unde provin datele {#data}

Căutarea de pe pagina [grupurilor locale](/community/) găsește o localitate
folosind o copie a listelor gratuite de localități și coduri poștale de la
[GeoNames](https://www.geonames.org/), sub licența
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Copia se află pe
acest site. Căutarea ta nu părăsește dispozitivul și nicio cerere nu ajunge la
GeoNames.
