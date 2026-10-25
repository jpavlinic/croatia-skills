---
name: hr-identifiers
description: >-
  Validate, parse, format and generate fictitious test data for Croatian identifiers and payment
  data: OIB (ISO 7064 MOD 11,10), PDV ID / VAT number HR+OIB and VIES checks, HR IBAN with bank
  codes (VBDI) and BIC/SWIFT, MB (DZS), MBS (sudski registar), MBO, legacy JMBG, poziv na broj
  models HR00-HR99 (HR01, HR68...) and check digits, HUB-3 / HUB 3A uplatnica PDF417 barcode
  payload (HRVHUB30), EPC QR, phone numbers (+385, E.164), postal codes, licence plates and
  company suffixes (d.o.o., j.d.o.o., d.d.). Use for form validation, data cleaning, payment slips,
  fixtures. Triggers: "OIB", "provjera OIB-a", "validate OIB", "generate test OIB", "IBAN",
  "poziv na broj", "model HR01", "kontrolni broj", "uplatnica", "opća uplatnica", "HUB-3", "HUB3A",
  "2D barkod", "PDF417", "PDV broj", "PDV ID", "VAT number", "VIES", "matični broj", "MBS",
  "JMBG", "telefonski broj", "poštanski broj", "registarska oznaka", "test data", "fake OIB".
---

# Croatian identifiers and payment data

Validate, parse, normalise and generate (fictitious) Croatian identifiers and payment data in
code and datasets: OIB, PDV ID, IBAN/VBDI/BIC, MB, MBS, MBO, JMBG, *poziv na broj* (payment
reference), the HUB-3 PDF417 payment-slip barcode, phone numbers, postal codes, vehicle plates
and company legal-form suffixes. Two stdlib-only Python scripts do the arithmetic; the
references hold the sourced rules.

Status: researched 2026-10-25.

> **Not legal, tax or financial advice.** This skill provides general,
> research-based information that may be incomplete or out of date. Always
> verify with the official sources cited and consult a qualified professional
> (lawyer / odvjetnik, tax adviser / porezni savjetnik, accountant /
> računovođa) before acting.

When an answer touches tax or contribution payments (HR68 and the other budget models), VIES/VAT
status or legal duties, end it with one line in the user's language:
- EN: *This is general information, not legal or tax advice. Check the cited sources and consult a professional.*
- HR: *Ovo su opće informacije, a ne pravni ni porezni savjet. Provjerite navedene izvore i posavjetujte se sa stručnjakom.*

Pure validation and formatting answers do not need the line.

## How to use

1. Identify the identifier and the task (validate, parse, generate test data, build a payment
   slip, normalise for storage).
2. Run the script instead of doing check digits by hand; quote its output:
   ```bash
   python3 scripts/hr_ids.py --self-test
   python3 scripts/hr_ids.py oib validate 12345678903          # masked output; --show for full
   python3 scripts/hr_ids.py oib generate --count 5 [--seed 1]   # FICTITIOUS test data
   python3 scripts/hr_ids.py vat validate HR12345678903          # offline; then VIES online
   python3 scripts/hr_ids.py iban validate "HR12 1001 0051 8630 0016 0"
   python3 scripts/hr_ids.py iban generate --bank 2340009 --count 3
   python3 scripts/hr_ids.py bic validate ZABAHR2X
   python3 scripts/hr_ids.py mb validate 01234560 ; python3 scripts/hr_ids.py mbs validate 012345679
   python3 scripts/hr_ids.py jmbg validate 0101990330124
   python3 scripts/hr_ids.py reference validate --model HR01 --value 102-3057-89016
   python3 scripts/hr_ids.py reference checkdigit --method mod11ini --value 10230578901
   python3 scripts/hr_ids.py phone normalize "091 234 5678"
   python3 scripts/hr_ids.py postcode check 21000 ; python3 scripts/hr_ids.py plate check "ZG 1234-AB"
   python3 scripts/hub3_barcode.py --self-test
   python3 scripts/hub3_barcode.py --amount 49,90 --recipient-name "Primjer d.o.o." \
     --iban HR2323400091234567897 --model HR00 --reference 2026-001 --purpose OTHR --visible
   ```
   Add `--json` (before the subcommand) for machine-readable output. Scripts are offline and
   deterministic with `--seed`; they never call VIES or any registry.
3. When writing validation code for the user's project, port the algorithms from
   `scripts/hr_ids.py` into the project's language and reuse its self-test vectors as unit tests.
   Follow the project's own conventions (CLAUDE.md, existing validators) where they don't conflict
   with the standard.
4. Load the reference you need:

| Topic | File | Grep hints |
|---|---|---|
| OIB, PDV ID + VIES API, MB, MBS/EUID, MBO, JMBG, legal-form suffixes, privacy/masking | `references/personal-and-business-ids.md` | `## 1. OIB`, `VIES`, `JMBG`, `ZTD`, `masking` |
| Poziv na broj: all models, lengths, check methods, worked examples, HR68 tax payments, RF | `references/payment-reference-models.md` | `HR01`, `HR68`, `MOD11INI`, `ISO 7064`, `Naputak` |
| HUB-3/HUB 3A slip, PDF417 payload (HRVHUB30), rendering libraries, EPC QR, instant payments/VoP | `references/hub3-barcode.md` | `Payload format`, `pdf417gen`, `EPC QR`, `Verification of Payee` |
| IBAN structure, inner check digits, VBDI → bank/BIC table | `references/bank-codes.md` | `VBDI`, `BIC`, `MOD 11,10` |
| Phone numbering (HAKOM), postal codes (Hrvatska pošta), vehicle plates | `references/phone-postal.md` | `NDC`, `E.164`, `postal`, `plates` |

## Quick reference

| Identifier | Format | Check | Source |
|---|---|---|---|
| OIB | 11 digits (string, may start with 0) | ISO 7064 MOD 11,10 | Pravilnik o OIB-u čl. 3 st. 1 |
| PDV ID | `HR` + OIB | as OIB; registration only via VIES (online) | Zakon o PDV-u čl. 77 st. 6 |
| IBAN HR | `HR` kk + 7-digit VBDI + 10-digit account = 21 chars | mod 97 (ISO 13616) **and** MOD 11,10 on VBDI and account | Odluka o transakcijskim računima (NN 13/2025) čl. 7–11 |
| BIC | 8 or 11 chars, e.g. `PBZGHR2X` | structure only | HNB VBDI/BIC table |
| MB (DZS) | 8 digits | MOD 11, weights 8..2, r 0/1 → 0 | empirical + HUB "MOD11INI" (VERIFY) |
| MBS | 9 digits | MOD 11,10 (empirical, VERIFY) | Zakon o sudskom registru |
| MBO | digits | none known (VERIFY) | Obrtni registar |
| JMBG | 13 digits DDMMYYYRRBBBK | weights 765432765432, sum%11 | Zakon o matičnom broju (NN 9/92) čl. 2 |
| Poziv na broj | `HRnn` + up to 22 chars, P1-P2-P3(-P4) | per model (MOD11INI, ISO 7064, …) | HUB Jedinstveni pregled (01/2026) |
| HUB-3 barcode | PDF417, 14 LF-separated UTF-8 fields, header `HRVHUB30`, amount 15-digit cents | lengths/charset | HUB Uputa, v6 (09/2022) |
| Phone | `+385` + NSN; Zagreb 1 + 7 digits; mobile 9x + 6–7 digits | NSN length per NDC | HAKOM Plan numeriranja (NN 45/2023) |
| Postal code | 5 digits | official list | Hrvatska pošta |
| Plate | AREA + 3–4 digits + 1–2 letters | area list | Pravilnik NN 130/2017 čl. 18 |

## Rules that cover most cases

- **Store identifiers as strings**, never integers (leading zeros in OIB, MB, MBS, accounts).
  Strip spaces and separators on input; keep hyphens in *poziv na broj* (they define the parts).
- **A checksum is not existence.** A valid OIB/IBAN/PDV ID only means "well-formed". VAT status
  needs VIES (online); company data needs the court register; an IBAN's owner needs the bank
  (Verification of Payee since 9 Oct 2025 for euro transfers, Regulation (EU) 2024/886).
- **Croatian IBANs have inner check digits** (bank code and account, MOD 11,10). Validate them
  too, and derive the bank and BIC from the VBDI instead of asking the user.
- **Payment references must match their model** or the bank will not execute the order: use
  HR00 for uncontrolled content, HR99 for none, HR01 for one check digit over everything.
  Tax and contribution payments use HR68 `vrsta prihoda-OIB(-JOPPD)` to the state budget
  account; codes change yearly with the Naputak.
- **HUB-3 barcode**: 14 fields in fixed order, LF-separated, UTF-8, lengths in characters,
  amount in cents zero-padded to 15, restricted charset (no €, &, @). Build with
  `hub3_barcode.py`; render PDF417 with an external library at 9 columns / ECL 4; test-scan with
  several bank apps.
- **Phone numbers**: store E.164 (`+385…`); the mobile prefix does not identify the operator
  (number portability). Display format: `croatia:hr-localization`.
- **Test data is fictitious**: generated values are checksum-valid but invented; label them, and
  keep them out of production and real payments. Use `Primjer d.o.o.`, `Ana Horvat`,
  `ana.horvat@primjer.hr` style names.

## Privacy

OIB, JMBG and personal IBANs of natural persons are personal data (GDPR Art. 4(1); an obrt uses
its owner's OIB). JMBG also encodes birth date and sex. In code and answers:
- never log, print in error messages, put in URLs or send to analytics the full value – mask
  (`12*******03`, `HR12 **** … 0160 0`); the scripts mask by default (`--show` to override);
- collect only with a need and lawful basis, encrypt at rest, restrict access; do not ask for
  JMBG in new systems; retention and legal basis questions → `croatia:hr-legal-compliance`;
- never paste real identifiers into tickets, fixtures, screenshots or prompts – generate test data.

## Related skills

`croatia:hr-localization` (display formats for dates, numbers, addresses, phones),
`croatia:hr-fiscalization-dev` (ZKI, JIR, invoice numbers – not covered here),
`croatia:hr-legal-compliance` (GDPR, VAT/OSS), `croatia:hr-payroll-employment` (JOPPD,
contributions), `croatia:hr-business-admin` (registering companies/obrt), `croatia:croatian-language`
(any Croatian UI text or error messages).

## Keeping current

| Fact | Goes stale when | Check |
|---|---|---|
| VBDI → bank/BIC table | bank mergers, renames | HNB page "Vodeći brojevi pružatelja platnih usluga" (snapshot 27.3.2025) |
| Poziv na broj models | HUB revises the pregled (last: primjena 01/2026) | hub.hr → poziv na broj; sepa.hr |
| HR68 revenue codes, budget accounts | every year (Naputak, e.g. NN 18/2026 + NN 39/2026) | narodne-novine.nn.hr, porezna-uprava.gov.hr |
| HUB-3 barcode spec | new version after v6 (09/2022) | hub.hr → HUB 3 obrasci |
| VIES endpoints | EC changes interfaces | ec.europa.eu/taxation_customs/vies → technical information |
| Numbering plan | HAKOM amends the Plan numeriranja | hakom.hr, NN |
| Postal codes | Hrvatska pošta changes | posta.hr search and download pages |
| Croatian QR payment standard | if HUB/HNB publish one | hub.hr, hnb.hr (none found as of 2026-10-25) |

Items marked **VERIFY** in the references (MB/MBS check-digit sources, MBO format, HR40 algorithm,
EUID suffix, plate letter set, PDF417 library options, bank-app EPC QR support) were not confirmed
against a primary source; surface them to the user when relevant.
