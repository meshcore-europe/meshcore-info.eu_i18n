---
title: Pakettisuodatin
lead: 'Estä toistintasi välittämästä roskaa: kauempaa tulvivia flood-paketteja, lakkaamatta postaavaa bottia, meluisaa kanavaa. Kokeile asetusta ensin, ota se sitten käyttöön.'
description: 'DMC-toistinlaiteohjelmiston pakettisuodatin: mitä se hylkää, valmiit asetukset tavalliselle ja vilkkaalle toistimelle, jokainen suodatinkomento oletusarvoineen, ja miten näet, mitä se hylkäsi.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '2bf23d24'
  seeded: '2026-10-26'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['0625daa2', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', 'ffc3f3a0', '3fa1bb28', '09511608']
---

Toistin (solmu, joka välittää viestejä eteenpäin) toistaa kaiken, mitä se kuulee.
Vilkkaassa meshissä mukana on myös roskaa. Botti postaa joka minuutti. Yksi solmu
lähettää ilmoituksensa, tervehdyksen, jonka avulla muut löytävät sen, uudestaan
muutaman minuutin välein. Perille tulee viestejä, jotka ovat kulkeneet puolen
maan halki. Jokainen toisto vie lähetysaikaa kaikilta ympärilläsi. Pakettisuodattimen
avulla toistimesi voi hylätä tällaisen liikenteen sen sijaan, että välittäisi sen eteenpäin.

{{< callout type="warning" >}}
Pakettisuodatin kuuluu **DMC-toistinlaiteohjelmistoon**, [Dutch-MeshCoren](https://github.com/Dutch-MeshCore/MeshCore)
toistinversioon. Vakio-MeshCoressa ei ole pakettisuodatinta; siinä on `region denyf *` ja
`set flood.max.unscoped`, jotka löydät [CLI-komennot](/guides/cli/)-sivulta. Tämä
opas noudattaa 19. lokakuuta 2026 julkaistua 1.18.0-kehitysversiota `ecfb2d4`. Vakaassa
1.17.1-versiossa on vain hyppy-, nopeus-, kanava-, hash- ja rikkinäisyyssuodattimet. Siinä
ei myöskään ole kokeilutilaa.
{{< /callout >}}

## Mitä suodatin tekee {#what}

Suodatin tarkastelee vain paketteja, jotka toistimesi välittää eteenpäin flood-tilassa
(lähettämällä ne jokaiselle kantaman sisällä olevalle solmulle). Se ei koskaan koske siihen,
mitä toistimesi itse lähettää, eikä paketteihin, jotka kulkevat tunnettua reittiä yhteen solmuun.
Myös yksityisviestit ja pyynnöt omille yhteystiedoillesi ja niiltä pääsevät läpi. Se voi hylätä:

- paketit, jotka ovat kulkeneet jo niin monen toistimen (hypyn) kautta kuin sallit,
  pakettityypin mukaan;
- yhden tyypin paketteja, joita tulee minuutissa enemmän kuin sallit;
- ilmoituksen solmulta, joka ilmoitti itsestään jo viime tunteina;
- viestit kanavalla, jonka estät;
- kaiken, mikä tuli yhden estämäsi toistimen kautta;
- ryhmäviestit yhdeltä lähettäjältä tai yhden sanan sisältävät, tai vain osan niistä;
- ryhmäviestit, jotka ovat rikki tai vanhempia kuin sallit.

Suodatin on **pois päältä**, kunnes otat sen käyttöön. Säädät sitä komennoilla. Kirjoita
ne USB:n yli tämän sivuston [sarjakonsolissa](/firmware/console/). Tai lähetä ne
MeshCore-sovelluksesta [toistinoppaan](/repeater-guide/#config) tapaan.

## Hanki laiteohjelmisto {#firmware}

Flashaa **DutchMeshCore Repeater** [DutchMeshCore Toolboxin](https://toolbox.dutchmeshcore.nl/)
flasherilla. Sama suodatin on myös tarkkailijan laiteohjelmistossa, josta kertoo sivu
[MQTT tarkkailijassasi](/guides/mqtt/).

## Kokeile ensin {#dryrun}

Kokeilutilassa suodatin laskee jokaisen paketin, jonka se hylkäisi, mutta välittää sen
silti eteenpäin. Mitoita asetus näin, ennen kuin se hylkää mitään:

```text
filter on
filter dryrun on
```

Kun kokeilutila on päällä, `filter`-komennon tilarivi päättyy tekstiin `(dry-run)`. Laskurit
kertovat, mitä se olisi hylännyt. Anna sen pyöriä päivän ja katso sitten lukemat
(katso [Mitä se hylkäsi](#stats)). Kun luvut näyttävät oikeilta, ota suodatin tosissaan käyttöön:

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

Ryhmäviestejä pääsee läpi enintään 20 minuutissa, yksityisviestejä enintään 5 minuutissa,
ja rikkinäiset ryhmäviestit hylätään. Laiteohjelmiston oma tavallinen asetus sallii
20 yksityisviestiä minuutissa. Tämä sivu käyttää sen suosittelemaa lukua 5 heinäkuussa 2026
tapahtuneen yksityisviestitulvan jälkeen.

### Vilkas toistin {#busy}

Toistimelle korkealla paikalla, joka kuulee kokonaisen alueen, tai toistimelle, joka hukkuu
liikenteeseen:

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

Tämä puolittaa ryhmäviestit ja ilmoitukset ja päästää jokaisen solmun ilmoituksen läpi
kerran päivässä. Se hylkää viestit, jotka ovat kulkeneet jo 16 toistimen kautta.
Uudelleenkäynnistyksen jälkeen jokaiselta solmulta pääsee yksi ilmoitus läpi. Laiteohjelmiston
oma dokumentaatio asettaa tässä myös `filter hash 2`; tämä sivu jättää sen pois (syy kohdassa
[Jokainen asetus](#settings)).

### Estä meluisa kanava {#channel}

```text
filter channel add #bot
```

Toistimesi kuulee kanavaa edelleen. Se ei enää välitä sitä muille toistimille eikä
kumppanilaitteille (solmuille, joista ihmiset lähettävät viestejä). Enintään 16 kanavaa.

### Hidasta yhtä lähettäjää {#sender}

Botti, joka postaa liian usein kanavalle, jonka haluat pitää:

```text
filter watch add #test
filter sender add Bob 60
```

Bobin viestit Public-kanavalla ja kanavalla `#test` pääsevät nyt läpi kerran minuutissa;
loput hylätään. Suodatin vertaa viestissä olevaa nimeä, joten nimensä vaihtava lähettäjä
pääsee siitä ohi.

### Estä yksi toistin ylävirrassa {#path}

Kun roska tulee yhden toistimen kautta, estä sen etuliite: tunnuksen alkuosa
heksadesimaalimuodossa (hex).

```text
filter path add a1b2
```

Lyhyt etuliite kuten `a1` estää myös jokaisen muun toistimen, jonka tunnus alkaa
merkeillä `a1`. Käytä mahdollisimman pitkää etuliitettä. Enintään 8 etuliitettä.

## Jokainen asetus {#settings}

Pakettityypeillä on numero. Toistimella `filter types` näyttää samat numerot
laiteohjelmiston nimillä, kuten `TXT_MSG` ja `GRP_TXT`:

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
| `filter on` / `filter off` | Ottaa suodattimen käyttöön tai pois käytöstä. | pois |
| `filter dryrun on` / `off` | Laskee hylkäykset mutta välittää silti kaiken eteenpäin. | pois |
| `filter hops <type> <max>` | Hylkää tyypin, joka on kulkenut jo näin monen toistimen kautta, 0–64. | 32 ryhmäviesteille, 8 muille |
| `filter rate <type> <limit> <secs> [soft]` | Päästää tyyppiä läpi enintään `limit` kappaletta `secs` sekunnissa. Kun `soft` on annettu, läpipääsy vähenee asteittain arvosta `soft` arvoon `limit`. `0` poistaa rajan. | 20 per 60 s yksityis- ja ryhmäviesteille, 10 ilmoituksille, 5 muille |
| `filter advert <hours>` | Päästää jokaisen solmun ilmoituksen läpi kerran näin monessa tunnissa, enintään 720. | 0 (pois) |
| `filter channel add <#name>` | Lopettaa kanavan välittämisen eteenpäin. | ei mitään |
| `filter path add <hex>` | Hylkää kaiken, mikä tuli tällä etuliitteellä alkavan toistimen kautta, 2–8 heksamerkkiä. | ei mitään |
| `filter sender add <name> [secs] [prob]` | Hylkää lähettäjän ryhmäviestit Public-kanavalla ja seuratuilla kanavilla. `Bot*` vastaa jokaista nimeä, joka alkaa sanalla Bot. | ei mitään |
| `filter text add <word> [secs] [prob]` | Hylkää sanan sisältävät ryhmäviestit Public-kanavalla ja seuratuilla kanavilla. `^word` vastaa vain viestin alussa. | ei mitään |
| `filter watch add <#name>` | Antaa lähettäjä- ja tekstisääntöjen lukea myös tätä kanavaa, enintään 4. Public luetaan aina. | Public |
| `filter malformed on` / `off` | Hylkää Public-viestit, jotka ovat tyhjiä, rikki tai yli viikon väärin päivättyjä (päiväystarkistus odottaa, kunnes kello on asetettu). | pois |
| `filter age <minutes>` / `off` | Hylkää tätä vanhemmat ryhmäviestit Public-kanavalla ja seuratuilla kanavilla, 1–10080. | pois |
| `filter hash <bytes>` | Hylkää paketit, joiden reittitunnus on tätä lyhyempi, 1–3. | 1 |
| `filter reset` | Palauttaa jokaisen asetuksen oletusarvoonsa. | |

Jokaiselle `add`-komennolle on `remove` ja `list`, kuten `filter channel remove #bot`.
Lähettäjä- ja tekstisäännöissä `secs` päästää läpi yhden viestin näin monessa sekunnissa.
`prob` soveltaa sääntöä vain tähän osuuteen osumista, 1–100. Enintään 8 lähettäjä- ja
8 tekstisääntöä. Nimissä ja sanoissa isot ja pienet kirjaimet erotetaan; nimi on enintään
15 merkkiä, sana enintään 23.

Kaksi asetusta hylkää enemmän kuin ehkä odotat:

- `filter hash 2` hylkää lähes kaiken liikenteen. Solmut lähettävät oletuksena 1 tavun
  reittitunnuksia.
- `filter age` luottaa toistimesi kelloon. Aseta kello sovelluksesta komennolla `clock sync`,
  tarkista se komennolla `clock` ja aloita väljästi: `filter age 60`.

Jokainen asetus säilyy uudelleenkäynnistyksen yli.

## Mitä se hylkäsi {#stats}

`filter` näyttää kokonaismäärät syyn mukaan:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` näyttää yhden asetuksen tiedot tarkemmin. Aiheet ovat
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` ja `age`. `filter stats top` näyttää eniten hylkäyksiä aiheuttaneiden solmujen
tunnusten ensimmäisen tavun, vihjeenä eikä todisteena.
`filter stats air` näyttää lähetysajan, jonka toistimesi säästi jättämällä nämä paketit
välittämättä.

Laskurit alkavat taas 0:sta uudelleenkäynnistyksen ja komennon `clear stats` jälkeen.
