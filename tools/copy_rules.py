"""Per-language word lists for the copy graders (tools/grade_copy.py).

Each list turns a rule of docs/design/ui-copy.md (and the writing rules it
shares with it) into words a search can find. Patterns are regular
expressions, matched case-insensitively unless a comment says otherwise.
A rule a search cannot decide (does the translation keep the meaning,
is a term explained on first use) goes to the judge (tools/judge.py).
"""

from __future__ import annotations

# ui-copy.md section 2: the reader is addressed informally, as one person.
# The hint goes into the translation prompt; the patterns find the formal or
# plural address. A pattern starting with "MID:" only counts in the middle of
# a sentence and is matched case-sensitively (German "Sie" at the start of a
# sentence can mean "they").
ADDRESS = {
    "en": ("you", []),
    "nl": ("je/jij, never u", [r"\bu\b(?!\.\w)", r"\buw\b", r"\bjullie\b"]),
    "de": ("du, never Sie", [r"MID:\bSie\b", r"MID:\bIhnen\b", r"MID:\bIhre?[mnrs]?\b", r"\beuch\b", r"\beure[mnrs]?\b"]),
    "fr": ("tu, never vous", [r"\bvous\b", r"\bvotre\b", r"\bvos\b"]),
    "es": ("tú, never usted or vosotros", [r"\busted(es)?\b", r"\bvosotr[oa]s\b", r"\bvuestr[oa]s?\b"]),
    "it": ("tu, never Lei or voi", [r"MID:\bLei\b", r"MID:\bSu[oae]i?\b", r"\bvoi\b", r"\bvostr[oaie]\b"]),
    "pl": ("ty, never Pan/Pani or wy", [r"\bpan(a|u|em|ie)?\b", r"\bpani\b", r"\bpaństw(o|a|u|em)\b(?! członkowsk)", r"\bwasz\w*\b"]),
    "pt": ("tu (European Portuguese), never você", [r"\bvocês?\b", r"\bo senhor\b", r"\ba senhora\b"]),
    "cs": ("ty, never vy", [r"\bvy\b", r"\bvám\b", r"\bvás\b", r"\bváš\b", r"\bvaš(e|i|eho|emu|ím|ich|im|imi)\b"]),
    "sv": ("du, never ni", [r"\bni\b", r"\ber\b", r"\bert\b", r"\bera\b"]),
    "da": ("du, never De or I", [r"MID:\bDe\b", r"MID:\bDem\b", r"MID:\bDeres\b", r"\bjer\b", r"\bjeres\b"]),
    "nb": ("du, never De or dere", [r"MID:\bDe\b", r"MID:\bDem\b", r"\bdere\b"]),
    "fi": ("sinä (often implied by the verb), never te", [r"\bte\b", r"\bteidän\b", r"\bteille\b", r"\bteitä\b", r"\bteillä\b"]),
    "hu": ("te, never Ön or maga", [r"\bön(ök|t|nek|nel|höz|től|ben|re|ön|öket|öknek|é|ét|nél|ért)?\b"]),
    "ro": ("tu, never dumneavoastră or voi", [r"\bdumneavoastră\b", r"\bdvs\b", r"\bdumneata\b", r"\bvă\b", r"\bvoi\b", r"\bvoastr[ăe]\b", r"\bvostru\b"]),
    "el": ("εσύ, never εσείς", [r"\bεσείς\b", r"\bσας\b"]),
}

# ui-copy.md sections 3 and 6, and the English proof of 20 October 2026:
# words for "about" next to a number. A hard limit is a number, so a
# translation may not add an "about" the English does not have.
APPROX = {
    "en": [r"\babout\b", r"\baround\b", r"\bapproximately\b", r"\broughly\b"],
    "nl": [r"\bongeveer\b", r"\bcirca\b", r"\bca\.", r"\bzo'n\b", r"\bpakweg\b"],
    "de": [r"\betwa\b", r"\bungefähr\b", r"\brund\b", r"\bca\.", r"\bcirca\b"],
    "fr": [r"\benviron\b", r"\bà peu près\b", r"\bapproximativement\b"],
    "es": [r"\baproximadamente\b", r"\balrededor de\b", r"\bunos\b", r"\bunas\b"],
    "it": [r"\bcirca\b", r"\ball'incirca\b", r"\bapprossimativamente\b"],
    "pl": [r"\boko[łl]o\b", r"\bok\.", r"\bmniej więcej\b"],
    "pt": [r"\bcerca de\b", r"\baproximadamente\b", r"\bpor volta de\b"],
    "cs": [r"\bpřibližně\b", r"\bzhruba\b", r"\basi\b", r"\bkolem\b", r"\bcca\b"],
    "sv": [r"\bungefär\b", r"\bcirka\b", r"\bca\b", r"\bomkring\b"],
    "da": [r"\bcirka\b", r"\bca\.", r"\bomkring\b", r"\bomtrent\b"],
    "nb": [r"\bomtrent\b", r"\bcirka\b", r"\bca\.", r"\brundt\b"],
    "fi": [r"\bnoin\b", r"\bsuunnilleen\b", r"\bn\.", r"\bkutakuinkin\b"],
    "hu": [r"\bkörülbelül\b", r"\bkb\.", r"\bnagyjából\b", r"\bmintegy\b"],
    "ro": [r"\baproximativ\b", r"\bcirca\b", r"\bîn jur de\b"],
    "el": [r"\bπερίπου\b", r"\bγύρω στ"],
}

# ui-copy.md section 9: no doubled negation. Only the word that negates a
# clause; words that only agree with it in negative-concord languages
# ("nada" after "no") are left out, so a correct sentence counts once.
NEGATION = {
    "en": [r"\bnot\b", r"n't\b", r"\bno\b", r"\bnever\b", r"\bnothing\b", r"\bnone\b", r"\bnobody\b", r"\bwithout\b", r"\bneither\b", r"\bnor\b", r"\bcannot\b"],
    "nl": [r"\bniet\b", r"\bgeen\b", r"\bnooit\b", r"\bniets\b", r"\bniemand\b", r"\bzonder\b", r"\bnoch\b"],
    "de": [r"\bnicht\b", r"\bkein\w*\b", r"\bnie\b", r"\bniemals\b", r"\bnichts\b", r"\bniemand\b", r"\bohne\b", r"\bweder\b"],
    "fr": [r"\bne\b", r"\bn['’]", r"\bsans\b"],
    "es": [r"\bno\b", r"\bnunca\b", r"\bsin\b"],
    "it": [r"\bnon\b", r"\bmai\b", r"\bsenza\b"],
    "pl": [r"\bnie\b", r"\bbez\b"],
    "pt": [r"\bnão\b", r"\bnunca\b", r"\bsem\b"],
    "cs": [r"\bne(?!bo\b|ž\b|boť\b|j)\w+\b", r"\bbez\b"],
    "sv": [r"\binte\b", r"\bingen\b", r"\binget\b", r"\binga\b", r"\baldrig\b", r"\butan\b"],
    "da": [r"\bikke\b", r"\bingen\b", r"\bintet\b", r"\baldrig\b", r"\buden\b"],
    "nb": [r"\bikke\b", r"\bingen\b", r"\bintet\b", r"\baldri\b", r"\buten\b"],
    "fi": [r"\be(i|n|t|mme|tte|ivät)\b", r"\bilman\b"],
    "hu": [r"\bnem\b", r"\bsem\b", r"\bnélkül\b"],
    "ro": [r"\bnu\b", r"\bfără\b"],
    "el": [r"\bδεν\b", r"\bμην?\b", r"\bχωρίς\b"],
}

# ui-copy.md section 6: no count sentence before a list. The number words 2
# to 10 per language; a digit counts in every language.
NUMBER_WORDS = {
    "en": "two three four five six seven eight nine ten",
    "nl": "twee drie vier vijf zes zeven acht negen tien",
    "de": "zwei drei vier fünf sechs sieben acht neun zehn",
    "fr": "deux trois quatre cinq six sept huit neuf dix",
    "es": "dos tres cuatro cinco seis siete ocho nueve diez",
    "it": "due tre quattro cinque sei sette otto nove dieci",
    "pl": "dwa trzy cztery pięć sześć siedem osiem dziewięć dziesięć",
    "pt": "dois três quatro cinco seis sete oito nove dez",
    "cs": "dva tři čtyři pět šest sedm osm devět deset",
    "sv": "två tre fyra fem sex sju åtta nio tio",
    "da": "to tre fire fem seks syv otte ni ti",
    "nb": "to tre fire fem seks sju åtte ni ti",
    "fi": "kaksi kolme neljä viisi kuusi seitsemän kahdeksan yhdeksän kymmenen",
    "hu": "két három négy öt hat hét nyolc kilenc tíz",
    "ro": "două trei patru cinci șase șapte opt nouă zece",
    "el": "δύο τρία τέσσερα πέντε έξι επτά οκτώ εννέα δέκα",
}

# ui-copy.md section 3 (filler, sales and generated-text words) and the
# project's writing rules (section 11). The guide lists
# them for EN, NL and DE; other languages are covered by the judge.
FILLER = {
    "en": [r"\bsimply\b", r"\bjust\b", r"\bactually\b", r"\breally\b", r"\bseamless(ly)?\b", r"\bpowerful\b",
           r"\bsmart\b", r"\brobust\b", r"\bsnappy\b", r"\bblazing\b", r"\bcutting-edge\b", r"\bsuper\b",
           r"\bdive into\b", r"\bin today's\b", r"\bit's not just\b"],
    "nl": [r"\bgewoon\b", r"\beigenlijk\b", r"\beven\b", r"\becht\b", r"\bnaadloos\b", r"\bkrachtig\w*\b",
           r"\bslim(me)?\b", r"\beenvoudig\w*\b", r"\bsupersnel\w*\b", r"\bgeavanceerd\w*\b", r"\bsuper\b",
           r"\been soort van\b", r"\bin principe\b", r"\bduik erin\b", r"\bin het huidige landschap\b"],
    "de": [r"\beinfach\b", r"\beigentlich\b", r"\bwirklich\b", r"\bnahtlos\w*\b", r"\bleistungsstark\w*\b",
           r"\bsmart\w*\b", r"\bblitzschnell\w*\b", r"\bsuper\b"],
}

# ui-copy.md section 3: no politeness filler and no apologies.
POLITE = {
    "en": [r"\bplease\b", r"\bsorry\b", r"\boops\b", r"\bfeel free\b", r"\bdon't hesitate\b", r"\bunfortunately\b"],
    "nl": [r"\balsjeblieft\b", r"\balstublieft\b", r"\bsorry\b", r"\boeps\b", r"\bhelaas\b", r"\bschroom niet\b"],
    "de": [r"\bbitte\b", r"\bentschuldigung\b", r"\bhoppla\b", r"\bleider\b"],
    "fr": [r"\bs'il (te|vous) pla[iî]t\b", r"\bdésolée?s?\b", r"\boups\b", r"\bmalheureusement\b", r"\bn'hésite[zr]? pas\b"],
    "es": [r"\bpor favor\b", r"\blo sentimos\b", r"\blo siento\b", r"\bups\b", r"\bdesafortunadamente\b", r"\blamentablemente\b", r"\bno dudes\b"],
    "it": [r"\bper favore\b", r"\bper piacere\b", r"\bci dispiace\b", r"\bspiacenti\b", r"\bpurtroppo\b", r"\bnon esitare\b"],
    "pl": [r"\bproszę\b", r"\bprzepraszamy\b", r"\bniestety\b", r"\bups\b", r"\bnie wahaj się\b"],
    "pt": [r"\bpor favor\b", r"\blamentamos\b", r"\bdesculp\w+\b", r"\binfelizmente\b", r"\bnão hesites\b"],
    "cs": [r"\bprosím\b", r"\bomlouváme se\b", r"\bbohužel\b", r"\bjejda\b", r"\bneváhej\b"],
    "sv": [r"\bvänligen\b", r"\bsnälla\b", r"\btyvärr\b", r"\bförlåt\b", r"\bursäkta\b", r"\btveka inte\b"],
    "da": [r"\bvenligst\b", r"\bdesværre\b", r"\bundskyld\b", r"\bhov\b", r"\btøv ikke\b"],
    "nb": [r"\bvennligst\b", r"\bdessverre\b", r"\bbeklager\b", r"\bunnskyld\b", r"\bnøl ikke\b"],
    "fi": [r"\bole hyvä\b", r"\bvalitettavasti\b", r"\bpahoittelemme\b", r"\bhups\b", r"\bystävällisesti\b"],
    "hu": [r"\bkérjük\b", r"\bkérem\b", r"\bsajnos\b", r"\belnézést\b", r"\bhoppá\b", r"\bne habozz\b"],
    "ro": [r"\bte rog\b", r"\bvă rugăm\b", r"\bne pare rău\b", r"\bdin păcate\b", r"\bhopa\b", r"\bnu ezita\b"],
    "el": [r"\bπαρακαλ\w+\b", r"\bδυστυχώς\b", r"\bσυγγνώμη\b", r"\bλυπούμαστε\b", r"\bωχ\b"],
}

# ui-copy.md sections 3 and 8, and the English proof: words a visitor never
# reads, in any language. Matched case-sensitively.
NEVER = [
    (r"\bMeshcore\b", "write MeshCore (section 8)"),
    (r"\bMesh Core\b", "write MeshCore (section 8)"),
    (r"\bISM\b", "868 MHz is a short range device band in Europe, not an ISM band (section 9)"),
    (r"\b[Tt]enants?\b", "internal term (section 3)"),
    (r"\bHugo\b", "internal term (section 3)"),
    (r"\bAstro\b", "internal term (section 3)"),
]

# ui-copy.md section 8, the "Do not use" column, where a search can decide.
# relay, router, client, zone, scope and device also have meanings the
# guide allows ("no router in between"), so the judge covers those.
DO_NOT_USE = {
    "en": [r"\bthe portal\b", r"\bthe platform\b", r"\bfeeders?\b", r"(?<!off )\bthe grid\b", r"\bthe MeshCore network\b"],
}

# ui-copy.md section 3: abbreviations a translation keeps as they are.
ABBREVIATIONS = ["LoRa", "MQTT", "USB", "GPS", "BLE", "SIM", "MHz", "WiFi"]

# ui-copy.md section 8: glossary rows for words the kiekr glossaries lack.
# They win over nothing: glossary/<lang>.tsv comes first.
GUIDE_GLOSSARY = {
    "nl": {"node": "node", "repeater": "repeater", "companion": "companion", "observer": "observer",
           "region": "regio", "local group": "lokale groep"},
    "de": {"node": "Knoten", "repeater": "Repeater", "companion": "Companion", "observer": "Observer",
           "region": "Region", "local group": "lokale Gruppe"},
}
