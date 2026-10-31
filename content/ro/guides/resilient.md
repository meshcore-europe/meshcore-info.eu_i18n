---
title: Fă rețeaua mesh rezistentă
lead: Rețeaua mesh din zona ta e lentă sau plină de mesaje inutile? Află ce o cauzează, pornește setarea de repetor care o oprește și anunță grupul local.
description: 'Flood și spam într-o rețea mesh MeshCore: cum recunoști fiecare tip, ce setare de repetor ajută, cum vezi un flood și cum îi găsești sursa.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-10-31'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Mesajele ajung târziu sau deloc? Public se umple de mesaje inutile? Acesta
e un flood: mai mult trafic decât poate duce rețeaua mesh, trimis din
greșeală sau intenționat. Caută în tabelele de mai jos ce vezi. Fiecare rând
numește setarea care îl oprește. Pornește-o pe repetorul tău, nodul care
transmite mesajele mai departe. Apoi anunță [grupul local](/community/),
ca repetoarele din jurul tău să facă la fel. Fiecare repetor care oprește un
flood lasă timp de emisie liber pentru toți ceilalți.

## Flood din greșeală {#mistake}

Un flood din greșeală vine de la un nod al cărui proprietar nu știe că îl
provoacă. Se oprește când proprietarul află. Un anunț, în tabelele de mai
jos, e salutul pe care un nod îl trimite ca să-l găsească ceilalți.

Setările din tabele se bazează pe ce face firmware-ul. Nu toate au oprit
deja un flood într-o rețea mesh reală.

{{< callout type="warning" >}}
Unele setări de pe această pagină au nevoie de firmware-ul DMC. **MeshCore**
1.18.0 standard are regiuni, limitele de salturi `flood.max.*`, detectarea
buclelor și ciclul de funcționare. Filtrul de pachete, regulile cu care
repetorul tău elimină mesajele inutile, vine cu **firmware-ul DMC** de la
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). La fel și
limitarea după ciclul de funcționare și filtrul din companion. Această
pagină urmează versiunea de dezvoltare DMC 1.18.0 `ecfb2d4` din 19 octombrie
2026. Pagina despre [filtrul de pachete](/guides/filter/#firmware) îți spune
de unde o iei.
{{< /callout >}}

| Ce vezi | Ce este | Ce ajută |
| --- | --- | --- |
| Cereri către repetoare de la un singur nod, zi și noapte, și o rețea mesh lentă zile la rând | O automatizare de casă sau un bot care cere prea des starea repetoarelor | `filter on`. Filtrul de pachete lasă apoi să treacă 5 cereri pe minut. Anunță proprietarul. |
| Același tip de mesaj pe un canal, în fiecare minut | Un bot care postează prea des | [Blochează canalul](/guides/filter/#channel) sau [încetinește expeditorul](/guides/filter/#sender). Anunță proprietarul. |
| Mesaje ilizibile pe Public și pe alte canale | Un nod cu firmware defect sau cu setări radio greșite | `filter malformed on` le elimină pe Public. Anunță proprietarul. |
| Anunțul aceluiași nod la câteva minute | Un nod setat să trimită anunțuri prea des | `filter advert 24` lasă să treacă anunțul fiecărui nod o dată pe zi. `set flood.max.advert 3` ține anunțurile în limita a 3 salturi. |
| Mesaje de departe, cu regiuni care nu sunt de aici | O punte care leagă rețele mesh prin internet | `set flood.max.unscoped 1` și pune repetorul doar în [regiunile pe care le deservește](/guides/settings/#traffic). |
| Același mesaj trece iar și iar, cu ID-ul repetorului tău de mai multe ori în rută | Un repetor care modifică pachetele și le transmite mai departe, așa că ele circulă în buclă | Detectarea buclelor rulează implicit pe `minimal`. `set loop.detect moderate` elimină mai repede o buclă. |

## Flood intenționat {#purpose}

Unele flooduri sunt spam: mesaje inutile trimise intenționat ca să
blocheze rețeaua mesh. Expeditorul schimbă nume, chei și rute, așa că nicio
regulă singură nu oprește floodul.

| Ce vezi | Ce este | Ce ajută |
| --- | --- | --- |
| Multe noduri noi cu nume aleatorii, fiecare cu o cheie nouă | Anunțuri false | `filter rate 04 5 60` lasă să treacă 5 anunțuri pe minut. `filter advert` nu ajută: fiecare anunț vine de la o [cheie nouă](#forged). |
| Mesaje cu text ilizibil de la expeditori inventați, adesea datate cu peste un an în urmă | Spam pe canal | `filter malformed on` le elimină pe Public. `filter age 60` le elimină pe cele cu dată veche pe Public și pe [canalele urmărite](/guides/filter/#settings). |
| Până la 200 de mesaje directe pe minut către noduri care nu există, fără confirmări înapoi | Un flood de mesaje directe | `filter rate 02 5 60`. Aplicația ta nu arată aceste mesaje. Un observer le vede. |
| Rafale de cereri de la un nod către zeci de alte noduri | Spam de cereri | Cu `filter on`, filtrul de pachete lasă să treacă 5 cereri pe minut. |
| Un mesaj revine după 10 până la 20 de minute, cu aproape aceeași rută | Replay: o copie trimisă din nou | Un repetor ține minte ultimele 160 de pachete văzute, așa că într-o rețea mesh aglomerată o copie ulterioară trece din nou. `filter age` elimină un mesaj de grup mai vechi decât permiți. |
| Mesaje de pe Public retrimise sub un expeditor inventat, uneori cu o dată veche | Spam de ecou | `filter age 60`. `filter malformed on` elimină și o dată decalată cu peste o săptămână. |
| Un mesaj la câteva secunde pe mai multe canale, de fiecare dată de la un nume nou, cu întrebări obișnuite | Un val de boți | `filter rate 05 10 60` și [blochează canalele](/guides/filter/#channel) pe care zona ta nu le folosește. Fiecare nume e nou, așa că [regulile pentru expeditor](#forged) îl ratează. |

## Ce a funcționat {#worked}

Grupurile locale au oprit flooduri cu acești pași:

1. **Anunță proprietarul.** Un flood din greșeală se oprește când
   proprietarul află. Trimite-i un mesaj prietenos.
2. **Nu reacționa în rețeaua mesh.** Un răspuns îi arată celui care trimite
   spam că spamul funcționează.
3. **Cere observeri.** Un observer e un nod care raportează prin MQTT fiecare
   pachet pe care îl aude. Cu cât sunt mai mulți observeri în jurul tău, cu
   atât vezi mai repede pe unde intră un flood. Transformă-ți propriul
   repetor într-un observer cu [MQTT pe observer](/guides/mqtt/).
4. **Găsește sursa.** Observerii plasează expeditorul într-o zonă. Ultimul
   kilometru îl fac oameni pe jos, cu un radio. Vezi
   [Găsește sursa](#source).
5. **Pune grupul local în mișcare.** Un repetor cu setările potrivite ajută.
   Toate repetoarele din zonă împreună opresc un flood. [Grupul tău
   local](/community/) îi convinge pe toți proprietarii să pornească setarea.

## Expeditori și rute inventate {#forged}

Expeditorul scrie aceste părți ale unui pachet și nimic nu le verifică:

- **Numele expeditorului.** Într-un mesaj de canal, numele face parte din
  text. Oricine are cheia canalului poate scrie orice nume.
- **Începutul rutei.** Fiecare repetor își adaugă ID-ul la capătul rutei.
  Nimic nu verifică ID-urile care erau deja acolo, așa că un expeditor poate
  începe ruta cu ID-uri inventate. Capătul rutei e real.

{{< forged-path >}}

Așadar `filter sender` și `filter path` opresc un expeditor doar până când
își schimbă numele sau ruta. O [blocare de rută](/guides/filter/#path)
elimină și traficul real al repetorului al cărui ID apare în ea. Limitele de
rată, limitele de salturi, verificările de vechime și de mesaje defecte,
blocările de canal, regiunile și ciclul de funcționare continuă să
funcționeze.

## Setări pentru orice flood {#always}

Acestea funcționează indiferent ce flood lovește rețeaua mesh:

- **Ciclul de funcționare la 10%.** Așa, repetorul tău nu emite niciodată
  mai mult decât permite legea, orice ar intra. [Ghidul
  repetorului](/repeater-guide/#duty-cycle) explică asta.
- **Regiuni și limite de salturi.** O regiune e zona în care rămâne un mesaj.
  Un repetor transmite mai departe doar mesajele din regiunile pe care le
  are, iar `flood.max.*` ține traficul aproape. Le găsești pe amândouă în
  [Reduce traficul](/guides/settings/#traffic).
- **Filtrul de pachete pentru un repetor aglomerat.** [Setările
  gata făcute](/guides/filter/#busy) înjumătățesc mesajele de grup și
  anunțurile. Încearcă-le întâi în [dry-run](/guides/filter/#dryrun): acest
  mod doar numără ce ar elimina.
- **Filtrul din companion, în firmware-ul DMC.** Companionul tău, nodul de pe
  care trimiți mesaje, ține mesajele inutile departe de aplicație. Ascunde
  mesajele defecte și vechi și mesajele de la un repetor, un expeditor sau cu
  un cuvânt pe care îl blochezi. O regulă pentru expeditor sau cuvânt
  ascunde mesajul doar de tine. Ceilalți îl primesc în continuare.

### Limitarea după ciclul de funcționare {#gate}

În firmware-ul DMC, repetorul tău poate da prioritate propriei regiuni când
devine aglomerat. Când a emis mai mult de 35% din ultimul minut, nu mai
transmite mai departe mesajele fără regiune. Dacă rămâne aglomerat, renunță
apoi la regiunea cea mai largă, câte un nivel pe rând. Propria regiune trece
mereu. Funcționează doar cu regiuni setate pe repetor. Pornește-o și
verific-o:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Ce elimină nu apare în `filter stats`. Când repetorul e din nou liniștit,
regiunile revin, începând cu cea mai interioară.

## Vezi un flood {#see}

Aplicația ta arată doar ce ajunge la tine. Doar un observer aude un flood de
mesaje directe către noduri care nu există. Fiecare observer raportează
către [MeshCore Analyzer](https://meshcore-analyzer.eu/), unde oricine poate
vedea ce raportează. Transformă-ți repetorul într-un observer cu
[MQTT pe observer](/guides/mqtt/).

În Analyzer, uită-te la fiecare copie a unui pachet. Ruta ei arată de obicei
de unde a venit. Cel care face flood poate începe ruta cu
[ID-uri inventate](#forged), așa că primele ID-uri nu îți spun nimic. Dar
fiecare copie poartă același început inventat. Copia cu ruta cea mai scurtă
a trecut prin cele mai puține repetoare reale, deci a fost auzită cel mai
aproape de expeditor.

{{< copies >}}

Pe propriul repetor, `filter stats` arată ce a eliminat filtrul de pachete.
`filter stats top` arată primul octet al ID-urilor de nod din spatele celor
mai multe eliminări. Multe noduri au același octet, așa că el restrânge
căutarea, dar nu îl identifică pe expeditor.

## Găsește sursa {#source}

Când un flood tot revine:

1. **Urmărește rutele.** Citește o rută de la capăt: ultimele ID-uri sunt
   repetoarele prin care a trecut floodul. Primul ID real e aproape de
   sursă. ID-urile dinaintea lui pot fi [inventate](#forged).
2. **Restrânge zona.** Mai mulți observeri care aud același pachet plasează
   expeditorul într-o zonă. [DMC
   Triangulator](https://triangulator.dutchmeshcore.nl/) calculează zona pe
   baza repetoarelor care l-au auzit.
3. **Parcurge pe jos ultimul kilometru.** Repetoarele aud sursa doar la
   marginea razei lor, așa că ultima parte o fac oameni pe jos.
   [Mesh-Hunter](https://mesh-hunter.eu/) se asociază cu companionul tău și
   înregistrează fiecare pachet pe care îl aude, cu poziția ta GPS. Mai mulți
   oameni care merg în același timp o găsesc mai repede.
4. **Anunță [grupul local](/community/).** Membrii lui văd mai mult din
   rețeaua mesh, decid ce urmează și îi contactează pe cei care fac flood
   intenționat.

## Adaugă ce ai văzut {#add}

Te-a lovit un flood care nu e
în aceste tabele? O setare a oprit un flood? Spune-ne pe
[Discord](https://discord.meshcore-info.eu/): ce ai văzut și ce ai
pornit. Le adăugăm în pagină.
