---
title: Checklist del ripetitore
lead: Controlla il tuo ripetitore prima di installarlo. Ogni riga indica cosa controllare, il comando che lo mostra e la guida che lo spiega.
description: 'Una checklist per un ripetitore MeshCore prima di montarlo su un tetto o un palo: cosa controllare via USB, come montarlo e il test da fare prima di andartene.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Un ripetitore su un tetto è difficile da raggiungere, quindi controllalo finché è ancora sulla tua scrivania. La [guida al ripetitore](/repeater-guide/) spiega ogni passaggio. I valori, come il preset e i limiti di hop, li trovi nelle [impostazioni della tua zona](/guides/settings/). Digita i comandi via USB, per esempio nella [console seriale](/firmware/console/). Questa lista fa riferimento al firmware MeshCore v1.18.0.

## Prima di iniziare {#start}

- [ ] Le [mappe di copertura](/map/) o il tuo [gruppo locale](/community/) indicano che la zona ha bisogno di un ripetitore. Vedi [Ti serve un ripetitore?](/repeater-guide/#need)
- [ ] Il proprietario del sito è d'accordo e puoi raggiungere il ripetitore per la manutenzione.
- [ ] Batteria e pannello sono dimensionati per il mese invernale peggiore. Vedi [Alimentazione e dimensionamento solare](/repeater-guide/#power).

## Alla scrivania, via USB {#usb}

- [ ] Sulla scheda gira il firmware **Repeater**: `ver` ne mostra la versione. Vedi [Configuralo](/repeater-guide/#config).
- [ ] Su una scheda nRF52, la risposta a `get bootloader.ver` contiene `OTAFIX`. Vedi [Aggiornalo via radio](/repeater-guide/#update).
- [ ] `get radio` mostra il preset della tua zona.
- [ ] `get dutycycle` mostra 10. Vedi [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] `get tx` sommato al guadagno della tua antenna resta entro 500 mW e.r.p. Vedi [Potenza: e.r.p. e la tua antenna](/repeater-guide/#erp).
- [ ] La password di amministratore non è più `password`.
- [ ] `get guest.password` mostra una password.
- [ ] `get name` mostra il nome che il tuo gruppo locale usa per i suoi ripetitori.
- [ ] `get lat` e `get lon` mostrano la posizione del sito.
- [ ] `get owner.info` mostra come gli altri operatori possono contattarti.
- [ ] `region` mostra le regioni della tua zona. `get flood.max.advert` e `get flood.max.unscoped` ne mostrano i limiti di hop. Vedi [Riduci il traffico](/guides/settings/#traffic).
- [ ] Hai salvato in un posto sicuro la chiave privata ottenuta con `get prv.key`.
- [ ] `clock` mostra l'ora attuale, in UTC.
- [ ] Con l'alimentazione solare, `powersaving` mostra `on`.

## Sul tetto {#roof}

- [ ] L'antenna è collegata prima che il ripetitore riceva alimentazione.
- [ ] L'antenna è in verticale in cima al palo, lontana dal metallo. Vedi [Montaggio](/guides/antenna/#mounting).
- [ ] Ogni connettore esterno è sigillato e il cavo ha un'ansa di gocciolamento.
- [ ] Il contenitore è chiuso, con un foro di ventilazione o di drenaggio. Vedi [Hardware](/repeater-guide/#hardware).

## Prima di andartene {#leave}

- [ ] Da lontano, con il tuo companion raggiungi il ripetitore nell'app.
- [ ] Hai inviato `advert`, così i nodi in tutta la mesh vengono a sapere del ripetitore.
- [ ] Il tuo [gruppo locale](/community/) sa che il ripetitore è attivo.
