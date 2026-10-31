---
title: Colabora
lead: Un grupo de voluntarios escribe, revisa y traduce esta guía. Aquí ves cómo ayudar, con o sin cuenta de GitHub.
description: Añade tu comunidad, un dispositivo o un proyecto, revisa una traducción o mejora una guía en meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-31'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Todo el contenido de este sitio está en un
[repositorio público de GitHub](https://github.com/meshcore-europe/meshcore-info.eu). Los cambios pequeños
se envían con un formulario de GitHub (una incidencia o «issue»). Los cambios más grandes se envían como pull
request: una propuesta de cambio en los archivos que revisa una persona responsable del sitio. Una persona responsable
comprueba cada cambio antes de que se publique.

¿No tienes cuenta de GitHub? Cuéntanoslo en [Discord](https://discord.meshcore-info.eu/): un
grupo que falta, un dato erróneo o una traducción que suena rara. Un voluntario
se encarga del resto.

## Añade tu comunidad {#community}

¿Llevas un grupo local de MeshCore abierto a todo el mundo? Rellena el
[formulario de comunidad](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
con el nombre, la zona y los enlaces públicos. Cuando lo añadamos, tu grupo aparecerá
en la página de [Grupos locales](/community/) en todos los idiomas.

## Propón un dispositivo o un proyecto {#device-project}

La [página de dispositivos](/devices/) recoge especificaciones de la documentación del fabricante
y nunca enlaza a tiendas. Propón hardware con el
[formulario de dispositivo](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
¿Has creado una app, una herramienta, un puente o un diseño de hardware para MeshCore con código fuente
público? Añádelo con el
[formulario de proyecto](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Revisa una traducción {#translate}

Las páginas en otros idiomas empiezan como traducciones automáticas y lo indican
arriba. Las traducciones están en su propio repositorio,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), así que
nunca tienes que tocar el código del sitio. Si dominas uno de los idiomas,
puedes mejorarla:

1. Abre la página y pulsa «Ayuda a mejorar esta traducción». Se abre el
   archivo en GitHub, donde puedes editarlo en el navegador.
2. Corrige la redacción. Deja los enlaces, el código, los números y los nombres como MeshCore
   tal como están.
3. En el bloque `translation` de arriba, cambia `status: ai` por
   `status: human` y propón el cambio.

¿Has encontrado una palabra incorrecta pero no tienes tiempo de corregirla? Avísanos con el
[formulario de traducción](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Mejora una guía {#guides}

Las guías se escriben primero en inglés y después se traducen. Puedes enviar correcciones
y temas nuevos con el
[formulario de contenido](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
o con una pull request. Cada dato necesita una fuente: el firmware de MeshCore y su
documentación, un regulador de radio o un fabricante. Escribe con tus propias palabras. Una
cita breve con su fuente está bien.

La [guía para colaboradores](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
explica cómo trabajar en el sitio desde tu propio ordenador.

## Estado de las traducciones {#coverage}

«Revisada» significa que una persona la ha revisado;
«Automática» significa traducida por máquina y aún sin revisar;
«Desactualizada» significa que el texto en inglés cambió después de hacer la traducción;
«Falta» significa que la página aún no tiene traducción.

{{< coverage >}}

## Créditos {#credits}

El sitio está hecho con [Astro](https://astro.build/). Usa las tipografías
IBM Plex Sans e IBM Plex Mono, bajo la licencia SIL Open Font License. Las traducciones
siguen las
convenciones de [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) y
comparten sus glosarios de MeshCore. El desarrollo de MeshCore se hace en
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Los textos y las traducciones tienen licencia CC BY 4.0, y el código, licencia MIT.
