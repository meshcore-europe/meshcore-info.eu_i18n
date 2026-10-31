---
title: Přispěj
lead: Tuhle příručku píšou, kontrolují a překládají dobrovolníci. Tady najdeš, jak pomoct, s účtem na GitHubu i bez něj.
description: Přidej svou komunitu, zařízení nebo projekt, zkontroluj překlad nebo vylepši příručku na meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-31'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Celý obsah webu je ve veřejném
[repozitáři na GitHubu](https://github.com/meshcore-europe/meshcore-info.eu). Drobné změny
pošleš přes formulář na GitHubu (issue). Větší změny pošleš jako pull
request: návrh úpravy souborů, který zkontroluje správce. Správce
prověří každou změnu, než se objeví na webu.

Nemáš účet na GitHubu? Napiš nám na [Discord](https://discord.meshcore-info.eu/): chybějící
skupinu, špatný údaj nebo překlad, který zní divně. Dobrovolník
se o to postará.

## Přidej svou komunitu {#community}

Vedeš místní skupinu MeshCore, do které se může přidat kdokoli? Vyplň
[formulář pro komunitu](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
a uveď název, oblast a veřejné odkazy. Po přidání se tvoje skupina zobrazí
na stránce [Místní skupiny](/community/) ve všech jazycích.

## Navrhni zařízení nebo projekt {#device-project}

Na [stránce zařízení](/devices/) jsou parametry z dokumentace výrobců
a nikdy tam nejsou odkazy na obchody. Hardware navrhneš přes
[formulář pro zařízení](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Vytvořil jsi aplikaci, nástroj, most nebo hardwarový návrh pro MeshCore s veřejným zdrojovým
kódem? Přidej ho přes
[formulář pro projekt](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Zkontroluj překlad {#translate}

Stránky v jiných jazycích vznikají jako strojový překlad a nahoře to
uvádějí. Překlady mají vlastní repozitář,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), takže
kódu webu se nikdy nemusíš dotknout. Pokud některý z jazyků dobře ovládáš,
můžeš překlad vylepšit:

1. Otevři stránku a klikni na „Pomoz vylepšit tento překlad“. Otevře se
   soubor na GitHubu, kde ho upravíš přímo v prohlížeči.
2. Oprav znění. Odkazy, kód, čísla a názvy jako MeshCore nech
   přesně tak, jak jsou.
3. V bloku `translation` nahoře změň `status: ai` na
   `status: human` a navrhni změnu.

Našel jsi špatné slovo, ale nemáš čas ho opravit? Nahlas ho přes
[formulář pro překlad](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Vylepši příručku {#guides}

Příručky píšeme nejdřív anglicky a z angličtiny je překládáme. Opravy
a nová témata uvítáme přes
[formulář pro obsah](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
nebo pull request. Každý údaj potřebuje zdroj: firmware MeshCore a jeho
dokumentaci, regulační úřad pro rádiový provoz nebo výrobce. Piš vlastními slovy.
Krátká citace se zdrojem je v pořádku.

V [příručce pro přispěvatele](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
najdeš, jak na webu pracovat na vlastním počítači.

## Stav překladů {#coverage}

„Zkontrolováno“ znamená, že překlad prověřil
člověk. „Strojově“ znamená strojový překlad, který zatím nikdo nezkontroloval.
„Zastaralé“ znamená, že se anglický text po vzniku překladu změnil.
„Chybí“ znamená, že stránka zatím nemá překlad.

{{< coverage >}}

## Poděkování {#credits}

Web je postavený na [Astro](https://astro.build/). Používá písma
IBM Plex Sans a IBM Plex Mono pod licencí SIL Open Font License. Překlady
se řídí
konvencemi projektu [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) a
sdílejí jeho glosáře pro MeshCore. Samotný MeshCore se vyvíjí v repozitáři
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Texty a překlady jsou pod licencí CC BY 4.0, kód pod licencí
MIT.
