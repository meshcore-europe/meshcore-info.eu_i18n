---
title: Primeiros pasos
lead: Desde unha placa nova ata a túa primeira mensaxe na malla. Necesitas unha placa LoRa, un ordenador con Chrome ou Edge e un teléfono ou portátil para a app.
description: Instala MeshCore desde o navegador, emparella a app, escolle o preset de radio da túa zona, envía a túa primeira mensaxe e únete á canle local.
eyebrow: 6 pasos · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0c1b08d9'
  seeded: '2026-11-03'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '90f3d626', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '757c634a', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Estes pasos corresponden ao firmware MeshCore v1.18.0 e ás ferramentas oficiais de
outubro de 2026. Os nomes dos menús da app poden variar un pouco dunha versión a outra.

## 1. Escolle un dispositivo {#device}

Serve calquera placa da [páxina de dispositivos](/devices/) que indique companion. Para
o teu primeiro nodo, escolle un *companion*: a radio coa que envías mensaxes. Emparéllao
co teu teléfono ou portátil por Bluetooth ou USB, ou escolle un con pantalla
e teclado propios que funcione por si só.

Colle a versión de 868 MHz. A antena incluída cumpre ben; na
[guía de antenas](/guides/antenna/) ves como comprobar unha.

A túa placa leva agora Meshtastic? Ao flashear MeshCore substitúelo, e os dous
non se comunican entre si. [Se vés de Meshtastic](/about/#meshtastic)
recolle o que funciona doutro xeito.

{{< callout type="warning" >}}
Conecta a antena antes de acender a radio. Unha radio LoRa que
transmite sen antena pode danar o seu propio chip.
{{< /callout >}}

## 2. Instala o firmware {#flash}

1. Conecta o dispositivo ao ordenador cun cable USB de datos.
2. Abre o flasher web en [flasher.meshcore.io](https://flasher.meshcore.io)
   con Chrome ou Edge. O flasher usa Web Serial, e os outros navegadores non o teñen.
3. Escolle o teu dispositivo e despois o firmware **Companion** para **Bluetooth** (ou
   USB, se só o vas usar cun cable conectado ao ordenador).
4. Inicia a instalación. Algunhas placas teñen que entrar antes en modo de actualización; o flasher
   indícache como facelo.

Usa *erase* só se queres empezar de cero: ao borrar, eliminas a identidade do dispositivo
e os teus contactos. Nas actualizacións posteriores, instala o firmware sen borrar. Para conservar a
identidade tras un borrado, exporta antes a chave privada do companion desde a app
e impórtaa despois.

## 3. Instala a app {#app}

A app oficial de MeshCore está dispoñible para Android, iOS, Windows e macOS;
en [meshcore.io](https://meshcore.io) tes as ligazóns a todas as versións. Tamén hai
unha app web en [app.meshcore.nz](https://app.meshcore.nz) que funciona con Chrome ou
Edge nun ordenador.

## 4. Emparella o teu nodo {#pair}

Acende o nodo, abre a app e conéctate a el por Bluetooth. Cando
che pida un PIN:

- un nodo **con** pantalla mostra un PIN; escribe ese;
- un nodo **sen** pantalla usa `123456`.

Se o emparellamento falla, elimina o dispositivo dos axustes de Bluetooth do teléfono e
téntao de novo. Despois ponlle un nome ao nodo. Os demais verán ese nome, así que non uses
o teu nome completo nin o teu enderezo, salvo que queiras.

## 5. Escolle o preset de radio da túa zona {#preset}

Todas as radios dunha zona usan a mesma frecuencia e os mesmos axustes; se non, non se oen entre si.
Nos axustes de radio da app, escolle o preset que se usa na túa zona.
Fóra das zonas que aparecen a continuación, en Europa úsase **EU/UK (Narrow)**. Os Países Baixos,
Chequia, Hungría, Eslovaquia, Portugal e Suíza usan o seu propio preset, e
Limburgo, nos Países Baixos, ten unha variante:

{{< presets >}}

O teu dispositivo non ofrece o preset da túa zona? Introduce a man os 4 valores da
táboa nos axustes de radio da app: frecuencia, largura de banda, factor de espallamento
e taxa de codificación. Un nodo con outros valores non oe a malla.

Non o tes claro? O teu [grupo local](/community/) sabe que preset se usa na túa zona.
A app descarga esta lista do proxecto MeshCore, así que un preset novo non
require actualizar a app.

## 6. Saúda {#hello}

1. **Date a coñecer.** Envía un *advert* desde a app. Un advert "flood"
   viaxa a través dos repetidores (nodos que retransmiten as mensaxes), de modo que calquera
   persoa da malla pode engadirte.
   Os companions nunca se anuncian automaticamente.
2. **Atopa outras persoas.** A xente aparece nos teus contactos cando che chegan
   os seus adverts. Os repetidores envían por defecto un advert flood cada 47 horas, así que a túa lista
   pode tardar 2 días en encherse.
3. **Envía unha mensaxe.** Abre un contacto e escribe. A primeira mensaxe inunda
   a rede; o destinatario informa da ruta que seguiu, e as mensaxes
   seguintes van por esa ruta.
4. **Únete a canles.** A canle **Public** xa vén configurada; o que escribas nela chega a
   toda a xente da malla. Engade a *canle hashtag* da túa rexión (un nome que empeza por `#`)
   escribindo o seu nome. O teu
   [grupo local](/community/) dirache que canles están activas.

## Cando algo non funciona {#troubleshooting}

**A app non atopa o meu dispositivo por Bluetooth.**
Probablemente instalaches o companion USB. Instala de novo o firmware e escolle a
versión Bluetooth. No Heltec V3, a pequena antena Bluetooth integrada ten
pouco alcance; mantén o teléfono preto.

**O emparellamento falla unha e outra vez.**
Elimina o dispositivo dos axustes de Bluetooth do teléfono, reinicia o Bluetooth
e emparéllao de novo co PIN da pantalla ou con `123456`.

**Non aparece ninguén nos meus contactos.**
Comproba que o teu preset coincide co da túa zona. Envía un advert flood. Se non tes ningún
repetidor ao alcance, só oirás as radios próximas; na
[páxina do mapa](/map/) ves onde hai repetidores.

**Un contacto aparece con "last seen" de hai días aínda que está activo.**
Un dos dous nodos ten a hora mal. Un companion colle a hora do
teu teléfono; nos repetidores e nos servidores de sala (nodos que gardan mensaxes para un
grupo), ten que axustala o seu dono.

**Unha mensaxe directa nunca chega.**
Cada persoa ten que ter a outra como contacto. Un nodo descarta as mensaxes de quen
non coñece, sen avisar a quen as envía. Envía un advert flood e pídelle á
outra persoa que envíe un tamén. Comproba na app que engade os contactos novos
automaticamente; só engade nodos dentro do seu límite de saltos.

**Os contactos antigos funcionan, pero os novos nunca se conectan.**
A primeira mensaxe inunda a rede, e un repetidor só a retransmite se ten a
rexión da mensaxe. As mensaxes seguintes van por unha ruta aprendida, e ningunha comprobación de rexión as detén.
Pregúntalle ao teu [grupo local](/community/) que rexións teñen os repetidores
próximos, e revisa [os axustes da túa zona](/guides/settings/#traffic).

**A app xa non se conecta ao teu companion.**
Algunhas placas teñen un botón de usuario, como algunhas placas RAK e o Heltec T114.
Mantén o botón premido durante os primeiros 8 segundos despois de que a placa arranque. O companion abre
unha consola de rescate por USB. Na consola de
[flasher.meshcore.io](https://flasher.meshcore.io), `set pin <pin>` define un
novo PIN de Bluetooth e `erase` borra o dispositivo.

**O flasher non pode abrir o porto serie en Linux.**
O teu usuario necesita acceso ao porto, por exemplo con
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, ou pertencer ao grupo
`dialout`.

**Outra cousa.** A
[FAQ de MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
trata moitos máis problemas.
