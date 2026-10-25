# Place names: u / na, genitive, "from" forms, ethnics

Read this when a template inserts a Croatian place name ("Smještaj u …", "Dostava iz …",
"Najbolji restorani na …"), when building location pages or filters, or when you need county data.
For SEO slugs and local landing pages see `croatia:hr-seo-local`; for tourism specifics
`croatia:hr-tourism-rentals`.

## 1. The data file: `assets/toponyms.csv`

236 rows (UTF-8, comma-separated):

| Column | Meaning | Example |
|---|---|---|
| `name` | nominative | Hvar |
| `type` | `grad` (one of the 128 legal cities/towns), `otok`, `poluotok`, `regija`, `općina/naselje`, `država` | otok |
| `county` | county (županija) without the word "županija"; `Grad Zagreb` | Splitsko-dalmatinska |
| `genitive` | genitive | Hvara |
| `locative` | locative **with its preposition** | na Hvaru |
| `from_form` | "from" phrase (`iz` + G for u-places, `s`/`sa` + G for na-places) | s Hvara |
| `ethnic_m`, `ethnic_f` | inhabitant nouns (only where IHJJ lists them) | Hvaranin, Hvaranka |
| `source` | `IHJJ` = forms read from IHJJ's list "Etnici i ktetici" (hrvatski.hr/etnici-i-ktetici); `rule` = composed by the skill author from regular declension | IHJJ |
| `note` | county seat, island/town distinction, **VERIFY** flags | island; town = u |

Coverage: all **128 legal cities/towns** (which include every county seat and every town with ≥ 10 000
inhabitants, 2021 census), 36 islands + Pelješac, 21 regions, 49 municipalities/tourist places, and
Hrvatska. 123 rows come from IHJJ; 18 rows carry a VERIFY note (fleeting *a*, adjectival declension,
plural-only names).

Lookup: `python3 scripts/hr_text.py place Hvar` (diacritics-insensitive: `place sibenik` works).

Ethnic parentheses are IHJJ notation for optional parts: `(Donjo)miholjčanin` = *Miholjčanin* or
*Donjomiholjčanin*. Optional endings (*Slavonskog(a) Broda*, *u Slavonskom(e) Brodu*) were normalised
to the shorter form; the longer one is equally correct.

## 2. u or na

- Towns and cities: **u** — *u Zagrebu, u Splitu, u Rijeci, u Puli, u Osijeku, u Dubrovniku, u Zadru*.
- Islands and peninsulas: **na** — *na Hvaru, na Krku, na Rabu, na Braču, na Pagu, na Pelješcu*.
- **Town and island with the same name are different places**: IHJJ (Cres, Hvar, Korčula, Krk, Pag,
  Rab, Vis, Lastovo): "Kad se misli na otok, lokativ dolazi isključivo uz prijedlog *na*, a kad se misli na
  istoimeno naselje, isključivo uz prijedlog *u*." The CSV has two rows for each (type `grad` vs `otok`).
  *Apartmani u Hvaru* = in Hvar town; *apartmani na Hvaru* = anywhere on the island.
- Mainland exceptions with *na*: some regions and areas — *na Banovini, na Kvarneru, na Žumberku,
  na Plitvičkim jezerima, na Lovreću*; IHJJ also records local *na Rijeci* and *na Klisu* (surrounding
  villages) but the standard choice is *u Rijeci*, *u Klisu*.
- Regions: *u Istri, u Dalmaciji, u Slavoniji, u Lici, u Zagorju, u Međimurju, u Gorskom kotaru,
  u Konavlima*.
- Plural names: *u Vinkovcima, u Križevcima, u Kaštelima, u Bujama, u Delnicama, u Našicama, u Pločama,
  u Vodicama, u Sesvetama; na Brijunima, na Kornatima*.
- Adjectival names decline like adjectives: *u Imotskom(e), iz Imotskog(a); u Jastrebarskom; u Novom
  Vinodolskom; u Malinskoj; u Makarskoj*.
- Fleeting *a*: *Zadar – Zadra – u Zadru; Sisak – Siska; Karlovac – Karlovca; Bakar – Bakra; Supetar –
  Supetra; Ozalj – Ozlja*.

## 3. Direction vs location vs origin

| Meaning | Case | Example |
|---|---|---|
| where (location) | u/na + locative | *Smještaj u Splitu / na Braču* |
| where to (direction) | u/na + accusative | *Putujemo u Split / na Brač* (accusative = nominative for inanimate masculine; *u Rijeku*, *u Puli* ✗ → *u Pulu*) |
| from | iz/s + genitive | *Polazak iz Splita / s Brača* |
| towards/near | prema, kod + dative/genitive | *prema Zadru*, *kod Zadra* |

The accusative is not in the CSV: for masculine and neuter names it equals the nominative
(*u Zagreb, na Hvar, u Đakovo*); feminine -a names take -u (*u Rijeku, u Pulu, na Šoltu*); plurals
take the accusative plural (*u Vinkovce, na Brijune*). For anything else, rephrase with a label.

`s` vs `sa`: *sa* before *s, š, z, ž* and before clusters like *ps-, ks-* (*sa Šolte, sa Silbe,
sa Zlarina, sa Žirja, sa Suska*); otherwise *s* (*s Hvara, s Krka, s Brača, s Pelješca*).

## 4. Template strategy

1. Prefer label syntax when the place comes from user data: *Lokacija: Split*.
2. For known places, store the inflected forms with the record (`locative`, `genitive`, `from_form`)
   and use them in templates: `Najbolji restorani {locative}` → *Najbolji restorani na Hvaru*.
3. For unknown places (user-entered villages), do not inflect automatically: *Smještaj – Mjesto: Ivinj*.
4. Capitalisation: only the first word and proper-name parts are capitalised: *Slavonski Brod,
   Biograd na Moru, Dugi otok, Plitvička jezera, Gorski kotar* (pravopis rules on multi-word names).

## 5. Counties (županije) — ISO 3166-2:HR

| Code | Official name | Seat |
|---|---|---|
| HR-01 | Zagrebačka županija | Zagreb |
| HR-02 | Krapinsko-zagorska županija | Krapina |
| HR-03 | Sisačko-moslavačka županija | Sisak |
| HR-04 | Karlovačka županija | Karlovac |
| HR-05 | Varaždinska županija | Varaždin |
| HR-06 | Koprivničko-križevačka županija | Koprivnica |
| HR-07 | Bjelovarsko-bilogorska županija | Bjelovar |
| HR-08 | Primorsko-goranska županija | Rijeka |
| HR-09 | Ličko-senjska županija | Gospić |
| HR-10 | Virovitičko-podravska županija | Virovitica |
| HR-11 | Požeško-slavonska županija | Požega |
| HR-12 | Brodsko-posavska županija | Slavonski Brod |
| HR-13 | Zadarska županija | Zadar |
| HR-14 | Osječko-baranjska županija | Osijek |
| HR-15 | Šibensko-kninska županija | Šibenik |
| HR-16 | Vukovarsko-srijemska županija | Vukovar |
| HR-17 | Splitsko-dalmatinska županija | Split |
| HR-18 | Istarska županija | Pazin |
| HR-19 | Dubrovačko-neretvanska županija | Dubrovnik |
| HR-20 | Međimurska županija | Čakovec |
| HR-21 | Grad Zagreb | Zagreb (city with county status) |

Legal basis: *Zakon o područjima županija, gradova i općina u Republici Hrvatskoj* (narodne-novine.nn.hr).
Code assignment per ISO 3166-2:HR — **VERIFY** against the ISO Online Browsing Platform before using
the codes as foreign keys. In dropdowns, sort with the Croatian collator, or list *Grad Zagreb* first
(common practice); "županija" can be dropped in a field labelled *Županija*.

## 6. Keeping the data current

- Cities: 128 since 2013 (*Zakon o područjima…*); a change needs an amendment published in Narodne
  novine — re-check after local-government reforms.
- Population threshold: 2021 census (DZS, dzs.hr); next census 2031.
- Postal codes are not in this file: validation and lookup → `croatia:hr-identifiers`.
- Extend the CSV in your project, not in the plugin (plugin files are replaced on update): copy it to
  e.g. `data/toponyms.csv` and add rows, marking self-composed forms as `rule` + VERIFY.
