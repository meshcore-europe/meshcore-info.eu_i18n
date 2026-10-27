---
title: Filtrul de pachete
lead: 'Nu lăsa repetorul tău să transmită gunoi mai departe: flood-uri de departe, un bot care nu se oprește, un canal zgomotos. Testează mai întâi o setare, apoi activeaz-o.'
description: 'Filtrul de pachete din firmware-ul de repetor DMC: ce aruncă, setări gata făcute pentru un repetor obișnuit și unul aglomerat, fiecare comandă de filtrare cu valoarea ei implicită și cum vezi ce a aruncat.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '2bf23d24'
  seeded: '2026-10-26'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['0625daa2', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', 'ffc3f3a0', '3fa1bb28', '09511608']
---

Un repetor (un nod care transmite mesajele mai departe) repetă tot ce aude.
Pe un mesh aglomerat, asta include și gunoi. Un bot postează în fiecare
minut. Un nod își trimite anunțul, salutul prin care îl găsesc ceilalți, din
nou la fiecare câteva minute. Sosesc mesaje care au străbătut jumătate de
țară. Fiecare repetare consumă timp de emisie al tuturor din jurul tău.
Filtrul de pachete îi permite repetorului tău să arunce acest trafic în loc
să îl transmită mai departe.

{{< callout type="warning" >}}
Filtrul de pachete face parte din **firmware-ul de repetor DMC**, varianta
de repetor de la [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore).
MeshCore standard nu are filtru de pachete; are `region denyf *` și
`set flood.max.unscoped`, descrise pe pagina
[Comenzi CLI](/guides/cli/). Acest ghid urmărește build-ul de dezvoltare
1.18.0 `ecfb2d4` din 19 octombrie 2026. Build-ul stabil 1.17.1 are doar
filtrele pentru salturi, rată, canal, hash și pachete defecte. Nu are nici
mod de test (dry-run).
{{< /callout >}}

## Ce face filtrul {#what}

Filtrul se uită doar la pachetele pe care repetorul tău le transmite mai
departe prin flood (le trimite fiecărui nod din rază). Nu atinge niciodată ce
trimite repetorul tău însuși, nici pachetele care urmează o rută cunoscută
către un singur nod. Mesajele directe și cererile către și de la contactele
tale trec și ele. Poate arunca:

- pachete care au trecut deja prin atâtea repetoare (salturi) câte permiți,
  pe tip de pachet;
- mai multe pachete de un tip decât permiți pe minut;
- un anunț de la un nod care a trimis deja un anunț în ultimele ore;
- mesaje pe un canal pe care îl blochezi;
- tot ce a venit printr-un repetor pe care îl blochezi;
- mesaje de grup de la un expeditor sau cu un anumit cuvânt, sau doar o parte
  din ele;
- mesaje de grup defecte sau mai vechi decât permiți.

Filtrul este **oprit** până îl activezi tu. Îl configurezi prin comenzi.
Tastează-le prin USB în [consola serială](/firmware/console/) de pe acest
site. Sau trimite-le din aplicația MeshCore, ca în
[ghidul pentru repetor](/repeater-guide/#config).

## Obține firmware-ul {#firmware}

Flash-uiește **DutchMeshCore Repeater** din flasher-ul din
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Firmware-ul de
observator din [MQTT pe observatorul tău](/guides/mqtt/) are același filtru.

## Testează mai întâi {#dryrun}

În modul de test (dry-run), filtrul numără fiecare pachet pe care l-ar
arunca, dar îl transmite totuși mai departe. Calibrează o setare în acest fel
înainte să arunce ceva:

```text
filter on
filter dryrun on
```

Cât timp modul de test este activ, linia de stare a comenzii `filter` se
termină cu `(dry-run)`. Contoarele arată ce ar fi aruncat. Lasă-l să ruleze
o zi, apoi uită-te la ele (vezi [Ce a aruncat](#stats)). Când cifrele arată
bine, pune-l să aplice filtrul:

```text
filter dryrun off
```

## Configurații recomandate {#configs}

### Un repetor obișnuit {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Mesajele de grup trec până la 20 pe minut, mesajele directe până la 5 pe
minut, iar mesajele de grup defecte sunt aruncate. Configurația obișnuită
din firmware permite 20 de mesaje directe pe minut. Această pagină preia
valoarea 5 pe care o recomandă firmware-ul după un flood de mesaje directe
din iulie 2026.

### Un repetor aglomerat {#busy}

Pentru un repetor amplasat sus, care aude o regiune întreagă, sau unul care
primește flood:

```text
filter on
filter malformed on
filter rate 05 10 60
filter rate 02 5 60
filter rate 04 5 60
filter advert 24
filter hops 05 16
filter hops 02 16
filter hops 04 8
```

Asta înjumătățește mesajele de grup și anunțurile și lasă anunțul fiecărui
nod să treacă o dată pe zi. Aruncă mesajele care au trecut deja prin 16
repetoare. După o repornire, fiecare nod primește un anunț prin filtru.
Documentația firmware-ului setează aici și `filter hash 2`; această pagină îl
omite (vezi [Toate setările](#settings) pentru motiv).

### Blochează un canal zgomotos {#channel}

```text
filter channel add #bot
```

Repetorul tău aude canalul în continuare. Nu îl mai transmite însă altor
repetoare și companioni (nodurile de pe care oamenii trimit mesaje). Până la
16 canale.

### Încetinește un expeditor {#sender}

Un bot care postează prea des pe un canal pe care vrei să îl păstrezi:

```text
filter watch add #test
filter sender add Bob 60
```

Mesajele lui Bob de pe canalul Public și de pe `#test` trec acum o dată pe
minut; restul sunt aruncate. Filtrul compară numele din mesaj, așa că un
expeditor care își schimbă numele trece de el.

### Blochează un repetor din amonte {#path}

Când gunoiul vine printr-un singur repetor, blochează-i prefixul: prima parte
a ID-ului său, în hexazecimal (hex).

```text
filter path add a1b2
```

Un prefix scurt precum `a1` blochează și orice alt repetor al cărui ID
începe cu `a1`. Folosește cel mai lung prefix pe care îl poți. Până la 8
prefixe.

## Toate setările {#settings}

Tipurile de pachete se identifică prin număr. Pe repetor, `filter types`
arată aceleași numere cu numele din firmware, precum `TXT_MSG` și `GRP_TXT`:

| Număr | Tip | Număr | Tip |
| --- | --- | --- | --- |
| `00` | cerere | `06` | date de grup |
| `01` | răspuns | `07` | cerere anonimă |
| `02` | mesaj direct | `08` | rută |
| `03` | confirmare | `09` | trace |
| `04` | anunț | `10` | multipart |
| `05` | mesaj de grup | `11` | control |

| Comandă | Ce face | Valoare inițială |
| --- | --- | --- |
| `filter on` / `filter off` | Pornește sau oprește filtrul. | oprit |
| `filter dryrun on` / `off` | Numără ce ar arunca, dar transmite totul mai departe. | oprit |
| `filter hops <type> <max>` | Aruncă un tip care a trecut deja prin atâtea repetoare, 0 până la 64. | 32 pentru mesaje de grup, 8 pentru restul |
| `filter rate <type> <limit> <secs> [soft]` | Lasă să treacă cel mult `limit` pachete de un tip la fiecare `secs` secunde. Cu `soft`, trecerea scade treptat de la `soft` la `limit`. `0` oprește limita. | 20 la 60 s pentru mesaje directe și de grup, 10 pentru anunțuri, 5 pentru restul |
| `filter advert <hours>` | Lasă anunțul fiecărui nod să treacă o dată la atâtea ore, până la 720. | 0 (oprit) |
| `filter channel add <#name>` | Nu mai transmite un canal mai departe. | niciunul |
| `filter path add <hex>` | Aruncă tot ce a venit printr-un repetor cu acest prefix, 2 până la 8 cifre hex. | niciunul |
| `filter sender add <name> [secs] [prob]` | Aruncă mesajele de grup de la un expeditor, pe Public și pe canalele urmărite. `Bot*` se potrivește cu orice nume care începe cu Bot. | niciunul |
| `filter text add <word> [secs] [prob]` | Aruncă mesajele de grup care conțin un cuvânt, pe Public și pe canalele urmărite. `^word` se potrivește doar la început. | niciunul |
| `filter watch add <#name>` | Lasă regulile de expeditor și text să citească și acest canal, până la 4. Public este citit întotdeauna. | Public |
| `filter malformed on` / `off` | Aruncă mesajele de pe Public care sunt goale, defecte sau datate cu peste o săptămână diferență (verificarea datei așteaptă până se setează ceasul). | oprit |
| `filter age <minutes>` / `off` | Aruncă mesajele de grup mai vechi de atât, pe Public și pe canalele urmărite, 1 până la 10080. | oprit |
| `filter hash <bytes>` | Aruncă pachetele cu un ID de rută mai scurt de atât, 1 până la 3. | 1 |
| `filter reset` | Readuce fiecare setare la valoarea implicită. | |

Fiecare `add` are un `remove` și un `list`, de exemplu
`filter channel remove #bot`. În regulile de expeditor și text, `secs` lasă
să treacă un mesaj la atâtea secunde. `prob` aplică regula doar acelei
proporții din potriviri, 1 până la 100. Până la 8 reguli de expeditor și 8
reguli de text. Numele și cuvintele țin cont de majuscule; un nume are cel
mult 15 caractere, un cuvânt cel mult 23.

Două setări aruncă mai mult decât te-ai aștepta:

- `filter hash 2` aruncă aproape tot traficul. Nodurile trimit implicit ID-uri
  de rută de 1 octet.
- `filter age` se bazează pe ceasul repetorului tău. Setează-l cu
  `clock sync` din aplicație, verifică-l cu `clock` și începe generos:
  `filter age 60`.

Fiecare setare se păstrează după o repornire.

## Ce a aruncat {#stats}

`filter` arată totalurile pe fiecare motiv:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` arată detaliile pentru o singură setare. Subiectele
sunt `hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`,
`sender`, `text` și `age`. `filter stats top` arată primul octet al ID-urilor
nodurilor din spatele celor mai multe aruncări, un indiciu, nu o dovadă.
`filter stats air` arată timpul de emisie pe care repetorul tău l-a
economisit netransmițând aceste pachete mai departe.

Contoarele pornesc din nou de la 0 după o repornire și după `clear stats`.
