---
title: "Contribute"
lead: "This guide is written, checked and translated by volunteers. Here is how to help, with or without a GitHub account."
description: "Add your community, a device or a project, review a translation, or improve a guide on meshcore-info.eu."
---

Everything on this site lives in a public
[GitHub repository](https://github.com/meshcore-europe/meshcore-info.eu). Small changes
go through a form on GitHub (an issue). Anything bigger goes in as a pull
request: a proposed change to the files that a maintainer reviews. A
maintainer checks every change before it goes live.

No GitHub account? Tell us on [Discord](https://discord.meshcore-info.eu/): a
missing group, a wrong fact or a translation that reads oddly. A volunteer
takes it from there.

## Add your community {#community}

Run a local MeshCore group that anyone can join? Fill in the
[community form](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
with the name, the area and the public links. Once added, your group appears
on the [Local groups](/community/) page in every language.

## Suggest a device or a project {#device-project}

The [devices page](/devices/) lists specifications from manufacturer
documentation and never links to shops. Suggest hardware with the
[device form](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Built an app, tool, bridge or hardware design for MeshCore with public source
code? Add it with the
[project form](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Review a translation {#translate}

Pages in other languages start as machine translations and say so at the
top. Translations live in their own repository,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), so
you never need to touch the site's code. If you speak one of the languages
well, you can make it better:

1. Open the page and follow "Help improve this translation". It opens the
   file on GitHub, where you can edit it in your browser.
2. Fix the wording. Keep links, code, numbers and names such as MeshCore
   exactly as they are.
3. In the `translation` block at the top, change `status: ai` to
   `status: human`, and propose the change.

Found a wrong word but no time to fix it? Report it with the
[translation form](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Improve a guide {#guides}

Guides are written in English first and translated from there. Corrections
and new topics are welcome through the
[content form](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
or a pull request. Facts need a source: the MeshCore firmware and its
documentation, a radio regulator, or a manufacturer. Write in your own words. A
short quote with its source is fine.

The [contributor guide](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
explains how to work on the site on your own computer.

## Translation status {#coverage}

"Reviewed" means checked
by a person; "Machine" means machine-translated and not yet reviewed;
"Outdated" means the English text changed after the translation was made;
"Missing" means the page has no translation yet.

{{< coverage >}}

## Credits {#credits}

The site is built with [Astro](https://astro.build/). It uses the typefaces
IBM Plex Sans and IBM Plex Mono, under the SIL Open Font License. Translations
follow the
conventions of [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) and
share its MeshCore glossaries. MeshCore itself is developed at
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Text and translations are licensed under CC BY 4.0, code under the MIT
licence.
