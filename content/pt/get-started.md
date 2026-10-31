---
title: Começar
lead: Do equipamento novo à tua primeira mensagem na mesh. Precisas de uma placa LoRa, de um computador com Chrome ou Edge e de um telemóvel ou portátil para a aplicação.
description: Instala o MeshCore a partir do browser, emparelha a aplicação, escolhe o preset de rádio da tua zona, envia a primeira mensagem e entra no canal local.
eyebrow: 6 passos · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-10-31'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Estes passos seguem o firmware MeshCore v1.18.0 e as ferramentas oficiais de
outubro de 2026. Os nomes dos menus na aplicação podem variar um pouco entre versões.

## 1. Escolhe um dispositivo {#device}

Serve qualquer placa da [página de dispositivos](/devices/) que indique companion.
Para o teu primeiro nó, escolhe um *companion*: o rádio a partir do qual envias
mensagens. Emparelha-o com o telemóvel ou o portátil por Bluetooth ou USB. Também
podes escolher um com ecrã e teclado próprios, que funciona sozinho.

Compra a versão de 868 MHz. A antena incluída cumpre a função; o
[guia de antenas](/guides/antenna/) explica como a verificar.

{{< callout type="warning" >}}
Monta a antena antes de ligares o rádio. Um rádio LoRa que transmite sem
antena pode danificar o próprio chip.
{{< /callout >}}

## 2. Instala o firmware {#flash}

1. Liga o dispositivo ao computador com um cabo USB de dados.
2. Abre o instalador web em [flasher.meshcore.io](https://flasher.meshcore.io)
   no Chrome ou no Edge. O instalador usa Web Serial, que os outros browsers não têm.
3. Escolhe o teu dispositivo e depois o firmware **Companion** para **Bluetooth** (ou
   USB, se só o fores usar com um cabo ligado ao computador).
4. Instala o firmware. Algumas placas têm primeiro de entrar em modo de atualização;
   o instalador explica-te como.

Usa *erase* só quando quiseres começar do zero: apagar elimina a identidade do
dispositivo e os teus contactos. Nas atualizações seguintes, instala sem apagar.
Para manteres a identidade quando apagas, exporta antes na aplicação a chave
privada do teu companion e importa-a no fim.

## 3. Instala a aplicação {#app}

A aplicação oficial do MeshCore existe para Android, iOS, Windows e macOS;
em [meshcore.io](https://meshcore.io) encontras as ligações para todas as versões.
Há também uma aplicação web em [app.meshcore.nz](https://app.meshcore.nz), que
funciona no Chrome ou no Edge num computador.

## 4. Emparelha o teu nó {#pair}

Liga o nó, abre a aplicação e liga-te a ele por Bluetooth. Quando te pedirem
um PIN:

- num nó **com** ecrã, aparece um PIN; escreve esse;
- num nó **sem** ecrã, o PIN é `123456`.

Se o emparelhamento falhar, remove o dispositivo das definições de Bluetooth do
telemóvel e tenta de novo. Depois dá um nome ao teu nó. Os outros veem este nome,
por isso não uses o teu nome completo nem a tua morada, a não ser que queiras.

## 5. Escolhe o preset de rádio da tua zona {#preset}

Todos os rádios de uma zona usam a mesma frequência e as mesmas definições.
Caso contrário, não se ouvem uns aos outros. Nas definições de rádio da aplicação,
escolhe o preset que a tua zona usa. Fora das zonas abaixo, a Europa usa
**EU/UK (Narrow)**. Os Países Baixos, a Chéquia, a Hungria, a Eslováquia, Portugal
e a Suíça têm o seu próprio preset, e o Limburgo, nos Países Baixos, tem uma variante:

{{< presets >}}

O teu dispositivo não tem o preset da tua zona? Introduz à mão os 4 valores da
tabela nas definições de rádio da aplicação: frequência, largura de banda,
spreading factor e coding rate. Um nó com outros valores não ouve a mesh.

Tens dúvidas? O teu [grupo local](/community/) sabe que preset a tua zona usa.
A aplicação descarrega esta lista do projeto MeshCore, por isso um preset novo
não exige atualizar a aplicação.

## 6. Diz olá {#hello}

1. **Anuncia-te.** Envia um *anúncio* a partir da aplicação. Um anúncio "flood"
   passa pelos repetidores (nós que reencaminham mensagens), e assim todos na
   mesh te podem adicionar.
   Os companions nunca se anunciam automaticamente.
2. **Encontra outras pessoas.** As pessoas aparecem nos teus contactos quando os
   anúncios delas te chegam. Por omissão, os repetidores enviam um anúncio flood
   a cada 47 horas, por isso a tua lista pode demorar 2 dias a encher.
3. **Envia uma mensagem.** Abre um contacto e escreve. A primeira mensagem
   espalha-se em flood pela rede; o destinatário devolve o caminho que ela seguiu,
   e as mensagens seguintes usam esse caminho.
4. **Entra em canais.** O canal **Public** já vem configurado; tudo o que lá
   escreves chega a todos na mesh. Para adicionares o *canal hashtag* da tua
   região (um nome que começa por `#`), escreve o nome dele. O teu
   [grupo local](/community/) diz-te que canais estão ativos.

## Quando algo não funciona {#troubleshooting}

**A aplicação não encontra o meu dispositivo por Bluetooth.**
Provavelmente instalaste o companion USB. Instala de novo e escolhe a versão
Bluetooth. No Heltec V3, a pequena antena Bluetooth integrada tem pouco alcance;
mantém o telemóvel perto.

**O emparelhamento falha sempre.**
Remove o dispositivo das definições de Bluetooth do telemóvel, reinicia o Bluetooth
e emparelha de novo com o PIN do ecrã ou com `123456`.

**Não aparece ninguém nos meus contactos.**
Confirma que o teu preset corresponde ao da tua zona. Envia um anúncio flood. Se
não houver nenhum repetidor ao alcance, só ouves rádios próximos; a
[página do mapa](/map/) mostra onde estão os repetidores.

**Um contacto aparece como "visto pela última vez" há dias, embora esteja ativo.**
Um dos dois nós tem a hora errada. Um companion recebe a hora do teu telemóvel;
nos repetidores e nos room servers (nós que guardam mensagens para um grupo),
é o dono que tem de acertar a hora.

**Uma mensagem direta nunca chega.**
Tu e a outra pessoa têm de ter um ao outro como contacto. Um nó descarta mensagens de
quem não conhece, sem avisar o remetente. Envia um anúncio flood e pede à outra
pessoa que também envie um. Confirma que a aplicação adiciona contactos novos
automaticamente; só adiciona nós dentro do limite de saltos.

**Os contactos antigos funcionam, os novos nunca se ligam.**
A primeira mensagem vai em flood, e um repetidor só a reencaminha se tiver a
região dessa mensagem. As mensagens seguintes usam um caminho aprendido, que
nenhuma verificação de região bloqueia. Pergunta ao teu [grupo local](/community/)
que regiões têm os repetidores à tua volta e vê
[as definições para a tua zona](/guides/settings/#traffic).

**A aplicação já não se liga ao teu companion.**
Algumas placas têm um botão de utilizador, como certas placas RAK e o Heltec T114.
Mantém-no premido nos primeiros 8 segundos depois de a placa arrancar. O companion
abre então uma consola de recuperação por USB. Na consola em
[flasher.meshcore.io](https://flasher.meshcore.io), `set pin <pin>` define um
novo PIN de Bluetooth e `erase` apaga o dispositivo.

**O instalador não consegue abrir a porta série no Linux.**
O teu utilizador precisa de acesso à porta, por exemplo com
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, ou de pertencer ao grupo `dialout`.

**Outro problema.** As
[FAQ do MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
abordam muitos outros problemas.
