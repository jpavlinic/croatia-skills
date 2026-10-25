#!/usr/bin/env python3
"""Build the QR-code content (verification URL) for a Croatian fiscalized B2C receipt.

Format per "Tehnicka specifikacija za korisnike fiskalizacije racuna u krajnjoj potrosnji"
v2.7 (21.07.2026), ch. 2.7, and Pravilnik NN 153/25 cl. 17-18:

    https://porezna.gov.hr/rn?jir=<JIR 36 chars>&datv=<YYYYMMDD_HHMM>&izn=<amount in cents>
    https://porezna.gov.hr/rn?zki=<ZKI 32 chars>&datv=<YYYYMMDD_HHMM>&izn=<amount in cents>

  * use the JIR when you have it; use the ZKI when the receipt was issued without a JIR
    (offline / error, later delivered with NakDost=true);
  * datv: issue date and time to the minute (13 chars);
  * izn: total in euro cents, no separators, no leading zeros, '-' for negative (storno),
    max 10 characters including the sign. 1.525,99 -> 152599; -105,50 -> -10550; 5,10 -> 510.

Physical rules (cl. 18): QR model 1 or 2, smallest possible version, at least 2 x 2 cm,
quiet zone at least 2 mm, error correction at least 'L', ISO/IEC 15415, no logo in or
under the code. This script produces the text only; render it with any QR encoder
(e.g. `qrencode -l L -m 2 -o qr.png "<url>"`) or your POS printer's QR command.

Standard library only. No network access. Developer aid, not legal or tax advice.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

BASE_URL = "https://porezna.gov.hr/rn"
NOTICE = ("TEMPLATE - not legal advice. Developer aid only: verify the QR format against the "
          "current Tehnicka specifikacija (ch. 2.7) before production.")
_RE_JIR = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
_RE_ZKI = re.compile(r"^[0-9a-f]{32}$")


def format_datv(value) -> str:
    if isinstance(value, _dt.datetime):
        return value.strftime("%Y%m%d_%H%M")
    s = str(value).strip()
    for fmt in ("%d.%m.%Y %H:%M:%S", "%d.%m.%YT%H:%M:%S", "%d.%m.%Y %H:%M",
                "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M", "%Y%m%d_%H%M"):
        try:
            return _dt.datetime.strptime(s, fmt).strftime("%Y%m%d_%H%M")
        except ValueError:
            continue
    raise ValueError(f"unrecognised date/time {value!r}")


def format_izn(value) -> str:
    try:
        d = Decimal(str(value).replace(",", ".")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    except InvalidOperation as exc:
        raise ValueError(f"invalid amount {value!r}") from exc
    cents = int(d * 100)
    s = str(cents)  # int() drops leading zeros; negative keeps '-'
    if len(s) > 10:
        raise ValueError("izn longer than 10 characters")
    return s


def build_url(issued_at, total, jir: str | None = None, zki: str | None = None) -> str:
    if bool(jir) == bool(zki):
        raise ValueError("give exactly one of jir or zki")
    if jir:
        if not _RE_JIR.match(jir):
            raise ValueError("JIR must be a 36-char UUID 8-4-4-4-12")
        ident = f"jir={jir.lower()}"
    else:
        if not _RE_ZKI.match(zki):
            raise ValueError("ZKI must be 32 lower-case hex characters")
        ident = f"zki={zki}"
    return f"{BASE_URL}?{ident}&datv={format_datv(issued_at)}&izn={format_izn(total)}"


def self_test() -> int:
    failures = 0

    def check(name, got, want):
        nonlocal failures
        ok = got == want
        failures += 0 if ok else 1
        print(f"[{'ok' if ok else 'FAIL'}] {name}" + ("" if ok else f": got {got!r}, want {want!r}"))

    j = "12345678-1234-1234-1234-123456789012"
    # Examples from spec v2.7 ch. 2.7 (amounts there are pre-2023 kuna; format is identical in EUR)
    check("spec JIR example", build_url("21.09.2020 06:30:00", "1525.99", jir=j),
          f"{BASE_URL}?jir={j}&datv=20200921_0630&izn=152599")
    check("spec storno example", build_url("10.01.2021 14:00:00", "-105.50", jir=j),
          f"{BASE_URL}?jir={j}&datv=20210110_1400&izn=-10550")
    check("spec ZKI example", build_url("05.02.2021 08:01:00", "5.10", zki="12345678123412341234123456789012"),
          f"{BASE_URL}?zki=12345678123412341234123456789012&datv=20210205_0801&izn=510")
    check("spec ZKI example 2", build_url("01.01.2021 19:00:00", "47.00", zki="12345678123412341234123456789010"),
          f"{BASE_URL}?zki=12345678123412341234123456789010&datv=20210101_1900&izn=4700")
    check("cents without leading zeros", format_izn("0.05"), "5")
    check("comma decimal input", format_izn("1.234,56".replace(".", "")), "123456")
    check("XML datetime input", format_datv("01.09.2012T21:10:34"), "20120901_2110")
    check("JIR upper-case normalised", build_url("2026-10-25T10:00:00", "1", jir=j.upper()).count(j), 1)
    for name, kw in [("both ids", dict(jir=j, zki="0" * 32)), ("no id", {}), ("bad jir", dict(jir="abc")),
                     ("bad zki", dict(zki="Z" * 32))]:
        try:
            build_url("2026-10-25T10:00:00", "1", **kw)
            check(f"reject {name}", "accepted", "rejected")
        except ValueError:
            check(f"reject {name}", "rejected", "rejected")
    try:
        format_izn("123456789.00")
        check("reject >10 chars", "accepted", "rejected")
    except ValueError:
        check("reject >10 chars", "rejected", "rejected")
    print("\nFormat: Tehnicka specifikacija v2.7 ch. 2.7; Pravilnik NN 153/25 cl. 17-18")
    print("ALL TESTS PASSED" if not failures else f"{failures} TEST(S) FAILED")
    return 1 if failures else 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--self-test", action="store_true")
    p.add_argument("--jir")
    p.add_argument("--zki")
    p.add_argument("--datetime", help="issue date/time, e.g. '25.10.2026 14:03:00'")
    p.add_argument("--amount", help="IznosUkupno in EUR, e.g. 145.68")
    a = p.parse_args(argv)
    if a.self_test:
        return self_test()
    if not (a.datetime and a.amount):
        p.print_help()
        return 2
    print(NOTICE, file=sys.stderr)
    try:
        print(build_url(a.datetime, a.amount, jir=a.jir, zki=a.zki))
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
