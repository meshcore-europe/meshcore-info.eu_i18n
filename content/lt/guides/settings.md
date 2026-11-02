---
title: Rekomenduojami nustatymai
layout: settings
lead: Radijo profilis, kurį naudoja tavo vietovė, ir nustatymai, kuriuos pakeitė tavo kaimynai. Pasirink šalį, nustatyk profilį ir nukopijuok komandas.
description: MeshCore radijo profilis pagal Europos vietoves, kartotuvų ir kompanionų nustatymai, kuriuos vietos grupės pakeitė, ir jų komandos.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-11-02'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Kiekviena toliau nurodyta vietovė naudoja savo radijo profilį arba pakeičia kelis
numatytuosius MeshCore nustatymus. Visi čia neišvardyti nustatymai lieka numatytieji,
todėl keiti tik tai, ką pakeitė tavo vietovė. Kartotuvas perduoda žinutes visiems;
kompanionas yra mazgas, iš kurio rašai žinutes. Jį susieji su telefonu ar nešiojamuoju
kompiuteriu per Bluetooth arba USB, arba naudoji jo paties ekraną.

[Kartotuvo vadove](/repeater-guide/#config) rasi, kaip pasiekti kartotuvo komandų eilutę.
Šios svetainės [nuosekliojoje konsolėje](/firmware/console/) komandas gali įvesti pats.
Prie kiekvienos vietovės jos nustatymus gali nusiųsti ir per USB. Kartotuvo vadove
taip pat rasi 868 MHz juostos [teisinius apribojimus](/repeater-guide/#legal).

## Mažink radijo srautą {#traffic}

Šie nustatymai galioja visoms vietovėms. Kiekvienas kartotuvas perduoda toliau kiekvieną
išgirstą flood žinutę. Viena tavo žinutė kainuoja vieną perdavimą ir dar po vieną kiekvienam
ją išgirdusiam kartotuvui. Kai darbo ciklas yra 10%, kartotuvas per valandą gali išsiųsti
apie 680 paketų, ir šiuo kiekiu dalijasi visi aplinkiniai. Žinutė, keliaujanti toliau,
nei reikia, išnaudoja dalį šio kiekio.

**Siųsk į mažiausią regioną, kuris pasiekia žmones, kuriems rašai.**
Regionai įeina vienas į kitą: šalis, provincija, vietos grupė. Kiekvienas turi savo
kodą, pavyzdžiui, `nl`, `nl-ov` ir `nl-ov-zwo`. Žinutė, skirta `nl-ov-zwo`, lieka
tos grupės kartotuvuose. Kartotuvas perduoda tik tuos regionus, kuriuos turi pats:
turėdamas `nl`, jis neperduos `nl-ov`. Įtrauk kiekvieną kartotuvą į visus regionus,
kuriuos jis aptarnauja, ir tik į juos. Kurie tai regionai, žino tavo
[vietos grupė](/community/).

**Apribok, ką tavo kartotuvas perduoda toliau.** Du nustatymai palieka arti namų
srautą, kuriam nereikia keliauti toli:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: skelbimai, kuriais mazgas praneša apie save tinklui, keliauja
  ne daugiau kaip 3 šuolius.
- `flood.max.unscoped 1`: žinutė be regiono praeina ne daugiau kaip per vieną kartotuvą.
