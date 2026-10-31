---
title: Guia do repetidor
lead: Um repetidor colocado no alto reencaminha as mensagens para todos à sua volta, numa cidade ou num vale inteiro. Escolhe um local, alimenta-o com energia solar, configura-o e cumpre a lei.
description: 'Planear, alimentar, configurar e operar legalmente um repetidor MeshCore na Europa: escolha do local, dimensionamento solar, definições por CLI, limites de potência e de duty cycle nos 868 MHz.'
eyebrow: 868 MHz · até 500 mW · sem licença
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-10-31'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

São os repetidores que sustentam a mesh. Os companions, os rádios a partir dos quais
envias mensagens, não reencaminham mensagens. Por isso, sem repetidores, só
chegas às pessoas que estão ao teu alcance direto. Um repetidor bem colocado
alarga a mesh para todos à sua volta. Este guia segue o firmware MeshCore
v1.18.0.

Antes de começares, fala com o teu [grupo local](/community/). Esse grupo sabe onde
falta cobertura, que [preset a tua zona usa](/guides/settings/) e como dar nome aos repetidores. Consulta os
[mapas de cobertura](/map/) para encontrares repetidores perto de ti e cumprimenta a comunidade nos [canais](/guides/channels/)
públicos ou locais.

## Precisas de um? {#need}

Um repetidor reenvia cada mensagem flood que ouve, e todos os repetidores
ao alcance partilham o mesmo tempo de antena. Onde a mesh já te alcança, mais um
repetidor acrescenta tráfego e nenhuma cobertura. Um companion colocado no alto, numa janela de sótão
ou numa varanda, pode bastar-te.

Instala um repetidor onde falta cobertura:

- os [mapas de cobertura](/map/) não mostram nenhum repetidor perto de ti, ou só mostram repetidores que o teu
  companion não ouve;
- o teu grupo local diz que a zona precisa de um.

## Escolhe um local {#site}

A altura vale mais do que a potência. O LoRa a 868 MHz propaga-se melhor em linha
de vista desimpedida. Colinas, edifícios e árvores densas custam muito mais alcance do que
alguns milliwatts extra conseguem recuperar.

- **Sobe o mais possível.** Um telhado, um mastro, um edifício alto ou uma colina cobrem muito mais
  do que um parapeito de janela. Até alguns metros acima dos telhados à volta ajudam.
- **Mantém a antena desimpedida.** Monta-a acima das beiras do telhado, longe de
  metal, de caleiras e de outras antenas.
- **Verifica a vista.** Com ferramentas como o [HeyWhatsThat](https://www.heywhatsthat.com/)
  vês o que é visível a partir de um local. Se consegues ver um ponto, um repetidor
  lá fica ao teu alcance.
- **Deixa espaço livre.** Um caminho de rádio precisa de algum espaço livre à volta da linha
  direta, e não só da própria linha. Em longas distâncias, o meio do caminho
  deve passar vários metros acima dos obstáculos.
- **Pede autorização.** Obtém o consentimento do dono do telhado ou do mastro e combina
  como vais aceder ao repetidor para manutenção.

## Hardware {#hardware}

- **Placa.** Escolhe uma placa nRF52 de baixo consumo, como a
  [Heltec T114](/devices/), a RAK WisBlock ou o SenseCAP Solar Node. As placas ESP32
  consomem mais energia (a página de dispositivos marca-as como High). Por isso é difícil
  alimentá-las a energia solar.
- **Antena.** Usa uma antena feita para 868 MHz, montada na vertical. O
  [guia de antenas](/guides/antenna/) explica tipos, conectores, cabo e
  montagem. O ganho da antena conta para o limite legal de potência: vê
  [Limites legais](#legal).
- **Cabo.** Usa um cabo coaxial curto, ou um cabo de baixas perdas. A 868 MHz, alguns
  metros de cabo fino podem fazer-te perder metade da potência.
- **Caixa.** Uma caixa estanque (IP65 ou melhor) com bucim, um orifício de
  ventilação ou drenagem contra a condensação, e uma cor clara ou proteção contra o sol.
  As baterias sofrem com o calor e não podem ser carregadas abaixo de zero graus.
- **Raios.** Uma antena num telhado é um alvo. Segue as regras locais de
  ligação à terra, ou monta-a num sítio onde um raio não chegue à instalação
  elétrica do edifício.

## Energia e dimensionamento solar {#power}

Um repetidor solar tem de aguentar as semanas mais escuras do inverno. Dimensiona-o
para elas:

1. **Mede o consumo.** Liga o repetidor já configurado a um medidor de energia USB
   durante um dia. Lê a energia gasta em watts-hora (Wh). O tráfego na
   tua zona altera o valor, por isso mede no local, se puderes.
2. **Acrescenta reserva.** Prevê capacidade de bateria para pelo menos 5 a 7 dias
   sem sol útil.
3. **Descobre o teu sol de inverno.** A [ferramenta PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/),
   gratuita e da UE, mostra para qualquer local quanta energia um painel produz por mês. Usa o mês com
   menos sol.
4. **Dimensiona o painel.** O painel tem de repor o consumo de cada dia nesse pior
   mês, com margem para as perdas de carregamento.

Um exemplo prático, com valores supostos: um repetidor que gasta 1 Wh por dia
precisa de uma bateria de pelo menos 7 Wh para uma semana de reserva, cerca de 2 Ah de
capacidade útil a 3,7 V. Se o PVGIS indicar que um painel de 1 W no teu local dá
0,5 Wh por dia em dezembro, precisas de pelo menos um painel de 2 W. Com 3 a 5 W
ficas com margem para nuvens, neve e envelhecimento.

## Configura-o {#config}

**Instala o firmware.** Usa o [web flasher](https://flasher.meshcore.io) e escolhe o
firmware **Repeater** para a tua placa. Os passos de instalação estão em
[Primeiros passos](/get-started/#flash).

**Configura por USB.** Com o repetidor ainda ligado ao computador,
abre [config.meshcore.io](https://config.meshcore.io) ou a consola do flasher.
Também podes usar qualquer terminal série a 115200 baud. Os comandos mais
importantes:

| O quê | Comando |
|---|---|
| Mudar a palavra-passe de administrador | `password <new password>` |
| Dar-lhe um nome | `set name <name>` |
| Preset de rádio: frequência, largura de banda, SF, CR (reinicia para aplicar) | `set radio 869.618,62.5,8,8` |
| Limite de duty cycle, em percentagem | `set dutycycle 10` |
| Potência de emissão do chip de rádio, em dBm | `set tx <dBm>` |
| Posição, para aparecer nos mapas | `set lat <degrees>` e `set lon <degrees>` |
| Dados de contacto para outros operadores | `set owner.info <text>` |
| Horas entre anúncios flood, os que toda a mesh ouve | `set flood.advert.interval <hours>` |
| Anunciá-lo agora | `advert` |
| Reiniciar | `reboot` |

A palavra-passe de administrador predefinida é `password`. Quem entrar com ela
passa a ser administrador. Muda-a antes de o repetidor entrar no ar.

O exemplo `set radio` acima corresponde a EU/UK (Narrow). Usa antes os valores do preset da tua
zona: as [Definições recomendadas](/guides/settings/) indicam-nos
por país.

**Acerta o relógio.** Sem um módulo de relógio (RTC), o repetidor perde a hora a
cada corte de energia e recomeça em maio de 2024. Enquanto funciona, o relógio também
deriva: vai ficando adiantado ou atrasado. Por isso, acerta o relógio de vez em quando: entra
remotamente a partir da app e usa `clock sync`, ou acerta a hora por USB. Com
um módulo RTC raramente precisas de o fazer: o módulo mantém a hora durante os cortes de energia e
deriva muito menos.

**Gere-o à distância.** Quando o repetidor já estiver na mesh, entra a partir da app MeshCore
com a palavra-passe de administrador. Aí lês o estado do repetidor e usas os mesmos comandos
por rádio. Alguns comandos só funcionam por USB, como `set freq` e a
reposição de fábrica `erase`.

**Guarda a identidade.** Antes de um erase, escreve `get prv.key` por USB e guarda
num sítio seguro a chave privada que aparece. Depois do erase, com `set prv.key <key>`
e um `reboot` devolves ao repetidor a identidade antiga. Assim, os nós que o
conhecem encontram-no com o mesmo prefixo.

A lista completa de comandos está na
[referência da CLI do MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Atualiza-o sem fios {#update}

Quando o repetidor já estiver lá em cima, atualizas-o a partir do chão. Entra a partir da
app MeshCore com a palavra-passe de administrador, abre a linha de comandos e escreve
`start ota`. O que acontece a seguir depende da placa. As outras placas respondem `Error`,
e essas atualizas por USB.

**Placas nRF52**, como RAK, Heltec T114, Seeed XIAO e SenseCAP Solar:

1. Descarrega o **ZIP** do novo firmware para a tua placa no
   [web flasher](https://flasher.meshcore.io).
2. Escreve `start ota`. O repetidor responde `OK` e aparece por Bluetooth
   como `<board>_OTA`, por exemplo `RAK4631_OTA`.
3. Abre a app nRF Device Firmware Update no telemóvel, escolhe o ZIP e
   o repetidor, e faz o envio. Demora alguns minutos.

Instala o [bootloader OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
numa placa nRF52 antes de a montares lá em cima. Com o bootloader de origem, só reparas
uma atualização falhada por USB. Com o OTAFIX, a placa volta ao
modo de atualização e tentas outra vez por Bluetooth.

**Placas ESP32**, como a Heltec V3 e a V4:

1. Descarrega no web flasher o `.bin` **não fundido** para a tua placa:
   o ficheiro sem "merged" no nome.
2. Escreve `start ota`. O repetidor abre uma rede WiFi chamada `MeshCore-OTA`
   e responde com o endereço da página de envio.
3. Dentro do alcance do WiFi, liga o telemóvel ou o portátil a essa rede, abre o
   endereço e envia o ficheiro.

## Limites legais {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Os presets europeus do MeshCore ficam na sub-banda **869.40-869.65 MHz**. Na
UE, no Reino Unido, na Suíça e na Noruega, esta sub-banda está aberta a dispositivos de curto alcance sem
licença, dentro destes limites:

- no máximo **500 mW e.r.p.** de potência radiada;
- no máximo **10% de duty cycle**: não mais de 360 segundos de emissão em
  cada hora, por dispositivo. Em alternativa, um dispositivo pode usar listen-before-talk
  com adaptive frequency agility, tal como definido na ETSI EN 300 220-2;
- o sinal inteiro, com no máximo 250 kHz de largura, tem de ficar dentro da sub-banda.

A banda é partilhada: não podes perturbar serviços licenciados, e outros podem
perturbar-te a ti.
O rádio tem de ter marcação CE (na Grã-Bretanha, CE ou UKCA).
{{< /callout >}}

Fontes: [Recomendação CEPT ERC 70-03](https://docdb.cept.org/document/845),
Anexo 1, banda h1.7;
[Decisão da Comissão 2006/771/CE](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
e respetivas alterações;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
banda O.

### Power: e.r.p. and your antenna {#erp}

The limit applies to the *radiated* power, measured against a simple dipole
antenna (e.r.p.). Antenna gain counts; cable loss subtracts. Makers state
antenna gain in dBi, which is 2.15 dB more than the same gain in dBd
(relative to a dipole). Keep this sum at or below 27 dBm (500 mW):

> transmit power (dBm) + antenna gain (dBi) − cable loss (dB) − 2.15 ≤ 27

- A board transmitting 22 dBm into a 5 dBi antenna through 1 dB of cable:
  22 + 5 − 1 − 2.15 = 23.85 dBm, about 240 mW e.r.p. Within the limit.
- A board with a 30 dBm (1 W) amplifier into a 3 dBi antenna:
  30 + 3 − 2.15 = 30.85 dBm, about 1.2 W e.r.p. Over the limit; lower the
  transmit power.

`set tx` sets the output of the LoRa chip, in dBm. The SX1262 chip itself
tops out at 22 dBm; the firmware does not check the number you enter. Boards with an extra
amplifier, such as the Heltec V4 or the Station G2, transmit much more than
the number you set. Check the manufacturer's table before you set it, and
start low.

### Duty cycle {#duty-cycle}

Um repetidor emite para todos à sua volta, por isso gasta o seu tempo de antena mais depressa
do que um companion. O limitador de duty cycle do MeshCore vem a 50% por predefinição, acima do que
esta banda permite. Define-o para 10% em todos os repetidores:

```text
set dutycycle 10
```

### Precisão da frequência {#frequency}

O canal EU/UK (Narrow), 869.618 MHz com 62.5 kHz de largura de banda, chega
até 869.649 MHz: menos de 1 kHz abaixo do topo da sub-banda. O sinal
tem de ficar dentro da banda a qualquer temperatura. Para isso é preciso um
cristal com compensação de temperatura (TCXO). Quase todas as placas atuais têm um.
As placas mais antigas sem TCXO, como a Heltec V2, derivam demasiado para funcionarem bem
a 62.5 kHz.

### Notas por país {#countries}

- **Os Estados-Membros da UE** têm de disponibilizar esta sub-banda nestas condições
  (Decisão 2006/771/CE, artigo 3.º).
- **Reino Unido:** os mesmos limites, na
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices) da Ofcom.
- **Suíça e Liechtenstein:** os mesmos limites, na
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09) do OFCOM.
- **Noruega:** os mesmos limites, no
  [regulamento sobre autorizações gerais](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Estas notas não são aconselhamento jurídico. As regras mudam. Em caso de dúvida, confirma junto
do regulador do teu país.

## Lista de verificação da instalação {#checklist}

- [ ] O dono do local concordou e consegues aceder ao repetidor para manutenção.
- [ ] A placa corre o firmware **Repeater** e ligaste a antena antes
      de a alimentares pela primeira vez.
- [ ] Mudaste a palavra-passe de administrador.
- [ ] O rádio corresponde ao [preset da tua zona](/guides/settings/) (`get radio`).
- [ ] Definiste `set dutycycle 10`.
- [ ] A potência de emissão mais o ganho da antena ficam dentro de 500 mW e.r.p.
- [ ] Definiste o nome, a posição e o `owner.info`, para os outros saberem quem gere o repetidor.
- [ ] Acertaste o relógio (`clock`).
- [ ] A caixa está vedada, com um orifício de drenagem ou ventilação, e o cabo tem um
      laço de gotejamento.
- [ ] A bateria e o painel estão dimensionados para o pior mês de inverno.
- [ ] Testaste o repetidor à distância com a app antes de saíres do local.
- [ ] O teu grupo local sabe que o repetidor está a funcionar.
