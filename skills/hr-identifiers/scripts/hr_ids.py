#!/usr/bin/env python3
"""Validate, parse and generate (fictitious test data) Croatian identifiers.

Python 3 standard library only. Offline and deterministic (no network).

Subcommands:
  oib validate|generate        OIB, ISO 7064 MOD 11,10 (Pravilnik o OIB-u, cl. 3 st. 1)
  vat validate                 PDV ID = "HR" + OIB (Zakon o PDV-u, cl. 77 st. 6), offline format check
  iban validate|generate       HR IBAN (Odluka o transakcijskim racunima, NN 13/2025, cl. 7-11)
  bic validate                 BIC/SWIFT structure (ISO 9362) + known Croatian banks
  mb validate|generate         DZS maticni broj poslovnog subjekta (8 digits, MOD 11 weights 8..2)
  mbs validate                 Sudski registar MBS (9 digits, MOD 11,10 - empirically, VERIFY)
  jmbg validate                legacy 13-digit JMBG / MBG
  reference validate           poziv na broj HR00-HR99 (HUB Jedinstveni pregled, primjena 01/2026) and RF (ISO 11649)
  reference checkdigit         compute one check digit with a named method
  phone normalize              Croatian numbers -> E.164 + classification (HAKOM Plan numeriranja, NN 45/2023)
  postcode check               5-digit postal code shape + approximate region
  plate check                  standard vehicle registration plate (Pravilnik NN 130/2017)

Privacy: OIB and JMBG of natural persons are personal data (GDPR). By default the
validators print a masked value; pass --show to print it in full. Never log them.

Generated values are FICTITIOUS TEST DATA. A random checksum-valid OIB/IBAN can
coincide with a real one - use generated values only in test/dev systems.
"""

import argparse
import json
import random
import re
import sys
from datetime import date

FICTITIOUS = "# FICTITIOUS TEST DATA - checksum-valid but not issued by any authority; do not use in production"

# ---------------------------------------------------------------------------
# Check-digit algorithms
# ---------------------------------------------------------------------------


def iso7064_mod11_10(payload):
    """Return the ISO 7064 MOD 11,10 check digit for a digit string (hybrid system)."""
    p = 10
    for ch in payload:
        s = (p + int(ch)) % 10
        if s == 0:
            s = 10
        p = (2 * s) % 11
    return (11 - p) % 10


def mod11ini(payload):
    """HUB 'MOD11INI': weights 2,3,4,... from the right (uncapped); remainder 0 or 1 -> 0."""
    total = sum(int(c) * w for c, w in zip(reversed(payload), range(2, 2 + len(payload))))
    r = total % 11
    return 0 if r in (0, 1) else 11 - r


def mod11_mb(payload7):
    """DZS MB: weights 8..2 over the first 7 digits; remainder 0 or 1 -> 0 (same as MOD11INI for 7 digits)."""
    return mod11ini(payload7)


def jmb_valid_whole(code):
    """HUB 'MOD11JMB': weights 1..7 from the right, then 2..7 repeating; whole sum % 11 == 0; not all digits equal."""
    if len(set(code)) == 1:
        return False
    weights = []
    w = 1
    for _ in range(len(code)):
        weights.append(w)
        w += 1
        if w > 7:
            w = 2
    total = sum(int(c) * wt for c, wt in zip(reversed(code), weights))
    return total % 11 == 0


def jmb_checkdigit(payload):
    """Check digit that makes payload+K pass MOD11JMB (K has weight 1). None if impossible (needs 10)."""
    for k in range(10):
        if jmb_valid_whole(payload + str(k)):
            return k
    return None


def mod11p7(payload):
    """HUB 'MOD11P7' (models HR13, HR18): weights 2..7 from the right, cycling; r0 -> 5, r1 -> 0, else 11-r."""
    total = 0
    w = 2
    for c in reversed(payload):
        total += int(c) * w
        w = 2 if w == 7 else w + 1
    r = total % 11
    if r == 0:
        return 5
    if r == 1:
        return 0
    return 11 - r


def mod10zb(payload):
    """HUB 'MOD10ZB' (model HR14): weights 1,2,1,2... from the right (plain products); remainder mod 10 is K."""
    total = sum(int(c) * (1 if i % 2 == 0 else 2) for i, c in enumerate(reversed(payload)))
    return total % 10


def mod10_digitsum(payload):
    """HUB modulus 10 (model HR15 and HR40 K1): weights 2,1,2,1... from the right, add digit sums; K = (10 - r) % 10."""
    total = 0
    for i, c in enumerate(reversed(payload)):
        prod = int(c) * (2 if i % 2 == 0 else 1)
        total += prod // 10 + prod % 10
    return (10 - total % 10) % 10


def mod97_iban(iban):
    rearranged = iban[4:] + iban[:4]
    digits = "".join(str(int(ch, 36)) for ch in rearranged)
    return int(digits) % 97


def iban_check_digits(country, bban):
    tmp = bban + country + "00"
    digits = "".join(str(int(ch, 36)) for ch in tmp)
    return "%02d" % (98 - int(digits) % 97)


METHODS = {
    "iso7064": iso7064_mod11_10,
    "mod11ini": mod11ini,
    "mod11p7": mod11p7,
    "mod10zb": mod10zb,
    "mod10": mod10_digitsum,
    "jmb": jmb_checkdigit,
}

# ---------------------------------------------------------------------------
# Masking helpers
# ---------------------------------------------------------------------------


def mask(value, keep_start=2, keep_end=2):
    if len(value) <= keep_start + keep_end:
        return "*" * len(value)
    return value[:keep_start] + "*" * (len(value) - keep_start - keep_end) + value[-keep_end:]


def shown(value, args, **kw):
    return value if getattr(args, "show", False) else mask(value, **kw)


def digits_only(s):
    return re.sub(r"[\s\-./]", "", s or "")


# ---------------------------------------------------------------------------
# OIB / VAT
# ---------------------------------------------------------------------------


def oib_check(value):
    v = digits_only(value)
    if not re.fullmatch(r"\d{11}", v):
        return False, "OIB must be exactly 11 digits"
    if iso7064_mod11_10(v[:10]) != int(v[10]):
        return False, "check digit mismatch (ISO 7064 MOD 11,10)"
    return True, "ok"


def oib_generate(rng):
    body = "".join(str(rng.randrange(10)) for _ in range(10))
    return body + str(iso7064_mod11_10(body))


def vat_check(value):
    v = re.sub(r"\s", "", value or "").upper()
    if not v.startswith("HR"):
        return False, "Croatian PDV ID must start with 'HR' (Zakon o PDV-u cl. 77 st. 6)"
    ok, msg = oib_check(v[2:])
    return ok, msg


# ---------------------------------------------------------------------------
# IBAN / BIC
# ---------------------------------------------------------------------------

# Source: HNB "Vodeci brojevi pruzatelja platnih usluga", updated 27.3.2025
# https://www.hnb.hr/temeljne-funkcije/platni-promet/vodeci-brojevi-pruzatelja-platnih-usluga
# Snapshot only - banks merge and rename; VERIFY against the live HNB table.
BANKS = {
    "2500009": ("Addiko Bank d.d.", "HAABHR22"),
    "2481000": ("Agram banka d.d.", "KREZHR2X"),
    "4501006": ("Aircash d.o.o.", ""),
    "4133006": ("Banka Kovanica d.d.", "SKOVHR22"),
    "2488001": ("BKS Bank AG, Glavna podruznica Hrvatska", "BFKKHR22"),
    "2485003": ("Croatia banka d.d.", "CROAHR2X"),
    "2402006": ("Erste&Steiermaerkische Bank d.d.", "ESBCHR22"),
    "1001005": ("Hrvatska narodna banka", "NBHRHR2X"),
    "2390001": ("Hrvatska postanska banka d.d.", "HPBZHR2X"),
    "2492008": ("Imex banka d.d.", "IMXXHR22"),
    "2380006": ("Istarska kreditna banka Umag d.d.", "ISKBHR2X"),
    "2489004": ("J&T banka d.d.", "VBVZHR22"),
    "2400008": ("Karlovacka banka d.d.", "KALCHR2X"),
    "4124003": ("KentBank d.d.", "KENBHR22"),
    "2407000": ("OTP banka d.d.", "OTPVHR2X"),
    "2408002": ("Partner banka d.d.", "PAZGHR2X"),
    "2386002": ("Podravska banka d.d.", "PDKCHR2X"),
    "2340009": ("Privredna banka Zagreb d.d.", "PBZGHR2X"),
    "2484008": ("Raiffeisenbank Austria d.d.", "RZBHHR2X"),
    "2403009": ("Samoborska banka d.d.", "SMBRHR22"),
    "2412009": ("Slatinska banka d.d.", "SBSLHR2X"),
    "2360000": ("Zagrebacka banka d.d.", "ZABAHR2X"),
}

IBAN_LENGTHS = {"HR": 21}  # other countries: only the mod-97 check is applied


def iban_check(value):
    v = re.sub(r"\s", "", value or "").upper()
    info = {"iban": v}
    if not re.fullmatch(r"[A-Z]{2}\d{2}[A-Z0-9]{1,30}", v):
        return False, "not an IBAN shape (CC + 2 digits + BBAN)", info
    cc = v[:2]
    if cc in IBAN_LENGTHS and len(v) != IBAN_LENGTHS[cc]:
        return False, "%s IBAN must have %d characters" % (cc, IBAN_LENGTHS[cc]), info
    if mod97_iban(v) != 1:
        return False, "IBAN check digits wrong (ISO 13616 mod 97)", info
    if cc != "HR":
        return True, "ok (mod 97 only; country-specific rules not checked)", info
    if not v[4:].isdigit():
        return False, "HR BBAN must be 17 digits", info
    vbdi, acct = v[4:11], v[11:]
    info.update({"vbdi": vbdi, "account": acct})
    if iso7064_mod11_10(vbdi[:6]) != int(vbdi[6]):
        return False, "bank code (vodeci broj) check digit wrong (MOD 11,10; Odluka cl. 10)", info
    if iso7064_mod11_10(acct[:9]) != int(acct[9]):
        return False, "account number check digit wrong (MOD 11,10; Odluka cl. 11)", info
    bank = BANKS.get(vbdi)
    if bank:
        info.update({"bank": bank[0], "bic": bank[1]})
        return True, "ok", info
    return True, "ok (bank code not in the 2025 snapshot - check the HNB list)", info


def iban_generate(vbdi, rng):
    if not re.fullmatch(r"\d{7}", vbdi):
        raise ValueError("bank code must be 7 digits (VBDI)")
    if iso7064_mod11_10(vbdi[:6]) != int(vbdi[6]):
        raise ValueError("bank code %s fails its own MOD 11,10 check digit" % vbdi)
    body = "".join(str(rng.randrange(10)) for _ in range(9))
    acct = body + str(iso7064_mod11_10(body))
    bban = vbdi + acct
    return "HR" + iban_check_digits("HR", bban) + bban


def bic_check(value):
    v = re.sub(r"\s", "", value or "").upper()
    if not re.fullmatch(r"[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}([A-Z0-9]{3})?", v):
        return False, "BIC must be 8 or 11 chars: 4 letters bank + 2 letters country + 2 location (+3 branch)", None
    known = [name for (name, bic) in BANKS.values() if bic and bic == v[:8]]
    return True, "ok", (known[0] if known else None)


# ---------------------------------------------------------------------------
# MB / MBS / JMBG
# ---------------------------------------------------------------------------


def mb_check(value):
    v = digits_only(value)
    if not re.fullmatch(r"\d{8}", v):
        return False, "MB must be 8 digits (keep leading zeros)"
    if mod11_mb(v[:7]) != int(v[7]):
        return False, "check digit mismatch (MOD 11, weights 8..2)"
    return True, "ok"


def mb_generate(rng):
    body = "".join(str(rng.randrange(10)) for _ in range(7))
    return body + str(mod11_mb(body))


def mbs_check(value):
    v = digits_only(value)
    if not re.fullmatch(r"\d{9}", v):
        return False, "MBS must be 9 digits (keep leading zeros)"
    if iso7064_mod11_10(v[:8]) != int(v[8]):
        return False, "last digit does not match MOD 11,10 (rule inferred from public data - VERIFY)"
    return True, "ok (MOD 11,10 rule inferred from public data - VERIFY)"


def jmbg_check(value):
    v = digits_only(value)
    info = {}
    if not re.fullmatch(r"\d{13}", v):
        return False, "JMBG must be 13 digits", info
    dd, mm, yyy = int(v[0:2]), int(v[2:4]), int(v[4:7])
    year = 1000 + yyy if yyy >= 800 else 2000 + yyy
    try:
        born = date(year, mm, dd)
    except ValueError:
        return False, "digits 1-7 are not a valid date (DDMMYYY)", info
    region = v[7:9]
    serial = int(v[9:12])
    info = {
        "birth_date": born.isoformat(),
        "register": region,
        "register_note": "30-39 = registration areas in Croatia (Zakon o maticnom broju, NN 9/92, cl. 2)"
        if 30 <= int(region) <= 39 else "assigned outside Croatia's 30-39 range",
        "sex": "M" if serial < 500 else "F",
    }
    if not jmb_valid_whole(v):
        return False, "check digit mismatch (weights 7654327654321, sum % 11 must be 0)", info
    return True, "ok", info


# ---------------------------------------------------------------------------
# Poziv na broj (payment reference)
# Source: HUB "Jedinstveni pregled osnovnih modela poziva na broj", primjena od sijecnja 2026.
# Part spec: (check, length) where check is one of
#   None, 'ini', 'iso', 'oib' (11 digits ISO), 'jmb', 'p7', 'zb', 'm10',
#   'ini_or_oib' (<=10 digits MOD11INI, 11 digits ISO), 'oib_if11' (ISO only if 11 digits),
#   'hr65p3' (<=5 or 11 digits ISO, 6-10 MOD11INI)
# length: int (exact), (min,max) tuple, or a set of allowed exact lengths
# ---------------------------------------------------------------------------

V12 = (1, 12)

MODELS = {
    "HR00": {"parts": [(None, V12)] * 3},
    "HR01": {"parts": [(None, V12)] * 3, "whole": "ini"},
    "HR02": {"parts": [(None, V12), ("ini", V12), ("ini", V12)]},
    "HR03": {"parts": [("ini", V12)] * 3},
    "HR04": {"parts": [("ini", V12), (None, V12), ("ini", V12)]},
    "HR05": {"parts": [("ini", V12), (None, V12), (None, V12)],
             "note": "P2 is under control (11-digit OIB) only for certain budget accounts when P1 is a city/municipality code - not checked here"},
    "HR06": {"parts": [(None, V12)] * 3, "combine": (1, 2)},
    "HR07": {"parts": [(None, V12), ("ini", V12), (None, V12)]},
    "HR08": {"parts": [(None, V12), (None, V12), ("ini", V12)], "combine": (0, 1)},
    "HR09": {"parts": [(None, V12)] * 3, "combine": (0, 1)},
    "HR10": {"parts": [("ini", V12), (None, V12), (None, V12)], "combine": (1, 2)},
    "HR11": {"parts": [("ini", V12), ("ini", V12), (None, V12)]},
    "HR12": {"parts": [("jmb", 13), (None, V12), (None, V12)]},
    "HR13": {"parts": [("p7", 10), (None, V12), (None, V12)]},
    "HR14": {"parts": [("zb", 10), (None, V12), (None, V12)]},
    "HR15": {"parts": [("m10", 8), ("m10", 11)], "max": 2},
    "HR16": {"parts": [("ini", 5), ("ini", 4), (None, 8)], "min": 3},
    "HR17": {"parts": [("iso", V12), (None, V12), (None, V12)]},
    "HR18": {"parts": [("p7", V12), (None, V12), (None, V12)]},
    "HR19": {"parts": [("ini", (1, 10)), ("oib", 11)], "min": 2, "max": 2},
    "HR23": {"parts": [("ini", 4), (None, V12), (None, V12), (None, V12)], "p1_first": "6",
             "note": "P2+P3+P4 together at most 15 digits"},
    "HR24": {"parts": [("ini", 4), (None, (1, 13)), (None, V12), (None, V12)]},
    "HR25": {"parts": [(None, 3), (None, 7)], "min": 2, "max": 2, "note": "FINA only"},
    "HR26": {"parts": [("ini", 4), ("ini_or_oib", (1, 11)), ("ini_or_oib", (1, 11)), (None, (1, 11))], "min": 3},
    "HR27": {"parts": [("ini", 4), ("ini", V12)], "min": 2, "max": 2},
    "HR28": {"parts": [("ini", 4), ("ini", 3), ("ini", 6), (None, (1, 6))], "min": 3},
    "HR29": {"parts": [("ini", 4), ("ini", V12), ("ini", V12)], "min": 3},
    "HR30": {"parts": [(None, 10), (None, 4), (None, (1, 6))], "min": 3},
    "HR31": {"parts": [("iso", (1, 6)), (None, V12), (None, V12), (None, V12)]},
    "HR33": {"parts": [("iso", (1, 6)), ("iso", (1, 7)), (None, (1, 7))], "min": 3},
    "HR34": {"parts": [("iso", (1, 6)), ("iso", (1, 7)), ("iso", (1, 5))], "min": 3},
    "HR35": {"parts": [("ini", (1, 10)), ("oib", 11)], "min": 2, "max": 2},
    "HR40": {"parts": [(None, 11), (None, V12), (None, V12)], "unsupported_check": True,
             "note": "P1 has two check digits (mod 10 + mod 11); exact digit ranges ambiguous in the HUB text - only format checked"},
    "HR41": {"parts": [("jmb", 13), ("ini", V12), (None, V12)]},
    "HR42": {"parts": [(None, V12)] * 3, "whole": "jmb"},
    "HR43": {"parts": [(None, 3), ("ini", 8), (None, 5), (None, 3)], "min": 4},
    "HR50": {"parts": [(None, 5), (None, 12), (None, 1)], "unsupported_check": True,
             "note": "PBZ-internal special algorithm - only format checked"},
    "HR55": {"parts": [("ini", V12), (None, V12), (None, V12)]},
    "HR62": {"parts": [("ini", 4), ("iso", (1, 5)), ("ini", (1, 6)), (None, (1, 11))], "min": 3},
    "HR63": {"parts": [("ini", 4), ("iso", (1, 5)), ("ini", V12)], "min": 3},
    "HR64": {"parts": [("ini", 4), ("iso", (1, 5)), ("oib_if11", V12), (None, V12)], "min": 3},
    "HR65": {"parts": [("ini", 4), ("ini", 3), ("hr65p3", (1, 11)), (None, (1, 10))], "min": 3},
    "HR66": {"parts": [("ini", 4), ("ini", 3), ("iso", {1, 2, 3, 4, 5, 7}), ("ini", (3, 7))], "min": 4},
    "HR67": {"parts": [("oib", 11), (None, (1, 10)), (None, (1, 8))]},
    "HR68": {"parts": [("ini", 4), ("oib", 11), (None, (1, 5))], "min": 2},
    "HR69": {"parts": [("iso", 5), ("oib", 11), (None, 3)], "min": 2},
    "HR83": {"parts": [("ini", 4), (None, {5, 7, 16}), (None, 6)], "min": 2, "note": "FINA only"},
    "HR84": {"parts": [("ini", 4), (None, {4, 8}), (None, 10)], "min": 2, "note": "FINA only"},
    "HR99": {"parts": [], "max": 0},
}

FOUR_PART = {"HR23", "HR24", "HR26", "HR28", "HR31", "HR43", "HR62", "HR64", "HR65", "HR66"}


def _len_ok(n, spec):
    if isinstance(spec, int):
        return n == spec
    if isinstance(spec, tuple):
        return spec[0] <= n <= spec[1]
    return n in spec


def _check_part(part, kind):
    """Return None if fine, else an error string."""
    if kind is None:
        return None
    body, k = part[:-1], int(part[-1])
    if kind == "ini":
        return None if mod11ini(body) == k else "MOD11INI check digit should be %d" % mod11ini(body)
    if kind == "iso":
        return None if iso7064_mod11_10(body) == k else "ISO 7064 MOD 11,10 check digit should be %d" % iso7064_mod11_10(body)
    if kind == "oib":
        ok, msg = oib_check(part)
        return None if ok else "OIB: " + msg
    if kind == "jmb":
        return None if jmb_valid_whole(part) else "MOD11JMB check fails"
    if kind == "p7":
        if part[0] != "3":
            return "MOD11P7: first digit must be 3"
        return None if mod11p7(body) == k else "MOD11P7 check digit should be %d" % mod11p7(body)
    if kind == "zb":
        return None if mod10zb(body) == k else "MOD10ZB check digit should be %d" % mod10zb(body)
    if kind == "m10":
        return None if mod10_digitsum(body) == k else "MOD 10 check digit should be %d" % mod10_digitsum(body)
    if kind == "ini_or_oib":
        return _check_part(part, "oib" if len(part) == 11 else "ini")
    if kind == "oib_if11":
        return _check_part(part, "oib") if len(part) == 11 else None
    if kind == "hr65p3":
        return _check_part(part, "iso" if len(part) <= 5 or len(part) == 11 else "ini")
    return "unknown check kind %s" % kind


def rf_check(value):
    v = re.sub(r"\s", "", value or "").upper()
    if not re.fullmatch(r"RF\d{2}[A-Z0-9]{1,21}", v):
        return False, "RF reference: 'RF' + 2 check digits + 1-21 alphanumerics (ISO 11649)"
    if mod97_iban(v) != 1:
        return False, "RF check digits wrong (mod 97)"
    return True, "ok"


def reference_check(model, value):
    """Validate model + poziv na broj. Returns (ok, list_of_messages)."""
    model = (model or "").upper().replace(" ", "")
    if model.startswith("RF") or (value or "").upper().startswith("RF"):
        ok, msg = rf_check(value if (value or "").upper().startswith("RF") else model + (value or ""))
        return ok, [msg]
    if re.fullmatch(r"\d{2}", model):
        model = "HR" + model
    if model not in MODELS:
        return False, ["unknown or unsupported model %s (known: %s)" % (model, ", ".join(sorted(MODELS)))]
    spec = MODELS[model]
    raw = (value or "").strip()
    msgs = []
    if spec.get("note"):
        msgs.append("note: " + spec["note"])
    if model == "HR99":
        return (raw == "", msgs + (["HR99 means 'no reference' - the reference field must be empty"] if raw else ["ok"]))
    if raw == "":
        return False, msgs + ["empty reference - use model HR99 when there is no reference"]
    if len(raw.replace(" ", "")) > 22:
        return False, msgs + ["reference longer than 22 characters (digits + hyphens)"]
    if not re.fullmatch(r"[0-9\- ]+", raw):
        return False, msgs + ["HR models allow digits and hyphens only"]
    parts = [p for p in re.split(r"\s*-\s*", raw.replace(" ", "-")) if p != ""]
    if "--" in raw.replace(" ", "") or raw.replace(" ", "").startswith("-") or raw.replace(" ", "").endswith("-"):
        return False, msgs + ["empty part (leading/trailing/double hyphen)"]
    max_parts = spec.get("max", 4 if model in FOUR_PART else 3)
    min_parts = spec.get("min", 1)
    if not (min_parts <= len(parts) <= max_parts):
        return False, msgs + ["%s needs %d-%d parts, got %d" % (model, min_parts, max_parts, len(parts))]
    total_digits = sum(len(p) for p in parts)
    limit = {1: 22, 2: 21, 3: 20, 4: 19}[len(parts)]
    if total_digits > limit:
        return False, msgs + ["too many digits for %d parts (max %d)" % (len(parts), limit)]
    errors = []
    for i, part in enumerate(parts):
        kind, length = spec["parts"][i]
        if not _len_ok(len(part), length):
            errors.append("P%d length %d not allowed (%s)" % (i + 1, len(part), length))
    if model == "HR23":
        if parts[0][0] != "6":
            errors.append("P1 must start with 6")
        if sum(len(p) for p in parts[1:]) > 15:
            errors.append("P2+P3+P4 may have at most 15 digits")
    if errors:
        return False, msgs + errors
    if spec.get("unsupported_check"):
        return True, msgs + ["format ok; check digits NOT verified for %s" % model]
    if "whole" in spec:
        whole = "".join(parts)
        if spec["whole"] == "ini":
            err = None if mod11ini(whole[:-1]) == int(whole[-1]) else "MOD11INI over the whole reference should end in %d" % mod11ini(whole[:-1])
        else:
            err = None if jmb_valid_whole(whole) else "MOD11JMB over the whole reference fails"
        return (err is None), msgs + [err or "ok"]
    combine = spec.get("combine")
    checked = set()
    if combine and len(parts) > combine[1]:
        a, b = combine
        joined = parts[a] + parts[b]
        if mod11ini(joined[:-1]) != int(joined[-1]):
            errors.append("P%d+P%d joint MOD11INI check digit should be %d" % (a + 1, b + 1, mod11ini(joined[:-1])))
        checked.update({a, b})
    elif combine and len(parts) == combine[1]:
        # fewer parts than the joint pair: the single part present (index a) is checked on its own
        a = combine[0]
        if mod11ini(parts[a][:-1]) != int(parts[a][-1]):
            errors.append("P%d MOD11INI check digit should be %d" % (a + 1, mod11ini(parts[a][:-1])))
        checked.add(a)
    for i, part in enumerate(parts):
        if i in checked:
            continue
        err = _check_part(part, spec["parts"][i][0])
        if err:
            errors.append("P%d: %s" % (i + 1, err))
    return (not errors), msgs + (errors or ["ok"])


# ---------------------------------------------------------------------------
# Phone numbers (HAKOM Plan numeriranja, NN 45/2023, Tablica 1)
# NDC -> (min NSN len, max NSN len, type, description). NSN length includes the NDC.
# ---------------------------------------------------------------------------

GEO = {
    "1": "Grad Zagreb i Zagrebacka zupanija", "20": "Dubrovacko-neretvanska", "21": "Splitsko-dalmatinska",
    "22": "Sibensko-kninska", "23": "Zadarska", "31": "Osjecko-baranjska", "32": "Vukovarsko-srijemska",
    "33": "Viroviticko-podravska", "34": "Pozesko-slavonska", "35": "Brodsko-posavska", "40": "Medimurska",
    "42": "Varazdinska", "43": "Bjelovarsko-bilogorska", "44": "Sisacko-moslavacka", "47": "Karlovacka",
    "48": "Koprivnicko-krizevacka", "49": "Krapinsko-zagorska", "51": "Primorsko-goranska", "52": "Istarska",
    "53": "Licko-senjska",
}
NDC = {}
for _k, _v in GEO.items():
    NDC[_k] = (8, 8, "geographic", _v) if _k == "1" else (8, 9, "geographic", _v + " zupanija")
NDC.update({
    "60": (6, 8, "premium-rate", "general content services"),
    "609": (6, 8, "premium-rate", "humanitarian / donations"),
    "61": (6, 8, "premium-rate", "voting / televoting"),
    "64": (8, 8, "premium-rate", "content unsuitable for children"),
    "65": (8, 8, "premium-rate", "prize games"),
    "69": (8, 8, "premium-rate", "services for children"),
    "72": (8, 8, "non-geographic", "uniform access number"),
    "74": (8, 8, "non-geographic", "personal number"),
    "75": (8, 8, "non-geographic", "personal number"),
    "800": (7, 9, "freephone", "free call"),
    "801": (7, 9, "freephone", "free call"),
    "98": (8, 9, "mobile", "mobile network"),
    "99": (9, 9, "mobile", "mobile network"),
})
for _m in ("90", "91", "92", "93", "94", "95", "96", "97"):
    NDC[_m] = (9, 9, "mobile", "mobile network")
for _m in ("890", "891", "892", "893", "894", "895", "896", "897"):
    NDC.setdefault(_m, (10, 10, "m2m", "machine-to-machine"))
SHORT = {"112": "EU emergency number", "192": "police", "193": "fire brigade", "194": "ambulance",
         "195": "sea search and rescue", "1987": "road assistance"}


def phone_normalize(raw):
    s = (raw or "").strip()
    s = s.replace("(0)", "")
    s = re.sub(r"[\s\-./()]", "", s)
    if s in SHORT:
        return {"input": raw, "valid": True, "type": "short code", "description": SHORT[s], "e164": None}
    if s.startswith("+"):
        s = s[1:]
        if not s.startswith("385"):
            return {"input": raw, "valid": None, "type": "foreign", "e164": "+" + s,
                    "description": "not a Croatian number (+385); not validated"}
        nsn = s[3:]
    elif s.startswith("00385"):
        nsn = s[5:]
    elif s.startswith("00"):
        return {"input": raw, "valid": None, "type": "foreign", "e164": "+" + s[2:],
                "description": "not a Croatian number; not validated"}
    elif s.startswith("385") and len(s) >= 9:
        nsn = s[3:]
    elif s.startswith("0"):
        nsn = s[1:]
    else:
        return {"input": raw, "valid": False, "description": "add the national prefix 0 or +385"}
    nsn = nsn.lstrip("0") if nsn.startswith("0") else nsn
    if not nsn.isdigit():
        return {"input": raw, "valid": False, "description": "non-digit characters"}
    for length in (3, 2, 1):
        ndc = nsn[:length]
        if ndc in NDC:
            lo, hi, typ, desc = NDC[ndc]
            ok = lo <= len(nsn) <= hi
            return {"input": raw, "valid": ok, "type": typ, "ndc": ndc, "description": desc,
                    "e164": "+385" + nsn if ok else None,
                    "national": "0" + nsn,
                    **({} if ok else {"error": "NSN length %d, allowed %d-%d" % (len(nsn), lo, hi)})}
    return {"input": raw, "valid": False, "description": "no matching NDC in the HAKOM numbering plan"}


# ---------------------------------------------------------------------------
# Postal codes and plates
# ---------------------------------------------------------------------------

POST_REGION = {  # first two digits -> region (approximate; mirrors the old area codes) - VERIFY
    "10": "Zagreb (city and county)", "20": "Dubrovnik-Neretva", "21": "Split-Dalmatia", "22": "Sibenik-Knin",
    "23": "Zadar", "31": "Osijek-Baranja", "32": "Vukovar-Srijem", "33": "Virovitica-Podravina",
    "34": "Pozega-Slavonia", "35": "Brod-Posavina", "40": "Medimurje", "42": "Varazdin",
    "43": "Bjelovar-Bilogora", "44": "Sisak-Moslavina", "47": "Karlovac", "48": "Koprivnica-Krizevci",
    "49": "Krapina-Zagorje", "51": "Primorje-Gorski kotar", "52": "Istria", "53": "Lika-Senj",
}


def postcode_check(value):
    v = (value or "").strip()
    if v.upper().startswith("HR-"):
        v = v[3:]
    if not re.fullmatch(r"\d{5}", v):
        return False, "Croatian postal codes are 5 digits", None
    return True, "shape ok - confirm the code exists in the Hrvatska posta list", POST_REGION.get(v[:2])


PLATE_AREAS = ["BJ", "BM", "ČK", "DA", "DE", "DJ", "DU", "GS", "IM", "KA", "KC", "KR", "KT", "KŽ", "MA", "NA",
               "NG", "OG", "OS", "PU", "PŽ", "RI", "SB", "SK", "SL", "ST", "ŠI", "VK", "VT", "VU", "VŽ", "ZD",
               "ZG", "ŽU"]
PLATE_RE = re.compile(r"^(%s)[\s\-]*(\d{3,4})[\s\-]*([A-ZČĆĐŠŽ]{1,2})$" % "|".join(PLATE_AREAS))


def plate_check(value):
    v = (value or "").strip().upper()
    m = PLATE_RE.match(v)
    if not m:
        return False, "not a standard plate (area code + 3-4 digits + 1-2 letters)", None
    return True, "ok", "%s %s-%s" % m.groups()


# ---------------------------------------------------------------------------
# Self-test (fictitious vectors only, plus algorithm examples from the HUB document)
# ---------------------------------------------------------------------------


def self_test():
    failures = []

    def expect(name, got, want):
        if got != want:
            failures.append("%s: got %r, want %r" % (name, got, want))

    # ISO 7064 MOD 11,10 example from the HUB document (234000 -> 9)
    expect("iso7064 HUB example", iso7064_mod11_10("234000"), 9)
    # MOD11INI examples from the HUB document
    expect("mod11ini HUB 33444555666", mod11ini("33444555666"), 9)
    expect("mod11ini HUB 10230578901", mod11ini("10230578901"), 6)
    expect("mod11p7 HUB 345678901", mod11p7("345678901"), 2)
    expect("mod10zb HUB 223344556", mod10zb("223344556"), 8)
    expect("mod10 HUB 54370395", mod10_digitsum("54370395"), 3)
    # OIB
    expect("oib fictitious valid", oib_check("12345678903")[0], True)
    expect("oib bad check", oib_check("12345678901")[0], False)
    expect("oib short", oib_check("1234567890")[0], False)
    expect("oib letters", oib_check("1234567890A")[0], False)
    rng = random.Random(42)
    for _ in range(200):
        expect("oib generate", oib_check(oib_generate(rng))[0], True)
    expect("vat ok", vat_check("HR12345678903")[0], True)
    expect("vat no prefix", vat_check("12345678903")[0], False)
    # IBAN
    gen = iban_generate("2340009", random.Random(1))
    expect("iban generated valid", iban_check(gen)[0], True)
    expect("iban generated bank", iban_check(gen)[2].get("bank"), "Privredna banka Zagreb d.d.")
    expect("iban public budget account", iban_check("HR12 1001 0051 8630 0016 0")[0], True)
    expect("iban wrong mod97", iban_check("HR1310010051863000160")[0], False)
    expect("iban wrong length", iban_check("HR121001005186300016")[0], False)
    bad_acct = "2340009" + "123456789" + str((iso7064_mod11_10("123456789") + 1) % 10)
    expect("iban bad internal account digit", iban_check("HR" + iban_check_digits("HR", bad_acct) + bad_acct)[0], False)
    expect("iban foreign (DE example from ISO 13616)", iban_check("DE89370400440532013000")[0], True)
    try:
        iban_generate("2340001", random.Random(1))
        failures.append("iban generate should reject bad VBDI")
    except ValueError:
        pass
    # BIC
    expect("bic ok", bic_check("ZABA HR 2X")[0], True)
    expect("bic known", bic_check("ZABAHR2X")[2], "Zagrebacka banka d.d.")
    expect("bic bad", bic_check("ZAB1HR2X")[0], False)
    # MB / MBS
    mbv = mb_generate(random.Random(7))
    expect("mb generated", mb_check(mbv)[0], True)
    expect("mb fictitious 01234560", mb_check("0123456" + str(mod11_mb("0123456")))[0], True)
    expect("mb bad", mb_check("0123456" + str((mod11_mb("0123456") + 1) % 10))[0], False)
    expect("mbs fictitious", mbs_check("01234567" + str(iso7064_mod11_10("01234567")))[0], True)
    # JMBG (fictitious: 01.01.1990, register 33, serial 123)
    payload = "010199033012"
    k = jmb_checkdigit(payload)
    expect("jmbg checkdigit exists", k is not None, True)
    ok, _, info = jmbg_check(payload + str(k))
    expect("jmbg valid", ok, True)
    expect("jmbg birth", info.get("birth_date"), "1990-01-01")
    expect("jmbg sex", info.get("sex"), "M")
    expect("jmbg bad date", jmbg_check("3102990330123")[0], False)
    expect("jmbg bad check", jmbg_check(payload + str((k + 1) % 10))[0], False)
    # References (examples from the HUB document, section 3)
    for model, ref, want in [
        ("HR01", "102-3057-89016", True), ("HR01", "10230578-9016", True), ("HR01", "10-230578901-6", True),
        ("HR01", "102-3057-89017", False),
        ("HR02", "1023-5789010", True), ("HR02", "1023-5789-9016", True),
        ("HR06", "102-3057-89015", True), ("HR06", "102-30578901-5", True), ("HR06", "102305-789011", True),
        ("HR06", "102-305789015", True),
        ("HR00", "123-456", True), ("HR00", "1234567890123", False),
        ("HR99", "", True), ("HR99", "123", False), ("HR01", "", False),
        ("HR68", "1651-12345678903", True), ("HR68", "1651-12345678901", False),
        ("HR68", "8168-12345678903-26001", True), ("HR68", "1650-12345678903", False),
        ("HR68", "1651", False),
        ("HR69", "40002-12345678903-100", True),
        ("HR67", "12345678903-1-2", True),
        ("HR13", "3456789012", True), ("HR13", "4456789012", False),
        ("HR14", "2233445568", True),
        ("HR15", "5437039%d-1234567890%d" % (mod10_digitsum("5437039"), mod10_digitsum("1234567890")), True),
        ("HR01", "1234567890123456789012", False),
        ("HR01", "7269-52601815906-00019", False),  # same shape as the HUB barcode spec example (fictitious OIB); fails HR01
        ("HR05", "abc", False),
    ]:
        expect("reference %s %s" % (model, ref), reference_check(model, ref)[0], want)
    expect("rf valid", reference_check("RF", "RF18539007547034")[0], True)
    expect("rf invalid", reference_check("RF", "RF19539007547034")[0], False)
    # Phones
    expect("phone mobile", phone_normalize("091 234 5678")["e164"], "+385912345678")
    expect("phone zagreb", phone_normalize("01/2345-678")["e164"], "+38512345678")
    expect("phone intl", phone_normalize("+385 (0)21 123 456")["e164"], "+38521123456")
    expect("phone 00385", phone_normalize("00385 98 123 456")["e164"], "+38598123456")
    expect("phone freephone", phone_normalize("0800 1234")["type"], "freephone")
    expect("phone premium", phone_normalize("060 123 456")["type"], "premium-rate")
    expect("phone short", phone_normalize("112")["type"], "short code")
    expect("phone too short mobile", phone_normalize("091 234 567")["valid"], False)
    expect("phone no prefix", phone_normalize("912345678")["valid"], False)
    # Postcode / plate
    expect("postcode", postcode_check("10000")[2], "Zagreb (city and county)")
    expect("postcode bad", postcode_check("1000")[0], False)
    expect("plate", plate_check("ZG 1234-AB")[2], "ZG 1234-AB")
    expect("plate diacritic", plate_check("ČK 123-A")[0], True)
    expect("plate bad area", plate_check("XX 1234-AB")[0], False)

    if failures:
        print("SELF-TEST FAILED (%d):" % len(failures))
        for f in failures:
            print("  - " + f)
        return 1
    print("self-test passed (hr_ids.py): all vectors OK")
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def emit(obj, as_json):
    if as_json:
        print(json.dumps(obj, ensure_ascii=False))
    else:
        print("  ".join("%s=%s" % (k, v) for k, v in obj.items() if v not in (None, "")))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog="Run with --self-test to verify the algorithms.")
    ap.add_argument("--self-test", action="store_true", help="run built-in test vectors and exit")
    ap.add_argument("--json", action="store_true", help="JSON output")
    sub = ap.add_subparsers(dest="cmd")

    def gen_args(p):
        p.add_argument("--count", type=int, default=1)
        p.add_argument("--seed", type=int, help="seed for reproducible test data")
        p.add_argument("--quiet", action="store_true", help="omit the FICTITIOUS header line")

    p = sub.add_parser("oib", help="OIB")
    s = p.add_subparsers(dest="action", required=True)
    v = s.add_parser("validate"); v.add_argument("value"); v.add_argument("--show", action="store_true")
    gen_args(s.add_parser("generate"))

    p = sub.add_parser("vat", help="PDV ID (HR + OIB)")
    s = p.add_subparsers(dest="action", required=True)
    v = s.add_parser("validate"); v.add_argument("value"); v.add_argument("--show", action="store_true")

    p = sub.add_parser("iban", help="IBAN")
    s = p.add_subparsers(dest="action", required=True)
    v = s.add_parser("validate"); v.add_argument("value")
    g = s.add_parser("generate"); g.add_argument("--bank", required=True, help="7-digit VBDI, e.g. 2340009"); gen_args(g)

    p = sub.add_parser("bic", help="BIC/SWIFT")
    s = p.add_subparsers(dest="action", required=True)
    v = s.add_parser("validate"); v.add_argument("value")

    p = sub.add_parser("mb", help="DZS maticni broj (8 digits)")
    s = p.add_subparsers(dest="action", required=True)
    v = s.add_parser("validate"); v.add_argument("value")
    gen_args(s.add_parser("generate"))

    p = sub.add_parser("mbs", help="Sudski registar MBS (9 digits)")
    s = p.add_subparsers(dest="action", required=True)
    v = s.add_parser("validate"); v.add_argument("value")

    p = sub.add_parser("jmbg", help="legacy JMBG/MBG (13 digits)")
    s = p.add_subparsers(dest="action", required=True)
    v = s.add_parser("validate"); v.add_argument("value"); v.add_argument("--show", action="store_true")

    p = sub.add_parser("reference", help="poziv na broj (HR00-HR99, RF)")
    s = p.add_subparsers(dest="action", required=True)
    v = s.add_parser("validate"); v.add_argument("--model", required=True); v.add_argument("--value", default="")
    c = s.add_parser("checkdigit"); c.add_argument("--method", required=True, choices=sorted(METHODS))
    c.add_argument("--value", required=True, help="digits WITHOUT the check digit")

    p = sub.add_parser("phone", help="phone numbers")
    s = p.add_subparsers(dest="action", required=True)
    v = s.add_parser("normalize"); v.add_argument("value")

    p = sub.add_parser("postcode", help="postal code")
    s = p.add_subparsers(dest="action", required=True)
    v = s.add_parser("check"); v.add_argument("value")

    p = sub.add_parser("plate", help="vehicle registration plate")
    s = p.add_subparsers(dest="action", required=True)
    v = s.add_parser("check"); v.add_argument("value")

    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.cmd:
        ap.print_help()
        return 2
    J = args.json

    def gen(fn):
        rng = random.Random(args.seed) if args.seed is not None else random.SystemRandom()
        if not args.quiet:
            print(FICTITIOUS)
        for _ in range(max(1, args.count)):
            print(fn(rng))
        return 0

    if args.cmd == "oib":
        if args.action == "generate":
            return gen(oib_generate)
        ok, msg = oib_check(args.value)
        emit({"type": "OIB", "value": shown(digits_only(args.value), args), "valid": ok, "detail": msg}, J)
        return 0 if ok else 1
    if args.cmd == "vat":
        ok, msg = vat_check(args.value)
        v_ = re.sub(r"\s", "", args.value).upper()
        emit({"type": "PDV ID", "value": shown(v_, args, keep_start=4), "valid": ok, "detail": msg,
              "next": "format only - confirm registration online via VIES (see references)" if ok else ""}, J)
        return 0 if ok else 1
    if args.cmd == "iban":
        if args.action == "generate":
            try:
                return gen(lambda r: iban_generate(args.bank, r))
            except ValueError as e:
                print("error: %s" % e, file=sys.stderr)
                return 2
        ok, msg, info = iban_check(args.value)
        emit(dict({"type": "IBAN", "valid": ok, "detail": msg}, **info), J)
        return 0 if ok else 1
    if args.cmd == "bic":
        ok, msg, bank = bic_check(args.value)
        emit({"type": "BIC", "valid": ok, "detail": msg, "bank": bank}, J)
        return 0 if ok else 1
    if args.cmd == "mb":
        if args.action == "generate":
            return gen(mb_generate)
        ok, msg = mb_check(args.value)
        emit({"type": "MB", "value": digits_only(args.value), "valid": ok, "detail": msg}, J)
        return 0 if ok else 1
    if args.cmd == "mbs":
        ok, msg = mbs_check(args.value)
        emit({"type": "MBS", "value": digits_only(args.value), "valid": ok, "detail": msg}, J)
        return 0 if ok else 1
    if args.cmd == "jmbg":
        ok, msg, info = jmbg_check(args.value)
        if not args.show:  # birth date and sex are personal data too
            info = {k: v for k, v in info.items() if k not in ("birth_date", "sex")}
        emit(dict({"type": "JMBG", "value": shown(digits_only(args.value), args), "valid": ok, "detail": msg},
                  **info), J)
        return 0 if ok else 1
    if args.cmd == "reference":
        if args.action == "checkdigit":
            if not args.value.isdigit():
                print("error: digits only", file=sys.stderr)
                return 2
            k = METHODS[args.method](args.value)
            emit({"method": args.method, "payload": args.value, "check_digit": k,
                  "full": None if k is None else args.value + str(k)}, J)
            return 0 if k is not None else 1
        ok, msgs = reference_check(args.model, args.value)
        emit({"type": "poziv na broj", "model": args.model.upper(), "value": args.value, "valid": ok,
              "detail": "; ".join(msgs)}, J)
        return 0 if ok else 1
    if args.cmd == "phone":
        res = phone_normalize(args.value)
        emit(res, J)
        return 0 if res.get("valid") else 1
    if args.cmd == "postcode":
        ok, msg, region = postcode_check(args.value)
        emit({"type": "postcode", "valid": ok, "detail": msg, "region_approx": region}, J)
        return 0 if ok else 1
    if args.cmd == "plate":
        ok, msg, norm = plate_check(args.value)
        emit({"type": "plate", "valid": ok, "detail": msg, "normalized": norm}, J)
        return 0 if ok else 1
    return 2


if __name__ == "__main__":
    sys.exit(main())
