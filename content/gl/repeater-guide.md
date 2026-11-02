---
title: Guía de repetidores
lead: Un repetidor colocado no alto reenvía as mensaxes de todos os que ten arredor, por toda unha vila ou un val. Escolle un lugar, aliméntao co sol, configúrao e cumpre a lei.
description: 'Planifica, alimenta, configura e usa legalmente un repetidor MeshCore en Europa: elección do lugar, dimensionamento solar, axustes por CLI, límites de potencia e de ciclo de traballo en 868 MHz.'
eyebrow: 868 MHz · ata 500 mW · sen licenza
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-11-02'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Os repetidores sosteñen a malla. Os companion, as radios coas que envías mensaxes, non reenvían as mensaxes. Por iso, sen repetidores só chegas ás persoas que tes en alcance directo. Un repetidor ben situado amplía a malla para todos os que ten arredor. Esta guía segue o firmware MeshCore v1.18.0.

Antes de empezar, fala co teu [grupo local](/community/). Saben onde falta cobertura, [que preset se usa na túa zona](/guides/settings/) e como se lles pon nome aos repetidores. Mira nos [mapas de cobertura](/map/) os repetidores que tes preto e saúda nas [canles](/guides/channels/) públicas ou locais.

## Precisas un? {#need}

Un repetidor reenvía cada mensaxe flood que escoita, e todos os repetidores en alcance comparten o mesmo tempo de emisión. Onde a malla xa che chega, un repetidor máis engade tráfico, non cobertura. Pode bastarche un companion colocado no alto, nunha fiestra do faiado ou nun balcón.

Instala un repetidor onde falte cobertura:

- os [mapas de cobertura](/map/) non mostran ningún repetidor preto de ti, ou só algúns que o teu companion non escoita;
- o teu grupo local di que a zona precisa un.

## Escolle un lugar {#site}

A altura vale máis ca a potencia. LoRa en 868 MHz viaxa mellor cunha liña de visión despexada. Os outeiros, os edificios e as árbores mestas quitan moito máis alcance do que recuperan uns poucos milivatios de máis.

- **Sube ao alto.** Un tellado, un mastro, un edificio alto ou un outeiro cobren moito máis ca o peitoril dunha fiestra. Mesmo uns poucos metros por riba dos tellados da contorna axudan.
- **Deixa a antena despexada.** Móntaa por riba dos bordos do tellado, lonxe de metais, canalóns e outras antenas.
- **Comproba a vista.** Con ferramentas como [HeyWhatsThat](https://www.heywhatsthat.com/) podes ver o que se divisa desde un lugar. Se ves un punto, un repetidor situado alí está ao teu alcance.
- **Deixa marxe libre.** Un traxecto de radio precisa algo de espazo libre arredor da liña directa, non só a propia liña. En distancias longas, a parte central do traxecto debe pasar varios metros por riba dos obstáculos.
- **Pide permiso.** Consegue o consentimento do dono do tellado ou do mastro, e acorda como vas chegar ao repetidor para o mantemento.

## Hardware {#hardware}

- **Placa.** Escolle unha placa nRF52 de baixo consumo, como a [Heltec T114](/devices/), a RAK WisBlock ou o SenseCAP Solar Node. As placas ESP32 consomen máis (a páxina de dispositivos márcaas como High), e iso dificulta o funcionamento con enerxía solar.
- **Antena.** Usa unha antena feita para 868 MHz e móntaa en vertical. A [guía de antenas](/guides/antenna/) trata os tipos, os conectores, o cable e a montaxe. A ganancia da antena conta para o límite legal de potencia: consulta [Límites legais](#legal).
- **Cable.** Usa un cable coaxial curto ou un cable de baixa perda. En 868 MHz, uns poucos metros de cable fino poden facerche perder a metade da potencia.
- **Caixa.** Unha caixa estanca (IP65 ou mellor) cun prensaestopas, un orificio de ventilación ou drenaxe contra a condensación, e unha cor clara ou unha protección contra o sol. As baterías sofren coa calor e non se poden cargar por debaixo de cero graos.
- **Raios.** Unha antena nun tellado é un branco. Segue as normas locais de toma de terra, ou móntaa onde un raio non chegue á instalación eléctrica do edificio.

## Enerxía e dimensionamento solar {#power}

Un repetidor solar ten que aguantar as semanas máis escuras do inverno. Dimensiónao para elas:

1. **Mide o consumo.** Deixa o repetidor xa configurado funcionando un día cun medidor de potencia USB. Le a enerxía consumida en vatios hora (Wh). O tráfico da túa zona cambia a cifra, así que mide no lugar se podes.
2. **Engade reserva.** Calcula a capacidade da batería para polo menos 5 a 7 días sen sol útil.
3. **Busca o teu sol de inverno.** A [ferramenta PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) gratuíta da UE indica, para calquera lugar, canta enerxía produce un panel cada mes. Usa o mes con menos sol.
4. **Dimensiona o panel.** O panel ten que repoñer o consumo de cada día nese peor mes, con marxe para as perdas de carga.

Un exemplo práctico, con cifras supostas: un repetidor que consome 1 Wh ao día precisa unha batería de polo menos 7 Wh para unha semana de reserva, uns 2 Ah de capacidade útil a 3.7 V. Se PVGIS indica que un panel de 1 W dá no teu lugar 0.5 Wh ao día en decembro, precisas polo menos un panel de 2 W, e con 3 a 5 W quédache marxe para nubes, neve e envellecemento.

## Configúrao {#config}

**Instala o firmware.** Usa o [instalador web](https://flasher.meshcore.io) e escolle o firmware **Repeater** para a túa placa. Tes os pasos da instalación en [Primeiros pasos](/get-started/#flash).

**Configura por USB.** Co repetidor aínda conectado ao ordenador, abre [config.meshcore.io](https://config.meshcore.io) ou a consola do instalador. Tamén podes usar calquera terminal serie a 115200 baud. Os comandos máis importantes:

| Que | Comando |
|---|---|
| Cambiar o contrasinal de administración | `password <new password>` |
| Poñerlle nome | `set name <name>` |
| Preset de radio: frecuencia, largo de banda, SF, CR (reinicia para aplicalo) | `set radio 869.618,62.5,8,8` |
| Límite do ciclo de traballo, en porcentaxe | `set dutycycle 10` |
| Potencia de transmisión do chip de radio, en dBm | `set tx <dBm>` |
| Posición, para que apareza nos mapas | `set lat <degrees>` e `set lon <degrees>` |
| Datos de contacto para outros operadores | `set owner.info <text>` |
| Horas entre anuncios flood, os que escoita toda a malla | `set flood.advert.interval <hours>` |
| Anuncialo agora | `advert` |
| Reiniciar | `reboot` |

O contrasinal de administración predeterminado é `password`, e quen entre con el pasa a ser administrador. Cámbiao antes de poñer o repetidor a emitir.

O exemplo de `set radio` de arriba corresponde a EU/UK (Narrow). Usa no seu lugar os valores do preset da túa zona: en [Axustes recomendados](/guides/settings/) tes a lista por países.

**Pon o reloxo en hora.** Sen módulo de reloxo (RTC), un repetidor perde a hora en cada corte de luz e volve arrancar en maio de 2024. Mentres funciona, o seu reloxo tamén deriva: vaise adiantando ou atrasando. Por iso, axústao de cando en vez: entra en remoto desde a aplicación e usa `clock sync`, ou pon a hora por USB. Cun módulo RTC poucas veces che fará falta: mantén a hora durante os cortes de luz e deriva moito menos.

**Xestiónao en remoto.** Cando estea na malla, entra desde a aplicación MeshCore co contrasinal de administración. Alí les o seu estado e usas os mesmos comandos pola radio. Algúns comandos só funcionan por USB, como `set freq` e o restablecemento de fábrica `erase`.

**Conserva a súa identidade.** Antes dun borrado, escribe `get prv.key` por USB e garda nun lugar seguro a chave privada que aparece. Despois do borrado, con `set prv.key <key>` e un `reboot` o repetidor recupera a súa identidade anterior. Así, os nodos que o coñecen atópano co mesmo prefixo.

Tes a lista completa de comandos na [referencia da CLI de MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Actualízao polo aire {#update}

Cando o repetidor xa estea no alto, actualízalo desde o chan. Entra desde a aplicación MeshCore co contrasinal de administración, abre a súa liña de comandos e escribe `start ota`. O que vén despois depende da placa: outras placas responden `Error`, e esas actualízalas por USB.

**Placas nRF52**, como RAK, Heltec T114, Seeed XIAO e SenseCAP Solar:

1. Descarga o **ZIP** do novo firmware para a túa placa desde o [instalador web](https://flasher.meshcore.io).
2. Escribe `start ota`. O repetidor responde `OK` e aparece por Bluetooth como `<board>_OTA`, por exemplo `RAK4631_OTA`.
3. Abre a aplicación nRF Device Firmware Update no teléfono, escolle o ZIP e o repetidor, e súbeo. Tarda uns poucos minutos.

Instala o [cargador de arranque OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX) nunha placa nRF52 antes de subila ao alto. Co cargador de arranque de serie, unha actualización fallida só se pode arranxar por USB. Con OTAFIX, a placa volve ao modo de actualización e ti volves tentalo por Bluetooth.

**Placas ESP32**, como as Heltec V3 e V4:

1. Descarga desde o instalador web o `.bin` **non combinado** para a túa placa: o ficheiro sen "merged" no nome.
2. Escribe `start ota`. O repetidor abre unha rede WiFi chamada `MeshCore-OTA` e responde co enderezo da súa páxina de subida.
3. Dentro do alcance da WiFi, conecta o teléfono ou o portátil a esa rede, abre o enderezo e sube o ficheiro.

## Límites legais {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Os presets europeos de MeshCore están na subbanda **869.40-869.65 MHz**. Na UE, no Reino Unido, en Suíza e en Noruega, os dispositivos de curto alcance poden usala sen licenza, dentro destes límites:

- como máximo **500 mW e.r.p.** de potencia radiada;
- como máximo un **10% de ciclo de traballo**: non máis de 360 segundos de transmisión en cada hora, por dispositivo. Como alternativa, un dispositivo pode usar listen-before-talk con adaptive frequency agility, segundo a definición de ETSI EN 300 220-2;
- o sinal completo, de 250 kHz de largo como máximo, ten que quedar dentro da subbanda.

A banda é compartida: non podes perturbar os servizos con licenza, e outros poden perturbarte a ti.
A radio ten que levar a marca CE (en Gran Bretaña, CE ou UKCA).
{{< /callout >}}

Fontes: [Recomendación CEPT ERC 70-03](https://docdb.cept.org/document/845), anexo 1, banda h1.7; [Decisión 2006/771/CE da Comisión](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) e as súas modificacións; [ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), banda O.

### Potencia: e.r.p. e a túa antena {#erp}

O límite aplícase á potencia *radiada*, medida en relación cunha antena dipolo simple (e.r.p.). A ganancia da antena suma e a perda do cable resta. Os fabricantes indican a ganancia da antena en dBi, unha cifra 2.15 dB maior ca a mesma ganancia en dBd (en relación cun dipolo). Mantén esta suma en 27 dBm (500 mW) ou menos:

> potencia de transmisión (dBm) + ganancia da antena (dBi) − perda do cable (dB) − 2.15 ≤ 27

- Unha placa que transmite 22 dBm a unha antena de 5 dBi a través dun cable con 1 dB de perda: 22 + 5 − 1 − 2.15 = 23.85 dBm, uns 240 mW e.r.p. Dentro do límite.
- Unha placa cun amplificador de 30 dBm (1 W) e unha antena de 3 dBi: 30 + 3 − 2.15 = 30.85 dBm, uns 1.2 W e.r.p. Por riba do límite: baixa a potencia de transmisión.

`set tx` fixa a saída do chip LoRa, en dBm. O propio chip SX1262 chega como máximo a 22 dBm, e o firmware non comproba a cifra que introduces. As placas cun amplificador adicional, como a Heltec V4 ou a Station G2, transmiten moito máis ca a cifra que fixas. Consulta a táboa do fabricante antes de fixala e empeza por un valor baixo.

### Ciclo de traballo {#duty-cycle}

Un repetidor transmite para todos os que ten arredor, así que esgota o seu tempo de emisión máis rápido ca un companion. O limitador do ciclo de traballo de MeshCore vén fixado por defecto no 50%, por riba do que permite esta banda. Ponno no 10% en cada repetidor:

```text
set dutycycle 10
```

### Precisión da frecuencia {#frequency}

A canle EU/UK (Narrow), 869.618 MHz con 62.5 kHz de largo de banda, chega ata 869.649 MHz: menos de 1 kHz por debaixo do límite superior da subbanda. O sinal ten que quedar dentro da banda a calquera temperatura. Para iso fai falta un cristal compensado en temperatura (TCXO). Case todas as placas actuais levan un. As placas máis antigas sen el, como a Heltec V2, derivan demasiado para funcionar de maneira fiable a 62.5 kHz.

### Notas por países {#countries}

- **Os Estados membros da UE** teñen que pór esta subbanda á disposición nestas condicións (Decisión 2006/771/CE, artigo 3).
- **Reino Unido:** os mesmos límites, en Ofcom [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Suíza e Liechtenstein:** os mesmos límites, en OFCOM [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Noruega:** os mesmos límites, no [regulamento sobre autorizacións xerais](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Estas notas non son asesoramento legal. As normas cambian: se tes dúbidas, consulta o regulador do teu país.

## Lista de comprobación da instalación {#checklist}

- [ ] O dono do lugar deu o seu consentimento e podes chegar ao repetidor para o mantemento.
- [ ] A placa leva o firmware **Repeater**, e conectaches a antena antes do primeiro acendido.
- [ ] Cambiaches o contrasinal de administración.
- [ ] A radio coincide co [preset da túa zona](/guides/settings/) (`get radio`).
- [ ] Executaches `set dutycycle 10`.
- [ ] A potencia de transmisión máis a ganancia da antena non pasan de 500 mW e.r.p.
- [ ] Configuraches o nome, a posición e `owner.info`, para que os demais saiban quen o xestiona.
- [ ] O reloxo está en hora (`clock`).
- [ ] A caixa está selada, cun orificio de drenaxe ou ventilación, e o cable ten un bucle de goteo.
- [ ] A batería e o panel están dimensionados para o peor mes do inverno.
- [ ] Probáchelo desde lonxe coa aplicación antes de deixar o lugar.
- [ ] O teu grupo local sabe que xa está en funcionamento.
