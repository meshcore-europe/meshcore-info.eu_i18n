---
title: Colabora
lead: Esta guía la escriben, revisan y traducen voluntarios. Así puedes ayudar, con o sin cuenta de GitHub.
description: Añade tu comunidad, un dispositivo o un proyecto, revisa una traducción o mejora una guía en meshcore-info.eu.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-26'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
---

Todo el contenido de este sitio está en un
[repositorio público de GitHub](https://github.com/meshcore-europe/meshcore-info.eu). Los cambios
pequeños se proponen con un formulario en GitHub (una issue). Los cambios mayores
entran como pull request: una propuesta de cambio en los archivos que revisa un
mantenedor. Un mantenedor comprueba cada cambio antes de publicarlo.

¿No tienes cuenta de GitHub? Cuéntanoslo en [Discord](https://discord.meshcore-info.eu/): un
grupo que falta, un dato erróneo o una traducción que suena rara. Un voluntario
se encarga a partir de ahí.

## Añade tu comunidad {#community}

¿Llevas un grupo local de MeshCore abierto a cualquiera? Rellena el
[formulario de comunidad](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
con el nombre, la zona y los enlaces públicos. Una vez añadido, tu grupo aparece
en la página [Grupos locales](/community/) en todos los idiomas.

## Propón un dispositivo o un proyecto {#device-project}

La [página de dispositivos](/devices/) recoge especificaciones de la documentación
de los fabricantes y nunca enlaza a tiendas. Propón hardware con el
[formulario de dispositivo](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
¿Has creado una app, una herramienta, un puente o un diseño de hardware para MeshCore con código
fuente público? Añádelo con el
[formulario de proyecto](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Revisa una traducción {#translate}

Las páginas en otros idiomas empiezan como traducciones automáticas y lo indican al
principio. Las traducciones están en su propio repositorio,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), así que
nunca tienes que tocar el código del sitio. Si dominas uno de los idiomas,
puedes mejorarla:

1. Abre la página y sigue el enlace "Ayuda a mejorar esta traducción". Abre el
   archivo en GitHub, donde puedes editarlo desde el navegador.
2. Corrige la redacción. Deja los enlaces, el código, los números y los nombres como MeshCore
   exactamente como están.
3. En el bloque `translation` del principio, cambia `status: ai` por
   `status: human` y propón el cambio.

¿Has visto una palabra mal traducida pero no tienes tiempo de corregirla? Notifícalo con el
[formulario de traducción](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Mejora una guía {#guides}

Las guías se escriben primero en inglés y se traducen a partir de ahí. Las correcciones
y los temas nuevos son bienvenidos a través del
[formulario de contenido](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
o de un pull request. Cada dato necesita una fuente: el firmware de MeshCore y su
documentación, un regulador de radio o un fabricante. Escribe con tus propias palabras. Una
cita breve con su fuente está bien.

La [guía para colaboradores](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
explica cómo trabajar en el sitio desde tu propio ordenador.

## Estado de las traducciones {#coverage}

"Revisada" significa que una persona la ha comprobado;
"Automática" significa traducida por máquina y aún sin revisar;
"Desactualizada" significa que el texto en inglés cambió después de hacer la traducción;
"Falta" significa que la página aún no tiene traducción.

{{< coverage >}}

## Créditos {#credits}

El sitio está construido con [Astro](https://astro.build/). Usa las tipografías
IBM Plex Sans e IBM Plex Mono, bajo la SIL Open Font License. Las traducciones
siguen las
convenciones de [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) y
comparten sus glosarios de MeshCore. MeshCore se desarrolla en
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Los textos y las traducciones tienen licencia CC BY 4.0, y el código, licencia
MIT.
