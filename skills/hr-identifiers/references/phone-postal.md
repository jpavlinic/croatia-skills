# Phone numbers, postal codes, vehicle plates

Display formatting (spacing, how numbers and addresses look in UI) belongs to
`croatia:hr-localization`; this file is about structure and validation.

## 1. Phone numbers – HAKOM numbering plan

Source: HAKOM, *Plan numeriranja*, NN 45/2023 (26.4.2023.), adopted under Zakon o elektroničkim
komunikacijama (NN 76/22): <https://narodne-novine.nn.hr/eli/sluzbeni/2023/45/783/pdf>.
Primary assignments per operator: data.gov.hr dataset "Popis primarne dodjele numeracija
operatora elektroničkih komunikacija".

Structure: country code **385**, international prefix `00` (or `+`), national prefix **`0`**
(not part of the national significant number, NSN). E.164 max 15 digits. E.164 form:
`+385` + NSN, no spaces, no leading 0 (e.g. `+38512345678`, `+385912345678`).

### Table 1 – NDC (national destination code) and NSN length (incl. NDC)

| NDC | NSN length | Use |
|---|---|---|
| 1 | 8 | geographic – Grad Zagreb and Zagrebačka županija |
| 20 | 8–9 | Dubrovačko-neretvanska |
| 21 | 8–9 | Splitsko-dalmatinska |
| 22 | 8–9 | Šibensko-kninska |
| 23 | 8–9 | Zadarska |
| 31 | 8–9 | Osječko-baranjska |
| 32 | 8–9 | Vukovarsko-srijemska |
| 33 | 8–9 | Virovitičko-podravska |
| 34 | 8–9 | Požeško-slavonska |
| 35 | 8–9 | Brodsko-posavska |
| 40 | 8–9 | Međimurska |
| 42 | 8–9 | Varaždinska |
| 43 | 8–9 | Bjelovarsko-bilogorska |
| 44 | 8–9 | Sisačko-moslavačka |
| 47 | 8–9 | Karlovačka |
| 48 | 8–9 | Koprivničko-križevačka |
| 49 | 8–9 | Krapinsko-zagorska |
| 51 | 8–9 | Primorsko-goranska |
| 52 | 8–9 | Istarska |
| 53 | 8–9 | Ličko-senjska |
| 60 | 6–8 | special tariff – general content |
| 609 | 6–8 | special tariff – humanitarian (Zakon o humanitarnoj pomoći) |
| 61 | 6–8 | special tariff – voting |
| 64 | 8 | special tariff – content unsuitable for children |
| 65 | 8 | special tariff – prize games |
| 69 | 8 | special tariff – services for children |
| 72 | 8 | uniform (single) access number |
| 74, 75 | 8 | personal number services |
| 800, 801 | 7–9 | free call (the plan's notes also mention prepaid internet calling-card services in this block – **VERIFY** which NDC) |
| 890xy, 89xy | 10 | M2M |
| 90x, 91, 92, 93, 94, 95, 96, 97x (975x, 975xy) | 9 | mobile networks |
| 98 | 8–9 | mobile network |
| 99 | 9 | mobile network |

Reserved: 2x (x = 4–9), 3x (x = 0, 6–9), 4x (x = 1, 5–6), 5x (x = 0, 4–9), 6x (x = 2, 3, 6–8),
7x (x = 0, 1, 3, 6–9), 8x (x = 1–7). In practice mobile numbers seen most are 091, 092, 095,
097, 098, 099.

**Do not infer the operator from the mobile prefix** – number portability makes the prefix only
the original allocation.

Short codes (Table 2): **112** EU emergency, **192** police, **193** fire brigade, **194**
ambulance, **195** sea search and rescue, **1987** road assistance, 116xxx harmonised European
services (116000 missing children, 116006 victims of crime, 116016 violence against women,
116111 children, 116117 medical, 116123 emotional support), 118xx directory enquiries. Short
codes have no E.164 form.

### Normalising user input

`python3 scripts/hr_ids.py phone normalize "091 234 5678"` → `+385912345678`, type `mobile`.

Accepts `+385`, `00385`, `385…` and national `0…`, removes spaces, `-`, `/`, `.`, brackets and the
common `(0)` in `+385 (0)1 …`. Validates the NSN length per NDC; returns type and region.
Validation is structural – it cannot tell whether a number is assigned. For SMS sending, require
`mobile` type. Store E.164; format for display only at the edge.

## 2. Postal codes (poštanski brojevi)

- 5 digits, written before the place name (`10000 ZAGREB`; in addresses the place is often
  uppercase). For mail from abroad, `HR-10000` is accepted. Hrvatska pošta's addressing guide:
  <https://www.posta.hr/pravilno-adresiranje-posiljaka>.
- Authoritative lists: search places by code <https://www.posta.hr/pretrazivanje-mjesta-s-pripadajucim-postanskim-brojem>,
  Zagreb streets (Zagreb has several codes by street, e.g. 10000, 10010, 10020, 10040, 10090,
  10110 – look up the street) <https://www.posta.hr/pretrazivanje-ulica-u-gradu-zagrebu>, and the
  download page for post offices/parcel lockers/Zagreb streets
  <https://www.posta.hr/preuzimanje-podataka-o-postanskim-uredima>.
- Approximate regions by first two digits (mirrors the old phone area codes – **VERIFY** for edge
  places near county borders): 10 Zagreb city and county · 20 Dubrovnik-Neretva · 21
  Split-Dalmatia · 22 Šibenik-Knin · 23 Zadar · 31 Osijek-Baranja · 32 Vukovar-Srijem · 33
  Virovitica-Podravina · 34 Požega-Slavonia · 35 Brod-Posavina · 40 Međimurje · 42 Varaždin · 43
  Bjelovar-Bilogora · 44 Sisak-Moslavina · 47 Karlovac · 48 Koprivnica-Križevci · 49
  Krapina-Zagorje · 51 Primorje-Gorski kotar · 52 Istria · 53 Lika-Senj.
- Special codes exist outside the "place" pattern: P.O. boxes (`p.p. 421, 10001 ZAGREB` in
  Hrvatska pošta's own examples) and parcel lockers (`64801 KOPRIVNICA` in the same guide). Do not
  reject a 5-digit code just because it is not a town's main code; validate against the official
  list when exactness matters.
- `hr_ids.py postcode check 21000` → shape OK + approximate region.

## 3. Vehicle registration plates (brief)

Source: *Pravilnik o registraciji i označavanju vozila*, NN 130/2017 (and amendments),
<https://narodne-novine.nn.hr/clanci/sluzbeni/2017_12_130_2993.html>.

- Standard plate: area code + Croatian coat of arms + registration number of **3 or 4 digits and
  1 or 2 letters** (čl. 18 st. 2), e.g. `ZG 1234-AB` (fictitious). Black characters on white
  reflective background (čl. 18 st. 1).
- Area codes (Prilog 1, referenced in čl. 57 st. 2): BJ Bjelovar, BM Beli Manastir, ČK Čakovec,
  DA Daruvar, DE Delnice, DJ Đakovo, DU Dubrovnik, GS Gospić, IM Imotski, KA Karlovac,
  KC Koprivnica, KR Krapina, KT Kutina, KŽ Križevci, MA Makarska, NA Našice, NG Nova Gradiška,
  OG Ogulin, OS Osijek, PU Pula, PŽ Požega, RI Rijeka, SB Slavonski Brod, SK Sisak, SL Slatina,
  ST Split, ŠI Šibenik, VK Vinkovci, VT Virovitica, VU Vukovar, VŽ Varaždin, ZD Zadar, ZG Zagreb,
  ŽU Županja.
- Store without the coat of arms; normalise to `AREA 1234-AB`. Special plates (diplomatic,
  police, army, temporary/export, personalised) follow other rules – the script validates only
  the standard pattern. Which letters may appear in the letter group (e.g. whether Č/Ć/Đ/Š/Ž or
  Q/W/X/Y are used) is not checked strictly – **VERIFY** in the Pravilnik if you need it.
- `hr_ids.py plate check "ST 123-AB"`.
