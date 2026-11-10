---
title: Lagundu
lead: Boluntarioek idazten, egiaztatzen eta itzultzen dute gida hau. Hona hemen nola lagun dezakezun, GitHub kontuarekin edo gabe.
description: Gehitu zure komunitatea, gailu bat edo proiektu bat, berrikusi itzulpen bat edo hobetu gida bat meshcore-info.eu webgunean.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '1a28f66a'
  seeded: '2026-11-10'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '4b12bb2c', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '8aa01985', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Webgune honetako eduki guztia
[GitHub biltegi publiko batean](https://github.com/meshcore-europe/meshcore-info.eu) dago. Aldaketa txikietarako,
GitHub-eko inprimaki bat dago (issue bat). Handiagoak pull request gisa
bidaltzen dira: fitxategiak aldatzeko proposamen bat, mantentzaile batek berrikusten duena.
Mantentzaile batek aldaketa guztiak egiaztatzen ditu argitaratu aurretik.

Ez duzu GitHub konturik? Esan iezaguzu [Discord-en](https://discord.meshcore-info.eu/):
talde bat falta dela, datu bat okerra dela edo itzulpen bat arraroa dela. Hortik aurrera,
boluntario batek hartuko du bere gain.

## Gehitu zure komunitatea {#community}

Edonor sar daitekeen tokiko MeshCore talde bat daramazu? Bete
[komunitate-inprimakia](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
izena, eremua eta esteka publikoak adierazita. Gehitutakoan, zure taldea
[Tokiko taldeak](/community/) orrian agertuko da hizkuntza guztietan.

## Proposatu gailu bat edo proiektu bat {#device-project}

[Gailuen orriak](/devices/) fabrikatzaileen dokumentazioko zehaztapenak jasotzen ditu, eta
ez du inoiz dendetara estekatzen. Hardwarea proposatzeko, erabili
[gailuen inprimakia](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Iturburu-kode publikoa duen aplikazio, tresna, zubi edo hardware-diseinu bat sortu duzu
MeshCore-rentzat? Gehitu
[proiektuen inprimakiarekin](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Berrikusi itzulpen bat {#translate}

Beste hizkuntzetako orriak itzulpen automatikoak dira hasieran, eta goialdean hala diote.
Itzulpenak beren biltegian daude,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n) izenekoan,
eta, beraz, ez duzu inoiz webgunearen kodea ukitu beharko. Hizkuntza horietakoren bat ondo badakizu,
hobetu dezakezu:

1. Ireki orria eta sakatu "Lagundu itzulpen hau hobetzen". Fitxategia GitHub-en irekiko da,
   eta nabigatzailean bertan editatu ahal izango duzu.
2. Zuzendu testua. Utzi estekak, kodea, zenbakiak eta MeshCore bezalako izenak
   dauden-daudenean.
3. Goialdeko `translation` blokean, aldatu `status: ai` eta jarri `status: human`, eta
   proposatu aldaketa.

Hitz oker bat aurkitu duzu, baina ez duzu zuzentzeko astirik? Jakinarazi
[itzulpen-inprimakiaren](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml) bidez.

## Hobetu gida bat {#guides}

Gidak ingelesez idazten dira lehenik, eta hortik abiatuta itzultzen dira. Zuzenketak
eta gai berriak ongi etorriak dira,
[edukien inprimakiaren](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
bidez edo pull request baten bidez. Datuek iturria behar dute: MeshCore-ren firmwarea edo dokumentazioa,
erregulatzaileren bat, fabrikatzaileren bat edo mantentzaileren bat. Idatzi zeure hitzekin.
Aipu labur bat, iturria adierazita, ondo dago.

[Laguntzaileen gidak](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
azaltzen du nola landu webgunea zure ordenagailuan.

## Itzulpenen egoera {#coverage}

"Berrikusia": pertsona batek egiaztatu du; "Automatikoa": makina batek itzuli du, eta
oraindik inork ez du berrikusi; "Zaharkitua": itzulpena egin ondoren, ingelesezko testua
aldatu da; "Falta da": orriak oraindik ez du itzulpenik.

{{< coverage >}}

## Kredituak {#credits}

Webgunea [Astro](https://astro.build/) tresnarekin eginda dago. IBM Plex Sans eta IBM Plex Mono
letra-tipoak erabiltzen ditu, SIL Open Font License lizentziapean. Itzulpenek
[kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) proiektuaren konbentzioei jarraitzen
diete, eta haren MeshCore glosarioak partekatzen dituzte. MeshCore bera
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) biltegian garatzen da.

Testuak eta itzulpenak CC BY 4.0 lizentziapean daude, eta kodea MIT lizentziapean.
