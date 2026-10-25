#!/usr/bin/env python3
"""Paušalni obrt estimate for 2026 (Croatia): tax class, annual tax, contributions.

ESTIMATE ONLY - not tax advice. Rules implemented (tax year 2026):

- Paušal tax = 12% of the class's annual paušal income
  (Zakon o porezu na dohodak čl. 82 st. 6; NN 152/24).
- Classes and annual paušal income: Pravilnik o paušalnom oporezivanju samostalnih
  djelatnosti (NN 1/24, 16/25); the same seven amounts appear as contribution bases in
  Naredba o iznosima osnovica za obračun doprinosa za 2026. (NN 150/2025) čl. 14.
- Paušal limit 60,000.00 EUR receipts (ZPD čl. 82 st. 1 + Zakon o PDV-u čl. 90 st. 1).
- Contributions, paušal obrt as main activity: base 797.20 EUR/month
  (0.4 x average wage 1,993.00 EUR; NN 150/2025 čl. 7; Zakon o doprinosima čl. 70),
  MIO I 15% + MIO II 5% (or 20% pillar I only) + health 16.5% (ZOD čl. 13, 14, 17).
- Paušal obrt as "druga djelatnost" (owner employed elsewhere): annual base = class
  paušal income (ZOD čl. 185 st. 3; NN 150/2025 čl. 14), MIO 7.5% + 2.5% (or 10%)
  + health 7.5% (ZOD čl. 13 st. 3, čl. 14 st. 2, čl. 17 st. 2), set by PU rješenje.
- Pensioner who keeps pension status: no contributions on paušal income (ZOD čl. 212 st. 3).
- HOK chamber contribution: 1.9% of the 600.00 EUR basic personal allowance = 11.40 EUR
  per month, first two years of a first-ever obrt exempt (Odluka, NN 154/2022, čl. 6, 15).

Python 3 standard library only. No network access.
"""
import argparse
import sys
from decimal import Decimal, ROUND_HALF_UP

YEAR = 2026
LIMIT = Decimal("60000.00")
TAX_RATE = Decimal("0.12")

# (upper limit of annual receipts, annual paušal income) - NN 1/24, 16/25; NN 150/2025 čl. 14
CLASSES = [
    (Decimal("11300.00"), Decimal("1695.00")),
    (Decimal("15300.00"), Decimal("2295.00")),
    (Decimal("19900.00"), Decimal("2985.00")),
    (Decimal("30600.00"), Decimal("4590.00")),
    (Decimal("40000.00"), Decimal("6000.00")),
    (Decimal("50000.00"), Decimal("7500.00")),
    (Decimal("60000.00"), Decimal("9000.00")),
]

AVG_WAGE = Decimal("1993.00")      # NN 150/2025 čl. 2
MAIN_BASE = Decimal("797.20")      # 0.4 x AVG_WAGE, NN 150/2025 čl. 7
HOK_MONTHLY = Decimal("11.40")     # 1.9% x 600.00

SOURCES = [
    "Zakon o porezu na dohodak čl. 82 (NN 115/16 ... 152/24) - zakon.hr/z/85",
    "Pravilnik o paušalnom oporezivanju samostalnih djelatnosti (NN 1/20 ... 1/24, 16/25) - narodne-novine.nn.hr/clanci/sluzbeni/2025_01_16_149.html",
    "Naredba o iznosima osnovica za obračun doprinosa za 2026. (NN 150/2025) čl. 2, 7, 14 - narodne-novine.nn.hr/clanci/sluzbeni/2025_12_150_2237.html",
    "Zakon o doprinosima čl. 13, 14, 17, 70, 185, 212 - zakon.hr/z/365",
    "Zakon o PDV-u čl. 90 st. 1 (60,000 EUR) - zakon.hr/z/1455",
    "Odluka o obveznom komorskom doprinosu (NN 154/2022) čl. 6, 15",
]


def r2(x):
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def find_class(receipts):
    """Return (class_no, paušal_income) or None if above the limit."""
    if receipts < 0:
        raise ValueError("receipts must be >= 0")
    for i, (upper, income) in enumerate(CLASSES, start=1):
        if receipts <= upper:
            return i, income
    return None


def estimate(receipts, status="main", pillar2=True, months=12, hok_exempt=False):
    """Compute the estimate. status: main | employed | pensioner."""
    receipts = Decimal(str(receipts))
    found = find_class(receipts)
    if found is None:
        return {"over_limit": True, "receipts": receipts}
    cls, income = found
    tax = r2(income * TAX_RATE)
    res = {
        "over_limit": False,
        "receipts": receipts,
        "class": cls,
        "pausal_income": income,
        "annual_tax": tax,
        "quarterly_tax": r2(tax / 4),
        "status": status,
    }
    if status == "main":
        if pillar2:
            mio1 = r2(MAIN_BASE * Decimal("0.15"))
            mio2 = r2(MAIN_BASE * Decimal("0.05"))
        else:
            mio1 = r2(MAIN_BASE * Decimal("0.20"))
            mio2 = Decimal("0.00")
        health = r2(MAIN_BASE * Decimal("0.165"))
        monthly = mio1 + mio2 + health
        res.update(contrib_base=MAIN_BASE, mio1=mio1, mio2=mio2, health=health,
                   contrib_monthly=monthly, contrib_annual=r2(monthly * months))
    elif status == "employed":
        if pillar2:
            mio1 = r2(income * Decimal("0.075"))
            mio2 = r2(income * Decimal("0.025"))
        else:
            mio1 = r2(income * Decimal("0.10"))
            mio2 = Decimal("0.00")
        health = r2(income * Decimal("0.075"))
        res.update(contrib_base=income, mio1=mio1, mio2=mio2, health=health,
                   contrib_monthly=None, contrib_annual=mio1 + mio2 + health)
    elif status == "pensioner":
        res.update(contrib_base=Decimal("0.00"), mio1=Decimal("0.00"), mio2=Decimal("0.00"),
                   health=Decimal("0.00"), contrib_monthly=Decimal("0.00"),
                   contrib_annual=Decimal("0.00"))
    else:
        raise ValueError("status must be main, employed or pensioner")
    res["hok_annual"] = Decimal("0.00") if hok_exempt else r2(HOK_MONTHLY * months)
    return res


def fmt(x):
    s = f"{x:,.2f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".") + " EUR"


def print_report(res, months):
    print("ESTIMATE ONLY - not tax advice. Verify with Porezna uprava / your accountant (računovođa).")
    print(f"Rules: Croatia, tax year {YEAR}, paušalni obrt (see sources below).")
    print()
    if res["over_limit"]:
        print(f"Annual receipts {fmt(res['receipts'])} exceed the paušal limit of {fmt(LIMIT)}.")
        print("Paušal no longer applies: VAT registration (P-PDV within 8 days, Zakon o PDV-u) and")
        print("switch to real income (ZPD čl. 82 st. 9-10). Talk to an accountant now.")
    else:
        print(f"Annual receipts:          {fmt(res['receipts'])}")
        print(f"Paušal class:             {res['class']} of 7")
        print(f"Annual paušal income:     {fmt(res['pausal_income'])}")
        print(f"Annual paušal tax (12%):  {fmt(res['annual_tax'])}  (quarterly {fmt(res['quarterly_tax'])},"
              " due 31.3., 30.6., 30.9., 31.12.)")
        print()
        st = res["status"]
        if st == "main":
            print(f"Contributions (main activity), base {fmt(res['contrib_base'])}/month:")
            print(f"  MIO I:   {fmt(res['mio1'])}")
            print(f"  MIO II:  {fmt(res['mio2'])}")
            print(f"  HZZO:    {fmt(res['health'])}")
            print(f"  Monthly: {fmt(res['contrib_monthly'])}  (due by the 15th for the previous month)")
            print(f"  For {months} month(s): {fmt(res['contrib_annual'])}")
        elif st == "employed":
            print("Contributions (paušal obrt next to employment = druga djelatnost), annual, by PU rješenje:")
            print(f"  Base:    {fmt(res['contrib_base'])} (class paušal income)")
            print(f"  MIO I:   {fmt(res['mio1'])}")
            print(f"  MIO II:  {fmt(res['mio2'])}")
            print(f"  HZZO:    {fmt(res['health'])}")
            print(f"  Annual:  {fmt(res['contrib_annual'])}")
        else:
            print("Contributions: 0 (pensioner who keeps pension status, ZOD čl. 212 st. 3).")
        print()
        print(f"HOK chamber contribution: {fmt(res['hok_annual'])} for {months} month(s)"
              " (0 in the first two years of a first-ever obrt).")
        total = res["annual_tax"] + res["contrib_annual"] + res["hok_annual"]
        print(f"Approximate total:        {fmt(total)}")
        print()
        print("Not included: turistička članarina, bank and fiscalization software costs, accountant,")
        print("reverse-charge VAT on foreign services, OSS. A 2027 reform for classes above 40,000 EUR")
        print("was announced in 2026 (VERIFY final law before using these figures for 2027).")
    print()
    print("Sources:")
    for s in SOURCES:
        print(f"  - {s}")


def self_test():
    ok = True

    def check(name, got, exp):
        nonlocal ok
        if got != exp:
            ok = False
            print(f"FAIL {name}: got {got}, expected {exp}")

    check("class 0", find_class(Decimal("0"))[0], 1)
    check("class edge 11300", find_class(Decimal("11300.00"))[0], 1)
    check("class edge 11300.01", find_class(Decimal("11300.01"))[0], 2)
    check("class 40000", find_class(Decimal("40000"))[0], 5)
    check("class 60000", find_class(Decimal("60000"))[0], 7)
    check("over limit", find_class(Decimal("60000.01")), None)
    expected_tax = ["203.40", "275.40", "358.20", "550.80", "720.00", "900.00", "1080.00"]
    for (upper, _), exp in zip(CLASSES, expected_tax):
        check(f"tax {upper}", estimate(upper)["annual_tax"], Decimal(exp))
    m = estimate(25000)
    check("main monthly", m["contrib_monthly"], Decimal("290.98"))
    check("main mio1", m["mio1"], Decimal("119.58"))
    check("main mio2", m["mio2"], Decimal("39.86"))
    check("main health", m["health"], Decimal("131.54"))
    check("main annual", m["contrib_annual"], Decimal("3491.76"))
    check("pillar1 only monthly", estimate(25000, pillar2=False)["contrib_monthly"], Decimal("290.98"))
    e = estimate(55000, status="employed")
    check("employed annual cls7", e["contrib_annual"], Decimal("1575.00"))
    e1 = estimate(5000, status="employed")
    check("employed annual cls1", e1["contrib_annual"], Decimal("296.64"))
    check("pensioner", estimate(5000, status="pensioner")["contrib_annual"], Decimal("0.00"))
    check("hok", estimate(5000)["hok_annual"], Decimal("136.80"))
    check("hok exempt", estimate(5000, hok_exempt=True)["hok_annual"], Decimal("0.00"))
    check("main base = 0.4 x avg", r2(AVG_WAGE * Decimal("0.4")), MAIN_BASE)
    check("over limit flag", estimate(70000)["over_limit"], True)
    print("self-test OK" if ok else "self-test FAILED")
    return 0 if ok else 1


def main(argv=None):
    p = argparse.ArgumentParser(
        description=f"Paušalni obrt estimate for {YEAR} (Croatia). ESTIMATE ONLY - not tax advice.")
    p.add_argument("receipts", nargs="?", type=str,
                   help="expected annual receipts (primici) in EUR, e.g. 24000 or 24000.50")
    p.add_argument("--status", choices=["main", "employed", "pensioner"], default="main",
                   help="main = obrt is your only insurance basis (default); employed = you are "
                        "employed full-time elsewhere (druga djelatnost); pensioner = keeps pension status")
    p.add_argument("--pillar1-only", action="store_true",
                   help="you are insured only in pension pillar I (no 2nd pillar); totals do not change")
    p.add_argument("--months", type=int, default=12,
                   help="months of activity this year for contribution/HOK totals (default 12)")
    p.add_argument("--hok-exempt", action="store_true",
                   help="first two years of a first-ever obrt: no HOK chamber contribution")
    p.add_argument("--self-test", action="store_true", help="run built-in tests and exit")
    a = p.parse_args(argv)
    if a.self_test:
        return self_test()
    if a.receipts is None:
        p.error("receipts is required (or use --self-test)")
    try:
        receipts = Decimal(a.receipts.replace(",", "."))
    except Exception:
        p.error("receipts must be a number")
    if receipts < 0:
        p.error("receipts must be >= 0")
    if not 1 <= a.months <= 12:
        p.error("--months must be 1-12")
    res = estimate(receipts, status=a.status, pillar2=not a.pillar1_only,
                   months=a.months, hok_exempt=a.hok_exempt)
    print_report(res, a.months)
    return 0


if __name__ == "__main__":
    sys.exit(main())
