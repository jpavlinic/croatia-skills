#!/usr/bin/env python3
"""ZKI (zastitni kod izdavatelja) helper for Croatian B2C fiscalization (Fiskalizacija 1.0).

Implements the algorithm from "Fiskalizacija racuna u krajnjoj potrosnji -
Tehnicka specifikacija za korisnike", v2.7 (21.07.2026), chapter 12:

    ZKI = MD5_hex( RSA_sign( OIB + datVrij + BrOznRac + OznPosPr + OznNapUr + IznosUkupno ) )

    datVrij      issue date/time as 'dd.MM.yyyy HH:mm:ss'  (SPACE, not the 'T' used in the XML)
    IznosUkupno  total with '.' as decimal separator, e.g. 1245.56 / -105.50
    RSA_sign     PKCS#1 v1.5 signature with the fiscal certificate's private key.
                 Spec v2.7 pseudocode: RSA-SHA256 (SHA1 was used by earlier versions and by
                 Pravilnik NN 153/2025 art. 16; production rejects RSA-SHA1 *message*
                 signatures from 1.1.2027).
    MD5_hex      32 lower-case hex characters, printed on the receipt.

The Python standard library cannot do RSA signing, so this script:
  * builds and validates the exact input string (``build``),
  * turns a raw signature file into the ZKI (``from-signature``),
  * optionally calls the ``openssl`` CLI for you (``sign``), and
  * prints the equivalent openssl commands (``commands``).

Standard library only. No network access. Developer aid, not legal or tax advice.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

SPEC = "Tehnicka specifikacija za korisnike fiskalizacije racuna u krajnjoj potrosnji v2.7 (21.07.2026), ch. 12"
NOTICE = ("TEMPLATE - not legal advice. Developer aid only: verify against the current "
          "Tehnicka specifikacija (porezna-uprava.gov.hr) and test on cistest before production.")

_RE_OPP = re.compile(r"^[0-9A-Za-z]{1,20}$")
_RE_NUM = re.compile(r"^[1-9][0-9]{0,19}$")


def oib_is_valid(oib: str) -> bool:
    """ISO 7064 MOD 11,10 check used by the Croatian OIB."""
    if not re.fullmatch(r"\d{11}", oib or ""):
        return False
    acc = 10
    for ch in oib[:10]:
        acc = (acc + int(ch)) % 10 or 10
        acc = (acc * 2) % 11
    return (11 - acc) % 10 == int(oib[10])


def format_datetime(value) -> str:
    """Return 'dd.MM.yyyy HH:mm:ss'. Accepts datetime, 'dd.mm.yyyy HH:MM:SS',
    'dd.mm.yyyyTHH:MM:SS' (XML form) or ISO 'yyyy-mm-ddTHH:MM:SS'."""
    if isinstance(value, _dt.datetime):
        return value.strftime("%d.%m.%Y %H:%M:%S")
    s = str(value).strip()
    for fmt in ("%d.%m.%Y %H:%M:%S", "%d.%m.%YT%H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return _dt.datetime.strptime(s, fmt).strftime("%d.%m.%Y %H:%M:%S")
        except ValueError:
            continue
    raise ValueError(f"unrecognised date/time {value!r}; use dd.mm.yyyy HH:MM:SS")


def format_amount(value) -> str:
    """Two decimals, '.' separator, optional leading '-'; same string as IznosUkupno."""
    try:
        d = Decimal(str(value).replace(",", "."))
    except InvalidOperation as exc:
        raise ValueError(f"invalid amount {value!r}") from exc
    return str(d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def build_input(oib, issued_at, broj, opp, onu, total, check_oib: bool = True) -> str:
    """Concatenate the ZKI input string exactly as chapter 12 describes."""
    oib = str(oib).strip()
    if check_oib and not oib_is_valid(oib):
        raise ValueError(f"OIB {oib!r} fails the ISO 7064 MOD 11,10 check")
    if not re.fullmatch(r"\d{11}", oib):
        raise ValueError("OIB must be 11 digits")
    broj, opp, onu = str(broj).strip(), str(opp).strip(), str(onu).strip()
    if not _RE_NUM.match(broj):
        raise ValueError("BrOznRac: digits only, no leading zeros, not 0, max 20 chars")
    if not _RE_OPP.match(opp):
        raise ValueError("OznPosPr: 1-20 characters, only 0-9 a-z A-Z")
    if not _RE_NUM.match(onu):
        raise ValueError("OznNapUr: digits only, no leading zeros, max 20 chars")
    return oib + format_datetime(issued_at) + broj + opp + onu + format_amount(total)


def zki_from_signature(signature: bytes) -> str:
    """MD5 (RFC 1321) of the raw RSA signature bytes, lower-case hex."""
    if not signature:
        raise ValueError("empty signature")
    return hashlib.md5(signature).hexdigest()


def openssl_commands(input_string: str, key: str = "fiskal-key.pem", digest: str = "sha256") -> str:
    q = input_string.replace("'", "'\\''")
    return "\n".join([
        "# 1) one-time: extract the private key from the FINA/QTSP .p12 (never commit either file)",
        "openssl pkcs12 -in fiskal.p12 -nocerts -nodes -out fiskal-key.pem   # OpenSSL 3+: add -legacy if it fails",
        "chmod 600 fiskal-key.pem",
        "# 2) sign the exact input string (no trailing newline!) and MD5 the raw signature",
        f"printf '%s' '{q}' \\",
        f"  | openssl dgst -{digest} -sign {key} -binary \\",
        "  | openssl dgst -md5 -r | cut -c1-32",
    ])


def sign_with_openssl(input_string: str, key_path: str, digest: str = "sha256") -> str:
    exe = shutil.which("openssl")
    if not exe:
        raise RuntimeError("openssl not found on PATH")
    proc = subprocess.run([exe, "dgst", f"-{digest}", "-sign", key_path, "-binary"],
                          input=input_string.encode("utf-8"), capture_output=True, check=False)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.decode("utf-8", "replace").strip())
    return zki_from_signature(proc.stdout)


# ----------------------------------------------------------------------------- self-test
def self_test() -> int:
    failures = 0

    def check(name, got, want):
        nonlocal failures
        ok = got == want
        failures += 0 if ok else 1
        print(f"[{'ok' if ok else 'FAIL'}] {name}" + ("" if ok else f": got {got!r}, want {want!r}"))

    # Spec v2.7 ch. 12.3 example values (spec OIB 00169331406 is not checksum-valid -> check_oib=False)
    s = build_input("00169331406", "01.10.2012 16:04:25", "12345", "blag001", "11245", "1245.56", check_oib=False)
    check("spec example concatenation", s, "0016933140601.10.2012 16:04:25" + "12345" + "blag001" + "11245" + "1245.56")
    check("XML-style T datetime is converted to space",
          format_datetime("01.09.2012T21:10:34"), "01.09.2012 21:10:34")
    check("ISO datetime accepted", format_datetime("2026-10-25T09:05:00"), "25.10.2026 09:05:00")
    check("amount 2 decimals", format_amount("10"), "10.00")
    check("amount comma input", format_amount("1245,5"), "1245.50")
    check("negative amount (storno)", format_amount("-105.5"), "-105.50")
    check("OIB valid (fictitious example)", oib_is_valid("12345678903"), True)
    check("OIB invalid", oib_is_valid("12345678901"), False)
    for bad in [("0", "BrOznRac 0"), ("012", "leading zero")]:
        try:
            build_input("12345678903", "01.01.2026 10:00:00", bad[0], "PP1", "1", "1.00")
            check(f"reject {bad[1]}", "accepted", "rejected")
        except ValueError:
            check(f"reject {bad[1]}", "rejected", "rejected")
    try:
        build_input("12345678903", "01.01.2026 10:00:00", "1", "PP-1", "1", "1.00")
        check("reject '-' in OznPosPr", "accepted", "rejected")
    except ValueError:
        check("reject '-' in OznPosPr", "rejected", "rejected")
    check("md5 of signature bytes", zki_from_signature(b"\x00\x01\x02"), hashlib.md5(b"\x00\x01\x02").hexdigest())
    check("zki shape", bool(re.fullmatch(r"[0-9a-f]{32}", zki_from_signature(b"x"))), True)

    # Optional end-to-end with a throwaway key (only if openssl is installed; no network).
    exe = shutil.which("openssl")
    if exe:
        with tempfile.TemporaryDirectory() as tmp:
            key = os.path.join(tmp, "k.pem")
            gen = subprocess.run([exe, "genpkey", "-algorithm", "RSA", "-pkeyopt", "rsa_keygen_bits:2048",
                                  "-out", key], capture_output=True)
            if gen.returncode == 0:
                z1 = sign_with_openssl(s, key)
                z2 = sign_with_openssl(s, key)
                check("openssl RSA-SHA256 ZKI deterministic (PKCS#1 v1.5)", z1, z2)
                check("openssl ZKI shape", bool(re.fullmatch(r"[0-9a-f]{32}", z1)), True)
            else:
                print("[skip] openssl genpkey failed; end-to-end test skipped")
    else:
        print("[skip] openssl not installed; end-to-end test skipped")

    print(f"\n{SPEC}\n{'ALL TESTS PASSED' if not failures else f'{failures} TEST(S) FAILED'}")
    return 1 if failures else 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--self-test", action="store_true", help="run built-in tests and exit")
    sub = p.add_subparsers(dest="cmd")

    def add_fields(sp):
        sp.add_argument("--oib", required=True, help="issuer OIB (11 digits)")
        sp.add_argument("--datetime", required=True, help="issue date/time, e.g. '25.10.2026 14:03:00'")
        sp.add_argument("--broj", required=True, help="BrOznRac, numeric receipt number")
        sp.add_argument("--opp", required=True, help="OznPosPr, business-premises label")
        sp.add_argument("--onu", required=True, help="OznNapUr, device number")
        sp.add_argument("--amount", required=True, help="IznosUkupno, e.g. 145.68 or -105.50")
        sp.add_argument("--no-oib-check", action="store_true", help="skip OIB checksum (spec examples)")

    b = sub.add_parser("build", help="print the ZKI input string")
    add_fields(b)
    c = sub.add_parser("commands", help="print openssl commands for this receipt")
    add_fields(c)
    c.add_argument("--key", default="fiskal-key.pem")
    c.add_argument("--digest", default="sha256", choices=["sha256", "sha1"])
    s = sub.add_parser("sign", help="compute ZKI by calling the local openssl CLI")
    add_fields(s)
    s.add_argument("--key", required=True, help="PEM private key file")
    s.add_argument("--digest", default="sha256", choices=["sha256", "sha1"],
                   help="sha256 per spec v2.7 (default); sha1 only for legacy comparison")
    f = sub.add_parser("from-signature", help="ZKI = MD5 of a raw binary signature file")
    f.add_argument("file")

    a = p.parse_args(argv)
    if a.self_test:
        return self_test()
    if not a.cmd:
        p.print_help()
        return 2
    print(NOTICE, file=sys.stderr)
    try:
        if a.cmd == "from-signature":
            with open(a.file, "rb") as fh:
                print(zki_from_signature(fh.read()))
            return 0
        inp = build_input(a.oib, a.datetime, a.broj, a.opp, a.onu, a.amount, check_oib=not a.no_oib_check)
        if a.cmd == "build":
            print(inp)
        elif a.cmd == "commands":
            print(openssl_commands(inp, a.key, a.digest))
        elif a.cmd == "sign":
            print(sign_with_openssl(inp, a.key, a.digest))
    except (ValueError, RuntimeError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
