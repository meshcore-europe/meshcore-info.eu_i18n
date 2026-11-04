---
title: Comença
lead: D'una placa nova al teu primer missatge a la mesh. Necessites una placa LoRa, un ordinador amb Chrome o Edge, i un telèfon o un portàtil per a l'app.
description: Flasheja MeshCore des del navegador, vincula l'app, tria el preset de ràdio de la teva zona, envia el primer missatge i entra al canal local.
eyebrow: 6 passos · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0490a311'
  seeded: '2026-11-04'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '5b6d136a', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', '1741ed35', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', 'e90b7859', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', '53276869', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Aquests passos corresponen al firmware MeshCore v1.18.0 i a les eines oficials
d'octubre de 2026. Els noms dels menús de l'app poden variar una mica segons la versió.

## 1. Tria un dispositiu {#device}

Et serveix qualsevol placa de la [pàgina de dispositius](/devices/) que indiqui
companion. Per al teu primer node, tria un *companion*: la ràdio des de la qual
envies missatges. Vincula'l amb el telèfon o el portàtil per Bluetooth o USB.
També en pots triar un amb pantalla i teclat propis, que funciona tot sol.

Agafa la versió de 868 MHz. L'antena inclosa ja fa el fet; a la
[guia d'antenes](/guides/antenna/) veuràs com comprovar-ne una.

La teva placa ara funciona amb Meshtastic? Si hi instal·les MeshCore, el substitueix, i l'un no es comunica amb l'altre.

{{< callout type="warning" >}}
Connecta l'antena abans d'encendre la ràdio. Si una ràdio LoRa transmet sense
antena, se li pot fer malbé el xip.
{{< /callout >}}

## 2. Flasheja el firmware {#flash}

1. Connecta el dispositiu a l'ordinador amb un cable USB de dades.
2. Obre el flasher web a [flasher.meshcore.io](https://flasher.meshcore.io)
   amb Chrome o Edge. Fa servir Web Serial, que els altres navegadors no tenen.
3. Tria el dispositiu i després el firmware **Companion** per a **Bluetooth** (o
   USB, si només el faràs servir amb un cable connectat a l'ordinador).
4. Flasheja'l. Algunes plaques han d'entrar primer en mode d'actualització; el
   flasher t'indica com fer-ho.

Fes servir *erase* només per començar de zero: en esborrar, perds la identitat
del dispositiu i els teus contactes. En les actualitzacions posteriors, flasheja
sense esborrar. Per conservar la identitat en un esborrat, exporta primer
la clau privada del companion des de l'app i importa-la després.

## 3. Instal·la l'app {#app}

L'app oficial de MeshCore està disponible per a Android, iOS, Windows i macOS;
a [meshcore.io](https://meshcore.io) trobaràs l'enllaç a cada versió. També hi ha
una app web a [app.meshcore.nz](https://app.meshcore.nz), que funciona amb Chrome
o Edge en un ordinador.

## 4. Vincula el node {#pair}

Encén el node, obre l'app i connecta-t'hi per Bluetooth. Quan l'app et demani un PIN:

- un node **amb** pantalla mostra un PIN; escriu-lo;
- un node **sense** pantalla fa servir `123456`.

Si la vinculació falla, elimina el dispositiu de la configuració de Bluetooth del
telèfon i torna-ho a provar. Després posa un nom al node. Els altres veuran aquest
nom, així que no hi posis el teu nom complet ni la teva adreça si no vols.

## 5. Tria el preset de ràdio de la teva zona {#preset}

Totes les ràdios d'una zona fan servir la mateixa freqüència i els mateixos
paràmetres; si no, no se senten entre elles. A la configuració de ràdio de
l'app, tria el preset de la teva zona. Fora de les zones següents, a Europa es fa
servir **EU/UK (Narrow)**. Els Països Baixos, Txèquia, Hongria, Eslovàquia, Portugal
i Suïssa tenen el seu, i Limburg, als Països Baixos, en té una variant:

{{< presets >}}

El teu dispositiu no ofereix el preset de la teva zona? Introdueix a mà els 4 valors
de la taula a la configuració de ràdio de l'app: freqüència, amplada de banda,
spreading factor i coding rate. Un node amb altres valors no sent la mesh.

Tens dubtes? El teu [grup local](/community/) sap quin preset es fa servir a
la teva zona. L'app baixa aquesta llista del projecte MeshCore, així que un
preset nou no necessita cap actualització de l'app.

## 6. Saluda {#hello}

1. **Anuncia't.** Envia un *anunci* des de l'app. Un anunci d'«inundació»
   passa pels repetidors (nodes que retransmeten els missatges), i així tothom
   de la malla et pot afegir.
   Els companions no s'anuncien mai automàticament.
2. **Troba altra gent.** Les persones apareixen als teus contactes quan
   t'arriben els seus anuncis. Per defecte, els repetidors envien un anunci
   d'inundació cada 47 hores, així que la teva llista pot trigar 2 dies a omplir-se.
3. **Envia un missatge.** Obre un contacte i escriu. El primer missatge inunda
   la xarxa. El destinatari et retorna la ruta que ha seguit, i els missatges
   següents segueixen aquesta ruta.
4. **Uneix-te a canals.** El canal **Public** ja està configurat. Tot el que hi
   escriguis arriba a tothom de la malla. Afegeix el *canal hashtag* de la teva
   regió (un nom que comença per `#`) escrivint-ne el nom. El teu
   [grup local](/community/) et dirà quins canals estan actius.
   Vols conèixer-los en persona? Mira les [trobades](/meetings/) a prop teu.

## Quan alguna cosa no funciona {#troubleshooting}

**L'app no troba el dispositiu per Bluetooth.**
Probablement has flashejat el companion USB. Torna a flashejar i tria la versió
Bluetooth. Al Heltec V3, la petita antena Bluetooth integrada té poc abast; mantén
el telèfon a prop.

**La vinculació falla una vegada i una altra.**
Elimina el dispositiu de la configuració de Bluetooth del telèfon, reinicia el
Bluetooth i torna a vincular-lo amb el PIN de la pantalla o amb `123456`.

**No apareix ningú als meus contactes.**
Comprova que el preset coincideixi amb el de la teva zona. Envia un advert flood. Si
no tens cap repetidor a l'abast, només sentiràs les ràdios properes; a la
[pàgina del mapa](/map/) pots veure on són els repetidors.

**Un contacte mostra "last seen" de fa dies tot i que està actiu.**
Un dels dos nodes té l'hora malament. Un companion agafa l'hora del telèfon; als
repetidors i als room servers (nodes que desen missatges per a un grup), l'ha
de configurar el propietari.

**Un missatge directe no arriba mai.**
Cal que cadascú tingui l'altra persona com a contacte. Un node descarta el missatge
d'algú que no coneix, sense avisar el remitent. Envia un advert flood i demana a
l'altra persona que també n'enviï un. Comprova a l'app que afegeixi contactes nous
automàticament; només afegeix nodes dins del seu límit de salts.

**Els contactes antics funcionen, però els nous no es connecten mai.**
Un primer missatge s'envia per inundació, i un repetidor només el retransmet si té
la regió del missatge. Els missatges següents segueixen una ruta apresa, i cap
comprovació de regió no els atura. Pregunta al teu [grup local](/community/) quines
regions tenen els repetidors del teu voltant, i comprova
[la configuració de la teva zona](/guides/settings/#traffic).

**L'app ja no es connecta al teu companion.**
Algunes plaques tenen un botó d'usuari, com ara algunes plaques RAK i el Heltec T114.
Mantén-lo premut en els primers 8 segons després que la placa arrenqui. El
companion obre una consola de rescat per USB. A la consola de
[flasher.meshcore.io](https://flasher.meshcore.io), `set pin <pin>` defineix un PIN
de Bluetooth nou i `erase` esborra el dispositiu.

**El flasher no pot obrir el port sèrie a Linux.**
El teu usuari necessita accés al port, per exemple amb
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, o bé formar part del grup `dialout`.

**Una altra cosa.** Les
[FAQ de MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
tracten molts més problemes.
