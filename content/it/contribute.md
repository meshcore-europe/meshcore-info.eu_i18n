---
title: Contribuire
lead: Questa guida è scritta, controllata e tradotta da volontari. Ecco come puoi dare una mano, con o senza un account GitHub.
description: Aggiungi la tua community, un dispositivo o un progetto, revisiona una traduzione o migliora una guida su meshcore-info.eu.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-26'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
---

Tutto il contenuto di questo sito si trova in un
[repository GitHub](https://github.com/meshcore-europe/meshcore-info.eu) pubblico. Per le modifiche
piccole usi un modulo su GitHub (una issue). Per tutto il resto serve una pull
request: una proposta di modifica ai file che un manutentore revisiona. Un
manutentore controlla ogni modifica prima della pubblicazione.

Non hai un account GitHub? Scrivici su [Discord](https://discord.meshcore-info.eu/): un
gruppo mancante, un dato sbagliato o una traduzione che suona strana. Un volontario
se ne occupa da lì.

## Aggiungi la tua community {#community}

Gestisci un gruppo MeshCore locale aperto a tutti? Compila il
[modulo per le community](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
con il nome, la zona e i link pubblici. Dopo l'aggiunta, il tuo gruppo compare
nella pagina [Gruppi locali](/community/) in tutte le lingue.

## Proponi un dispositivo o un progetto {#device-project}

La [pagina dei dispositivi](/devices/) riporta le specifiche tratte dalla documentazione
dei produttori e non contiene mai link a negozi. Proponi un hardware con il
[modulo per i dispositivi](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Hai creato un'app, uno strumento, un bridge o un progetto hardware per MeshCore con codice
sorgente pubblico? Aggiungilo con il
[modulo per i progetti](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Revisiona una traduzione {#translate}

Le pagine nelle altre lingue nascono come traduzioni automatiche e lo dichiarano in
cima. Le traduzioni vivono in un repository separato,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), quindi
non devi mai toccare il codice del sito. Se conosci bene una di queste
lingue, puoi migliorarla:

1. Apri la pagina e segui "Aiuta a migliorare questa traduzione". Si apre il
   file su GitHub, dove puoi modificarlo dal browser.
2. Correggi la formulazione. Lascia link, codice, numeri e nomi come MeshCore
   esattamente come sono.
3. Nel blocco `translation` in cima, cambia `status: ai` in
   `status: human` e proponi la modifica.

Hai trovato una parola sbagliata ma non hai tempo di correggerla? Segnalala con il
[modulo per le traduzioni](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Migliora una guida {#guides}

Le guide vengono scritte prima in inglese e tradotte da lì. Correzioni
e nuovi argomenti sono benvenuti tramite il
[modulo per i contenuti](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
o una pull request. Ogni dato ha bisogno di una fonte: il firmware MeshCore e la sua
documentazione, un'autorità per le radiocomunicazioni o un produttore. Scrivi con parole tue. Una
breve citazione con la sua fonte va bene.

La [guida per i contributori](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
spiega come lavorare sul sito dal tuo computer.

## Stato delle traduzioni {#coverage}

"Revisionata" significa controllata
da una persona; "Automatica" significa tradotta automaticamente e non ancora revisionata;
"Obsoleta" significa che il testo inglese è cambiato dopo la traduzione;
"Mancante" significa che la pagina non ha ancora una traduzione.

{{< coverage >}}

## Crediti {#credits}

Il sito è costruito con [Astro](https://astro.build/). Usa i caratteri
IBM Plex Sans e IBM Plex Mono, con licenza SIL Open Font License. Le traduzioni
seguono le
convenzioni di [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) e
condividono i suoi glossari MeshCore. MeshCore stesso viene sviluppato su
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Testi e traduzioni sono rilasciati con licenza CC BY 4.0, il codice con licenza
MIT.
