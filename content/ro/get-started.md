---
title: Primii pași
lead: De la o placă nouă la primul tău mesaj în mesh. Ai nevoie de o placă LoRa, de un calculator cu Chrome sau Edge și de un telefon sau laptop pentru aplicație.
description: Instalează MeshCore din browser, asociază aplicația, alege presetarea radio din zona ta, trimite primul mesaj și intră pe canalul local.
eyebrow: 6 pași · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-10-31'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Pașii de mai jos se bazează pe firmware-ul MeshCore v1.18.0 și pe instrumentele oficiale
din octombrie 2026. Numele meniurilor din aplicație pot diferi puțin de la o versiune la alta.

## 1. Alege un dispozitiv {#device}

Merge orice placă de pe [pagina de dispozitive](/devices/) la care scrie companion.
Pentru primul tău nod, alege un *companion*: radioul de pe care trimiți mesaje.
Îl asociezi cu telefonul sau laptopul prin Bluetooth sau USB. Poți alege și unul
cu ecran și tastatură proprii, care funcționează singur.

Ia versiunea de 868 MHz. Antena din pachet își face treaba. În
[ghidul despre antene](/guides/antenna/) afli cum verifici o antenă.

{{< callout type="warning" >}}
Montează antena înainte să pornești radioul. Un radio LoRa care
emite fără antenă își poate distruge propriul cip.
{{< /callout >}}

## 2. Instalează firmware-ul {#flash}

1. Conectează dispozitivul la calculator cu un cablu USB de date.
2. Deschide flasher-ul web de la [flasher.meshcore.io](https://flasher.meshcore.io)
   în Chrome sau Edge. Flasher-ul folosește Web Serial, pe care alte browsere nu îl au.
3. Alege dispozitivul, apoi firmware-ul **Companion** pentru **Bluetooth** (sau
   USB, dacă îl vei folosi doar cu un cablu la calculator).
4. Pornește instalarea. Unele plăci trebuie mai întâi trecute în modul de actualizare.
   Flasher-ul îți arată cum.

Folosește *erase* doar când vrei să o iei de la zero. Ștergerea elimină identitatea
dispozitivului și contactele tale. La actualizările ulterioare, instalează fără ștergere.
Ca să îți păstrezi identitatea după o ștergere, exportă mai întâi din aplicație
cheia privată a companion-ului. După ștergere, o imporți înapoi.

## 3. Instalează aplicația {#app}

Aplicația oficială MeshCore există pentru Android, iOS, Windows și macOS.
Pe [meshcore.io](https://meshcore.io) găsești linkuri către toate versiunile. Există și o
aplicație web la [app.meshcore.nz](https://app.meshcore.nz), care rulează în Chrome sau
Edge pe calculator.

## 4. Asociază nodul {#pair}

Pornește nodul, deschide aplicația și conectează-te la nod prin Bluetooth. Când
ți se cere un PIN:

- un nod **cu** ecran afișează un PIN; tastează-l pe acela;
- un nod **fără** ecran folosește `123456`.

Dacă asocierea eșuează, șterge dispozitivul din setările Bluetooth ale telefonului și
încearcă din nou. Apoi dă-i un nume nodului. Ceilalți văd acest nume. Nu folosi
numele complet sau adresa ta decât dacă vrei asta.

## 5. Alege presetarea radio din zona ta {#preset}

Toate radiourile dintr-o zonă folosesc aceeași frecvență și aceleași setări. Altfel nu se aud între ele.
În setările radio ale aplicației, alege presetarea folosită în zona ta.
În afara zonelor de mai jos, Europa folosește **EU/UK (Narrow)**. Țările de Jos,
Cehia, Ungaria, Slovacia, Portugalia și Elveția au propriile presetări. Limburg, în
Țările de Jos, are o variantă proprie:

{{< presets >}}

Dispozitivul tău nu oferă presetarea din zona ta? Introdu manual cele 4 valori din
tabel în setările radio ale aplicației: frecvența, lățimea de bandă, factorul de
împrăștiere și rata de codare. Un nod cu alte valori nu aude mesh-ul.

Nu ești sigur? [Grupul tău local](/community/) știe ce presetare se folosește în zona ta.
Aplicația descarcă această listă de la proiectul MeshCore. De aceea, pentru o presetare nouă
nu ai nevoie de o actualizare a aplicației.

## 6. Salută {#hello}

1. **Anunță-te.** Trimite un *anunț* din aplicație. Un anunț „flood” trece
   prin repetoare (noduri care transmit mesajele mai departe). Așa te poate adăuga
   oricine din mesh.
   Un companion nu se anunță niciodată singur.
2. **Găsește-i pe ceilalți.** Oamenii apar în contactele tale când anunțurile lor ajung
   la tine. Implicit, repetoarele trimit un anunț flood la fiecare 47 de ore. De aceea, lista ta
   se poate umple abia în 2 zile.
3. **Trimite un mesaj.** Deschide un contact și scrie. Primul mesaj se răspândește prin flood
   în toată rețeaua. Destinatarul îți trimite înapoi ruta pe care a venit mesajul, iar
   mesajele următoare urmează acea rută.
4. **Intră pe canale.** Canalul **Public** este deja configurat. Tot ce scrii acolo
   ajunge la toată lumea din mesh. Adaugă *canalul hashtag* al regiunii tale (un nume
   care începe cu `#`) tastându-i numele. [Grupul tău local](/community/) îți spune
   ce canale sunt active.

## Când ceva nu merge {#troubleshooting}

**Aplicația nu îmi găsește dispozitivul prin Bluetooth.**
Probabil ai instalat companion-ul pentru USB. Instalează din nou și alege
versiunea pentru Bluetooth. Pe Heltec V3, mica antenă Bluetooth integrată are
o rază scurtă. Ține telefonul aproape.

**Asocierea eșuează mereu.**
Șterge dispozitivul din setările Bluetooth ale telefonului, repornește Bluetooth-ul
și asociază din nou cu PIN-ul de pe ecran sau cu `123456`.

**Nu apare nimeni în contactele mele.**
Verifică dacă presetarea ta corespunde zonei tale. Trimite un anunț flood. Dacă nu ai
niciun repetor în rază, auzi doar radiourile din apropiere. Pe
[pagina cu harta](/map/) vezi unde sunt repetoarele.

**Un contact apare „văzut ultima dată” acum câteva zile, deși e activ.**
Unul dintre cele două noduri are ora greșită. Un companion ia ora de pe
telefonul tău. La repetoare și la room servere (noduri care păstrează mesajele pentru un
grup), proprietarul trebuie să le seteze ora.

**Un mesaj direct nu ajunge niciodată.**
Trebuie să îl ai pe celălalt în contacte, iar el trebuie să te aibă pe tine. Un nod ignoră mesajul de la cineva
pe care nu îl cunoaște, fără să îl anunțe pe expeditor. Trimite un anunț flood și roagă-l
pe celălalt să trimită și el unul. Verifică în aplicație dacă adaugă automat contactele noi.
Aplicația adaugă doar nodurile aflate în limita ei de salturi.

**Contactele vechi merg, cele noi nu se conectează niciodată.**
Un prim mesaj se trimite prin flood. Un repetor îl transmite mai departe doar dacă are
regiunea mesajului. Mesajele următoare urmează o rută învățată, pe care nicio verificare
de regiune nu o oprește. Întreabă [grupul tău local](/community/) ce regiuni au repetoarele
din jurul tău și verifică [setările pentru zona ta](/guides/settings/#traffic).

**Aplicația nu se mai conectează la companion.**
Unele plăci au un buton de utilizator, de exemplu unele plăci RAK și Heltec T114.
Ține-l apăsat în primele 8 secunde după ce pornește placa. Companion-ul deschide
atunci o consolă de recuperare prin USB. În consola de pe
[flasher.meshcore.io](https://flasher.meshcore.io), `set pin <pin>` setează un
PIN Bluetooth nou, iar `erase` șterge tot de pe dispozitiv.

**Flasher-ul nu poate deschide portul serial pe Linux.**
Utilizatorul tău are nevoie de acces la port, de exemplu prin
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, sau trebuie să fie membru al grupului
`dialout`.

**Altceva.** În
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
găsești multe alte probleme.
