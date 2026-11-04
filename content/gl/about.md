---
title: Que é MeshCore?
lead: MeshCore envía mensaxes de texto por radio, de nodo en nodo. Funciona sen internet e sen subscrición.
description: 'O que é e o que non é MeshCore: tipos de nodo, enrutamento, cifrado e a banda de 868 MHz.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '2a40da22'
  seeded: '2026-11-04'
  fields: {title: '06eda66b', lead: 'c0174569', description: 'c2255f49', eyebrow: '8610c822'}
  sections: ['aa768ac3', '92fc3ea7', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '203a07ef', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'ac039316', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '5d796ffb', '1a490368', 'f0dd237f', '3182d5c8', '02f1fe2f', 'e6b5b258']
---

MeshCore é software libre para radios LoRa pequenas. LoRa é unha técnica de
radio que envía poucos datos a moita distancia e consome moi pouca enerxía. Unha radio con MeshCore
chámase *nodo*. Coa aplicación do teu móbil ou portátil, ou coa súa propia
pantalla e teclado, o nodo envía texto a persoas que están a quilómetros de ti. Polo medio non hai torres, routers nin provedores.

O software é de código aberto. Desenvólvese en
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) con licenza
MIT.

## Que non é MeshCore {#not}

Acabas de chegar ao mundo da radio? Isto é o que a xente espera máis a miúdo de MeshCore,
e que non fai.

- **Non é internet nin un teléfono.** MeshCore envía mensaxes de texto curtas,
  máis ou menos do tamaño dunha mensaxe de texto no teu móbil. Non hai voz, fotos, vídeo
  nin webs, e non podes contactar cun número de teléfono normal.
- **Non é un servizo de emerxencias.** Ningún servizo de emerxencias se compromete a
  escoitar na malla, e ninguén promete que alguén lea a túa mensaxe.
- **Non é instantáneo nin chega a todas partes.** Unha mensaxe salta de radio en
  radio e pode tardar uns segundos, ou non chegar nunca. Que chegue ou non
  depende dos repetidores que teñas preto, da altura, dos edificios e da túa
  antena. Unha radio pequena dentro da casa moitas veces non chega a ninguén. Un repetidor nun tellado
  chega a quilómetros.
- **Non é un servizo que alguén xestione por ti.** Non hai provedor, nin servizo
  de axuda, nin promesa de cobertura. A malla existe onde a xente da
  comunidade instalou repetidores.
- **Non todo o que circula nela é privado.** As mensaxes directas van cifradas. Pero
  calquera pode ler Public e as canles con cancelo, e o nome e a posición
  compartida do teu nodo son visibles para todos os que están ao alcance.
  Os [observadores](/network/) envían a mapas públicos o que escoitan. A
  [sección sobre cifrado](#encryption) explica o que segue sendo privado.
- **Non é ilimitado.** Todos os dunha zona comparten unha soa canle de radio, e
  as normas da [banda de 868 MHz](#band) limitan canto tempo pode emitir cada radio.
  Cada mensaxe quítalles tempo de emisión a todos os demais. Por iso os bots, os anuncios frecuentes
  e as mensaxes de proba fan a malla máis lenta para todos.
- **Non é Meshtastic.** Meshtastic é un sistema distinto que funciona en
  placas moi parecidas. Os dous non se poden comunicar entre si.

## A malla nun minuto {#mesh}

Unha radio LoRa chega a uns poucos quilómetros nunha cidade, e moito máis lonxe desde un
outeiro ou un tellado. Para chegar máis lonxe, as radios reenvían as mensaxes unhas das outras: iso
é unha *malla*. En MeshCore, desa tarefa encárganse unhas radios chamadas *repetidores*. Cando un
repetidor escoita unha mensaxe, envíaa de novo, e así a mensaxe pode cruzar toda unha rexión.

A malla non ten dono. Cada nodo e cada repetidor pertence a alguén da
comunidade. A malla chega ata onde chegan os seus repetidores.

## Os 3 tipos de nodo {#roles}

Escolles o tipo de nodo ao instalarlle o firmware. O teu primeiro nodo é un compañeiro.

**Compañeiro.** A túa propia radio. Conéctala á aplicación MeshCore do teu móbil ou
portátil por Bluetooth ou USB; algunhas teñen pantalla e teclado propios. Na aplicación
les e escribes. O compañeiro garda os teus contactos e canles,
e as mensaxes que chegaron mentres a aplicación non estaba conectada. Un compañeiro non reenvía mensaxes doutras persoas.

**Repetidor.** Unha radio colocada en alto que reenvía as mensaxes de todo o mundo. A maioría
funciona con enerxía solar. Só necesitas o teu propio onde a malla aínda non
chega. Non ten aplicación propia. Configúralo por USB, ou
inicias sesión cun contrasinal e xestiónalo por radio. A
[guía de repetidores](/repeater-guide/) explica como facelo.

**Servidor de sala.** Un pequeno taboleiro de mensaxes na malla. Cando inicias sesión, recibes
as publicacións que perdiches mentres estabas fóra de alcance, ata as últimas 32. O servidor só as garda
na memoria, así que un reinicio ou un corte de luz bórraas. Os grupos locais usan
un para os avisos.

## Como atopa o camiño unha mensaxe {#routing}

Cada nodo ten unha clave secreta e unha clave pública. A clave pública é a súa identidade. Un nodo
preséntase cun *anuncio*: un paquete asinado co seu nome e, se queres,
a súa posición. Unha persoa aparece nos teus contactos despois de que che chegue un dos seus
anuncios, ou cando escaneas o seu código QR. A aplicación ten un botón para enviar o teu.

A túa primeira mensaxe a un contacto sae por *inundación*. Cada repetidor que
a escoita reenvíaa unha vez, e engade polo camiño o seu ID curto. A resposta
trae de volta esa lista de ID. A partir de aí, as túas mensaxes a ese contacto
seguen a ruta rexistrada, e só emiten os repetidores que están nela. Cando a ruta
se rompe, a aplicación volve usar a inundación.

As mensaxes a unha canle non teñen un único enderezo, así que sempre van por inundación.
Os repetidores lembran o que reenviaron hai pouco e descartan as copias que volven
chegar por outra ruta. Unha mensaxe pode cruzar ata 64 repetidores, ou 32 se a predefinición usa ID de 2
bytes.

## Cifrado e privacidade {#encryption}

As túas mensaxes directas van cifradas de extremo a extremo: só ti e a outra persoa
podedes lelas. Un repetidor só sabe para quen é un paquete por unha pista de 1 byte.

As canles cífranse cunha clave compartida, así que quen pode lelas depende de quen
teña esa clave:

- **Public** vén configurada en todos os compañeiros. A súa clave está publicada, así que calquera
  pode lela.
- **As canles con hashtag**, como `#utrecht`, obteñen a clave do seu nome.
  Calquera que coñeza o nome pode entrar, así que trátaas tamén como públicas.
- **As canles privadas** usan unha clave aleatoria que compartes ti, por exemplo
  cun código QR.

Os anuncios van asinados, pero non cifrados. Todo o mundo ao teu alcance ve o nome do teu nodo e,
se a compartes, a súa posición. Escolle un nome que non diga máis do
que queres.

## A banda de 868 MHz en Europa {#band}

En Europa, MeshCore usa unha pequena parte da banda de 868 MHz que calquera pode usar
sen licenza. A súa predefinición de radio europea, EU/UK (Narrow), está en
869.618 MHz, nunha canle de 62.5 kHz. Iso queda dentro da subbanda de 869.40-869.65 MHz,
que permite ata 500 mW e.r.p. Un dispositivo pode emitir nela como máximo o 10%
do tempo. A
[sección legal da guía de repetidores](/repeater-guide/#legal) ten os detalles
e os límites de cada país.

Todas as persoas dunha zona usan a mesma predefinición porque, se non, as súas radios non se poden escoitar
entre si. Algúns países e rexións usan unha variante: o teu
[grupo local](/community/) sabe cal.

## Para que o usa a xente {#uses}

- Manter o contacto en rutas de montaña, no mar e en festivais onde a rede móbil
  está saturada ou non existe.
- Unha canle de reserva para a familia ou a veciñanza cando falla a luz ou a rede
  móbil.
- Unha reserva para as autoridades locais cando fallan as súas redes habituais.
- Conversas locais en radios que son da propia xente.
- Manter en contacto un equipo de busca e rescate onde non hai rede móbil.
  MeshCore SAR, unha aplicación da comunidade que atopas en [Proxectos](/projects/), engade mapas e
  posicións compartidas.
- Comprobar un lugar afastado desde casa. Os repetidores e os nodos sensores informan da
  tensión da batería e doutras medidas cando llas pides.
- Vixiar un sensor. Un nodo sensor leva o firmware de MeshCore para medir
  cousas. Garda un historial da tensión da súa batería. Se inicias sesión como admin,
  avísate cando a batería está baixa. Os avisos para outras medidas engádelos ti
  co teu propio código.
- Accionar algo lonxano, como unha bomba. Iso engádelo ti ao firmware do sensor
  co teu propio código.
- Experimentar con radio, antenas, enerxía solar e software de código aberto.

Algunhas autoridades están a construír ou a probar un sistema de reserva baseado en MeshCore. Revisamos
estes exemplos en novembro de 2026.

- O ciclón Gabrielle cortou todas as comunicacións en Tairāwhiti, Nova Zelandia. En
  setembro de 2025, a xestión de emerxencias da rexión citou MeshCore como
  [unha de polo menos 6 vías de reserva para comunicarse](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Tamén estaba a construír repetidores solares como columna vertebral.
- O distrito alemán de Bad Kissingen
  [está a construír unha rede de texto con MeshCore](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  para autoridades, servizos de emerxencia e instalacións críticas. Os parques de bombeiros
  son os primeiros en conectarse.
- O concello de Hilversum, nos Países Baixos,
  [votou 34 a 1 a favor dunha proba](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  cun repetidor na torre da casa do concello. O municipio
  [avaliaraa no outono de 2027](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Dúas rexións de seguridade neerlandesas, que organizan a resposta ante unha crise, están
  a experimentar con MeshCore:
  [Limburgo do Sur](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  e [Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Drenthe di que aínda é cedo para saber como ou cando podería usalo.
- En Dalfsen, tamén nos Países Baixos, un grupo de voluntarios
  [leva a cabo un proxecto piloto xunto cos municipios](https://noodnetoverijssel.nl/).
  Usan primeiro a radio de voz, e MeshCore como segunda capa para o texto.

Ninguén che promete que alguén lea a túa mensaxe na malla preto de ti.

## De onde veñen os datos {#data}

A busca da páxina de [grupos locais](/community/) localiza un lugar cunha copia das
listas libres de lugares e códigos postais de [GeoNames](https://www.geonames.org/),
con licenza
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). A copia está neste
sitio. A túa busca nunca sae do teu dispositivo, e non se envía ningunha petición a
GeoNames.
