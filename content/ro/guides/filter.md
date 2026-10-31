---
title: Filtru de pachete
lead: 'Nu lăsa repetorul tău să transmită mai departe gunoiul: flood-uri de departe, un bot care nu se oprește, un canal zgomotos. Încearcă întâi o setare, apoi activeaz-o.'
description: 'Filtrul de pachete din firmware-ul de repetor DMC: ce aruncă, setări gata făcute pentru un repetor obișnuit și unul aglomerat, fiecare comandă de filtru cu valoarea ei implicită și cum vezi ce a aruncat.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-10-31'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Un repetor (un nod care transmite mesajele mai departe) repetă tot ce aude.
Pe un mesh aglomerat, asta include și gunoi. Un bot postează în fiecare minut.
Un nod își trimite anunțul (salutul prin care ceilalți îl găsesc) din nou la
câteva minute. Sosesc mesaje care au străbătut jumătate de țară. Fiecare
repetare consumă timp de emisie de la toți cei din jurul tău. Cu filtrul de
pachete, repetorul tău aruncă acest trafic în loc să-l transmită mai departe.
Ca să afli întâi ce inundă mesh-ul tău și ce mai ajută în afară de filtru,
citește [Fă mesh-ul rezistent](/guides/resilient/).

{{< callout type="warning" >}}
Filtrul de pachete face parte din **firmware-ul de repetor DMC**, varianta de
repetor a [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore).
MeshCore standard nu are filtru de pachete. Are în schimb `region denyf *` și
`set flood.max.unscoped`, descrise pe pagina [Comenzi CLI](/guides/cli/).
Ghidul acesta urmează versiunea dev 1.18.0 `ecfb2d4` din 19 octombrie 2026.
Versiunea stabilă 1.17.1 are doar filtrele de salturi, rată, canal, hash și
pachete defecte. Nu are nici modul dry-run.
{{< /callout >}}

## Ce face filtrul {#what}

Filtrul se uită doar la pachetele pe care repetorul tău le transmite prin flood
(adică le trimite tuturor nodurilor din rază). Nu atinge niciodată ce trimite
repetorul tău însuși și nici pachetele care urmează o rută cunoscută spre un
singur nod. Trec și mesajele directe și cererile de la și spre contactele tale.
Filtrul poate arunca:

- pachete care au trecut deja prin atâtea repetoare (salturi) câte permiți tu,
  pe tip de pachet;
- mai multe pachete de un tip decât permiți tu pe minut;
- un anunț de la un nod care s-a anunțat deja în ultimele ore;
- mesaje de pe un canal pe care îl blochezi;
- tot ce a venit printr-un repetor pe care îl blochezi;
- mesaje de grup de la un anumit expeditor sau cu un anumit cuvânt, ori doar o
  parte din ele;
- mesaje de grup defecte sau mai vechi decât permiți tu.

Filtrul este **oprit** până îl pornești tu. Îl configurezi cu comenzi. Le
tastezi prin USB în [consola serială](/firmware/console/) de pe acest site.
Sau le trimiți din aplicația MeshCore, ca în
[ghidul pentru repetor](/repeater-guide/#config).

## Obține firmware-ul {#firmware}

Instalează **DutchMeshCore Repeater** cu flasher-ul din
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Firmware-ul de
observator din [MQTT pe observatorul tău](/guides/mqtt/) are același filtru.

## Încearcă-l întâi {#dryrun}

În modul dry-run, filtrul numără fiecare pachet pe care l-ar arunca, dar îl
transmite totuși mai departe. Așa calibrezi o setare înainte să arunce ceva:

```text
filter on
filter dryrun on
```

Cât timp dry-run e pornit, linia de stare a comenzii `filter` se termină cu
`(dry-run)`. Numerele arată ce ar fi aruncat filtrul. Lasă-l să ruleze o zi,
apoi uită-te la ele (vezi [Ce a aruncat](#stats)). Când numerele par corecte,
activează-l de-a binelea:

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

Trec până la 20 de mesaje de grup pe minut și până la 5 mesaje directe pe
minut. Mesajele de grup defecte sunt aruncate. Configurația obișnuită a
firmware-ului permite 20 de mesaje directe pe minut. Pagina aceasta folosește
valoarea 5 recomandată de firmware de la un flood de mesaje directe din iulie
2026 încoace.

### Un repetor aglomerat {#busy}

Pentru un repetor amplasat sus, care aude o regiune întreagă, sau pentru unul
inundat:

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

Așa reduci la jumătate mesajele de grup și anunțurile. Anunțul fiecărui nod
trece o dată pe zi. Mesajele care au trecut deja prin 16 repetoare sunt
aruncate. După o repornire, fiecare nod trece cu un anunț. Documentația
firmware-ului setează aici și `filter hash 2`. Pagina aceasta o omite (motivul
e în [Toate setările](#settings)).

### Blochează un canal zgomotos {#channel}

```text
filter channel add #bot
```

Repetorul tău aude în continuare canalul. Nu-l mai transmite însă altor
repetoare și companion-uri (nodurile din care oamenii trimit mesaje). Poți
bloca până la 16 canale.

### Încetinește un expeditor {#sender}

Un bot care postează prea des pe un canal pe care vrei să-l păstrezi:

```text
filter watch add #test
filter sender add Bob 60
```

Mesajele lui Bob de pe canalul Public și de pe `#test` trec acum o dată pe
minut. Restul e aruncat. Filtrul compară numele din mesaj, așa că un
expeditor care își schimbă numele trece de el.

### Blochează un repetor din amonte {#path}

Când gunoiul vine printr-un singur repetor, blochează-i prefixul: prima parte
a ID-ului său, în hexazecimal (hex). Ai nevoie de versiunea dev 1.18. Versiunea
1.17.1 nu are filtru de rută.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` arată prefixele pe care le blochezi, iar `filter stats path`
cât a aruncat fiecare. Cu `filter path remove a1b2` îl lași din nou să treacă.
Un prefix scurt ca `a1` blochează și orice alt repetor al cărui ID începe cu
`a1`. Folosește cel mai lung prefix posibil. Poți bloca până la 8 prefixe.

## Toate setările {#settings}

Tipurile de pachete au numere. Pe repetor, `filter types` arată aceleași
numere cu denumirile din firmware, cum ar fi `TXT_MSG` și `GRP_TXT`:

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
| `filter dryrun on` / `off` | Numără pachetele care ar fi aruncate, dar le transmite pe toate mai departe. | oprit |
| `filter hops <type> <max>` | Aruncă un tip care a trecut deja prin atâtea repetoare, între 0 și 64. | 32 pentru mesaje de grup, 8 pentru restul |
| `filter rate <type> <limit> <secs> [soft]` | Lasă să treacă cel mult `limit` pachete de un tip la fiecare `secs`. Cu `soft`, trecerea scade treptat de la `soft` la `limit`. `0` dezactivează limita. | 20 la 60 s pentru mesaje directe și de grup, 10 pentru anunțuri, 5 pentru restul |
| `filter advert <hours>` | Lasă anunțul fiecărui nod să treacă o dată la atâtea ore, până la 720. | 0 (oprit) |
| `filter channel add <#name>` | Nu mai transmite un canal mai departe. | niciunul |
| `filter path add <hex>` | Aruncă tot ce a venit printr-un repetor cu acest prefix, de 2 până la 8 cifre hex. | niciunul |
| `filter sender add <name> [secs] [prob]` | Aruncă mesajele de grup ale unui expeditor, pe Public și pe canalele urmărite. `Bot*` se potrivește cu orice nume care începe cu Bot. | niciuna |
| `filter text add <word> [secs] [prob]` | Aruncă mesajele de grup care conțin un cuvânt, pe Public și pe canalele urmărite. `^word` se potrivește doar la început. | niciuna |
| `filter watch add <#name>` | Regulile de expeditor și de text citesc și acest canal, până la 4 canale. Public e citit mereu. | Public |
| `filter malformed on` / `off` | Aruncă mesajele de pe Public care sunt goale, defecte sau cu data decalată cu peste o săptămână (verificarea datei așteaptă până e setat ceasul). | oprit |
| `filter age <minutes>` / `off` | Aruncă mesajele de grup mai vechi de atât, pe Public și pe canalele urmărite, între 1 și 10080. | oprit |
| `filter hash <bytes>` | Aruncă pachetele cu un ID de rută mai scurt de atât, între 1 și 3. | 1 |
| `filter reset` | Readuce fiecare setare la valoarea implicită. | |

Fiecare `add` are un `remove` și un `list`, de exemplu `filter channel remove #bot`.
În regulile de expeditor și de text, `secs` lasă să treacă un mesaj la atâtea
secunde. `prob` aplică regula doar acelui procent din potriviri, între 1 și
100. Poți avea până la 8 reguli de expeditor și 8 reguli de text. La nume și
cuvinte contează majusculele. Un nume are cel mult 15 caractere, un cuvânt
cel mult 23.

Două setări aruncă mai mult decât te-ai aștepta:

- `filter hash 2` aruncă aproape tot traficul. Nodurile trimit implicit ID-uri
  de rută de 1 byte.
- `filter age` se bazează pe ceasul repetorului tău. Setează-l cu `clock sync`
  din aplicație, verifică-l cu `clock` și începe cu o valoare generoasă:
  `filter age 60`.

Toate setările se păstrează după o repornire.

## Ce a aruncat {#stats}

`filter` arată totalurile pe fiecare motiv:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` arată detaliile pentru o singură setare. Subiectele sunt
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` și `age`. `filter stats top` arată primul byte din ID-urile nodurilor
din spatele celor mai multe pachete aruncate. Multe noduri au același byte.
`filter stats air` arată timpul de emisie economisit de repetorul tău pentru că
nu a transmis aceste pachete mai departe.

Contoarele pornesc din nou de la 0 după o repornire și după `clear stats`.
