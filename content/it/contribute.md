---
title: Contribuisci
lead: Questa guida la scrivono, la verificano e la traducono dei volontari. Ecco come puoi aiutare, con o senza un account GitHub.
description: Aggiungi la tua comunità, un dispositivo o un progetto, rivedi una traduzione o migliora una guida su meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-31'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Tutto il contenuto di questo sito si trova in un
[repository GitHub](https://github.com/meshcore-europe/meshcore-info.eu) pubblico. Per le piccole modifiche
compili un modulo su GitHub (una issue). Le modifiche più grandi le invii come pull
request: una proposta di modifica ai file che un maintainer esamina. Un
maintainer controlla ogni modifica prima che vada online.

Non hai un account GitHub? Scrivici su [Discord](https://discord.meshcore-info.eu/): un
gruppo che manca, un dato sbagliato o una traduzione che suona strana. Poi se ne
occupa un volontario.

## Aggiungi la tua comunità {#community}

Gestisci un gruppo MeshCore locale aperto a tutti? Compila il
[modulo per le comunità](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
con il nome, la zona e i link pubblici. Una volta aggiunto, il tuo gruppo compare
nella pagina [Gruppi locali](/community/) in ogni lingua.

## Proponi un dispositivo o un progetto {#device-project}

La [pagina dei dispositivi](/devices/) riporta le specifiche tratte dalla documentazione dei produttori
e non rimanda mai a negozi. Puoi proporre un hardware con il
[modulo per i dispositivi](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Hai creato un'app, uno strumento, un bridge o un progetto hardware per MeshCore con codice sorgente
pubblico? Aggiungilo con il
[modulo per i progetti](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Rivedi una traduzione {#translate}

Le pagine nelle altre lingue nascono come traduzioni automatiche e lo indicano in
alto. Le traduzioni si trovano in un repository a parte,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), quindi
non devi mai toccare il codice del sito. Se conosci bene una delle lingue,
puoi migliorarla:

1. Apri la pagina e clicca su "Help improve this translation". Il link apre il
   file su GitHub, dove puoi modificarlo nel browser.
2. Correggi il testo. Lascia link, codice, numeri e nomi come MeshCore
   esattamente come sono.
3. Nel blocco `translation` in alto, cambia `status: ai` in
   `status: human` e proponi la modifica.

Hai trovato una parola sbagliata ma non hai tempo di correggerla? Segnalala con il
[modulo per le traduzioni](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Migliora una guida {#guides}

Le guide nascono in inglese e poi vengono tradotte. Puoi inviare correzioni
e nuovi argomenti tramite il
[modulo per i contenuti](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
o una pull request. Ogni dato richiede una fonte: il firmware MeshCore e la sua
documentazione, un'autorità di regolamentazione radio o un produttore. Scrivi con parole tue. Una
breve citazione con la sua fonte va bene.

La [guida per chi contribuisce](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
spiega come lavorare al sito sul tuo computer.

## Stato delle traduzioni {#coverage}

"Reviewed" significa controllata
da una persona; "Machine" significa tradotta automaticamente e non ancora rivista;
"Outdated" significa che il testo inglese è cambiato dopo la traduzione;
"Missing" significa che la pagina non ha ancora una traduzione.

{{< coverage >}}

## Riconoscimenti {#credits}

Il sito è realizzato con [Astro](https://astro.build/). Usa i caratteri
IBM Plex Sans e IBM Plex Mono, con licenza SIL Open Font License. Le traduzioni
seguono le
convenzioni di [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) e
ne condividono i glossari MeshCore. MeshCore stesso viene sviluppato su
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Testi e traduzioni sono rilasciati con licenza CC BY 4.0, il codice con licenza
MIT.
