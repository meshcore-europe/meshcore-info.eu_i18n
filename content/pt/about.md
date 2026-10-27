---
title: O que é o MeshCore?
lead: O MeshCore envia mensagens de texto por rádio, de nó para nó. Funciona sem internet e sem subscrição.
description: 'O que o MeshCore é e não é: a mesh, companions, repetidores e room servers, encaminhamento, cifragem e a banda de 868 MHz na Europa.'
eyebrow: MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '33e571f0'
  seeded: '2026-10-26'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['a3a6c1ff', '007314d2', 'f1f23981', '493b444f', '429f699c', 'f8008f48', '655373a9']
---

O MeshCore é software gratuito para pequenos rádios LoRa. LoRa é uma técnica de rádio
que envia poucos dados a grande distância, com muito pouca energia. Um rádio com MeshCore
chama-se *nó*. Emparelhado com a app no teu telemóvel ou portátil, ou com o seu próprio
ecrã e teclado, envia texto a pessoas a quilómetros de distância. Não há torre, router nem operador pelo meio.

O MeshCore envia apenas mensagens de texto curtas: nada de voz, fotografias ou tráfego de
internet.
Uma mensagem pode demorar alguns segundos, e chegar ou não depende dos
repetidores à tua volta. Não substitui os serviços de emergência: numa
emergência, liga para o 112.

O software é de código aberto, desenvolvido em
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) sob a licença
MIT.

## A mesh num minuto {#mesh}

Um rádio LoRa alcança alguns quilómetros numa vila, e muito mais a partir de uma
colina ou de um telhado. Para chegar mais longe, os rádios passam as mensagens uns aos outros: isso
é uma *mesh*. No MeshCore, quem faz essa passagem são rádios chamados *repetidores*. Um
repetidor que ouve uma mensagem volta a enviá-la, e assim ela pode atravessar uma região inteira.

A mesh não tem dono. Cada nó e cada repetidor pertence a alguém da
comunidade. A mesh vale o que valem os repetidores que as pessoas instalam.

## Os 3 tipos de nó {#roles}

Escolhes o tipo de um nó quando gravas o firmware. O teu primeiro nó é um companion.

**Companion.** O teu próprio rádio. Emparelha com a app MeshCore no teu telemóvel ou
portátil por Bluetooth ou USB; alguns têm ecrã e teclado próprios. É na app
que lês e escreves. O companion guarda os teus contactos e canais,
e as mensagens que chegaram enquanto a app não estava ligada. Um companion não passa mensagens de outros.

**Repetidor.** Um rádio colocado num ponto alto que passa mensagens para toda a gente. A maioria
funciona a energia solar. Só precisas de um teu onde a mesh ainda não
chega. Não tem app própria. Configuras o repetidor por USB, ou
entras com uma palavra-passe e geres-lo pelo rádio. O
[guia de repetidores](/repeater-guide/) explica como.

**Room server.** Um pequeno quadro de mensagens na mesh. Quando entras, recebes
as publicações que perdeste enquanto estavas fora de alcance, até às últimas 32. Um grupo local
usa um room server para avisos.

## Como uma mensagem encontra o caminho {#routing}

Cada nó tem uma chave secreta e uma chave pública. A chave pública é a sua identidade. Um nó
dá-se a conhecer com um *anúncio*: um pacote assinado com o seu nome e, se
quiseres, a sua posição. Alguém aparece nos teus contactos depois de um dos seus
anúncios te chegar, ou quando lês o seu código QR. A app tem um botão para enviares o teu.

A tua primeira mensagem para um contacto sai como *flood*. Cada repetidor que
a ouve passa-a uma vez, e junta pelo caminho o seu próprio ID curto. A resposta
traz essa lista de IDs de volta. A partir daí, as tuas mensagens para esse contacto
seguem o caminho registado, e só os repetidores nesse caminho transmitem. Quando o caminho
se quebra, a app faz flood outra vez.

As mensagens para um canal não têm um endereço único, por isso fazem sempre flood.
Os repetidores lembram-se do que passaram recentemente e descartam cópias que cheguem
de novo por outro caminho. Uma mensagem pode atravessar até 64 repetidores, ou 32 onde o preset usa IDs de 2
bytes.

## Cifragem e privacidade {#encryption}

As tuas mensagens diretas são cifradas de ponta a ponta: só tu e a outra pessoa
as conseguem ler. Um repetidor só vê a quem um pacote se destina como uma pista de 1 byte.

Os canais são cifrados com uma chave partilhada, por isso quem os pode ler depende de quem
tem essa chave:

- **Public** está configurado em todos os companions. A sua chave é publicada, por isso qualquer pessoa
  o pode ler.
- **Canais com hashtag**, como `#utrecht`, derivam a chave do seu nome.
  Quem souber o nome pode entrar, por isso trata-os também como públicos.
- **Canais privados** usam uma chave aleatória que tu próprio partilhas, por exemplo
  como código QR.

Os anúncios são assinados mas não cifrados. O nome do teu nó, e a sua posição se
a partilhares, ficam visíveis para todos ao alcance. Escolhe um nome que não diga mais
do que queres.

## A banda de 868 MHz na Europa {#band}

Na Europa, o MeshCore usa uma pequena parte da banda de 868 MHz que qualquer pessoa pode usar
sem licença. O seu preset de rádio europeu, EU/UK (Narrow), fica em
869.618 MHz num canal de 62.5 kHz. Isso está dentro da sub-banda
869.40-869.65 MHz, que permite até 500 mW e.r.p. Um dispositivo pode transmitir aí no máximo 10%
do tempo. A
[secção legal do guia de repetidores](/repeater-guide/#legal) tem os detalhes
e os limites por país.

Toda a gente numa área usa o mesmo preset, ou os rádios não se ouvem uns aos
outros. Alguns países e regiões usam uma variante: o teu
[grupo local](/community/) sabe qual.

## Para que as pessoas o usam {#uses}

- Manter o contacto em caminhadas, no mar e em festivais onde a rede móvel
  está sobrecarregada ou não existe.
- Um canal de reserva para a família ou os vizinhos quando a eletricidade ou as redes móveis
  falham.
- Conversa local em rádios que as próprias pessoas possuem.
- Experimentar com rádio, antenas, energia solar e software de código aberto.
