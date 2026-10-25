# HUB-3 / HUB 3A payment slip and its PDF417 barcode

Primary source: HUB, *Uputa o upotrebi PDF417 2D bar koda na papirnatim nalozima za plaćanje u
domaćem platnom prometu (obrazac HUB3A), Prilog A – Format zapisa 2D barkoda prema HUB-3
standardu*, **verzija 6, rujan 2022.** (EUR), PDF:
<https://hub.hr/sites/default/files/inline-files/2DBK_EUR_Uputa_1.pdf> (same file as `…_0.pdf`).
Index of forms and documents: <https://hub.hr/index.php/hr/hub-3-obrasci> (HUB 3 and HUB 3A forms,
interactive PDF, *Uputa o obliku, sadržaju i upotrebi standardiziranih naloga za plaćanje HUB 3 i
HUB 3A* (June 2013), *Šifre namjene* list).

Builder: `python3 scripts/hub3_barcode.py --help` (prints the payload text; see §5 for drawing).

## Contents
1. Forms
2. Barcode symbol requirements
3. Payload format (field table, rules)
4. Example payload
5. Rendering the symbol (external library)
6. EPC QR, instant payments, Verification of Payee
7. Testing checklist

## 1. Forms

- **HUB 3** – general payment order (*nalog za plaćanje*) used at bank counters, national and
  cross-border.
- **HUB 3A** – the *opća uplatnica* that a recipient (utility, company, landlord) prints and sends
  to the payer, with the PDF417 barcode in the **bottom-left field**, 1 mm from the left and top
  edge of that field. The barcode spec version 6 applies **only to HUB 3A**.
- Printing HUB 3/3A forms for distribution requires approval; HUB publishes a *Zahtjev za
  odobrenje za korištenje HUB 3 obrazaca*. **VERIFY** current practice if you print forms on a large
  scale.

## 2. Barcode symbol requirements (spec v6, p. 5 and 12)

| Property | Value |
|---|---|
| Symbology | PDF417 (not Compact/truncated, not Macro) |
| Module (narrow bar) width | 0.254 mm (10 mil) |
| Module height : width | 3 : 1 |
| Error correction level | 4 |
| Data columns | 9 |
| Encoding | binary (byte compaction), UTF-8 text |
| Size | width ≈ 58 mm; height ≤ 26 mm including quiet zones |
| Quiet zone | ≥ 2 module widths |
| Printing | laser printer; module = 6 dots at 600 dpi, 12 dots at 1200 dpi |
| Scanning | 10-mil capable scanner, or ≥ 3.2 MP autofocus camera |

## 3. Payload format (spec v6, p. 6–9)

14 fields, in this order, each followed by **LF (0x0A)**. Lengths are **characters, not bytes**
(Č č Ć ć Đ đ Š š Ž ž are 2 bytes in UTF-8). Fields are **not padded**, except the amount. Text
longer than the field must be **shortened** to the field length. Max 273 characters of data.

| # | Field (HR) | English | Max | Rule |
|---|---|---|---|---|
| 1 | Zaglavlje | header | 8 | always `HRVHUB30` (the final `0` is reserved) |
| 2 | Valuta | currency | 3 | `EUR` (ISO 4217) |
| 3 | Iznos | amount | 15 | euro **cents**, no separators/sign, right-aligned, **zero-padded to 15** (123,55 EUR → `000000000012355`) |
| 4 | Platitelj | payer name | 30 | company name or *first name then surname* |
| 5 | Adresa platitelja (ulica i broj) | payer street and number | 27 | |
| 6 | Adresa platitelja (poštanski broj i mjesto) | payer postcode and place | 27 | |
| 7 | Primatelj | recipient name | 25 | |
| 8 | Adresa primatelja (ulica i broj) | recipient street | 25 | |
| 9 | Adresa primatelja (poštanski broj i mjesto) | recipient postcode and place | 27 | |
| 10 | Broj računa primatelja (IBAN) | recipient IBAN | 21 | HR IBAN, no spaces |
| 11 | Model kontrole poziva na broj primatelja | reference model | 4 | `HR` + 2 digits, e.g. `HR01` |
| 12 | Poziv na broj primatelja | recipient reference | 22 | digits in groups with hyphens per the model (see `payment-reference-models.md`) |
| 13 | Šifra namjene | purpose code | 4 | ISO 20022 purpose code, e.g. `COST`, `OTHR` (HUB list "Šifre namjene") |
| 14 | Opis plaćanja | description | 35 | free text; the form allows 4 × 35 but only 35 go in the barcode |

Allowed characters: digits 0–9, the 27 letters of the Croatian alphabet, Q W X Y, space and
`, . : - + ? ' / ( )`. Upper and lower case allowed. DŽ, LJ, NJ count as two characters.
Anything else (€, &, @, %, quotes, `_`, emoji, other diacritics such as ä, é) is **not allowed** –
transliterate or remove it before building the payload. Note that `&` is common in company names
("J&T banka") – replace it (e.g. "J i T" or "J-T"); **VERIFY** what your bank apps accept.

Empty optional fields are written as empty lines (two consecutive LFs). The spec's example shows
an LF after the last field too; the script follows that and has `--no-trailing-lf`. Most
readers accept both – test with bank apps.

## 4. Example payload (fictitious data, structure as in the spec example)

```
HRVHUB30
EUR
000000000012355
ANA HORVAT
PRIMJERNA ULICA 1
10000 ZAGREB
PRIMJER d.o.o.
ILICA 1
21000 SPLIT
HR1210010051863000160
HR01
102-3057-89016
COST
Troškovi za 1. mjesec
```

(The IBAN shown is the public state-budget account used in HUB's own example; never send test
payments to it.) Generate this with:

```bash
python3 scripts/hub3_barcode.py --amount 123,55 --payer-name "ANA HORVAT" \
  --payer-street "PRIMJERNA ULICA 1" --payer-city "10000 ZAGREB" \
  --recipient-name "PRIMJER d.o.o." --recipient-street "ILICA 1" --recipient-city "21000 SPLIT" \
  --iban HR1210010051863000160 --model HR01 --reference 102-3057-89016 \
  --purpose COST --description "Troškovi za 1. mjesec" --visible
```

Note: the reference in HUB's own spec example ((of the form `HR01 7269-<OIB>-00019`)) fails the HR01
check digit; the example above uses a valid HR01 reference from the HUB reference-model document.

## 5. Rendering the symbol

There is no PDF417 encoder in the Python standard library (it needs Reed–Solomon over GF(929)
and the 3 × 929 codeword pattern tables from ISO/IEC 15438), so `hub3_barcode.py` does not draw
images. Options (third-party, install only if the project allows it):

- **Python**: `pdf417gen` (PyPI, 0.8.1, Jan 2025) –
  `codes = encode(text, columns=9, security_level=4)`, then `render_image(codes, scale=3, ratio=3)`
  (Pillow) or `render_svg(...)`. It chooses compaction modes automatically; HUB asks for binary
  encoding – check whether your version has a force-binary option. **VERIFY** by scanning.
- **JavaScript/TypeScript**: `bwip-js` (`bcid: 'pdf417'`, columns 9, error-correction level 4) –
  **VERIFY** option names against its docs.
- **Java/.NET**: ZXing (`BarcodeFormat.PDF_417`, error correction 4, set dimensions so there are 9
  data columns).
- **PHP**: libraries exist; check they support PDF417 with ECL 4 and 9 columns.

For print, size the module at 0.254 mm and keep the 3:1 height ratio; at screen resolution keep
the barcode wide enough (several cm) for phone cameras.

## 6. EPC QR, instant payments, Verification of Payee

- **EPC QR code** (European Payments Council, *Quick Response Code – Guidelines to Enable the Data
  Capture for the Initiation of a SEPA Credit Transfer*, EPC069-12 v3.0, Sept 2022:
  <https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2022-09/EPC069-12%20v3.0%20Quick%20Response%20Code%20-%20Guidelines%20to%20Enable%20the%20Data%20Capture%20for%20the%20Initiation%20of%20an%20SCT_0.pdf>):
  QR, ECL M, max 331 bytes, lines: `BCD` / version `001` or `002` / charset (`1` = UTF-8) / `SCT` /
  BIC (optional in v002 within the EEA) / name (≤70) / IBAN / `EUR12.30` / purpose (4) /
  structured reference (RF, ≤35) **or** unstructured text (≤140) / info (≤70). There is no field
  for the Croatian model, so an HR model + reference can only go in the unstructured text.
- **Croatia**: research on 2026-10-25 found **no HUB-published Croatian QR payment standard**;
  HUB-3 PDF417 (`HRVHUB30`) remains the domestic slip standard. Whether a given Croatian bank app
  scans EPC QR is a per-bank question – **VERIFY** with the banks you target. (The "IPS QR" format
  seen online is the Serbian NBS standard, not Croatian.)
- **Instant payments / VoP**: under Regulation (EU) 2024/886 (Instant Payments Regulation),
  euro-area payment service providers had to receive SEPA instant credit transfers from
  9 Jan 2025 and send them and offer **Verification of Payee** (IBAN–name match) from
  9 Oct 2025. Practical effect: the recipient name on the slip should match the account holder's
  name, or payers see a "no match / close match" warning. Croatian instant clearing runs through
  FINA's EuroNKSInst and TIPS (<https://www.fina.hr/platni-promet-i-platni-sustavi-za-poslovne-subjekte/platni-sustavi/euronksinst>).

## 7. Testing checklist

- [ ] Payload built by `hub3_barcode.py` without errors (lengths, charset, IBAN, model check).
- [ ] Amount in cents, 15 digits; currency `EUR`.
- [ ] Recipient name matches the account holder (VoP).
- [ ] Symbol: 9 columns, ECL 4, module 0.254 mm, ratio 3:1, ≤ 58 × 26 mm.
- [ ] Scanned successfully with at least 2–3 different Croatian bank apps (PDF on screen and on
      paper), and every field lands where expected.
- [ ] Test data only: fictitious payer names and a test IBAN from `hr_ids.py iban generate`.
