---
title: Padari tīklu noturīgu
lead: Vai tīkls tavā apkārtnē ir lēns vai pilns ar atkritumiem? Noskaidro cēloni, ieslēdz retranslatorā iestatījumu, kas to aptur, un pastāsti vietējai grupai.
description: 'Pārpludinājumi un spams MeshCore tīklā: kā atpazīt katru veidu, kurš retranslatora iestatījums palīdz, kā pamanīt pārpludinājumu un atrast tā avotu.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-11-02'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Vai ziņas pienāk vēlu vai nepienāk vispār? Vai Public pildās ar atkritumiem? Tas ir
pārpludinājums: vairāk datplūsmas, nekā tīkls spēj pārnest, un to kāds sūta kļūdas
pēc vai ar nodomu. Atrodi to, ko redzi, tālāk dotajās tabulās. Katrā rindā ir nosaukts iestatījums,
kas to aptur. Ieslēdz to savā retranslatorā, mezglā, kas pārsūta ziņas tālāk. Pēc tam
pastāsti par to savai [vietējai grupai](/community/), lai apkārtējie retranslatori
darītu to pašu. Katrs retranslators, kas atmet pārpludinājumu, atstāj ēterlaiku
visiem pārējiem.

## Pārpludinājumi kļūdas pēc {#mistake}

Pārpludinājumu kļūdas pēc rada mezgls, kura īpašnieks par to nezina. Tas beidzas,
tiklīdz īpašnieks to uzzina. Tālāk tabulās pieteikums (advert) ir sveiciens, ko
mezgls sūta, lai citi to varētu atrast.

Tabulās minētie iestatījumi balstās uz to, ko dara programmaparatūra. Ne visi no
tiem jau ir apturējuši pārpludinājumu īstā tīklā.

{{< callout type="warning" >}}
Dažiem iestatījumiem šajā lapā vajadzīga DMC programmaparatūra. Standarta **MeshCore**
1.18.0 ietver reģionus, lēcienu ierobežojumus `flood.max.*`, cilpu noteikšanu un darba
ciklu (duty cycle). Pakešu filtrs ir noteikumi, ar kuriem tavs retranslators atmet
atkritumus. Tas ir pieejams **DMC programmaparatūrā** no
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Tāpat tur ir darba cikla
ierobežošana un kompanjona filtrs. Šī lapa atbilst DMC 1.18.0 izstrādes būvējumam
`ecfb2d4` no 2026. gada 19. oktobra. Lapā par
[pakešu filtru](/guides/filter/#firmware) ir norādīts, kur to iegūt.
{{< /callout >}}

| Ko tu redzi | Kas tas ir | Kas palīdz |
| --- | --- | --- |
| Viena mezgla pieprasījumi retranslatoriem dienu un nakti, un tīkls vairākas dienas paliek lēns | Mājas automatizācija vai bots, kas pārāk bieži prasa retranslatoriem statusu | `filter on`. Pēc tam pakešu filtrs pārsūta 5 pieprasījumus minūtē. Pastāsti īpašniekam. |
| Kanālā katru minūti parādās viena veida ziņa | Bots, kas publicē pārāk bieži | [Bloķē kanālu](/guides/filter/#channel) vai [palēnini sūtītāju](/guides/filter/#sender). Pastāsti īpašniekam. |
| Nesalasāmas ziņas kanālā Public un citos kanālos | Mezgls ar bojātu programmaparatūru vai nepareiziem radio iestatījumiem | `filter malformed on` atmet tās kanālā Public. Pastāsti īpašniekam. |
| Viena mezgla pieteikums ik pēc dažām minūtēm | Mezgls, kas iestatīts sūtīt pieteikumus pārāk bieži | `filter advert 24` pārsūta katra mezgla pieteikumu reizi dienā. `set flood.max.advert 3` notur pieteikumus 3 lēcienu robežās. |
| Ziņas no tālienes ar reģioniem, kas nav no šejienes | Tilts, kas savieno tīklus caur internetu | `set flood.max.unscoped 1` un iekļauj retranslatoru tikai tajos [reģionos, kurus tas apkalpo](/guides/settings/#traffic). |
| Tā pati ziņa iet cauri atkal un atkal, un tās ceļā tava retranslatora ID ir vairāk nekā vienreiz | Retranslators, kas maina paketes un pārsūta tās tālāk, tāpēc tās nonāk cilpā | Cilpu noteikšana pēc noklusējuma darbojas līmenī `minimal`. `set loop.detect moderate` atmet cilpu ātrāk. |

## Pārpludinājumi ar nodomu {#purpose}

Daži pārpludinājumi ir spams: atkritumi, ko kāds sūta ar nodomu aizsprostot tīklu.
Sūtītājs maina vārdus, atslēgas un ceļus, tāpēc neviens atsevišķs noteikums
pārpludinājumu neaptur.

| Ko tu redzi | Kas tas ir | Kas palīdz |
| --- | --- | --- |
| Daudz jaunu mezglu ar nejaušiem vārdiem, katram sava jauna atslēga | Viltoti pieteikumi | `filter rate 04 5 60` pārsūta 5 pieteikumus minūtē. `filter advert` nepalīdz: katrs pieteikums nāk no [jaunas atslēgas](#forged). |
| Ziņas ar nesalasāmu tekstu no izdomātiem sūtītājiem, bieži ar datumu, kas vecāks par gadu | Kanālu spams | `filter malformed on` atmet tās kanālā Public. `filter age 60` atmet ziņas ar vecu datumu kanālā Public un [uzraudzītajos kanālos](/guides/filter/#settings). |
| Līdz 200 tiešajām ziņām minūtē neesošiem mezgliem, un apstiprinājumi neatnāk | Tiešo ziņu pārpludinājums | `filter rate 02 5 60`. Tava lietotne šīs ziņas nerāda, bet novērotājs tās rāda. |
| Viena mezgla pieprasījumu uzliesmojumi desmitiem citu mezglu | Pieprasījumu spams | Ar `filter on` pakešu filtrs pārsūta 5 pieprasījumus minūtē. |
| Ziņa atgriežas pēc 10 līdz 20 minūtēm gandrīz pa to pašu ceļu | Atkārtošana: kāds vēlreiz nosūta kopiju | Retranslators atceras pēdējās 160 redzētās paketes, tāpēc noslogotā tīklā vēlāka kopija atkal iet cauri. `filter age` atmet grupas ziņu, kas ir vecāka, nekā tu atļauj. |
| Ziņas no kanāla Public, kas nosūtītas vēlreiz ar izdomātu sūtītāju, dažreiz ar vecu datumu | Atbalss spams | `filter age 60`. `filter malformed on` atmet arī ziņu, kuras datums atšķiras vairāk nekā par nedēļu. |
| Ik pēc dažām sekundēm vairākos kanālos parādās ziņa ar parastu jautājumu, katra ar jaunu vārdu | Botu vilnis | `filter rate 05 10 60` un [bloķē kanālus](/guides/filter/#channel), ko tavā apkārtnē neizmanto. Katrs vārds ir jauns, tāpēc [sūtītāju noteikumi](#forged) to nenotver. |

## Kas ir palīdzējis {#worked}

Vietējās grupas ir apturējušas pārpludinājumus ar šādiem soļiem:

1. **Pastāsti īpašniekam.** Pārpludinājums kļūdas pēc beidzas, tiklīdz īpašnieks par to
   uzzina. Uzraksti viņam draudzīgu ziņu.
2. **Nereaģē tīklā.** Atbilde parāda spameram, ka spams darbojas.
3. **Palūdz ierīkot novērotājus.** Novērotājs ir mezgls, kas pa MQTT ziņo par katru dzirdēto
   paketi. Jo vairāk novērotāju ir tev apkārt, jo ātrāk tu redzi, kur pārpludinājums
   ienāk tīklā. Pārvērt savu retranslatoru par novērotāju ar
   [MQTT novērotājā](/guides/mqtt/).
4. **Atrodi avotu.** Novērotāji parāda apgabalu, kurā atrodas sūtītājs. Pēdējo kilometru
   cilvēki iet kājām ar radio rokās. Skati sadaļu
   [Atrodi avotu](#source).
5. **Iekustini vietējo grupu.** Viens retranslators ar pareiziem iestatījumiem palīdz.
   Visi apgabala retranslatori kopā aptur pārpludinājumu. Tava
   [vietējā grupa](/community/) panāk, ka katrs īpašnieks šo iestatījumu ieslēdz.

## Izdomāti sūtītāji un ceļi {#forged}

Šīs paketes daļas raksta sūtītājs, un nekas tās nepārbauda:

- **Sūtītāja vārds.** Kanāla ziņā vārds ir daļa no teksta. Ikviens, kam ir kanāla
  atslēga, var ierakstīt jebkuru vārdu.
- **Ceļa sākums.** Katrs retranslators pievieno savu ID ceļa beigās. Nekas nepārbauda
  ID, kas tur jau bija, tāpēc sūtītājs var sākt ceļu ar izdomātiem ID. Ceļa beigas ir
  īstas.

{{< forged-path >}}

Tāpēc `filter sender` un `filter path` aptur sūtītāju tikai līdz brīdim, kad viņš
nomaina vārdu vai ceļu. [Ceļa bloķēšana](/guides/filter/#path) atmet arī tā retranslatora
īsto datplūsmu, kura ID tajā ir minēts. Ātruma ierobežojumi, lēcienu ierobežojumi,
vecuma un bojātu ziņu pārbaudes, kanālu bloķēšana, reģioni un darba cikls turpina
darboties.

## Iestatījumi pret jebkuru pārpludinājumu {#always}

Šie iestatījumi darbojas neatkarīgi no tā, kas pārpludina tīklu:

- **Darba cikls 10%.** Tad tavs retranslators nekad neraida vairāk, nekā atļauj likums,
  lai arī kas ienāktu. Par to raksta
  [retranslatoru ceļvedī](/repeater-guide/#duty-cycle).
- **Reģioni un lēcienu ierobežojumi.** Reģions ir apgabals, kurā ziņa paliek.
  Retranslators pārsūta tikai to reģionu ziņas, kuri tam ir iestatīti, un `flood.max.*`
  notur datplūsmu tuvumā. Abi ir aprakstīti sadaļā
  [Samazini datplūsmu](/guides/settings/#traffic).
- **Pakešu filtrs noslogotam retranslatoram.** [Gatavie iestatījumi](/guides/filter/#busy)
  uz pusi samazina grupas ziņas un pieteikumus. Vispirms izmēģini tos
  [dry-run režīmā](/guides/filter/#dryrun): tas tikai saskaita, ko atmestu.
- **Kompanjona filtrs DMC programmaparatūrā.** Tavs kompanjons, mezgls, no kura tu sūti
  ziņas, notur atkritumus ārpus tavas lietotnes. Tas paslēpj bojātas un vecas ziņas,
  kā arī ziņas no retranslatora, sūtītāja vai ar vārdu, ko tu bloķē. Sūtītāja vai vārda
  noteikums paslēpj ziņu tikai no tevis: citi to joprojām saņem.

### Darba cikla ierobežošana {#gate}

DMC programmaparatūrā tavs retranslators noslodzes laikā var dot prioritāti savam
reģionam. Kad tas pēdējā minūtē ir raidījis vairāk nekā 35% laika, tas pārtrauc
pārsūtīt ziņas bez reģiona. Ja noslodze saglabājas, tas pēc tam atmet plašāko reģionu,
pa vienam līmenim. Retranslatora paša reģiona ziņas vienmēr iet cauri. Tas darbojas tikai tad, ja
tavā retranslatorā ir iestatīti reģioni. Ieslēdz to un pārbaudi:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

To, ko šī funkcija atmet, `filter stats` nerāda. Kad retranslatora noslodze atkal
samazinās, reģioni atgriežas, sākot ar iekšējāko.

## Pamani pārpludinājumu {#see}

Tava lietotne rāda tikai to, kas sasniedz tevi. Tiešo ziņu pārpludinājumu neesošiem
mezgliem dzird tikai novērotājs. Katrs novērotājs ziņo vietnei
[MeshCore Analyzer](https://meshcore-analyzer.eu/), kur to var redzēt ikviens. Pārvērt
savu retranslatoru par novērotāju ar [MQTT novērotājā](/guides/mqtt/).

Analyzer vietnē apskati katru vienas paketes kopiju. Tās ceļš parasti parāda, no kurienes
tā nākusi. Pārpludinātājs var sākt ceļu ar [izdomātiem ID](#forged), tāpēc pirmie ID
neko nepasaka. Taču katrai kopijai ir tas pats izdomātais sākums. Kopija ar īsāko ceļu ir
gājusi caur vismazāk īstiem retranslatoriem, tāpēc tā dzirdēta vistuvāk sūtītājam.

{{< copies >}}

Savā retranslatorā ar `filter stats` vari redzēt, ko pakešu filtrs ir atmetis.
`filter stats top` parāda to mezglu ID pirmo baitu, kuru dēļ atmests visvairāk.
Daudziem mezgliem šis baits ir vienāds, tāpēc tas sašaurina meklēšanu, taču sūtītāju
nenosauc.

## Atrodi avotu {#source}

Kad pārpludinājums atgriežas atkal un atkal:

1. **Seko ceļiem.** Lasi ceļu no beigām: pēdējie ID ir retranslatori, caur kuriem
   pārpludinājums gājis. Agrākais īstais ID ir avota tuvumā. ID pirms tā var būt
   [izdomāti](#forged).
2. **Sašaurini apgabalu.** Vairāki novērotāji, kas dzird vienu paketi, parāda apgabalu,
   kurā atrodas sūtītājs. [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) to
   aprēķina pēc retranslatoriem, kas paketi dzirdējuši.
3. **Noej pēdējo kilometru.** Retranslatori dzird avotu tikai sava darbības rādiusa malā,
   tāpēc pēdējo posmu cilvēki iet kājām.
   [Mesh-Hunter](https://mesh-hunter.eu/) savienojas pārī ar tavu kompanjonu un reģistrē
   katru dzirdēto paketi kopā ar tavu GPS atrašanās vietu. Vairāki cilvēki, kas iet
   vienlaikus, atrod avotu ātrāk.
4. **Pastāsti savai [vietējai grupai](/community/).** Tā redz lielāku tīkla daļu, izlemj,
   kas notiek tālāk, un sazinās ar to, kurš pārpludina ar nodomu.

## Pievieno to, ko redzēji {#add}

Vai tevi skāra pārpludinājums, kura nav šajās tabulās? Vai kāds iestatījums to apturēja?
Pastāsti mums [Discord](https://discord.meshcore-info.eu/): ko tu redzēji un ko ieslēdzi.
Mēs to pievienosim šai lapai.
