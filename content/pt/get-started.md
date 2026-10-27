---
title: Começar
lead: De uma placa nova até à tua primeira mensagem na mesh. Precisas de uma placa LoRa, de um computador com Chrome ou Edge, e de um telemóvel ou portátil para a app.
description: Instala o firmware MeshCore a partir do browser, emparelha a app, escolhe a predefinição de rádio da tua zona, envia a primeira mensagem e entra no canal local.
eyebrow: 6 passos · MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '68c89544'
  seeded: '2026-10-26'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', '36a3eba3', '6da9fd7a', 'cb5fb72e', '89626504', 'a419ce79', 'aa273b20']
---

Estes passos seguem o firmware MeshCore v1.18.0 e as ferramentas oficiais de
outubro de 2026. Os nomes dos menus na app podem variar um pouco entre versões.

## 1. Escolhe um dispositivo {#device}

Qualquer placa da [página de dispositivos](/devices/) marcada como companion serve. Para
o teu primeiro nó, escolhe um *companion*: o rádio a partir do qual envias mensagens. Emparelha-o com
o telemóvel ou o portátil por Bluetooth ou USB, ou escolhe um com ecrã
e teclado próprios, que funciona sozinho.

Compra a versão de 868 MHz. A antena fornecida chega; o
[guia de antenas](/guides/antenna/) explica como verificar uma.

{{< callout type="warning" >}}
Liga a antena antes de ligares o rádio. Um rádio LoRa que
transmite sem antena pode danificar o próprio chip.
{{< /callout >}}

## 2. Instala o firmware {#flash}

1. Liga o dispositivo ao computador com um cabo USB de dados.
2. Abre o flasher web em [flasher.meshcore.io](https://flasher.meshcore.io)
   no Chrome ou no Edge. Usa Web Serial, que os outros browsers não têm.
3. Escolhe o teu dispositivo e depois o firmware **Companion** para **Bluetooth** (ou
   USB, se só o fores usar com um cabo ligado ao computador).
4. Grava. Algumas placas entram primeiro em modo de atualização; o flasher explica
   como.

Só uses *erase* para começar do zero: apagar elimina a identidade do dispositivo
e os teus contactos. Nas atualizações seguintes, grava sem apagar.

## 3. Instala a app {#app}

A app oficial do MeshCore existe para Android, iOS, Windows e macOS;
[meshcore.io](https://meshcore.io) tem ligações para todas as versões. Há também uma
app web em [app.meshcore.nz](https://app.meshcore.nz) que corre no Chrome ou
no Edge num computador.

## 4. Emparelha o teu nó {#pair}

Liga o nó, abre a app e liga-te a ele por Bluetooth. Quando
te pedir um PIN:

- um nó **com** ecrã mostra um PIN; escreve esse;
- um nó **sem** ecrã usa `123456`.

Se o emparelhamento falhar, remove o dispositivo das definições de Bluetooth do telemóvel e
tenta outra vez. Depois dá um nome ao teu nó. Os outros veem este nome, por isso não uses
o teu nome completo nem a tua morada, a não ser que queiras.

## 5. Escolhe a predefinição de rádio da tua zona {#preset}

Todos os rádios de uma zona usam a mesma frequência e as mesmas definições, senão não
se ouvem uns aos outros. Nas definições de rádio da app, escolhe a predefinição da tua zona.
Fora das zonas abaixo, a Europa usa **EU/UK (Narrow)**. Os Países Baixos,
a Chéquia, a Hungria, a Eslováquia, Portugal e a Suíça têm a sua própria, e
Limburgo, nos Países Baixos, tem uma variante:

{{< presets >}}

Tens dúvidas? O teu [grupo local](/community/) sabe que predefinição a tua zona usa.
A app descarrega esta lista do projeto MeshCore, por isso uma predefinição nova
não exige atualizar a app.

## 6. Diz olá {#hello}

1. **Anuncia-te.** Envia um *anúncio* a partir da app. Um anúncio "flood"
   percorre os repetidores (nós que reencaminham mensagens), para que toda a gente
   na mesh te possa adicionar.
   Os companions nunca se anunciam automaticamente.
2. **Encontra os outros.** As pessoas aparecem nos teus contactos quando os anúncios delas chegam
   até ti. Por defeito, os repetidores enviam um anúncio flood a cada 47 horas, por isso a tua lista
   pode levar 2 dias a encher.
3. **Envia uma mensagem.** Abre um contacto e escreve. A primeira mensagem faz flood
   pela rede; quem a recebe devolve o caminho que ela percorreu, e as mensagens
   seguintes seguem esse caminho.
4. **Entra em canais.** O canal **Public** já está configurado; tudo o que
   escreveres lá chega a toda a gente na mesh. Adiciona o *canal hashtag*
   da tua região (um nome que começa por `#`) escrevendo o nome dele. O teu
   [grupo local](/community/) diz-te que canais estão ativos.

## Quando algo não funciona {#troubleshooting}

**A app não encontra o meu dispositivo por Bluetooth.**
Provavelmente instalaste o companion USB. Grava outra vez e escolhe a
versão Bluetooth. No Heltec V3, a pequena antena Bluetooth integrada
tem pouco alcance; mantém o telemóvel perto.

**O emparelhamento falha sempre.**
Remove o dispositivo das definições de Bluetooth do telemóvel, reinicia o Bluetooth
e emparelha outra vez com o PIN do ecrã ou com `123456`.

**Não aparece ninguém nos meus contactos.**
Confirma que a tua predefinição corresponde à tua zona. Envia um anúncio flood. Se não houver
nenhum repetidor ao alcance, só ouves os rádios mais próximos; a
[página do mapa](/map/) mostra onde estão os repetidores.

**Um contacto aparece como "visto pela última vez" há dias, apesar de estar ativo.**
Um dos dois nós tem a hora errada. Um companion recebe a hora do
teu telemóvel; os repetidores e os room servers (nós que guardam mensagens para um
grupo) precisam que o dono lhes acerte a hora.

**O flasher não consegue abrir a porta série no Linux.**
O teu utilizador precisa de acesso à porta, por exemplo com
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, ou pertencendo ao grupo
`dialout`.

**Outra coisa.** A
[FAQ do MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
cobre muitos mais problemas.
