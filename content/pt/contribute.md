---
title: Contribuir
lead: Este guia é escrito, verificado e traduzido por voluntários. Aqui explicamos como podes ajudar, com ou sem conta no GitHub.
description: Adiciona a tua comunidade, um dispositivo ou um projeto, revê uma tradução ou melhora um guia no meshcore-info.eu.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-26'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
---

Tudo o que está neste site vive num
[repositório público no GitHub](https://github.com/meshcore-europe/meshcore-info.eu). As pequenas alterações
passam por um formulário no GitHub (uma issue). Tudo o que for maior entra como pull
request: uma proposta de alteração aos ficheiros que um responsável revê. Um
responsável verifica cada alteração antes de ela ficar publicada.

Não tens conta no GitHub? Diz-nos no [Discord](https://discord.meshcore-info.eu/): um
grupo em falta, um facto errado ou uma tradução que soa estranha. A partir daí, um voluntário
trata do assunto.

## Adiciona a tua comunidade {#community}

Tens um grupo local de MeshCore a que qualquer pessoa se pode juntar? Preenche o
[formulário de comunidade](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
com o nome, a área e as ligações públicas. Depois de adicionado, o teu grupo aparece
na página [Grupos locais](/community/) em todas as línguas.

## Sugere um dispositivo ou um projeto {#device-project}

A [página de dispositivos](/devices/) lista especificações retiradas da documentação
dos fabricantes e nunca liga a lojas. Sugere hardware com o
[formulário de dispositivo](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Criaste uma app, uma ferramenta, uma ponte ou um projeto de hardware para MeshCore com código-fonte
público? Adiciona-o com o
[formulário de projeto](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Revê uma tradução {#translate}

As páginas noutras línguas começam como traduções automáticas e indicam-no no
topo. As traduções vivem num repositório próprio,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), por isso
nunca precisas de tocar no código do site. Se falas bem uma dessas
línguas, podes melhorá-la:

1. Abre a página e segue "Ajuda a melhorar esta tradução". Isso abre o
   ficheiro no GitHub, onde o podes editar no browser.
2. Corrige a redação. Mantém as ligações, o código, os números e os nomes como MeshCore
   exatamente como estão.
3. No bloco `translation` no topo, muda `status: ai` para
   `status: human` e propõe a alteração.

Encontraste uma palavra errada mas não tens tempo para a corrigir? Comunica-a com o
[formulário de tradução](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Melhora um guia {#guides}

Os guias são escritos primeiro em inglês e traduzidos a partir daí. As correções
e os novos temas são bem-vindos através do
[formulário de conteúdo](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
ou de um pull request. Os factos precisam de uma fonte: o firmware do MeshCore e a sua
documentação, um regulador de radiocomunicações ou um fabricante. Escreve pelas tuas próprias palavras. Uma
citação curta com a respetiva fonte não há problema.

O [guia de contribuição](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
explica como trabalhar no site no teu próprio computador.

## Estado das traduções {#coverage}

"Revista" significa verificada
por uma pessoa; "Automática" significa traduzida por máquina e ainda não revista;
"Desatualizada" significa que o texto em inglês mudou depois de a tradução ter sido feita;
"Em falta" significa que a página ainda não tem tradução.

{{< coverage >}}

## Créditos {#credits}

O site é construído com [Astro](https://astro.build/). Usa os tipos de letra
IBM Plex Sans e IBM Plex Mono, sob a SIL Open Font License. As traduções
seguem as
convenções do [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) e
partilham os seus glossários de MeshCore. O próprio MeshCore é desenvolvido em
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

O texto e as traduções estão licenciados sob CC BY 4.0, o código sob a licença
MIT.
