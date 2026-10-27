---
title: Guia de repetidores
lead: Um repetidor colocado num ponto alto reencaminha mensagens para todos à sua volta, por uma cidade ou um vale inteiro. Escolhe um local, alimenta-o com energia solar, configura-o e cumpre a lei.
description: 'Planear, alimentar, configurar e operar legalmente um repetidor MeshCore na Europa: escolha do local, dimensionamento solar, comandos CLI, potência e limites de duty cycle a 868 MHz.'
eyebrow: 868 MHz · até 500 mW · sem licença
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '4a0fe39f'
  seeded: '2026-10-26'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['1de4a4f7', '766086be', '70faf508', '8bc641aa', '2018aa04', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
---

Os repetidores sustentam a mesh. Os companions, os rádios a partir dos quais envias mensagens, não reencaminham mensagens. Sem repetidores, só chegas às pessoas ao teu alcance direto. Cada repetidor que instalas alarga a mesh para todos à sua volta. Este guia segue o firmware MeshCore v1.18.0.

Antes de começares, fala com o teu [grupo local](/community/). Eles sabem onde falta cobertura, qual é o [preset usado na tua zona](/guides/settings/) e como dar nomes aos repetidores. Consulta os [mapas de cobertura](/map/) para ver os repetidores perto de ti e apresenta-te nos [canais](/guides/channels/) públicos ou locais.

## Escolhe um local {#site}

A altura vale mais do que a potência. A 868 MHz, o LoRa propaga-se melhor com linha de vista desimpedida. Colinas, edifícios e árvores densas custam muito mais alcance do que uns miliwatts a mais recuperam.

- **Sobe o mais possível.** Um telhado, um mastro, um edifício alto ou uma colina cobrem muito mais do que um parapeito de janela. Mesmo uns metros acima dos telhados vizinhos já ajudam.
- **Deixa a antena desimpedida.** Monta-a acima das bordas do telhado, longe de metal, caleiras e outras antenas.
- **Verifica a vista.** Ferramentas como o [HeyWhatsThat](https://www.heywhatsthat.com/) mostram o que se vê a partir de um local. Se consegues ver um ponto, um repetidor nesse ponto está ao alcance.
- **Deixa espaço livre.** Um percurso de rádio precisa de algum espaço livre à volta da linha direta, não só da linha em si. Em distâncias longas, o meio do percurso deve passar vários metros acima dos obstáculos.
- **Pede autorização.** Obtém o consentimento do dono do telhado ou do mastro e combina como vais aceder ao repetidor para manutenção.

## Hardware {#hardware}

- **Placa.** Escolhe uma placa nRF52 de baixo consumo, como a [Heltec T114](/devices/), a RAK WisBlock ou o SenseCAP Solar Node. As placas ESP32 consomem mais energia (a página de dispositivos marca-as como High), o que dificulta o funcionamento a energia solar.
- **Antena.** Usa uma antena feita para 868 MHz, montada na vertical. O [guia de antenas](/guides/antenna/) explica tipos, conectores, cabo e montagem. O ganho da antena conta para o limite legal de potência; vê [Limites legais](#legal).
- **Cabo.** Mantém o cabo coaxial curto ou usa cabo de baixas perdas. A 868 MHz, uns metros de cabo fino podem perder metade da tua potência.
- **Caixa.** Uma caixa estanque (IP65 ou melhor) com bucim, um furo de ventilação ou drenagem contra a condensação, e de cor clara ou com proteção solar. As baterias sofrem com o calor e não carregam abaixo de zero graus.
- **Raios.** Uma antena num telhado é um alvo. Segue as regras locais de ligação à terra ou monta-a onde uma descarga não chegue à instalação elétrica do edifício.

## Alimentação e dimensionamento solar {#power}

Um repetidor solar tem de sobreviver às semanas mais escuras do inverno. Dimensiona-o para elas:

1. **Mede o consumo.** Liga o repetidor já configurado a um medidor de energia USB durante um dia. Lê a energia gasta em watt-hora (Wh). O tráfego na tua zona altera o valor, por isso mede no local se puderes.
2. **Acrescenta reserva.** Prevê capacidade de bateria para pelo menos 5 a 7 dias sem sol útil.
3. **Descobre o teu sol de inverno.** A ferramenta gratuita da UE [PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) mostra, para qualquer local, quanta energia um painel produz por mês. Usa o mês com menos sol.
4. **Dimensiona o painel.** O painel tem de repor o consumo de cada dia nesse pior mês, com folga para as perdas de carregamento.

Um exemplo prático, com valores assumidos: um repetidor que gasta 1 Wh por dia precisa de uma bateria de pelo menos 7 Wh para uma semana de reserva, cerca de 2 Ah de capacidade útil a 3,7 V. Se o PVGIS indicar que um painel de 1 W no teu local dá 0,5 Wh por dia em dezembro, precisas de um painel de pelo menos 2 W. Com 3 a 5 W ficas com margem para nuvens, neve e envelhecimento.

## Configura-o {#config}

**Grava o firmware.** Usa o [web flasher](https://flasher.meshcore.io) e escolhe o firmware **Repeater** para a tua placa. Vê os passos de gravação em [Começar](/get-started/#flash).

**Configura por USB.** Com o repetidor ainda ligado ao computador, abre o [config.meshcore.io](https://config.meshcore.io) ou a consola do flasher. Também podes usar qualquer terminal série a 115200 baud. Os comandos mais importantes:

| O quê | Comando |
|---|---|
| Alterar a palavra-passe de administrador | `password <new password>` |
| Dar-lhe um nome | `set name <name>` |
| Preset de rádio: frequência, largura de banda, SF, CR (reinicia para aplicar) | `set radio 869.618,62.5,8,8` |
| Limite de duty cycle, em percentagem | `set dutycycle 10` |
| Potência de emissão do chip de rádio, em dBm | `set tx <dBm>` |
| Posição, para aparecer nos mapas | `set lat <degrees>` e `set lon <degrees>` |
| Contacto para outros operadores | `set owner.info <text>` |
| Horas entre anúncios por flood, os que toda a mesh ouve | `set flood.advert.interval <hours>` |
| Anunciá-lo agora | `advert` |
| Reiniciar | `reboot` |

A palavra-passe de administrador por omissão é `password`, e quem entrar com ela torna-se administrador. Altera-a antes de o repetidor entrar no ar.

O exemplo de `set radio` acima é o EU/UK (Narrow). Usa antes os valores do preset da tua zona: as [Definições recomendadas](/guides/settings/) listam-nos por país.

**Acerta o relógio.** Sem módulo de relógio (RTC), um repetidor perde a hora a cada falha de energia e reinicia em maio de 2024. Enquanto funciona, o relógio vai-se desviando. Entra remotamente a partir da app e usa `clock sync`, ou acerta a hora por USB. Um módulo RTC é um extra que compensa num repetidor: mantém a hora durante as falhas de energia e desvia-se muito menos.

**Gere-o remotamente.** Quando estiver na mesh, entra a partir da app MeshCore com a palavra-passe de administrador. Aí lês o estado dele e usas os mesmos comandos por rádio. Alguns comandos só funcionam por USB, como `set freq` e o reset de fábrica `erase`.

A lista completa de comandos está na [referência CLI do MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Limites legais {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Os presets europeus do MeshCore ficam na sub-banda **869.40-869.65 MHz**. Na UE, no Reino Unido, na Suíça e na Noruega, esta sub-banda está aberta a dispositivos de curto alcance sem licença, dentro destes limites:

- no máximo **500 mW e.r.p.** de potência radiada;
- no máximo **10% de duty cycle**: não mais de 360 segundos de emissão em qualquer hora, por dispositivo. Em alternativa, um dispositivo pode usar listen-before-talk com agilidade de frequência adaptativa, como definido na ETSI EN 300 220-2;
- o sinal completo, com no máximo 250 kHz de largura, tem de ficar dentro da sub-banda.

A banda é partilhada: não podes perturbar serviços licenciados, e outros podem perturbar-te.
O rádio tem de ter marcação CE (na Grã-Bretanha, CE ou UKCA).
{{< /callout >}}

Fontes: [Recomendação CEPT ERC 70-03](https://docdb.cept.org/document/845), Anexo 1, banda h1.7; [Decisão da Comissão 2006/771/CE](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) e respetivas alterações; [ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), banda O.

### Potência: e.r.p. e a tua antena {#erp}

O limite aplica-se à potência *radiada*, medida em relação a uma antena dipolo simples (e.r.p.). O ganho da antena conta; as perdas no cabo subtraem-se. Os fabricantes indicam o ganho da antena em dBi, que é 2.15 dB mais do que o mesmo ganho em dBd (relativo a um dipolo). Mantém esta soma igual ou abaixo de 27 dBm (500 mW):

> potência de emissão (dBm) + ganho da antena (dBi) − perdas no cabo (dB) − 2.15 ≤ 27

- Uma placa a emitir 22 dBm numa antena de 5 dBi através de 1 dB de cabo:
  22 + 5 − 1 − 2.15 = 23.85 dBm, cerca de 240 mW e.r.p. Dentro do limite.
- Uma placa com um amplificador de 30 dBm (1 W) numa antena de 3 dBi:
  30 + 3 − 2.15 = 30.85 dBm, cerca de 1.2 W e.r.p. Acima do limite; baixa a potência de emissão.

`set tx` define a saída do chip LoRa, em dBm. O próprio chip SX1262 chega no máximo a 22 dBm; o firmware não verifica o número que introduzes. As placas com amplificador extra, como a Heltec V4 ou a Station G2, emitem muito mais do que o número que defines. Consulta a tabela do fabricante antes de o definir e começa baixo.

### Duty cycle {#duty-cycle}

Um repetidor emite por todos à sua volta, por isso gasta o seu tempo de antena mais depressa do que um companion. O limitador de duty cycle do MeshCore vem por omissão a 50%, acima do que esta banda permite. Define-o a 10% em todos os repetidores:

```text
set dutycycle 10
```

### Precisão de frequência {#frequency}

O canal EU/UK (Narrow), 869.618 MHz com 62.5 kHz de largura de banda, chega até 869.649 MHz: menos de 1 kHz abaixo do topo da sub-banda. O sinal tem de ficar dentro da banda a qualquer temperatura. Isso exige um cristal com compensação de temperatura (TCXO). Quase todas as placas atuais têm um. As placas mais antigas sem TCXO, como a Heltec V2, desviam-se demasiado para funcionar de forma fiável a 62.5 kHz.

### Notas por país {#countries}

- **Estados-membros da UE** têm de disponibilizar esta sub-banda nestes termos (Decisão 2006/771/CE, artigo 3.º).
- **Reino Unido:** os mesmos limites, na [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices) da Ofcom.
- **Suíça e Liechtenstein:** os mesmos limites, na [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09) da OFCOM.
- **Noruega:** os mesmos limites, no [regulamento sobre autorizações gerais](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Estas notas não são aconselhamento jurídico. As regras mudam; em caso de dúvida, consulta o regulador nacional.

## Lista de verificação para a instalação {#checklist}

- [ ] O dono do local concordou e consegues aceder ao repetidor para manutenção.
- [ ] A placa corre o firmware **Repeater** e a antena foi ligada antes do primeiro arranque.
- [ ] A palavra-passe de administrador foi alterada.
- [ ] O rádio corresponde ao [preset da tua zona](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` está definido.
- [ ] A potência de emissão mais o ganho da antena ficam dentro dos 500 mW e.r.p.
- [ ] O nome, a posição e o `owner.info` estão definidos, para que os outros saibam quem o opera.
- [ ] O relógio está acertado (`clock`).
- [ ] A caixa está vedada, com furo de drenagem ou ventilação, e o cabo tem uma curva de gotejamento.
- [ ] A bateria e o painel estão dimensionados para o pior mês de inverno.
- [ ] Testaste-o à distância com a app antes de sair do local.
- [ ] O teu grupo local sabe que está no ar.
