---
title: Aita kaasa
lead: Selle juhendi kirjutavad, kontrollivad ja tõlgivad vabatahtlikud. Siit saad teada, kuidas aidata, GitHubi kontoga või ilma.
description: Lisa oma kogukond, seade või projekt, vaata tõlge üle või täienda mõnda juhendit saidil meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '1a28f66a'
  seeded: '2026-11-10'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '4b12bb2c', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '8aa01985', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Kogu selle saidi sisu asub avalikus
[GitHubi hoidlas](https://github.com/meshcore-europe/meshcore-info.eu). Väikesed muudatused
esitad GitHubis vormiga (issue). Suuremad muudatused esitad pull requestina: see on
failide muudatusettepanek, mille hooldaja üle vaatab. Hooldaja kontrollib iga muudatust,
enne kui see avaldatakse.

Sul pole GitHubi kontot? Anna meile [Discordis](https://discord.meshcore-info.eu/) teada,
kui mõni grupp on puudu, mõni fakt vale või tõlge kõlab veidralt. Edasi tegeleb sellega
vabatahtlik.

## Lisa oma kogukond {#community}

Haldad kohalikku MeshCore'i gruppi, millega saab liituda igaüks? Täida
[kogukonnavorm](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
ning lisa grupi nimi, piirkond ja avalikud lingid. Pärast lisamist on sinu grupp
[kohalike gruppide](/community/) lehel näha igas keeles.

## Soovita seadet või projekti {#device-project}

[Seadmete lehel](/devices/) on tootjate dokumentatsioonist pärit tehnilised andmed ja
sealt ei lingita kunagi poodidesse. Riistvara saad soovitada
[seadmevormiga](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Oled teinud MeshCore'i jaoks avaliku lähtekoodiga rakenduse, tööriista, silla või
riistvaralahenduse? Lisa see
[projektivormiga](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Vaata tõlge üle {#translate}

Teiskeelsed lehed on algul masintõlked ja lehe ülaosas on see ka kirjas. Tõlked on
eraldi hoidlas
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), nii et
saidi koodi ei pea sa kunagi puutuma. Kui valdad mõnda neist keeltest hästi, saad tõlget
parandada:

1. Ava leht ja vajuta linki „Aita seda tõlget parandada“. Fail avaneb GitHubis, kus saad
   seda brauseris muuta.
2. Paranda sõnastust. Jäta lingid, kood, numbrid ja nimed, näiteks MeshCore, täpselt
   samaks.
3. Muuda ülaosas plokis `translation` väärtus `status: ai` väärtuseks `status: human` ja
   esita muudatusettepanek.

Leidsid vale sõna, aga sul pole aega seda parandada? Teata sellest
[tõlkevormiga](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Täienda juhendit {#guides}

Juhendid kirjutatakse kõigepealt inglise keeles ja tõlgitakse sealt edasi. Parandused
ja uued teemad on oodatud
[sisuvormi](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
või pull requesti kaudu. Faktidel peab olema allikas: MeshCore'i püsivara või
dokumentatsioon, järelevalveasutus, tootja või hooldaja. Kirjuta oma sõnadega. Lühike
tsitaat koos allikaga sobib.

[Kaastöö juhendis](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
on kirjas, kuidas saidi kallal oma arvutis töötada.

## Tõlgete olek {#coverage}

„Üle vaadatud“ tähendab, et tõlget on kontrollinud inimene. „Masintõlge“ tähendab, et tõlke
on teinud masin ja keegi pole seda veel üle vaadanud. „Aegunud“ tähendab, et ingliskeelne
tekst on pärast tõlkimist muutunud. „Puudub“ tähendab, et lehel pole veel tõlget.

{{< coverage >}}

## Tänuavaldused {#credits}

Sait on ehitatud raamistikuga [Astro](https://astro.build/). Saidil on kasutusel kirjatüübid
IBM Plex Sans ja IBM Plex Mono, mille litsents on SIL Open Font License. Tõlked järgivad
projekti [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) tavasid ja kasutavad selle
MeshCore'i sõnastikke. MeshCore'i ennast arendatakse hoidlas
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Tekstide ja tõlgete litsents on CC BY 4.0, koodi litsents on MIT.
