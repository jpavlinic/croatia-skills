#!/usr/bin/env python3
"""Format, parse and check Croatian fiscal receipt numbers (broj racuna).

Rules implemented (Zakon o fiskalizaciji NN 89/25 cl. 9; Pravilnik NN 153/25 Privitak 1;
Tehnicka specifikacija v2.7 ch. 2.1.1):

  printed form   brojcana_oznaka/oznaka_poslovnog_prostora/oznaka_naplatnog_uredaja
                 e.g. 1234567890/POSL1/12
  BrOznRac       digits 0-9, no leading zeros, max 20 chars, must not be 0 (restrictive error 178)
  OznPosPr       0-9 a-z A-Z only, max 20 chars, unique per OIB
  OznNapUr       digits 0-9, no leading zeros, max 20 chars, unique per business premises
  OznSlijed      P = sequence per business premises, N = sequence per device
  sequence       unbroken, no gaps, per premises (P) or per device (N); may restart from any
                 number each calendar year / tax period (cl. 9(4)); rules set in the internal act.

Commands:
  format  --broj 15 --opp POSL1 --onu 2         -> 15/POSL1/2
  parse   15/POSL1/2                            -> validated parts (JSON)
  check-sequence --slijed P file.txt            -> gaps/duplicates in a list of numbers

Standard library only. No network access. Developer aid, not legal or tax advice.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict

NOTICE = ("TEMPLATE - not legal advice. Developer aid only: numbering rules must also match "
          "your internal act (interni akt) and the current regulations.")
_RE_NUM = re.compile(r"^[1-9][0-9]{0,19}$")
_RE_OPP = re.compile(r"^[0-9A-Za-z]{1,20}$")


def validate_parts(broj: str, opp: str, onu: str) -> list[str]:
    errors = []
    if not _RE_NUM.match(str(broj)):
        errors.append("BrOznRac must be 1-20 digits, no leading zeros, not 0")
    if not _RE_OPP.match(str(opp)):
        errors.append("OznPosPr must be 1-20 characters from 0-9 a-z A-Z (no '-', '/', spaces or diacritics)")
    if not _RE_NUM.match(str(onu)):
        errors.append("OznNapUr must be 1-20 digits, no leading zeros")
    return errors


def format_number(broj, opp, onu) -> str:
    errs = validate_parts(str(broj), str(opp), str(onu))
    if errs:
        raise ValueError("; ".join(errs))
    return f"{broj}/{opp}/{onu}"


def parse_number(text: str) -> dict:
    parts = str(text).strip().split("/")
    if len(parts) != 3:
        raise ValueError("expected exactly three parts: broj/oznakaPP/oznakaNU")
    errs = validate_parts(*parts)
    if errs:
        raise ValueError("; ".join(errs))
    return {"BrOznRac": parts[0], "OznPosPr": parts[1], "OznNapUr": parts[2]}


def check_sequence(numbers: list[str], slijed: str = "P") -> dict:
    """Check gaps and duplicates. ``numbers`` are full receipt numbers in issue order.
    slijed 'P': one sequence per premises; 'N': one sequence per premises+device."""
    if slijed not in ("P", "N"):
        raise ValueError("slijed must be P or N")
    groups: dict[tuple, list[int]] = defaultdict(list)
    bad = []
    for raw in numbers:
        raw = raw.strip()
        if not raw:
            continue
        try:
            p = parse_number(raw)
        except ValueError as exc:
            bad.append({"number": raw, "error": str(exc)})
            continue
        key = (p["OznPosPr"],) if slijed == "P" else (p["OznPosPr"], p["OznNapUr"])
        groups[key].append(int(p["BrOznRac"]))
    report = {"slijed": slijed, "invalid": bad, "groups": []}
    for key, nums in sorted(groups.items()):
        seen, dups = set(), []
        for n in nums:
            if n in seen:
                dups.append(n)
            seen.add(n)
        lo, hi = min(seen), max(seen)
        gaps = sorted(set(range(lo, hi + 1)) - seen)
        out_of_order = [b for a, b in zip(nums, nums[1:]) if b <= a and b not in dups]
        report["groups"].append({
            "key": "/".join(key), "count": len(nums), "first": lo, "last": hi,
            "gaps": gaps[:200], "gap_count": len(gaps), "duplicates": sorted(set(dups)),
            "not_increasing": out_of_order[:50],
        })
    report["ok"] = not bad and all(not g["gap_count"] and not g["duplicates"] for g in report["groups"])
    return report


def self_test() -> int:
    failures = 0

    def check(name, cond):
        nonlocal failures
        failures += 0 if cond else 1
        print(f"[{'ok' if cond else 'FAIL'}] {name}")

    check("format spec example", format_number("1234567890", "POSL1", "12") == "1234567890/POSL1/12")
    check("parse spec example", parse_number("123456789/POSL1/12") == {
        "BrOznRac": "123456789", "OznPosPr": "POSL1", "OznNapUr": "12"})
    for bad in ["0/POSL1/1", "01/POSL1/1", "1/POS-1/1", "1/POSL1/01", "1/POSL1", "1/ŠIBENIK/1",
                "1/" + "A" * 21 + "/1", "1" * 21 + "/P/1"]:
        try:
            parse_number(bad)
            check(f"reject {bad[:30]}", False)
        except ValueError:
            check(f"reject {bad[:30]}", True)
    r = check_sequence(["1/PP1/1", "2/PP1/2", "3/PP1/1", "5/PP1/1"], "P")
    check("P-sequence gap detected", r["groups"][0]["gaps"] == [4] and not r["ok"])
    r = check_sequence(["1/PP1/1", "1/PP1/2", "2/PP1/1", "2/PP1/2"], "N")
    check("N-sequence per device ok", r["ok"])
    r = check_sequence(["1/PP1/1", "1/PP1/2"], "P")
    check("P-sequence duplicate across devices detected", r["groups"][0]["duplicates"] == [1])
    r = check_sequence(["100/PP1/1", "101/PP1/1"], "P")
    check("sequence may start at any number (cl. 9(4))", r["ok"])
    print("\nRules: Zakon o fiskalizaciji NN 89/25 cl. 9; Pravilnik NN 153/25 Privitak 1; Teh. spec. v2.7")
    print("ALL TESTS PASSED" if not failures else f"{failures} TEST(S) FAILED")
    return 1 if failures else 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--self-test", action="store_true")
    sub = p.add_subparsers(dest="cmd")
    f = sub.add_parser("format")
    f.add_argument("--broj", required=True)
    f.add_argument("--opp", required=True)
    f.add_argument("--onu", required=True)
    pa = sub.add_parser("parse")
    pa.add_argument("number")
    c = sub.add_parser("check-sequence", help="file with one receipt number per line, in issue order")
    c.add_argument("file")
    c.add_argument("--slijed", default="P", choices=["P", "N"])
    a = p.parse_args(argv)
    if a.self_test:
        return self_test()
    if not a.cmd:
        p.print_help()
        return 2
    print(NOTICE, file=sys.stderr)
    try:
        if a.cmd == "format":
            print(format_number(a.broj, a.opp, a.onu))
        elif a.cmd == "parse":
            print(json.dumps(parse_number(a.number), ensure_ascii=False))
        else:
            with open(a.file, encoding="utf-8") as fh:
                rep = check_sequence(fh.read().splitlines(), a.slijed)
            print(json.dumps(rep, ensure_ascii=False, indent=2))
            return 0 if rep["ok"] else 1
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
