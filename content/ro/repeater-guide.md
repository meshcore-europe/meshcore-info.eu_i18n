---
title: Ghid pentru repetoare
lead: Un repetor amplasat la înălțime transmite mesajele mai departe pentru toți cei din jur, peste un oraș sau o vale întreagă. Alege un loc, alimentează-l de la soare, configurează-l și respectă legea.
description: 'Planifică, alimentează, configurează și operează legal un repetor MeshCore în Europa: alegerea locului, dimensionarea solară, setări CLI, limite de putere și duty cycle la 868 MHz.'
eyebrow: 868 MHz · până la 500 mW · fără licență
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '4a0fe39f'
  seeded: '2026-10-26'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['1de4a4f7', '766086be', '70faf508', '8bc641aa', '2018aa04', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
---

Repetoarele duc rețeaua mesh. Companionii, adică radiourile de pe care scrii mesaje, nu
transmit mesajele mai departe, așa că fără
repetoare ajungi doar la oamenii aflați în raza directă. Fiecare repetor pe care îl
instalezi extinde rețeaua mesh pentru toți cei din jur. Acest ghid urmează
firmware-ul MeshCore v1.18.0.

Înainte să începi, vorbește cu [grupul tău local](/community/). Ei știu unde
lipsește acoperirea, ce [preset se folosește în zona ta](/guides/settings/) și cum se denumesc repetoarele. Verifică pe
[hărțile de acoperire](/map/) repetoarele din apropierea ta și salută lumea pe
[canalele](/guides/channels/) publice sau locale.

## Alege un loc {#site}

Înălțimea bate puterea. LoRa la 868 MHz se propagă cel mai bine pe o linie
de vizibilitate liberă. Dealurile, clădirile și copacii deși costă mult mai multă rază decât
câștigă câțiva miliwați în plus.

- **Urcă sus.** Un acoperiș, un pilon, o clădire înaltă sau un deal acoperă mult mai mult
  decât un pervaz. Chiar și câțiva metri peste acoperișurile din jur ajută.
- **Ține antena în câmp liber.** Montează-o deasupra marginilor acoperișului, departe de
  metal, jgheaburi și alte antene.
- **Verifică vederea.** Instrumente precum [HeyWhatsThat](https://www.heywhatsthat.com/)
  arată ce se vede dintr-un anumit loc. Dacă vezi un punct, un repetor
  aflat acolo este la îndemână.
- **Lasă spațiu liber.** O cale radio are nevoie de ceva spațiu liber în jurul liniei
  directe, nu doar de linia în sine. Pe distanțe lungi, mijlocul căii
  trebuie să treacă pe deasupra obstacolelor cu câțiva metri.
- **Cere permisiunea.** Obține acordul proprietarului pentru acoperiș sau pilon și stabiliți
  cum vei ajunge la repetor pentru întreținere.

## Hardware {#hardware}

- **Placă.** Alege o placă nRF52 cu consum redus, precum
  [Heltec T114](/devices/), RAK WisBlock sau SenseCAP Solar Node. Plăcile ESP32
  consumă mai mult (pagina dispozitivelor le marchează cu High), ceea ce face
  dificilă alimentarea solară.
- **Antenă.** Folosește o antenă făcută pentru 868 MHz, montată vertical;
  [ghidul pentru antene](/guides/antenna/) acoperă tipurile, conectorii, cablul și
  montajul. Câștigul antenei se adună la limita legală de putere; vezi
  [Limite legale](#legal).
- **Cablu.** Ține cablul coaxial scurt sau folosește cablu cu pierderi mici. La 868 MHz, câțiva
  metri de cablu subțire pot pierde jumătate din putere.
- **Carcasă.** O cutie rezistentă la intemperii (IP65 sau mai bună), cu presetupă, o
  gaură de aerisire sau de scurgere împotriva condensului și o culoare deschisă sau un parasolar.
  Bateriile suferă la căldură și nu pot fi încărcate sub zero grade.
- **Fulgere.** O antenă pe acoperiș este o țintă. Respectă regulile locale de
  împământare sau montează-o acolo unde o lovitură nu ar ajunge la instalația
  electrică a clădirii.

## Alimentare și dimensionare solară {#power}

Un repetor solar trebuie să supraviețuiască celor mai întunecate săptămâni de iarnă. Dimensionează-l
pentru ele:

1. **Măsoară consumul.** Lasă repetorul configurat să funcționeze o zi printr-un
   wattmetru USB. Citește energia consumată în wați-oră (Wh). Traficul din
   zona ta schimbă cifra, așa că măsoară la locul instalării dacă poți.
2. **Adaugă rezervă.** Planifică o capacitate a bateriei pentru cel puțin 5 până la 7 zile
   fără soare util.
3. **Află soarele de iarnă.** Instrumentul gratuit al UE,
   [PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/), arată, pentru orice
   loc, câtă energie produce un panou pe lună. Folosește luna cu cel mai
   puțin soare.
4. **Dimensionează panoul.** Panoul trebuie să înlocuiască zilnic consumul din acea lună
   cea mai slabă, cu marjă pentru pierderile de încărcare.

Un exemplu calculat, cu cifre presupuse: un repetor care consumă 1 Wh pe zi
are nevoie de o baterie de cel puțin 7 Wh pentru o săptămână de rezervă, adică aproximativ 2 Ah
capacitate utilă la 3,7 V. Dacă PVGIS spune că un panou de 1 W la locul tău dă
0,5 Wh pe zi în decembrie, ai nevoie de un panou de cel puțin 2 W, iar 3 până la 5 W
lasă marjă pentru nori, zăpadă și îmbătrânire.

## Configurează-l {#config}

**Scrie firmware-ul.** Folosește [web flasher-ul](https://flasher.meshcore.io) și alege
firmware-ul **Repeater** pentru placa ta. Vezi
[Primii pași](/get-started/#flash) pentru pașii de scriere.

**Configurează prin USB.** Cu repetorul încă conectat la calculator,
deschide [config.meshcore.io](https://config.meshcore.io) sau consola
flasher-ului. Poți folosi și orice terminal serial la 115200 baud. Cele mai
importante comenzi:

| Ce | Comandă |
|---|---|
| Schimbă parola de administrator | `password <new password>` |
| Dă-i un nume | `set name <name>` |
| Preset radio: frecvență, lățime de bandă, SF, CR (repornește pentru a aplica) | `set radio 869.618,62.5,8,8` |
| Limita de duty cycle, în procente | `set dutycycle 10` |
| Puterea de emisie a cipului radio, în dBm | `set tx <dBm>` |
| Poziția, ca să apară pe hărți | `set lat <degrees>` și `set lon <degrees>` |
| Date de contact pentru alți operatori | `set owner.info <text>` |
| Ore între anunțurile flood, cele pe care le aude întreaga rețea mesh | `set flood.advert.interval <hours>` |
| Anunță-l acum | `advert` |
| Repornire | `reboot` |

Parola de administrator implicită este `password`, și oricine se conectează cu ea
devine administrator. Schimbă-o înainte ca repetorul să intre în emisie.

Exemplul `set radio` de mai sus este EU/UK (Narrow). Folosește în loc valorile
presetului din zona ta: [Setări recomandate](/guides/settings/) le listează
pe țări.

**Setează ceasul.** Fără un modul de ceas (RTC), un repetor pierde ora la
fiecare întrerupere de curent și repornește în mai 2024, iar în timpul funcționării ceasul lui deviază.
Conectează-te de la distanță din aplicație și folosește `clock sync`, sau setează ora prin USB.
Un modul RTC este un accesoriu util pentru un repetor: păstrează ora
la întreruperile de curent și deviază mult mai puțin.

**Administrează-l de la distanță.** Odată ce este în rețeaua mesh, conectează-te din aplicația MeshCore
cu parola de administrator. Acolo îi citești starea și folosești aceleași comenzi
prin radio. Unele comenzi merg doar prin USB, precum `set freq` și
resetarea la setările din fabrică `erase`.

Lista completă de comenzi se găsește în
[referința CLI MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Limite legale {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Preseturile europene MeshCore se află în sub-banda **869.40-869.65 MHz**. În
UE, Regatul Unit, Elveția și Norvegia, ea este deschisă dispozitivelor cu rază scurtă fără
licență, în aceste limite:

- cel mult **500 mW e.r.p.** putere radiată;
- cel mult **10% duty cycle**: nu mai mult de 360 de secunde de emisie în
  orice oră, per dispozitiv. Alternativ, un dispozitiv poate folosi listen-before-talk
  cu agilitate adaptivă de frecvență, conform ETSI EN 300 220-2;
- întregul semnal, cu o lățime de cel mult 250 kHz, trebuie să rămână în sub-bandă.

Banda este partajată: nu ai voie să deranjezi serviciile licențiate, iar alții te pot
deranja pe tine.
Radioul trebuie să aibă marcaj CE (în Marea Britanie, CE sau UKCA).
{{< /callout >}}

Surse: [Recomandarea CEPT ERC 70-03](https://docdb.cept.org/document/845),
anexa 1, banda h1.7;
[Decizia Comisiei 2006/771/CE](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
și modificările ei;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
banda O.

### Putere: e.r.p. și antena ta {#erp}

Limita se aplică puterii *radiate*, măsurată față de o antenă dipol
simplă (e.r.p.). Câștigul antenei se adună; pierderea de cablu se scade. Producătorii dau
câștigul antenei în dBi, adică cu 2.15 dB mai mult decât același câștig în dBd
(față de un dipol). Ține această sumă la cel mult 27 dBm (500 mW):

> putere de emisie (dBm) + câștig antenă (dBi) − pierdere cablu (dB) − 2.15 ≤ 27

- O placă care emite 22 dBm într-o antenă de 5 dBi printr-un cablu cu 1 dB pierdere:
  22 + 5 − 1 − 2.15 = 23.85 dBm, adică aproximativ 240 mW e.r.p. În limită.
- O placă cu amplificator de 30 dBm (1 W) într-o antenă de 3 dBi:
  30 + 3 − 2.15 = 30.85 dBm, adică aproximativ 1.2 W e.r.p. Peste limită; scade
  puterea de emisie.

`set tx` setează puterea de ieșire a cipului LoRa, în dBm. Cipul SX1262 în sine
ajunge la cel mult 22 dBm; firmware-ul nu verifică cifra pe care o introduci. Plăcile cu un
amplificator suplimentar, precum Heltec V4 sau Station G2, emit mult mai mult decât
cifra pe care o setezi. Verifică tabelul producătorului înainte să o setezi și
începe cu o valoare mică.

### Duty cycle {#duty-cycle}

Un repetor emite pentru toți cei din jur, așa că își consumă timpul de emisie mai repede
decât un companion. Limitatorul de duty cycle din MeshCore are implicit 50%, adică
peste ce permite această bandă. Setează-l la 10% pe fiecare repetor:

```text
set dutycycle 10
```

### Precizia frecvenței {#frequency}

Canalul EU/UK (Narrow), 869.618 MHz cu lățime de bandă de 62.5 kHz, ajunge până
la 869.649 MHz: cu mai puțin de 1 kHz sub marginea de sus a sub-benzii. Semnalul
trebuie să rămână în bandă la orice temperatură. Pentru asta e nevoie de un
cristal compensat termic (TCXO). Aproape fiecare placă actuală are unul;
plăcile mai vechi fără el, precum Heltec V2, deviază prea mult pentru a funcționa fiabil
la 62.5 kHz.

### Note pe țări {#countries}

- **Statele membre UE** trebuie să pună la dispoziție această sub-bandă în aceste condiții
  (Decizia 2006/771/CE, articolul 3).
- **Regatul Unit:** aceleași limite, în Ofcom
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Elveția și Liechtenstein:** aceleași limite, în OFCOM
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norvegia:** aceleași limite, în
  [regulamentul privind autorizațiile generale](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Aceste note nu sunt consultanță juridică. Regulile se schimbă; dacă ai îndoieli, verifică la
autoritatea națională de reglementare.

## Lista de verificare la instalare {#checklist}

- [ ] Proprietarul locului a fost de acord și poți ajunge la repetor pentru întreținere.
- [ ] Placa rulează firmware-ul **Repeater**, iar antena a fost atașată
      înainte de prima pornire.
- [ ] Parola de administrator este schimbată.
- [ ] Radioul corespunde [presetului din zona ta](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` este setat.
- [ ] Puterea de emisie plus câștigul antenei rămâne în limita de 500 mW e.r.p.
- [ ] Numele, poziția și `owner.info` sunt setate, ca alții să știe cine îl administrează.
- [ ] Ceasul este setat (`clock`).
- [ ] Carcasa este etanșată, cu gaură de scurgere sau aerisire, iar cablul are o
      buclă de picurare.
- [ ] Bateria și panoul sunt dimensionate pentru cea mai slabă lună de iarnă.
- [ ] L-ai testat de la distanță cu aplicația înainte să pleci de la locul instalării.
- [ ] Grupul tău local știe că este în funcțiune.
