# Sources, spec versions and open-source libraries

Status: researched 2026-10-25. Re-check versions before every integration project: PU replaces
documents in place and the change history inside each PDF is the only reliable changelog.

## 1. Law and rulebooks

| Document | Version / status | Where |
|---|---|---|
| Zakon o fiskalizaciji | NN 89/25; in force 1.9.2025; eRačun part from 1.1.2026; non-VAT issuing from 1.1.2027 (čl. 80) | narodne-novine.nn.hr/clanci/sluzbeni/2025_06_89_1233.html |
| Pravilnik o fiskalizaciji računa u krajnjoj potrošnji | NN 153/25, from 1.1.2026; Privitci 1–7 = data sets and error codes | narodne-novine.nn.hr/clanci/sluzbeni/2025_12_153_2278.html |
| Pravilnik o izmjenama i dopunama (B2C) | NN 97/26 (2.9.2026), **in force 1.1.2027**: eIDAS QTSP certificates with OIB; signature/hash methods per Tehnička specifikacija; old certificates valid to expiry | narodne-novine.nn.hr/clanci/sluzbeni/2026_09_97_1181.html |
| Pravilnik o eRačunu | NN 11/26: AS4, AMS/MPS lookup steps, CIS DEMO, data use | narodne-novine.nn.hr/clanci/sluzbeni/full/2026_01_11_88.html |
| Legal obligations, penalties, VAT/OSS | – | `croatia:hr-legal-compliance` reference 04 |

## 2. Technical specifications (porezna.gov.hr / porezna-uprava.gov.hr)

| Document | Latest version found | Notes |
|---|---|---|
| Fiskalizacija računa u krajnjoj potrošnji – Tehnička specifikacija za korisnike | **v2.7** (16.06., 06.07., 21.07.2026) | RSA-SHA256, TLS 1.1/RSA-SHA1 removal dates, eIDAS certs, ZKI ch. 12, QR ch. 2.7, error codes ch. 2.1.5 and 13. File: `UserDocsImages/Fiskalizacija/Tehničke specifikacije/Fiskalizacija - Tehnicka specifikacija za korisnike_v2.7 (21.07.2026.).pdf` |
| F1 WSDL/XSD | `Fiskalizacija-WSDL-EDUC_v1.10.zip`, `Fiskalizacija-WSDL-PROD_v1.10.zip` | attachments of spec v2.7 (ch. 14) |
| Tehnička specifikacija Fiskalizacija eRačuna i eIzvještavanje | **v1.15** (6.2.2026) | methods, XAdES-B, endpoints :8509, code lists; WSDLs "Fiskalizacija eRačuna – wsdl", "eIzvještavanje – wsdl" |
| Specifikacija osnovne uporabe eRačuna s proširenjima (HR CIUS + HR EXT 2025) | dated **12.3.2026** | CustomizationID, HR-BT/HR-BR, HR-TB code lists |
| Validator (UBL schematron) | "dorađena verzija – u primjeni od 15.3.2026." | community reports file `HRUBLSchematron_13032026-2` (**VERIFY**) |
| UBL 2.1 eRačun samples, fiscalization message samples | published with the documentation | use them as golden files |

Portal pages: porezna.gov.hr/fiskalizacija/gotovinski-racuni (F1 news, spec link) ·
porezna.gov.hr/fiskalizacija/bezgotovinski-racuni/eracun and …/fiskalizacija-bezgotovinskih-racuna
(F2 documentation) · porezna-uprava.gov.hr/hr/fiskalizacija-eracuna-azurirano-17-4-2026/8049
(F2 Q&A, updated 5.6.2026) · porezna-uprava.gov.hr/hr/popis-informacijskih-posrednika/8019
(intermediaries, 37 entries on 16.10.2026) · porezna-uprava.gov.hr/hr/klasifikacija-proizvoda-kpd-2025/7718
· Q&A PDF "Pitanja i odgovori vezani uz Zakon o fiskalizaciji".

PU notices used: "Obavijest obveznicima fiskalizacije u krajnjoj potrošnji – tehnička unapređenja"
(6.7.2026: SHA1/TLS 1.1 dates) · replacement of production *Fiskalcis* certificate 8.9.2026 05:00 ·
expiry of DEMO *Fiskalcistest* certificate mid-July 2026.

## 3. Certificates

- FINA: fina.hr → Poslovni digitalni certifikati → Poslovni certifikati za fiskalizaciju
  (production and demo application certificates); demo FAQ: free, 2-year validity, request via
  `certifikati-fiskalizacija@fina.hr`.
- Other QTSPs on the EU/HR trusted lists may issue certificates with the OIB
  (`organizationIdentifier = VATHR-<OIB>`, ETSI EN 319 412-3) – accepted since 1.5.2026 per spec
  v2.7; foreign issuers must be announced to APIS IT.
- KPD 2025 lookup: DZS KLASUS, web.dzs.hr/App/klasus; `KPD@dzs.hr`.

## 4. Open-source libraries (found on GitHub, 2026-10-25)

**No endorsement.** Before using any of these, check: last commit date, whether it implements
spec **v2.7** (RSA-SHA256 signing, `OibPrimateljaRacuna`, `PromijeniPodatkeRacuna`, payment code
`C` removed) or HR CIUS 2025 / F2 spec v1.15, licence, tests against cistest, and how it handles
the private key. Many older F1 libraries sign with RSA-SHA1, which production rejects from
**1.1.2027**.

| Language | Repository | Scope (from its README) | Last push seen |
|---|---|---|---|
| PHP | `nticaric/fiskalizacija` | F1 API client | 2026-10 |
| PHP | `stboris/laravel-eracun` | read/build/validate HR CIUS 2025 UBL | 2026-08 |
| PHP | `GTCrais/hr-einvoicing` | Laravel HR CIUS UBL + an intermediary client | 2026-10 |
| Python | `senko/fiskal-hr` | F1 client | 2023-12 (likely pre-2026 spec) |
| Python | `kodmasin/fiskpy` | F1 client | 2022-06 (likely pre-2026 spec) |
| Python | `boris-savic/python-eracun` | eRačun | 2026-08 |
| Java | `aradovanJava/Fiskalizacija` | F1 (historic) | 2013 (outdated) |
| .NET | `tgrospic/Cis.Fiscalization` | F1 wrapper | 2020 (likely pre-2026 spec) |
| .NET | `MAES-Software/MAES.Fiskal` | F1 for POS/invoicing | 2026-05 |
| .NET | `MAES-Software/MAES.Fiskal2`, `pervanluka/Fiskalizacija2` | F2 / intermediaries | 2026 |
| Node/TS | `shunkica/fiskalizacija2-js` | Croatian fiscalization library for Node.js | 2026-08 |
| Docs | `shunkica/fiskalizacija2` | collected F2 documents/XSLT | 2026-07 |
| Docs | `dageci/eracun-fiskalizacija-datumi` | community notes on HR CIUS date fields (explicitly unofficial) | 2026-10 |

Java has no well-maintained public F1 library found; Java teams typically generate a JAX-WS/CXF
client from the WSDL and sign with Apache Santuario (F1) or EU DSS (F2 XAdES-B; spec v1.15 §11.2
has a DSS example).

## 5. Third-party sources used only as pointers (verify against primary)

- einvoicechecker.com/hr/eracun-greske – HR-BR rule catalogue quoting the PU schematron.
- Community forum "Fiskalizacija za developere" (forum.hr) – practical issues; not authoritative.
