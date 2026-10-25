# Fiskalizacija računa u krajnjoj potrošnji (B2C receipts, "F1") – implementation reference

Status: researched 2026-10-25. Primary sources: Zakon o fiskalizaciji (NN 89/25), Pravilnik o
fiskalizaciji računa u krajnjoj potrošnji (NN 153/25, amended NN 97/26), and *Fiskalizacija računa
u krajnjoj potrošnji – Tehnička specifikacija za korisnike* **v2.7** (APIS IT, versions 16.06.,
06.07. and 21.07.2026), with WSDL packages `Fiskalizacija-WSDL-EDUC_v1.10.zip` (test) and
`Fiskalizacija-WSDL-PROD_v1.10.zip` (production). "Spec §x" below means that v2.7 document.
Who must fiscalize, and which sales: see `croatia:hr-legal-compliance` (reference 04, §1).

## Contents
1. Legal and spec timeline that affects code
2. Message flow
3. Endpoints, transport, timeouts
4. RacunZahtjev: data set and XML names
5. ZKI
6. XML signature (XMLDSig)
7. JIR and the response
8. Receipt number and sequencing
9. Printed receipt content and QR code
10. Offline mode, late delivery, device failure
11. Storno, refunds and corrections
12. Other methods (payment change, tips, echo, working hours)
13. Business premises (poslovni prostor)
14. Certificates

## 1. Timeline that affects code

| Date | Change | Source |
|---|---|---|
| 1.7.2017 | Business premises are registered only in ePorezna; XML premises messages abolished | Spec §2 notes |
| 1.1.2021 | QR code mandatory on every fiscalized receipt | Spec §2 notes |
| 1.1.2023 | Amounts in EUR (XML schema unchanged) | Spec §2 notes |
| 1.1.2024 | Tip (napojnica) fiscalization method | Spec §2.3 |
| 1.9.2025 | New Act in force; "prateći dokumenti" methods removed; payment method **C (ček) removed**; certificates from any trusted-list QTSP with OIB accepted | Zakon čl. 80; Spec §2 notes |
| 1.1.2026 | Bank-transfer B2C sales in scope; `OibPrimateljaRacuna` for B2B cash/card (Zakon čl. 39); new method `PromijeniPodatkeRacuna`; working-hours methods; **restrictive errors** reject a receipt (`s013`) | Zakon čl. 15(6); Spec §2 notes |
| 1.5.2026 | Production accepts RSA-SHA256 as well as RSA-SHA1; eIDAS trusted-list certificates accepted | Spec §2 notes |
| 1.7.2026 | **Test** rejects RSA-SHA1 signatures and TLS 1.1 | Spec §2 notes; PU notice 6.7.2026 |
| 8.9.2026 05:00 | Production response-signing certificate *fiskalcis* replaced | PU notice (porezna.gov.hr, F1 news) |
| **1.1.2027** | **Production rejects RSA-SHA1 signatures and TLS 1.1.** Pravilnik NN 97/26 in force (certificate from any eIDAS QTSP; signature and hash methods defined by the Tehnička specifikacija) | Spec §2 notes; NN 97/26 čl. 5, 13 |

**Action item for any system still signing with RSA-SHA1:** migrate to RSA-SHA256 and TLS 1.2+
before 1.1.2027 and retest on cistest.

## 2. Message flow (Pravilnik čl. 8; Spec §2.1)

1. Build the receipt data and compute the **ZKI** (§5).
2. Build `RacunZahtjev`, sign it with the fiscal certificate (enveloped XMLDSig, §6).
3. Open 1-way TLS to the Fiscalization System (server presents `cis.porezna-uprava.hr`,
   test `cistest.apis-it.hr`).
4. Call the service (synchronous SOAP).
5. The system returns `RacunOdgovor` with the **JIR**, signed with the *fiskalcis* certificate
   (test: *fiskalcistest*). Verify the response signature.
6. Print/deliver the receipt with JIR, ZKI and QR.

On any error (schema, signature, timeout, no internet) the sale **must not be blocked**: issue the
receipt without JIR (ZKI and QR with `zki=` still printed) and re-send later (Pravilnik čl. 9(3);
Zakon čl. 21). Current receipts have priority over the backlog when the connection returns.

## 3. Endpoints, transport, timeouts (Spec §3, §6.1)

| Environment | URL | Server TLS cert | Response signing cert |
|---|---|---|---|
| Test | `https://cistest.apis-it.hr:8449/FiskalizacijaServiceTest` | `cistest.apis-it.hr` (FINA Demo CA) | `fiskalcistest` |
| Production | `https://cis.porezna-uprava.hr:8449/FiskalizacijaService` | `cis.porezna-uprava.hr` (FINA RDC CA) | `fiskalcis` |

- SOAP 1.1, document-literal, WS-I, UTF-8, TCP port **8449** outbound.
- TLS 1.2 or 1.3 with AES (Spec §3.2). TLS 1.1: rejected in test since 1.7.2026, in production
  from 1.1.2027.
- Test maintenance windows: working days 16:00–17:00, Sundays 08:00–12:00 (Spec §6.1).
- Timeout: chosen by you; the system's processing target is **2 seconds** from request in to
  response out (Pravilnik čl. 10(3)). A practical POS timeout is a few seconds, then fall back to
  offline mode (§10). Working-hours methods: about 10 s (Pravilnik čl. 19(10)).
- Network sizing recommendation: symmetric link, min. 2 Mb/s for up to 40 msg/s at 6 KB (Spec §3.1).
- Do **not** hard-pin the leaf certificates: PU rotates *fiskalcis*/*fiskalcistest* (e.g.
  8.9.2026 production; July 2026 test). Trust the issuing CA chain and alert on expiry.

## 4. RacunZahtjev (Pravilnik Privitak 1; Spec §2.1.1, §9.1)

Namespace `http://www.apis-it.hr/fin/2012/types/f73`, root `tns:RacunZahtjev` with an `Id`
attribute (referenced by the signature).

| XML element | Meaning | Req. | Format / rule |
|---|---|---|---|
| `Zaglavlje/IdPoruke` | message UUID | yes | new UUID for **every** send, including retries |
| `Zaglavlje/DatumVrijeme` | send time | yes | `dd.mm.yyyyThh:mm:ss` |
| `Racun/Oib` | issuer OIB | yes | must equal the OIB in the certificate (`s005`) |
| `USustPdv` | in VAT system | yes | `true`/`false` |
| `DatVrijeme` | issue date/time | yes | `dd.mm.yyyyThh:mm:ss`; not in the future (177), not >30 days old (176) |
| `OznSlijed` | sequence level | yes | `P` premises, `N` device |
| `BrRac/BrOznRac` | numeric number | yes | digits, no leading zeros, ≠0 (178), ≤20 |
| `BrRac/OznPosPr` | premises label | yes | `[0-9a-zA-Z]{1,20}`, unique per OIB |
| `BrRac/OznNapUr` | device number | yes | digits, no leading zeros, ≤20, unique per premises |
| `Pdv/Porez/{Stopa,Osnovica,Iznos}` | VAT per rate | if VAT | rate as `25.00`; allowed rates 0, 5, 13, 25 (182) |
| `Pnp/Porez/...` | consumption tax | if any | 0.00–3.00 % (183/184) |
| `OstaliPor/Porez/{Naziv,Stopa,Osnovica,Iznos}` | other taxes | if any | |
| `IznosOslobPdv` | VAT-exempt amount | if any | Decimal(15,2) |
| `IznosMarza` | margin scheme amount | if any | |
| `IznosNePodlOpor` | not subject to tax | if any | |
| `Naknade/Naknada/{NazivN,IznosN}` | fees (e.g. povratna naknada) | if any | |
| `IznosUkupno` | total | yes | Decimal(15,2), `.` separator, may be negative |
| `NacinPlac` | payment method | yes | `G` gotovina, `K` kartice, `T` transakcijski račun, `O` ostalo (also for mixed payments) |
| `OibOper` | operator OIB | yes | formally valid (179); issuer's OIB allowed where no operator (Zakon čl. 8(4)) |
| `ZastKod` | ZKI | yes | 32 lower-case hex |
| `NakDost` | late delivery flag | yes | `true` when the receipt was issued without JIR |
| `ParagonBrRac` | paper-book receipt number | no | only after total device failure |
| `SpecNamj` | reserved | no | |
| `OibPrimateljaRacuna` | buyer OIB | no | only B2B paid cash/card under Zakon čl. 39; **not with `T`** (181); valid OIB (180) |

Mobile apps and online card payments map to `K` or `O` depending on the instrument; there is no
separate code. **VERIFY** the mapping for wallets/BNPL with your adviser.

## 5. ZKI – zaštitni kod izdavatelja (Spec §12; Pravilnik čl. 13–16)

```
input = OIB + datVrij + BrOznRac + OznPosPr + OznNapUr + IznosUkupno
        datVrij = 'dd.MM.yyyy HH:mm:ss'   <- SPACE, not the 'T' of the XML
        IznosUkupno with '.' decimal separator, e.g. 1245.56
signature = RSA PKCS#1 v1.5 sign(input as UTF-8, private key of the fiscal certificate)
ZKI = lower-case hex MD5(signature bytes)   -> 32 chars
```

- Spec v2.7 §12.1 pseudocode and Java/.NET samples use **RSA-SHA256** (`SHA256withRSA`);
  earlier spec versions and Pravilnik NN 153/25 čl. 16(2) said RSA-SHA1. NN 97/26 (from 1.1.2027)
  replaces the fixed algorithm with "methods defined in the Tehnička specifikacija".
  **VERIFY** with APIS IT (`fiskalizacija.help@apis-it.hr`) whether ZKIs computed with SHA1 remain
  acceptable until 31.12.2026; new code should use SHA256.
- PKCS#1 v1.5 signatures are deterministic, so the same inputs always give the same ZKI: you must
  be able to reproduce it on request (Spec §12). Store the exact input fields.
- The amount string must be the same value as `IznosUkupno` (keep two decimals; a storno uses
  `-105.50`).
- `scripts/zki.py build|commands|sign|from-signature` builds the string and prints the exact
  `openssl` pipeline:

```bash
printf '%s' '1234567890325.10.2026 14:03:0015POSL12145.68' \
  | openssl dgst -sha256 -sign fiskal-key.pem -binary \
  | openssl dgst -md5 -r | cut -c1-32
```
(Example OIB 12345678903 is fictitious. Never `echo` without `-n`: a trailing newline changes the ZKI.)

## 6. XML signature (Spec §7)

- Enveloped XMLDSig inside the signed root (`RacunZahtjev`, `PromijeniPodatkeRacunaZahtjev`, …).
- `Reference URI="#<Id of root>"`; Transforms: `…xmldsig#enveloped-signature` then
  `http://www.w3.org/2001/10/xml-exc-c14n#`.
- `CanonicalizationMethod`: `http://www.w3.org/2001/10/xml-exc-c14n#` (mandatory).
- `SignatureMethod`: `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256`;
  `DigestMethod`: `http://www.w3.org/2001/04/xmlenc#sha256`. RSA-SHA1/SHA1 only until 31.12.2026
  in production. Not every "stronger" algorithm is accepted; an unsupported one gives `s004`.
- `KeyInfo/X509Data/X509Certificate` (Base64). Spec examples also include `X509IssuerSerial`.
- The response is signed with the same family of algorithm as the request, but always with
  **inclusive** c14n (`http://www.w3.org/TR/2001/REC-xml-c14n-20010315`) – make your verifier
  accept that.
- Typical `s004` causes: pretty-printing or re-serialising the XML after signing, signing the SOAP
  envelope instead of the root element, a namespace prefix added after signing, wrong `Id`.

## 7. JIR and the response (Pravilnik čl. 6–7; Spec §2.1.3)

- `RacunOdgovor` contains `Zaglavlje/IdPoruke` (echoed), `DatumVrijeme`, and `Jir` on success or
  `Greske/Greska/{SifraGreske,PorukaGreske}` on error.
- JIR is a UUID: 36 characters, 32 hex digits in groups 8-4-4-4-12 (Pravilnik čl. 7).
- The receipt counts as reported only when a valid signed response with JIR arrives (Pravilnik
  čl. 9(4)).

## 8. Receipt number and sequencing (Zakon čl. 9)

- Printed and sent as three parts: `numerički broj / oznaka poslovnog prostora / oznaka naplatnog
  uređaja`, e.g. `1234567890/POSL1/12` (Pravilnik Privitak 2).
- Unbroken sequence without gaps, per premises (`OznSlijed=P`) or per device in the premises
  (`N`); each calendar year or tax period may restart from any number (čl. 9(4)).
- Rules, premises list and device numbering go in the internal act (interni akt, čl. 9(3)).
- Allocate the number **inside a transaction with a lock per sequence key** before signing;
  never reuse a number after a failed send (re-send the same receipt instead).
- `scripts/receipt_number.py` formats, parses and checks a list for gaps/duplicates.

## 9. Printed receipt content and QR

Fiscal elements (Zakon čl. 7(1)), in addition to the general invoice content required by VAT law
(see `croatia:hr-legal-compliance`):
1. time of issue (hour and minute), 2. operator label (oznaka operatera, mapped to an OIB in the
internal act, čl. 8), 3. payment method (novčanice, kartica, transakcijski račun, ostalo), 4. JIR,
5. ZKI, 6. QR code.

QR content (Spec §2.7; Pravilnik čl. 17):

```
https://porezna.gov.hr/rn?jir=<JIR>&datv=YYYYMMDD_HHMM&izn=<cents>
https://porezna.gov.hr/rn?zki=<ZKI>&datv=YYYYMMDD_HHMM&izn=<cents>   (receipt without JIR)
```
`izn` = total in euro cents, no separators, no leading zeros, `-` for negative, max 10 chars
(145,68 € → `14568`). Physical rules (Pravilnik čl. 18): model 1 or 2, smallest version, ≥ 2 × 2 cm,
quiet zone ≥ 2 mm, ECC ≥ L, ISO/IEC 15415, no logo. `scripts/fiscal_qr.py` builds the URL.

Documents with payment details issued **before** the receipt (pro-forma, order confirmation,
payment-provider receipt) must say **"OVO NIJE FISKALIZIRANI RAČUN"** (Zakon čl. 29).

## 10. Offline mode, late delivery, device failure

- Connection lost (Zakon čl. 21): issue receipts with all čl. 7 data except JIR; re-establish the
  connection and deliver every such receipt within **2 working days** from the day of the outage,
  with `NakDost=true`. The system then returns a JIR (čl. 21(6)); you do not reprint.
- Use the original `DatVrijeme` and ZKI; generate a **new** `IdPoruke` for each attempt.
- In the test validation (`ProvjeraZahtjev`), lateness shows as v174 (10 min–2 days), v152
  (>2–5 days), v153 (>5 days).
- Total device failure: paper book of receipts (uvezana knjiga računa, Zakon čl. 22; Pravilnik
  čl. 37–38) and later entry with `ParagonBrRac`. No internet available at all: HAKOM certificate
  procedure (Pravilnik čl. 39–42).

## 11. Storno, refunds and corrections (Zakon čl. 24; Spec §2.1.6)

- A storno or (partial) return is a **new fiscalized receipt** with its own number and negative
  amounts (čl. 24(2) allows fiscalizing receipts with a negative sign). Reference the original
  number in the receipt text (good practice; no dedicated XML field in F1).
- Payment method or buyer OIB wrong on an already fiscalized receipt: same day, until midnight,
  use `PromijeniPodatkeRacunaZahtjev` (or the older `PromijeniNacPlacZahtjev`). After midnight:
  storno the original and issue a new receipt (Spec §2.1.6; Pravilnik čl. 11–12).
- The last accepted change message wins (Spec §2.1.6 notes).

## 12. Other methods (Spec §2.1.6, 2.3, 2.4, 2.5, 2.8)

| Method / root element | Use | Success | Specific errors |
|---|---|---|---|
| `PromijeniNacPlacZahtjev` | change payment method, same day | `p001` | `s007` date ≠ today, `s008` data differ / not fiscalized |
| `PromijeniPodatkeRacunaZahtjev` | change payment method and/or buyer OIB, same day (from 1.1.2026); carries the original data plus `PromijenjeniNacinPlac` / `PromijenjeniOibPrimateljaRacuna` | `p005` | `s011`, `s012` |
| `NapojnicaZahtjev` | tip on a fiscalized receipt (`Napojnica/iznosNapojnice`, `nacinPlacanjaNapojnice`) | `p002` | `s009` receipt date >2 days old, `s010` |
| `EchoRequest` | connectivity check; no certificate or signature check | echo text | – |
| `ProvjeraZahtjev` | **test only**: validates a receipt against rules, returns v-codes | – | see testing reference |
| working-hours methods (prijava, brisanje, dohvat, lista poslovnih prostora) | report opening hours via the service | `p003`, `p004` | Privitak 4 |

## 13. Business premises (poslovni prostor)

- Register each premises (including an online shop, mobile shop, vending device) **before**
  issuing receipts, via **ePorezna** (Pravilnik čl. 19(1), (8)); report changes of address, hours,
  activity, closure and of the software producer/maintainer (čl. 19(2)).
- Online shop: the address is the seat or residence; hours may be 0–24 (čl. 19(4)–(5)).
- The premises label you register is the `OznPosPr` you send.
- Self-service devices get an ISU (9 digits) from PU; the number is `broj/OznPosPr/ISU`
  (Pravilnik čl. 29–30).

## 14. Certificates (Pravilnik čl. 2–3 as amended by NN 97/26; Spec §5, §11)

- Production: a certificate containing the taxpayer's **OIB** from a trust-service provider. Since
  1.5.2026 certificates from QTSPs on the eIDAS trusted lists are accepted; legal-person profile
  per ETSI EN 319 412-3 with `organizationIdentifier` (OID 2.5.4.97) = `VATHR-<OIB>` (Spec §11).
  Existing FINA "Fiskal" application certificates remain valid until expiry (NN 97/26 čl. 12).
- Test: a **DEMO** certificate. FINA demo certificates are free, valid 2 years; request through
  `certifikati-fiskalizacija@fina.hr` or a FINA office; the custodian (skrbnik) receives activation
  data by e-mail and SMS (fina.hr). A software company may test with its own demo certificate
  (Spec §6). Production certificates are refused on test and vice versa (except foreign issuers).
- Non-Croatian issuer: announce it to `fiskalizacija.help@apis-it.hr` at least one month before
  going live (Spec §6).
- Handling: the `.p12`/`.pfx` and its password are secrets. Keep them in a secret manager or HSM,
  never in git, images or logs; restrict file permissions; monitor expiry (FINA application
  certificates are typically 5 years – **VERIFY** for your issuer); test renewal on cistest first.
  One certificate per OIB can serve many devices (Pravilnik čl. 2(3)); the OIB in the certificate
  must match `Racun/Oib`.
