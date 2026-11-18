# Names, vocative, grammatical case and gender in UI strings

Read this when a template inserts a person's name, a place, a number or a product into Croatian
text; when writing e-mail greetings; or when a string depends on the user's gender. Letter and e-mail
etiquette in general (Poštovani, sign-offs, Vi/vi) is in `croatia:croatian-language`.

## 1. Why concatenation breaks Croatian

Croatian has seven cases; the form of a noun depends on its role in the sentence:

| Template (English-style) | Croatian result | Correct |
|---|---|---|
| `"Poslano korisniku " + name` | *Poslano korisniku Ana Horvat* | *Poslano korisnici Ani Horvat* (dative, feminine) |
| `"Dobrodošli, " + name` | *Dobrodošli, Ivan* | *Dobro došli, Ivane* (vocative) — or avoid the name |
| `"Dostava u " + city` | *Dostava u Zagreb* (accusative = direction) vs *Dostava u Zagrebu* (locative = location) — and *u Hvar* is wrong for the island | look up the form (places.md) |
| `name + " vam je poslao poruku"` | gender of the verb follows the sender | *Ana vam je poslala poruku* |
| `"Obrisati " + item + "?"` | object in accusative: *Obrisati datoteka?* | *Obrisati datoteku?* |

The greeting is two words (*Dobro došli!*); *dobrodošao* in one word is only the adjective
(*dobrodošla pomoć*).

Rules for templates:

1. **Put the variable in the nominative**, as a label, not inside the sentence:
   - *Pošiljatelj: Ana Horvat* · *Grad: Split* · *Datoteka: izvjestaj.pdf*
   - *Novu poruku poslao je korisnik: Ana Horvat* (awkward) → better: *Nova poruka – Ana Horvat*.
2. **Translate whole sentences**, never fragments ("You have" + n + "new messages").
3. **Use ICU `select` for gender and `plural` for numbers**; let the translator write each variant.
4. If the form must be inflected (place names, the vocative), take it from data (`assets/toponyms.csv`,
   a vocative table) or from a conservative helper, never from naive string rules.

## 2. Gender agreement

Past tense, adjectives and many nouns change with the person's gender:

| Neutral English | Masculine | Feminine | Gender-neutral rewrite |
|---|---|---|---|
| You signed in | Prijavio si se / Prijavili ste se | Prijavila si se / Prijavili ste se | **Prijava je uspjela.** / *Prijavljeni ste.* |
| X commented | X je komentirao | X je komentirala | *Novi komentar: X* |
| user | korisnik | korisnica | *korisnik/korisnica*; or *korisnički račun*, *osoba* |
| Are you sure? | Jeste li sigurni? (polite Vi → plural form, no gender) | same | — |

- The polite **Vi** form uses masculine-plural agreement ("Jeste li **sigurni**", "Vi ste se
  **prijavili**") for both genders — a useful way to avoid gender in UI.
- Slash forms (*Prijavio/la se*, *korisnik/ca*) are understandable but clumsy; acceptable in forms
  and system messages, not in marketing text. Prefer a rewrite with a noun or the passive:
  *Uspješna prijava*, *Promjene su spremljene*, *Račun je izrađen*.
- ICU select:

```text
{gender, select,
  male {{name} je komentirao vašu objavu.}
  female {{name} je komentirala vašu objavu.}
  other {Novi komentar na vašoj objavi: {name}}
}
```

Store gender only if you need it and the user gave it (GDPR minimisation → `croatia:hr-legal-compliance`);
never guess gender from the first name for anything visible.

## 3. Declension of personal names (reference)

| Who | Rule | Examples |
|---|---|---|
| Male first names, consonant-final | decline like masculine nouns | Ivan, Ivana, Ivanu, **Ivane** (V) |
| Male first names in -o / -e | -o/-e declension | Marko, Marka, Marku, **Marko** (V); Ante, Ante, Anti, **Ante** |
| Male names in -a | like feminine nouns | Luka, Luke, Luki, **Luka** (V); Nikola |
| Female names in -a | decline | Ana, Ane, Ani, **Ana** (V, neutral) |
| Female names, consonant-final | **do not decline** | Ines, Nives, Karmen (all cases) |
| Male surnames | **decline** | Horvat, Horvata, Horvatu; Babić, Babića, Babiću |
| Female surnames | **do not decline**, except those ending in -a | *gospođi Horvat*, *s Anom Babić*; but *Ani Desnici* |
| Foreign names | decline by sound, keep the original spelling; no apostrophe or hyphen (IHJJ 6.3) | *Johna*, *Smitha*; IHJJ: *Hemingwaya*, *Shakespearea* (G) |

IHJJ (*Jezični savjetnik*): foreign names and surnames are declined like Croatian ones — "Kao što se
sklanja npr. Ivan Horvat, Ivana Horvata, Ivanu Horvatu…, tako treba sklanjati i strano…".

In software, **don't decline names automatically** except in the narrow, tested cases of §4.
Put names in the nominative after a colon or as the subject.

## 4. Vocative in greetings — current guidance

### What the sources say

- **First names (male)**: the vocative is used: *Dragi Ivane*, *Poštovani Petre*, *Marko*, *Luka*.
- **First names (female)**: in conventional, stylistically neutral address the vocative **equals the
  nominative** — *Draga Ana*, *Draga Marija*, *Poštovana Ivana*. Forms in -o (*Ano*, *Marijo*) are
  emotionally marked/colloquial (jezicni-savjetnik.com, "(Gotovo) sve o vokativu", a private
  language blog, not IHJJ's jezicni-savjetnik.hr; Težak–Babić,
  *Gramatika hrvatskoga jezika*). Never generate the -o form.
- **Names in -ica (female and male)** are the exception: the standard vocative ends in **-ice** —
  *Draga Ankice*, *Draga Danice*, *Draga Ljubice*, *Dragi Ivice*, *Dragi Jurice*, *Dragi Perice* (same
  article, points 6 and 7: "imena na -ica također imaju u vokativu nastavak -e: Danice, Dragice,
  Ivice, Perice"). The nominative (*Draga Ankica*) is heard, but -ice is the neutral written form.
  Foreign names spelled with -ica and pronounced with *k* (*Monica*, *Jessica*) do not take it.
- **Male surnames after a title** (*gospodine*, *profesore*, *doktore*):
  - Older normative view (Težak, Ham, Raguž): surnames have a vocative — *gospodine Horvate*, *Babiću*.
  - Handbooks already allow the **nominative** for many surname types (-ac/-ak/-ek, surnames that are
    common nouns like Novak, Kolar, ending in -k/-g/-h/-c or a vowel), and Težak argued the norm
    should also allow *gospodine Petrović*.
  - Usage research (A. Orlić, "Vokativ prezimena muških osoba u suvremenom hrvatskom jeziku",
    2022, hrcak.srce.hr/clanak/410750): in *Poštovani gospodine Horvat/Horvate/Horvatu* 94 % chose
    the nominative *Horvat*; the more formal the situation, the more the nominative prevails; even -ić
    surnames (*Kovačić*, *Milić*) are mostly left in the nominative, although handbooks prescribe -iću.
  - IHJJ's Jezični savjetnik ("profesore Kovačić > profesore Kovačiću"): in formal address surnames in
    -ić are declined (*poštovani gospodine Kovačiću*), and the vocative of male surnames that do not
    end in -ić equals the nominative (*poštovani gospodine Kaliterna / Mimica / Hodak / Horvat*).
  - Conclusion for software, following IHJJ: **decline -ić surnames (*Poštovani gospodine Babiću,*)
    and leave all other male surnames in the nominative (*Poštovani gospodine Horvat,*).** The
    nominative for -ić surnames is common in everyday usage; offer it only as an option.
- **Female surnames**: never declined: *Poštovana gospođo Kovač*, *Poštovana gospođo Babić*.
- Do not combine title + first name in formal address (*gospođo Ana* is familiar); use the surname.
- No abbreviations in the salutation: *Poštovani gospodine Horvat*, not *Poštovani g. Horvat*.

### Safe patterns

| Situation | Use |
|---|---|
| Formal, gender known (m) | `Poštovani gospodine {surname},` → *Horvat,* but *Babiću,* for surnames in -ić |
| Formal, gender known (f) | `Poštovana gospođo {surname},` |
| Formal, gender unknown | `Poštovani,` (or `Poštovani/Poštovana,`) |
| Informal, first name, m, vocative known | `Dragi {vocative},` → *Dragi Ivane,* |
| Informal, first name, f | `Draga {name},` → *Draga Ana,*; names in -ica: *Draga Ankice,* |
| Informal, gender or vocative unknown | `Dobar dan,` (no name) or `Poštovani,`; `Bok, {first}!` only if the brand voice uses *ti* |
| Push/notification text | avoid names in the vocative; *Vaša narudžba je poslana.* |

IHJJ continues in lower case after the salutation comma; a capital letter is common in e-mails.
Details in `croatia:croatian-language` (e-mail reference).

### The helper (`scripts/hr_text.py vocative` / `greeting`)

Conservative by design — it returns the nominative unless it is sure:

- names in -ica from a curated set, male and female → -ice (*Ivica → Ivice*, *Ankica → Ankice*); any
  other name in -ica (*Monica*) → unchanged with `confident=False`;
- female or unknown name in -a → unchanged (*Ana*, *Ivana*);
- male name ending in a vowel → unchanged (*Marko*, *Ante*, *Luka*, *Mario*);
- male consonant-final names → only from a curated table (*Ivan → Ivane*, *Petar → Petre*,
  *Matej → Mateju*, *Aleksandar → Aleksandre*…) or the safe suffixes *-mir/-slav* (+e) and *-ej* (+u);
- deliberately **not** declined: names ending in -k/-g/-h/-c where palatalisation would apply
  (*Dominik*, *Patrik*), names with disputed forms (*Juraj*, *Domagoj*), and all foreign names
  (*John*) → returned unchanged with `confident=False`;
- male surnames in -ić → *-iću* (*Babić → Babiću*); all other surnames, and all female surnames →
  unchanged; `decline_ic=False` keeps -ić surnames in the nominative.

```text
$ python3 scripts/hr_text.py vocative Petar --gender m       → Petre
$ python3 scripts/hr_text.py vocative Dominik --gender m     → Dominik  (not confident - nominative kept)
$ python3 scripts/hr_text.py vocative Ivica --gender m       → Ivice
$ python3 scripts/hr_text.py greeting --first Ivan --last Horvat --gender m            → Poštovani gospodine Horvat,
$ python3 scripts/hr_text.py greeting --first Ivan --last Babić --gender m             → Poštovani gospodine Babiću,
$ python3 scripts/hr_text.py greeting --first Ivan --last Horvat --gender m --informal → Dragi Ivane,
```

When `confident` is false in an informal greeting, fall back to *Dobar dan,* without the name rather than
printing a possibly wrong vocative. Let users correct how they are addressed if the product greets by
name often (store an optional "vocative/how to address you" field).

## 5. Inserting numbers and dates into sentences

- Numbers → ICU plural with full sentences (plurals.md).
- Dates in running text use the genitive month: *Narudžba stiže 25. listopada.* Use the date formatter
  with `day` + `month:'long'`, never a nominative month array.
- "On Monday" → *u ponedjeljak* (accusative, unchanged for masculine weekdays), *u srijedu*, *u subotu*,
  *u nedjelju* (feminine → accusative -u). Keep the whole phrase in the message:
  `{weekday, select, monday {u ponedjeljak} wednesday {u srijedu} ...}`.
- Ordinals: *1. mjesto*, *2. kat* — the dot is the ordinal marker; don't append "st/nd/th"-style
  suffixes.
