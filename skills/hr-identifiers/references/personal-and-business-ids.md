# OIB, PDV ID, MB, MBS, MBO, JMBG, legal-form suffixes – detail

## Contents
1. OIB
2. PDV ID (VAT number) and VIES
3. MB – matični broj poslovnog subjekta (DZS)
4. MBS – matični broj subjekta (sudski registar) and EUID
5. MBO – matični broj obrta
6. JMBG / MBG (legacy)
7. Legal-form suffixes in company names
8. Privacy and masking

## 1. OIB – osobni identifikacijski broj (personal identification number)

- Legal basis: *Zakon o osobnom identifikacijskom broju* (NN 60/08, in force 1 Jan 2009) and
  *Pravilnik o osobnom identifikacijskom broju* (pročišćeni tekst NN 1/09 … 44/21, 101/25),
  zakon.hr <https://www.zakon.hr/cms.htm?id=43147>. Assigned by Ministarstvo financija – Porezna
  uprava.
- Format: **11 digits** = 10 randomly chosen digits + 1 check digit per **ISO 7064 MOD 11,10**
  (Pravilnik čl. 3 st. 1). The digits are "not telling" about the holder (no date of birth, sex
  or region), it never changes and is never reassigned (Pravilnik čl. 2). Leading zeros are
  possible (store as a string, never as an integer).
- Who gets one: Croatian citizens (at birth registration / acquiring citizenship), legal persons
  seated in Croatia (state bodies, companies, institutions, associations, foundations, political
  parties, religious communities, tourist boards, condominium communities *zajednice suvlasnika*,
  etc.; even bankruptcy/liquidation estates), and foreign natural and legal persons when there is
  a "reason for tracking" – residence permit, entry in an official register of persons or
  property, or becoming a taxpayer (Pravilnik čl. 3, 5, 28). Foreigners can request one at a
  Porezna uprava office (often needed to buy property, open a bank account or register a rental).
- An obrt (sole trader) has no separate OIB: it uses the owner's personal OIB (so an obrt's OIB
  is personal data).
- Algorithm (MOD 11,10): `p = 10`; for each of the first 10 digits `s = (p + d) % 10 or 10;
  p = 2·s % 11`; check = `(11 − p) % 10`.
- Fictitious examples (checksum-valid, widely used dummies): `12345678903`, `00000000001`.
  Generate more: `python3 scripts/hr_ids.py oib generate --count 5`. A random valid OIB may belong
  to a real person – keep generated OIBs out of production and out of public demos.
- Checking that an OIB **exists / belongs to someone**: there is no public open lookup for
  natural persons. For businesses, the court register (sudreg.pravosudje.hr), the obrtni registar
  and the VIES check (if VAT-registered) show OIBs. **VERIFY** current e-services of Porezna
  uprava before promising an existence check.

## 2. PDV ID (PDV identifikacijski broj, VAT number) and VIES

- "PDV identifikacijski broj je osobni identifikacijski broj (OIB) kojemu se dodaje predznak
  »HR«" – Zakon o PDV-u čl. 77 st. 6. Format: `HR` + 11 digits, e.g. `HR12345678903` (fictitious).
- Assigned to VAT-registered taxpayers and to taxpayers/legal persons that acquire goods or
  services within the EU (čl. 77 st. 5). Small taxpayers outside the VAT system may still get one
  for intra-EU services. So: a valid OIB checksum ≠ an active VAT number.
- **VIES** (European Commission) answers "is this VAT number valid for intra-EU transactions"
  – an **online** check, not offline maths:
  - Web: <https://ec.europa.eu/taxation_customs/vies/#/vat-validation>
  - REST (official swagger: <https://ec.europa.eu/assets/taxud/vow-information/swagger_publicVAT.yaml>):
    `POST https://ec.europa.eu/taxation_customs/vies/rest-api/check-vat-number` with JSON
    `{"countryCode": "HR", "vatNumber": "12345678903"}` (number **without** the `HR` prefix).
    Response has `valid`, `name`, `address`, `requestDate`; add `requesterMemberStateCode` and
    `requesterNumber` to receive a `requestIdentifier` (consultation number, useful as evidence for
    zero-rated intra-EU supplies).
    Test endpoint: `POST …/rest-api/check-vat-test-service`; status: `GET …/rest-api/check-status`.
    A GET form `…/rest-api/ms/HR/vat/12345678903` is widely used but is not in the published
    swagger – **VERIFY** before depending on it.
  - SOAP: `https://ec.europa.eu/taxation_customs/vies/services/checkVatService.wsdl`
    (test WSDL: `…/vies/checkVatTestService.wsdl`, vatNumber `100` = valid, `200` = invalid).
  - Member-state services go down; handle `MS_UNAVAILABLE`/timeouts by retrying later, not by
    treating the number as invalid. Cache results with the date.
- `hr_ids.py vat validate` does the offline format/checksum part only.
- VAT/OSS rules themselves: `croatia:hr-legal-compliance` (and `croatia:hr-business-admin`).

## 3. MB – matični broj poslovnog subjekta (DZS business registration number)

- Assigned by Državni zavod za statistiku (DZS) in the *Registar poslovnih subjekata*; 8 digits,
  leading zeros significant (HNB lists e.g. "00560286"). Still printed on older documents and
  requested by some forms; OIB has replaced it as the main identifier.
- Check digit: MOD 11 with weights 8, 7, 6, 5, 4, 3, 2 on the first 7 digits; remainder 0 or 1
  → check digit 0, else 11 − remainder (identical to the HUB "MOD11INI" method, which HUB labels
  "MAT_BR"). Verified against all 25 MBs published in HNB's credit-institution list; the DZS
  specification itself was not found online – **VERIFY** if you need a normative citation.
- Fictitious example: `01234560`. `hr_ids.py mb validate|generate`.

## 4. MBS – matični broj subjekta (court register) and EUID

- Assigned on entry in the *sudski registar* (court register of companies, institutions…);
  unique, unchangeable, never reused (Zakon o sudskom registru). 9 digits, often shown with
  leading zero(s) (e.g. `080…` for Zagreb-registered companies).
- Check digit: the 9th digit matched ISO 7064 MOD 11,10 over the first 8 for every public MBS
  sampled; no official statement found – **VERIFY**. `hr_ids.py mbs validate` reports this.
- **EUID** (European Unique Identifier, BRIS) for Croatian companies: `HRSR` + 9-digit MBS +
  a suffix letter, per *Uredba o načinu utvrđivanja jedinstvenog identifikatora* (NN 51/15).
  **VERIFY** the suffix letter meaning in the Uredba before generating EUIDs.
- Lookup: <https://sudreg.pravosudje.hr> (public search) and the open-data API at
  sudreg-data.gov.hr (**VERIFY** current URL/registration).

## 5. MBO – matični broj obrta

- Number of a sole-trader business (*obrt*) in the *Obrtni registar* (kept by the ministry responsible for crafts and the county offices).
  Shown on the obrtnica / registry extract. Length and check-digit rule could not be confirmed
  from a primary source – validate as digits only and **VERIFY**. For identification use the
  owner's OIB. Lookup: Obrtni registar public search (<https://pretrazivac-obrta.gov.hr>, **VERIFY**).

## 6. JMBG / MBG – jedinstveni matični broj građana (legacy)

- *Zakon o matičnom broju* (NN 9/92), čl. 2: 13 digits in six groups – DD (day), MM (month),
  YYY (last three digits of the birth year), RR (register area; **30–39 = Croatia**), BBB
  (sex + serial: 000–499 male, 500–999 female), K (check digit). Assigned by the police
  (MUP) (čl. 3).
- Year: YYY ≥ 800 → 1YYY (e.g. 990 → 1990); else 2YYY (e.g. 005 → 2005).
- Check digit: weights 7 6 5 4 3 2 7 6 5 4 3 2 on the first 12 digits; `K = 11 − (Σ % 11)`;
  if the result is 11 → 0; a result of 10 cannot be expressed – such numbers fail the HUB
  "MOD11JMB" whole-number check (Σ incl. K·1 must be divisible by 11). Some implementations
  accept 0 in that case – **VERIFY** for your data source.
- Replaced by OIB in 2009 for most purposes, but still on old IDs, pension and health records,
  and in legacy databases (Pravilnik o OIB-u created MBG–OIB pairs, čl. 17, 21).
- It **encodes date of birth and sex** – more sensitive than OIB. Do not ask for it in new
  systems unless a law requires it.
- Fictitious example: `0101990330124` (01.01.1990, register 33, male).

## 7. Legal-form suffixes in company names

Zakon o trgovačkim društvima (ZTD) čl. 13 st. 2: the *tvrtka* (company name) must contain the
legal form in words or abbreviation.

| Suffix | Form (HR) | English |
|---|---|---|
| d.o.o. | društvo s ograničenom odgovornošću | limited liability company |
| j.d.o.o. | jednostavno društvo s ograničenom odgovornošću (ZTD čl. 390.a) | simple LLC |
| d.d. | dioničko društvo | joint-stock company |
| j.t.d. | javno trgovačko društvo | general partnership |
| k.d. | komanditno društvo | limited partnership |
| GIU | gospodarsko interesno udruženje (at start or end of the name) | economic interest grouping |
| obrt | obrt (Zakon o obrtu) – name typically "<activity>, vl. <owner name>, <place>" | sole trader |
| ustanova | ustanova (Zakon o ustanovama) | public/private institution |
| udruga | udruga (Zakon o udrugama) | association / NGO |
| zadruga | zadruga (Zakon o zadrugama) | cooperative |

Parsing tips: match suffixes case-insensitively, with or without spaces (`d. o. o.`, `D.O.O.`,
`doo`), and check `j.d.o.o.` before `d.o.o.`; also seen: `d.o.o. u stečaju` (in bankruptcy),
`u likvidaciji` (in liquidation), and foreign branches (`podružnica`). "vl." = *vlasnik/vlasnica*
(owner) in obrt names.

## 8. Privacy and masking

- OIB, JMBG and IBANs of **natural persons** are personal data (GDPR Art. 4(1) names
  "identification number" explicitly); GDPR Art. 87 lets member states set conditions for national
  identification numbers. An obrt's OIB is its owner's personal OIB. Legal persons' OIB/MB/MBS are
  not personal data (they are public in registers).
- Rules for code: never log full values (mask in logs, analytics, error trackers); never put them
  in URLs or query strings; do not use OIB as a primary key exposed to clients; encrypt at rest
  where feasible; collect only when a legal basis/need exists. Retention and lawful basis:
  `croatia:hr-legal-compliance`.
- Masking conventions: OIB `12*******03`; IBAN `HR12 **** **** **** 0160 0`-style (keep country,
  check digits and last 4); JMBG `01*********24` and never show derived birth date/sex.
  `hr_ids.py` masks OIB/VAT/JMBG output unless `--show` is given.
- Test data: use only fictitious generated values in fixtures, screenshots and docs.
