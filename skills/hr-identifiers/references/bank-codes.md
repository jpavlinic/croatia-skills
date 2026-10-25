# Croatian IBAN, bank codes (VBDI) and BIC/SWIFT

## IBAN structure

Source: HNB *Odluka o transakcijskim računima*, NN 13/2025
(<https://narodne-novine.nn.hr/clanci/sluzbeni/2025_01_13_123.html>), čl. 5–11.

```
HR kk VVVVVVV AAAAAAAAAA        21 characters, no spaces in data
|  |  |       └ broj (partija) računa – 10 digits, 10th = check digit (čl. 11)
|  |  └ vodeći broj (VBDI, bank code) – 7 digits, 7th = check digit (čl. 10)
|  └ IBAN check digits, ISO 13616-1 mod 97 (čl. 9)
└ country code HR (čl. 7–8)
```

- IBAN check: move the first 4 characters to the end, letters → numbers (A = 10 … Z = 35), the
  number % 97 must be 1 (ISO 13616-1 / ISO 7064 MOD 97-10).
- **Inner check digits** (Croatia-specific, often forgotten): the 7th digit of the bank code and
  the 10th digit of the account are ISO 7064 **MOD 11,10** check digits over the preceding 6 and 9
  digits ("prema hrvatskoj normi HRN ISO/IEC 7064"). An IBAN can pass mod 97 and still be invalid
  here – `hr_ids.py iban validate` checks both.
- Display: groups of 4 (`HR12 1001 0051 8630 0016 0`); store without spaces. Formatting for UI is
  covered by `croatia:hr-localization`.
- Payment institutions and e-money institutions also have VBDI codes (e.g. Aircash below).
- Banks must check the structure and check digits of the payee IBAN (Odluka čl. 6).

## Bank codes and BIC – snapshot

Source: HNB, *Vodeći brojevi pružatelja platnih usluga*, page updated **27.3.2025**:
<https://www.hnb.hr/temeljne-funkcije/platni-promet/vodeci-brojevi-pruzatelja-platnih-usluga>
(downloadable table on the same page). Credit institutions list with OIB/MB:
<https://www.hnb.hr/temeljne-funkcije/supervizija/popis-kreditnih-institucija>.

**VERIFY against the live HNB table before hard-coding.** Banks merge (codes of merged banks stop
being issued; old IBANs may be migrated) and BICs change with renames. All codes below pass their
own MOD 11,10 check digit.

| VBDI | Institution (HNB spelling) | BIC (8) |
|---|---|---|
| 2500009 | Addiko Bank d.d. Zagreb | HAABHR22 |
| 2481000 | Agram banka d.d. Zagreb | KREZHR2X |
| 4501006 | Aircash d.o.o. Zagreb | – |
| 4133006 | Banka Kovanica d.d. Varaždin | SKOVHR22 |
| 2488001 | BKS Bank AG, Glavna podružnica Hrvatska | BFKKHR22 |
| 2485003 | Croatia banka d.d. Zagreb | CROAHR2X |
| 2402006 | Erste & Steiermärkische Bank d.d. Rijeka | ESBCHR22 |
| 1001005 | Hrvatska narodna banka | NBHRHR2X |
| 2390001 | Hrvatska poštanska banka d.d. Zagreb | HPBZHR2X |
| 2492008 | Imex banka d.d. Split | IMXXHR22 |
| 2380006 | Istarska kreditna banka Umag d.d. | ISKBHR2X |
| 2489004 | J&T banka d.d. Varaždin | VBVZHR22 |
| 2400008 | Karlovačka banka d.d. | KALCHR2X |
| 4124003 | KentBank d.d. Zagreb | KENBHR22 |
| 2407000 | OTP banka d.d. Split | OTPVHR2X |
| 2408002 | Partner banka d.d. Zagreb | PAZGHR2X |
| 2386002 | Podravska banka d.d. Koprivnica | PDKCHR2X |
| 2340009 | Privredna banka Zagreb d.d. | PBZGHR2X |
| 2484008 | Raiffeisenbank Austria d.d. Zagreb | RZBHHR2X |
| 2403009 | Samoborska banka d.d. | SMBRHR22 |
| 2412009 | Slatinska banka d.d. | SBSLHR2X |
| 2360000 | Zagrebačka banka d.d. | ZABAHR2X |

For a bank picker, derive the bank from the IBAN (characters 5–11) instead of asking the user;
the script's lookup table mirrors this snapshot.

HNB publishes BICs with spaces ("ZABA HR 2X"); the 8-character BIC is the same without spaces.
The 11-character form adds a branch code (`XXX` = head office). Since SEPA, BIC is not needed for
euro transfers within the EEA; derive it from the VBDI only for display, never require the user
to type it.

## BIC structure (ISO 9362)

`AAAA BB CC (DDD)`: 4 letters institution, 2 letters country (`HR`), 2 alphanumeric location,
optional 3 alphanumeric branch. `hr_ids.py bic validate` checks the shape and looks up the table
above.

## Test data

- `python3 scripts/hr_ids.py iban generate --bank 2340009 --count 5 --seed 1` – fictitious,
  checksum-valid (mod 97 + both inner MOD 11,10 digits). A random account number can coincide with
  a real account: never use generated IBANs for real payments.
- Fictitious documentation example: `HR2323400091234567897` (PBZ bank code, invented account).
- Public, real accounts (fine to show, never send test payments): state budget
  `HR1210010051863000160` (HNB).

## Keeping current

- HNB VBDI/BIC table (page date shown on the page) – re-check yearly and after bank mergers.
- Odluka o transakcijskim računima – replaced NN 57/2019 with NN 13/2025; check for amendments.
