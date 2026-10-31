---
title: Tee meshistä kestävä
lead: Onko lähelläsi oleva mesh hidas tai täynnä roskaa? Selvitä, mistä se johtuu, kytke päälle toistimen asetus, joka pysäyttää sen, ja kerro paikalliselle ryhmällesi.
description: 'Floodit ja roskaviestit MeshCore-meshissä: miten tunnistat kunkin tyypin, mikä toistimen asetus auttaa, miten näet floodin ja miten löydät sen lähteen.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-10-31'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Tulevatko viestit perille myöhässä tai eivät lainkaan? Täyttyykö Public
roskasta? Silloin kyse on floodista: liikennettä on enemmän kuin mesh jaksaa
välittää, joko vahingossa tai tahallaan. Etsi näkemäsi alla olevista
taulukoista. Jokaisella rivillä on asetus, joka pysäyttää sen. Kytke se
päälle toistimessasi eli solmussa, joka välittää viestejä eteenpäin. Kerro
sitten [paikalliselle ryhmällesi](/community/), jotta ympärilläsi olevat
toistimet tekevät saman. Jokainen floodin pudottava toistin jättää lähetysaikaa
kaikille muille.

## Vahingossa syntyvät floodit {#mistake}

Vahingossa syntyvä flood tulee solmusta, jonka omistaja ei tiedä sen
aiheuttavan floodia. Se loppuu, kun omistaja saa tietää. Alla olevissa
taulukoissa ilmoitus on tervehdys, jonka solmu lähettää, jotta muut löytävät
sen.

Taulukoiden asetukset perustuvat siihen, mitä laiteohjelmisto tekee. Kaikki
niistä eivät ole vielä pysäyttäneet floodia oikeassa meshissä.

{{< callout type="warning" >}}
Osa tämän sivun asetuksista vaatii DMC-laiteohjelmiston. Tavallisessa
**MeshCore** 1.18.0:ssa on alueet, hyppyrajat `flood.max.*`, silmukoiden
tunnistus ja duty cycle. Pakettisuodatin eli säännöt, joilla toistimesi
pudottaa roskan, tulee **DMC-laiteohjelmiston** mukana
[Dutch-MeshCorelta](https://github.com/Dutch-MeshCore/MeshCore). Sen mukana
tulevat myös duty cycle -rajoitus ja companion-suodatin. Tämä sivu perustuu
DMC 1.18.0 -kehitysversioon `ecfb2d4` 19. lokakuuta 2026;
[pakettisuodattimen](/guides/filter/#firmware) sivulla kerrotaan, mistä sen
saa.
{{< /callout >}}

| Mitä näet | Mistä on kyse | Mikä auttaa |
| --- | --- | --- |
| Pyyntöjä toistimille yhdestä solmusta yötä päivää, ja mesh pysyy hitaana päiväkausia | Kotiautomaatio tai botti, joka kysyy toistimilta niiden tilaa liian usein | `filter on`. Pakettisuodatin päästää silloin läpi 5 pyyntöä minuutissa. Kerro omistajalle. |
| Samanlainen viesti kanavalla joka minuutti | Botti, joka lähettää liian usein | [Estä kanava](/guides/filter/#channel) tai [hidasta lähettäjää](/guides/filter/#sender). Kerro omistajalle. |
| Lukukelvottomia viestejä Publicissa ja muilla kanavilla | Solmu, jonka laiteohjelmisto on rikki tai radioasetukset väärät | `filter malformed on` pudottaa ne Publicissa. Kerro omistajalle. |
| Saman solmun ilmoitus muutaman minuutin välein | Solmu, joka on asetettu lähettämään ilmoituksia liian usein | `filter advert 24` päästää kunkin solmun ilmoituksen läpi kerran vuorokaudessa. `set flood.max.advert 3` pitää ilmoitukset 3 hypyn sisällä. |
| Viestejä kaukaa, ja niissä alueita, jotka eivät kuulu tänne | Silta, joka yhdistää meshejä internetin yli | `set flood.max.unscoped 1`, ja liitä toistimesi vain niihin [alueisiin, joita se palvelee](/guides/settings/#traffic). |
| Sama viesti kulkee yhä uudelleen, ja toistimesi tunnus on sen reitissä useammin kuin kerran | Toistin, joka muuttaa paketteja ja välittää ne eteenpäin, jolloin ne kiertävät silmukassa | Silmukoiden tunnistus on oletuksena tasolla `minimal`. `set loop.detect moderate` pudottaa silmukan aiemmin. |

## Tahalliset floodit {#purpose}

Osa floodeista on roskapostia: roskaa, jota joku lähettää tahallaan tukkiakseen
meshin. Lähettäjä vaihtaa nimiä, avaimia ja reittejä, joten mikään yksittäinen
sääntö ei pysäytä floodia.

| Mitä näet | Mistä on kyse | Mikä auttaa |
| --- | --- | --- |
| Monta uutta solmua satunnaisilla nimillä, jokaisella uusi avain | Väärennetyt ilmoitukset | `filter rate 04 5 60` päästää läpi 5 ilmoitusta minuutissa. `filter advert` ei auta: jokainen ilmoitus tulee [uudesta avaimesta](#forged). |
| Viestejä lukukelvottomalla tekstillä keksityiltä lähettäjiltä, usein yli vuoden takaisella päiväyksellä | Kanavaroskaposti | `filter malformed on` pudottaa ne Publicissa. `filter age 60` pudottaa vanhalla päiväyksellä olevat Publicissa ja [seuratuilla kanavilla](/guides/filter/#settings). |
| Jopa 200 yksityisviestiä minuutissa solmuille, joita ei ole olemassa, eikä yhtään kuittausta takaisin | Yksityisviestien flood | `filter rate 02 5 60`. Sovelluksesi ei näytä näitä viestejä, observer näyttää. |
| Pyyntöryöppyjä yhdestä solmusta kymmenille muille | Pyyntöroskaposti | Kun `filter on` on päällä, pakettisuodatin päästää läpi 5 pyyntöä minuutissa. |
| Viesti palaa 10–20 minuuttia myöhemmin lähes samalla reitillä | Uudelleentoisto: kopio, joka lähetetään uudelleen | Toistin muistaa 160 viimeksi näkemäänsä pakettia, joten vilkkaassa meshissä myöhempi kopio pääsee taas läpi. `filter age` pudottaa ryhmäviestin, joka on sallimaasi vanhempi. |
| Publicin viestejä uudelleen lähetettyinä keksityn lähettäjän nimissä, joskus vanhalla päiväyksellä | Kaikuroskaposti | `filter age 60`. `filter malformed on` pudottaa myös päiväyksen, joka heittää yli viikon. |
| Viesti muutaman sekunnin välein useilla kanavilla, joka kerta uudelta nimeltä, ja siinä tavallisia kysymyksiä | Bottiaalto | `filter rate 05 10 60`, ja [estä kanavat](/guides/filter/#channel), joita alueellasi ei käytetä. Jokainen nimi on uusi, joten [lähettäjäsäännöt](#forged) eivät osu siihen. |

## Mikä on toiminut {#worked}

Paikalliset ryhmät ovat pysäyttäneet floodeja näillä askelilla:

1. **Kerro omistajalle.** Vahingossa syntyvä flood loppuu, kun omistaja saa
   tietää. Lähetä hänelle ystävällinen viesti.
2. **Älä reagoi meshissä.** Vastaus kertoo roskapostittajalle, että roskaposti
   toimii.
3. **Pyydä observereita.** Observer on solmu, joka raportoi jokaisen
   kuulemansa paketin MQTT:n kautta. Mitä enemmän observereita ympärilläsi on,
   sitä nopeammin näet, mistä flood tulee sisään. Tee omasta toistimestasi
   sellainen: katso [MQTT observerissasi](/guides/mqtt/).
4. **Etsi lähde.** Observerit paikantavat lähettäjän tietylle alueelle.
   Viimeinen kilometri vaatii ihmisiä jalan radion kanssa. Katso
   [Etsi lähde](#source).
5. **Saa paikallinen ryhmäsi liikkeelle.** Yksi oikein asetettu toistin
   auttaa. Alueen kaikki toistimet yhdessä pysäyttävät floodin.
   [Paikallinen ryhmäsi](/community/) saa jokaisen omistajan kytkemään
   asetuksen päälle.

## Keksityt lähettäjät ja reitit {#forged}

Lähettäjä kirjoittaa nämä paketin osat, eikä mikään tarkista niitä:

- **Lähettäjän nimi.** Kanavaviestissä nimi on osa tekstiä. Kuka tahansa,
  jolla on kanavan avain, voi kirjoittaa minkä nimen tahansa.
- **Reitin alku.** Jokainen toistin lisää oman tunnuksensa reitin loppuun.
  Mikään ei tarkista aiemmin siellä olleita tunnuksia, joten lähettäjä voi
  aloittaa reitin keksityillä tunnuksilla. Reitin loppu on aito.

{{< forged-path >}}

Siksi `filter sender` ja `filter path` pysäyttävät lähettäjän vain siihen
asti, kun hän vaihtaa nimeään tai reittiään. [Reittiesto](/guides/filter/#path)
pudottaa myös sen toistimen aidon liikenteen, jonka tunnus estossa on.
Nopeusrajat, hyppyrajat, ikä- ja virhetarkistukset, kanavaestot, alueet ja
duty cycle toimivat edelleen.

## Asetukset jokaista floodia vastaan {#always}

Nämä toimivat, olipa flood mikä tahansa:

- **Duty cycle 10 %:ssa.** Toistimesi ei silloin koskaan lähetä enempää kuin
  laki sallii, tuli sisään mitä tahansa. Asiasta kerrotaan
  [toistinoppaassa](/repeater-guide/#duty-cycle).
- **Alueet ja hyppyrajat.** Alue on se seutu, jonka sisällä viesti pysyy.
  Toistin välittää vain niiden alueiden viestejä, joihin se kuuluu, ja
  `flood.max.*` pitää liikenteen lähellä. Molemmista kerrotaan sivulla
  [Pidä liikenne kurissa](/guides/settings/#traffic).
- **Pakettisuodatin vilkkaalle toistimelle.**
  [Valmiit asetukset](/guides/filter/#busy) puolittavat ryhmäviestit ja
  ilmoitukset. Kokeile niitä ensin [dry-run-tilassa](/guides/filter/#dryrun):
  se vain laskee, mitä se pudottaisi.
- **Companion-suodatin DMC-laiteohjelmistossa.** Companionisi eli solmu, josta
  lähetät viestejä, pitää roskan poissa sovelluksestasi. Se piilottaa rikkinäiset
  ja vanhat viestit sekä viestit, joissa on estämäsi toistin, lähettäjä tai
  sana. Lähettäjä- tai sanasääntö
  piilottaa viestin vain sinulta; muut saavat sen silti.

### Duty cycle -rajoitus {#gate}

DMC-laiteohjelmistossa voit antaa toistimesi asettaa oman alueensa etusijalle,
kun sillä on kiire. Kun toistin on lähettänyt yli 35 % viimeisestä minuutista,
se lakkaa välittämästä viestejä, joilla ei ole aluetta. Jos kiire jatkuu, se
pudottaa seuraavaksi laajimman alueen, taso kerrallaan. Sen oma alue pääsee
aina läpi. Rajoitus toimii vain, jos olet asettanut toistimellesi alueet.
Kytke se päälle ja tarkista se:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Rajoituksen pudottamat viestit eivät näy `filter stats` -tuloksissa. Kun
toistin rauhoittuu, alueet palaavat, sisin ensin.

## Havaitse flood {#see}

Sovelluksesi näyttää vain sen, mikä tavoittaa sinut. Vain observer kuulee
yksityisviestien floodin solmuille, joita ei ole olemassa. Jokainen observer
raportoi [MeshCore Analyzeriin](https://meshcore-analyzer.eu/), jossa kuka
tahansa näkee sen. Tee toistimestasi observer: katso
[MQTT observerissasi](/guides/mqtt/).

Katso Analyzerissa jokaista saman paketin kopiota. Sen reitti kertoo yleensä,
mistä se tuli. Flooderi voi aloittaa reitin [keksityillä tunnuksilla](#forged),
joten ensimmäiset tunnukset eivät kerro mitään. Jokaisessa kopiossa on
kuitenkin sama keksitty alku. Lyhimmän reitin kopio kulki harvimman aidon
toistimen kautta, joten se kuultiin lähimpänä lähettäjää.

{{< copies >}}

Omassa toistimessasi `filter stats` näyttää, mitä pakettisuodatin pudotti.
`filter stats top` näyttää solmutunnusten ensimmäisen tavun niiltä, jotka
aiheuttivat eniten pudotuksia. Monella solmulla on sama tavu, joten se rajaa
etsintää mutta ei nimeä lähettäjää.

## Etsi lähde {#source}

Kun flood palaa yhä uudelleen:

1. **Seuraa reittejä.** Lue reitti lopusta alkaen: viimeiset tunnukset ovat
   toistimia, joiden kautta flood kulki. Varhaisin aito tunnus on lähellä
   lähdettä; sitä edeltävät tunnukset voivat olla [keksittyjä](#forged).
2. **Rajaa alue.** Kun useampi observer kuulee saman paketin, ne paikantavat
   lähettäjän tietylle alueelle.
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) laskee sen
   paketin kuulleiden toistimien perusteella.
3. **Kävele viimeinen kilometri.** Toistimet kuulevat lähteen vain kuuluvuutensa
   reunalla, joten viimeinen osuus vaatii ihmisiä jalan.
   [Mesh-Hunter](https://mesh-hunter.eu/) muodostaa pariliitoksen
   companionisi kanssa ja tallentaa jokaisen kuulemansa paketin
   GPS-sijaintisi kera. Kun useampi ihminen kävelee yhtä aikaa, lähde löytyy
   nopeammin.
4. **Kerro [paikalliselle ryhmällesi](/community/).** He näkevät meshistä
   enemmän, päättävät jatkotoimista ja ottavat yhteyttä siihen, joka floodaa
   tahallaan.

## Lisää havaintosi {#add}

Osuiko sinuun flood, jota ei ole
näissä taulukoissa? Pysäyttikö jokin asetus sellaisen? Kerro meille
[Discordissa](https://discord.meshcore-info.eu/): mitä näit ja minkä asetuksen
kytkit päälle. Lisäämme sen sivulle.
