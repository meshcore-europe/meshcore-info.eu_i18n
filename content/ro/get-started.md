---
title: Primii pași
lead: De la o placă nouă la primul tău mesaj pe mesh. Ai nevoie de o placă LoRa, un calculator cu Chrome sau Edge și un telefon sau laptop pentru aplicație.
description: Instalează MeshCore din browser, asociază aplicația, alege presetul radio folosit în zona ta, trimite primul mesaj și intră pe canalul local.
eyebrow: 6 pași · MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '68c89544'
  seeded: '2026-10-26'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', '36a3eba3', '6da9fd7a', 'cb5fb72e', '89626504', 'a419ce79', 'aa273b20']
---

Acești pași urmează firmware-ul MeshCore v1.18.0 și instrumentele oficiale din
octombrie 2026. Numele din meniurile aplicației pot diferi puțin între versiuni.

## 1. Alege un dispozitiv {#device}

Merge orice placă de pe [pagina de dispozitive](/devices/) marcată ca companion. Pentru
primul tău nod, alege un *companion*: radioul de pe care trimiți mesaje. Îl asociezi cu
telefonul sau laptopul prin Bluetooth sau USB, sau alegi unul cu ecran și tastatură proprii,
care funcționează singur.

Ia versiunea de 868 MHz. Antena livrată își face treaba; în
[ghidul despre antene](/guides/antenna/) vezi cum o verifici.

{{< callout type="warning" >}}
Montează antena înainte să pornești radioul. Un radio LoRa care
emite fără antenă își poate distruge propriul cip.
{{< /callout >}}

## 2. Instalează firmware-ul {#flash}

1. Conectează dispozitivul la calculator cu un cablu USB de date.
2. Deschide flasher-ul web de la [flasher.meshcore.io](https://flasher.meshcore.io)
   în Chrome sau Edge. Folosește Web Serial, pe care alte browsere nu îl au.
3. Alege dispozitivul tău, apoi firmware-ul **Companion** pentru **Bluetooth** (sau
   USB, dacă îl vei folosi doar legat prin cablu la un calculator).
4. Scrie firmware-ul. Unele plăci intră mai întâi în modul de actualizare; flasher-ul îți
   spune cum.

Folosește *erase* doar pentru un început de la zero: ștergerea elimină identitatea
dispozitivului și contactele tale. La actualizările ulterioare, scrie firmware-ul fără ștergere.

## 3. Instalează aplicația {#app}

Aplicația oficială MeshCore există pentru Android, iOS, Windows și macOS;
pe [meshcore.io](https://meshcore.io) găsești linkuri către fiecare versiune. Există și o
aplicație web la [app.meshcore.nz](https://app.meshcore.nz), care rulează în Chrome sau
Edge pe un calculator.

## 4. Asociază nodul tău {#pair}

Pornește nodul, deschide aplicația și conectează-te la el prin Bluetooth. Când
îți cere un PIN:

- un nod **cu** ecran afișează un PIN; tastează-l pe acela;
- un nod **fără** ecran folosește `123456`.

Dacă asocierea eșuează, șterge dispozitivul din setările Bluetooth ale telefonului și
încearcă din nou. Apoi dă-i nodului un nume. Ceilalți văd acest nume, așa că nu folosi
numele complet sau adresa decât dacă vrei.

## 5. Alege presetul radio al zonei tale {#preset}

Toate radiourile dintr-o zonă folosesc aceeași frecvență și aceleași setări, altfel nu
se aud între ele. În setările radio ale aplicației, alege presetul folosit în zona ta.
În afara zonelor de mai jos, Europa folosește **EU/UK (Narrow)**. Țările de Jos, Cehia,
Ungaria, Slovacia, Portugalia și Elveția au preseturi proprii, iar Limburg din Țările de Jos
are o variantă:

{{< presets >}}

Nu ești sigur? [Grupul tău local](/community/) știe ce preset folosește zona ta.
Aplicația descarcă lista de la proiectul MeshCore, așa că un preset nou nu are nevoie
de o actualizare a aplicației.

## 6. Spune salut {#hello}

1. **Anunță-te.** Trimite un *anunț* din aplicație. Un anunț "flood"
   trece prin repetoare (noduri care transmit mesajele mai departe), astfel încât toți
   de pe mesh te pot adăuga.
   Companionii nu se anunță niciodată automat.
2. **Găsește-i pe ceilalți.** Oamenii apar în contactele tale după ce anunțurile lor ajung
   la tine. Repetoarele trimit implicit un anunț flood la fiecare 47 de ore, așa că lista
   ta se poate umple în 2 zile.
3. **Trimite un mesaj.** Deschide un contact și scrie. Primul mesaj pleacă prin flood
   în rețea; destinatarul raportează ruta pe care a mers, iar mesajele
   următoare urmează acea rută.
4. **Intră pe canale.** Canalul **Public** este deja configurat; tot ce
   scrii acolo ajunge la toți de pe mesh. Adaugă *canalul hashtag* al regiunii tale
   (un nume care începe cu `#`) tastându-i numele.
   [Grupul tău local](/community/) îți spune ce canale sunt active.

## Când ceva nu merge {#troubleshooting}

**Aplicația nu îmi găsește dispozitivul prin Bluetooth.**
Probabil ai instalat companionul USB. Instalează din nou și alege
versiunea Bluetooth. Pe Heltec V3, mica antenă Bluetooth integrată
are o rază scurtă; ține telefonul aproape.

**Asocierea eșuează mereu.**
Șterge dispozitivul din setările Bluetooth ale telefonului, repornește Bluetooth
și asociază din nou cu PIN-ul de pe ecran sau cu `123456`.

**Nu apare nimeni în contactele mele.**
Verifică dacă presetul tău se potrivește cu zona. Trimite un anunț flood. Dacă nu ai niciun
repetor în rază, auzi doar radiourile din apropiere;
[pagina cu harta](/map/) arată unde sunt repetoarele.

**Un contact apare "văzut ultima dată" cu zile în urmă, deși este activ.**
Unul dintre cele două noduri are ora greșită. Un companion preia ora de la
telefonul tău; repetoarele și serverele de cameră (noduri care stochează mesaje pentru un
grup) au nevoie ca proprietarul lor să le seteze ora.

**Flasher-ul nu poate deschide portul serial pe Linux.**
Utilizatorul tău are nevoie de acces la port, de exemplu cu
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0` sau prin apartenența la grupul
`dialout`.

**Altceva.**
[Întrebările frecvente MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
acoperă multe alte probleme.
