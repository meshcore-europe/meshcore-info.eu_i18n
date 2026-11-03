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

- **Site terms**: `site/<lang>.tsv`, the words only this site needs, such as
  antenna and clock terms. Same format as the files above, so kiekr-i18n can
  take a file over as it is. A site term never repeats a term of
  `<lang>.tsv` (`tools/sync_glossary.py --validate` fails on it), so the two
  can be joined into one file without a conflict. The seeders and graders
  read both, the shared terms first.

- **Synced from kiekr-i18n**: nl, de, fr, es, it, pl, pt (from pt-PT), cs, sv,
  da, nb, fi, hu, ro, el. `tools/sync_glossary.py` copies them verbatim; do
  not edit them here. Propose changes to kiekr-i18n, then run the sync.
- **Local**: languages kiekr-i18n lacks (fy, bg, hr, et, ga, lv, lt, mt, sk,
  sl, sr, uk, ca, eu, gl, cy, lb). They are created here and offered upstream
  to kiekr-i18n. Once kiekr-i18n has a file for the language, the sync takes
  it over. These files came on 3 November 2026 with kiekr's core terms plus
  public and private key: each takes the word its translations already used
  most, except where that word reads as a commercial ad for an advert. They
  were drafted without a native speaker. A native speaker's review is welcome.

```sh
python tools/sync_glossary.py          # update synced files
python tools/sync_glossary.py --check  # report drift, write nothing
```

## Protected terms

`protected.txt` lists terms that are never translated (product and project
names, standards). The validators check that each one that appears in an
English string or page also appears in its translation. Numbers with radio
units (869.525 MHz, 25 mW) are protected without being listed.
