---
title: Kom igång
lead: Från ett nytt kort till ditt första meddelande i meshen. Du behöver ett LoRa-kort, en dator med Chrome eller Edge och en telefon eller laptop för appen.
description: Flasha MeshCore från webbläsaren, parkoppla appen, välj den radioförinställning som ditt område använder, skicka ditt första meddelande och gå med i din lokala kanal.
eyebrow: 6 steg · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-10-31'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Stegen utgår från MeshCore-firmware v1.18.0 och de officiella verktygen från
oktober 2026. Menynamnen i appen kan skilja sig lite mellan versioner.

## 1. Välj en enhet {#device}

Alla kort på [enhetssidan](/devices/) som anger companion fungerar. Som din
första nod väljer du en *companion*: radion du skickar meddelanden från. Du
parkopplar den med telefonen eller laptopen via Bluetooth eller USB. Du kan
också välja en med egen skärm och eget tangentbord som fungerar fristående.

Köp 868 MHz-versionen. Den medföljande antennen räcker. I
[antennguiden](/guides/antenna/) ser du hur du kontrollerar en antenn.

{{< callout type="warning" >}}
Montera antennen innan du slår på radion. En LoRa-radio som sänder utan
antenn kan skada sitt eget chip.
{{< /callout >}}

## 2. Flasha firmware {#flash}

1. Anslut enheten till datorn med en USB-kabel som klarar dataöverföring.
2. Öppna webbflashern på [flasher.meshcore.io](https://flasher.meshcore.io)
   i Chrome eller Edge. Den använder Web Serial, som andra webbläsare saknar.
3. Välj din enhet och sedan firmware för **Companion** med **Bluetooth** (eller
   USB, om du bara ska använda den med en kabel till datorn).
4. Flasha. Vissa kort måste först sättas i uppdateringsläge. Flashern visar
   hur du gör.

Använd *erase* bara när du vill börja om från början. En radering tar bort
enhetens identitet och dina kontakter. Vid senare uppdateringar flashar du utan
att radera. Om du vill behålla din identitet vid en radering exporterar du först
companionens privata nyckel från appen och importerar den efteråt.

## 3. Installera appen {#app}

Den officiella MeshCore-appen finns för Android, iOS, Windows och macOS. På
[meshcore.io](https://meshcore.io) hittar du länkar till alla versioner. Det
finns också en webbapp på [app.meshcore.nz](https://app.meshcore.nz) som
körs i Chrome eller Edge på en dator.

## 4. Parkoppla din nod {#pair}

Slå på noden, öppna appen och anslut till noden via Bluetooth. När appen
frågar efter en PIN-kod:

- en nod **med** skärm visar en PIN-kod, och du skriver in den;
- en nod **utan** skärm använder `123456`.

Om parkopplingen misslyckas tar du bort enheten i telefonens
Bluetooth-inställningar och försöker igen. Ge sedan noden ett namn. Andra
ser namnet, så använd inte ditt fullständiga namn eller din adress om du inte
vill det.

## 5. Välj ditt områdes radioförinställning {#preset}

Alla radior i ett område använder samma frekvens och inställningar. Annars
hör de inte varandra. Välj den förinställning som ditt område använder i
appens radioinställningar. Utanför områdena nedan använder Europa
**EU/UK (Narrow)**. Nederländerna, Tjeckien, Ungern, Slovakien, Portugal och
Schweiz har egna, och Limburg i Nederländerna har en variant:

{{< presets >}}

Erbjuder din enhet inte ditt områdes förinställning? Ange då de 4 värdena från
tabellen för hand i appens radioinställningar: frekvens, bandbredd, spreading
factor och coding rate. En nod med andra värden hör inte meshen.

Osäker? Din [lokala grupp](/community/) vet vilken förinställning ditt område
använder. Appen hämtar listan från MeshCore-projektet, så en ny förinställning
kräver ingen uppdatering av appen.

## 6. Säg hej {#hello}

1. **Presentera dig.** Skicka en *advert* från appen. En advert av typen
   "flood" går vidare via repeatrarna (noder som skickar meddelanden vidare).
   Då kan alla i meshen lägga till dig.
   En companion presenterar sig aldrig automatiskt.
2. **Hitta andra.** Andra dyker upp bland dina kontakter när deras adverts når
   dig. Repeatrar skickar som standard en flood-advert var 47:e timme. Det kan
   alltså ta 2 dagar innan din lista fylls.
3. **Skicka ett meddelande.** Öppna en kontakt och skriv. Det första
   meddelandet sprids med flood genom nätet. Mottagaren skickar tillbaka vilken
   väg det tog, och senare meddelanden följer den vägen.
4. **Gå med i kanaler.** Kanalen **Public** är redan inställd. Allt du skriver
   där når alla i meshen. Lägg till din regions *hashtag-kanal* (ett namn som
   börjar med `#`) genom att skriva in namnet. Din
   [lokala grupp](/community/) berättar vilka kanaler som är aktiva.

## När något inte fungerar {#troubleshooting}

**Appen hittar inte min enhet via Bluetooth.**
Troligen flashade du USB-versionen av companion. Flasha igen och välj
Bluetooth-versionen. På Heltec V3 har den lilla inbyggda Bluetooth-antennen
kort räckvidd. Håll telefonen nära.

**Parkopplingen misslyckas hela tiden.**
Ta bort enheten i telefonens Bluetooth-inställningar och starta om Bluetooth.
Parkoppla sedan igen med PIN-koden på skärmen eller `123456`.

**Ingen dyker upp bland mina kontakter.**
Kontrollera att din förinställning stämmer med ditt område. Skicka en
flood-advert. Finns ingen repeater inom räckhåll hör du bara radior i närheten.
På [kartsidan](/map/) ser du var repeatrarna finns.

**En kontakt visas som "senast sedd" för flera dagar sedan fast hen är aktiv.**
En av de två noderna har fel tid. En companion hämtar tiden från din telefon.
Repeatrar och room servers (noder som sparar meddelanden åt en grupp) behöver
få tiden inställd av sin ägare.

**Ett direktmeddelande kommer aldrig fram.**
Du och den andra personen behöver ha varandra som kontakter. En nod kastar
meddelanden från någon den inte känner till, utan att avsändaren får veta det.
Skicka en flood-advert och be den andra personen skicka en också. Kontrollera
i appen att den lägger till nya kontakter automatiskt. Den lägger bara till
noder inom sin hoppgräns.

**Gamla kontakter fungerar, nya får aldrig kontakt.**
Ett första meddelande skickas med flood. En repeater skickar det bara vidare
om den har meddelandets region. Senare meddelanden följer en inlärd väg, och
där stoppar ingen regionkontroll dem. Fråga din [lokala grupp](/community/)
vilka regioner repeatrarna runt dig har. Kontrollera också
[inställningarna för ditt område](/guides/settings/#traffic).

**Appen ansluter inte längre till din companion.**
Vissa kort har en användarknapp, till exempel några RAK-kort och Heltec T114.
Håll in den under de första 8 sekunderna efter att kortet startat. Då öppnar
companionen en räddningskonsol via USB. I konsolen på
[flasher.meshcore.io](https://flasher.meshcore.io) ställer du in en ny
Bluetooth-PIN med `set pin <pin>`, och med `erase` raderar du enheten.

**Flashern kan inte öppna serieporten i Linux.**
Din användare behöver åtkomst till porten, till exempel med
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, eller medlemskap i gruppen
`dialout`.

**Något annat.**
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
tar upp många fler problem.
