# Freelancing and foreign clients – 2026

Status: researched 2026-10-25. **VERIFY** marks unconfirmed or changing points.

Contents: 1 Choosing the vehicle · 2 Drugi dohodak (ugovor o djelu, autorski honorar) · 3 Obrt/paušal for
foreign clients · 4 Invoicing foreign clients · 5 Receiving payments · 6 Digital nomads and foreigners

---

## 1. Choosing the vehicle

| Situation | Usual fit |
|---|---|
| One-off or occasional job, the payer is a Croatian business/person | **Drugi dohodak** (other income): ugovor o djelu or autorski ugovor; the payer withholds tax and contributions |
| Regular work, receipts up to €60,000, low expenses | **Paušalni obrt** (`pausalni-obrt.md`) |
| Regular work, high expenses or above €60,000 | Obrt na dohodak or d.o.o. (`legal-forms.md`) |
| Paid by a **foreign** client who cannot withhold Croatian tax | Drugi dohodak is possible but the person must report and pay it themselves (§2.4); an obrt is usually simpler for anything regular |
| Long-term work for one client under its direction, fixed hours | Risk of disguised employment – `croatia:hr-payroll-employment` |

## 2. Drugi dohodak (other income)

### 2.1 What it is
Income that is not salary, self-employment, property or capital (ZPD čl. 39 st. 2): e.g. ugovor o djelu
(contract for work), autorski honorar (copyright fee), supervisory-board fees, consultants, translators,
agents (čl. 39 st. 3). Taxed per payment.

### 2.2 Tax and contributions 2026 (Croatian payer)
- **Contributions** (ZOD čl. 13 st. 3, čl. 14 st. 2, čl. 17 st. 2):
  - Pension: **10%** from the gross (7.5% pillar I + 2.5% pillar II, or 10% pillar I only) – withheld from the
    recipient.
  - Health: **7.5%** on top, paid by the payer.
- **Income tax advance:** withheld at the **lower income-tax rate of the recipient's city of residence** (15–23%,
  see `obrt-dohodak.md` §3), **without** the personal allowance (ZPD čl. 40 st. 1). Base = gross − pension
  contributions.
- **Autorski honorar** (fee under the Copyright Act) and certain journalists/artists/athletes: **30% normed
  expenses** are deducted first (ZPD čl. 39 st. 5); contributions are then calculated on the reduced base
  (**VERIFY** base for contributions with an accountant – practitioner calculators apply it).
- Drugi dohodak is included in the annual income-tax calculation (it is not on the čl. 49 exclusion list), so the
  final tax can differ from the advance (refund or top-up).
- Payer reports via JOPPD and pays tax and contributions at the time of payment (ZPD čl. 40 st. 2).

### 2.3 Example (2026, estimate; city lower rate 20%, recipient in both pension pillars)

| | Ugovor o djelu | Autorski honorar |
|---|---|---|
| Gross (bruto) | 1,000.00 | 1,000.00 |
| Normed expenses 30% | — | 300.00 |
| Pension 10% (from gross / reduced base) | 100.00 | 70.00 |
| Tax base | 900.00 | 630.00 |
| Tax 20% | 180.00 | 126.00 |
| **Net to recipient** | **720.00** | **804.00** |
| Health 7.5% paid by payer | 75.00 | 52.50 |
| **Total cost to payer** | **1,075.00** | **1,052.50** |

Pensioners, students (student service: `croatia:hr-payroll-employment`) and people insured abroad have
different contribution rules – **VERIFY** per case.

### 2.4 Foreign payer
A foreign client does not withhold Croatian tax. The Croatian resident must report the income and pay tax and
contributions themselves (forms and deadlines via PU / ePorezna; **VERIFY** current form and the 8-day / 15-day
deadlines with PU before advising). For repeated foreign income this quickly becomes more work than a paušal obrt.

## 3. Obrt (paušal) with foreign clients

- Receipts from foreign clients count as obrt receipts (KPR, PO-SD). See the open question on the paušal limit
  in `pausalni-obrt.md` §1.
- **EU business clients:** get a **PDV-ID before the first invoice**, invoice with reverse-charge wording, file PDV
  + ZP for each month with such invoices (`pdv-vat.md` §3–4, §6).
- **Non-EU business clients:** no PDV-ID needed for the sale itself, but you will usually need one anyway for
  foreign services you buy (ads, SaaS).
- **Foreign consumers:** fiscalization questions for foreign B2C and e-services: legal skill 04 §1.7.
- Social security if you also work abroad or for one foreign client long term: A1 certificate (HZZO/HZMO) –
  **VERIFY** with HZMO.

## 4. Invoicing foreign clients

- Invoices may be issued in a foreign language and currency, but VAT-relevant amounts must also be expressed in
  **EUR** using the applicable exchange rate (ZPDV čl. 79 / Pravilnik o PDV-u; **VERIFY** whether HNB middle rate
  or ECB rate and which date). Bilingual (HR/EN) invoices are common.
- Mandatory elements: legal skill 04 §2 (number, date, OIB/VAT IDs, supplier data, description, amounts, VAT note
  or reverse-charge note, fiscal data where required).
- Reverse-charge note: **"Prijenos porezne obveze / Reverse charge – čl. 17. st. 1. Zakona o PDV-u"** (ZPDV
  čl. 79 st. 7 requires the words "prijenos porezne obveze" or "reverse charge").
- KPR entry: the EUR amount actually credited to the account (receipt), on the day received (**VERIFY** treatment
  of FX differences and platform fees with an accountant).
- Templates you generate must start with the template header from SKILL.md.

## 5. Receiving payments (Wise, Payoneer, PayPal, Stripe)

- Practical rule: receive business payments **to the obrt's/company's business account** (IBAN in Croatia or an
  EU e-money account in the business's name). Whether an obrtnik is legally obliged to have a separate business
  account is a **VERIFY** item (practice and PU expect one; fiscalization and eRačun reporting are easier with
  it).
- Wise / Payoneer / PayPal business accounts are e-money accounts; record receipts when they arrive there, not
  only when transferred to the Croatian bank. Keep monthly statements as bookkeeping documents.
- Their fees: generally exempt payment services (no reverse charge), but check invoices (`pdv-vat.md` §5).
- Accounts held abroad by a Croatian resident may need to be reported to HNB/PU under certain conditions –
  **VERIFY** (FATCA/CRS reporting is done by the institutions).
- Cash: businesses may not accept or make cash payments of **€10,000 or more** (including linked transactions)
  under the Zakon o sprječavanju pranja novca i financiranja terorizma (NN 151/22 amendment; **VERIFY** article
  number). Between businesses that are fiscalization obligors, cash is capped at **€700 per invoice** (Zakon o
  fiskalizaciji čl. 30 st. 3 – legal skill 04 §5).

## 6. Digital nomads and foreigners

- Croatia grants temporary stay to **digital nomads** (Zakon o strancima) who work remotely for non-Croatian
  employers or their own foreign company; their foreign income is exempt from Croatian income tax during the
  permit (ZPD exemption list – **VERIFY** article and conditions on gov.hr / MUP). They **may not work for
  Croatian employers or provide services to Croatian clients** under that permit (**VERIFY**).
- A digital nomad who wants Croatian clients needs a different residence basis and a business form (obrt/d.o.o.).
- EU/EEA citizens can open an obrt or d.o.o. like Croatian citizens; START requires Croatian residence and
  e-identity, otherwise use e-Sudski registar or the in-person route (gov.hr). Third-country nationals: residence
  and work permit rules first (MUP).
