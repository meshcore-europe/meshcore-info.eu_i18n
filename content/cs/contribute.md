---
title: Přispěj
lead: Tento průvodce píšou, kontrolují a překládají dobrovolníci. Tady se dozvíš, jak pomoct, s účtem na GitHubu i bez něj.
description: Přidej svou komunitu, zařízení nebo projekt, zkontroluj překlad nebo vylepši průvodce na meshcore-info.eu.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-26'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
---

Všechno na tomto webu je uložené ve veřejném
[repozitáři na GitHubu](https://github.com/meshcore-europe/meshcore-info.eu). Malé změny
se zadávají přes formulář na GitHubu (issue). Cokoli většího přichází jako pull
request: návrh změny souborů, který správce posoudí. Správce
zkontroluje každou změnu, než se zveřejní.

Nemáš účet na GitHubu? Napiš nám na [Discord](https://discord.meshcore-info.eu/):
chybějící skupina, nesprávný údaj nebo překlad, který zní divně. Dál se toho
ujme dobrovolník.

## Přidej svou komunitu {#community}

Vedeš místní skupinu MeshCore, do které se může přidat kdokoli? Vyplň
[formulář pro komunity](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
s názvem, oblastí a veřejnými odkazy. Po přidání se tvoje skupina objeví
na stránce [Místní skupiny](/community/) ve všech jazycích.

## Navrhni zařízení nebo projekt {#device-project}

[Stránka se zařízeními](/devices/) uvádí specifikace z dokumentace výrobců
a nikdy neodkazuje na obchody. Hardware navrhni přes
[formulář pro zařízení](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Vytvořil jsi pro MeshCore aplikaci, nástroj, most nebo návrh hardwaru s veřejným zdrojovým
kódem? Přidej ho přes
[formulář pro projekty](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Zkontroluj překlad {#translate}

Stránky v jiných jazycích vznikají jako strojové překlady a nahoře to
o sobě uvádějí. Překlady mají vlastní repozitář,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), takže
se nikdy nemusíš dotýkat kódu webu. Pokud některý z těchto jazyků dobře
ovládáš, můžeš překlad vylepšit:

1. Otevři stránku a klikni na „Pomoz vylepšit tento překlad“. Otevře se
   soubor na GitHubu, kde ho můžeš upravit přímo v prohlížeči.
2. Oprav formulace. Odkazy, kód, čísla a názvy jako MeshCore nech
   přesně tak, jak jsou.
3. V bloku `translation` nahoře změň `status: ai` na
   `status: human` a změnu navrhni.

Našel jsi špatné slovo, ale nemáš čas ho opravit? Nahlas ho přes
[formulář pro překlady](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Vylepši průvodce {#guides}

Průvodce vznikají nejdřív v angličtině a z ní se překládají. Opravy
a nová témata vítáme přes
[formulář pro obsah](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
nebo přes pull request. Každý údaj potřebuje zdroj: firmware MeshCore a jeho
dokumentaci, regulátora rádiového spektra nebo výrobce. Piš vlastními slovy.
Krátká citace s uvedeným zdrojem je v pořádku.

[Průvodce pro přispěvatele](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
vysvětluje, jak na webu pracovat na vlastním počítači.

## Stav překladů {#coverage}

„Zkontrolováno“ znamená, že překlad prošel kontrolou člověkem;
„Strojový“ znamená strojový překlad, který ještě nikdo nezkontroloval;
„Zastaralý“ znamená, že se anglický text po vytvoření překladu změnil;
„Chybí“ znamená, že stránka zatím překlad nemá.

{{< coverage >}}

## Poděkování {#credits}

Web je postavený na [Astro](https://astro.build/). Používá písma
IBM Plex Sans a IBM Plex Mono pod licencí SIL Open Font License. Překlady
se řídí
konvencemi projektu [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) a
sdílejí jeho glosáře MeshCore. Samotný MeshCore se vyvíjí na
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Texty a překlady jsou pod licencí CC BY 4.0, kód pod licencí MIT.
