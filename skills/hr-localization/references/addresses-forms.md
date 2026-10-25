# Addresses, phone display and form fields for Croatia

Read this when designing address/phone/name forms for Croatian users, formatting addresses for
labels or invoices, or importing address data. Validation of postal codes, phone numbers, OIB and
IBAN → `croatia:hr-identifiers`.

## 1. Address format (Hrvatska pošta)

Examples published by Hrvatska pošta ("Pravilno adresiranje pošiljaka", posta.hr):

```text
gosp. Hrvoje Poštić            Poduzeće d.o.o.            prof Ivan Ivanović
Maksimirska ulica 72           n/r Mare Primatelj         Jadranovo
31000 OSIJEK                   Jurišićeva 120             Matije Gupca 10K
                               10000 ZAGREB               51260 CRIKVENICA
```

Line order:

1. Recipient (person or company; `n/r` = *na ruke*, "attention of"; `(kod Radić)` = c/o).
2. Settlement name **only if it differs from the post office** (*Jadranovo* above, served by the
   51260 Crikvenica post office).
3. Street and house number: `Ilica 1`, `Maksimirska ulica 72`, `Perićeva ulica 28/1`, `Matije Gupca 10K`
   (letter suffix), or `p.p. 421` (poštanski pretinac, P.O. box, with its own postal code 10001).
4. Postal code (5 digits) + post office name; Hrvatska pošta writes the place in capitals on mail.
   In UI and invoices normal case is fine: `10000 Zagreb`.
5. International mail: country on the last line (`HRVATSKA` / `CROATIA`), optional `HR-` before the
   postal code.

Single-line form: **`Ilica 1, 10000 Zagreb`** (street + number, comma, postal code + place).

- House number after the street name, never before (*Ilica 1*, not *1 Ilica*).
- `bb` = *bez broja* (no number): `Industrijska zona bb, 31000 Osijek`. Allow it in the house-number field.
- Street names are often genitive personal names without "ulica": *Ulica Matije Gupca* = *Matije Gupca*;
  *Trg bana Josipa Jelačića*. Don't try to normalise them; store as entered.
- Floor and flat: `Ilica 1, 3. kat, stan 12` (ordinal dot on the floor). Optional free-text line.
- Districts/quarters (*Trnje, Sesvete*) are not part of the postal address in Zagreb; settlements in
  multi-settlement municipalities are (line 2).

## 2. Recommended form fields

| Field | Label (hr) | Notes |
|---|---|---|
| Name | *Ime*, *Prezime* (or one *Ime i prezime*) | allow č ć đ š ž, hyphen, apostrophe, spaces; female surnames like *Horvat-Kovač* |
| Company | *Naziv tvrtke* | optional; OIB field for B2B (`croatia:hr-identifiers`) |
| Street + number | *Ulica i kućni broj* | one field is friendlier than separate street/number; if split, number accepts `10K`, `28/1`, `bb` |
| Additional | *Kat, stan, ulaz (neobvezno)* | |
| Settlement | *Mjesto* | needed when it differs from the post office; autocomplete from postal data |
| Postal code | *Poštanski broj* | 5 digits; can prefill the post office name |
| Post office / city | *Grad / pošta* | |
| County | *Županija* | rarely needed for delivery; list in places.md §5 |
| Country | *Država* | default *Hrvatska* |
| Phone | *Broj mobitela* / *Telefon* | accept spaces, `+385`, leading `0`; store E.164 |
| E-mail | *E-adresa* / *Adresa e-pošte* | |

- No "State/Province" or "ZIP code" labels; no US-style address order.
- Mark optional fields with *(neobvezno)* rather than marking required ones with `*`, or do both
  consistently (accessibility).
- Autocomplete attributes still use the English tokens (`autocomplete="postal-code"`, `"address-line1"`).

## 3. Phone number display (convention, not a standard)

| Type | National display | International display | E.164 storage |
|---|---|---|---|
| Zagreb landline (area code 1) | `01 234 5678` | `+385 1 234 5678` | `+38512345678` |
| Other landline (e.g. Split 021) | `021 123 456` | `+385 21 123 456` | `+38521123456` |
| Mobile (e.g. 091, 092, 095, 097, 098, 099) | `091 234 5678` | `+385 91 234 5678` | `+385912345678` |

- Drop the leading `0` after `+385`. Users type `0912345678`, `091/234-5678`, `+385 91 234 5678`,
  `00385…`; normalise to E.164 on input, format on output.
- Grouping varies in practice (`01 2345 678` is also common); pick one style per product.
  Validation, number ranges and lengths → `croatia:hr-identifiers`.
- Use `tel:` links with E.164: `<a href="tel:+38512345678">01 234 5678</a>`.

## 4. Personal data minimisation

Collect only what the purpose needs (date of birth, gender, OIB are often not needed). Legal basis,
retention and privacy notices → `croatia:hr-legal-compliance`.
