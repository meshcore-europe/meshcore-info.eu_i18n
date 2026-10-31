# meshcore-info.eu translations

Translations of [meshcore-info.eu](https://meshcore-info.eu), the
non-commercial community guide to MeshCore in Europe, into 15 languages. The
site itself lives in [meshcore-europe/meshcore-info.eu](https://github.com/meshcore-europe/meshcore-info.eu);
this repository holds only the translated text, so translators can work
without touching the site's code.

The conventions follow [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n)
and share its MeshCore glossaries.

## What is here

| Path | What | Edit it? |
|---|---|---|
| `data/i18n/<lang>.json` | Interface text: menus, buttons, labels, descriptions | Yes |
| `content/<lang>/*.md` | Translated pages | Yes |
| `data/i18n/en.json`, `content/en/` | The English source | No: copied from the site |
| `glossary/` | Agreed translations of MeshCore terms, and `protected.txt`: terms that are never translated | No: copied from the site, which syncs most of them from kiekr-i18n. Suggest changes in an issue |
| `tools/`, `hugo.toml`, `data/schema/` | Checks and seeders | No: copied from the site |

Languages: nl, de, fr, es, it, pl, pt (European Portuguese), cs, sv, da, nb,
fi, hu, ro, el.

## How to improve a translation

Every machine-translated page on the site has a link "Help improve this
translation" that opens the file here on GitHub.

**A page** (`content/<lang>/<page>.md`): fix the wording, then change
`status: ai` to `status: human` in the `translation` block at the top. Keep
the structure of the English page: the same headings, heading ids such as
`{#legal}`, links, shortcodes such as `{{< callout >}}`, code, numbers and
names. Do not change `source_hash` unless you checked the page against the
current English version; then set it to what
`python tools/source_hash.py content/en/<page>.md` prints.
Leave `fields` and `sections` as they are: the seeder uses them to translate
only what changes in English.

**Interface text** (`data/i18n/<lang>.json`): replace a machine entry
`{"value": "...", "_ai": true, "_seeded": "...", "_source": "..."}` by a plain string `"..."`.
Keep `{placeholders}` such as `{shown}` as they are.

A plain string and a `status: human` page count as reviewed. The seeders
never overwrite reviewed text, and CI rejects a change that turns reviewed
text back into machine text.

## Checks

```sh
python -m pip install -r requirements-dev.txt
bash tools/ci.sh
```

CI runs the same on every pull request. A translated page must keep the
English page's headings, heading ids, links, shortcodes and code;
`glossary/protected.txt` terms and radio values such as `869.618 MHz` stay
unchanged.

## Machine translations (maintainers)

`tools/seed_strings.py` and `tools/seed_pages.py` fill missing or outdated
text with a language model on your own computer (OpenAI-compatible API, set
`LLM_ENDPOINT` and `LLM_MODEL`), or with Claude through the Claude Code CLI
(`LLM_MODEL=claude-opus-5-5`, `LLM_EFFORT=low`; a page then goes in one
request that translates it as a native writer would, and a second one at
effort medium rewrites it without the patterns of generated text). They only fill missing text
and outdated machine translations (a page by its `source_hash`, a string by
its `_source`), never reviewed text; `--reseed-ai` also
redoes current machine translations.

`tools/grade_copy.py` holds the translations to the site's copy guide
(`docs/design/ui-copy.md` in the site repository) with search rules, per
language: informal address, no em dash, numbers and terms kept, sentence
length and more. `--check` fails on a hard rule; CI runs it with `--since` on what a pull
request changes. `tools/judge.py` asks Claude
whether a translation keeps the meaning of the English and reads as written
in its language.

## How text flows

1. English changes on the site. On every push to its main, the site's
   workflow `export-i18n` copies the English source and the tools here
   (`tools/sync_i18n.py export`) and commits them.
2. Translators and seeders update `data/i18n/` and `content/<lang>/` here.
3. Within the hour after a merge here, the site opens a pull request with the
   import (`i18n/import`). Its CI checks the result, and a maintainer merges it
   before it goes live.

## Licence

Translations are licensed under CC BY 4.0, like the site's text.
