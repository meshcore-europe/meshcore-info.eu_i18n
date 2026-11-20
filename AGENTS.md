# Translating with an agent

This file is for a coding agent (Claude Code, Codex and the like) that helps a
volunteer translate meshcore-info.eu. The README explains the files and the
checks; read it first. Generated from the site repository
(tools/i18n-repo/); edit it there.

Two rules come before everything else:

- **A person reviews, the agent does not.** An agent may translate on behalf
  of a person. Its output stays marked as machine text (`"_ai": true` for a
  string, `status: ai` for a page) until a person who speaks the language
  has read it. Only then does it become a plain string or `status: human`.
- **No slop.** Write the way a native speaker of the language writes. No
  filler, no padding, no inflated words. Read
  <https://gist.github.com/dexhorthy/4cc96f01be5b1208519e75dad250a948>.

## The steps

Ask the volunteer which language they speak well (`<lang>` below). Work in
batches of 50 strings, and ask after each batch whether to go on.

1. Work in the volunteer's fork, with LF line endings. Run
   `python -m pip install -r requirements-dev.txt`.
2. **Translate what is missing or outdated.** `python tools/gaps.py` lists
   it. Fill it with the seeders, which keep the output marked as machine
   text:
   ```sh
   LLM_MODEL=claude-opus-5-5 LLM_EFFORT=low python tools/seed_strings.py --langs <lang>
   LLM_MODEL=claude-opus-5-5 python tools/seed_pages.py --langs <lang>
   ```
   `tools/llm.py` lists the settings for a local model instead.
3. **Review.** Take the next 50 entries in `data/i18n/<lang>.json` that are
   marked `_ai`, the ones from step 2 first. Show them as a compact table:
   key, English (from `data/i18n/en.json`), translation. Read only those
   entries, not whole files, and do not translate them again.
4. **Apply the answers.** An approved line becomes a plain string. A
   corrected line becomes the volunteer's wording, as a plain string. A
   skipped line stays `_ai`. A page becomes `status: human` only after the
   volunteer has read all of it. Keep `{placeholders}`, the terms in
   `glossary/protected.txt` and radio values such as `869.618 MHz` exactly
   as they are.
5. **Check and propose.** Run `bash tools/ci.sh` until it passes, then open
   a pull request. List what the seeders translated and which keys the
   volunteer reviewed.

Never edit `data/i18n/en.json`, `content/en/`, `glossary/` or `tools/`: they
are copied from the site, and a change there is lost at the next sync.
