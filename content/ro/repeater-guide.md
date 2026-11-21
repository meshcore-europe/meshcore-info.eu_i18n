---
title: Ghid pentru repetoare
lead: Un repetor pus la înălțime transmite mai departe mesajele pentru toți cei din jur, pe tot cuprinsul unui oraș sau al unei văi. Alege un loc, alimentează-l de la soare, configurează-l și respectă legea.
description: 'Planifică, alimentează, configurează și operează legal un repetor MeshCore în Europa: alegerea locului, dimensionarea sistemului solar, setări CLI, limite de putere și de duty cycle la 868 MHz.'
eyebrow: 868 MHz · până la 500 mW · fără licență
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'd42ee2ac'
  seeded: '2026-11-21'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '824ab38e', '662ea23c', '70faf508', 'b9991666', '69d7162f', 'bf712994', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'cc266810']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', 'bbea9a0c', '2b9fab3b', 'b13d1947', 'c2bad16f', '636edc86', 'c2d6bcd1', '957ae975', '98874949', '96d1ebad', 'dbd9fa1f', 'aa06d32b', '9958aad3', '73642ab6', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '90338c64', '2b1d995b', '992bed82', '62eb1543', '210f1b66', 'e817b1f7', '63f961dc', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', '50af0550', 'dd7c556b', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '7cf2bc81']
---

Mesh-ul se sprijină pe repetoare. Dispozitivele companion, adică radiourile de pe care trimiți mesaje, nu
transmit mesajele mai departe. Fără
repetoare ajungi doar la oamenii aflați în raza ta directă. Un repetor pus în locul
potrivit extinde mesh-ul pentru toți cei din jur. Ghidul urmează firmware-ul MeshCore
v1.18.0.

Înainte să începi, vorbește cu [grupul local](/community/). Membrii lui știu unde
lipsește acoperirea, ce [preset folosește zona ta](/guides/settings/) și cum să denumești repetoarele. Caută pe
[hărțile de acoperire](/map/) repetoarele din apropiere și salută-i pe ceilalți pe
[canalele](/guides/channels/) publice sau locale.

## Ai nevoie de unul? {#need}

Un repetor retransmite fiecare mesaj flood pe care îl aude. Toate repetoarele din
rază împart același timp de emisie. Acolo unde mesh-ul ajunge deja la tine, încă un
repetor adaugă trafic, nu acoperire. Un companion pus la înălțime, la o fereastră
de mansardă sau pe un balcon, poate fi tot ce îți trebuie.

Instalează un repetor acolo unde lipsește acoperirea:

- pe [hărțile de acoperire](/map/) nu vezi niciun repetor lângă tine, sau doar unele pe care
  companionul tău nu le aude;
- grupul tău local spune că zona are nevoie de unul.

## Alege locul {#site}

Înălțimea contează mai mult decât puterea. LoRa pe 868 MHz ajunge cel mai departe în linie
de vedere liberă. Dealurile, clădirile și copacii denși îți iau mult mai multă rază decât
recuperează câțiva miliwați în plus.

- **Alege un loc înalt.** Un acoperiș, un catarg, o clădire înaltă sau un deal acoperă mult mai mult
  decât un pervaz. Ajută chiar și câțiva metri deasupra acoperișurilor din jur.
- **Lasă antena liberă.** Montează-o deasupra marginilor acoperișului, departe de
  metal, jgheaburi și alte antene.
- **Verifică vizibilitatea.** Instrumente precum [HeyWhatsThat](https://www.heywhatsthat.com/)
  arată ce se vede dintr-un loc. Aplicația MeshCore
  [calculează unde poate ajunge un repetor pus acolo](#check-site).
- **Lasă spațiu liber.** O rută radio are nevoie de spațiu liber în jurul liniei directe,
  nu doar de linia în sine. La 868 MHz, acest spațiu are aproximativ 20 m în jurul
  mijlocului unei rute de 5 km. Pe 20 km are aproximativ 40 m.
- **Cere permisiunea.** Obține acordul proprietarului pentru acoperiș sau catarg și stabilește
  cum vei ajunge la repetor pentru întreținere.

### Verifică un amplasament în aplicație {#check-site}

Aplicația MeshCore, versiunea 1.33 sau mai nouă, are aceste instrumente în
meniu, la **Tools**. Funcționează fără un radio conectat.

- **Line of Sight** desenează terenul dintre 2 puncte și spațiul de care semnalul
  are nevoie deasupra lui. Ține apăsat pe 2 puncte de pe hartă sau atinge repetoare.
- **Antenna Coverage** arată pe hartă unde ajunge o antenă amplasată în 1 punct.
  Ține apăsat pe un punct sau atinge un repetor. Adaugă mai multe puncte ca să compari amplasamentele.

Pe calculator, alege **Add Point** din meniul instrumentului și introdu coordonatele.

Ambele instrumente pun inițial antena din locul tău la 5 m, așa că setează
în setările instrumentului înălțimea pe care o plănuiești. Antenna Coverage pune
inițial antena de recepție la 1 m. Fără un radio conectat, Line of Sight folosește
inițial 915 MHz: setează în setările lui frecvența [presetării](/guides/settings/) tale.

Instrumentele calculează pe baza datelor de altitudine și nu îți testează radioul. Verifică
tu copacii și clădirile noi, apoi du un companion la fața locului și vezi ce
repetoare aude.

![Line of Sight în aplicația MeshCore: terenul dintre 2 puncte și spațiul de care semnalul are nevoie deasupra lui](/media/guides/line-of-sight.webp)

![Antenna Coverage în aplicația MeshCore: zona pe care o poate acoperi o antenă de pe un deal, pe hartă](/media/guides/antenna-coverage.webp)

## Hardware {#hardware}

- **Placa.** Alege o placă nRF52 cu consum redus, cum ar fi
  [Heltec T114](/devices/), RAK WisBlock sau SenseCAP Solar Node. Plăcile ESP32
  consumă mai mult (pe pagina de dispozitive au marcajul High), iar asta îngreunează
  funcționarea pe energie solară.
- **Antena.** Folosește o antenă făcută pentru 868 MHz, montată vertical. În
  [ghidul despre antene](/guides/antenna/) găsești tipuri, conectori, cabluri și
  montare. Câștigul antenei intră în limita legală de putere; vezi
  [Limite legale](#legal).
- **Cablul.** Folosește cablu coaxial scurt sau cablu cu pierderi mici. La 868 MHz, câțiva
  metri de cablu subțire pot pierde jumătate din putere.
- **Carcasa.** Ia o cutie etanșă (IP65 sau mai bine) cu presetupă de cablu, un
  orificiu de aerisire sau de scurgere contra condensului și o culoare deschisă sau o protecție contra soarelui.
  Bateriile suferă la căldură și nu se pot încărca sub punctul de îngheț.
- **Trăsnetul.** O antenă pe acoperiș este o țintă. Respectă regulile locale de
  împământare sau monteaz-o acolo unde un trăsnet nu ar ajunge la instalația electrică
  a clădirii.

## Alimentare și dimensionarea sistemului solar {#power}

Un repetor solar trebuie să reziste în cele mai întunecate săptămâni ale iernii. Activează
mai întâi economisirea energiei: după `powersaving on`, repetorul doarme între pachete.
Funcționează pe plăcile nRF52 și pe plăcile ESP32 al căror firmware nu are bridge.
Apoi dimensionează bateria și panoul:

1. **Măsoară consumul.** Conectează repetorul configurat la un wattmetru USB
   timp de o zi. Citește energia consumată în wați-oră (Wh). Traficul din
   zona ta schimbă valoarea, așa că măsoară la fața locului dacă poți.
2. **Adaugă o rezervă.** Calculează capacitatea bateriei pentru cel puțin 5 până la 7 zile
   fără soare util.
3. **Află cât soare ai iarna.** Instrumentul gratuit
   [PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) al UE îți arată, pentru orice
   loc, câtă energie produce un panou în fiecare lună. Folosește luna cu
   cel mai puțin soare.
4. **Dimensionează panoul.** Panoul trebuie să acopere consumul zilnic din cea mai slabă lună,
   cu rezervă pentru pierderile de încărcare.

Un exemplu calculat, cu valori presupuse: un repetor care consumă 1 Wh pe zi
are nevoie de o baterie de cel puțin 7 Wh pentru o săptămână de rezervă, adică circa 2 Ah
de capacitate utilizabilă la 3.7 V. Dacă PVGIS arată că un panou de 1 W din locul tău dă
0.5 Wh pe zi în decembrie, îți trebuie un panou de cel puțin 2 W. Cu 3 până la 5 W
ai rezervă pentru nori, zăpadă și îmbătrânire.

## Configurarea {#config}

**Flash.** Deschide [web flasher-ul](https://flasher.meshcore.io) și alege
firmware-ul **Repeater** pentru placa ta. Pașii pentru flash sunt în
[Primii pași](/get-started/#flash).

**Configurează prin USB.** Cu repetorul încă legat la calculator,
deschide [config.meshcore.io](https://config.meshcore.io) sau consola din flasher.
Poți folosi și orice terminal serial la 115200 baud. Cele mai
importante comenzi:

| Ce | Comandă |
|---|---|
| Schimbă parola de administrator | `password <new password>` |
| Parola pentru vizitatori, care îi pot citi starea | `set guest.password <password>` |
| Dă-i un nume | `set name <name>` |
| Presetarea radio: frecvență, lățime de bandă, SF, CR (repornește ca să se aplice) | `set radio 869.618,62.5,8,8` |
| Limita ciclului de lucru, în procente | `set dutycycle 10` |
| Puterea de emisie a cipului radio, în dBm | `set tx <dBm>` |
| Poziția, ca să apară pe hărți | `set lat <degrees>` și `set lon <degrees>` |
| Date de contact pentru alți operatori | `set owner.info <text>` |
| Numărul de ore dintre anunțurile flood, cele pe care le aude tot mesh-ul | `set flood.advert.interval <hours>` |
| Anunță-l acum | `advert` |
| Repornire | `reboot` |

Parola implicită de admin este `password`. Oricine se autentifică cu ea
devine admin. Schimb-o înainte ca repetorul să intre în emisie.

La început, parola pentru vizitatori este goală. Atunci oricine se poate conecta ca vizitator fără
parolă și poate citi starea repetorului și vecinii lui. Fiecare cerere înseamnă
trafic în mesh. Pune o parolă pentru vizitatori și dă-o celor care au nevoie
de ea.

**Alege un nume.** Denumește-l așa cum își denumește grupul tău local repetoarele.
Dacă nu ai un grup, pune în nume țara, localitatea și un nume scurt, de exemplu
`DE-63477-MUF1`. Așa, ceilalți operatori văd unde se află repetorul. Un nume
poate avea cel mult 31 de bytes, iar 23 încap într-un anunț care conține și o poziție.

Exemplul `set radio` de mai sus este EU/UK (Narrow). Folosește în schimb valorile presetului
din zona ta: în [Setări recomandate](/guides/settings/) le găsești
pe țări.

**Setează ceasul.** Fără un modul de ceas (RTC), un repetor pierde ora la
fiecare pană de curent și repornește cu data din mai 2024. Cât timp funcționează, ceasul lui
se și decalează: o ia înainte sau rămâne în urmă. Așa că setează ceasul din când în când:
conectează-te de la distanță din aplicație și folosește `clock sync` sau setează ora prin USB. Cu
un modul RTC ai rar nevoie de asta: el păstrează ora și în timpul penelor de curent și
se decalează mult mai puțin. Firmware-ul găsește singur un modul DS3231, RV3028, PCF8563
sau RX8130.

**O placă cu GPS** le setează pe amândouă în locul tău. După `gps on`, repetorul preia
ora de la GPS la fiecare 30 de minute, iar `gps setloc` îi copiază poziția în
`lat` și `lon`. GPS-ul consumă energie tot timpul cât e pornit. La o instalare solară, rulează
`gps setloc` o dată la fața locului și oprește-l cu `gps off`. După aceea, ceasul
are iar nevoie de `clock sync`.

**Administrează-l de la distanță.** După ce repetorul e în mesh, autentifică-te din aplicația MeshCore
cu parola de admin. Acolo îi citești starea și folosești aceleași comenzi
prin radio. Unele comenzi merg doar prin USB, cum ar fi `set freq` și resetarea
din fabrică `erase`.

**Păstrează-i identitatea.** Înainte de un erase, tastează `get prv.key` prin USB și păstrează
cheia privată afișată într-un loc sigur. După erase, dai `set prv.key <key>`
și un `reboot`, iar repetorul își recapătă vechea identitate. Astfel, nodurile care îl
cunosc îl găsesc sub același prefix.

Lista completă de comenzi este în
[referința CLI MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Actualizează-l prin aer {#update}

După ce repetorul e sus, îl actualizezi de la sol. Autentifică-te din
aplicația MeshCore cu parola de admin, deschide-i linia de comandă și tastează
`start ota`. Ce urmează depinde de placă. Alte plăci răspund `Error`,
iar pe acestea le actualizezi prin USB.

**Plăcile nRF52**, cum ar fi RAK, Heltec T114, Seeed XIAO și SenseCAP Solar:

1. Descarcă din [web flasher](https://flasher.meshcore.io) fișierul **ZIP** cu noul firmware
   pentru placa ta.
2. Tastează `start ota`. Repetorul răspunde `OK` și apare prin Bluetooth
   ca `<board>_OTA`, de exemplu `RAK4631_OTA`.
3. Deschide pe telefon aplicația nRF Device Firmware Update, alege fișierul ZIP și
   repetorul, apoi încarcă. Durează câteva minute.

Instalează [bootloader-ul OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
pe o placă nRF52 înainte s-o montezi sus. Cu bootloader-ul original, o actualizare
eșuată se repară doar prin USB. Cu OTAFIX, placa revine în modul de
actualizare și încerci din nou prin Bluetooth. `get bootloader.ver` arată
ce bootloader are o placă: cu OTAFIX, răspunsul conține `OTAFIX`.

După o actualizare, `ver` arată versiunea de firmware care rulează acum.

**Plăcile ESP32**, cum ar fi Heltec V3 și V4:

1. Descarcă din web flasher fișierul `.bin` **non-merged** pentru placa ta:
   cel fără „merged” în nume.
2. Tastează `start ota`. Repetorul deschide o rețea WiFi numită `MeshCore-OTA`
   și răspunde cu adresa paginii de încărcare.
3. În raza WiFi, conectează telefonul sau laptopul la acea rețea, deschide
   adresa și încarcă fișierul.

## Limite legale {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Preseturile europene MeshCore se află în sub-banda **869.40-869.65 MHz**. În
UE, Regatul Unit, Elveția și Norvegia, dispozitivele cu rază scurtă de acțiune o pot folosi fără
licență, în aceste limite:

- cel mult **500 mW e.r.p.** putere radiată;
- cel mult **10% duty cycle**: nu mai mult de 360 de secunde de emisie în
  orice oră, pentru fiecare dispozitiv. Alternativ, un dispozitiv poate folosi listen-before-talk
  cu adaptive frequency agility, așa cum le definește ETSI EN 300 220-2;
- tot semnalul, cu o lățime de cel mult 250 kHz, trebuie să rămână în sub-bandă.

Banda este partajată: nu ai voie să perturbi serviciile licențiate, iar alții te pot
perturba pe tine.
Radioul trebuie să aibă marcaj CE (în Marea Britanie, CE sau UKCA).
{{< /callout >}}

Surse: [Recomandarea CEPT ERC 70-03](https://docdb.cept.org/document/845),
Anexa 1, banda h1.7;
[Decizia Comisiei 2006/771/CE](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
și modificările ei;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
banda O.

### Puterea: e.r.p. și antena ta {#erp}

Limita se aplică puterii *radiate*, măsurate față de o antenă dipol simplă
(e.r.p.). Câștigul antenei se adună, pierderile din cablu se scad. Producătorii indică
câștigul antenei în dBi, adică cu 2.15 dB mai mult decât același câștig în dBd
(raportat la un dipol). Ține această sumă la cel mult 27 dBm (500 mW):

> putere de emisie (dBm) + câștigul antenei (dBi) − pierderi în cablu (dB) − 2.15 ≤ 27

- O placă ce emite 22 dBm într-o antenă de 5 dBi printr-un cablu cu 1 dB pierderi:
  22 + 5 − 1 − 2.15 = 23.85 dBm, circa 240 mW e.r.p. În limită.
- O placă cu amplificator de 30 dBm (1 W) într-o antenă de 3 dBi:
  30 + 3 − 2.15 = 30.85 dBm, circa 1.2 W e.r.p. Peste limită: scade
  puterea de emisie.

`set tx` setează puterea de ieșire a cipului LoRa, în dBm. Cipul SX1262 ajunge
cel mult la 22 dBm, iar firmware-ul nu verifică valoarea introdusă. Plăcile cu
amplificator suplimentar, cum ar fi Heltec V4 sau Station G2, emit mult mai mult decât
valoarea setată. Verifică tabelul producătorului înainte s-o setezi și
începe cu o valoare mică.

### Duty cycle {#duty-cycle}

Un repetor emite pentru toți cei din jur, așa că își consumă timpul de emisie mai repede
decât un companion. Limitatorul de duty cycle din MeshCore are implicit 50%, mai mult
decât permite această bandă. Setează-l la 10% pe fiecare repetor:

```text
set dutycycle 10
```

### Precizia frecvenței {#frequency}

Canalul EU/UK (Narrow), 869.618 MHz cu lățime de bandă de 62.5 kHz, ajunge până
la 869.649 MHz: la mai puțin de 1 kHz sub capătul de sus al sub-benzii. Semnalul
trebuie să rămână în bandă la orice temperatură. Pentru asta e nevoie de un
cristal compensat termic (TCXO). Aproape toate plăcile actuale au unul. Plăcile
mai vechi fără TCXO, cum ar fi Heltec V2, deviază prea mult ca să funcționeze fiabil
la 62.5 kHz.

### Note pe țări {#countries}

- **Statele membre UE** trebuie să pună această sub-bandă la dispoziție în aceste condiții
  (Decizia 2006/771/CE, articolul 3).
- **Regatul Unit:** aceleași limite, în Ofcom
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Elveția și Liechtenstein:** aceleași limite, în OFCOM
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norvegia:** aceleași limite, în
  [regulamentul privind autorizațiile generale](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Aceste note nu sunt consultanță juridică. Regulile se schimbă. Dacă ai dubii, întreabă
autoritatea națională de reglementare.

## Listă de verificare pentru instalare {#checklist}

Înainte să urci repetorul sus, parcurge
[lista de verificare pentru repetoare](/guides/repeater-checklist/). Lista arată fiecare lucru de
verificat, împreună cu comanda care îl afișează.
