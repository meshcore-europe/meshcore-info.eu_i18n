---
title: Contribuir
lead: Este guia é escrito, verificado e traduzido por voluntários. Vê como podes ajudar, com ou sem conta no GitHub.
description: Adiciona a tua comunidade, um dispositivo ou um projeto, revê uma tradução ou melhora um guia no meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-31'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Todo o conteúdo deste site está num
[repositório público no GitHub](https://github.com/meshcore-europe/meshcore-info.eu). As alterações pequenas
passam por um formulário no GitHub (um issue). As maiores entram como pull
request: uma proposta de alteração aos ficheiros, que um responsável revê. Um
responsável verifica cada alteração antes de ela ficar online.

Não tens conta no GitHub? Diz-nos no [Discord](https://discord.meshcore-info.eu/): um
grupo em falta, um dado errado ou uma tradução que soa estranha. Um voluntário
trata do resto.

## Adiciona a tua comunidade {#community}

Geres um grupo local de MeshCore aberto a qualquer pessoa? Preenche o
[formulário de comunidade](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
com o nome, a zona e as ligações públicas. Depois de o adicionarmos, o teu grupo aparece
na página [Grupos locais](/community/) em todas as línguas.

## Sugere um dispositivo ou um projeto {#device-project}

A [página de dispositivos](/devices/) mostra especificações tiradas da documentação dos fabricantes
e nunca tem ligações para lojas. Sugere hardware com o
[formulário de dispositivo](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Criaste uma app, ferramenta, ponte ou design de hardware para MeshCore com código-fonte
público? Adiciona-o com o
[formulário de projeto](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Revê uma tradução {#translate}

As páginas noutras línguas começam por ser traduções automáticas e indicam-no no
topo. As traduções estão num repositório próprio,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), por isso
nunca precisas de mexer no código do site. Se falas bem uma das línguas,
podes melhorá-la:

1. Abre a página e clica em "Ajuda a melhorar esta tradução". Assim abres o
   ficheiro no GitHub, onde o podes editar no navegador.
2. Corrige o texto. Mantém as ligações, o código, os números e nomes como MeshCore
   exatamente como estão.
3. No bloco `translation` no topo, muda `status: ai` para
   `status: human` e propõe a alteração.

Encontraste uma palavra errada mas não tens tempo para a corrigir? Comunica-a com o
[formulário de tradução](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Melhora um guia {#guides}

Os guias são escritos primeiro em inglês e traduzidos a partir daí. Aceitamos correções
e temas novos através do
[formulário de conteúdo](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
ou de um pull request. Os factos precisam de uma fonte: o firmware MeshCore e a respetiva
documentação, um regulador de rádio ou um fabricante. Escreve por palavras tuas. Uma
citação curta com a fonte não tem problema.

O [guia para contribuidores](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
explica como trabalhar no site no teu próprio computador.

## Estado das traduções {#coverage}

"Revista" significa verificada
por uma pessoa; "Automática" significa traduzida por máquina e ainda não revista;
"Desatualizada" significa que o texto em inglês mudou depois de a tradução ser feita;
"Em falta" significa que a página ainda não tem tradução.

{{< coverage >}}

## Créditos {#credits}

O site é feito com [Astro](https://astro.build/). Usa os tipos de letra
IBM Plex Sans e IBM Plex Mono, sob a SIL Open Font License. As traduções
seguem as
convenções do [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) e
partilham os seus glossários de MeshCore. O próprio MeshCore é desenvolvido em
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Os textos e as traduções estão sob a licença CC BY 4.0, o código sob a licença
MIT.
