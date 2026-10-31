---
title: O que é o MeshCore?
lead: O MeshCore envia mensagens de texto por rádio, de nó em nó. Funciona sem internet e sem assinatura.
description: 'O que o MeshCore é e não é: a mesh, companions, repetidores e room servers, o encaminhamento, a encriptação e a banda de 868 MHz na Europa.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '78bc31e8'
  seeded: '2026-10-31'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['aa768ac3', 'c9b24089', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '655373a9', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b9fc8810', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '0eb54b47', '02f1fe2f', 'e6b5b258']
---

O MeshCore é software livre para pequenos rádios LoRa. O LoRa é uma técnica de
rádio que envia poucos dados a grande distância, com muito pouca energia. Um
rádio com o MeshCore chama-se *nó*. Ligado à app no teu telemóvel ou portátil,
ou com ecrã e teclado próprios, envia texto a pessoas a quilómetros de
distância. Não há antena de operador, router nem fornecedor pelo meio.

O software é open source e é desenvolvido em
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) sob a licença
MIT.

## O que o MeshCore não é {#not}

És novo no mundo da rádio? Estas são as coisas que as pessoas mais vezes
esperam do MeshCore e que ele não faz.

- **Não é a internet nem um telefone.** O MeshCore envia mensagens de texto
  curtas, mais ou menos do tamanho de um SMS no teu telemóvel. Não há voz,
  fotos, vídeo nem sites, e não consegues contactar um número de telefone
  normal.
- **Não é um serviço de emergência.** Nenhum serviço de emergência está à
  escuta na mesh, e ninguém garante que alguém leia a tua mensagem. Numa
  emergência, liga para o 112.
- **Não é instantâneo nem chega a todo o lado.** Uma mensagem salta de rádio
  em rádio e pode demorar alguns segundos, ou nem chegar. Se passa ou não
  depende dos repetidores à tua volta, da altura, dos edifícios e da tua
  antena. Um rádio pequeno dentro de casa muitas vezes não chega a ninguém.
  Um repetidor num telhado chega a quilómetros.
- **Não é um serviço que alguém gere por ti.** Não há fornecedor, nem apoio
  ao cliente, nem garantia de cobertura. A mesh existe onde pessoas da
  comunidade instalaram repetidores, e em mais lado nenhum.
- **Nem tudo o que lá circula é privado.** As mensagens diretas são
  encriptadas, mas qualquer pessoa pode ler o Public e os canais com hashtag.
  O nome do teu nó e a posição que partilhas ficam visíveis para todos ao
  alcance. Os [observers](/network/) enviam o que ouvem para mapas públicos.
  A [secção sobre encriptação](#encryption) explica o que fica privado.
- **Não é ilimitado.** Todos numa zona partilham um único canal de rádio, e
  as regras da [banda de 868 MHz](#band) limitam quanto tempo cada rádio pode
  emitir. Cada mensagem tira tempo de emissão a todos os outros. Por isso,
  bots, anúncios frequentes e mensagens de teste tornam a mesh mais lenta para
  todos.
- **Não é o Meshtastic.** O Meshtastic é outro sistema, que funciona em placas
  muito parecidas. Os dois não comunicam entre si.

## A mesh num minuto {#mesh}

Um rádio LoRa chega a alguns quilómetros numa cidade, e muito mais longe a
partir de um monte ou de um telhado. Para irem mais longe, os rádios
retransmitem as mensagens uns dos outros: isso é uma *mesh*. No MeshCore, quem
retransmite são rádios chamados *repetidores*. Quando um repetidor ouve uma
mensagem, volta a enviá-la, e assim ela pode atravessar uma região inteira.

A mesh não tem dono. Cada nó e cada repetidor pertence a alguém da comunidade.
A mesh chega até onde chegam os repetidores dessas pessoas.

## Os 3 tipos de nó {#roles}

Escolhes o tipo de um nó quando instalas o firmware. O teu primeiro nó é um
companion.

**Companion.** O teu próprio rádio. Emparelha-se com a app MeshCore no teu
telemóvel ou portátil por Bluetooth ou USB. Alguns têm ecrã e teclado
próprios. É na app que lês e escreves. O companion guarda os teus contactos e
canais, e as mensagens que chegaram enquanto a app estava desligada. Um
companion não retransmite mensagens de outras pessoas.

**Repetidor.** Um rádio instalado num sítio alto que retransmite mensagens para
todos. A maioria funciona a energia solar. Só precisas de ter um teu onde a
mesh ainda não chega. Não tem app própria. Configura-lo por USB, ou entras com
uma palavra-passe e geres o repetidor por rádio. O
[guia do repetidor](/repeater-guide/) mostra como.

**Room server.** Um pequeno quadro de mensagens na mesh. Quando entras,
recebes as publicações que perdeste enquanto estavas fora de alcance, até às
últimas 32. Guarda-as só em memória, por isso um reinício ou um corte de
energia apaga-as. Um grupo local usa um para avisos.

## Como uma mensagem encontra o caminho {#routing}

Cada nó tem uma chave secreta e uma chave pública. A chave pública é a sua
identidade. Um nó apresenta-se com um *anúncio*: um pacote assinado com o seu
nome e, se quiseres, a sua posição. Alguém aparece nos teus contactos depois de
te chegar um dos anúncios dessa pessoa, ou quando lês o código QR dela. A app
tem um botão para enviares o teu.

A tua primeira mensagem a um contacto sai como *flood*. Cada repetidor que a
ouve retransmite-a uma vez e junta-lhe o seu próprio ID curto. A resposta traz
essa lista de IDs de volta. A partir daí, as tuas mensagens para esse contacto
seguem o caminho registado, e só os repetidores desse caminho emitem. Quando o
caminho se quebra, a app volta a fazer flood.

As mensagens para um canal não têm um endereço único, por isso fazem sempre
flood. Os repetidores lembram-se do que retransmitiram há pouco e descartam as
cópias que voltam a chegar por outro caminho. Uma mensagem pode atravessar até
64 repetidores, ou 32 quando o preset usa IDs de 2 bytes.

## Encriptação e privacidade {#encryption}

As tuas mensagens diretas são encriptadas de ponta a ponta: só tu e a outra
pessoa as conseguem ler. Um repetidor só vê a quem se destina um pacote através
de uma pista de 1 byte.

Os canais são encriptados com uma chave partilhada. Quem os pode ler depende de
quem tem essa chave:

- O **Public** vem configurado em todos os companions. A chave está publicada,
  por isso qualquer pessoa o pode ler.
- Os **canais com hashtag**, como `#utrecht`, tiram a chave do próprio nome.
  Quem souber o nome pode entrar, por isso trata-os também como públicos.
- Os **canais privados** usam uma chave aleatória que tu próprio partilhas, por
  exemplo como código QR.

Os anúncios são assinados mas não encriptados. O nome do teu nó, e a posição se
a partilhares, ficam visíveis para todos ao alcance. Escolhe um nome que não
diga mais do que queres.

## A banda de 868 MHz na Europa {#band}

Na Europa, o MeshCore usa uma pequena parte da banda de 868 MHz que qualquer
pessoa pode usar sem licença. O preset de rádio europeu, EU/UK (Narrow), fica
em 869.618 MHz, num canal de 62.5 kHz. Isso está dentro da sub-banda de
869.40-869.65 MHz, que permite até 500 mW e.r.p. Um dispositivo pode emitir aí
no máximo 10% do tempo. A
[secção legal do guia do repetidor](/repeater-guide/#legal) tem os detalhes e
os limites por país.

Todos numa zona usam o mesmo preset, senão os rádios não se ouvem uns aos
outros. Alguns países e regiões usam uma variante: o teu
[grupo local](/community/) sabe qual.

## Para que é usado {#uses}

- Manter o contacto em caminhadas, no mar e em festivais onde a rede móvel
  está sobrecarregada ou não existe.
- Um canal de reserva para a família ou os vizinhos quando a eletricidade ou as
  redes móveis falham.
- Conversa local em rádios que são das próprias pessoas.
- Fazer experiências com rádio, antenas, energia solar e software open source.

## De onde vêm os dados {#data}

A pesquisa na página dos [grupos locais](/community/) encontra um local através
de uma cópia das listas gratuitas de localidades e códigos postais do
[GeoNames](https://www.geonames.org/), com licença
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). A cópia está neste
site. A tua pesquisa nunca sai do teu dispositivo, e nenhum pedido vai para o
GeoNames.
