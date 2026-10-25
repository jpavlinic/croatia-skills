#!/usr/bin/env python3
"""Expand Croatian keywords into inflected and diacritic-free variants.

Rule-based and deliberately conservative. It does NOT know Croatian
morphology in general; it only declines nouns you name, using the class you
give (or explicit forms), and it folds diacritics. Always check the output
against real search data (Search Console queries, Keyword Planner, the SERP).

Two modes:

  forms   Print the paradigm of each noun (singular/plural, main cases)
          plus diacritic-free spellings.

            python3 kw_variants.py forms stan:m2 kuća:f selo:n

  phrase  Take a seed phrase and produce realistic query variants:
          singular <-> plural of the named noun (same case), place name with
          and without the locative ("zagreb" <-> "u zagrebu"), and
          diacritic-free spellings (đ -> d and dj).

            python3 kw_variants.py phrase "najam stana zagreb" --noun stan:m2 --place zagreb:u:zagrebu

Noun spec:  lemma:class[:oblique_stem]   or   lemma:x:f1,f2,...,f12
  m    masculine, consonant-final, short plural      (apartman -> apartmani)
  m2   masculine, consonant-final, long plural -ovi/-evi (stan -> stanovi)
  f    nouns ending in -a (feminine, and masculine like računovođa) (kuća -> kuće)
  fi   feminine ending in a consonant                 (noć -> noći)
  n    neuter ending in -o / -e                       (selo -> sela, more -> mora)
  x    explicit 12 forms in this order:
       sg N,G,D,A,L,I  then  pl N,G,D,A,L,I
  oblique_stem  for nouns that change stem (fleeting a etc.):
       vrabac:m:vrapc  ->  vrapca, vrapcu, vrapci ...

Place spec: lemma:preposition:locative   e.g. split:u:splitu, hvar:na:hvaru
(Croatian place locatives and u/na are irregular; you must supply them.)

Python 3 standard library only. No network access. Run --self-test to check.
"""

import argparse
import json
import sys

CASES = ["N", "G", "D", "A", "L", "I"]
CASE_NAMES_HR = {
    "N": "nominativ", "G": "genitiv", "D": "dativ",
    "A": "akuzativ", "L": "lokativ", "I": "instrumental",
}
PALATALS = ("lj", "nj", "dž", "č", "ć", "đ", "j", "š", "ž", "c")
SIBILARIZATION = {"k": "c", "g": "z", "h": "s"}
VOWELS = set("aeiou")


class SpecError(ValueError):
    pass


# --------------------------------------------------------------------------
# Diacritics
# --------------------------------------------------------------------------

def fold(text, dj="d"):
    """Remove Croatian diacritics. dj='d' gives đ->d, dj='dj' gives đ->dj."""
    out = text.lower()
    out = out.replace("dž", "dz")
    out = out.replace("đ", dj)
    for a, b in (("č", "c"), ("ć", "c"), ("š", "s"), ("ž", "z")):
        out = out.replace(a, b)
    return out


def folded_variants(text):
    """All distinct diacritic-free spellings of text (đ as d and as dj)."""
    seen = []
    for v in (text.lower(), fold(text, "d"), fold(text, "dj")):
        if v not in seen:
            seen.append(v)
    return seen


# --------------------------------------------------------------------------
# Declension
# --------------------------------------------------------------------------

def _ends_palatal(stem):
    return stem.endswith(PALATALS)


def _cluster_end(stem):
    """True if the stem ends in two consonants (genitive plural often inserts
    an 'a' or takes -i: sestra -> sestara, pismo -> pisama). We skip those
    forms instead of guessing."""
    s = stem.lower()
    if len(s) < 2:
        return False
    tail = s[-2:]
    if tail in ("lj", "nj", "dž"):
        # digraph counts as one consonant; look one further back
        return len(s) >= 3 and s[-3] not in VOWELS
    return tail[0] not in VOWELS and tail[1] not in VOWELS


def decline(spec):
    """Return (lemma, forms, warnings).

    forms: dict {("sg"|"pl", case): form or None}. None = deliberately not
    generated (too irregular to guess)."""
    parts = spec.split(":")
    if len(parts) < 2:
        raise SpecError("noun spec must be lemma:class, got %r" % spec)
    lemma = parts[0].strip().lower()
    cls = parts[1].strip().lower()
    extra = ":".join(parts[2:]).strip().lower() if len(parts) > 2 else ""
    warnings = []
    forms = {}

    if not lemma:
        raise SpecError("empty lemma in %r" % spec)

    if cls == "x":
        lst = [f.strip().lower() for f in extra.split(",")]
        if len(lst) != 12 or not all(lst):
            raise SpecError("class x needs 12 comma-separated forms: %r" % spec)
        for i, c in enumerate(CASES):
            forms[("sg", c)] = lst[i]
            forms[("pl", c)] = lst[6 + i]
        return lemma, forms, warnings

    if cls in ("m", "m2"):
        stem = extra or lemma
        if lemma[-1] in VOWELS:
            raise SpecError(
                "%r ends in a vowel; use class x with explicit forms" % lemma)
        palatal = _ends_palatal(stem)
        forms[("sg", "N")] = lemma
        forms[("sg", "G")] = stem + "a"
        forms[("sg", "D")] = stem + "u"
        forms[("sg", "A")] = lemma  # inanimate; animate A = G (see warning)
        forms[("sg", "L")] = stem + "u"
        forms[("sg", "I")] = stem + ("em" if palatal else "om")
        if cls == "m2":
            pstem = stem + ("ev" if palatal else "ov")
        else:
            pstem = stem
        if cls == "m" and stem[-1] in SIBILARIZATION:
            nom_pl = stem[:-1] + SIBILARIZATION[stem[-1]] + "i"
            dl_pl = stem[:-1] + SIBILARIZATION[stem[-1]] + "ima"
        else:
            nom_pl = pstem + "i"
            dl_pl = pstem + "ima"
        forms[("pl", "N")] = nom_pl
        forms[("pl", "G")] = pstem + "a"
        forms[("pl", "D")] = dl_pl
        forms[("pl", "A")] = pstem + "e"
        forms[("pl", "L")] = dl_pl
        forms[("pl", "I")] = dl_pl
        warnings.append(
            "%s: accusative singular given as inanimate (= nominative); "
            "for people/animals it equals the genitive." % lemma)
        return lemma, forms, warnings

    if cls == "f":
        if not lemma.endswith("a"):
            raise SpecError("class f expects a lemma ending in -a: %r" % lemma)
        stem = extra or lemma[:-1]
        forms[("sg", "N")] = lemma
        forms[("sg", "G")] = stem + "e"
        if stem[-1] in SIBILARIZATION:
            forms[("sg", "D")] = None
            forms[("sg", "L")] = None
            warnings.append(
                "%s: dative/locative singular skipped (stem ends in k/g/h; "
                "ruka -> ruci but baka -> baki). Add it by hand." % lemma)
        else:
            forms[("sg", "D")] = stem + "i"
            forms[("sg", "L")] = stem + "i"
        forms[("sg", "A")] = stem + "u"
        forms[("sg", "I")] = stem + "om"
        forms[("pl", "N")] = stem + "e"
        if _cluster_end(stem):
            forms[("pl", "G")] = None
            warnings.append(
                "%s: genitive plural skipped (consonant cluster: "
                "sestra -> sestara, majka -> majki). Add it by hand." % lemma)
        else:
            forms[("pl", "G")] = stem + "a"
        forms[("pl", "D")] = stem + "ama"
        forms[("pl", "A")] = stem + "e"
        forms[("pl", "L")] = stem + "ama"
        forms[("pl", "I")] = stem + "ama"
        return lemma, forms, warnings

    if cls == "fi":
        if lemma[-1] in VOWELS:
            raise SpecError("class fi expects a consonant-final lemma: %r" % lemma)
        stem = extra or lemma
        forms[("sg", "N")] = lemma
        forms[("sg", "G")] = stem + "i"
        forms[("sg", "D")] = stem + "i"
        forms[("sg", "A")] = lemma
        forms[("sg", "L")] = stem + "i"
        forms[("sg", "I")] = None
        warnings.append(
            "%s: instrumental singular skipped (noću / stvari / ljubavlju "
            "vary). Add it by hand." % lemma)
        forms[("pl", "N")] = stem + "i"
        forms[("pl", "G")] = stem + "i"
        forms[("pl", "D")] = stem + "ima"
        forms[("pl", "A")] = stem + "i"
        forms[("pl", "L")] = stem + "ima"
        forms[("pl", "I")] = stem + "ima"
        return lemma, forms, warnings

    if cls == "n":
        if lemma[-1] not in "oe":
            raise SpecError("class n expects a lemma ending in -o/-e: %r" % lemma)
        stem = extra or lemma[:-1]
        forms[("sg", "N")] = lemma
        forms[("sg", "G")] = stem + "a"
        forms[("sg", "D")] = stem + "u"
        forms[("sg", "A")] = lemma
        forms[("sg", "L")] = stem + "u"
        forms[("sg", "I")] = stem + ("om" if lemma.endswith("o") else "em")
        forms[("pl", "N")] = stem + "a"
        if _cluster_end(stem):
            forms[("pl", "G")] = None
            warnings.append(
                "%s: genitive plural skipped (consonant cluster: "
                "pismo -> pisama). Add it by hand." % lemma)
        else:
            forms[("pl", "G")] = stem + "a"
        forms[("pl", "D")] = stem + "ima"
        forms[("pl", "A")] = stem + "a"
        forms[("pl", "L")] = stem + "ima"
        forms[("pl", "I")] = stem + "ima"
        return lemma, forms, warnings

    raise SpecError("unknown class %r in %r (use m, m2, f, fi, n, x)" % (cls, spec))


# --------------------------------------------------------------------------
# Phrase variants
# --------------------------------------------------------------------------

def parse_place(spec):
    parts = [p.strip().lower() for p in spec.split(":")]
    if len(parts) != 3 or not all(parts) or parts[1] not in ("u", "na"):
        raise SpecError(
            "place spec must be lemma:u|na:locative, e.g. hvar:na:hvaru; got %r"
            % spec)
    return parts[0], parts[1], parts[2]


def phrase_variants(seed, noun_specs, place_specs):
    """Return list of (variant, note) for a seed phrase."""
    tokens = seed.lower().split()
    results = []  # list of (tokens, note)
    results.append((tokens, "seed"))
    warnings = []

    # 1. singular <-> plural for each named noun, same case
    for spec in noun_specs:
        lemma, forms, w = decline(spec)
        warnings.extend(w)
        index = {}
        for key, form in forms.items():
            if form:
                index.setdefault(form, []).append(key)
        new = []
        for toks, note in results:
            for i, t in enumerate(toks):
                if t not in index:
                    continue
                keys = index[t]
                if t == lemma:
                    keys = [("sg", "N")]  # treat the dictionary form as N sg
                ambiguous = len({k[0] for k in keys}) > 1
                for number, case in keys:
                    other = "pl" if number == "sg" else "sg"
                    alt = forms.get((other, case))
                    if not alt or alt == t:
                        continue
                    n = "%s %s->%s (%s)" % (lemma, number, other, CASE_NAMES_HR[case])
                    if ambiguous:
                        n += " CHECK: form is ambiguous"
                    new.append((toks[:i] + [alt] + toks[i + 1:], n))
        results.extend(new)

    # 2. place name: bare <-> with locative preposition
    for spec in place_specs:
        lemma, prep, loc = parse_place(spec)
        new = []
        for toks, note in results:
            joined = " ".join(toks)
            if (" %s %s " % (prep, loc)) in (" %s " % joined):
                bare = (" %s " % joined).replace(" %s %s " % (prep, loc),
                                                 " %s " % lemma).strip()
                new.append((bare.split(), "place: bare nominative"))
            elif lemma in toks:
                i = toks.index(lemma)
                new.append((toks[:i] + [prep, loc] + toks[i + 1:],
                            "place: %s + locative" % prep))
        results.extend(new)

    # 3. diacritic folding
    out = []
    seen = set()
    for toks, note in results:
        phrase = " ".join(toks)
        for j, v in enumerate(folded_variants(phrase)):
            if v in seen:
                continue
            seen.add(v)
            out.append((v, note if j == 0 else note + " / no diacritics"))
    return out, warnings


def forms_table(spec):
    lemma, forms, warnings = decline(spec)
    rows = []
    for number in ("sg", "pl"):
        for case in CASES:
            f = forms.get((number, case))
            rows.append({
                "number": number,
                "case": CASE_NAMES_HR[case],
                "form": f,
                "no_diacritics": [v for v in folded_variants(f)[1:]] if f else [],
            })
    return lemma, rows, warnings


# --------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------

def self_test():
    fails = []

    def eq(label, got, want):
        if got != want:
            fails.append("%s: got %r, want %r" % (label, got, want))

    eq("fold ć", fold("ćevapi"), "cevapi")
    eq("fold đ d", fold("računovođa"), "racunovoda")
    eq("fold đ dj", fold("računovođa", "dj"), "racunovodja")
    eq("fold dž", fold("džep"), "dzep")
    eq("variants", folded_variants("Đakovo"), ["đakovo", "dakovo", "djakovo"])

    _, f, _ = decline("stan:m2")
    eq("stan G", f[("sg", "G")], "stana")
    eq("stan L", f[("sg", "L")], "stanu")
    eq("stan I", f[("sg", "I")], "stanom")
    eq("stan pl N", f[("pl", "N")], "stanovi")
    eq("stan pl G", f[("pl", "G")], "stanova")
    eq("stan pl L", f[("pl", "L")], "stanovima")

    _, f, _ = decline("nož:m2")
    eq("nož I", f[("sg", "I")], "nožem")
    eq("nož pl N", f[("pl", "N")], "noževi")

    _, f, _ = decline("apartman:m")
    eq("apartman pl N", f[("pl", "N")], "apartmani")
    eq("apartman pl G", f[("pl", "G")], "apartmana")

    _, f, _ = decline("računovodstveni:x:" + ",".join(["a"] * 12))
    eq("x forms", f[("pl", "I")], "a")

    _, f, _ = decline("frizer:m")
    eq("frizer pl N", f[("pl", "N")], "frizeri")

    _, f, _ = decline("vojnik:m")
    eq("vojnik pl N (sibilarization)", f[("pl", "N")], "vojnici")

    _, f, _ = decline("vrabac:m:vrapc")
    eq("vrabac G (oblique stem)", f[("sg", "G")], "vrapca")

    _, f, _ = decline("kuća:f")
    eq("kuća G", f[("sg", "G")], "kuće")
    eq("kuća L", f[("sg", "L")], "kući")
    eq("kuća pl G", f[("pl", "G")], "kuća")
    eq("kuća pl L", f[("pl", "L")], "kućama")

    _, f, w = decline("ruka:f")
    eq("ruka D skipped", f[("sg", "D")], None)
    _, f, w = decline("sestra:f")
    eq("sestra pl G skipped", f[("pl", "G")], None)

    _, f, _ = decline("noć:fi")
    eq("noć G", f[("sg", "G")], "noći")
    eq("noć pl D", f[("pl", "D")], "noćima")

    _, f, _ = decline("selo:n")
    eq("selo I", f[("sg", "I")], "selom")
    eq("selo pl N", f[("pl", "N")], "sela")
    _, f, _ = decline("more:n")
    eq("more I", f[("sg", "I")], "morem")
    _, f, _ = decline("pismo:n")
    eq("pismo pl G skipped", f[("pl", "G")], None)

    out, _ = phrase_variants("najam stana zagreb", ["stan:m2"], ["zagreb:u:zagrebu"])
    got = [v for v, _ in out]
    for want in ("najam stana zagreb", "najam stanova zagreb",
                 "najam stana u zagrebu", "najam stanova u zagrebu"):
        if want not in got:
            fails.append("phrase missing %r in %r" % (want, got))

    out, _ = phrase_variants("ćevapi u splitu", [], ["split:u:splitu"])
    got = [v for v, _ in out]
    for want in ("ćevapi u splitu", "cevapi u splitu", "ćevapi split", "cevapi split"):
        if want not in got:
            fails.append("phrase missing %r in %r" % (want, got))

    out, _ = phrase_variants("apartmani hvar", ["apartman:m"], ["hvar:na:hvaru"])
    got = [v for v, _ in out]
    for want in ("apartman hvar", "apartmani na hvaru", "apartman na hvaru"):
        if want not in got:
            fails.append("phrase missing %r in %r" % (want, got))

    for bad in ("stan", "auto:m", "kuća:q", "kuć:f", "x:x:a,b"):
        try:
            decline(bad)
            fails.append("expected SpecError for %r" % bad)
        except SpecError:
            pass
    try:
        parse_place("hvar:iz:hvara")
        fails.append("expected SpecError for bad place")
    except SpecError:
        pass

    if fails:
        print("SELF-TEST FAILED (%d):" % len(fails))
        for f in fails:
            print("  - " + f)
        return 1
    print("self-test OK (all checks passed)")
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

NOTICE = ("Rule-based variants for keyword research only. Check every form "
          "against real queries and the SERP before using it.")


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Croatian keyword variants: noun cases, singular/plural, "
                    "u/na + locative for places, diacritic-free spellings.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("Python 3 standard library")[0].split("Two modes:")[1])
    p.add_argument("--self-test", action="store_true", help="run built-in tests")
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--json", action="store_true", help="JSON output")
    sub = p.add_subparsers(dest="mode")

    pf = sub.add_parser("forms", parents=[common], help="print noun paradigms")
    pf.add_argument("nouns", nargs="+", help="noun specs, e.g. stan:m2 kuća:f")

    pp = sub.add_parser("phrase", parents=[common], help="expand a seed phrase")
    pp.add_argument("seed", help='seed phrase, e.g. "najam stana zagreb"')
    pp.add_argument("--noun", action="append", default=[],
                    help="noun in the seed to switch singular/plural (repeatable)")
    pp.add_argument("--place", action="append", default=[],
                    help="place spec lemma:u|na:locative (repeatable)")

    args = p.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.mode:
        p.print_help()
        return 2

    try:
        if args.mode == "forms":
            data = []
            all_w = []
            for spec in args.nouns:
                lemma, rows, w = forms_table(spec)
                data.append({"lemma": lemma, "forms": rows})
                all_w.extend(w)
            if args.json:
                print(json.dumps({"notice": NOTICE, "nouns": data,
                                  "warnings": all_w}, ensure_ascii=False, indent=2))
            else:
                print(NOTICE)
                for d in data:
                    print("\n%s" % d["lemma"])
                    for r in d["forms"]:
                        form = r["form"] or "(skipped, add by hand)"
                        nd = ", ".join(r["no_diacritics"])
                        print("  %-2s %-12s %-20s %s" % (
                            r["number"], r["case"], form, nd))
                for w in all_w:
                    print("note: " + w)
        else:
            out, w = phrase_variants(args.seed, args.noun, args.place)
            if args.json:
                print(json.dumps({"notice": NOTICE,
                                  "variants": [{"query": v, "how": n} for v, n in out],
                                  "warnings": w}, ensure_ascii=False, indent=2))
            else:
                print(NOTICE + "\n")
                for v, n in out:
                    print("%-45s %s" % (v, n))
                for x in w:
                    print("note: " + x)
    except SpecError as e:
        print("error: %s" % e, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
