#!/usr/bin/env python3
"""Croatian (hr) text helpers for software localisation. Python 3 standard library only.

Subcommands
  plural N [ONE FEW OTHER]   CLDR plural category for hr (one/few/other); with three word
                             forms, prints "N word" (e.g. plural 22 dan dana dana -> 22 dana)
  slugify TEXT [--dj]        URL slug; đ -> d by default, --dj gives đ -> dj
  fold TEXT [--dj]           lowercase + remove diacritics for search keys (č ć -> c, š -> s, ž -> z, đ -> d/dj)
  sort [FILE]                sort lines (stdin or FILE) in Croatian alphabetical order
  fix-mojibake TEXT|-        repair UTF-8 read as Windows-1252/Latin-1, and (with --legacy) Windows-1250
                             or ISO-8859-2 bytes read as Windows-1252/Latin-1
  vocative NAME [--gender m|f] [--surname]
                             conservative vocative; falls back to the nominative when unsure
  greeting --first F --last L [--gender m|f] [--formal|--informal]
                             salutation line, e.g. "Poštovani gospodine Horvat,"
  place NAME [--type grad|otok|...]
                             look up genitive, locative (u/na), "from" form and ethnics in assets/toponyms.csv
  --self-test                run the built-in tests

Library use:  from hr_text import plural, slugify, fold, sort_key, fix_mojibake, vocative, place
"""
import argparse
import csv
import os
import re
import sys
import unicodedata
from decimal import Decimal

# ---------------------------------------------------------------------------
# Plurals (CLDR 47 rules for "hr"; identical for bs and sr-Latn)
#   one: v = 0 and i % 10 = 1 and i % 100 != 11  or  f % 10 = 1 and f % 100 != 11
#   few: v = 0 and i % 10 = 2..4 and i % 100 != 12..14  or  f % 10 = 2..4 and f % 100 != 12..14
#   other: everything else
# i = integer digits, v = number of visible fraction digits, f = visible fraction digits as integer
# ---------------------------------------------------------------------------

def _operands(n):
    """Return (i, v, f) CLDR operands. Pass a str or Decimal to keep trailing zeros ("1.0")."""
    if isinstance(n, bool):
        raise TypeError("bool is not a number")
    if isinstance(n, float):
        s = repr(n)
        if "e" in s or "E" in s:
            s = format(Decimal(s), "f")
    else:
        s = str(n)
    s = s.strip().replace(",", ".").lstrip("+-")
    if not re.fullmatch(r"\d+(\.\d+)?", s):
        raise ValueError("not a plain number: %r" % (n,))
    if isinstance(n, float) and s.endswith(".0"):
        s = s[:-2]  # Python prints 1.0 for the float 1; treat it as the integer 1 (like Intl does)
    ip, _, fp = s.partition(".")
    return int(ip), len(fp), int(fp) if fp else 0


def plural(n):
    """CLDR plural category for Croatian: 'one', 'few' or 'other'."""
    i, v, f = _operands(n)
    if (v == 0 and i % 10 == 1 and i % 100 != 11) or (f % 10 == 1 and f % 100 != 11):
        return "one"
    if (v == 0 and 2 <= i % 10 <= 4 and not 12 <= i % 100 <= 14) or \
       (2 <= f % 10 <= 4 and not 12 <= f % 100 <= 14):
        return "few"
    return "other"


def plural_form(n, one, few, other):
    return {"one": one, "few": few, "other": other}[plural(n)]


# gettext / Django / PHP header (integers only; gettext cannot see decimals)
GETTEXT_PLURAL_FORMS = ("nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : "
                        "n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);")


def gettext_index(n):
    n = int(n)
    if n % 10 == 1 and n % 100 != 11:
        return 0
    if 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        return 1
    return 2

# ---------------------------------------------------------------------------
# Normalisation, folding, slugs
# ---------------------------------------------------------------------------

# Unicode digraph code points (U+01C4..U+01CC) -> two letters
DIGRAPHS = {"Ǆ": "DŽ", "ǅ": "Dž", "ǆ": "dž", "Ǉ": "LJ", "ǈ": "Lj",
            "ǉ": "lj", "Ǌ": "NJ", "ǋ": "Nj", "ǌ": "nj"}


def normalize(text):
    """NFC + split legacy digraph code points. Use on every input before storing/comparing."""
    text = unicodedata.normalize("NFC", text)
    return "".join(DIGRAPHS.get(ch, ch) for ch in text)


_HR_FOLD = {"č": "c", "ć": "c", "š": "s", "ž": "z", "đ": "d",
            "Č": "C", "Ć": "C", "Š": "S", "Ž": "Z", "Đ": "D"}


def strip_diacritics(text, dj=False):
    text = normalize(text)
    out = []
    for ch in text:
        if ch in "đĐ" and dj:
            out.append("dj" if ch == "đ" else "Dj")
        elif ch in _HR_FOLD:
            out.append(_HR_FOLD[ch])
        else:
            dec = unicodedata.normalize("NFKD", ch)
            out.append("".join(c for c in dec if not unicodedata.combining(c)))
    return "".join(out)


def fold(text, dj=False):
    """Search key: NFC, digraph code points split, casefolded, diacritics removed, spaces collapsed."""
    return re.sub(r"\s+", " ", strip_diacritics(text, dj=dj).casefold()).strip()


def search_variants(text):
    """Both đ conventions, for indexing: {'dakovo', 'djakovo'}."""
    return {fold(text), fold(text, dj=True)}


def slugify(text, dj=False, max_len=80):
    s = strip_diacritics(text, dj=dj).lower()
    s = s.replace("&", " i ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if max_len and len(s) > max_len:
        s = s[:max_len].rsplit("-", 1)[0] or s[:max_len]
    return s

# ---------------------------------------------------------------------------
# Collation: a b c č ć d dž đ e f g h i j k l lj m n nj o p (q) r s š t u v (w x y) z ž
# Same primary order as CLDR/ICU "hr" (Intl.Collator('hr'), PostgreSQL "hr-HR-x-icu",
# MySQL utf8mb4_croatian_ci / utf8mb4_hr_0900_ai_ci). Like ICU, dž/lj/nj are always treated as
# digraphs (so "nadživjeti" or "injekcija" sort as if they contained dž / nj).
# ---------------------------------------------------------------------------

_ALPHABET = ["a", "b", "c", "č", "ć", "d", "dž", "đ", "e", "f", "g", "h", "i", "j", "k", "l", "lj",
             "m", "n", "nj", "o", "p", "q", "r", "s", "š", "t", "u", "v", "w", "x", "y", "z", "ž"]
_RANK = {l: i for i, l in enumerate(_ALPHABET)}


def _tokens(word):
    w = normalize(word)
    i = 0
    while i < len(w):
        two = w[i:i + 2].lower()
        if two in ("dž", "lj", "nj"):
            yield two, w[i:i + 2]
            i += 2
            continue
        yield w[i].lower(), w[i]
        i += 1


def sort_key(text):
    """Key for sorted(): Croatian primary order, then accents, then lowercase-before-uppercase."""
    prim, sec, ter = [], [], []
    for low, orig in _tokens(text):
        if low in _RANK:
            prim.append((3, _RANK[low])); sec.append(0)
        else:
            base = "".join(c for c in unicodedata.normalize("NFKD", low) if not unicodedata.combining(c))
            if base in _RANK:  # foreign accented letter (é, ü ...) sorts with its base letter
                prim.append((3, _RANK[base])); sec.append(1)
            elif low.isdigit():
                prim.append((2, int(low) if low.isascii() else ord(low))); sec.append(0)
            elif low.isspace() or not low.isalnum():
                prim.append((1, ord(low))); sec.append(0)
            else:
                prim.append((4, ord(low))); sec.append(0)
        ter.append(0 if orig == orig.lower() else 1)
    return (prim, sec, ter)


def hr_sorted(items, key=None):
    k = (lambda x: sort_key(key(x))) if key else sort_key
    return sorted(items, key=k)

# ---------------------------------------------------------------------------
# Mojibake repair
# ---------------------------------------------------------------------------

_UTF8_MARKERS = re.compile("[ÃÄÅÆÐ][\u0080-ÿŒœŠšŸŽžƒˆ˜–-›€™]")


def _to_bytes_1252(s):
    out = bytearray()
    for ch in s:
        try:
            out += ch.encode("cp1252")
        except UnicodeEncodeError:
            if ord(ch) < 256:
                out.append(ord(ch))  # C1 controls that cp1252 leaves undefined (latin-1 path)
            else:
                raise
    return bytes(out)


# Windows-1250 / ISO-8859-2 single bytes shown as Windows-1252 / Latin-1 characters
_LEGACY_1250 = {"è": "č", "È": "Č", "æ": "ć", "Æ": "Ć", "ð": "đ", "Ð": "Đ",
                "š": "š", "Š": "Š", "ž": "ž", "Ž": "Ž",     # identical in 1250 and 1252
                "¹": "š", "©": "Š", "¾": "ž", "®": "Ž",     # ISO-8859-2 read as Latin-1
                "\x9a": "š", "\x8a": "Š", "\x9e": "ž", "\x8e": "Ž"}


def fix_mojibake(text, legacy=False, max_rounds=3):
    """Repair 'Ä\\x8d'/'Ä‡'/'Å¡' style text (UTF-8 decoded as cp1252/latin-1), repeatedly if double-encoded.
    With legacy=True also map single-byte cp1250/ISO-8859-2 confusions (è->č, æ->ć, ð->đ, ¹->š, ¾->ž).
    legacy is opt-in because è/æ/ð are legitimate in French, Danish, Icelandic text."""
    for _ in range(max_rounds):
        if not _UTF8_MARKERS.search(text):
            break
        try:
            fixed = _to_bytes_1252(text).decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            break
        if fixed == text:
            break
        text = fixed
    if legacy:
        text = "".join(_LEGACY_1250.get(ch, ch) for ch in text)
    return normalize(text)

# ---------------------------------------------------------------------------
# Vocative (conservative). Returns (form, confident: bool).
# ---------------------------------------------------------------------------

# Common Croatian male first names ending in a consonant, with their standard vocative.
_MALE_VOC = {
    "Ivan": "Ivane", "Tomislav": "Tomislave", "Petar": "Petre", "Filip": "Filipe",
    "Stjepan": "Stjepane", "Antun": "Antune", "Matej": "Mateju", "Andrej": "Andreju", "Krešimir": "Krešimire",
    "Damir": "Damire", "Zvonimir": "Zvonimire", "Vladimir": "Vladimire", "Branimir": "Branimire",
    "Dražen": "Dražene", "Goran": "Gorane", "Zoran": "Zorane", "Dejan": "Dejane", "Igor": "Igore",
    "Robert": "Roberte", "Marin": "Marine", "Martin": "Martine", "Valentin": "Valentine", "Leon": "Leone",
    "Fran": "Frane", "Jakov": "Jakove", "Davor": "Davore", "Dalibor": "Dalibore", "Mihovil": "Mihovile",
    "Vedran": "Vedrane", "Mladen": "Mladene", "Nenad": "Nenade", "Bojan": "Bojane", "Neven": "Nevene",
    "Slaven": "Slavene", "Boris": "Borise", "Denis": "Denise", "Kristijan": "Kristijane",
    "Gabrijel": "Gabrijele", "Šimun": "Šimune", "Aleksandar": "Aleksandre", "Dragan": "Dragane",
    "Hrvoje": "Hrvoje", "Tihomir": "Tihomire", "Ivica": "Ivica", "Emanuel": "Emanuele", "David": "Davide",
    "Adam": "Adame", "Vid": "Vide", "Roko": "Roko", "Edin": "Edine", "Dino": "Dino",
    "Lovro": "Lovro", "Bernard": "Bernarde", "Bartol": "Bartole", "Toma": "Toma",
    "Tin": "Tine", "Patrik": None, "Dominik": None, "Domagoj": None, "Juraj": None,
    "Mirko": "Mirko", "Željko": "Željko",
}
_FEMALE_HINT = {"Ines", "Nives", "Karmen", "Dolores", "Doris", "Ruth", "Miriam", "Mirjam", "Ester", "Margit"}
_PALATAL_END = ("j", "lj", "nj", "č", "ć", "dž", "đ", "š", "ž")


def vocative(name, gender=None, surname=False, decline_ic=False):
    """Conservative vocative.

    First names:
      * female (or name ending in -a, unless known male): unchanged - the neutral, conventional form
        (Ana, Ivana, Marija). The -o forms (Ano, Ivano) are colloquial/marked; never generate them.
      * male ending in a vowel (Marko, Ante, Luka, Mario): unchanged.
      * male consonant-final: only names in the curated table, plus the safe Slavic suffixes
        -mir/-slav (+e) and -ej (+u). Anything else is returned unchanged with confident=False.
    Surnames (surname=True): unchanged. After "gospodine"/"gospođo" the nominative is accepted in
    current usage and handbooks; pass decline_ic=True to produce the textbook -iću form for -ić.
    Female surnames are never declined.
    """
    name = normalize(name).strip()
    if not name:
        return name, False
    if " " in name or "-" in name:
        parts = re.split(r"([ -])", name)
        res = [vocative(p, gender, surname, decline_ic) if p not in (" ", "-") else (p, True) for p in parts]
        return "".join(r[0] for r in res), all(r[1] for r in res)
    if surname:
        if gender == "m" and decline_ic and name.endswith("ić"):
            return name + "u", True
        return name, gender in ("m", "f")
    if name in _MALE_VOC and gender != "f":
        v = _MALE_VOC[name]
        return (v, True) if v else (name, False)
    if gender == "f" or (gender is None and (name.endswith("a") or name in _FEMALE_HINT)):
        return name, gender == "f" or name.endswith("a")
    if gender is None:
        return name, False
    # male, not in table
    if name[-1] in "aeiou":
        return name, True
    low = name.lower()
    if low.endswith(("mir", "slav")):
        return name + "e", True
    if low.endswith("ej"):
        return name + "u", True
    return name, False


def greeting(first="", last="", gender=None, formal=True):
    """Salutation line. Formal: 'Poštovani gospodine Horvat,' / 'Poštovana gospođo Horvat,'.
    Informal: 'Dragi Ivane,' / 'Draga Ana,'. Unknown gender -> 'Poštovani,' (formal) or
    'Dobar dan, Ana Horvat,' (informal, nominative full name)."""
    first, last = normalize(first).strip(), normalize(last).strip()
    if formal:
        if gender == "m" and last:
            return "Poštovani gospodine %s," % vocative(last, "m", surname=True)[0]
        if gender == "f" and last:
            return "Poštovana gospođo %s," % last
        return "Poštovani,"
    if gender in ("m", "f") and first:
        v, ok = vocative(first, gender)
        if ok:
            return ("Dragi %s," if gender == "m" else "Draga %s,") % v
    full = (first + " " + last).strip()
    return "Dobar dan, %s," % full if full else "Dobar dan,"

# ---------------------------------------------------------------------------
# Place names
# ---------------------------------------------------------------------------

_HERE = os.path.dirname(os.path.abspath(__file__))
TOPONYMS = os.path.join(_HERE, "..", "assets", "toponyms.csv")
_PLACES = None


def _load_places():
    global _PLACES
    if _PLACES is None:
        with open(TOPONYMS, encoding="utf-8", newline="") as f:
            _PLACES = list(csv.DictReader(f))
    return _PLACES


def place(name, type_=None):
    """All rows matching name (diacritics-insensitive). Islands and same-name towns are separate rows
    (Hvar town: u Hvaru, Hvar island: na Hvaru)."""
    key = fold(name)
    rows = [r for r in _load_places() if fold(r["name"]) == key]
    if type_:
        rows = [r for r in rows if r["type"].startswith(type_)]
    return rows

# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def _self_test():
    fails = []

    def eq(got, exp, label):
        if got != exp:
            fails.append("%s: expected %r, got %r" % (label, exp, got))

    # plurals - expected values match Node 22 Intl.PluralRules('hr') (ICU 77, CLDR 47)
    exp = {0: "other", 1: "one", 2: "few", 3: "few", 4: "few", 5: "other", 10: "other", 11: "other",
           12: "other", 14: "other", 15: "other", 20: "other", 21: "one", 22: "few", 24: "few",
           25: "other", 101: "one", 111: "other", 112: "other", 121: "one", 1001: "one", 1011: "other"}
    for n, c in exp.items():
        eq(plural(n), c, "plural(%d)" % n)
    for n, c in [("1.1", "one"), ("1.5", "other"), ("2.1", "one"), ("0.1", "one"), (0.2, "few"),
                 ("2.5", "other"), ("21.1", "one"), ("11.1", "one"), ("1.0", "other"), ("2.0", "other"),
                 (1.0, "one"), ("1,5", "other"), ("0.11", "other"), ("0.12", "other"), ("3.22", "few"),
                 (Decimal("5.00"), "other"), ("1.21", "one")]:
        eq(plural(n), c, "plural(%r)" % (n,))
    eq(plural_form(22, "dan", "dana", "dana"), "dana", "22 dana")
    eq(plural_form(25, "dan", "dana", "dana"), "dana", "25 dana")
    eq(plural_form(21, "poruka", "poruke", "poruka"), "poruka", "21 poruka")
    eq(plural_form(23, "poruka", "poruke", "poruka"), "poruke", "23 poruke")
    eq(plural_form(13, "korisnik", "korisnika", "korisnika"), "korisnika", "13 korisnika")
    for n in range(0, 300):
        cldr = {"one": 0, "few": 1, "other": 2}[plural(n)]
        eq(gettext_index(n), cldr, "gettext(%d)" % n)

    # folding / slugs
    eq(fold("Čćšžđ ČĆŠŽĐ"), "ccszd ccszd", "fold")
    eq(fold("Đakovo", dj=True), "djakovo", "fold dj")
    eq(search_variants("Đurđevac"), {"durdevac", "djurdjevac"}, "variants")
    eq(fold("ǆem ǉubav ǋiva"), "džem ljubav njiva".replace("ž", "z"), "fold digraph cps")
    eq(fold("čevapčić"), "cevapcic", "fold NFD input")
    eq(slugify("Šibenik – Đakovo: 25 % popusta!"), "sibenik-dakovo-25-popusta", "slug")
    eq(slugify("Šibenik – Đakovo", dj=True), "sibenik-djakovo", "slug dj")
    eq(slugify("Ćevapi & pivo"), "cevapi-i-pivo", "slug &")
    eq(slugify("Žuti  čamac...   "), "zuti-camac", "slug spaces")
    eq(normalize("ǄAMIJA ǅamija"), "DŽAMIJA Džamija", "normalize digraph")

    # collation - expected order produced by Node 22 Intl.Collator('hr') on the same list
    words = ["čaša", "cesta", "ćup", "dno", "džem", "đak", "dub", "ljubav", "lopta", "luk", "njiva",
             "noga", "nož", "šuma", "sat", "žaba", "zec", "Zagreb", "Čakovec", "Đakovo", "Crikvenica",
             "Ćićarija", "Lika", "Ljubljana", "Ludbreg", "Nin", "Njivice", "Novalja", "Dubrovnik", "Drniš",
             "Džamija", "Šibenik", "Split", "Sisak", "Županja", "Zadar", "Osijek", "Ozalj"]
    intl = ("cesta,Crikvenica,Čakovec,čaša,Ćićarija,ćup,dno,Drniš,dub,Dubrovnik,Džamija,džem,đak,Đakovo,"
            "Lika,lopta,Ludbreg,luk,ljubav,Ljubljana,Nin,noga,Novalja,nož,njiva,Njivice,Osijek,Ozalj,sat,"
            "Sisak,Split,Šibenik,šuma,Zadar,Zagreb,zec,žaba,Županja").split(",")
    eq(hr_sorted(words), intl, "collation vs Intl.Collator('hr')")
    eq(hr_sorted(["ana", "Ana", "ána", "anb"]), ["ana", "Ana", "ána", "anb"], "collation tiers")
    eq(hr_sorted(["b", "10", "2", "a b", "ab"]), ["10", "2", "a b", "ab", "b"], "collation digits/space (Intl default, not numeric)")

    # mojibake
    eq(fix_mojibake("Ä\x8dokolada"), "čokolada", "moji latin1")
    eq(fix_mojibake("Å¡kola Ä‡evapi Å¾aba Ä‘ak"), "škola ćevapi žaba đak", "moji cp1252")
    eq(fix_mojibake("ÄŒakovec Ä\u0090akovo"), "Čakovec Đakovo", "moji capitals")
    eq(fix_mojibake("ÃƒÂ©"), "é", "moji double")
    eq(fix_mojibake("Zagreb, Ilica 1"), "Zagreb, Ilica 1", "moji clean ascii")
    eq(fix_mojibake("čokolada"), "čokolada", "moji clean hr")
    eq(fix_mojibake("Kuæa u Ðakovu, ¹kola, mo¾da, èaj", legacy=True), "Kuća u Đakovu, škola, možda, čaj", "moji legacy")
    eq(fix_mojibake("café"), "café", "moji no legacy keeps é")

    # vocative
    for n, g, v in [("Ivan", "m", "Ivane"), ("Petar", "m", "Petre"), ("Marko", "m", "Marko"),
                    ("Luka", "m", "Luka"), ("Ana", "f", "Ana"), ("Ivana", None, "Ivana"),
                    ("Matej", "m", "Mateju"), ("Krešimir", "m", "Krešimire"), ("Ines", "f", "Ines"),
                    ("Ratimir", "m", "Ratimire"), ("Miroslav", "m", "Miroslave"), ("Dominik", "m", "Dominik"),
                    ("John", "m", "John"), ("Ivan", None, "Ivane"), ("Ivan-Mario", "m", "Ivane-Mario")]:
        eq(vocative(n, g)[0], v, "vocative(%s)" % n)
    eq(vocative("John", "m")[1], False, "vocative John not confident")
    eq(vocative("Dominik", "m")[1], False, "vocative Dominik not confident")
    eq(vocative("Horvat", "m", surname=True)[0], "Horvat", "surname nominative")
    eq(vocative("Babić", "m", surname=True, decline_ic=True)[0], "Babiću", "surname -iću")
    eq(vocative("Babić", "f", surname=True, decline_ic=True)[0], "Babić", "female surname")
    eq(greeting("Ivan", "Horvat", "m"), "Poštovani gospodine Horvat,", "greet m")
    eq(greeting("Ana", "Kovač", "f"), "Poštovana gospođo Kovač,", "greet f")
    eq(greeting("Ana", "Kovač"), "Poštovani,", "greet unknown formal")
    eq(greeting("Ivan", "Horvat", "m", formal=False), "Dragi Ivane,", "greet informal m")
    eq(greeting("Marija", "Horvat", "f", formal=False), "Draga Marija,", "greet informal f")
    eq(greeting("Alex", "Horvat", None, formal=False), "Dobar dan, Alex Horvat,", "greet unknown informal")
    eq(greeting("John", "Smith", "m", formal=False), "Dobar dan, John Smith,", "greet unsure male")

    # places
    try:
        z = place("Zagreb")[0]
        eq((z["genitive"], z["locative"], z["from_form"]), ("Zagreba", "u Zagrebu", "iz Zagreba"), "place Zagreb")
        eq(place("hvar", "otok")[0]["locative"], "na Hvaru", "place Hvar island")
        eq(place("Hvar", "grad")[0]["locative"], "u Hvaru", "place Hvar town")
        eq(place("Cres", "grad")[0]["from_form"], "iz Cresa", "place Cres town")
        eq(place("Rijeka")[0]["locative"], "u Rijeci", "place Rijeka")
        eq(place("Sibenik")[0]["ethnic_m"], "Šibenčanin", "place folded lookup")
        eq(place("Šolta")[0]["from_form"], "sa Šolte", "place sa")
        eq(place("Brač")[0]["from_form"], "s Brača", "place s")
        names = [r["name"] for r in _load_places()]
        if len(names) < 150:
            fails.append("toponyms.csv has only %d rows" % len(names))
    except FileNotFoundError:
        fails.append("assets/toponyms.csv not found")

    if fails:
        print("SELF-TEST FAILED (%d):" % len(fails))
        for f in fails:
            print("  -", f)
        return 1
    print("self-test OK (plural, gettext, fold, slugify, collation, mojibake, vocative, greeting, place)")
    return 0

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if "--self-test" in argv:
        return _self_test()
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("plural"); a.add_argument("n"); a.add_argument("forms", nargs="*")
    a = sub.add_parser("slugify"); a.add_argument("text"); a.add_argument("--dj", action="store_true")
    a = sub.add_parser("fold"); a.add_argument("text"); a.add_argument("--dj", action="store_true")
    a = sub.add_parser("sort"); a.add_argument("file", nargs="?")
    a = sub.add_parser("fix-mojibake"); a.add_argument("text"); a.add_argument("--legacy", action="store_true")
    a = sub.add_parser("vocative"); a.add_argument("name"); a.add_argument("--gender", choices=["m", "f"])
    a.add_argument("--surname", action="store_true"); a.add_argument("--decline-ic", action="store_true")
    a = sub.add_parser("greeting"); a.add_argument("--first", default=""); a.add_argument("--last", default="")
    a.add_argument("--gender", choices=["m", "f"]); g = a.add_mutually_exclusive_group()
    g.add_argument("--formal", action="store_true", default=True); g.add_argument("--informal", action="store_true")
    a = sub.add_parser("place"); a.add_argument("name"); a.add_argument("--type", dest="type_")
    args = p.parse_args(argv)

    if args.cmd == "plural":
        cat = plural(args.n)
        if len(args.forms) == 3:
            print("%s %s" % (args.n, plural_form(args.n, *args.forms)))
        else:
            print(cat)
    elif args.cmd == "slugify":
        print(slugify(args.text, dj=args.dj))
    elif args.cmd == "fold":
        print(fold(args.text, dj=args.dj))
    elif args.cmd == "sort":
        src = open(args.file, encoding="utf-8") if args.file else sys.stdin
        lines = [l.rstrip("\n") for l in src if l.strip()]
        print("\n".join(hr_sorted(lines)))
    elif args.cmd == "fix-mojibake":
        text = sys.stdin.read() if args.text == "-" else args.text
        print(fix_mojibake(text, legacy=args.legacy))
    elif args.cmd == "vocative":
        v, ok = vocative(args.name, args.gender, args.surname, args.decline_ic)
        print(v if ok else "%s\t(not confident - nominative kept)" % v)
    elif args.cmd == "greeting":
        print(greeting(args.first, args.last, args.gender, formal=not args.informal))
    elif args.cmd == "place":
        rows = place(args.name, args.type_)
        if not rows:
            print("not in assets/toponyms.csv - build the forms by hand and check them (see references/places.md)")
            return 1
        for r in rows:
            print("%s (%s, %s): G %s | %s | %s | %s %s | source: %s%s" % (
                r["name"], r["type"], r["county"] or "-", r["genitive"], r["locative"], r["from_form"],
                r["ethnic_m"], r["ethnic_f"], r["source"], (" | " + r["note"]) if r["note"] else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
