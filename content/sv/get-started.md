---
title: Kom igång
lead: Från ett nytt kort till ditt första meddelande på meshen. Du behöver ett LoRa-kort, en dator med Chrome eller Edge, och en telefon eller bärbar dator för appen.
description: Flasha MeshCore från webbläsaren, parkoppla appen, välj den radioförinställning ditt område använder, skicka ditt första meddelande och gå med i din lokala kanal.
eyebrow: 6 steg · MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '68c89544'
  seeded: '2026-10-26'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', '36a3eba3', '6da9fd7a', 'cb5fb72e', '89626504', 'a419ce79', 'aa273b20']
---

De här stegen följer MeshCore-firmware v1.18.0 och de officiella verktygen från
oktober 2026. Menynamnen i appen kan skilja sig lite mellan versioner.

## 1. Välj en enhet {#device}

Alla kort på [enhetssidan](/devices/) som är märkta companion fungerar. Till
din första nod väljer du en *companion*: radion du skickar meddelanden från.
Parkoppla den med din telefon eller bärbara dator via Bluetooth eller USB,
eller välj en med egen skärm och eget tangentbord som fungerar på egen hand.

Skaffa versionen för 868 MHz. Antennen som följer med duger; i
[antennguiden](/guides/antenna/) ser du hur du kontrollerar en antenn.

{{< callout type="warning" >}}
Sätt fast antennen innan du slår på radion. En LoRa-radio som sänder utan
antenn kan skada sitt eget chip.
{{< /callout >}}

## 2. Flasha firmwaren {#flash}

1. Anslut enheten till datorn med en USB-datakabel.
2. Öppna webbflashern på [flasher.meshcore.io](https://flasher.meshcore.io)
   i Chrome eller Edge. Den använder Web Serial, som andra webbläsare saknar.
3. Välj din enhet och sedan firmwaren **Companion** för **Bluetooth** (eller
   USB, om du bara ska använda den med en datorkabel).
4. Flasha. Vissa kort går först in i uppdateringsläge; flashern visar dig
   hur.

Använd *erase* bara för en helt ny start: radering tar bort enhetens identitet
och dina kontakter. Vid senare uppdateringar flashar du utan att radera.

## 3. Installera appen {#app}

Den officiella MeshCore-appen finns för Android, iOS, Windows och macOS;
[meshcore.io](https://meshcore.io) länkar till alla versioner. Det finns också
en webbapp på [app.meshcore.nz](https://app.meshcore.nz) som körs i Chrome
eller Edge på en dator.

## 4. Parkoppla din nod {#pair}

Slå på noden, öppna appen och anslut till den via Bluetooth. När appen ber om
en PIN-kod:

- en nod **med** skärm visar en PIN-kod; skriv in den;
- en nod **utan** skärm använder `123456`.

Om parkopplingen misslyckas tar du bort enheten i telefonens
Bluetooth-inställningar och försöker igen. Ge sedan noden ett namn. Andra ser
det här namnet, så använd inte ditt fullständiga namn eller din adress om du
inte vill det.

## 5. Välj radioförinställningen för ditt område {#preset}

Alla radior i ett område använder samma frekvens och inställningar, annars hör
de inte varandra. I appens radioinställningar väljer du den förinställning
ditt område använder. Utanför områdena nedan använder Europa **EU/UK
(Narrow)**. Nederländerna, Tjeckien, Ungern, Slovakien, Portugal och Schweiz
använder egna, och Limburg i Nederländerna har en variant:

{{< presets >}}

Osäker? Din [lokala grupp](/community/) vet vilken förinställning ditt område
använder. Appen hämtar listan från MeshCore-projektet, så en ny förinställning
kräver ingen appuppdatering.

## 6. Säg hej {#hello}

1. **Annonsera dig.** Skicka en *advert* från appen. En advert av typen
   "flood" går via repeatrarna (noder som skickar meddelanden vidare), så att
   alla på meshen kan lägga till dig.
   Companions annonserar sig aldrig automatiskt.
2. **Hitta andra.** Personer dyker upp bland dina kontakter när deras adverts
   når dig. Repeatrar skickar som standard en flood-advert var 47:e timme, så
   det kan ta 2 dagar innan listan fylls.
3. **Skicka ett meddelande.** Öppna en kontakt och skriv. Det första
   meddelandet floodar nätet; mottagaren rapporterar tillbaka vägen det tog,
   och senare meddelanden följer den vägen.
4. **Gå med i kanaler.** Kanalen **Public** är redan inställd; allt du skriver
   där når alla på meshen. Lägg till din regions *hashtagkanal* (ett namn som
   börjar med `#`) genom att skriva in namnet. Din
   [lokala grupp](/community/) berättar vilka kanaler som är aktiva.

## När något inte fungerar {#troubleshooting}

**Appen hittar inte min enhet via Bluetooth.**
Du har troligen flashat USB-companionen. Flasha igen och välj
Bluetooth-versionen. På Heltec V3 har den lilla inbyggda Bluetooth-antennen
kort räckvidd; håll telefonen nära.

**Parkopplingen misslyckas hela tiden.**
Ta bort enheten i telefonens Bluetooth-inställningar, starta om Bluetooth och
parkoppla igen med PIN-koden på skärmen eller `123456`.

**Ingen dyker upp bland mina kontakter.**
Kontrollera att din förinställning stämmer med ditt område. Skicka en
flood-advert. Om ingen repeater finns inom räckhåll hör du bara radior i
närheten; på [kartsidan](/map/) ser du var repeatrarna finns.

**En kontakt visar "senast sedd" för flera dagar sedan fast den är aktiv.**
En av de två noderna har fel tid. En companion tar tiden från din telefon;
repeatrar och room servers (noder som lagrar meddelanden åt en grupp) behöver
få tiden inställd av sin ägare.

**Flashern kan inte öppna serieporten i Linux.**
Din användare behöver åtkomst till porten, till exempel
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, eller medlemskap i gruppen
`dialout`.

**Något annat.**
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
tar upp många fler problem.
