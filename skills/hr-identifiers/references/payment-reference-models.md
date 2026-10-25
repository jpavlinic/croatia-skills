# Poziv na broj (payment reference) – models HR00–HR99

Primary source: HUB (Hrvatska udruga banaka), *Jedinstveni pregled osnovnih modela „poziva na
broj“, s opisom modela, sadržajem i objašnjenjem za njihovu primjenu te načinom izračuna
kontrolnog broja*, version "primjena od siječnja 2026."
<https://sepa.hr/wp-content/uploads/2026/01/Jedinstveni-pregled-osnovnih-modela-poziva-na-broj-primjena-sijecanj-2026.pdf>
(index page: <https://www.hub.hr/hr/poziv-na-broj-jedinstveni-pregled-osnovnih-modela>).
Budget/tax models: Ministarstvo financija, *Naputak o načinu uplaćivanja prihoda proračuna,
obveznih doprinosa te prihoda za financiranje drugih javnih potreba u 2026. godini*, NN 18/2026,
amended NN 39/2026 (<https://narodne-novine.nn.hr/clanci/sluzbeni/2026_02_18_197.html>).

Validator: `python3 scripts/hr_ids.py reference validate --model HR01 --value 102-3057-89016`.

## Contents
1. General rules
2. Model table (structure, lengths, check method)
3. Check-digit algorithms (with worked examples)
4. Tax and contribution payments (HR68, HR65, HR67…)
5. RF creditor reference (ISO 11649)
6. Implementation notes and gotchas

## 1. General rules (HUB pregled, p. 1–2)

- "Model" = `HR` + 2 digits, written in its own field. The reference content (*sadržaj*) goes in
  *poziv na broj platitelja* (payer) or *poziv na broj primatelja* (recipient), **max 22
  characters** including hyphens. Model + content together max 26 characters.
- In ISO 20022 `pain.001.001.09` (incl. instant) model and reference are written as **one string
  without a space** (e.g. `HR01102-3057-89016`): payer's in *End to End Identification*,
  recipient's in *Remittance Information / Structured / Creditor Reference Information / Reference*.
- Content = 1–3 data parts P1-P2-P3 separated by `-`; models HR23, HR24, HR26, HR28, HR31, HR43,
  HR62, HR64, HR65, HR66 allow a 4th part P4.
- If fewer parts are written, they are read from P1 onwards (one part = P1, two = P1+P2).
- Minimum parts: ≥2 for HR25, HR27, HR35, HR68, HR69, HR83, HR84; ≥3 for HR16, HR26, HR28, HR29,
  HR30, HR33, HR34, HR62, HR63, HR64, HR65; exactly 4 for HR43, HR66.
- Total digits: 2 parts ≤ 21 digits + 1 hyphen; 3 parts ≤ 20 + 2; 4 parts ≤ 19 + 3.
- One part ≤ 12 digits, except: HR12 and HR41 P1 = 13; HR24 P2 up to 13; HR83 P2 up to 16.
- The last digit of a controlled part is its check digit (HR40 P1 has two: 10th and 11th).
- **HR00** = content not under check-digit control (still digits/hyphens, length rules apply).
  **HR99** = no reference at all (field empty; payer data and description are then mandatory).
  Both are compulsory in those cases since 6 June 2018.
- The content must match the model, "otherwise the payment order will not be executed".
- Usage limits: HR23, HR24, HR26–HR29, HR62–HR66, HR68 only per the Naputak (budget revenue);
  HR30, HR31, HR33, HR34 per their description (state treasury); HR69 also for salary/benefit
  payouts; HR19 only for FINA enforcement fees to IBAN HR70 2340 0091 5109 4633 8; HR25, HR83,
  HR84 FINA only; HR50 PBZ only. Other models are free choice.

## 2. Model table

`K` = check digit. "INI" = MOD11INI, "ISO" = ISO 7064 MOD 11,10, "JMB" = MOD11JMB, "P7" =
MOD11P7, "ZB" = MOD10ZB, "M10" = modulus 10 with digit sums. `≤12` = variable up to 12 digits.

| Model | Structure | Lengths | Check method | Note |
|---|---|---|---|---|
| HR00 | P1-P2-P3 | ≤12 each | none | no control |
| HR01 | (P1-P2-P3)K | ≤12 each | INI over the whole content (hyphens removed) | most common for invoices |
| HR02 | P1-(P2)K-(P3)K | ≤12 | INI on P2, INI on P3 | |
| HR03 | (P1)K-(P2)K-(P3)K | ≤12 | INI on each | |
| HR04 | (P1)K-P2-(P3)K | ≤12 | INI on P1, P3 | |
| HR05 | (P1)K-P2 or P2K-P3 | ≤12 | INI on P1; P2 = OIB (ISO) only for certain budget accounts when P1 is a city/municipality code | MB in P1 must be 8 digits with leading zeros |
| HR06 | P1-(P2-P3)K | ≤12 | INI over P2+P3 joined; with 2 parts only P2 | P3 has no leading zeros |
| HR07 | P1-(P2)K-P3 | ≤12 | INI on P2 | |
| HR08 | (P1-P2)K-(P3)K | ≤12 | INI over P1+P2 joined; INI on P3 | P2 no leading zeros |
| HR09 | (P1-P2)K-P3 | ≤12 | INI over P1+P2 | |
| HR10 | (P1)K-(P2-P3)K | ≤12 | INI on P1; INI over P2+P3 (with 2 parts: P1 and P2 each) | |
| HR11 | (P1)K-(P2)K-P3 | ≤12 | INI on P1, P2 | |
| HR12 | (P1)K-P2-P3 | P1 = 13 | JMB on P1 | |
| HR13 | (P1)K-P2-P3 | P1 = 10, first digit 3 | P7 | |
| HR14 | (P1)K-P2-P3 | P1 = 10 | ZB | |
| HR15 | (P1)K-(P2)K | 8 and 11 | M10 on each | never P3 |
| HR16 | (P1)K-(P2)K-P3 | 5, 4, 8 | INI on P1, P2 | exactly 3 parts |
| HR17 | (P1)K-P2-P3 | ≤12 | ISO on P1 | |
| HR18 | (P1)K-P2-P3 | ≤12 | P7 on P1 (first digit 3) | |
| HR19 | (P1)K-(P2)K | ≤10, 11 | INI on P1; P2 = OIB (ISO) | FINA enforcement fees only |
| HR23 | (P1)K-P2-P3-P4 | P1 = 4, starts with 6; P2+P3+P4 ≤ 15 digits | INI on P1 | budget (Naputak) |
| HR24 | (P1)K-P2-P3-P4 | P1 = 4; P2 ≤ 13 | INI on P1 | budget |
| HR25 | P1-P2 | 3, 7 | none | FINA only |
| HR26 | (P1)K-(P2)K-(P3)K-P4 | P1 = 4; P2, P3 ≤ 11 | INI on P1; P2/P3: INI if ≤10 digits, ISO if 11 (= OIB) | budget |
| HR27 | (P1)K-(P2)K | 4, ≤12 | INI | budget |
| HR28 | (P1)K-(P2)K-(P3)K-P4 | 4, 3, 6, ≤6 | INI on P1–P3 | budget |
| HR29 | (P1)K-(P2)K-(P3)K | 4, ≤12, ≤12 | INI | budget |
| HR30 | P1-P2-P3 | 10, 4, ≤6 | none | state budget expenditures |
| HR31 | (P1)K-P2-P3-P4 | P1 ≤ 6 | ISO on P1 | treasury / HZZO |
| HR33 | (P1)K-(P2)K-P3 | ≤6, ≤7, ≤7 | ISO on P1, P2 | refunds to budget/HZZO |
| HR34 | (P1)K-(P2)K-(P3)K | ≤6, ≤7, ≤5 | ISO on all | special-purpose budget accounts |
| HR35 | (P1)K-(P2)K | ≤10, 11 | INI on P1; P2 = OIB (ISO) | |
| HR40 | (P1)K1K2-P2-P3 | P1 = 11, first digit 0 | K1 mod 10 + K2 mod 11; no 3 equal consecutive digits | **script checks format only** (algorithm scope ambiguous) |
| HR41 | (P1)K-(P2)K-P3 | 13, ≤12 | JMB on P1; INI on P2 | |
| HR42 | (P1-P2-P3)K | ≤12 | JMB over the whole content | |
| HR43 | P1-(P2)K-P3-P4 | 3, 8, 5, 3 | INI on P2 | cheque collection |
| HR50 | (P1)K-P2-P3 | 5, 12, 1 | PBZ special algorithm | **format only**; PBZ internal |
| HR55 | (P1)K-P2-P3 | ≤12 | INI on P1 | list of multiple invoices |
| HR62 | (P1)K-(P2)K-(P3)K-P4 | 4, ≤5, ≤6, ≤11 | INI, ISO, INI | budget users (RKP) |
| HR63 | (P1)K-(P2)K-(P3)K | 4, ≤5, ≤12 | INI, ISO, INI | budget |
| HR64 | (P1)K-(P2)K-P3 or (P3)K-P4 | 4, ≤5, ≤12, ≤12 | INI, ISO; P3 ISO only if 11 digits (OIB) | budget |
| HR65 | (P1)K-(P2)K-(P3)K-P4 | 4, 3, ≤11, ≤10 | INI, INI; P3: ISO if ≤5 or 11 digits, INI if 6–10 | budget (e.g. goods/services sales) |
| HR66 | (P1)K-(P2)K-(P3)K-(P4)K | 4, 3, ≤5 or 7, 3–7 | INI, INI, ISO, INI | budget |
| HR67 | (P1)K-P2-P3 | 11 (OIB), ≤10, ≤8 | ISO on P1 | e.g. state agricultural land |
| HR68 | (P1)K-(P2)K-P3 | 4, 11 (OIB), ≤5 | INI on P1; ISO on P2 | **taxes and contributions** |
| HR69 | (P1)K-(P2)K-P3 | 5, 11 (OIB), 3 | ISO on P1 and P2 | salaries/benefits: P1 = 40002, P3 = income-type code |
| HR83 | (P1)K-P2-P3 | 4, 5/7/16, 6 | INI on P1 | FINA only |
| HR84 | (P1)K-P2-P3 | 4, 4 or 8, 10 | INI on P1 | FINA only |
| HR99 | — | empty | — | no reference |

HR69 variant II: P1 = `40002`, P2 = OIB of the payer of the income, P3 = 3-digit code from the
*Šifarnik vrsta osobnih primanja* (e.g. 100 full salary, 110 protected part, 600 pension). The
full code list with "protected from enforcement" flags is in the HUB pregled, p. 20–21.

## 3. Check-digit algorithms (HUB pregled, section 4)

All operate on the digits of a part (or of joined parts) **without** the check digit `K`, then
compare with `K`.

**MOD11INI** (most models; also the DZS MB). Weights 2, 3, 4, … from the **right**, uncapped.
`r = Σ % 11`; `K = 0` if `r ∈ {0, 1}`, else `11 − r`.
Example: `33444555666` → Σ = 321, r = 2, K = 9 → `334445556669`.
Example (HR01): `10230578901` → Σ = 214, r = 5, K = 6 → `HR01 102-3057-89016`.

**ISO 7064 MOD 11,10** (OIB, HR17, HR31, HR33, HR34, HR62–HR66 parts, HR67–HR69). Start
`p = 10`; for each digit left→right: `s = (p + d) % 10`, if `s == 0` then `s = 10`;
`p = (2·s) % 11`. Then `K = (11 − p) % 10`. Example: `234000` → K = 9.

**MOD11JMB** (HR12, HR41 P1, HR42). Applied to the whole code incl. K. Not all digits equal.
Weights 1, 2, …, 7 from the right, then 2…7 repeating. Valid if `Σ % 11 == 0`.
(For a 13-digit JMBG this equals the classic weights 7 6 5 4 3 2 7 6 5 4 3 2 1.)

**MOD11P7** (HR13, HR18). First digit must be 3. Weights 2…7 from the right, cycling.
`r = Σ % 11`; `r = 0 → K = 5`; `r = 1 → K = 0`; else `K = 11 − r`.
Example: `345678901` → Σ = 196, r = 9, K = 2.

**MOD10ZB** (HR14). Weights 1, 2, 1, 2… from the right (plain products). `K = Σ % 10`.
Example: `223344556` → Σ = 48, K = 8.

**Modulus 10 with digit sums** (HR15; HR40 K1). Weights 2, 1, 2, 1… from the right; add the
digits of each product (14 → 1 + 4). `K = (10 − Σ % 10) % 10`. Example: `54370395` → Σ = 37 → 3.

**HR40 K2** (mod 11): weights 2…7 from the right, cycling; `r = 0` → invalid, `r = 1` → K2 = 0,
else `11 − r`. The text does not say unambiguously whether K1 is included in the K2 input, so the
script does not verify HR40. **VERIFY** with the recipient (or a bank) before relying on it.

Compute a single check digit: `python3 scripts/hr_ids.py reference checkdigit --method mod11ini --value 10230578901`.

## 4. Tax and contribution payments

From the Naputak (NN 18/2026, section 1.11.1 and others):

- State budget account (Državni proračun RH): **HR1210010051863000160** (HNB bank code 1001005).
- **HR68**: P1 = 4-digit *vrsta prihoda* (revenue type) code incl. MOD11INI check digit;
  P2 = taxpayer's OIB; P3 optional and not controlled, except: JOPPD-linked contributions
  → P3 = 5-digit JOPPD report label (format `YYDDD`, e.g. `26001`); MIO codes 8109, 8117, 8150,
  8249, 8290, 8303, 8338 → 4-digit R-Sm identifier; 1244 (VAT, special scheme for foreign
  traders) → period.
- Examples of revenue-type codes in the 2026 Naputak: **1201** PDV (VAT), **1651** porez na
  dobit (corporate income tax), **8168** MIO I. stup temeljem radnog odnosa (pension pillar I,
  employment, JOPPD). Example reference: `HR68 1651-<OIB>`. Codes and accounts change with each
  yearly Naputak – **VERIFY** in the current one; Porezna uprava publishes payment tables
  (<https://porezna-uprava.gov.hr>). For payroll details see `croatia:hr-payroll-employment`.
- Other budget models seen in the Naputak: HR65 (sale of goods/services, donations), HR26 (some
  gaming fees), HR67 (agricultural land, P1 = OIB), HR05 (hunting lease), HR63 (port concessions),
  HR11 (customs).

## 5. RF creditor reference (ISO 11649)

`RF` + 2 check digits + 1–21 alphanumerics, mod-97 like IBAN (move first 4 chars to the end,
letters → numbers A = 10 … Z = 35, result % 97 == 1). The HUB-3 spec says ISO 11649 references
"will be written" in the reference field after its introduction; in practice domestic HUB-3 slips
use HR models. EPC QR codes (SEPA) use RF references. Validator: `reference validate --model RF
--value RF18539007547034` (the ISO 11649 sample value).

## 6. Implementation notes and gotchas

- Store model and reference separately; strip spaces; keep hyphens (they define the parts and
  joint checks). Do not zero-pad parts unless the model says so (HR05 MB = 8 digits).
- For invoices, HR01 or HR00 are the usual choices. A typical pattern is
  `HR01 <invoice no.>-<year>` with one check digit over everything, or HR00 without control.
- The illustrative reference in the HUB **barcode** spec ((of the form `HR01 7269-<OIB>-00019`)) does
  **not** satisfy HR01's MOD11INI check; don't use it as a positive test vector.
- Bank apps reject payments whose reference fails the model check; validate before printing.
- Fiscal-receipt numbers, ZKI and JIR are a different topic: `croatia:hr-fiscalization-dev`.
