---
name: hr-fiscalization-dev
description: >-
  Technical guide to implementing Croatian fiscalization and e-invoicing in
  software: Fiskalizacija 1.0 B2C receipts (RacunZahtjev SOAP, ZKI, JIR, XML
  signature, QR code, offline mode, storno, receipt numbering, FINA/demo
  certificates, cistest) and Fiskalizacija 2.0 eRačun (UBL 2.1, EN 16931, HR
  CIUS, KPD codes, AS4, AMS/MPS, informacijski posrednik, fiscalization of
  eRačun, eIzvještavanje), plus integration architecture, testing and error
  codes. Use for POS, web shop, SaaS billing, Stripe webhooks or invoice
  software for Croatia. Triggers: fiskalizacija, fiskalni račun, fiskalna
  blagajna, ZKI, zaštitni kod, JIR, CIS, cistest, FINA certifikat, demo
  certifikat, eRačun, e-račun, UBL, EN 16931, HR CIUS, KPD, Peppol,
  informacijski posrednik, MPS, AMS, eIzvještavanje, FiskAplikacija,
  s001/s004/S008 errors, "receipt Croatia", "POS Croatia", "invoice software
  Croatia", "Croatian e-invoice".
---

# Croatian fiscalization and eRačun – developer guide

Use this skill to design, build, review or debug software that fiscalizes Croatian B2C receipts
(Fiskalizacija 1.0, "F1") or issues, receives and fiscalizes eRačuni with e-reporting
(Fiskalizacija 2.0, "F2"). It covers the technical HOW: message formats, cryptography, endpoints,
architecture, testing. Who is obliged and what the law requires is in `croatia:hr-legal-compliance`.

Status: researched 2026-10-25.

> **Not legal, tax or financial advice.** This skill provides general,
> research-based information that may be incomplete or out of date. Always
> verify with the official sources cited and consult a qualified professional
> (lawyer / odvjetnik, tax adviser / porezni savjetnik, accountant /
> računovođa) before acting.

## How to use

1. Pin the facts (ask or infer from the code): seller's VAT status, B2C or B2B, buyer country,
   payment method (cash, card, bank transfer, PSP like Stripe), POS/offline needs, volume, whether
   an intermediary is already contracted, language/stack.
2. Run the decision tree below, then load only the reference you need:

| Need | Reference | Grep hints |
|---|---|---|
| F1 receipts: flow, XML fields, ZKI, signature, JIR, numbering, QR, offline, storno, premises, certificates | `references/fiskalizacija-1-b2c.md` | `RacunZahtjev`, `ZKI`, `NakDost`, `QR`, `storno`, `1.1.2027` |
| F2: exchange (AS4, AMS/MPS), intermediaries, `EvidentirajERacun`, eIzvještavanje, archiving | `references/fiskalizacija-2-eracun.md` | `AMS`, `EvidentirajNaplatu`, `XAdES`, `8509`, `posrednik` |
| UBL/HR CIUS fields, HR-BR rules, KPD, HR VAT labels, UBL skeleton | `references/hr-cius-fields.md` | `CustomizationID`, `ProfileID`, `HR-BR-`, `listID="CG"`, `HR:PDV25` |
| Build vs buy, outbox/retry/locks, Stripe webhooks, refunds, multi-tenant | `references/integration-architecture.md` | `idempotency`, `Stripe`, `lock`, `refund`, `tenant` |
| Test URLs, demo certs, smoke tests, all error codes (s0xx, restrictive 176–184, v-codes, S0xx) | `references/testing-and-errors.md` | `s004`, `s013`, `v166`, `S006`, `Echo` |
| Spec versions, laws, URLs, open-source libraries | `references/sources.md` | `v2.7`, `v1.15`, `GitHub` |

3. Use the scripts (Python 3 stdlib, each has `--self-test`):
   - `scripts/zki.py` – build the exact ZKI input string, print the `openssl` signing pipeline,
     sign via local `openssl`, or turn a raw signature into the ZKI.
   - `scripts/receipt_number.py` – format/parse `broj/oznakaPP/oznakaNU`, check a list for gaps.
   - `scripts/fiscal_qr.py` – build the `https://porezna.gov.hr/rn?...` QR content.
4. Cite the source (Act article, Pravilnik article, or spec version + chapter) for every rule you
   state, and surface **VERIFY** items as open questions.
5. Generated code, XML templates or invoice logic start with
   `TEMPLATE – not legal advice. Adapt it to your case and have it reviewed by a professional.`
   (HR: `PREDLOŽAK – nije pravni savjet. Prilagodite ga svom slučaju i dajte ga na provjeru stručnjaku.`)
6. Croatian-language output (receipt texts, UI strings, e-mails) → also apply
   `croatia:croatian-language`. OIB/IBAN validation → `croatia:hr-identifiers`. VAT registration
   and paušal questions → `croatia:hr-business-admin`.
7. End every answer that touches these topics with one line in the user's language:
   - EN: *This is general information, not legal or tax advice. Check the cited sources and consult a professional.*
   - HR: *Ovo su opće informacije, a ne pravni ni porezni savjet. Provjerite navedene izvore i posavjetujte se sa stručnjakom.*

## Decision tree

```
Sale with Croatian place of supply?
├─ Buyer is a consumer (B2C), any payment method (cash, card, Stripe, bank transfer)
│    → F1 fiscal receipt: RacunZahtjev → JIR; print/send JIR + ZKI + QR.   [fiskalizacija-1-b2c.md]
├─ Buyer is a Croatian business (has OIB, listed in AMS)
│    ├─ seller in VAT system → eRačun (UBL HR CIUS) via access point + fiscalize (I)
│    │     + report payment by the 20th.                                  [fiskalizacija-2-eracun.md]
│    │     Paid cash/card? Zakon čl. 39 allows an F1 receipt with buyer OIB instead (then no eRačun).
│    └─ seller not in VAT system → 2026: may issue ordinary invoices, must RECEIVE eRačuni;
│          from 1.1.2027: issue eRačuni too (MIKROeRAČUN or intermediary). Check the legal skill.
├─ Buyer is an EU or non-EU business → no eRačun/e-reporting duty; ordinary invoice
│    (reverse-charge wording per legal skill); UBL via Peppol optional.
└─ EU consumer under OSS / non-EU consumer → usually no F1 (see legal skill reference 04 §1.7; VERIFY).
Receiving any eRačun (all businesses since 1.1.2026) → be in AMS, fiscalize (U) within
5 working days, report rejections by the 20th.
```

## Facts that cover most cases

- **F1 endpoint** test `https://cistest.apis-it.hr:8449/FiskalizacijaServiceTest`, production
  `https://cis.porezna-uprava.hr:8449/FiskalizacijaService`; SOAP 1.1, 1-way TLS, synchronous,
  2 s processing target (spec v2.7 §6.1; Pravilnik čl. 10).
- **Deadline: from 1.1.2027 production rejects RSA-SHA1 signatures and TLS 1.1** (test already since
  1.7.2026). Sign with `rsa-sha256` + `sha256` digest, exc-c14n, enveloped (spec v2.7 §2, §7).
- **ZKI** = MD5 hex of the RSA signature of `OIB + 'dd.MM.yyyy HH:mm:ss' + BrOznRac + OznPosPr +
  OznNapUr + IznosUkupno` (note the space in the date; spec v2.7 §12 uses RSA-SHA256).
- **JIR** = UUID returned by CIS; a receipt without JIR must still be issued and re-sent within
  **2 working days** with `NakDost=true` (Zakon čl. 21).
- **Receipt number** `broj/oznakaPP/oznakaNU`, unbroken per premises (`P`) or device (`N`)
  (Zakon čl. 9). Payment codes `G`, `K`, `T`, `O` (cheque `C` removed 1.9.2025).
- **QR** `https://porezna.gov.hr/rn?jir=…&datv=YYYYMMDD_HHMM&izn=<cents>` (or `zki=`), ≥ 2 × 2 cm
  (spec v2.7 §2.7; Pravilnik čl. 17–18).
- **Restrictive errors** since 1.1.2026 reject a receipt (`s013`): future date, > 30 days old,
  number 0, bad OIBs, `T` with buyer OIB, VAT rate not 0/5/13/25.
- **Storno/refund** = new receipt with negative amounts (Zakon čl. 24). Same-day payment-method or
  buyer-OIB fix: `PromijeniPodatkeRacunaZahtjev`.
- **eRačun** = UBL 2.1 EN 16931 with HR CIUS `CustomizationID …cius-2025:1.0#conformant#…ext-2025:1.0`,
  `ProfileID` P1–P12/P99, `IssueTime`, operator OIB + label, KPD (`listID="CG"`) per line, HR VAT
  labels, EUR. No JIR/ZKI/QR on an eRačun. A PDF is not an eRačun.
- **F2 web service** port 8509, XAdES-B signature; `EvidentirajERacun` (I/U),
  `EvidentirajNaplatu`, `EvidentirajOdbijanje`, `EvidentirajIsporukuZaKojuNijeIzdanERacun`.
- **Stripe/PSP receipts are not fiscal receipts**; documents with payment data before the fiscal
  receipt need "OVO NIJE FISKALIZIRANI RAČUN" (Zakon čl. 29).
- **Certificates**: OIB-bearing certificate from a trust-service provider (FINA "Fiskal" or eIDAS
  QTSP); demo certificate for test; never commit `.p12` files or passwords.

## Go-live checklist (F1)

- [ ] Premises registered in ePorezna; `OznPosPr` labels and device numbers fixed in the internal act
- [ ] Sequence mode P/N chosen; number allocation locked per key; no reuse after failures
- [ ] ZKI reproducible from stored fields; amount string identical to `IznosUkupno`
- [ ] RSA-SHA256 + TLS 1.2+ verified on cistest (SHA1 rejected there since 1.7.2026)
- [ ] Response signature verified against the CA chain (no leaf pinning)
- [ ] Offline queue with `NakDost`, new `IdPoruke` per attempt, alert well before 2 working days
- [ ] Receipt layout: time (hh:mm), operator label, payment method, JIR, ZKI, QR (≥ 2 × 2 cm)
- [ ] Storno flow, same-day correction flow, tips (if hospitality)
- [ ] Clock sync (NTP), timezone Europe/Zagreb on print
- [ ] Production certificate in a secret store; expiry monitoring; demo cert only in test config
- [ ] 2+ days stable run on test (spec v2.7 §6); `ProvjeraZahtjev` returns `v100`

## Go-live checklist (F2)

- [ ] Intermediary chosen from PU's current list (or own access point certified); FiskAplikacija
      authorisations for receiving and fiscalization granted
- [ ] Receiving identifier published in AMS
- [ ] UBL passes XSD + CEN + current PU HR schematron for every document type you issue
- [ ] KPD 2025 code stored per product/service; HR VAT labels and exemption reasons mapped
- [ ] Buyer AMS lookup before issuing; fallback per Zakon čl. 40 logged
- [ ] Outgoing fiscalization at issue; incoming within 5 working days
- [ ] Monthly jobs: payments (čl. 53) and rejections (čl. 52) reported by the 20th
- [ ] XML archive immutable, indexed, retained ≥ 6 years (čl. 35) – 11 years recommended

## Keeping current

These facts go stale; check them before each project:
- F1 *Tehnička specifikacija* version (v2.7 on 2026-10-25), WSDL package version, algorithm and TLS
  cut-off dates, rotated *fiskalcis*/*fiskalcistest* certificates – porezna.gov.hr →
  Fiskalizacija u krajnjoj potrošnji → Novosti.
- Pravilnik amendments (NN 97/26 applies from 1.1.2027) – narodne-novine.nn.hr.
- F2 spec (v1.15 on 2026-10-25), HR CIUS spec (12.3.2026), validator version (15.3.2026), WSDLs,
  samples – porezna.gov.hr → Fiskalizacija 2.0 / eRačun → Dokumentacija.
- Intermediary list (37 on 16.10.2026) – porezna-uprava.gov.hr → Popis informacijskih posrednika.
- KPD version (KPD 2025) – DZS KLASUS.
- Open-source library maintenance – see `references/sources.md`.

Anything project-specific (chosen intermediary, premises labels, sequence mode, certificate
location) belongs in the user's project, e.g. `.claude/croatia/hr-fiscalization-dev.md`, never in
this skill's files.
