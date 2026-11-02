---
title: Urob sieť odolnou
lead: Je sieť vo tvojom okolí pomalá alebo plná smetí? Zisti príčinu, zapni na repeateri nastavenie, ktoré ju zastaví, a povedz to svojej miestnej skupine.
description: 'Záplavy a spam v sieti MeshCore: ako rozpoznáš jednotlivé druhy, ktoré nastavenie repeatera pomáha, ako záplavu uvidíš a ako nájdeš jej zdroj.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-11-02'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Prichádzajú správy neskoro alebo vôbec nie? Plní sa Public smeťami? To je
záplava: viac prevádzky, než sieť unesie, či už omylom, alebo zámerne.
Nájdi v tabuľkách nižšie to, čo vidíš. Každý riadok uvádza nastavenie,
ktoré to zastaví. Zapni ho na svojom repeateri, teda uzle, ktorý posúva
správy ďalej. Potom to povedz svojej [miestnej skupine](/community/), aby
to isté urobili aj repeatery okolo teba. Každý repeater, ktorý záplavu
zahodí, uvoľní vysielací čas pre všetkých ostatných.

## Záplavy omylom {#mistake}

Záplava omylom pochádza z uzla, ktorého majiteľ nevie, že ju spôsobuje. Skončí,
keď sa to dozvie. Advert v tabuľkách nižšie je pozdrav, ktorým sa uzol ohlasuje,
aby ho ostatní našli.

Nastavenia v tabuľkách vychádzajú z toho, čo robí firmvér. Nie každé z nich
už zastavilo záplavu v skutočnej sieti.

{{< callout type="warning" >}}
Niektoré nastavenia na tejto stránke vyžadujú firmvér DMC. Štandardný
**MeshCore** 1.18.0 má regióny, limity skokov `flood.max.*`, detekciu slučiek
a duty cycle. Paketový filter, teda pravidlá, ktorými tvoj repeater zahadzuje
smeti, prináša **firmvér DMC** od
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). To isté platí
pre duty-cycle gating a filter companionu. Táto stránka vychádza z DMC
1.18.0 dev buildu `ecfb2d4` z 19. októbra 2026. Na stránke
[paketový filter](/guides/filter/#firmware) zistíš, kde ho získaš.
{{< /callout >}}

| Čo vidíš | Čo to je | Čo pomáha |
| --- | --- | --- |
| Požiadavky na repeatery z jedného uzla, vo dne v noci, a sieť, ktorá zostáva pomalá celé dni | Domáca automatizácia alebo bot, ktorý sa repeaterov pýta na stav príliš často | `filter on`. Paketový filter potom prepustí 5 požiadaviek za minútu. Povedz to majiteľovi. |
| Každú minútu rovnaký druh správy na kanáli | Bot, ktorý posiela správy príliš často | [Zablokuj kanál](/guides/filter/#channel) alebo [spomaľ odosielateľa](/guides/filter/#sender). Povedz to majiteľovi. |
| Nečitateľné správy na Public a ďalších kanáloch | Uzol s pokazeným firmvérom alebo nesprávnymi nastaveniami rádia | `filter malformed on` ich na Public zahodí. Povedz to majiteľovi. |
| Advert jedného uzla každých pár minút | Uzol nastavený tak, že posiela adverty príliš často | `filter advert 24` prepustí advert každého uzla raz za deň. `set flood.max.advert 3` udrží adverty v rámci 3 skokov. |
| Správy zďaleka, s regiónmi, ktoré sem nepatria | Most, ktorý spája siete cez internet | `set flood.max.unscoped 1` a zaraď svoj repeater len do [regiónov, ktoré obsluhuje](/guides/settings/#traffic). |
| Tá istá správa prechádza znova a znova a ID tvojho repeatera je v jej ceste viackrát | Repeater, ktorý mení pakety a posúva ich ďalej, takže krúžia v slučke | Detekcia slučiek beží predvolene na `minimal`. `set loop.detect moderate` zahodí slučku skôr. |

## Zámerné záplavy {#purpose}

Niektoré záplavy sú spam: smeti, ktoré niekto posiela zámerne, aby upchal
sieť. Odosielateľ mení mená, kľúče a cesty, preto záplavu žiadne pravidlo
samo osebe nezastaví.

| Čo vidíš | Čo to je | Čo pomáha |
| --- | --- | --- |
| Veľa nových uzlov s náhodnými menami, každý s novým kľúčom | Falošné adverty | `filter rate 04 5 60` prepustí 5 advertov za minútu. `filter advert` nepomáha: každý advert prichádza z [nového kľúča](#forged). |
| Správy s nečitateľným textom od vymyslených odosielateľov, často s dátumom spred viac ako roka | Spam na kanáloch | `filter malformed on` ich na Public zahodí. `filter age 60` zahodí správy so starým dátumom na Public a na [sledovaných kanáloch](/guides/filter/#settings). |
| Až 200 priamych správ za minútu pre uzly, ktoré neexistujú, a žiadne potvrdenia späť | Záplava priamych správ | `filter rate 02 5 60`. Tvoja aplikácia tieto správy nezobrazí, observer áno. |
| Nárazy požiadaviek z jedného uzla na desiatky ďalších | Spam požiadaviek | S `filter on` paketový filter prepustí 5 požiadaviek za minútu. |
| Správa sa vráti o 10 až 20 minút, s takmer rovnakou cestou | Replay: kópia odoslaná znova | Repeater si pamätá posledných 160 paketov, ktoré videl, takže v rušnej sieti neskoršia kópia znova prejde. `filter age` zahodí skupinovú správu staršiu, než povolíš. |
| Správy z Public odoslané znova pod vymysleným odosielateľom, niekedy so starým dátumom | Echo spam | `filter age 60`. `filter malformed on` zahodí aj správu s dátumom, ktorý sa líši o viac ako týždeň. |
| Správa každých pár sekúnd na viacerých kanáloch, vždy pod novým menom, s bežnými otázkami | Vlna botov | `filter rate 05 10 60` a [zablokuj kanály](/guides/filter/#channel), ktoré sa vo tvojej oblasti nepoužívajú. Každé meno je nové, preto ho [pravidlá pre odosielateľov](#forged) nezachytia. |

## Čo zafungovalo {#worked}

Miestne skupiny zastavili záplavy týmito krokmi:

1. **Povedz to majiteľovi.** Záplava omylom skončí, keď sa o nej majiteľ
   dozvie. Pošli mu priateľskú správu.
2. **Nereaguj v sieti.** Odpoveď ukáže spamerovi, že jeho spam funguje.
3. **Požiadaj o observery.** Observer je uzol, ktorý cez MQTT hlási každý
   paket, ktorý počuje. Čím viac observerov je okolo teba, tým skôr uvidíš,
   kde záplava vstupuje do siete. Urob zo svojho repeatera observer pomocou
   [MQTT na observeri](/guides/mqtt/).
4. **Nájdi zdroj.** Observery určia oblasť, v ktorej je odosielateľ.
   Posledný kilometer musia ľudia prejsť pešo s rádiom. Pozri si časť
   [Nájdi zdroj](#source).
5. **Rozhýb svoju miestnu skupinu.** Jeden repeater so správnymi nastaveniami
   pomáha. Všetky repeatery v oblasti spolu záplavu zastavia. Tvoja
   [miestna skupina](/community/) zariadi, aby si nastavenie zapol každý
   majiteľ.

## Vymyslení odosielatelia a cesty {#forged}

Tieto časti paketu píše odosielateľ a nič ich nekontroluje:

- **Meno odosielateľa.** V správe na kanáli je meno súčasťou textu. Každý,
  kto má kľúč kanála, môže napísať akékoľvek meno.
- **Začiatok cesty.** Každý repeater pridá na koniec cesty svoje ID. ID,
  ktoré tam už boli, nič nekontroluje, takže odosielateľ môže cestu začať
  vymyslenými ID. Koniec cesty je skutočný.

{{< forged-path >}}

Preto `filter sender` a `filter path` zastavia odosielateľa len dovtedy, kým
si nezmení meno alebo cestu. [Blokovanie cesty](/guides/filter/#path) zahodí
aj skutočnú prevádzku repeatera, ktorého ID v nej je. Limity rýchlosti,
limity skokov, kontroly veku a poškodených správ, blokovanie kanálov, regióny
a duty cycle fungujú ďalej.

## Nastavenia pre každú záplavu {#always}

Tieto nastavenia platia, nech sieť zaplavuje čokoľvek:

- **Duty cycle na 10%.** Tvoj repeater potom nikdy nevysiela viac, než dovoľuje
  zákon, nech prichádza čokoľvek. Viac nájdeš v
  [príručke k repeateru](/repeater-guide/#duty-cycle).
- **Regióny a limity skokov.** Región je oblasť, v ktorej správa zostáva.
  Repeater posúva ďalej len správy v regiónoch, ktoré má nastavené, a
  `flood.max.*` drží prevádzku nablízku. Oboje nájdeš v časti
  [Obmedz prevádzku](/guides/settings/#traffic).
- **Paketový filter pre rušný repeater.**
  [Pripravené nastavenia](/guides/filter/#busy) znížia počet skupinových správ
  a advertov na polovicu. Najprv ich vyskúšaj v režime
  [dry-run](/guides/filter/#dryrun): ten len počíta, čo by zahodil.
- **Filter companionu vo firmvéri DMC.** Tvoj companion, teda uzol, z ktorého
  posielaš správy, drží smeti mimo tvojej aplikácie. Skryje poškodené a staré
  správy aj správy od repeatera, odosielateľa alebo so slovom, ktoré
  zablokuješ. Pravidlo pre odosielateľa alebo slovo skryje správu len tebe,
  ostatní ju dostanú aj tak.

### Duty-cycle gating {#gate}

Vo firmvéri DMC môže tvoj repeater pri veľkej záťaži uprednostniť vlastný
región. Keď vysielal viac ako 35% poslednej minúty, prestane posúvať správy
bez regiónu. Ak záťaž trvá, zahodí ako ďalší najširší región, vždy po jednej
úrovni. Vlastný región prejde vždy. Funguje to len vtedy, keď máš na repeateri
nastavené regióny. Zapni to a skontroluj:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

To, čo takto zahodí, sa v `filter stats` nezobrazí. Keď sa repeater opäť
upokojí, regióny sa vrátia, najprv tie najvnútornejšie.

## Ako uvidíš záplavu {#see}

Tvoja aplikácia ukazuje len to, čo sa dostane k tebe. Záplavu priamych správ
pre uzly, ktoré neexistujú, počuje len observer. Každý observer posiela hlásenia
do [MeshCore Analyzera](https://meshcore-analyzer.eu/), kde ich môže vidieť
každý. Urob zo svojho repeatera observer pomocou
[MQTT na observeri](/guides/mqtt/).

V Analyzeri si pozri všetky kópie jedného paketu. Jeho cesta zvyčajne ukáže,
odkiaľ prišiel. Odosielateľ záplavy môže cestu začať [vymyslenými ID](#forged),
takže prvé ID ti nič nepovedia. Každá kópia však nesie ten istý vymyslený
začiatok. Kópia s najkratšou cestou prešla cez najmenej skutočných repeaterov,
takže ju niekto počul najbližšie k odosielateľovi.

{{< copies >}}

Na svojom repeateri uvidíš cez `filter stats`, čo paketový filter zahodil.
`filter stats top` ukáže prvý bajt ID uzlov, ktoré stoja za väčšinou
zahodených paketov. Tento bajt má veľa uzlov, takže hľadanie zúži, ale
odosielateľa neurčí.

## Nájdi zdroj {#source}

Keď sa záplava stále vracia:

1. **Sleduj cesty.** Cestu čítaj od konca: posledné ID patria repeaterom,
   ktorými záplava prešla. Prvé skutočné ID je blízko zdroja. ID pred
   ním môžu byť [vymyslené](#forged).
2. **Zúž oblasť.** Viacero observerov, ktoré počujú ten istý paket, určí
   oblasť, v ktorej je odosielateľ.
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) ju vypočíta z
   repeaterov, ktoré paket počuli.
3. **Prejdi posledný kilometer pešo.** Repeatery počujú zdroj len na hranici
   svojho dosahu, preto poslednú časť musia ľudia prejsť pešo.
   [Mesh-Hunter](https://mesh-hunter.eu/) sa spáruje s tvojím companionom a
   každý paket, ktorý počuje, zaznamená s tvojou GPS polohou. Keď ide naraz
   viac ľudí, nájdu zdroj skôr.
4. **Povedz to svojej [miestnej skupine](/community/).** Vidí väčšiu časť
   siete, rozhoduje, čo bude ďalej, a kontaktuje toho, kto zaplavuje sieť
   zámerne.

## Doplň, čo si videl {#add}

Zasiahla ťa záplava, ktorá v týchto tabuľkách nie je? Zastavilo niektoré
nastavenie záplavu? Napíš nám na [Discord](https://discord.meshcore-info.eu/),
čo si videl a čo si zapol. Doplníme to na stránku.
