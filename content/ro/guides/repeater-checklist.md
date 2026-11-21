---
title: Listă de verificare pentru repetor
lead: Verifică-ți repetorul înainte să-l montezi sus. Fiecare rând îți spune ce verifici, comanda care îți arată valoarea și ghidul care o explică.
description: 'O listă de verificare pentru un repetor MeshCore înainte să ajungă pe un acoperiș sau pe un catarg: ce verifici prin USB, cum îl montezi și testul de dinainte să pleci.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Un repetor de pe acoperiș e greu de accesat, așa că verifică-l cât e încă pe
birou. [Ghidul pentru repetor](/repeater-guide/) explică fiecare pas. Valorile,
cum ar fi presetarea și limitele de salturi, le iei din
[setările zonei tale](/guides/settings/). Tastează comenzile prin USB, de
exemplu în [consola serială](/firmware/console/). Lista se bazează pe firmware-ul
MeshCore v1.18.0.

## Înainte să începi {#start}

- [ ] [Hărțile de acoperire](/map/) sau [grupul tău local](/community/) arată
      că zona are nevoie de un repetor. Vezi [Ai nevoie de unul?](/repeater-guide/#need)
- [ ] Proprietarul locului și-a dat acordul, iar tu poți ajunge la repetor
      pentru întreținere.
- [ ] Bateria și panoul sunt dimensionate pentru cea mai grea lună de iarnă.
      Vezi [Dimensionarea alimentării și a panoului solar](/repeater-guide/#power).

## La birou, prin USB {#usb}

- [ ] Placa rulează firmware-ul **Repeater**: `ver` îi arată versiunea. Vezi
      [Configurează-l](/repeater-guide/#config).
- [ ] Pe o placă nRF52, răspunsul la `get bootloader.ver` conține `OTAFIX`.
      Vezi [Actualizează-l prin aer](/repeater-guide/#update).
- [ ] `get radio` arată presetarea zonei tale.
- [ ] `get dutycycle` arată 10. Vezi [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] Valoarea din `get tx`, plus câștigul antenei tale, nu depășește 500 mW e.r.p.
      Vezi [Puterea: e.r.p. și antena ta](/repeater-guide/#erp).
- [ ] Parola de administrator nu mai este `password`.
- [ ] `get guest.password` arată o parolă.
- [ ] `get name` arată numele pe care grupul tău local îl folosește pentru repetoare.
- [ ] `get lat` și `get lon` arată poziția locului.
- [ ] `get owner.info` arată cum te pot contacta ceilalți operatori.
- [ ] `region` arată regiunile zonei tale. `get flood.max.advert` și
      `get flood.max.unscoped` arată limitele ei de salturi. Vezi
      [Limitează traficul](/guides/settings/#traffic).
- [ ] Ai salvat cheia privată din `get prv.key` într-un loc sigur.
- [ ] `clock` arată ora curentă, în UTC.
- [ ] Dacă repetorul e alimentat solar, `powersaving` arată `on`.

## Pe acoperiș {#roof}

- [ ] Antena e montată înainte ca repetorul să primească alimentare.
- [ ] Antena stă verticală în vârful catargului, departe de metal. Vezi
      [Montarea](/guides/antenna/#mounting).
- [ ] Fiecare conector din exterior e etanșat, iar cablul are o buclă de picurare.
- [ ] Carcasa e închisă și are un orificiu de aerisire sau de scurgere. Vezi
      [Hardware](/repeater-guide/#hardware).

## Înainte să pleci {#leave}

- [ ] De la distanță, companionul tău ajunge la repetor în aplicație.
- [ ] Ai trimis `advert`, ca nodurile din tot mesh-ul să afle de repetor.
- [ ] [Grupul tău local](/community/) știe că repetorul funcționează.
