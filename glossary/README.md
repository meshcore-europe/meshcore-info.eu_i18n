# Glossary

MeshCore terminology per language, shared with
[kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) so the website and
the KiekR app use the same words. The seeders (plan 4) feed these terms to the
translation model.

## Format

`<lang>.tsv`, where `<lang>` is the language key from `hugo.toml` (`pt` for
Portuguese). Tab-separated, two columns, no header: the English term and its
translation. Each English term appears once (case-insensitive).

```
node	knoop
repeater	repeater
```

## Where each file comes from

- **Synced from kiekr-i18n**: nl, de, fr, es, it, pl. `tools/sync_glossary.py`
  copies them verbatim; do not edit them here. Propose changes to
  kiekr-i18n, then run the sync.
- **Local**: languages kiekr-i18n lacks (pt for pt-PT, cs, sv, da, nb, fi,
  hu, ro, el). They are created here and offered upstream to kiekr-i18n.
  Once kiekr-i18n has a file for the language, the sync takes it over.
  The first versions (2026-10-02) cover kiekr's core terms plus public and
  private key. They were drafted without a native speaker: technical terms
  that communities usually keep in English (flood, mesh, often repeater and
  advert) stay English. A native speaker's review is welcome.

```sh
python tools/sync_glossary.py          # update synced files
python tools/sync_glossary.py --check  # report drift, write nothing
```

## Protected terms

`protected.txt` lists terms that are never translated (product and project
names, standards). The validators check that each one that appears in an
English string or page also appears in its translation. Numbers with radio
units (869.525 MHz, 25 mW) are protected without being listed.
