#!/usr/bin/env python3
"""Croatian public holidays, working days and deadline arithmetic.

Python 3 standard library only. Deterministic, no network access.

Rules implemented (researched 2026-10-25):
  * Public holidays (blagdani i neradni dani): Zakon o blagdanima, spomendanima
    i neradnim danima u Republici Hrvatskoj, NN 110/19, 72/25, cl. 1.
    In force since 1 Jan 2020; years before 2020 are refused (old list differs).
  * A holiday falling on a Sunday is NOT moved to another day (cl. 4).
  * Religious days off for believers only (cl. 3): 7 Jan (Orthodox Christmas),
    Orthodox (Julian) Easter Monday; Bajram / Jewish holidays are not computed.
  * Memorial days (spomendani, cl. 2 as amended by NN 72/25) are NOT days off.
  * Working day (radni dan) = Monday-Friday that is not a public holiday.
  * Procedural deadlines:
      zup  - Zakon o opcem upravnom postupku (NN 47/09, 110/21) cl. 80-81:
             the day of service is not counted; if the last day is a Sunday,
             a holiday or another day the authority does not work, the deadline
             ends on the next working day. Saturdays are treated as closed days
             by default (public authorities do not work on Saturdays).
             Tax procedure: Opci porezni zakon cl. 4 refers to ZUP.
      zpp  - Zakon o parnicnom postupku cl. 112 st. 2 and 4: same logic
             ("drzavni blagdan, nedjelja ili koji drugi dan kad sud ne radi").
      zoo  - Zakon o obveznim odnosima cl. 300 st. 1 and 3 (contracts): only a
             day on which "zakonom je odredeno da se ne radi" rolls forward.
             Implemented as Sundays + public holidays (Saturday does not roll).
  * Interbank payment days: EuroNKS follows TARGET; closed on Saturdays,
    Sundays, 1 Jan, Good Friday, Easter Monday, 1 May, 25 Dec, 26 Dec.
    Other Croatian holidays are EuroNKS working days (Fina EuroNKS rules).
    Instant payments run every calendar day.

Usage examples:
  python3 hr_calendar.py holidays 2026
  python3 hr_calendar.py holidays 2026 --json
  python3 hr_calendar.py holidays 2026 --to 2028 --ics > blagdani.ics
  python3 hr_calendar.py is-working-day 2026-06-04
  python3 hr_calendar.py working-days 2026-01-01 2026-12-31
  python3 hr_calendar.py add-working-days 2026-12-23 3
  python3 hr_calendar.py easter 2027 [--julian]
  python3 hr_calendar.py deadline 2026-12-10 15 [--rule zup|zpp|zoo] [--unit days|months|years]
  python3 hr_calendar.py is-payment-day 2026-04-03
  python3 hr_calendar.py --self-test
"""

import argparse
import calendar
import datetime as dt
import json
import sys

FIRST_SUPPORTED_YEAR = 2020  # current holiday list in force since 1 Jan 2020
LAW = ("Zakon o blagdanima, spomendanima i neradnim danima u Republici Hrvatskoj "
       "(NN 110/19, 72/25)")
NOTICE = ("Estimate only - general information, not legal or tax advice. "
          "Check the cited sources and consult a professional.")

WEEKDAYS_HR = ["ponedjeljak", "utorak", "srijeda", "četvrtak", "petak",
               "subota", "nedjelja"]
WEEKDAYS_EN = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
               "Saturday", "Sunday"]
MONTHS_HR = ["siječanj", "veljača", "ožujak", "travanj", "svibanj", "lipanj",
             "srpanj", "kolovoz", "rujan", "listopad", "studeni", "prosinac"]
# Genitive form used in dates: "1. siječnja 2026."
MONTHS_HR_GEN = ["siječnja", "veljače", "ožujka", "travnja", "svibnja",
                 "lipnja", "srpnja", "kolovoza", "rujna", "listopada",
                 "studenoga", "prosinca"]


# ---------------------------------------------------------------- Easter ---

def easter_gregorian(year):
    """Western (Gregorian) Easter Sunday, anonymous Gregorian / Meeus algorithm."""
    a = year % 19
    b, c = divmod(year, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month, day = divmod(h + l - 7 * m + 114, 31)
    return dt.date(year, month, day + 1)


def easter_julian(year):
    """Orthodox Easter Sunday (Julian computus, Meeus), as a Gregorian date."""
    a, b, c = year % 4, year % 7, year % 19
    d = (19 * c + 15) % 30
    e = (2 * a + 4 * b - d + 34) % 7
    month, day = divmod(d + e + 114, 31)
    julian = dt.date(year, month, day + 1)
    # Julian -> Gregorian offset: 13 days for 1900-03-01 .. 2100-02-28.
    if not 1900 <= year <= 2099:
        raise ValueError("Julian Easter conversion implemented for 1900-2099 only")
    return julian + dt.timedelta(days=13)


# -------------------------------------------------------------- holidays ---

def _check_year(year):
    if year < FIRST_SUPPORTED_YEAR:
        raise ValueError(
            "Years before %d used a different holiday list (old law NN 33/96 ... "
            "130/11, e.g. 25 June and 8 October were holidays). Not supported."
            % FIRST_SUPPORTED_YEAR)
    if year > 2099:
        raise ValueError("Year out of supported range (2020-2099)")


def holidays(year):
    """Return list of dicts for public holidays (cl. 1) in `year`, sorted."""
    _check_year(year)
    e = easter_gregorian(year)
    D = dt.date
    items = [
        (D(year, 1, 1), "Nova godina", "New Year's Day"),
        (D(year, 1, 6), "Bogojavljenje ili Sveta tri kralja", "Epiphany"),
        (e, "Uskrs", "Easter Sunday"),
        (e + dt.timedelta(days=1), "Uskrsni ponedjeljak", "Easter Monday"),
        (D(year, 5, 1), "Praznik rada", "Labour Day"),
        (D(year, 5, 30), "Dan državnosti", "Statehood Day"),
        (e + dt.timedelta(days=60), "Tijelovo", "Corpus Christi"),
        (D(year, 6, 22), "Dan antifašističke borbe", "Anti-Fascist Struggle Day"),
        (D(year, 8, 5), "Dan pobjede i domovinske zahvalnosti i Dan hrvatskih branitelja",
         "Victory and Homeland Thanksgiving Day and Day of Croatian Defenders"),
        (D(year, 8, 15), "Velika Gospa", "Assumption of Mary"),
        (D(year, 11, 1), "Svi sveti", "All Saints' Day"),
        (D(year, 11, 18),
         "Dan sjećanja na žrtve Domovinskog rata i Dan sjećanja na žrtvu Vukovara i Škabrnje",
         "Remembrance Day for the Victims of the Homeland War and for Vukovar and Škabrnja"),
        (D(year, 12, 25), "Božić", "Christmas Day"),
        (D(year, 12, 26), "Sveti Stjepan", "St Stephen's Day"),
    ]
    out = [dict(date=d, name_hr=hr, name_en=en, kind="holiday",
                source=LAW + ", čl. 1") for d, hr, en in items]
    out.sort(key=lambda x: x["date"])
    return out


def religious_days(year):
    """Days off only for believers of the given faith (cl. 3). Computable ones."""
    _check_year(year)
    oe = easter_julian(year)
    note = "only for believers who celebrate it (" + LAW + ", čl. 3)"
    return [
        dict(date=dt.date(year, 1, 7), name_hr="Božić (pravoslavni)",
             name_en="Orthodox Christmas", kind="religious", source=note),
        dict(date=oe + dt.timedelta(days=1),
             name_hr="Uskrsni ponedjeljak (pravoslavni)",
             name_en="Orthodox Easter Monday", kind="religious", source=note),
    ]


def _nearest_weekend_to_may15(year):
    d = dt.date(year, 5, 15)
    wd = d.weekday()
    if wd >= 5:
        return d, False
    back = wd + 1           # distance to previous Sunday
    fwd = 5 - wd            # distance to next Saturday
    if back < fwd:
        return d - dt.timedelta(days=back), False
    if fwd < back:
        return d + dt.timedelta(days=fwd), False
    return d - dt.timedelta(days=back), True  # Wednesday: equidistant, ambiguous


def memorial_days(year):
    """Spomendani (cl. 2, NN 72/25). Working days - NOT days off."""
    _check_year(year)
    D = dt.date
    src = LAW + ", čl. 2 (list as amended by NN 72/25; not days off)"
    rows = [
        (D(year, 1, 9), "Dan sjedinjenja Međimurja s maticom zemljom Hrvatskom"),
        (D(year, 1, 15), "Dan međunarodnoga priznanja Republike Hrvatske i Dan mirne "
                         "reintegracije hrvatskog Podunavlja"),
        (D(year, 3, 15), "Dan osnivanja Narodne zaštite"),
        (D(year, 4, 30), "Dan pogibije Zrinskog i Frankopana"),
        (D(year, 5, 3), "Dan sjećanja na ubijenu i stradalu djecu u Domovinskom ratu"),
        (D(year, 5, 9), "Dan Europe i Dan pobjede nad fašizmom"),
        (D(year, 6, 25), "Dan neovisnosti"),
        (D(year, 8, 23), "Europski dan sjećanja na žrtve totalitarnih i autoritarnih "
                         "režima – nacizma, fašizma i komunizma"),
        (D(year, 8, 30), "Dan sjećanja na nestale osobe u Domovinskom ratu"),
        (D(year, 9, 25), "Dan donošenja Odluke o sjedinjenju Istre, Rijeke, Zadra i "
                         "otoka s maticom zemljom Hrvatskom"),
        (D(year, 10, 8), "Dan Hrvatskoga sabora"),
    ]
    d15, ambiguous = _nearest_weekend_to_may15(year)
    name = "Dan spomena na hrvatske žrtve u borbi za slobodu i nezavisnost"
    if ambiguous:
        name += " (VERIFY: 15 May is a Wednesday, Sat 18 and Sun 12 are equidistant)"
    rows.append((d15, name))
    out = [dict(date=d, name_hr=n, name_en="", kind="memorial", source=src)
           for d, n in rows]
    out.sort(key=lambda x: x["date"])
    return out


_HOLIDAY_CACHE = {}


def holiday_map(year):
    if year not in _HOLIDAY_CACHE:
        _HOLIDAY_CACHE[year] = {h["date"]: h for h in holidays(year)}
    return _HOLIDAY_CACHE[year]


def is_holiday(d):
    return d in holiday_map(d.year)


def is_working_day(d, saturday_working=False):
    if d.weekday() == 6:
        return False
    if d.weekday() == 5 and not saturday_working:
        return False
    return not is_holiday(d)


def count_working_days(start, end, saturday_working=False):
    """Inclusive count of working days between start and end."""
    if end < start:
        start, end = end, start
    n, d = 0, start
    one = dt.timedelta(days=1)
    while d <= end:
        if is_working_day(d, saturday_working):
            n += 1
        d += one
    return n


def add_working_days(start, n, saturday_working=False):
    """Date that is n working days after (n<0: before) start; start not counted."""
    step = dt.timedelta(days=1 if n >= 0 else -1)
    d, left = start, abs(n)
    if left == 0:
        while not is_working_day(d, saturday_working):
            d += dt.timedelta(days=1)
        return d
    while left:
        d += step
        if is_working_day(d, saturday_working):
            left -= 1
    return d


# ------------------------------------------------------------- deadlines ---

RULES = {
    "zup": dict(
        saturday_closed=True,
        source="Zakon o općem upravnom postupku (NN 47/09, 110/21) čl. 80 st. 2 "
               "i čl. 81 st. 2; tax procedure via Opći porezni zakon čl. 4"),
    "zpp": dict(
        saturday_closed=True,
        source="Zakon o parničnom postupku čl. 112 st. 2 i 4"),
    "zoo": dict(
        saturday_closed=False,
        source="Zakon o obveznim odnosima čl. 300 st. 1 i 3"),
}


def add_months(d, months):
    y, m = divmod(d.month - 1 + months, 12)
    y += d.year
    m += 1
    last = calendar.monthrange(y, m)[1]
    return dt.date(y, m, min(d.day, last))


def deadline(trigger, amount, rule="zup", unit="days", saturday_closed=None):
    """Return (raw_end, final_end, rolled_over_days list).

    trigger = day of service / event; it is not counted (ZUP čl. 80 st. 2,
    ZPP čl. 112 st. 2, ZOO čl. 300 st. 1).
    """
    cfg = RULES[rule]
    sat_closed = cfg["saturday_closed"] if saturday_closed is None else saturday_closed
    if unit == "days":
        raw = trigger + dt.timedelta(days=amount)
    elif unit == "months":
        raw = add_months(trigger, amount)
    elif unit == "years":
        raw = add_months(trigger, 12 * amount)
    else:
        raise ValueError("unit must be days, months or years")
    end, skipped = raw, []
    while end.weekday() == 6 or is_holiday(end) or (sat_closed and end.weekday() == 5):
        skipped.append(end)
        end += dt.timedelta(days=1)
    return raw, end, skipped


# --------------------------------------------------------- payment days ---

def target_closed_days(year):
    e = easter_gregorian(year)
    return {
        dt.date(year, 1, 1): "Nova godina",
        e - dt.timedelta(days=2): "Veliki petak (Good Friday)",
        e + dt.timedelta(days=1): "Uskrsni ponedjeljak",
        dt.date(year, 5, 1): "Praznik rada",
        dt.date(year, 12, 25): "Božić",
        dt.date(year, 12, 26): "Sveti Stjepan",
    }


def is_payment_day(d):
    if d.weekday() >= 5:
        return False, "weekend"
    closed = target_closed_days(d.year)
    if d in closed:
        return False, "TARGET/EuroNKS closing day: " + closed[d]
    return True, ""


# ------------------------------------------------------------ formatting ---

def fmt_hr(d):
    return "%d. %s %d." % (d.day, MONTHS_HR_GEN[d.month - 1], d.year)


def parse_date(s):
    s = s.strip()
    for f in ("%Y-%m-%d", "%d.%m.%Y.", "%d.%m.%Y"):
        try:
            return dt.datetime.strptime(s.replace(" ", ""), f).date()
        except ValueError:
            pass
    raise argparse.ArgumentTypeError("invalid date %r (use YYYY-MM-DD or D.M.YYYY.)" % s)


def _ics_escape(text):
    return (text.replace("\\", "\\\\").replace(";", "\\;")
            .replace(",", "\\,").replace("\n", "\\n"))


def _ics_fold(line):
    """Fold to max 75 octets per RFC 5545 without splitting UTF-8 sequences."""
    out, cur, cur_len = [], "", 0
    for ch in line:
        n = len(ch.encode("utf-8"))
        limit = 75 if not out else 74  # continuation lines start with a space
        if cur_len + n > limit:
            out.append(cur)
            cur, cur_len = "", 0
        cur += ch
        cur_len += n
    out.append(cur)
    return "\r\n ".join(out)


def _slug(text):
    keep = "abcdefghijklmnopqrstuvwxyz0123456789"
    tr = str.maketrans("čćžšđ", "cczsd")
    s = text.lower().translate(tr)
    return "".join(c if c in keep else "-" for c in s).strip("-")[:40]


def to_ics(rows, calname):
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0",
             "PRODID:-//croatia plugin//hr-calendar//HR",
             "CALSCALE:GREGORIAN", "METHOD:PUBLISH",
             "X-WR-CALNAME:" + _ics_escape(calname),
             "X-WR-TIMEZONE:Europe/Zagreb"]
    for r in rows:
        d = r["date"]
        uid = "%s-%s@hr-calendar.croatia-plugin" % (d.strftime("%Y%m%d"), _slug(r["name_hr"]))
        summary = r["name_hr"]
        desc = r["source"]
        if r.get("name_en"):
            desc = r["name_en"] + ". " + desc
        lines += [
            "BEGIN:VEVENT",
            "UID:" + uid,
            "DTSTAMP:%04d0101T000000Z" % d.year,  # deterministic
            "DTSTART;VALUE=DATE:" + d.strftime("%Y%m%d"),
            "DTEND;VALUE=DATE:" + (d + dt.timedelta(days=1)).strftime("%Y%m%d"),
            "SUMMARY:" + _ics_escape(summary),
            "DESCRIPTION:" + _ics_escape(desc),
            "CATEGORIES:" + {"holiday": "Blagdan", "religious": "Vjerski blagdan",
                             "memorial": "Spomendan"}[r["kind"]],
            "TRANSP:TRANSPARENT",
            "END:VEVENT",
        ]
    lines.append("END:VCALENDAR")
    return "\r\n".join(_ics_fold(l) for l in lines) + "\r\n"


def _collect(year, to_year, religious, memorial):
    rows = []
    for y in range(year, (to_year or year) + 1):
        rows += holidays(y)
        if religious:
            rows += religious_days(y)
        if memorial:
            rows += memorial_days(y)
    rows.sort(key=lambda r: (r["date"], r["kind"]))
    return rows


# ------------------------------------------------------------------ CLI ---

def cmd_holidays(a):
    rows = _collect(a.year, a.to, a.religious, a.memorial)
    if a.ics:
        span = str(a.year) if not a.to or a.to == a.year else "%d-%d" % (a.year, a.to)
        sys.stdout.buffer.write(to_ics(rows, "Blagdani i neradni dani RH " + span)
                                .encode("utf-8"))
        print(NOTICE, file=sys.stderr)
        return 0
    if a.json:
        data = [dict(date=r["date"].isoformat(), weekday_hr=WEEKDAYS_HR[r["date"].weekday()],
                     weekday_en=WEEKDAYS_EN[r["date"].weekday()], name_hr=r["name_hr"],
                     name_en=r["name_en"], kind=r["kind"],
                     day_off=r["kind"] == "holiday", source=r["source"]) for r in rows]
        print(json.dumps(data, ensure_ascii=False, indent=2))
        print(NOTICE, file=sys.stderr)
        return 0
    print("Rules: " + LAW + ", čl. 1-4 (in force 2020+; Sunday holidays are not moved).")
    for r in rows:
        d = r["date"]
        tag = {"holiday": "", "religious": "  [believers only, čl. 3]",
               "memorial": "  [spomendan, not a day off]"}[r["kind"]]
        en = (" (%s)" % r["name_en"]) if r["name_en"] else ""
        print("%s  %-11s %s%s%s" % (d.isoformat(), WEEKDAYS_HR[d.weekday()], r["name_hr"], en, tag))
    wd = [r for r in rows if r["kind"] == "holiday" and r["date"].weekday() < 5]
    print("Holidays on Mon-Fri: %d" % len(wd))
    print(NOTICE)
    return 0


def cmd_is_working_day(a):
    d = a.date
    ok = is_working_day(d, a.saturday_working)
    reason = ""
    if is_holiday(d):
        reason = "public holiday: " + holiday_map(d.year)[d]["name_hr"]
    elif d.weekday() == 6:
        reason = "Sunday"
    elif d.weekday() == 5 and not a.saturday_working:
        reason = "Saturday (not counted as a working day by default)"
    print("%s (%s): %s%s" % (d.isoformat(), WEEKDAYS_HR[d.weekday()],
                             "working day" if ok else "NOT a working day",
                             (" - " + reason) if reason else ""))
    return 0 if ok else 1


def cmd_working_days(a):
    n = count_working_days(a.start, a.end, a.saturday_working)
    days = "Mon-Sat" if a.saturday_working else "Mon-Fri"
    print("%d working days (%s, excluding public holidays) from %s to %s inclusive"
          % (n, days, a.start.isoformat(), a.end.isoformat()))
    lo, hi = sorted((a.start, a.end))
    hol = 0
    d = lo
    while d <= hi:
        if is_holiday(d) and (d.weekday() < 5 or (a.saturday_working and d.weekday() == 5)):
            hol += 1
        d += dt.timedelta(days=1)
    print("Working hours (8 h/day): %d; holidays on working weekdays: %d (%d h); "
          "fond sati (working + paid holiday hours): %d" % (n * 8, hol, hol * 8, (n + hol) * 8))
    print(NOTICE)
    return 0


def cmd_add_working_days(a):
    d = add_working_days(a.date, a.n, a.saturday_working)
    print("%s (%s, %s)" % (d.isoformat(), WEEKDAYS_HR[d.weekday()], fmt_hr(d)))
    return 0


def cmd_easter(a):
    if a.julian:
        e = easter_julian(a.year)
        print("Orthodox Easter %d: %s (%s); Orthodox Easter Monday %s"
              % (a.year, e.isoformat(), fmt_hr(e), (e + dt.timedelta(days=1)).isoformat()))
        return 0
    e = easter_gregorian(a.year)
    print("Uskrs (Easter Sunday) %d: %s (%s)" % (a.year, e.isoformat(), fmt_hr(e)))
    print("Veliki petak (Good Friday, not a public holiday): %s"
          % (e - dt.timedelta(days=2)).isoformat())
    print("Uskrsni ponedjeljak (Easter Monday): %s" % (e + dt.timedelta(days=1)).isoformat())
    print("Tijelovo (Corpus Christi = Easter + 60): %s" % (e + dt.timedelta(days=60)).isoformat())
    return 0


def cmd_deadline(a):
    sat = None
    if a.saturday_open:
        sat = False
    raw, end, skipped = deadline(a.date, a.amount, a.rule, a.unit, sat)
    print("Rule: " + RULES[a.rule]["source"])
    print("Trigger (service/event) day %s is not counted; %d %s -> %s (%s)"
          % (a.date.isoformat(), a.amount, a.unit, raw.isoformat(), WEEKDAYS_HR[raw.weekday()]))
    if skipped:
        print("Last day falls on non-working day(s): " +
              ", ".join("%s %s" % (s.isoformat(), WEEKDAYS_HR[s.weekday()]) for s in skipped))
    print("Deadline ends: %s (%s, %s)" % (end.isoformat(), WEEKDAYS_HR[end.weekday()], fmt_hr(end)))
    print("Check special rules: some laws define their own computation, substantive "
          "(material) deadlines may not roll over, and filing by registered post counts "
          "on the day of posting in many procedures.")
    print(NOTICE)
    return 0


def cmd_is_payment_day(a):
    ok, why = is_payment_day(a.date)
    print("%s (%s): %s%s" % (a.date.isoformat(), WEEKDAYS_HR[a.date.weekday()],
                             "interbank (EuroNKS/TARGET) settlement day" if ok
                             else "NO regular interbank settlement",
                             (" - " + why) if why else ""))
    if is_holiday(a.date) and ok:
        print("Note: Croatian public holiday, but EuroNKS/TARGET operate; bank branches "
              "may be closed.")
    print("Instant payments (SCT Inst) settle every calendar day.")
    return 0 if ok else 1


# ------------------------------------------------------------ self-test ---

def self_test():
    D = dt.date
    greg = {2000: D(2000, 4, 23), 2008: D(2008, 3, 23), 2011: D(2011, 4, 24),
            2019: D(2019, 4, 21), 2024: D(2024, 3, 31), 2025: D(2025, 4, 20),
            2026: D(2026, 4, 5), 2027: D(2027, 3, 28), 2028: D(2028, 4, 16),
            2029: D(2029, 4, 1), 2030: D(2030, 4, 21), 2038: D(2038, 4, 25),
            2285: D(2285, 3, 22)}
    for y, d in greg.items():
        assert easter_gregorian(y) == d, (y, easter_gregorian(y))
    jul = {2024: D(2024, 5, 5), 2025: D(2025, 4, 20), 2026: D(2026, 4, 12),
           2027: D(2027, 5, 2), 2028: D(2028, 4, 16), 2029: D(2029, 4, 8),
           2030: D(2030, 4, 28)}
    for y, d in jul.items():
        assert easter_julian(y) == d, (y, easter_julian(y))
    # Corpus Christi, spot-checked against published Croatian calendars.
    cc = {2025: D(2025, 6, 19), 2026: D(2026, 6, 4), 2027: D(2027, 5, 27),
          2028: D(2028, 6, 15), 2029: D(2029, 5, 31), 2030: D(2030, 6, 20)}
    for y, d in cc.items():
        assert any(h["date"] == d and h["name_hr"] == "Tijelovo" for h in holidays(y)), y
    for y in range(2020, 2100):
        assert len(holidays(y)) == 14
    # Working days 2026: 261 weekdays - 9 weekday holidays = 252.
    assert count_working_days(D(2026, 1, 1), D(2026, 12, 31)) == 252
    assert count_working_days(D(2025, 1, 1), D(2025, 12, 31)) == 250
    assert not is_working_day(D(2026, 6, 4))           # Tijelovo
    assert not is_working_day(D(2026, 11, 18))
    assert is_working_day(D(2026, 6, 25))              # Dan neovisnosti = spomendan
    assert is_working_day(D(2026, 10, 8))
    assert not is_working_day(D(2026, 11, 1))          # Sunday holiday, not moved
    assert is_working_day(D(2026, 11, 2))              # ... so Monday is a working day
    assert add_working_days(D(2026, 12, 23), 1) == D(2026, 12, 24)
    assert add_working_days(D(2026, 12, 24), 1) == D(2026, 12, 28)
    assert add_working_days(D(2026, 12, 28), -1) == D(2026, 12, 24)
    assert add_working_days(D(2026, 12, 26), 0) == D(2026, 12, 28)
    # Deadlines
    raw, end, sk = deadline(D(2026, 12, 10), 15, "zup")
    assert raw == D(2026, 12, 25) and end == D(2026, 12, 28) and len(sk) == 3
    assert deadline(D(2026, 10, 3), 14, "zup")[1] == D(2026, 10, 19)   # Sat rolls
    assert deadline(D(2026, 10, 3), 14, "zoo")[1] == D(2026, 10, 17)   # Sat does not
    assert deadline(D(2026, 10, 3), 14, "zup", saturday_closed=False)[1] == D(2026, 10, 17)
    assert deadline(D(2026, 1, 31), 1, "zup", "months")[1] == D(2026, 3, 2)  # 28.2. Sat
    assert deadline(D(2026, 3, 31), 1, "zoo", "months")[1] == D(2026, 4, 30)
    assert deadline(D(2026, 5, 20), 10, "zpp")[1] == D(2026, 6, 1)     # 30.5. Sat holiday
    # Payment days
    assert is_payment_day(D(2026, 4, 3))[0] is False                  # Good Friday
    assert is_payment_day(D(2026, 6, 4))[0] is True                   # Tijelovo: EuroNKS open
    assert is_payment_day(D(2026, 5, 1))[0] is False
    # Memorial day nearest weekend to 15 May
    assert _nearest_weekend_to_may15(2026)[0] == D(2026, 5, 16)       # 15.5.2026 Fri
    assert _nearest_weekend_to_may15(2027)[0] == D(2027, 5, 15)       # Sat
    assert _nearest_weekend_to_may15(2030)[1] is True                 # Wed: ambiguous
    # Old years refused
    try:
        holidays(2019)
        raise AssertionError("2019 should be refused")
    except ValueError:
        pass
    # ICS sanity
    ics = to_ics(_collect(2026, None, True, True), "Test")
    assert ics.startswith("BEGIN:VCALENDAR\r\n") and ics.endswith("END:VCALENDAR\r\n")
    assert ics.count("BEGIN:VEVENT") == 14 + 2 + 12
    for line in ics.split("\r\n"):
        assert len(line.encode("utf-8")) <= 75, line
    assert "DTSTART;VALUE=DATE:20260604" in ics
    assert parse_date("4.6.2026.") == D(2026, 6, 4)
    print("self-test OK (Easter 13 yrs, Orthodox Easter 7 yrs, Corpus Christi 2025-2030, "
          "working days 2025/2026, deadlines, payment days, ICS)")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Croatian public holidays, working days and deadlines "
                    "(rules researched 2026-10-25). " + NOTICE)
    p.add_argument("--self-test", action="store_true", help="run built-in tests")
    sub = p.add_subparsers(dest="cmd")

    s = sub.add_parser("holidays", help="list public holidays for a year")
    s.add_argument("year", type=int)
    s.add_argument("--to", type=int, help="last year of a range (inclusive)")
    s.add_argument("--religious", action="store_true",
                   help="add čl. 3 days off for believers (Orthodox Christmas, Orthodox Easter Monday)")
    s.add_argument("--memorial", action="store_true", help="add spomendani (not days off)")
    g = s.add_mutually_exclusive_group()
    g.add_argument("--json", action="store_true")
    g.add_argument("--ics", action="store_true", help="iCalendar output (RFC 5545)")
    s.set_defaults(func=cmd_holidays)

    sat_help = "count Saturdays as working days (6-day week)"
    s = sub.add_parser("is-working-day", help="exit code 0 if working day, 1 if not")
    s.add_argument("date", type=parse_date)
    s.add_argument("--saturday-working", action="store_true", help=sat_help)
    s.set_defaults(func=cmd_is_working_day)

    s = sub.add_parser("working-days", help="count working days, both ends inclusive")
    s.add_argument("start", type=parse_date)
    s.add_argument("end", type=parse_date)
    s.add_argument("--saturday-working", action="store_true", help=sat_help)
    s.set_defaults(func=cmd_working_days)

    s = sub.add_parser("add-working-days", help="date N working days after (or before) a date")
    s.add_argument("date", type=parse_date)
    s.add_argument("n", type=int)
    s.add_argument("--saturday-working", action="store_true", help=sat_help)
    s.set_defaults(func=cmd_add_working_days)

    s = sub.add_parser("easter", help="Easter and movable feasts")
    s.add_argument("year", type=int)
    s.add_argument("--julian", action="store_true", help="Orthodox (Julian) Easter")
    s.set_defaults(func=cmd_easter)

    s = sub.add_parser("deadline", help="procedural deadline from a trigger date")
    s.add_argument("date", type=parse_date, help="day of service / event (not counted)")
    s.add_argument("amount", type=int)
    s.add_argument("--unit", choices=["days", "months", "years"], default="days")
    s.add_argument("--rule", choices=sorted(RULES), default="zup")
    s.add_argument("--saturday-open", action="store_true",
                   help="do not roll over a Saturday (body works on Saturdays)")
    s.set_defaults(func=cmd_deadline)

    s = sub.add_parser("is-payment-day", help="EuroNKS/TARGET interbank settlement day?")
    s.add_argument("date", type=parse_date)
    s.set_defaults(func=cmd_is_payment_day)

    a = p.parse_args(argv)
    if a.self_test:
        return self_test()
    if not a.cmd:
        p.print_help()
        return 2
    try:
        return a.func(a)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
