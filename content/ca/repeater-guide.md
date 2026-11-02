---
title: Guia de repetidors
lead: Un repetidor col·locat ben alt retransmet els missatges per a tothom del voltant, per tota una població o una vall. Tria un emplaçament, alimenta'l amb energia solar, configura'l i respecta la llei.
description: 'Planifica, alimenta, configura i fes servir legalment un repetidor MeshCore a Europa: emplaçament, càlcul solar, ordres CLI, límits de potència i de cicle de treball a 868 MHz.'
eyebrow: 868 MHz · fins a 500 mW · sense llicència
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-11-02'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Els repetidors sostenen la malla. Els companions, les ràdios amb què envies missatges, no
retransmeten missatges. Per tant, sense
repetidors només arribes a la gent que tens a l'abast directe. Un repetidor ben situat
amplia la malla per a tothom del voltant. Aquesta guia segueix el firmware
MeshCore v1.18.0.

Abans de començar, parla amb el teu [grup local](/community/). El grup sap on
falta cobertura, [quin preset es fa servir a la teva zona](/guides/settings/) i com es posa nom als repetidors. Mira els
[mapes de cobertura](/map/) per trobar repetidors a prop teu, i saluda als
[canals](/guides/channels/) públics o locals.

## El necessites? {#need}

Un repetidor retransmet cada missatge flood que capta, i tots els repetidors a
l'abast comparteixen el mateix temps d'emissió. Si la malla ja t'arriba, un repetidor
més afegeix trànsit, no cobertura. Potser en tens prou amb un companion col·locat
ben alt, a la finestra de les golfes o en un balcó.

Instal·la un repetidor on falti cobertura:

- els [mapes de cobertura](/map/) no mostren cap repetidor a prop teu, o només
  n'hi ha que el teu companion no capta;
- el teu grup local diu que la zona en necessita un.

## Tria un emplaçament {#site}

L'alçada val més que la potència. A 868 MHz, LoRa arriba més lluny amb una línia de
visió lliure. Els turons, els edificis i els arbres densos et fan perdre molt més abast
del que recuperes amb uns quants mil·liwatts de més.

- **Puja ben amunt.** Un terrat, un pal, un edifici alt o un turó cobreixen molt més
  que l'ampit d'una finestra. Fins i tot uns quants metres per sobre dels terrats del voltant ajuden.
- **Deixa l'antena ben lliure.** Munta-la per sobre de les vores del terrat, lluny
  del metall, de les canals i d'altres antenes.
- **Comprova què es veu.** Eines com [HeyWhatsThat](https://www.heywhatsthat.com/)
  mostren què es veu des d'un lloc. Si veus un punt, un repetidor
  situat allà és al teu abast.
- **Deixa espai lliure.** Un trajecte de ràdio necessita cert espai lliure al voltant de la línia
  directa, no només la línia. En distàncies llargues, el tram central del trajecte
  ha de passar uns quants metres per sobre dels obstacles.
- **Demana permís.** Obtén el consentiment del propietari del terrat o del pal, i
  acorda amb ell com accediràs al repetidor per fer-ne el manteniment.

## Maquinari {#hardware}

- **Placa.** Tria una placa nRF52 de baix consum, com la
  [Heltec T114](/devices/), la RAK WisBlock o la SenseCAP Solar Node. Les plaques ESP32
  consumeixen més (la pàgina de dispositius les marca com a High), i per això costa
  fer-les funcionar amb energia solar.
- **Antena.** Fes servir una antena feta per a 868 MHz, muntada en vertical. La
  [guia d'antenes](/guides/antenna/) explica els tipus, els connectors, el cable i
  el muntatge. El guany de l'antena compta per al límit legal de potència: consulta
  [Límits legals](#legal).
- **Cable.** Fes servir un cable coaxial curt, o un cable de baixes pèrdues. A 868 MHz, uns quants
  metres de cable prim et poden fer perdre la meitat de la potència.
- **Caixa.** Una caixa estanca (IP65 o millor) amb premsaestopes, un forat
  de ventilació o de drenatge contra la condensació, i un color clar o una protecció contra el sol.
  Les bateries pateixen amb la calor i no es poden carregar per sota de zero graus.
- **Llamps.** Una antena en un terrat és un blanc per als llamps. Segueix les normes locals de
  presa de terra, o munta-la on un llamp no arribi al cablejat de
  l'edifici.

## Alimentació i càlcul solar {#power}

Un repetidor solar ha d'aguantar les setmanes més fosques de l'hivern. Dimensiona'l
per a aquestes setmanes:

1. **Mesura el consum.** Connecta el repetidor ja configurat a un mesurador de potència USB
   durant un dia. Llegeix l'energia consumida en watts hora (Wh). El trànsit de
   la teva zona fa variar aquesta xifra, així que mesura-la al lloc si pots.
2. **Afegeix una reserva.** Preveu una capacitat de bateria per a almenys 5 a 7 dies
   sense sol útil.
3. **Esbrina quant sol tens a l'hivern.** L'eina gratuïta
   [PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) de la UE mostra, per a qualsevol
   lloc, quanta energia produeix un panell cada mes. Agafa el mes amb
   menys sol.
4. **Dimensiona el panell.** El panell ha de compensar el consum de cada dia del pitjor
   mes, amb marge per a les pèrdues de càrrega.

Un exemple de càlcul, amb xifres suposades: un repetidor que consumeix 1 Wh al dia
necessita una bateria d'almenys 7 Wh per tenir una setmana de reserva, uns 2 Ah de
capacitat útil a 3.7 V. Si PVGIS indica que un panell d'1 W al teu emplaçament dona
0.5 Wh al dia al desembre, necessites un panell d'almenys 2 W, i amb un de 3 a 5 W
tens marge per als núvols, la neu i l'envelliment.

## Configura'l {#config}

**Flasheja'l.** Fes servir el [flasher web](https://flasher.meshcore.io) i tria el
firmware **Repeater** per a la teva placa. Consulta
[Primers passos](/get-started/#flash) per veure com es flasheja.

**Configura'l per USB.** Amb el repetidor encara connectat a l'ordinador,
obre [config.meshcore.io](https://config.meshcore.io) o la consola del flasher.
També pots fer servir qualsevol terminal sèrie a 115200 baud. Les ordres
més importants:

| Què | Ordre |
|---|---|
| Canviar la contrasenya d'administrador | `password <new password>` |
| Posar-li nom | `set name <name>` |
| Preset de ràdio: freqüència, amplada de banda, SF, CR (reinicia per aplicar-lo) | `set radio 869.618,62.5,8,8` |
| Límit del cicle de treball, en percentatge | `set dutycycle 10` |
| Potència de transmissió del xip de ràdio, en dBm | `set tx <dBm>` |
| Posició, perquè surti als mapes | `set lat <degrees>` i `set lon <degrees>` |
| Dades de contacte per a altres operadors | `set owner.info <text>` |
| Hores entre anuncis flood, els que rep tota la malla | `set flood.advert.interval <hours>` |
| Anunciar-lo ara | `advert` |
| Reiniciar | `reboot` |

La contrasenya d'administrador per defecte és `password`, i qui hi entri amb aquesta contrasenya
es converteix en administrador. Canvia-la abans que el repetidor comenci a emetre.

L'exemple de `set radio` d'aquí dalt és EU/UK (Narrow). En lloc d'aquests, fes servir els valors del preset
de la teva zona: [Configuració recomanada](/guides/settings/) els indica
per països.

**Posa el rellotge en hora.** Sense un mòdul de rellotge (RTC), un repetidor perd l'hora a
cada tall de corrent i torna a arrencar amb la data de maig de 2024. Mentre funciona, el rellotge també
es desvia: s'avança o s'endarrereix cada cop més. Per això has de posar-lo en hora de tant en tant: entra
a distància des de l'app i fes servir `clock sync`, o ajusta l'hora per USB. Amb
un mòdul RTC poques vegades cal: manté l'hora durant els talls de corrent i
es desvia molt menys.

**Gestiona'l a distància.** Quan ja és a la malla, entra des de l'app de MeshCore
amb la contrasenya d'administrador. Allà en consultes l'estat i fas servir les mateixes ordres
per ràdio. Algunes ordres només funcionen per USB, com ara `set freq` i el
restabliment de fàbrica `erase`.

**Conserva'n la identitat.** Abans d'un esborrat, escriu `get prv.key` per USB i desa
en un lloc segur la clau privada que apareix. Després de l'esborrat, amb `set prv.key <key>`
i un `reboot` el repetidor recupera la identitat d'abans, i així els nodes que el coneixen
el troben amb el mateix prefix.

Tens la llista completa d'ordres a la
[referència CLI de MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Actualitza'l sense fil {#update}

Quan el repetidor ja és dalt, l'actualitzes des de terra. Entra des de l'app de
MeshCore amb la contrasenya d'administrador, obre la línia d'ordres i escriu
`start ota`. El que passa després depèn de la placa. Les altres plaques responen `Error`,
i aquestes les actualitzes per USB.

**Plaques nRF52**, com ara RAK, Heltec T114, Seeed XIAO i SenseCAP Solar:

1. Baixa el **ZIP** del firmware nou per a la teva placa des del
   [flasher web](https://flasher.meshcore.io).
2. Escriu `start ota`. El repetidor respon `OK` i apareix per Bluetooth
   com a `<board>_OTA`, per exemple `RAK4631_OTA`.
3. Obre l'app nRF Device Firmware Update al mòbil, tria el ZIP i
   el repetidor, i puja el fitxer. Triga uns quants minuts.

Instal·la el [bootloader OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
en una placa nRF52 abans de pujar-la. Amb el bootloader de sèrie, una actualització
fallida només es pot reparar per USB. Amb OTAFIX, la placa torna al
mode d'actualització, i ho tornes a provar per Bluetooth.

**Plaques ESP32**, com ara la Heltec V3 i la V4:

1. Baixa el `.bin` **non-merged** per a la teva placa des del flasher web:
   el fitxer sense "merged" al nom.
2. Escriu `start ota`. El repetidor obre una xarxa WiFi anomenada `MeshCore-OTA`
   i respon amb l'adreça de la seva pàgina de càrrega.
3. Dins de l'abast del WiFi, connecta el mòbil o el portàtil a aquesta xarxa, obre
   l'adreça i puja el fitxer.

## Límits legals {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Els presets europeus de MeshCore són a la subbanda **869.40-869.65 MHz**. A la
UE, el Regne Unit, Suïssa i Noruega, els dispositius de curt abast la poden fer servir sense
llicència, dins d'aquests límits:

- com a màxim **500 mW e.r.p.** de potència radiada;
- com a màxim un **10% de cicle de treball**: no més de 360 segons de transmissió en
  qualsevol hora, per dispositiu. Com a alternativa, un dispositiu pot fer servir listen-before-talk
  amb adaptive frequency agility, tal com es defineix a ETSI EN 300 220-2;
- tot el senyal, de 250 kHz d'amplada com a màxim, ha de quedar dins de la subbanda.

La banda és compartida: no pots causar interferències a serveis amb llicència, i altres
te'n poden causar a tu.
La ràdio ha de portar el marcatge CE (a la Gran Bretanya, CE o UKCA).
{{< /callout >}}

Fonts: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
annex 1, banda h1.7;
[Decisió 2006/771/CE de la Comissió](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
i les seves modificacions;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
banda O.

### Potència: e.r.p. i la teva antena {#erp}

El límit s'aplica a la potència *radiada*, mesurada respecte a una antena dipol
simple (e.r.p.). El guany de l'antena hi suma i la pèrdua del cable hi resta. Els fabricants indiquen
el guany de l'antena en dBi, que és 2.15 dB més que el mateix guany en dBd
(relatiu a un dipol). Mantén aquesta suma a 27 dBm (500 mW) o per sota:

> potència de transmissió (dBm) + guany de l'antena (dBi) − pèrdua del cable (dB) − 2.15 ≤ 27

- Una placa que transmet 22 dBm a una antena de 5 dBi amb 1 dB de pèrdua de cable:
  22 + 5 − 1 − 2.15 = 23.85 dBm, uns 240 mW e.r.p. Dins del límit.
- Una placa amb un amplificador de 30 dBm (1 W) i una antena de 3 dBi:
  30 + 3 − 2.15 = 30.85 dBm, uns 1.2 W e.r.p. Per sobre del límit: abaixa la
  potència de transmissió.

`set tx` fixa la sortida del xip LoRa, en dBm. El xip SX1262 arriba com a màxim
a 22 dBm. El firmware no comprova el número que hi poses. Les plaques amb un
amplificador addicional, com la Heltec V4 o la Station G2, transmeten molt més del
número que hi poses. Consulta la taula del fabricant abans de posar-lo, i
comença amb un valor baix.

### Cicle de treball {#duty-cycle}

Un repetidor transmet per a tothom del voltant, i per això gasta el temps d'emissió més de pressa
que un companion. El limitador del cicle de treball de MeshCore és del 50% per defecte, per sobre
del que permet aquesta banda. Posa'l al 10% a cada repetidor:

```text
set dutycycle 10
```

### Precisió de la freqüència {#frequency}

El canal EU/UK (Narrow), 869.618 MHz amb 62.5 kHz d'amplada de banda, arriba fins
a 869.649 MHz: menys d'1 kHz per sota del límit superior de la subbanda. El senyal
ha de quedar dins de la banda a qualsevol temperatura. Per aconseguir-ho cal un
cristall compensat en temperatura (TCXO). Gairebé totes les plaques actuals en porten un. Les
plaques antigues que no en tenen, com la Heltec V2, es desvien massa per funcionar de manera fiable
a 62.5 kHz.

### Notes per països {#countries}

- **Els estats membres de la UE** han d'oferir aquesta subbanda en aquestes condicions
  (Decisió 2006/771/CE, article 3).
- **Regne Unit:** els mateixos límits, a la norma
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices) d'Ofcom.
- **Suïssa i Liechtenstein:** els mateixos límits, a la norma
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09) d'OFCOM.
- **Noruega:** els mateixos límits, al
  [reglament d'autoritzacions generals](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Aquestes notes no són assessorament legal. Les normes canvien. Si tens dubtes, consulta
el regulador del teu país.

## Llista de comprovació per a la instal·lació {#checklist}

- [ ] El propietari del lloc hi està d'acord, i pots accedir al repetidor per fer-ne el manteniment.
- [ ] La placa porta el firmware **Repeater**, i has connectat l'antena abans
      de la primera engegada.
- [ ] Has canviat la contrasenya d'administrador.
- [ ] La ràdio coincideix amb [el preset de la teva zona](/guides/settings/) (`get radio`).
- [ ] Has executat `set dutycycle 10`.
- [ ] La potència de transmissió més el guany de l'antena no passen de 500 mW e.r.p.
- [ ] Has posat el nom, la posició i `owner.info`, perquè els altres sàpiguen qui el gestiona.
- [ ] El rellotge està en hora (`clock`).
- [ ] La caixa està segellada, amb un forat de drenatge o de ventilació, i el cable fa un
      bucle de degoteig.
- [ ] La bateria i el panell estan dimensionats per al pitjor mes d'hivern.
- [ ] L'has provat a distància amb l'app abans de marxar del lloc.
- [ ] El teu grup local sap que ja funciona.
