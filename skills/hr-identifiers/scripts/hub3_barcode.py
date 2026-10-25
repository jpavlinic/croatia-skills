#!/usr/bin/env python3
"""Build the HUB-3 (HUB 3A uplatnica) PDF417 text payload, header HRVHUB30.

Implements: HUB "Uputa o upotrebi PDF417 2D bar koda na papirnatim nalozima za placanje
u domacem platnom prometu (obrazac HUB3A), Prilog A - Format zapisa 2D barkoda prema
HUB-3 standardu", verzija 6, rujan 2022 (euro amounts, applies from 1 Jan 2023):
https://hub.hr/sites/default/files/inline-files/2DBK_EUR_Uputa_1.pdf

The script prints the TEXT that goes into the barcode. Python's standard library has
no PDF417 encoder, so drawing the symbol is a separate step with an external library
(see --help-render). Python 3 standard library only; offline; deterministic.

Fields (max length in characters, not bytes; separator LF 0x0A; UTF-8):
   1 header HRVHUB30 (8)       2 currency EUR (3)          3 amount, cents, 15 digits zero-padded
   4 payer name (30)           5 payer street+no. (27)     6 payer postcode+place (27)
   7 recipient name (25)       8 recipient street (25)     9 recipient postcode+place (27)
  10 recipient IBAN (21)      11 model HRnn (4)           12 poziv na broj primatelja (22)
  13 purpose code (4)         14 description (35)
"""

import argparse
import json
import os
import re
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

sys.dont_write_bytecode = True  # keep the plugin folder clean
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hr_ids  # noqa: E402  (same folder)

HEADER = "HRVHUB30"
FIELDS = [  # (key, max_len, label)
    ("payer_name", 30, "Platitelj (naziv/ime i prezime)"),
    ("payer_street", 27, "Adresa platitelja (ulica i broj)"),
    ("payer_city", 27, "Adresa platitelja (postanski broj i mjesto)"),
    ("recipient_name", 25, "Primatelj (naziv/ime i prezime)"),
    ("recipient_street", 25, "Adresa primatelja (ulica i broj)"),
    ("recipient_city", 27, "Adresa primatelja (postanski broj i mjesto)"),
    ("iban", 21, "Broj racuna primatelja (IBAN)"),
    ("model", 4, "Model kontrole poziva na broj primatelja"),
    ("reference", 22, "Poziv na broj primatelja"),
    ("purpose", 4, "Sifra namjene (ISO 20022)"),
    ("description", 35, "Opis placanja"),
]
# Allowed characters (spec, "Zapis 2D barkoda"): digits, the 27 letters of the Croatian
# alphabet (DZ, LJ, NJ written as two letters), Q W X Y, space and , . : - + ? ' / ( )
ALLOWED = re.compile(r"^[0-9A-Za-zČčĆćĐđŠšŽž ,.:\-+?'/()]*$")

RENDER_HELP = """Rendering the PDF417 symbol (not possible with the standard library):

  pip install pdf417gen pillow          # third-party, optional
  python3 hub3_barcode.py ... > payload.txt
  python3 - <<'PY'
  from pdf417gen import encode, render_image
  text = open('payload.txt', encoding='utf-8').read()
  codes = encode(text, columns=9, security_level=4)   # HUB: 9 data columns, ECL 4
  render_image(codes, scale=3, ratio=3, padding=10).save('hub3.png')  # module h:w = 3:1
  PY

HUB requirements: module width 0.254 mm (10 mil) when printed, height:width 3:1,
error-correction level 4, 9 data columns, binary encoding, no Compact/Macro PDF417,
printed size about 58 x 26 mm max incl. quiet zone. pdf417gen chooses compaction modes
itself; if your version offers a force-binary option use it (check help(encode)),
and always test-scan the result with several Croatian bank apps. VERIFY.
"""


def parse_amount(text):
    """'123,55' / '123.55' / '1.234,55' -> cents (int). Empty -> 0."""
    if text is None or str(text).strip() == "":
        return 0
    t = str(text).strip().replace(" ", "")
    if "," in t and "." in t:
        t = t.replace(".", "").replace(",", ".")  # Croatian style 1.234,55
    else:
        t = t.replace(",", ".")
    try:
        d = Decimal(t)
    except InvalidOperation:
        raise ValueError("amount not understood: %r" % text)
    if d < 0:
        raise ValueError("amount must not be negative")
    cents = int((d * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    if (d * 100) != cents:
        raise ValueError("amount has more than 2 decimals: %r" % text)
    if cents > 10 ** 15 - 1:
        raise ValueError("amount too large for 15 digits")
    return cents


def build(data, truncate=False, strict=True, trailing_lf=True):
    """Return (payload, warnings). Raises ValueError on invalid input."""
    warnings = []
    cur = (data.get("currency") or "EUR").upper()
    if cur != "EUR":
        raise ValueError("HUB-3 version 6 uses EUR only")
    amount = "%015d" % parse_amount(data.get("amount"))
    values = {}
    for key, max_len, label in FIELDS:
        v = (data.get(key) or "").strip()
        v = re.sub(r"\s+", " ", v)
        if key in ("iban", "model", "purpose"):
            v = v.replace(" ", "").upper()
        if key == "reference":
            v = v.replace(" ", "")
        if not ALLOWED.match(v):
            bad = sorted(set(ch for ch in v if not ALLOWED.match(ch)))
            raise ValueError("%s contains characters not allowed by HUB-3: %s" % (label, "".join(bad)))
        if len(v) > max_len:
            if truncate and key not in ("iban", "model", "reference", "purpose"):
                warnings.append("%s truncated to %d characters" % (label, max_len))
                v = v[:max_len]
            else:
                raise ValueError("%s longer than %d characters (%d)" % (label, max_len, len(v)))
        values[key] = v
    if not values["iban"]:
        raise ValueError("recipient IBAN is required")
    ok, msg, _ = hr_ids.iban_check(values["iban"])
    if not ok:
        raise ValueError("IBAN invalid: " + msg)
    if not values["iban"].startswith("HR"):
        warnings.append("HUB 3A is for domestic payments; the spec describes a 21-character HR IBAN")
    model = values["model"]
    if model and not re.fullmatch(r"HR\d{2}", model):
        raise ValueError("model must be 'HR' + 2 digits, e.g. HR01, HR00, HR99")
    if model:
        ok, msgs = hr_ids.reference_check(model, values["reference"])
        if not ok:
            text = "poziv na broj does not satisfy %s: %s" % (model, "; ".join(msgs))
            if strict:
                raise ValueError(text + " (use --no-strict to only warn)")
            warnings.append(text)
    elif values["reference"]:
        raise ValueError("a reference needs a model (HR00 when no check digit, HR99 when there is no reference)")
    if values["purpose"] and not re.fullmatch(r"[A-Z]{4}", values["purpose"]):
        raise ValueError("purpose code must be 4 letters (ISO 20022 ExternalPurpose1Code, e.g. COST, OTHR)")
    lines = [HEADER, cur, amount] + [values[k] for k, _, _ in FIELDS]
    payload = "\n".join(lines) + ("\n" if trailing_lf else "")
    if len(payload.replace("\n", "")) > 273:
        raise ValueError("payload exceeds 273 characters")
    return payload, warnings


def self_test():
    failures = []

    def expect(name, got, want):
        if got != want:
            failures.append("%s: got %r, want %r" % (name, got, want))

    # Structure mirrors the example in the HUB spec (v6, p. 10) with fictitious names and a
    # reference that passes HR01 (the spec's own illustrative reference does not).
    data = {
        "amount": "123,55",
        "payer_name": "ANA HORVAT",
        "payer_street": "PRIMJERNA ULICA 1",
        "payer_city": "10000 ZAGREB",
        "recipient_name": "PRIMJER d.o.o.",
        "recipient_street": "ILICA 1",
        "recipient_city": "21000 SPLIT",
        "iban": "HR12 1001 0051 8630 0016 0",
        "model": "HR01",
        "reference": "102-3057-89016",
        "purpose": "COST",
        "description": "Troškovi za 1. mjesec",
    }
    want = ("HRVHUB30\nEUR\n000000000012355\nANA HORVAT\nPRIMJERNA ULICA 1\n10000 ZAGREB\n"
            "PRIMJER d.o.o.\nILICA 1\n21000 SPLIT\nHR1210010051863000160\nHR01\n102-3057-89016\n"
            "COST\nTroškovi za 1. mjesec\n")
    got, warns = build(data)
    expect("payload", got, want)
    expect("no warnings", warns, [])
    expect("14 fields", len(got.rstrip("\n").split("\n")), 14)
    expect("amount 1.234,56", parse_amount("1.234,56"), 123456)
    expect("amount 0.1", parse_amount("0.1"), 10)
    expect("amount empty", parse_amount(""), 0)
    for bad in ("12,345", "-1", "abc"):
        try:
            parse_amount(bad)
            failures.append("amount %r should fail" % bad)
        except ValueError:
            pass

    def fails(d, **kw):
        try:
            build(d, **kw)
            return False
        except ValueError:
            return True

    expect("long name rejected", fails(dict(data, recipient_name="X" * 26)), True)
    expect("long name truncated", build(dict(data, recipient_name="X" * 26), truncate=True)[0].split("\n")[6], "X" * 25)
    expect("bad char rejected", fails(dict(data, description="cijena 10€")), True)
    expect("bad iban rejected", fails(dict(data, iban="HR1310010051863000160")), True)
    expect("bad reference rejected", fails(dict(data, reference="102-3057-89017")), True)
    expect("bad reference warn", len(build(dict(data, reference="102-3057-89017"), strict=False)[1]), 1)
    expect("HR99 empty ok", fails(dict(data, model="HR99", reference="")), False)
    expect("reference without model", fails(dict(data, model="", reference="123")), True)
    expect("bad purpose", fails(dict(data, purpose="CO1T")), True)
    expect("no trailing LF", build(data, trailing_lf=False)[0].endswith("mjesec"), True)
    expect("utf8 bytes", len(want.encode("utf-8")), len(want) + 1)  # one 'š' = 2 bytes
    if failures:
        print("SELF-TEST FAILED (%d):" % len(failures))
        for f in failures:
            print("  - " + f)
        return 1
    print("self-test passed (hub3_barcode.py): all vectors OK")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--help-render", action="store_true", help="how to draw the PDF417 symbol")
    ap.add_argument("--from-json", metavar="FILE", help="read fields from a JSON object with the keys below")
    ap.add_argument("--amount", help="e.g. 123,55 or 123.55 (EUR)")
    ap.add_argument("--currency", default="EUR")
    for key, max_len, label in FIELDS:
        ap.add_argument("--" + key.replace("_", "-"), dest=key, help="%s (max %d)" % (label, max_len))
    ap.add_argument("--truncate", action="store_true", help="truncate over-long text fields instead of failing")
    ap.add_argument("--no-strict", action="store_true", help="only warn when the reference fails its model check")
    ap.add_argument("--no-trailing-lf", action="store_true",
                    help="omit LF after the last field (the spec example shows LF after every field)")
    ap.add_argument("--visible", action="store_true", help="print LF as '\\n' markers for inspection")
    ap.add_argument("--hex", action="store_true", help="print UTF-8 bytes as hex")
    ap.add_argument("--png", action="store_true", help="not supported (no stdlib PDF417 encoder); see --help-render")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if args.help_render or args.png:
        print(RENDER_HELP)
        return 0 if args.help_render else 2
    data = {}
    if args.from_json:
        with open(args.from_json, encoding="utf-8") as fh:
            data = json.load(fh)
    for key in ["amount", "currency"] + [k for k, _, _ in FIELDS]:
        val = getattr(args, key)
        if val is not None:
            data[key] = val
    try:
        payload, warnings = build(data, truncate=args.truncate, strict=not args.no_strict,
                                  trailing_lf=not args.no_trailing_lf)
    except ValueError as e:
        print("error: %s" % e, file=sys.stderr)
        return 1
    for w in warnings:
        print("warning: %s" % w, file=sys.stderr)
    if args.hex:
        print(payload.encode("utf-8").hex())
    elif args.visible:
        print(payload.replace("\n", "\\n\n"), end="")
    else:
        sys.stdout.write(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
