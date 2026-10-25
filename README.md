# croatia-skills

> **Not legal, tax or financial advice.** These skills give general,
> research-based information that may be incomplete or out of date. Always
> check the official sources they cite and consult a qualified professional.
> See [DISCLAIMER.md](DISCLAIMER.md).
>
> **Nije pravni, porezni ni financijski savjet.** Ovi skillovi daju opće
> informacije koje mogu biti nepotpune ili zastarjele. Uvijek provjerite
> navedene službene izvore i posavjetujte se sa stručnjakom.

A Claude Code plugin with skills for anything Croatian: the language, the law,
running a business, payroll, invoicing, tourism, property, grants, local SEO,
and the data formats developers meet (OIB, IBAN, HUB-3, dates, plurals,
place names).

## Install

```text
/plugin marketplace add jpavlinic/croatia-skills
/plugin install croatia@croatia-skills
```

Skills load automatically when a request matches them. You can also call one
by name, e.g. `/croatia:croatian-language`.

## Skills

| Skill | What it covers |
|---|---|
| `croatian-language` | Writing and proofreading Croatian to the IHJJ standard: grammar, spelling, Croatian vs Serbian, anglicisms, punctuation, polite **Vi**, UI text, e-mails, AI-text smells |
| `hr-legal-compliance` | GDPR/ZPDZ, cookies, e-mail marketing, consumer law (ZZP), terms, impressum, DSA, AI Act, accessibility, fiscalization basics; audits and templates; EN↔HR legal glossary |
| `hr-identifiers` | OIB, VAT ID, IBAN, MB/MBS, payment reference models (poziv na broj), HUB-3 payment slip barcode, phone and postal formats; validators and test-data generators |
| `hr-localization` | Croatian in code: dates, numbers, euro format, plural rules, collation, slugs and diacritics, name vocative, place names with u/na, addresses; framework setup |
| `hr-calendar` | Public holidays, Easter-based dates, working days, procedural deadlines, Sunday shop trading, school calendar, recurring tax and filing deadlines; `.ics` export |
| `hr-market-brands` | Current, correctly spelled Croatian retailers, banks, telecoms, delivery, payments, media and more, with dated status and common mistakes |
| `hr-fiscalization-dev` | Implementing Fiskalizacija 1.0 (B2C receipts, ZKI/JIR, QR) and Fiskalizacija 2.0 (eRačun, UBL / HR CIUS, KPD, intermediaries, eIzvještavanje) |
| `hr-business-admin` | Choosing obrt, paušalni obrt, j.d.o.o. or d.o.o.; taxes and owner contributions, VAT registration, freelancing for foreign clients, registration and closing |
| `hr-payroll-employment` | Labour law (contracts, working time, leave, termination), gross↔net salary calculator, non-taxable payments, student work, foreign workers |
| `hr-tourism-rentals` | Private accommodation: categorisation, eVisitor, tourist tax and membership fee, flat-rate tax per bed, VAT and platforms, DAC7, 2025–2027 regulation, guest templates |
| `hr-seo-local` | SEO for Croatian: inflected and diacritic-free queries, slugs, hreflang, .hr domains, Google Business Profile, local citations, AI search |
| `hr-real-estate` | Buying and selling property, land registry, taxes and costs, long-term renting, foreign buyers, apartment buildings, legalisation, energy certificates |
| `hr-eu-funding` | Finding and applying for EU and national grants (eufondovi, HZZ, HAMAG-BICRO, HBOR, FZOEU), eligibility and de minimis, application writing, compliance after award |

Several skills include small Python scripts (standard library only), for example:

```bash
python3 skills/hr-identifiers/scripts/hr_ids.py oib validate 12345678903
python3 skills/hr-calendar/scripts/hr_calendar.py holidays 2027 --ics > blagdani-2027.ics
python3 skills/hr-payroll-employment/scripts/hr_salary.py --help
python3 skills/hr-localization/scripts/hr_text.py place Hvar
```

Every script has `--self-test`.

## How accurate is it?

- Each skill states the date it was researched and cites acts, articles and
  official URLs.
- Anything that could not be confirmed against a primary source is marked
  **VERIFY**.
- Croatian law, tax amounts and specifications change often. Skills tell Claude
  which facts go stale and where to re-check them.
- Regulated skills end every relevant answer with a one-line disclaimer and
  start every generated document with a `PREDLOŽAK – nije pravni savjet` line.

Found something wrong or outdated? Open an issue or a pull request with the
source.

## Per-project notes

Skills never edit themselves. Where a skill should remember something for a
project (accepted risks, house style, decisions), it keeps it in that project
under `.claude/croatia/`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the skill conventions: layout,
sources, disclaimers and the no-personal-data rule.

## Licence

Code: [MIT](LICENSE). Written content: [CC BY 4.0](LICENSE-CONTENT.md).
Brand names belong to their owners.
