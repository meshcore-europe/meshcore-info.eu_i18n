---
title: Antenniopas
lead: Oikea antenni hyvin asennettuna kantaa pidemmälle kuin lisäteho. Tarkista ensin companion-laitteesi antenni. Valitse sitten toistimelle antenni, liitä se ja asenna se.
description: 'Valitse ja asenna MeshCore-antenni 868 MHz:lle: companion-laitteen piiska-antennin tarkistus, antennityypit ja vahvistus, liittimet, kaapelin vaimennus metriä kohden, suodattimet, asennus ja vahvistuksen vaikutus lailliseen rajaan.'
eyebrow: Companion ja toistin · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-10-31'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Korkeus, viritetty antenni ja lyhyt kaapeli tuovat enemmän kantamaa kuin
yksikään lisämilliwatti. Opas alkaa companion-laitteesta eli radiosta, jolla
lähetät viestejä. Sen jälkeen opas käsittelee toistimen antennin. Toistin on
solmu, joka välittää viestejä eteenpäin katolta tai mastosta.

## Companion-laitteesi {#companion}

{{< callout type="warning" >}}
Kiinnitä antenni ennen kuin kytket radion päälle. LoRa-radio, joka lähettää
ilman antennia, voi vaurioittaa omaa piiriään.
{{< /callout >}}

Piirilevyn mukana tullut antenni riittää. Kiinnitä se, pidä solmua pystyssä
ja aloita viestittely. Parempi antenni companion-laitteessa hyödyttää vähän.
Toistin kantaman sisällä hyödyttää paljon.

Osta erillinen piiska-antenni vain, jos mukana tullut on rikki tai puuttuu.
Kaikkia 868 MHz:lle myytäviä piiska-antenneja ei ole viritetty sille.
[Tarkista antenni NanoVNA:lla](#nanovna) ennen kuin luotat siihen. NanoVNA on
taskukokoinen antennianalysaattori. Voit myös lainata antennin toimivasta
laitteesta.

Vahvan lähettimen vieressä oleva solmu kuulee huonommin kuin sen pitäisi.
Pieni [SAW-suodatin (surface acoustic wave)](#filters) radion ja antennin
välissä pitää lähettimen signaalin poissa vastaanottimesta. Tarkista ensin
suodattimen datalehti:

- **Suurin tuloteho.** Myös oma lähetyksesi kulkee suodattimen läpi. Jos
  laite lähettää 22 dBm (160 mW) suodattimeen, joka on mitoitettu 15 dBm:lle,
  suodatin hajoaa.
- **Päästökaista.** Sen täytyy kattaa esiasetuksesi taajuus. Suodatin
  taajuuksille 868.65–869.25 MHz ei päästä läpi EU/UK (Narrow) -kanavaa,
  joka on 869.618 MHz:ssä.

## Toistimen antennityypit {#types}

Meshin jokainen antenni on pystyasennossa. Valitse tyyppi sen mukaan, missä
ne solmut ovat, jotka haluat tavoittaa:

- **Lasikuitukollineaari.** Valkoinen putki mastossa, vahvistus joka
  suuntaan horisontin ympäri. Tavallinen valinta toistimelle, joka palvelee
  kaupunkia.
- **Dipoli.** Lyhyempi, vahvistus pienempi ja keila korkea. Se tavoittaa
  kollineaaria paremmin solmut alapuolellasi ja yläpuolellasi, esimerkiksi
  laakson yllä olevalta mäeltä.
- **Yagi.** Puomi, jossa on poikittaiset elementit, suunnattuna yhteen
  paikkaan. Se tavoittaa yhden kaukaisen toistimen eikä juuri muuta.
  Asenna elementit pystyyn, koska polarisaatio seuraa elementtejä.

## Vahvistus ja keila {#gain}

Vahvistus ei lisää tehoa. Se ottaa signaalin, joka menisi ylös ja alas, ja
lähettää sen horisontin suuntaan. Kuin taskulamppu, jonka valon tarkennat:
sama paristo, pidempi ja kapeampi keila. Saman valmistajan dipoli ja
kollineaari näyttävät tämän:

| Antenni | Vahvistus | Pystykeilan leveys |
|---|---|---|
| Dipoli (Sirio SO 868-915-2) | 2.2 dBi | 88 astetta |
| Lasikuitukollineaari (Sirio SPO 868-915-6) | 5.8 dBi | 23 astetta |

{{< gain >}}

Kuva on leikkaus maston läpi sivulta katsottuna. Kun kierrät sitä maston
ympäri, saat koko keilan: dipolilla donitsin, kollineaarilla litteän kiekon.
Pystyantenni lähettää samalla tavalla joka suuntaan ympärilleen. Piirretyn
keilan ulkopuolella signaali ei lopu. Se on heikompi mutta riittää lähellä
olevalle solmulle.

Katolla haluat litteän keilan. Mäellä korkealla solmujen yläpuolella 23
asteen keila kulkee niiden päiden yli, dipoli taas kattaa ne. Yagi vie tämän
pidemmälle: 16.6 dBi keilassa, joka on 23 astetta korkea ja 25 astetta leveä
(Amphenol Procom 7176870), eikä mitään sivuille.

Vahvistus ilmoitetaan suhteessa vertailukohtaan. dBi vertaa ihanteelliseen
antenniin, joka lähettää tasaisesti joka suuntaan. dBd vertaa
puoliaaltodipoliin, jonka oma vahvistus on 2.15 dBi: yksinkertaisinkaan
antenni ei lähetä mitään suoraan ylös tai alas. Pidempi dipoli, 1.25
aallonpituutta, yltää 5.2 dBi:hin. Kollineaari taas pinoaa
puoliaaltoelementtejä päällekkäin: mitä enemmän elementtejä, sitä suurempi
vahvistus. Kun sama signaali puristetaan puoleen tilasta, se on siellä
kaksi kertaa vahvempi: 3 dB. Neljännekseen puristettuna 4 kertaa vahvempi:
6 dB. Valmistajat ilmoittavat vahvistuksen dBi:nä, laillinen raja lasketaan
dBd:nä, katso [Laillisen rajan sisällä](#legal).

### Mikä vahvistus sopii paikallesi {#choose-gain}

- **Mäet, laaksot tai tiivis kaupunki: noin 3 dBi.** Korkea keila
  tavoittaa solmut yläpuolellasi ja alapuolellasi sekä välissä olevien
  rinteiden ja rakennusten takana. Tämä pätee myös toisin päin: laaksosta
  litteä keila kulkee yläpuolisella mäellä olevan toistimen alta.
  RAKwireless RAKARG12 on tällainen: 36 cm:n lasikuituputki.
- **Esikaupungit tai matalien kattojen kaupunki: 5–6 dBi.** Tavallinen
  lasikuitukollineaari.
- **Tasainen, avoin maasto: 8–10 dBi.** Litteimmällä keilalla pääset
  pisimmälle horisontin suuntaan. Korkealle asennettuna se kulkee
  lähellä olevien solmujen yli.

Nimessä mainittu vahvistus on paras lukema antennin koko kaistalla.
RAKARG12 myydään 3 dBi:n antennina, mutta taajuuksilla 865–870 MHz sen
vahvistus on 2.8 dBi. Lue datalehden vahvistustaulukosta esiasetuksesi
taajuuden arvo.

Yli 7 dBi:n antennilla 22 dBm:n laite ylittää laillisen rajan, ellei
kaapelin ja suodattimen vaimennus kata eroa. Laske lähetystehoa vastaavasti.

Suuresta vahvistuksesta on hyötyä vain, kun tiedät, missä solmut ovat:
horisontin suunnassa toistimen ympärillä tai Yagilla yhdessä kaukaisessa
toistimessa. Kädessäsi oleva companion osoittaa joka suuntaan, joten sille
sopii parhaiten sen mukana tullut pienen vahvistuksen antenni.

## Miksi pystyyn {#vertical}

Antennit kuulevat toisiaan parhaiten, kun ne osoittavat samaan suuntaan.
Vaimennus kasvaa niiden välisen kulman mukaan: 45 astetta maksaa 3 dB eli
puolet signaalistasi. 90 asteessa, kun vaaka-antenni on pystyantennia
vasten, teoriassa mitään ei tule perille. Meshin antennit ovat pystyssä,
joten myös sinun antennisi on pystyssä. Tämä pätee myös pöydällä olevaan
companion-laitteeseen: jos lasket sen makuulleen, jokainen ympärilläsi oleva
solmu kuulee huonommin.

## Liittimet {#connectors}

Tilaa antenni, jossa on sama liitin kuin laitteessasi. Jokainen sovitin on
yksi tiivistettävä liitos lisää ja lisää signaalihäviötä.

- **SMA.** Kierteellinen, noin 6 mm leveä liitin. Useimpien laitteiden
  liittimessä on reikä keskellä, antennissa on tappi. Tällainen liitin
  vaimentaa noin 0.03 dB 868 MHz:llä.
- **RP-SMA.** Sama runko ja kierre kuin SMA:ssa, mutta tappi ja reikä ovat
  vaihtaneet paikkaa. Se näyttää SMA:lta mutta ei sovi siihen. Tarkista
  laitteesi liitin ennen kuin tilaat.
- **U.FL (IPEX).** Pieni painettava liitin suoraan piirilevyssä. Siitä
  kulkee lyhyt pigtail-kaapeli kotelon SMA-liittimeen. Se on mitoitettu 30
  liitäntäkertaan, joten liitä se kerran ja jätä paikalleen.
- **N.** Iso kierteellinen liitin lasikuituantenneissa ja paksussa
  kaapelissa. Se vaimentaa enintään 0.05 dB. Toistimeen tarvitset yhden
  sovittimen tai pigtail-kaapelin N-liittimestä laitteen SMA-liittimeen.

## Kaapelin vaimennus {#cable}

Kaapeli vie signaalia ennen kuin se lähtee antennista, molempiin suuntiin.
3 dB on puolet tehostasi. Valmistajien lukemat metriä kohden taajuuksilla
868–900 MHz:

| Kaapeli | Vaimennus metriä kohden | Vaimennus 5 m:llä |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metriä RG174:ää, ohutta pigtail-kaapelia, joka tulee monen laitteen
mukana, vie puolet tehostasi. Asenna laite antennin luo lyhyellä
pigtail-kaapelilla tai vedä siihen paksu kaapeli. Lisää summaan jokainen
reitillä oleva sovitin ja suodatin.

## Suodattimet {#filters}

Suodatin on radion ja antennin välissä. Se päästää läpi oman kaistasi ja
estää muut, joten lähellä oleva vahva lähetin ei tukahduta vastaanotinta.
Tarvitset suodattimen, kun solmu kuulee muiden lähettimien lähellä huonommin
kuin sen pitäisi. Tällainen solmu on esimerkiksi toistin mastossa, jossa on
matkapuhelinten tukiasemia. Suodatin vie signaalia molempiin suuntiin:
laske sen vaimennus kuten kaapelin.

| | SAW-suodatin | Onteloresonaattorisuodatin |
|---|---|---|
| Koko | Muutama millimetri, pienellä piirilevyllä | Metallikappale tai -putki |
| Hyvän suodattimen vaimennus | alle 2 dB | alle 1 dB |
| Hyvän suodattimen suurin tuloteho | 500 mW | useita watteja |

Esimerkiksi sysmocom cf866.5-kt30 on onteloresonaattorisuodatin
taajuuksille 863–870 MHz. Sen vaimennus on enintään 1.0 dB, ja se kestää
30 W. Se on tehty sisäkäyttöön, joten laita se mastossa tiiviiseen
koteloon.

Suodattimet eroavat paljon toisistaan, joten tarkista datalehti ennen
ostoa. Suodattimen nimellistulotehon täytyy ylittää lähetystehosi, ja sen
päästökaistan täytyy kattaa esiasetuksesi taajuus.

## Asennus {#mounting}

- **Katon reunan yläpuolelle.** Antenni tarvitsee esteettömän näkymän joka
  suuntaan, jota se palvelee. Jo muutama metri ympäröivien kattojen
  yläpuolella auttaa. Toistinoppaan kohdassa [Valitse paikka](/repeater-guide/#site)
  näytetään, miten tarkistat näkymän.
- **Kauas metallista.** Antennin vieressä olevat rännit, mastot, muut
  antennit ja peltikatot muuttavat sen säteilykuviota ja viritystä. Asenna
  antenni maston huipulle, ei sen kylkeen.
- **Pystyyn.** Käytä vesivaakaa, katso [Miksi pystyyn](#vertical).
- **Tippalenkki.** Anna kaapelin roikkua liittimen alapuolella ennen kuin
  se nousee ylös tai menee sisään. Silloin vesi tippuu pois eikä valu
  liitokseen.
- **Tiivistä jokainen ulkoliitin.** Vesi liittimessä kasvattaa vaimennusta
  ja syövyttää tappia. Tiivistä liitin sateelta ja tarkista tiiviste joka
  vuosi.
- **Salama.** Katolla oleva antenni on kohde. Kaapeliin asennettu
  kaasupurkaussuoja laukeaa ylijännitteessä ja ohjaa sen maahan. Noudata
  maadoituksessa toistinoppaan kohtaa [Laitteisto](/repeater-guide/#hardware)
  ja paikallisia määräyksiä.

## Laillisen rajan sisällä {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
Euroopassa MeshCore käyttää alikaistaa 869.40-869.65 MHz, ja efektiivinen
säteilyteho (e.r.p.) on enintään **500 mW**. Raja koskee sitä, mikä lähtee
antennista: antennin vahvistus lisää, kaapelin ja suodattimen vaimennus
vähentää. dBi:nä ilmoitettu vahvistus lasketaan 2.15 dB pienempänä, koska
raja mitataan suhteessa dipoliin.
{{< /callout >}}

5.8 dBi:n kollineaari 22 dBm:n laitteessa pysyy rajan sisällä. Sama
antenni vahvistimella varustetussa laitteessa ei pysy, ennen kuin lasket
lähetystehoa. Toistinoppaan kohdassa [Teho: e.r.p. ja antennisi](/repeater-guide/#erp)
on laskukaava ja 2 laskettua esimerkkiä.

## Tarkista antenni NanoVNA:lla {#nanovna}

NanoVNA on taskukokoinen vektoripiirianalysaattori. Sillä näet, mille
taajuudelle antenni on viritetty, joten tiedät sen ennen asennusta.
NanoVNA-H mittaa 1.5 GHz:iin asti, mikä kattaa 868 MHz:n.

1. Kalibroi se välille 800–950 MHz sarjan open-, short- ja load-osilla.
2. Liitä antenni sen sovittimen kautta, jota käytät solmussa. Pidä antenni
   pystyssä ja kaukana kehostasi ja pöydästä.
3. Lue SWR-käyrä (seisovan aallon suhde): se näyttää, kuinka paljon
   signaalia antenni heijastaa takaisin. Kuopan täytyy osua esiasetuksesi
   taajuudelle, joka on EU/UK (Narrow) -esiasetuksella 869.618 MHz. Jos
   kuoppa on satojen MHz:ien päässä, antenni on tehty toiselle kaistalle.

Neljännesaalto 868 MHz:llä on 86 mm (aallonpituus on 345 mm). Pelkästä
pituudesta et näe kaistaa, koska valmistajat taittavat ja kuormittavat
piiska-antenneja. NanoVNA näyttää sen.

## Lähteet {#sources}

- Kaapelin vaimennus: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  Huber+Suhner RG316 -datalehti,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  Times Microwave LMR-240- ja LMR-400-datalehdet,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antennit: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  Sirio SO 868-915-2 -datalehti,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Vahvistus pienempään tilaan puristettuna signaalina: [RF Cafe, antennien perusteet](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Liittimet: Rosenberger 32S102 (SMA)- ja 53S101 (N) -datalehdet,
  Hirose U.FL -luettelo.
- Suodattimet: sysmocom cf866.5-kt30 -tuotesivu,
  [Citel-kaasupurkaussuojat](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarisaatiovaimennus: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipolin vahvistus pituuden mukaan: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Aallonpituus: valon nopeus, [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Laillinen raja: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Annex 1, kaista h1.7. Loput lähteet ovat [toistinoppaassa](/repeater-guide/#legal).
