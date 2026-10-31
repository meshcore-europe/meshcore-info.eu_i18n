---
title: Pakettisuodatin
lead: 'Estä toistintasi välittämästä roskaa: kaukaa tulevia floodeja, loputtomasti postaavaa bottia tai meluisaa kanavaa. Kokeile asetusta ensin ja ota se sitten käyttöön.'
description: 'DMC-toistinlaiteohjelmiston pakettisuodatin: mitä se pudottaa, valmiit asetukset tavalliselle ja kiireiselle toistimelle, jokainen suodatinkomento oletusarvoineen ja miten näet, mitä se pudotti.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-10-31'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Toistin (solmu, joka välittää viestejä eteenpäin) toistaa kaiken kuulemansa.
Vilkkaassa meshissä mukana on myös roskaa. Botti postaa joka minuutti. Yksi
solmu lähettää ilmoituksensa muutaman minuutin välein. Ilmoitus on tervehdys,
jonka avulla muut löytävät solmun. Perille tulee viestejä, jotka ovat kulkeneet
puolen maan halki. Jokainen toisto vie lähetysaikaa kaikilta ympärilläsi.
Pakettisuodattimella toistimesi pudottaa tämän liikenteen eikä välitä sitä.
Sivulla [Tee meshistä kestävä](/guides/resilient/) selvität ensin, mikä
meshiisi tulvii, ja mikä auttaa suodattimen lisäksi.

{{< callout type="warning" >}}
Pakettisuodatin kuuluu **DMC-toistinlaiteohjelmistoon**, joka on
[Dutch-MeshCoren](https://github.com/Dutch-MeshCore/MeshCore) toistinversio.
Tavallisessa MeshCoressa ei ole pakettisuodatinta. Siinä on `region denyf *` ja
`set flood.max.unscoped`, jotka löydät sivulta [CLI-komennot](/guides/cli/).
Tämä opas perustuu 19. lokakuuta 2026 julkaistuun 1.18.0-kehitysversioon
`ecfb2d4`. Vakaassa 1.17.1-versiossa on vain hyppy-, nopeus-, kanava-, hash- ja
virhesuodattimet. Siinä ei myöskään ole kuivaharjoitustilaa (dry-run).
{{< /callout >}}

## Mitä suodatin tekee {#what}

Suodatin katsoo vain paketteja, jotka toistimesi välittää floodina (lähettää
kaikille kantaman solmuille). Se ei koske toistimesi omiin lähetyksiin eikä
paketteihin, jotka kulkevat tunnettua reittiä yhdelle solmulle. Myös
yksityisviestit ja pyynnöt omille yhteystiedoillesi ja niiltä kulkevat läpi.
Suodatin voi pudottaa:

- paketit, jotka ovat jo kulkeneet niin monen toistimen (hypyn) kautta kuin
  sallit, pakettityypeittäin;
- yhden tyypin paketit, kun niitä tulee minuutissa enemmän kuin sallit;
- ilmoituksen solmulta, joka on jo ilmoittautunut viime tuntien aikana;
- viestit kanavalla, jonka estät;
- kaiken, mikä tuli yhden estämäsi toistimen kautta;
- ryhmäviestit yhdeltä lähettäjältä tai ryhmäviestit, joissa on tietty sana, tai vain osan niistä;
- ryhmäviestit, jotka ovat rikki tai vanhempia kuin sallit.

Suodatin on **pois päältä**, kunnes kytket sen päälle. Asetat sen komennoilla.
Kirjoita ne USB:n kautta tämän sivuston [sarjakonsoliin](/firmware/console/).
Voit myös lähettää ne MeshCore-sovelluksesta, kuten
[toistinoppaassa](/repeater-guide/#config) neuvotaan.

## Hanki laiteohjelmisto {#firmware}

Flashaa **DutchMeshCore Repeater**
[DutchMeshCore Toolboxin](https://toolbox.dutchmeshcore.nl/) flasherilla.
Sivun [MQTT observerissasi](/guides/mqtt/) observer-laiteohjelmistossa on sama
suodatin.

## Kokeile ensin {#dryrun}

Dry-run-tilassa suodatin laskee jokaisen paketin, jonka se pudottaisi, mutta
välittää sen silti. Näin mitoitat asetuksen ennen kuin se pudottaa mitään:

```text
filter on
filter dryrun on
```

Kun dry-run on päällä, `filter`-komennon tilarivi päättyy tekstiin `(dry-run)`.
Luvut kertovat, mitä suodatin olisi pudottanut. Anna sen olla päällä vuorokauden ja
katso sitten lukuja (katso [Mitä se pudotti](#stats)). Kun luvut näyttävät
oikeilta, ota suodatin käyttöön:

```text
filter dryrun off
```

## Suositellut asetukset {#configs}

### Tavallinen toistin {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Ryhmäviestejä menee läpi enintään 20 minuutissa ja yksityisviestejä enintään 5
minuutissa. Rikkinäiset ryhmäviestit pudotetaan. Laiteohjelmiston oma tavallinen
asetus sallii 20 yksityisviestiä minuutissa. Tämä sivu käyttää arvoa 5, jota
laiteohjelmisto suosittelee heinäkuun 2026 yksityisviestitulvasta lähtien.

### Kiireinen toistin {#busy}

Toistimelle korkealla paikalla, josta se kuulee koko alueen, tai toistimelle,
joka on tulvan alla:

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

Tämä puolittaa ryhmäviestit ja ilmoitukset ja päästää jokaisen solmun
ilmoituksen läpi kerran vuorokaudessa. Se pudottaa viestit, jotka ovat jo
kulkeneet 16 toistimen kautta. Uudelleenkäynnistyksen jälkeen jokaiselta
solmulta pääsee yksi ilmoitus läpi. Laiteohjelmiston omissa ohjeissa tähän
asetetaan myös `filter hash 2`. Tämä sivu jättää sen pois (syy kohdassa
[Kaikki asetukset](#settings)).

### Estä meluisa kanava {#channel}

```text
filter channel add #bot
```

Toistimesi kuulee kanavan edelleen. Se ei enää välitä sitä muille toistimille
ja companioneille (solmuille, joilla ihmiset lähettävät viestejä). Enintään 16
kanavaa.

### Hidasta yhtä lähettäjää {#sender}

Botti postaa liian usein kanavalla, jonka haluat pitää:

```text
filter watch add #test
filter sender add Bob 60
```

Bobin viestit Public-kanavalla ja `#test`-kanavalla menevät nyt läpi kerran
minuutissa. Loput pudotetaan. Suodatin vertaa viestissä olevaa nimeä, joten
nimensä vaihtava lähettäjä pääsee läpi.

### Estä yksi toistin ylävirrassa {#path}

Kun roska tulee yhden toistimen kautta, estä sen etuliite. Etuliite on toistimen
tunnuksen alku heksadesimaalina (hex). Tähän tarvitset 1.18-kehitysversion,
sillä versiossa 1.17.1 ei ole reittisuodatinta.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` näyttää estämäsi etuliitteet ja `filter stats path` sen,
paljonko kukin pudotti. `filter path remove a1b2` päästää toistimen taas läpi.
Lyhyt etuliite kuten `a1` estää myös kaikki muut toistimet, joiden tunnus
alkaa merkeillä `a1`. Käytä niin pitkää etuliitettä kuin voit. Enintään 8 etuliitettä.

## Kaikki asetukset {#settings}

Pakettityypit merkitään numeroilla. Toistimella `filter types` näyttää samat
numerot laiteohjelmiston nimillä, kuten `TXT_MSG` ja `GRP_TXT`:

| Numero | Tyyppi | Numero | Tyyppi |
| --- | --- | --- | --- |
| `00` | pyyntö | `06` | ryhmädata |
| `01` | vastaus | `07` | anonyymi pyyntö |
| `02` | yksityisviesti | `08` | reitti |
| `03` | kuittaus | `09` | jäljitys |
| `04` | ilmoitus | `10` | moniosainen |
| `05` | ryhmäviesti | `11` | ohjaus |

| Komento | Mitä se tekee | Oletus |
| --- | --- | --- |
| `filter on` / `filter off` | Kytkee suodattimen päälle tai pois. | pois |
| `filter dryrun on` / `off` | Laskee pudotukset, mutta välittää silti kaiken. | pois |
| `filter hops <type> <max>` | Pudottaa tyypin, joka on jo kulkenut näin monen toistimen kautta, 0–64. | 32 ryhmäviesteille, 8 muille |
| `filter rate <type> <limit> <secs> [soft]` | Päästää läpi enintään `limit` tyypin pakettia `secs` sekunnissa. `soft`-arvolla läpäisy vähenee vähitellen `soft`-arvosta `limit`-arvoon. `0` poistaa rajan. | 20 / 60 s yksityis- ja ryhmäviesteille, 10 ilmoituksille, 5 muille |
| `filter advert <hours>` | Päästää kunkin solmun ilmoituksen läpi kerran näin monessa tunnissa, enintään 720. | 0 (pois) |
| `filter channel add <#name>` | Lopettaa kanavan välittämisen. | ei mitään |
| `filter path add <hex>` | Pudottaa kaiken, mikä tuli tällä etuliitteellä alkavan toistimen kautta, 2–8 heksanumeroa. | ei mitään |
| `filter sender add <name> [secs] [prob]` | Pudottaa lähettäjän ryhmäviestit Public-kanavalla ja seuratuilla kanavilla. `Bot*` osuu jokaiseen nimeen, joka alkaa sanalla Bot. | ei mitään |
| `filter text add <word> [secs] [prob]` | Pudottaa sanan sisältävät ryhmäviestit Public-kanavalla ja seuratuilla kanavilla. `^word` osuu vain viestin alussa olevaan sanaan. | ei mitään |
| `filter watch add <#name>` | Antaa lähettäjä- ja tekstisääntöjen lukea myös tämän kanavan, enintään 4. Public luetaan aina. | Public |
| `filter malformed on` / `off` | Pudottaa Public-viestit, jotka ovat tyhjiä, rikki tai joiden päiväys poikkeaa yli viikon (päiväystarkistus odottaa, kunnes kello on asetettu). | pois |
| `filter age <minutes>` / `off` | Pudottaa tätä vanhemmat ryhmäviestit Public-kanavalla ja seuratuilla kanavilla, 1–10080. | pois |
| `filter hash <bytes>` | Pudottaa paketit, joiden reittitunnus on tätä lyhyempi, 1–3. | 1 |
| `filter reset` | Palauttaa jokaisen asetuksen oletusarvoonsa. | |

Jokaisella `add`-komennolla on `remove` ja `list`, kuten `filter channel remove #bot`.
Lähettäjä- ja tekstisäännöissä `secs` päästää läpi yhden viestin näin monessa
sekunnissa. `prob` soveltaa sääntöä vain tähän osuuteen osumista, 1–100.
Enintään 8 lähettäjä- ja 8 tekstisääntöä. Nimissä ja sanoissa isot ja pienet
kirjaimet erotetaan. Nimi on enintään 15 merkkiä, sana enintään 23.

Kaksi asetusta pudottaa enemmän kuin ehkä odotat:

- `filter hash 2` pudottaa lähes kaiken liikenteen. Solmut lähettävät
  oletuksena 1 tavun reittitunnuksia.
- `filter age` luottaa toistimesi kelloon. Aseta kello sovelluksesta komennolla
  `clock sync`, tarkista se komennolla `clock` ja aloita väljästi: `filter age 60`.

Jokainen asetus säilyy uudelleenkäynnistyksen jälkeen.

## Mitä se pudotti {#stats}

`filter` näyttää kokonaismäärät syittäin:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` näyttää yhden asetuksen tiedot tarkemmin. Aiheet ovat
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` ja `age`. `filter stats top` näyttää niiden solmujen tunnusten
ensimmäisen tavun, joiden takia pudotuksia on eniten. Monella solmulla on sama
tavu. `filter stats air` näyttää lähetysajan, jonka toistimesi säästi, kun se
ei välittänyt näitä paketteja.

Laskurit alkavat taas 0:sta uudelleenkäynnistyksen ja `clear stats`
-komennon jälkeen.
