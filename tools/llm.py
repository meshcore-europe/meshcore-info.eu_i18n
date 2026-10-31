"""LLM translation client for the seeders (spec section 6.3).

Same conventions as kiekr-i18n's seed_llm.py: an OpenAI-compatible
endpoint on the maintainer's machine (LM Studio, Ollama, MLX), configured
through the environment, and a prompt steered by the language's glossary,
the protected terms and the rules of docs/design/ui-copy.md. No API keys;
CI never calls this.

A model id starting with "claude-" runs through the Claude Code CLI
(`claude -p`) on the maintainer's own login, with no tools, settings,
skills or MCP servers loaded, so a call carries only this prompt. The
translation model is claude-opus-5-5 at effort low, followed by a rewrite
pass at effort medium (REWRITE_SYSTEM). Measured on 31 October 2026 on 6
changed paragraphs in Dutch, judged blind by two models and a native
reader: claude-fable-5-1 cost 2 to 2.5 times as much as Opus and never
read better; a rewrite pass changed nothing for claude-sonnet-5-5 and won
most often for Opus; effort high read no better than medium. On the
whole about.md page, Opus with its rewrite cost the same as Fable alone
($0.26) and both judges ranked it first; Sonnet ($0.05) changed facts.

  LLM_ENDPOINT  base URL (default http://localhost:1234/v1)
  LLM_MODEL     model id as the server lists it, or a claude-* model (required)
  LLM_TEMP      sampling temperature (default 0.2; not used by claude-*)
  LLM_EFFORT    effort for claude-* models: low, medium, high (default low)
  LLM_REWRITE_EFFORT  effort of the rewrite pass of a claude-* model (default medium)
  LLM_TIMEOUT   seconds per request (default 300)
"""

from __future__ import annotations

import json
import os
import subprocess
import urllib.request
from dataclasses import dataclass
from pathlib import Path

import copy_rules
import protected
import sync_glossary
from common import ROOT, Language

# Language names steer models far better than codes. Keyed by hugo.toml key.
LANG_NAMES = {
    "nl": "Dutch", "de": "German", "fr": "French", "es": "Spanish", "it": "Italian",
    "pl": "Polish", "pt": "European Portuguese (Portugal, not Brazil)", "cs": "Czech",
    "sv": "Swedish", "da": "Danish", "nb": "Norwegian Bokmål", "fi": "Finnish",
    "hu": "Hungarian", "ro": "Romanian", "el": "Greek",
    "fy": "West Frisian (Frysk, as written in Fryslân)",
    "bg": "Bulgarian",
    "hr": "Croatian",
    "et": "Estonian",
    "ga": "Irish (Gaeilge)",
    "lv": "Latvian",
    "lt": "Lithuanian",
    "mt": "Maltese",
    "sk": "Slovak",
    "sl": "Slovenian",
    "sr": "Serbian in Latin script (never Cyrillic)",
    "uk": "Ukrainian",
    "ca": "Catalan",
    "eu": "Basque",
    "gl": "Galician",
    "cy": "Welsh",
    "lb": "Luxembourgish",
}

# The rules every translation follows, from docs/design/ui-copy.md
# (sections 1 to 3, 6 and 7, and the before/after table of section 9).
COPY_RULES = (
    "Rules for the text:\n"
    "- Translate the meaning, not the words: the text must read as if it was written in the "
    "target language for people curious about MeshCore.\n"
    "- Address the reader informally, as one person, in the form the request names.\n"
    "- Keep every fact: who does what, conditions, limits and numbers. Add nothing, drop nothing.\n"
    "- Numbers stay digits with the exact value. Never add a word like 'about' to a number the "
    "English gives exactly.\n"
    "- Where the English explains a term (companion, repeater, room server, observer), explain it "
    "in the same place.\n"
    "- Keep sentences short, 10 to 15 words, as the English does. Never merge two sentences.\n"
    "- Use the active voice and name who does it, as the English does.\n"
    "- No em dash: use a comma, a colon, parentheses or 2 sentences. No exclamation marks.\n"
    "- No filler, sales or politeness words (simply, just, powerful, please, sorry, "
    "unfortunately) and no count sentence before a list.\n"
    "- Known abbreviations stay as written: LoRa, MQTT, USB, GPS, BLE, SIM, MHz, WiFi.\n"
    "- Add no generated-text pattern the English does not have: no closing line that repeats the "
    "point, no tail that tacks a claim onto a sentence (', making it easy to ...'), no 'not X but Y' "
    "contrast, no row of 3 where the English names 2, no inflating adjective (powerful, seamless, "
    "crucial, emerging), and 'is' where the English says is, not 'serves as' or 'acts as'.\n"
    "- Where the English makes a device the subject but the reader does it, make the reader the "
    "subject. Never turn a statement into a question.\n"
)

STRING_SYSTEM = (
    "You translate short texts for meshcore-info.eu, a non-commercial community website "
    "about MeshCore, a LoRa radio mesh messaging system. The texts are interface labels, "
    "buttons and one- or two-sentence descriptions.\n"
    + COPY_RULES +
    "Rules for the form:\n"
    "- Match the register of the English: a label stays a label, a button stays a short "
    "imperative.\n"
    "- Keep placeholders in curly braces, such as {shown}, exactly as written.\n"
    "- Keep the protected terms, numbers with units (869.618 MHz, 25 mW), channel names "
    "starting with # and product names exactly as written.\n"
    "- Use the glossary translations for the terms it lists.\n"
    "- Output only the translation: no quotes, no notes, no alternatives."
)

PAGE_SYSTEM = (
    "You translate one section of a Markdown page for meshcore-info.eu, a non-commercial "
    "community website about MeshCore, a LoRa radio mesh messaging system.\n"
    + COPY_RULES +
    "Rules for the form:\n"
    "- Keep the Markdown structure exactly: the same headings with the same number of #, "
    "the same lists, tables and paragraphs.\n"
    "- Never change link targets: in [text](target) translate only the text. Keep heading "
    "ids such as {#legal} exactly.\n"
    "- Never split a word over 2 lines with a hyphen: a line break inside a paragraph shows "
    "as a space.\n"
    "- Keep everything between backticks, code blocks and Hugo shortcode tags such as "
    "{{< callout type=\"legal\" verified=\"2026-10-02\" >}} exactly as written; translate "
    "only the text between a shortcode's opening and closing tag.\n"
    "- Keep the protected terms, numbers with units (869.618 MHz, 500 mW, 10%), commands, "
    "channel names starting with # and product names exactly as written.\n"
    "- Use the glossary translations for the terms it lists.\n"
    "- Use one term for one thing on the whole page: where the request gives the sections "
    "translated earlier, use their terms and spelling.\n"
    "- Output only the translated Markdown section, nothing else."
)


# A claude-* model gets the whole page in one call: the front matter fields
# and the body, written as a native writer would. Measured on about.md
# (26 October 2026, nl and de): 1 call and about 6,500 tokens instead of 12
# calls and about 45,000 for a call per section plus a rewrite pass, with the
# same judge scores (meaning 4 to 5, natural 4).
WHOLE_SYSTEM = (
    "You translate a Markdown page for meshcore-info.eu, a non-commercial community website about MeshCore, "
    "a LoRa radio mesh messaging system. Write it so a native writer of the target language could have "
    "written it.\n"
    + COPY_RULES +
    "Rules for a native text:\n"
    "- Never follow English word order or render an English verb literally. Restructure sentences freely, "
    "and pick the verb a native writer uses.\n"
    "- Where the English makes a page or a tool the subject of an action, write who does what in the natural "
    "way for the target language.\n"
    "- You may use more words where the target language needs them to read naturally or to be clear. Split a "
    "sentence rather than make it long.\n"
    "Rules for the form:\n"
    "- The page starts with front matter between two --- lines. Translate the values; keep the keys.\n"
    "- Keep the Markdown structure exactly: the same headings with the same number of #, "
    "the same lists, tables and paragraphs.\n"
    "- Never change link targets: in [text](target) translate only the text. Keep heading "
    "ids such as {#legal} exactly.\n"
    "- Never split a word over 2 lines with a hyphen: a line break inside a paragraph shows "
    "as a space.\n"
    "- Keep everything between backticks, code blocks and Hugo shortcode tags such as "
    "{{< callout type=\"legal\" verified=\"2026-10-02\" >}} exactly as written; translate "
    "only the text between a shortcode's opening and closing tag.\n"
    "- Keep the protected terms, numbers with units (869.618 MHz, 500 mW, 10%), commands, "
    "channel names starting with # and product names exactly as written.\n"
    "- Use the glossary translations for the terms it lists, and one term for one thing on the whole page.\n"
    "- Output only the translated page, front matter included, nothing else."
)




@dataclass(frozen=True)
class Config:
    endpoint: str
    model: str
    temperature: float
    timeout: float
    effort: str = "low"

    @classmethod
    def from_env(cls) -> "Config":
        model = os.environ.get("LLM_MODEL", "")
        if not model:
            raise SystemExit("set LLM_MODEL to the model id your LLM server lists "
                             "(and LLM_ENDPOINT if it is not http://localhost:1234/v1)")
        return cls(os.environ.get("LLM_ENDPOINT", "http://localhost:1234/v1").rstrip("/"), model,
                   float(os.environ.get("LLM_TEMP", "0.2")), float(os.environ.get("LLM_TIMEOUT", "300")),
                   os.environ.get("LLM_EFFORT", "low"))


# The second pass for a claude-* model: the translation, rewritten so a native
# writer could have written it, without the patterns of generated text.
REWRITE_SYSTEM = (
    "You edit a translation for meshcore-info.eu, a non-commercial community website about MeshCore, a "
    "LoRa radio mesh messaging system. You get the English Markdown and its translation. Rewrite the "
    "translation so a native writer of the target language could have written it, and remove every "
    "pattern of generated text.\n"
    + COPY_RULES +
    "Rules for the edit:\n"
    "- Fix every phrase that follows English word order or renders an English verb literally.\n"
    "- Keep every fact, number, limit and condition of the English. Add nothing, drop nothing.\n"
    "- Keep the Markdown exactly: headings, heading ids, the paragraphs and lists as they are, link "
    "targets, code, shortcodes, protected terms and radio values. Keep the glossary terms.\n"
    "- If the translation already reads as native, return it unchanged.\n"
    "- Output only the edited translation: no notes, no comments, no explanation."
)


def rewriter(config: Config, root: Path = ROOT):
    """A function (English, translation, language) -> rewritten translation (REWRITE_SYSTEM)."""
    from dataclasses import replace
    cfg = replace(config, effort=os.environ.get("LLM_REWRITE_EFFORT", "medium"))

    def rewrite(en: str, translated: str, lang: Language) -> str:
        user = (prompt(lang, en, root).removesuffix("Translation:")
                + f"Translation to edit:\n{translated}\n\nEdited translation:")
        return chat(cfg, REWRITE_SYSTEM, user)
    return rewrite


def glossary_block(lang: str, root: Path = ROOT) -> str:
    rows = sync_glossary.rows(lang, root)
    if not rows:
        return ""
    return "Glossary (English = translation): " + "; ".join(f"{en} = {tr}" for en, tr in rows) + "\n"


def prompt(lang: Language, text: str, root: Path = ROOT, context: str = "") -> str:
    terms = ", ".join(protected.load_terms(root))
    earlier = (f"Earlier on this page, already translated. Use the same terms; do not output it again:\n"
               f"{context}\n\n") if context.strip() else ""
    return (f"Target language: {LANG_NAMES[lang.key]}\n"
            f"Address the reader as: {copy_rules.ADDRESS[lang.key][0]}\n"
            f"{glossary_block(lang.key, root)}"
            f"Protected terms (never translate): {terms}\n"
            f"{earlier}English:\n{text}\n\nTranslation:")


def clean(text: str) -> str:
    """Strip what models wrap around an answer: one pair of quotes or a code fence."""
    t = text.strip()
    if t.startswith("```") and t.endswith("```") and t.count("```") == 2:
        t = t.split("\n", 1)[1].rsplit("```", 1)[0].strip() if "\n" in t else t
    if len(t) >= 2 and t[0] in "\"'“" and t[-1] in "\"'”" and "\n" not in t:
        t = t[1:-1].strip()
    return t


# What the claude-* calls of this process cost, as `claude -p` reports it.
spent_usd = 0.0
spent_tokens = {"calls": 0, "input": 0, "cache_write": 0, "cache_read": 0, "output": 0, "thinking": 0}


def spent() -> str:
    """One line: the calls, tokens and dollars of the claude-* calls so far."""
    t = spent_tokens
    return (f"{t['calls']} calls, input {t['input'] + t['cache_write'] + t['cache_read']} tokens "
            f"({t['cache_write']} cache write, {t['cache_read']} cache read), output {t['output']} tokens "
            f"({t['thinking']} thinking), ${spent_usd:.2f}")


def claude_command(config: Config, system: str) -> list[str]:
    """`claude -p` with nothing but this system prompt: no tools, settings or MCP servers."""
    return ["claude", "-p", "--model", config.model, "--effort", config.effort, "--system-prompt", system,
            "--tools", "", "--strict-mcp-config", "--disable-slash-commands", "--setting-sources", "",
            "--no-session-persistence", "--output-format", "json"]


def chat(config: Config, system: str, user: str) -> str:
    return clean(chat_raw(config, system, user))


def chat_raw(config: Config, system: str, user: str) -> str:
    if config.model.startswith("claude-"):
        done = subprocess.run(claude_command(config, system), input=user, capture_output=True, text=True,
                              encoding="utf-8", timeout=config.timeout, check=True)
        answer = json.loads(done.stdout)
        global spent_usd
        spent_usd += float(answer.get("total_cost_usd") or 0)
        usage = answer.get("usage") or {}
        spent_tokens["calls"] += 1
        for key, field in (("input", "input_tokens"), ("cache_write", "cache_creation_input_tokens"),
                           ("cache_read", "cache_read_input_tokens"), ("output", "output_tokens")):
            spent_tokens[key] += int(usage.get(field) or 0)
        spent_tokens["thinking"] += int((usage.get("output_tokens_details") or {}).get("thinking_tokens") or 0)
        if answer.get("is_error"):
            raise RuntimeError(answer.get("result") or "claude -p failed")
        return answer["result"]
    body = json.dumps({
        "model": config.model,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "temperature": config.temperature,
        "stream": False,
    }).encode("utf-8")
    request = urllib.request.Request(config.endpoint + "/chat/completions", data=body,
                                     headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=config.timeout) as response:
        answer = json.loads(response.read())
    return answer["choices"][0]["message"]["content"]


BATCH_SYSTEM = STRING_SYSTEM.replace(
    "- Output only the translation: no quotes, no notes, no alternatives.",
    "- You get a JSON object of keys and English texts. Translate each text on its own; the keys "
    "only name the place in the interface.\n"
    "- Output only a JSON object with the same keys and the translations as values, nothing else.")


def parse_batch(answer: str) -> dict[str, str]:
    """The JSON object of a batch answer, even inside a code fence; only string values."""
    start, end = answer.find("{"), answer.rfind("}")
    data = json.loads(answer[start:end + 1]) if start >= 0 < end else {}
    return {k: v.strip() for k, v in data.items() if isinstance(v, str)}


def batch_translator(config: Config, root: Path = ROOT):
    """A function ({key: English}, language) -> {key: translation}, one request per call."""
    def translate(texts: dict[str, str], lang: Language) -> dict[str, str]:
        source = json.dumps(texts, ensure_ascii=False, indent=1)
        return parse_batch(chat_raw(config, BATCH_SYSTEM, prompt(lang, source, root)))
    return translate


def page_translator(config: Config, root: Path = ROOT):
    """A function (English page, language) -> translated page, in one call (WHOLE_SYSTEM)."""
    return lambda text, lang: chat(config, WHOLE_SYSTEM, prompt(lang, text, root))


def translator(config: Config, kind: str, root: Path = ROOT):
    """A function (text, language, context="") -> translation, for 'string' or 'page' texts.

    context is what the page already has in the target language, for consistent terms."""
    system = STRING_SYSTEM if kind == "string" else PAGE_SYSTEM
    return lambda text, lang, context="": chat(config, system, prompt(lang, text, root, context))
