# Contributing and skill conventions

Every skill in this plugin follows the rules below. They exist so the plugin stays
accurate, safe to publish, and consistent from one skill to the next.

## 1. Layout

```
skills/<skill-name>/
├── SKILL.md              # required, ideally under ~400 lines
├── references/*.md       # long material, loaded only when needed
├── scripts/*.py          # optional, Python 3 standard library only
└── assets/*              # optional templates, data files
```

- Skill names are kebab-case. Croatia-specific skills use the `hr-` prefix
  (`croatian-language` is the exception).
- Inside the plugin a skill is invoked as `croatia:<skill-name>`.

## 2. SKILL.md frontmatter

```yaml
---
name: hr-example
description: >-
  What the skill does and, above all, WHEN to use it: concrete trigger phrases
  in English AND Croatian (e.g. "OIB", "porez na dohodak", "payroll"), and file
  or project signals. Max ~1,000 characters. Third person or imperative.
---
```

The description is what makes Claude pick the skill, so it must contain the
words people actually type, in both languages.

## 3. Body of SKILL.md

1. One-paragraph purpose and a **status line**: `Status: researched YYYY-MM-DD.`
2. The disclaimer block (section 5) if the skill is in a regulated area.
3. "How to use": the steps Claude follows, and which reference to load for what
   (a table with grep hints works well).
4. The short list of rules or facts that cover most cases.
5. "Keeping current": which facts go stale, and the official source to check.

Put detail in `references/` and tell Claude when to read each file.

## 4. Accuracy

- Every legal, tax or numeric claim cites its source: act + article
  (e.g. "ZZP čl. 81.a", "Zakon o porezu na dohodak čl. 24") or an official URL
  (narodne-novine.nn.hr, zakon.hr, porezna-uprava.gov.hr, gov.hr, hzzo.hr,
  mirovinsko.hr, fina.hr, azop.hr, hnb.hr, dzs.hr, ihjj.hr / pravopis.hr …).
- Write amounts with the year they apply to ("2026: …"). Never present an old
  figure as current.
- Mark anything not confirmed against a primary source, or still changing, with
  **VERIFY** and say what to check and where.
- Do not invent facts, numbers, brands, article numbers or URLs. If research
  could not confirm something, say so.

## 5. Disclaimers (mandatory for regulated topics)

Skills about law, tax, payroll, accounting, fiscalization, real estate, tourism
regulation or grants MUST:

1. Include this block near the top of SKILL.md:

   > **Not legal, tax or financial advice.** This skill provides general,
   > research-based information that may be incomplete or out of date. Always
   > verify with the official sources cited and consult a qualified professional
   > (lawyer / odvjetnik, tax adviser / porezni savjetnik, accountant /
   > računovođa) before acting.

2. Instruct Claude to **end every answer that touches these topics** with a
   one-line disclaimer in the user's language:
   - EN: *This is general information, not legal or tax advice. Check the cited sources and consult a professional.*
   - HR: *Ovo su opće informacije, a ne pravni ni porezni savjet. Provjerite navedene izvore i posavjetujte se sa stručnjakom.*
3. Instruct Claude to start every generated document, template or calculation
   output (policy, contract, terms, payslip estimate, invoice logic) with:
   - HR: `PREDLOŽAK – nije pravni savjet. Prilagodite ga svom slučaju i dajte ga na provjeru stručnjaku.`
   - EN: `TEMPLATE – not legal advice. Adapt it to your case and have it reviewed by a professional.`
   Every template file in `assets/` starts with this line too.

Calculators (scripts) print an "estimate only" notice in their output.

## 6. No personal or project-specific content

This repository is public. Skills must not contain:

- names of real private projects, products, clients or companies used as
  examples, people's names, e-mail addresses, OIBs, IBANs or addresses
  (use clearly fake examples: "Primjer d.o.o.", `ana.horvat@primjer.hr`,
  a checksum-valid but fictitious OIB marked as an example);
- references to skills that are not part of this plugin (no "use the X skill"
  for outside skills). Generic phrasing is fine: "if an SEO tool is available";
- "the owner prefers …" rules. A house style is configurable: tell Claude to
  follow the project's own conventions (CLAUDE.md, existing content) when they
  are allowed by the standard, and otherwise to follow the standard;
- instructions to edit the skill's own files at runtime. Plugin files are
  replaced on update. Anything a skill should remember per project goes in the
  user's project, e.g. `.claude/croatia/<skill>.md`.

Well-known public brands, institutions and companies may be named as facts.

## 7. Scripts

- Python 3, standard library only, runnable as `python3 scripts/x.py --help`.
- Deterministic, no network access unless the script's purpose is a lookup and
  it says so.
- Include a self-test (`--self-test`) or a `tests/` file, and make sure it passes.
- Calculators print the year/rules they implement and an "estimate only" line.

## 8. Language

- Skill instructions are written in English (wider audience), except where the
  content is about Croatian itself.
- Every Croatian sentence in a skill must be correct standard Croatian: ijekavica,
  no Serbian forms, no calques, and the polite capital **Vi/Vaš/Vam** when one
  person is addressed (lower-case **vi/vaš** only for several people). Apply the
  `croatia:croatian-language` skill.
- Croatian legal and official terms are given in Croatian with an English gloss
  the first time ("voditelj obrade (controller)").
