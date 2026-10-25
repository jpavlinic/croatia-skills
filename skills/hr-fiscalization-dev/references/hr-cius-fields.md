# HR CIUS 2025 – Croatian eRačun fields that trip up implementers

Status: researched 2026-10-25. Authoritative documents (porezna.gov.hr → Fiskalizacija 2.0 /
eRačun → Dokumentacija): *Specifikacija osnovne uporabe eRačuna s proširenjima* (version dated
**12.3.2026**), the PU UBL **validator / schematron in use from 15.3.2026**, official UBL samples,
and the field mapping in *Tehnička specifikacija Fiskalizacija eRačuna i eIzvještavanje* v1.15.
The HR-BR rule texts below were cross-checked against a third-party catalogue that quotes the
official schematron (einvoicechecker.com, accessed 2026-10-25) – **VERIFY** rule numbers and texts
against the current official schematron before relying on them.

Rule of thumb: generate EN 16931 UBL that passes the CEN rules (BR-xx, BR-CO-xx), then add the HR
layer below, then run **the PU validator** (or your intermediary's) on every template.

## 1. Header

| Field | UBL | HR requirement |
|---|---|---|
| BT-24 Specification identifier | `cbc:CustomizationID` | exactly `urn:cen.eu:en16931:2017#compliant#urn:mfin.gov.hr:cius-2025:1.0#conformant#urn:mfin.gov.hr:ext-2025:1.0` (HR-BR-5) |
| BT-23 Business process | `cbc:ProfileID` | `P1`–`P12` or `P99:<buyer's label>` (HR-BR-34), max 200 chars (HR-BR-42) |
| BT-1 Invoice number | `cbc:ID` | no whitespace (HR-BR-1); must follow the Zakon čl. 9 numbering (čl. 48(5)) |
| BT-2 Issue date | `cbc:IssueDate` | ≥ 2026-01-01 and < 2100-01-01 (HR-BR-40) – old test files from 2025 fail |
| HR-BT-2 Issue time | `cbc:IssueTime` | **mandatory**, `hh:mm:ss` (HR-BR-2) |
| BT-3 Type | `cbc:InvoiceTypeCode` / `cbc:CreditNoteTypeCode` | UNTDID 1001 subset (spec v1.15 Dodatak 18), e.g. 380 commercial, 381 credit note, 383 debit, 384 corrective, 386 prepayment, 389 self-billed, 326 partial |
| BT-5 Currency | `cbc:DocumentCurrencyCode` | `EUR` (spec v1.15 Table 6) |
| BT-9 Due date | `cbc:DueDate` | mandatory when amount due (BT-115) > 0 (HR-BR-4) |
| BG-3 Preceding invoice | `cac:BillingReference/cac:InvoiceDocumentReference` | must include `cbc:IssueDate` (HR-BR-6) |
| Copy indicator | `cbc:CopyIndicator` | `true` only for a non-tax correction re-sent under the same number (Zakon čl. 43) |
| Empty elements | – | none allowed except the signature element (HR-BR-33) |

Process types (spec v1.15 Dodatak 14): P1 orders under a contract · P2 periodic invoicing under a
contract · P3 unforeseen order · P4 advance payment · P5 spot payment · P6 payment before delivery
on order · P7 with despatch-advice reference · P8 with despatch and receipt-advice references ·
P9 credit note / negative invoicing · P10 corrective invoicing · P11 partial and final invoicing ·
P12 self-billing · P99 buyer-defined. (Some open-source READMEs give a different meaning for
P1–P12; ignore them and use this list.)

## 2. Parties, operator, identifiers

| Field | UBL | HR requirement |
|---|---|---|
| BT-34 Seller electronic address | `cac:AccountingSupplierParty/cac:Party/cbc:EndpointID` | mandatory (HR-BR-7); normally OIB with `schemeID="9934"` |
| BT-49 Buyer electronic address | `cac:AccountingCustomerParty/cac:Party/cbc:EndpointID` | mandatory (HR-BR-10); the identifier the buyer published in AMS |
| BT-31 / BT-48 VAT ID | `cac:PartyTaxScheme/cbc:CompanyID`, `cac:TaxScheme/cbc:ID = VAT` | `HR` + valid OIB (HR-BR-53) |
| HR-BT-5 Operator OIB | `cac:AccountingSupplierParty/cac:SellerContact/cbc:ID` | mandatory, valid OIB (HR-BR-9); same concept as F1 `OibOper` |
| HR-BT-4 Operator label | `cac:AccountingSupplierParty/cac:SellerContact/cbc:Name` | mandatory (HR-BR-37) |
| Buyer VAT ID | BT-48 | required when lines use category S, Z, E or AE (HR-BR-S-1, Z-1, E-1, AE-1 …) |

OIB check digit: ISO 7064 MOD 11,10 – see `croatia:hr-identifiers`.

## 3. Lines and KPD

| Field | UBL | HR requirement |
|---|---|---|
| KPD code | `cac:InvoiceLine/cac:Item/cac:CommodityClassification/cbc:ItemClassificationCode listID="CG"` | **every line** except prepayment invoices and credit notes (HR-BR-25, HR-BR-CL-2; Zakon čl. 42; spec v1.11 note); code must exist in **KPD 2025** |
| HR-BT-12 line HR VAT label | `cac:Item/cac:ClassifiedTaxCategory/cbc:Name` | mandatory for exempt / not-subject lines (HR-BR-16) |
| HR-BT-13/14 exemption reason / code | line tax category | mandatory for exempt / not-subject lines (HR-BR-36) |
| BT-149/150 base quantity | `cac:Price/cbc:BaseQuantity` | > 0 and same `unitCode` as invoiced quantity (HR-BR-20, -21) |
| Precision | prices, rates, quantities | max 10 decimals, 30 digits (HR-BR-56) |
| Lengths | BT-153 name < 1024, BT-154 description < 4096 | HR-BR-46, -47 |
| Order / despatch / receipt refs | line-level HR-BT-9/10/11 **or** header BT-13/16/15, never both | HR-BR-17, -18, -19 |

KPD 2025 (Klasifikacija proizvoda po djelatnostima, maintained by DZS – Zakon čl. 42): six-digit
code written `NN.NN.NN` (e.g. `62.01.11`). Look codes up in DZS **KLASUS**
(web.dzs.hr/App/klasus); help: `KPD@dzs.hr`. There is no official mapping from your product
catalogue: map each SKU/service once, store the code on the product, and have an accountant sign
off. A wrong KPD is a minor offence (Zakon čl. 73; see legal skill). PU's example for restaurant
service: 56.30.00 (PU F2 Q&A page).

## 4. VAT categories – EN codes plus HR labels

- EN 16931 `cbc:ID` (UNTDID 5305): `S` standard, `Z` zero, `E` exempt, `AE` reverse charge,
  `K` intra-EU, `G` export, `O` not subject (spec v1.15 Dodatak 19).
- **HR label** in `cbc:Name` of the tax category (HR-BT-22 at document level, HR-BT-12 on lines):
  allowed values (HR-BR-CL-1, as quoted by the third-party catalogue – **VERIFY** in table HR-TB-2
  of the official spec): `HR:PDV25`, `HR:PDV13`, `HR:PDV5`, `HR:Z`, `HR:K`, `HR:G`, `HR:AE`,
  `HR:E`, `HR:POVNAK`, `HR:PP`, `HR:PPMV`, `HR:O`, `HR:N`. Pattern in spec v1.15 Table 45:
  `HR:PDV<1–2 digits>` or `HR:<1–10 letters>`.
- `HR:POVNAK` (povratna naknada, deposit-return fee) and other amounts outside the tax base go to
  category `O` with tax 0 and require the HR totals block (HR-BR-29, -30, -32).
- Exemption reason: VATEX code (e.g. `VATEX-EU-132-1A`, mapped in Dodatak 16 to ZPDV čl. 39) and/or
  text; mandatory for `AE` (spec v1.15 Table 79) and for `E`.
- Rates: S > 0; Z, E, AE rate 0 (HR-BR-S-10, Z-10, E-10, AE-10). Croatian rates 25, 13, 5 (2026).
- Cash-accounting VAT (obračun po naplaćenoj naknadi, ZPDV čl. 125.i): carried both in BT-8 = 432
  and an HR extension field (HR-BT-15); practitioners report ambiguity about using both – **VERIFY**
  with the official spec and your intermediary.

## 5. HR extension block (HR-BG-2 / HR-BG-3)

Located in `ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/hrextac:HRFISK20Data` with
`hrextac:HRTaxTotal/hrextac:HRTaxSubtotal{cbc:TaxableAmount, cbc:TaxAmount,
hrextac:HRTaxCategory{cbc:ID, cbc:Percent, cbc:Name, cbc:TaxExemptionReason…}}` (spec v1.15
mapping tables). Required when the invoice has exempt / not-subject items, discounts or charges
(HR-BR-26, -30). Consistency rules: HR taxable amount = sum of line nets − discounts + charges −
non-taxable amount (HR-BR-27); HR total VAT = sum of HR category VAT = BT-110 (HR-BR-54, -55);
E/O category VAT = 0 (HR-BR-28). Copy the namespace URI and structure from the **official UBL
samples** (do not guess the namespace).

## 6. Minimal Invoice skeleton (illustrative)

```xml
<!-- TEMPLATE – not legal advice. Illustrative only: validate with the PU validator. Fictitious OIBs. -->
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
         xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
         xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:mfin.gov.hr:cius-2025:1.0#conformant#urn:mfin.gov.hr:ext-2025:1.0</cbc:CustomizationID>
  <cbc:ProfileID>P1</cbc:ProfileID>
  <cbc:ID>15/POSL1/2</cbc:ID>
  <cbc:IssueDate>2026-10-25</cbc:IssueDate>
  <cbc:IssueTime>14:03:00</cbc:IssueTime>
  <cbc:DueDate>2026-11-09</cbc:DueDate>
  <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>
  <cbc:DocumentCurrencyCode>EUR</cbc:DocumentCurrencyCode>
  <cac:AccountingSupplierParty><cac:Party>
    <cbc:EndpointID schemeID="9934">12345678903</cbc:EndpointID>
    <!-- PostalAddress, PartyTaxScheme (HR12345678903 / VAT), PartyLegalEntity ... -->
  </cac:Party>
  <cac:SellerContact><cbc:ID>98765432106</cbc:ID><cbc:Name>Operater 1</cbc:Name></cac:SellerContact>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty><cac:Party>
    <cbc:EndpointID schemeID="9934">52601815906</cbc:EndpointID>
    <!-- address, PartyTaxScheme HR52601815906 / VAT, legal entity ... -->
  </cac:Party></cac:AccountingCustomerParty>
  <!-- PaymentMeans (IBAN), TaxTotal + TaxSubtotal (S, 25, HR:PDV25 in TaxCategory/Name),
       LegalMonetaryTotal ... -->
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="H87">1</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="EUR">100.00</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Name>Licenca za softver – mjesečna pretplata</cbc:Name>
      <cac:CommodityClassification>
        <cbc:ItemClassificationCode listID="CG">00.00.00</cbc:ItemClassificationCode><!-- real KPD 2025 code here -->
      </cac:CommodityClassification>
      <cac:ClassifiedTaxCategory><cbc:ID>S</cbc:ID><cbc:Percent>25</cbc:Percent>
        <cac:TaxScheme><cbc:ID>VAT</cbc:ID></cac:TaxScheme></cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price><cbc:PriceAmount currencyID="EUR">100.00</cbc:PriceAmount></cac:Price>
  </cac:InvoiceLine>
</Invoice>
```
Element order matters in UBL (XSD sequence) – generate from the schema, not by string templates.
OIBs above are checksum-valid **fictitious** examples.

## 7. Validation workflow

1. XSD (UBL 2.1) → 2. CEN EN 16931 UBL schematron → 3. HR schematron (PU validator, version in
force) → 4. intermediary's own checks → 5. fiscalization response `prihvacenZahtjev=true`.
Keep a regression folder of real (anonymised) invoices per document type and process (380/P1,
381/P9, 386/P4, reverse charge, exempt line, povratna naknada) and run it in CI on every change
and whenever PU publishes a new validator.
