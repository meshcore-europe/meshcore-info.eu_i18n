---
title: Antenniopas
lead: Antenni on puolet solmustasi. Oikea antenni hyvin asennettuna kantaa pidemmälle kuin suurempi teho. Tarkista kumppanilaitteesi antenni ja valitse, kytke ja asenna sitten antenni toistimelle.
description: 'Valitse ja asenna MeshCore-antenni 868 MHz:lle: tarkista kumppanilaitteen piiska-antenni, antennityypit ja vahvistus, liittimet, kaapelihäviö metriä kohti, suodattimet, asennus ja miten vahvistus lasketaan lakisääteiseen rajaan.'
eyebrow: Kumppanilaite ja toistin · 868 MHz
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '45010ad0'
  seeded: '2026-10-26'
  fields: {title: '3a76cb0e', lead: '98430ade', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', '94c5bae4', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
---

Korkeus, viritetty antenni ja lyhyt kaapeli tuovat enemmän kantamaa kuin yksikään ylimääräinen milliwatti. Tämä opas alkaa kumppanilaitteesta, radiosta, jolla lähetät viestejä. Sen jälkeen käsitellään toistimen antennia. Toistin on solmu, joka välittää viestejä eteenpäin katolta tai mastosta.

## Kumppanilaitteesi {#companion}

{{< callout type="warning" >}}
Kiinnitä antenni ennen kuin kytket radion päälle. LoRa-radio, joka
lähettää ilman antennia, voi vaurioittaa omaa piiriään.
{{< /callout >}}

Levyn mukana tullut antenni riittää. Kiinnitä se, pidä solmu pystyssä ja
aloita viestittely. Parempi antenni kumppanilaitteessa tuo vähän lisää;
kantaman sisällä oleva toistin tuo paljon.

Osta erillinen piiska-antenni vain, kun mukana tullut on rikki tai puuttuu.
Kaikkia 868 MHz:lle myytäviä piiska-antenneja ei ole viritetty sille.
[Tarkista se NanoVNA:lla](#nanovna), taskukokoisella antennianalysaattorilla,
ennen kuin luotat siihen, tai lainaa antenni toimivasta levystä.

Vahvan lähettimen vieressä oleva solmu kuulee vähemmän kuin sen pitäisi.
Pieni [SAW-suodatin (surface acoustic wave)](#filters) radion ja antennin
välissä pitää tuon lähettimen poissa vastaanottimesta. Tarkista ensin sen
datalehti:

- **Suurin sallittu tuloteho.** Suodatin on myös oman lähetyksesi reitillä.
  Levy, joka lähettää 22 dBm (160 mW) 15 dBm:lle mitoitettuun suodattimeen,
  rikkoo suodattimen.
- **Päästökaista.** Sen on katettava esiasetuksesi taajuus. Suodatin, joka
  on tarkoitettu alueelle 868.65–869.25 MHz, ei päästä läpi EU/UK (Narrow)
  -kanavaa taajuudella 869.618 MHz.

## Antennityypit toistimelle {#types}

Jokainen antenni meshissä on pystyssä. Valitse tyyppi sen mukaan, missä tavoiteltavat solmut ovat:

- **Lasikuituinen kollineaariantenni.** Valkoinen putki mastossa, joka vahvistaa joka suuntaan horisontin tasossa. Vakiovalinta toistimelle, joka palvelee kaupunkia.
- **Dipoli.** Lyhyempi, vähemmän vahvistusta ja korkea keila. Se tavoittaa ala- ja yläpuolellasi olevat solmut paremmin kuin kollineaariantenni. Sillä on merkitystä mäellä laakson yläpuolella.
- **Yagi.** Puomi poikittaisilla elementeillä, suunnattuna yhteen paikkaan. Se tavoittaa yhden kaukaisen toistimen eikä juuri muuta. Asenna se elementit pystyssä, koska sen polarisaatio seuraa elementtejä.

## Vahvistus ja keila {#gain}

Vahvistus ei lisää tehoa. Se ottaa signaalin, joka menisi ylös ja alas, ja lähettää sen horisontin suuntaan. Kuin taskulamppu, jonka tarkennat: sama paristo, pidempi ja kapeampi keila. Saman valmistajan dipoli ja kollineaariantenni näyttävät sen:

| Antenni | Vahvistus | Pystykeilan leveys |
|---|---|---|
| Dipoli (Sirio SO 868-915-2) | 2.2 dBi | 88 astetta |
| Lasikuituinen kollineaariantenni (Sirio SPO 868-915-6) | 5.8 dBi | 23 astetta |

{{< gain >}}

Kaavio leikkaa maston poikki sivulta katsottuna. Pyöräytä se maston ympäri, niin saat koko keilan: donitsin dipolille, litteän kiekon kollineaariantennille. Pystyssä oleva antenni lähettää samalla tavalla joka suuntaan ympärillään. Piirretyn keilan ulkopuolella signaali ei lopu; se on heikompi, mutta riittää yhä lähellä olevalle solmulle.

Katolla litteä keila on juuri se, mitä haluat. Korkealla mäellä solmujen yläpuolella 23 asteen keila menee niiden yli; dipoli kattaa ne. Yagi vie tämän pidemmälle: 16.6 dBi keilassa, joka on 23 astetta korkea ja 25 astetta leveä (Amphenol Procom 7176870), eikä mitään sivuille.

Vahvistus lasketaan vertailukohtaa vasten. dBi vertaa ihanteelliseen antenniin, joka lähettää yhtä paljon joka suuntaan. dBd vertaa puoliaaltodipoliin, jolla itsellään on 2.15 dBi: yksinkertaisinkaan antenni ei lähetä mitään suoraan ylös tai alas. Pidempi dipoli, 1.25 aallonpituutta, yltää 5.2 dBi:hin. Kollineaariantenni sen sijaan pinoaa puoliaaltoelementtejä päällekkäin: mitä enemmän se pinoaa, sitä suurempi vahvistus. Purista sama signaali puoleen tilasta, niin se on siellä kaksi kertaa vahvempi: 3 dB. Neljäsosaan, niin 4 kertaa vahvempi: 6 dB. Valmistajat ilmoittavat vahvistuksen dBi:nä; lakisääteinen raja lasketaan dBd:nä, katso [Lakisääteisen rajan sisällä](#legal).

### Mikä vahvistus sinun paikallesi {#choose-gain}

- **Mäet, laaksot tai tiheä kaupunki: noin 3 dBi.** Korkea keila tavoittaa
  solmut ylä- ja alapuolellasi sekä tiellä olevien rinteiden ja rakennusten
  ympäri. Se toimii myös toisinpäin: laaksosta litteä keila menee mäellä
  yläpuolella olevan toistimen ali. RAKwireless RAKARG12 on yksi tällainen:
  36 cm pitkä lasikuituputki.
- **Lähiöt tai pikkukaupunki matalilla katoilla: 5–6 dBi.** Vakiomallinen
  lasikuituinen kollineaariantenni.
- **Tasainen, avoin maasto: 8–10 dBi.** Litteimmän keilan kantama horisontin
  suuntaan on pisin. Korkealle asennettuna se menee lähellä olevien solmujen
  yli.

Nimessä oleva vahvistus on paras lukema antennin koko kaistalta.
RAKARG12, jota myydään 3 dBi:n antennina, antaa 2.8 dBi alueella 865–870 MHz.
Lue datalehden vahvistustaulukko esiasetuksesi taajuudelta.

Yli 7 dBi:llä 22 dBm:n levy ylittää lakisääteisen rajan, ellei kaapelin ja
suodattimen häviö kata erotusta. Laske lähetystehoa vastaavasti.

Suuri vahvistus auttaa vain, kun tiedät, missä solmut ovat: horisontin
tasossa toistimen ympärillä tai yhdessä kaukaisessa toistimessa Yagille.
Kädessäsi oleva kumppanilaite osoittaa joka suuntaan, joten sen mukana tullut
pieni vahvistus sopii sille parhaiten.

## Miksi pystyssä {#vertical}

Antennit kuulevat toisensa parhaiten, kun ne osoittavat samaan suuntaan. Häviö kasvaa niiden välisen kulman mukana: 45 astetta maksaa 3 dB, puolet signaalistasi. 90 asteessa, vaakasuora antenni pystysuoraa vasten, teoriassa mitään ei tule perille. Mesh seisoo pystyssä, joten sinun antennisi myös. Tämä pätee myös pöydällä olevaan kumppanilaitteeseen: laske se lappeelleen, niin jokainen solmu ympärilläsi kuulee heikommin.

## Liittimet {#connectors}

Tilaa antenni sillä liittimellä, joka piirilevylläsi on. Jokainen sovitin on yksi tiivistettävä liitos lisää ja lisää signaalihäviötä.

- **SMA.** Kierteellinen liitin, noin 6 mm leveä. Useimpien piirilevyjen liittimessä on reikä keskellä; antennissa on piikki. Tällainen liitin hävittää noin 0.03 dB 868 MHz:llä.
- **RP-SMA.** Sama runko ja kierre kuin SMA, mutta piikki ja reikä ovat vaihtaneet paikkaa. Se näyttää SMA:lta eikä sovi siihen. Tarkista ennen tilaamista, kumpi piirilevylläsi on.
- **U.FL (IPEX).** Pikkuruinen painoliitin itse piirilevyllä. Lyhyt pigtail-kaapeli kulkee siitä kotelon SMA-liittimeen. Sen kestoksi ilmoitetaan 30 kytkentäkertaa, joten kytke se kerran ja jätä rauhaan.
- **N.** Suuri kierteellinen liitin lasikuituantenneissa ja paksussa kaapelissa. Se hävittää enintään 0.05 dB. Toistin tarvitsee yhden sovittimen tai pigtailin N:stä piirilevyn SMA:han.

## Kaapelihäviö {#cable}

Kaapeli syö signaalia ennen kuin se lähtee antennista, molempiin suuntiin. 3 dB
on puolet tehostasi. Valmistajien luvut metriä kohden, 868–900 MHz:llä:

| Kaapeli | Häviö metriä kohden | Häviö 5 m:llä |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metriä RG174:ää, monien levyjen mukana tulevaa ohutta pigtail-kaapelia,
hävittää puolet tehostasi. Asenna levy antennin viereen lyhyellä pigtaililla
tai vedä siihen paksu kaapeli. Lisää summaan jokainen reitillä oleva sovitin
ja suodatin.

## Suodattimet {#filters}

Suodatin on radion ja antennin välissä. Se päästää läpi oman kaistasi ja
estää muut, jotta lähellä oleva vahva lähetin ei tukahduta vastaanotinta.
Tarvitset sellaisen, kun solmu kuulee vähemmän kuin sen pitäisi muiden
lähettimien lähellä. Toistin mastossa, jossa on matkapuhelintukiasemia, on
tällainen solmu. Suodatin maksaa signaalia molempiin suuntiin: laske sen
häviö kuten kaapelin.

| | SAW-suodatin | Onkalosuodatin |
|---|---|---|
| Koko | Muutama millimetri, pienellä piirilevyllä | Metallilohko tai -putki |
| Hyvän häviö | alle 2 dB | alle 1 dB |
| Hyvän suurin sallittu tuloteho | 500 mW | useita watteja |

Esimerkiksi sysmocom cf866.5-kt30 on onkalosuodatin alueelle 863–870 MHz,
joka hävittää enintään 1.0 dB ja kestää 30 W. Se on tehty sisätiloihin,
joten laita se mastossa tiiviiseen koteloon.

Suodattimet eroavat paljon toisistaan, joten tarkista datalehti ennen ostoa.
Sen suurimman sallitun tulotehon on ylitettävä lähetystehosi, ja sen
päästökaistan on katettava esiasetuksesi taajuus.

## Asennus {#mounting}

- **Katon reunan yläpuolelle.** Antenni tarvitsee esteettömän näkymän jokaiseen palvelemaansa suuntaan. Jo muutama metri ympäröivien kattojen yläpuolella auttaa. Toistinoppaan kohta [Valitse paikka](/repeater-guide/#site) näyttää, miten näkymä tarkistetaan.
- **Kauas metallista.** Rännit, mastot, muut antennit ja peltikatot antennin vieressä muuttavat sen suuntakuviota ja viritystä. Asenna se maston huipulle, ei sen kylkeen.
- **Pystyyn.** Käytä vesivaakaa; katso [Miksi pystyssä](#vertical).
- **Tippalenkki.** Anna kaapelin roikkua liittimen alapuolella ennen kuin se nousee ylös tai menee sisään. Vesi tippuu silloin pois sen sijaan, että valuisi liitokseen.
- **Tiivistä jokainen ulkoliitin.** Vesi liittimessä kasvattaa häviötä ja syövyttää piikin. Tiivistä se sadetta vastaan ja tarkista tiiviste joka vuosi.
- **Salama.** Antenni katolla on kohde. Kaasupurkaussuoja kaapelissa laukeaa ylijännitteestä ja ohjaa sen maahan. Noudata toistinoppaan kohtaa [Laitteisto](/repeater-guide/#hardware) ja paikallisia maadoitussääntöjä.

## Lakisääteisen rajan sisällä {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
Euroopassa MeshCore käyttää alikaistaa 869.40-869.65 MHz, jolla suurin sallittu efektiivinen säteilyteho (e.r.p.) on **500 mW**. Raja lasketaan siitä, mitä antennista lähtee: antennin vahvistus lisätään, kaapeli- ja suodatinhäviöt vähennetään. Vahvistus dBi:nä lasketaan 2.15 dB pienempänä, koska raja mitataan dipolia vasten.
{{< /callout >}}

5.8 dBi:n kollineaariantenni 22 dBm:n piirilevyllä pysyy rajan sisällä. Sama antenni vahvistimella varustetulla piirilevyllä ei pysy, ennen kuin lasket lähetystehoa. Toistinoppaan kohdassa [Teho: e.r.p. ja antennisi](/repeater-guide/#erp) on laskukaava ja 2 laskettua esimerkkiä.

## Tarkista antenni NanoVNA:lla {#nanovna}

NanoVNA on taskukokoinen vektoripiirianalysaattori. Se näyttää, mille
taajuudelle antenni on viritetty, joten tiedät sen ennen asennusta.
NanoVNA-H mittaa 1.5 GHz:iin asti, mikä kattaa 868 MHz:n.

1. Kalibroi se alueelle 800–950 MHz sen sarjan avoin-, oikosulku- ja
   kuormakappaleilla.
2. Kytke antenni sen sovittimen kautta, jota se käyttää solmussa. Pidä se
   pystyssä ja kaukana kehostasi ja pöydästä.
3. Lue SWR-käyrä (seisovan aallon suhde): se näyttää, kuinka paljon
   signaalia antenni lähettää takaisin. Kuopan on oltava esiasetuksesi
   taajuudella, 869.618 MHz EU/UK (Narrow) -kanavalle. Satojen MHz:ien
   päässä oleva kuoppa tarkoittaa, että antenni on tehty toiselle kaistalle.

Neljännesaalto 868 MHz:llä on 86 mm (aallonpituus on 345 mm). Pituus yksin
ei kerro kaistaa, koska valmistajat taittavat ja kuormittavat piiskoja;
NanoVNA kertoo.

## Lähteet {#sources}

- Kaapelihäviö: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  Huber+Suhnerin RG316-datalehti,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  Times Microwaven LMR-240- ja LMR-400-datalehdet,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antennit: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  Sirio SO 868-915-2 -datalehti,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Vahvistus signaalina, joka puristetaan pienempään tilaan: [RF Cafe, antenna introduction](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Liittimet: Rosenbergerin 32S102 (SMA)- ja 53S101 (N) -datalehdet, Hirosen U.FL-luettelo.
- Suodattimet: sysmocom cf866.5-kt30 -tuotesivu,
  [Citelin kaasupurkaussuojat](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarisaatiohäviö: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipolin vahvistus pituuden mukaan: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Aallonpituus: valonnopeus lähteestä [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Lakisääteinen raja: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  liite 1, kaista h1.7; [toistinopas](/repeater-guide/#legal) luettelee loput.
