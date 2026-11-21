---
title: Guia do repetidor
lead: Um repetidor num ponto alto retransmite as mensagens para todos à sua volta, numa cidade ou num vale inteiro. Escolhe um local, alimenta-o com energia solar, configura-o e cumpre a lei.
description: 'Planeia, alimenta, configura e opera legalmente um repetidor MeshCore na Europa: escolha do local, dimensionamento solar, definições CLI, limites de potência e de ciclo de trabalho a 868 MHz.'
eyebrow: 868 MHz · até 500 mW · sem licença
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'd42ee2ac'
  seeded: '2026-11-21'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '824ab38e', '662ea23c', '70faf508', 'b9991666', '69d7162f', 'bf712994', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'cc266810']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', 'bbea9a0c', '2b9fab3b', 'b13d1947', 'c2bad16f', '636edc86', 'c2d6bcd1', '957ae975', '98874949', '96d1ebad', 'dbd9fa1f', 'aa06d32b', '9958aad3', '73642ab6', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '90338c64', '2b1d995b', '992bed82', '62eb1543', '210f1b66', 'e817b1f7', '63f961dc', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', '50af0550', 'dd7c556b', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '7cf2bc81']
---

Os repetidores sustentam a mesh. Os companions, os rádios com que envias mensagens, não retransmitem mensagens. Sem repetidores, só chegas às pessoas ao teu alcance direto. Um repetidor no sítio certo alarga a mesh para todos à sua volta. Este guia segue o firmware MeshCore v1.18.0.

Antes de começares, fala com o teu [grupo local](/community/). O grupo sabe onde falta cobertura, [que predefinição se usa na tua zona](/guides/settings/) e como dar nome aos repetidores. Procura repetidores perto de ti nos [mapas de cobertura](/map/) e diz olá nos [canais](/guides/channels/) públicos ou locais.

## Precisas de um? {#need}

Um repetidor retransmite todas as mensagens flood que ouve, e todos os repetidores ao alcance partilham o mesmo tempo de emissão. Onde a mesh já chega até ti, mais um repetidor acrescenta tráfego, não cobertura. Um companion num ponto alto, à janela do sótão ou numa varanda, pode ser suficiente.

Instala um repetidor onde falta cobertura:

- os [mapas de cobertura](/map/) não mostram nenhum repetidor perto de ti, ou só mostram repetidores que o teu companion não ouve;
- o teu grupo local diz que a zona precisa de um.

## Escolhe um local {#site}

A altura vale mais do que a potência. O LoRa a 868 MHz propaga-se melhor com linha de vista desimpedida. Colinas, edifícios e árvores densas tiram muito mais alcance do que uns miliwatts a mais conseguem recuperar.

- **Sobe alto.** Um telhado, um mastro, um edifício alto ou uma colina cobrem muito mais do que um parapeito de janela. Mesmo poucos metros acima dos telhados à volta já ajudam.
- **Deixa a antena desimpedida.** Monta-a acima das beiras do telhado, longe de metal, caleiras e outras antenas.
- **Verifica o que se vê.** Ferramentas como o [HeyWhatsThat](https://www.heywhatsthat.com/) mostram o que se vê a partir de um local. A app MeshCore [calcula até onde chega um repetidor nesse local](#check-site).
- **Deixa espaço livre.** Um caminho de rádio precisa de espaço livre à volta da linha direta, não só da própria linha. A 868 MHz, esse espaço é de cerca de 20 m à volta do meio de um caminho de 5 km. Num caminho de 20 km, é de cerca de 40 m.
- **Pede autorização.** Obtém o consentimento do dono do telhado ou do mastro. Combina com ele como vais chegar ao repetidor para a manutenção.

### Verificar um local na app {#check-site}

A versão 1.33 ou posterior da app MeshCore tem estas ferramentas em **Tools**, no
menu. Funcionam sem rádio ligado.

- **Line of Sight** desenha o terreno entre 2 pontos e o espaço de que o sinal
  precisa acima dele. Mantém premidos 2 pontos no mapa, ou toca em repetidores.
- **Antenna Coverage** mostra no mapa o que uma antena em 1 ponto consegue alcançar.
  Mantém premido um ponto ou toca num repetidor. Junta mais pontos para comparar locais.

Num computador, escolhe **Add Point** no menu da ferramenta e escreve as coordenadas.

Ambas as ferramentas partem de uma antena a 5 m no teu local, por isso
indica a altura que prevês nas definições da ferramenta. A Antenna Coverage parte
de uma antena recetora a 1 m. Sem um rádio ligado, a Line of Sight parte dos
915 MHz: indica a frequência da tua [predefinição](/guides/settings/) nas definições da ferramenta.

As ferramentas fazem cálculos com dados de altitude e não testam o teu rádio. Verifica tu mesmo as árvores e os edifícios novos. Depois leva um companion ao local e vê que repetidores ele ouve.

![Line of Sight na app MeshCore: o terreno entre 2 pontos e o espaço de que o sinal precisa acima dele](/media/guides/line-of-sight.webp)

![Antenna Coverage na app MeshCore: a área que uma antena numa colina consegue alcançar, mostrada num mapa](/media/guides/antenna-coverage.webp)

## Hardware {#hardware}

- **Placa.** Escolhe uma placa nRF52 de baixo consumo, como a [Heltec T114](/devices/), a RAK WisBlock ou o SenseCAP Solar Node. As placas ESP32 consomem mais energia (a página de dispositivos assinala-as como High), o que dificulta o funcionamento a energia solar.
- **Antena.** Usa uma antena feita para 868 MHz, montada na vertical. O [guia de antenas](/guides/antenna/) explica os tipos, os conectores, o cabo e a montagem. O ganho da antena conta para o limite legal de potência: consulta os [Limites legais](#legal).
- **Cabo.** Mantém o cabo coaxial curto, ou usa cabo de baixas perdas. A 868 MHz, poucos metros de cabo fino podem custar-te metade da potência.
- **Caixa.** Uma caixa à prova de intempéries (IP65 ou melhor) com bucim, um orifício de ventilação ou drenagem contra a condensação, e cor clara ou proteção solar. As baterias sofrem com o calor e não podem ser carregadas abaixo de zero graus.
- **Raios.** Uma antena num telhado é um alvo. Segue as regras locais de ligação à terra, ou monta-a onde um raio não chegue à instalação elétrica do edifício.

## Energia e dimensionamento solar {#power}

Um repetidor solar tem de sobreviver às semanas mais escuras do inverno. Liga primeiro a poupança de energia: depois de `powersaving on`, o repetidor dorme entre pacotes. Funciona em placas nRF52 e em placas ESP32 cujo firmware não tenha bridge. Depois dimensiona a bateria e o painel:

1. **Mede o consumo.** Liga o repetidor já configurado a um medidor de energia USB durante um dia. Lê a energia consumida em watts-hora (Wh). O tráfego na tua zona altera o valor, por isso mede no local, se puderes.
2. **Acrescenta reserva.** Planeia a capacidade da bateria para pelo menos 5 a 7 dias sem sol útil.
3. **Vê quanto sol tens no inverno.** A [ferramenta PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) da UE, gratuita, mostra quanta energia um painel produz por mês em qualquer local. Usa o mês com menos sol.
4. **Dimensiona o painel.** O painel tem de repor o consumo de cada dia nesse pior mês, com margem para as perdas de carregamento.

Um exemplo prático, com valores hipotéticos: um repetidor que consome 1 Wh por dia precisa de uma bateria de pelo menos 7 Wh para uma semana de reserva, cerca de 2 Ah de capacidade útil a 3.7 V. Se o PVGIS indicar que um painel de 1 W no teu local dá 0.5 Wh por dia em dezembro, precisas de um painel de pelo menos 2 W. Com 3 a 5 W, ficas com margem para nuvens, neve e envelhecimento.

## Configura-o {#config}

**Instala o firmware.** Usa o [instalador web](https://flasher.meshcore.io) e escolhe o firmware **Repeater** para a tua placa. Encontras os passos da instalação em [Primeiros passos](/get-started/#flash).

**Configura por USB.** Com o repetidor ainda ligado ao computador, abre [config.meshcore.io](https://config.meshcore.io) ou a consola do instalador. Também podes usar qualquer terminal série a 115200 baud. Os comandos mais importantes:

| O quê | Comando |
|---|---|
| Mudar a palavra-passe de administrador | `password <new password>` |
| Palavra-passe para convidados, que podem ler o estado | `set guest.password <password>` |
| Dar-lhe um nome | `set name <name>` |
| Predefinição de rádio: frequência, largura de banda, SF, CR (reinicia para aplicar) | `set radio 869.618,62.5,8,8` |
| Limite de duty cycle, em percentagem | `set dutycycle 10` |
| Potência de emissão do chip de rádio, em dBm | `set tx <dBm>` |
| Posição, para aparecer nos mapas | `set lat <degrees>` e `set lon <degrees>` |
| Dados de contacto para outros operadores | `set owner.info <text>` |
| Horas entre anúncios flood, os que toda a mesh ouve | `set flood.advert.interval <hours>` |
| Anunciá-lo agora | `advert` |
| Reiniciar | `reboot` |

A palavra-passe de administrador predefinida é `password`, e quem entrar com ela fica administrador. Muda-a antes de pores o repetidor no ar.

A palavra-passe de convidado vem vazia de origem. Assim, qualquer pessoa pode entrar como convidado sem
palavra-passe e ver o estado do repetidor e os seus vizinhos. Cada pedido gera
tráfego na mesh. Define uma palavra-passe de convidado e dá-a a quem
precisa dela.

**Escolhe um nome.** Dá-lhe um nome à maneira como o teu grupo local chama aos repetidores.
Se não tens grupo, põe no nome o país, a localidade e um nome curto, como
`DE-63477-MUF1`. Assim, os outros operadores veem onde está o repetidor. Um nome
tem até 31 bytes, e num anúncio que também leva uma posição cabem 23.

O exemplo de `set radio` acima é EU/UK (Narrow). Usa antes os valores da predefinição da tua zona: as [Definições recomendadas](/guides/settings/) indicam-nos por país.

**Acerta o relógio.** Sem um módulo de relógio (RTC), um repetidor perde as horas
a cada corte de energia e volta a maio de 2024. Enquanto funciona, o relógio também
se desvia: vai-se adiantando ou atrasando. Por isso, acerta o relógio de vez em quando: inicia
sessão remotamente a partir da app e usa `clock sync`, ou acerta as horas por USB. Com
um módulo RTC raramente precisas de o fazer: o módulo mantém as horas durante os cortes de energia e
desvia-se muito menos. O firmware deteta sozinho um módulo DS3231, RV3028, PCF8563 ou RX8130.

**Uma placa com GPS** acerta as duas coisas por ti. Depois de `gps on`, o repetidor
vai buscar as horas ao GPS a cada 30 minutos, e `gps setloc` copia a posição para
`lat` e `lon`. O GPS gasta energia durante todo o tempo em que está ligado. Se usas energia solar, executa
`gps setloc` uma vez no local e desliga o GPS com `gps off`. Depois disso, o relógio
volta a precisar de `clock sync`.

**Gere-o à distância.** Quando o repetidor estiver na mesh, inicia sessão na app MeshCore com a palavra-passe de administrador. Aí consultas o estado dele e usas os mesmos comandos por rádio. Alguns comandos só funcionam por USB, como `set freq` e a reposição de fábrica `erase`.

**Guarda a identidade.** Antes de um erase, escreve `get prv.key` por USB e guarda num lugar seguro a chave privada que aparece. Depois do erase, `set prv.key <key>` e um `reboot` devolvem ao repetidor a identidade antiga. Assim, os nós que o conhecem encontram-no com o mesmo prefixo.

A lista completa de comandos está na [referência da CLI do MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Atualiza-o sem fios {#update}

Com o repetidor lá em cima, atualizas o firmware a partir do chão. Inicia sessão na app MeshCore com a palavra-passe de administrador, abre a linha de comandos dele e escreve `start ota`. O que se segue depende da placa. As outras placas respondem `Error`, e essas atualizas por USB.

**Placas nRF52**, como RAK, Heltec T114, Seeed XIAO e SenseCAP Solar:

1. Descarrega o **ZIP** do novo firmware para a tua placa no [instalador web](https://flasher.meshcore.io).
2. Escreve `start ota`. O repetidor responde `OK` e aparece por Bluetooth como `<board>_OTA`, por exemplo `RAK4631_OTA`.
3. Abre a app nRF Device Firmware Update no telemóvel, escolhe o ZIP e o repetidor, e envia o ficheiro. Demora alguns minutos.

Instala o [bootloader OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
numa placa nRF52 antes de a montares lá em cima. Com o bootloader de origem, uma
atualização falhada só se repara por USB. Com o OTAFIX, a placa volta ao modo de
atualização e tentas outra vez por Bluetooth. `get bootloader.ver` mostra
qual deles a placa tem: com o OTAFIX, a resposta contém `OTAFIX`.

Depois de uma atualização, `ver` mostra a versão do firmware que está agora a correr.

**Placas ESP32**, como a Heltec V3 e a V4:

1. Descarrega do instalador web o `.bin` **non-merged** para a tua placa: o ficheiro sem "merged" no nome.
2. Escreve `start ota`. O repetidor abre uma rede WiFi chamada `MeshCore-OTA` e responde com o endereço da página de envio.
3. Dentro do alcance do WiFi, liga o telemóvel ou o portátil a essa rede, abre o endereço e envia o ficheiro.

## Limites legais {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
As predefinições europeias do MeshCore ficam na sub-banda **869.40-869.65 MHz**. Na UE, no Reino Unido, na Suíça e na Noruega, os dispositivos de curto alcance podem usá-la sem licença, dentro destes limites:

- no máximo **500 mW e.r.p.** de potência radiada;
- no máximo **10% de ciclo de trabalho**: não mais de 360 segundos de transmissão em cada hora, por dispositivo. Em alternativa, um dispositivo pode usar listen-before-talk com agilidade de frequência adaptativa, tal como definido na ETSI EN 300 220-2;
- todo o sinal, com 250 kHz de largura no máximo, tem de ficar dentro da sub-banda.

A banda é partilhada: não podes perturbar serviços licenciados, e outros podem perturbar-te a ti.
O rádio tem de ter marcação CE (na Grã-Bretanha, CE ou UKCA).
{{< /callout >}}

Fontes: [Recomendação CEPT ERC 70-03](https://docdb.cept.org/document/845), Anexo 1, banda h1.7; [Decisão 2006/771/CE da Comissão](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) e respetivas alterações; [ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), banda O.

### Potência: e.r.p. e a tua antena {#erp}

O limite aplica-se à potência *radiada*, medida em relação a uma antena dipolo simples (e.r.p.). O ganho da antena conta e a perda no cabo desconta. Os fabricantes indicam o ganho da antena em dBi, o que dá mais 2.15 dB do que o mesmo ganho em dBd (relativo a um dipolo). Mantém esta soma igual ou inferior a 27 dBm (500 mW):

> potência de transmissão (dBm) + ganho da antena (dBi) − perda no cabo (dB) − 2.15 ≤ 27

- Uma placa que transmite 22 dBm para uma antena de 5 dBi, através de um cabo com 1 dB de perda: 22 + 5 − 1 − 2.15 = 23.85 dBm, cerca de 240 mW e.r.p. Dentro do limite.
- Uma placa com um amplificador de 30 dBm (1 W) e uma antena de 3 dBi: 30 + 3 − 2.15 = 30.85 dBm, cerca de 1.2 W e.r.p. Acima do limite: baixa a potência de transmissão.

`set tx` define a saída do chip LoRa, em dBm. O próprio chip SX1262 chega no máximo a 22 dBm. O firmware não verifica o número que introduzes. As placas com amplificador adicional, como a Heltec V4 ou a Station G2, transmitem muito mais do que o número que defines. Consulta a tabela do fabricante antes de o definires, e começa com um valor baixo.

### Ciclo de trabalho {#duty-cycle}

Um repetidor transmite para todos à sua volta, por isso gasta o tempo de emissão mais depressa do que um companion. O limitador do ciclo de trabalho do MeshCore vem predefinido em 50%, acima do que esta banda permite. Define-o para 10% em todos os repetidores:

```text
set dutycycle 10
```

### Precisão da frequência {#frequency}

O canal EU/UK (Narrow), 869.618 MHz com 62.5 kHz de largura de banda, chega até 869.649 MHz: menos de 1 kHz abaixo do limite superior da sub-banda. O sinal tem de ficar dentro da banda a qualquer temperatura. Para isso, é preciso um cristal com compensação de temperatura (TCXO). Quase todas as placas atuais têm um. As placas mais antigas sem TCXO, como a Heltec V2, desviam-se demasiado para funcionarem de forma fiável a 62.5 kHz.

### Notas por país {#countries}

- **Os Estados-Membros da UE** têm de disponibilizar esta sub-banda nestas condições (Decisão 2006/771/CE, artigo 3).
- **Reino Unido:** os mesmos limites, na [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices) do Ofcom.
- **Suíça e Liechtenstein:** os mesmos limites, na [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09) do OFCOM.
- **Noruega:** os mesmos limites, no [regulamento sobre autorizações gerais](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Estas notas não são aconselhamento jurídico. As regras mudam: em caso de dúvida, confirma junto do regulador do teu país.

## Lista de verificação da instalação {#checklist}

Antes de instalares o repetidor no alto, percorre a
[lista de verificação do repetidor](/guides/repeater-checklist/). A lista indica cada ponto a
verificar, com o comando que o mostra.
