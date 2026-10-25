#!/usr/bin/env python3
"""Croatian salary calculator (bruto -> neto and neto -> bruto), rules for 2026.

ESTIMATE ONLY. Not legal or tax advice. Python 3 standard library only, no network.

Implements, for one monthly salary paid by one employer to a tax resident:
  * pension contributions from salary (MIO I 15 % + MIO II 5 %, or MIO I 20 % if
    the worker is only in pillar I), Zakon o doprinosima;
  * the MIO I base reduction for gross pay up to EUR 1,300 ("umanjenje mjesecne
    osnovice na temelju generacijske solidarnosti"): EUR 300 up to EUR 700 gross
    (never more than the gross), 0.5 x (1,300 - gross) between EUR 700.01 and 1,300;
    it reduces the MIO I base only, MIO II is always on the full base
    (Porezna uprava brochure "Umanjenje mjesecne osnovice");
  * the 2026 maximum monthly contribution base of EUR 11,958.00 (Naredba, NN 150/2025);
  * personal deduction (osobni odbitak) 2026: EUR 600 x coefficients
    (Zakon o porezu na dohodak cl. 14), capped at the income;
  * income tax at the city/municipality rates, lower rate up to EUR 5,000/month
    (EUR 60,000/year), higher rate above (ZPD cl. 19 and 19.a; no prirez since 2024);
  * employer health insurance 16.5 % on gross (no cap);
  * optional estimates of the youth relief (100 % under 25 / 50 % age 26-30 of the
    tax on the lower-rate part) and the 50 % relief for residents of assisted areas
    group I / Vukovar (ZPD cl. 45). These are granted in the ANNUAL assessment, so by
    default they are shown as a separate "expected annual refund" line, not in net.

Not modelled: several employers in one month, part-month MIO relief splits,
non-residents, directors' minimum base, special contribution regimes, employer
health exemptions (only a manual --health-exempt switch), non-taxable payments,
annual equalisation. Always verify with the official sources.
"""

import argparse
import json
import sys
from decimal import ROUND_HALF_UP, Decimal

RULE_YEAR = 2026

D = Decimal
CENT = D("0.01")


def r2(x):
    """Round half-up to cents."""
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------- 2026 parameters
PARAMS_2026 = {
    "minimum_wage_gross": D("1050.00"),        # Uredba, NN 132/2025
    "personal_deduction_base": D("600.00"),    # ZPD cl. 14 st. 1
    "mio1_rate": D("0.15"),                    # pillar I when also in pillar II
    "mio2_rate": D("0.05"),                    # pillar II
    "mio1_only_rate": D("0.20"),               # pillar I only
    "health_rate": D("0.165"),                 # employer, on gross
    "mio_relief_fixed": D("300.00"),           # gross <= 700
    "mio_relief_low": D("700.00"),
    "mio_relief_high": D("1300.00"),
    "max_monthly_base": D("11958.00"),         # Naredba NN 150/2025 cl. 4
    "min_monthly_base": D("757.34"),           # Naredba NN 150/2025 cl. 3
    "monthly_tax_threshold": D("5000.00"),     # EUR 60,000 / 12
    "default_rates": (D("20"), D("30")),       # ZPD cl. 19.a st. 5
}

# Rates applying from 1 January 2026 (Porezna uprava table, as reproduced by
# RRiF "Stope poreza na dohodak za isplate od 1. sijecnja 2026."). Only big
# cities are listed; for anything else pass --lower/--higher.
CITY_RATES_2026 = {
    "zagreb": ("23", "33"),
    "split": ("21.5", "32"),
    "rijeka": ("20", "25"),
    "osijek": ("20", "30"),
    "zadar": ("20", "30"),
    "pula": ("22", "32"),
    "varazdin": ("21", "32"),
    "slavonski-brod": ("20", "30"),
    "velika-gorica": ("20", "30"),
    "sibenik": ("20", "30"),
    "dubrovnik": ("20", "30"),
    "karlovac": ("19", "29"),
    "sisak": ("21.6", "31.6"),
    "bjelovar": ("18", "25"),
    "samobor": ("18", "27"),
    "cakovec": ("20", "30"),
    "koprivnica": ("20", "30"),
    "vukovar": ("20", "30"),
    "gospic": ("22", "32"),
    "pazin": ("22", "30"),
    "vinkovci": ("20", "30"),
    "pozega": ("20", "30"),
    "virovitica": ("20", "30"),
    "krapina": ("20", "30"),
}

# ZPD cl. 14 st. 3: coefficients for the 1st..9th dependent child.
CHILD_COEFFS = [D(x) for x in ("0.5", "0.7", "1.0", "1.4", "1.9", "2.5", "3.2", "4.0", "4.9")]

SOURCES = [
    "Uredba o visini minimalne place za 2026. (NN 132/2025): EUR 1,050.00 gross",
    "Zakon o porezu na dohodak (NN 115/16 ... 152/24) cl. 14, 19, 19.a, 45",
    "Naredba o iznosima osnovica za obracun doprinosa za 2026. (NN 150/2025)",
    "Porezna uprava: brosura 'Umanjenje mjesecne osnovice za obracun doprinosa za MO'",
    "Porezna uprava / RRiF: stope poreza na dohodak od 1.1.2026.",
]


def child_coefficient_total(children):
    if children < 0:
        raise ValueError("children must be >= 0")
    if children > len(CHILD_COEFFS):
        raise ValueError("more than 9 children: compute the coefficient by hand (ZPD cl. 14 st. 3 r.br. 11)")
    return sum(CHILD_COEFFS[:children], D("0"))


def personal_deduction(base, children=0, dependants=0, disabled=0, disabled100=0):
    coeff = D("1.0") + child_coefficient_total(children)
    coeff += D("0.5") * dependants
    coeff += D("0.3") * disabled
    coeff += D("1.0") * disabled100
    return r2(base * coeff), coeff


def mio_relief(gross, p):
    if gross <= p["mio_relief_low"]:
        return r2(min(p["mio_relief_fixed"], gross))
    if gross <= p["mio_relief_high"]:
        return r2(D("0.5") * (p["mio_relief_high"] - gross))
    return D("0.00")


def gross_to_net(gross, lower, higher, children=0, dependants=0, disabled=0,
                 disabled100=0, pillar1_only=False, no_mio_relief=False,
                 youth=None, assisted_area=False, apply_reliefs_monthly=False,
                 health_exempt=False, personal_base=None, params=None):
    """Return a dict with the full monthly calculation. Amounts are Decimals."""
    p = dict(PARAMS_2026 if params is None else params)
    gross = r2(gross)
    if gross < 0:
        raise ValueError("gross must be >= 0")
    lower = D(str(lower)) / 100
    higher = D(str(higher)) / 100
    pbase = p["personal_deduction_base"] if personal_base is None else D(str(personal_base))

    base = min(gross, p["max_monthly_base"])
    relief = D("0.00") if no_mio_relief else mio_relief(gross, p)
    mio1_base = max(D("0"), base - relief)
    if pillar1_only:
        mio1 = r2(mio1_base * p["mio1_only_rate"])
        mio2 = D("0.00")
    else:
        mio1 = r2(mio1_base * p["mio1_rate"])
        mio2 = r2(base * p["mio2_rate"])
    contributions = mio1 + mio2
    income = gross - contributions

    pd_full, coeff = personal_deduction(pbase, children, dependants, disabled, disabled100)
    pd_used = min(pd_full, income)
    tax_base = max(D("0"), income - pd_used)

    thr = p["monthly_tax_threshold"]
    base_low = min(tax_base, thr)
    base_high = max(D("0"), tax_base - thr)
    tax_low = r2(base_low * lower)
    tax_high = r2(base_high * higher)
    tax = tax_low + tax_high

    # ZPD cl. 45: youth relief first (st. 7), then 50 % assisted-area relief (st. 1).
    youth_red = D("0.00")
    if youth == "under25":
        youth_red = tax_low
    elif youth == "26-30":
        youth_red = r2(tax_low * D("0.5"))
    area_red = r2((tax - youth_red) * D("0.5")) if assisted_area else D("0.00")
    reliefs = youth_red + area_red

    tax_withheld = tax - reliefs if apply_reliefs_monthly else tax
    net = income - tax_withheld
    health = D("0.00") if health_exempt else r2(gross * p["health_rate"])
    total_cost = gross + health

    warnings = []
    if gross < p["minimum_wage_gross"]:
        warnings.append("Gross is below the 2026 minimum wage (EUR 1,050.00) - fine only for part-time work.")
    if pd_used < pd_full:
        warnings.append("Personal deduction exceeds income; the unused part is lost for this month.")
    if reliefs and not apply_reliefs_monthly:
        warnings.append("Youth/assisted-area relief is granted in the annual assessment (ZPD cl. 45); shown as expected refund, not in net.")
    if apply_reliefs_monthly and reliefs:
        warnings.append("Reliefs applied monthly at your request - VERIFY that the payroll may do this.")
    if gross > p["max_monthly_base"]:
        warnings.append("MIO contributions capped at the 2026 maximum monthly base EUR 11,958.00.")
    if health_exempt:
        warnings.append("Employer health contribution set to 0 - VERIFY the exemption under Zakon o doprinosima.")

    return {
        "rule_year": RULE_YEAR,
        "gross": gross,
        "mio_relief": relief,
        "mio1_base": r2(mio1_base),
        "mio1": mio1,
        "mio2": mio2,
        "contributions_from_salary": contributions,
        "income": income,
        "personal_deduction_coefficient": coeff,
        "personal_deduction": pd_used,
        "tax_base": tax_base,
        "tax_rates_pct": (lower * 100, higher * 100),
        "tax_lower_part": tax_low,
        "tax_higher_part": tax_high,
        "tax": tax,
        "youth_reduction": youth_red,
        "assisted_area_reduction": area_red,
        "reliefs_applied_monthly": bool(apply_reliefs_monthly),
        "tax_withheld": tax_withheld,
        "net": net,
        "expected_annual_refund_for_month": D("0.00") if apply_reliefs_monthly else reliefs,
        "employer_health": health,
        "employer_total_cost": total_cost,
        "warnings": warnings,
    }


def net_to_gross(target_net, **kw):
    """Binary search on cents: smallest gross whose net >= target."""
    target = r2(target_net)
    lo, hi = 0, 10_000_000  # cents (EUR 100,000)
    while lo < hi:
        mid = (lo + hi) // 2
        if gross_to_net(D(mid) / 100, **kw)["net"] >= target:
            hi = mid
        else:
            lo = mid + 1
    return gross_to_net(D(lo) / 100, **kw)


def resolve_rates(city, lower, higher):
    if lower is not None or higher is not None:
        if lower is None or higher is None:
            raise ValueError("give both --lower and --higher")
        return D(str(lower)), D(str(higher)), "custom rates"
    if city:
        key = city.strip().lower().replace(" ", "-")
        for a, b in (("č", "c"), ("ć", "c"), ("ž", "z"), ("š", "s"), ("đ", "d")):
            key = key.replace(a, b)
        if key not in CITY_RATES_2026:
            raise ValueError("city '%s' not in the built-in table; pass --lower/--higher "
                             "from the Porezna uprava table" % city)
        lo, hi = CITY_RATES_2026[key]
        return D(lo), D(hi), city
    lo, hi = PARAMS_2026["default_rates"]
    return lo, hi, "default 20/30 % (no city given)"


def fmt(x):
    return "{:,.2f}".format(x)


def print_report(res, place, mode):
    print("ESTIMATE ONLY - not legal or tax advice. Rules: Croatia %d payroll." % res["rule_year"])
    print("Mode: %s | Tax rates: %s/%s %% (%s)" % (
        mode, res["tax_rates_pct"][0].normalize(), res["tax_rates_pct"][1].normalize(), place))
    rows = [
        ("Bruto (gross)", res["gross"]),
        ("MIO I base reduction", res["mio_relief"]),
        ("MIO I (pillar I)", res["mio1"]),
        ("MIO II (pillar II)", res["mio2"]),
        ("Contributions from salary", res["contributions_from_salary"]),
        ("Dohodak (income)", res["income"]),
        ("Osobni odbitak used (coef. %s)" % res["personal_deduction_coefficient"].normalize(), res["personal_deduction"]),
        ("Porezna osnovica (tax base)", res["tax_base"]),
        ("Tax at lower rate", res["tax_lower_part"]),
        ("Tax at higher rate", res["tax_higher_part"]),
        ("Income tax withheld", res["tax_withheld"]),
        ("NETO (net pay)", res["net"]),
        ("Employer health 16.5 %", res["employer_health"]),
        ("Employer total cost", res["employer_total_cost"]),
    ]
    for label, val in rows:
        print("  %-36s %12s" % (label, fmt(val)))
    if res["expected_annual_refund_for_month"]:
        print("  %-36s %12s" % ("Expected annual refund (this month)", fmt(res["expected_annual_refund_for_month"])))
    for w in res["warnings"]:
        print("  ! " + w)
    print("Sources:")
    for s in SOURCES:
        print("  - " + s)
    print("ESTIMATE ONLY. Check the cited sources and a payroll professional (racunovoda).")


def to_jsonable(res):
    out = {}
    for k, v in res.items():
        if isinstance(v, Decimal):
            out[k] = float(v)
        elif isinstance(v, tuple):
            out[k] = [float(x) for x in v]
        else:
            out[k] = v
    out["notice"] = "ESTIMATE ONLY - not legal or tax advice"
    out["sources"] = SOURCES
    return out


# ---------------------------------------------------------------- self-test
def self_test():
    z = dict(lower=23, higher=33)
    cases = []

    def check(name, got, exp):
        ok = r2(got) == r2(D(str(exp)))
        cases.append((name, ok, got, exp))

    # 1. EUR 1,500 Zagreb, single, pillar II: 225 + 75; 1,200 - 600 = 600 x 23 % = 138.
    r = gross_to_net(1500, **z)
    check("1500 ZG mio1", r["mio1"], "225.00")
    check("1500 ZG mio2", r["mio2"], "75.00")
    check("1500 ZG tax", r["tax"], "138.00")
    check("1500 ZG net", r["net"], "1062.00")
    check("1500 ZG health", r["employer_health"], "247.50")
    check("1500 ZG total", r["employer_total_cost"], "1747.50")

    # 2. Minimum wage 1,050 Zagreb: relief 0.5 x 250 = 125; MIO I 15 % x 925 = 138.75;
    #    MIO II 52.50; income 858.75; base 258.75; tax 59.51; net 799.24.
    r = gross_to_net(1050, **z)
    check("1050 relief", r["mio_relief"], "125.00")
    check("1050 mio1", r["mio1"], "138.75")
    check("1050 mio2", r["mio2"], "52.50")
    check("1050 tax", r["tax"], "59.51")
    check("1050 net", r["net"], "799.24")
    check("1050 total", r["employer_total_cost"], "1223.25")

    # 3. Official Porezna uprava brochure example (2024 rules: odbitak 560,
    #    Veliko Trojstvo 17.5 %): Martina (pillar II) net 836.37, Sanja (pillar I only)
    #    net 840.50, worker B (500 gross) net 445.00.
    vt = dict(lower="17.5", higher="27.5", personal_base=560)
    check("PU Martina net", gross_to_net(1100, **vt)["net"], "836.37")
    check("PU Martina tax", gross_to_net(1100, **vt)["tax"], "58.63")
    check("PU Sanja net", gross_to_net(1100, pillar1_only=True, **vt)["net"], "840.50")
    check("PU Sanja mio1", gross_to_net(1100, pillar1_only=True, **vt)["mio1"], "200.00")
    check("PU worker B net", gross_to_net(500, **vt)["net"], "445.00")
    check("PU Goran net", gross_to_net(250, **vt)["net"], "237.50")

    # 4. EUR 8,000 Zagreb: MIO 1,600; income 6,400; base 5,800;
    #    tax 5,000 x 23 % + 800 x 33 % = 1,150 + 264 = 1,414; net 4,986.
    r = gross_to_net(8000, **z)
    check("8000 tax", r["tax"], "1414.00")
    check("8000 net", r["net"], "4986.00")

    # 5. EUR 15,000 Zagreb: MIO capped at 11,958 x 20 % = 2,391.60; income 12,608.40;
    #    base 12,008.40; tax 1,150 + 7,008.40 x 33 % = 1,150 + 2,312.77 = 3,462.77.
    r = gross_to_net(15000, **z)
    check("15000 contributions", r["contributions_from_salary"], "2391.60")
    check("15000 tax", r["tax"], "3462.77")
    check("15000 net", r["net"], "9145.63")
    check("15000 health uncapped", r["employer_health"], "2475.00")

    # 6. Two children: odbitak 600 x (1 + 0.5 + 0.7) = 1,320 > income 1,200 -> no tax.
    r = gross_to_net(1500, children=2, **z)
    check("1500 2 kids tax", r["tax"], "0.00")
    check("1500 2 kids net", r["net"], "1200.00")
    check("odbitak 3 kids", personal_deduction(D("600"), children=3)[0], "1920.00")

    # 7. Youth under 25: expected refund equals the lower-rate tax (138), net unchanged.
    r = gross_to_net(1500, youth="under25", **z)
    check("youth refund", r["expected_annual_refund_for_month"], "138.00")
    check("youth net unchanged", r["net"], "1062.00")
    r = gross_to_net(1500, youth="26-30", apply_reliefs_monthly=True, **z)
    check("youth 26-30 monthly net", r["net"], "1131.00")

    # 8. Net -> gross: 1,062 Zagreb -> 1,500; 1,200 Zagreb -> 1,724.02 (MIO 258.60 + 86.20, tax 179.22).
    check("n2g 1062", net_to_gross(1062, **z)["gross"], "1500.00")
    check("n2g 1200", net_to_gross(1200, **z)["gross"], "1724.02")

    # 9. Rijeka 20/25 at 6,000 gross: income 4,800; base 4,200 x 20 % = 840; net 3,960.
    lo, hi, _ = resolve_rates("Rijeka", None, None)
    check("rijeka net", gross_to_net(6000, lower=lo, higher=hi)["net"], "3960.00")

    failed = [c for c in cases if not c[1]]
    for name, ok, got, exp in cases:
        print("%s  %-26s got %-10s expected %s" % ("PASS" if ok else "FAIL", name, got, exp))
    print("%d/%d checks passed" % (len(cases) - len(failed), len(cases)))
    return 0 if not failed else 1


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Croatian salary calculator, %d rules. ESTIMATE ONLY - not tax advice." % RULE_YEAR)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--gross", type=str, help="monthly gross (bruto 1) in EUR")
    g.add_argument("--net", type=str, help="target monthly net in EUR (neto -> bruto)")
    ap.add_argument("--city", help="city from the built-in 2026 table (e.g. zagreb, split, rijeka)")
    ap.add_argument("--lower", type=str, help="lower income-tax rate in %% (e.g. 20)")
    ap.add_argument("--higher", type=str, help="higher income-tax rate in %% (e.g. 30)")
    ap.add_argument("--children", type=int, default=0, help="number of dependent children")
    ap.add_argument("--dependants", type=int, default=0, help="other dependent family members (0.5 each)")
    ap.add_argument("--disabled", type=int, default=0, help="persons with disability (0.3 each)")
    ap.add_argument("--disabled100", type=int, default=0, help="persons with 100 %% disability / care allowance (1.0 each)")
    ap.add_argument("--pillar1-only", action="store_true", help="worker only in MIO pillar I (20 %%)")
    ap.add_argument("--no-mio-relief", action="store_true", help="do not apply the MIO I base reduction")
    ap.add_argument("--youth", choices=["under25", "26-30"], help="youth relief estimate (ZPD cl. 45 st. 2)")
    ap.add_argument("--assisted-area", action="store_true", help="residence in assisted area group I / Vukovar (50 %%)")
    ap.add_argument("--apply-reliefs-monthly", action="store_true", help="include youth/area relief in monthly net (VERIFY)")
    ap.add_argument("--health-exempt", action="store_true", help="no employer health contribution (VERIFY eligibility)")
    ap.add_argument("--list-cities", action="store_true", help="print the built-in city table")
    ap.add_argument("--json", action="store_true", help="JSON output")
    ap.add_argument("--self-test", action="store_true", help="run the hand-checked test cases")
    a = ap.parse_args(argv)

    if a.self_test:
        return self_test()
    if a.list_cities:
        print("2026 income-tax rates (lower/higher %%), source: Porezna uprava table via RRiF:")
        for k in sorted(CITY_RATES_2026):
            print("  %-16s %s / %s" % (k, *CITY_RATES_2026[k]))
        print("Other municipalities: see porezna-uprava.gov.hr; default without a decision is 20/30 %.")
        return 0
    if a.gross is None and a.net is None:
        ap.error("give --gross or --net (or --self-test)")

    try:
        lo, hi, place = resolve_rates(a.city, a.lower, a.higher)
        kw = dict(lower=lo, higher=hi, children=a.children, dependants=a.dependants,
                  disabled=a.disabled, disabled100=a.disabled100, pillar1_only=a.pillar1_only,
                  no_mio_relief=a.no_mio_relief, youth=a.youth, assisted_area=a.assisted_area,
                  apply_reliefs_monthly=a.apply_reliefs_monthly, health_exempt=a.health_exempt)
        if a.gross is not None:
            res, mode = gross_to_net(D(a.gross.replace(",", ".")), **kw), "bruto -> neto"
        else:
            res, mode = net_to_gross(D(a.net.replace(",", ".")), **kw), "neto -> bruto"
    except (ValueError, ArithmeticError) as e:
        print("error: %s" % e, file=sys.stderr)
        return 2

    if a.json:
        out = to_jsonable(res)
        out["mode"] = mode
        out["rates_source"] = place
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print_report(res, place, mode)
    return 0


if __name__ == "__main__":
    sys.exit(main())
