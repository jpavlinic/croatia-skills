# eVisitor, tourist tax and tourist board membership fee

Status: researched 2026-10-25. Main acts:
- Zakon o turističkoj pristojbi (ZoTP; NN 52/19, 32/20, 42/20)
- Pravilnik o najnižem i najvišem iznosu turističke pristojbe (NN 71/2019), still in kuna; euro
  figures below use the fixed rate 7.5345
- Zakon o članarinama u turističkim zajednicama (NN 52/19, 144/20)
- County decisions (odluke županijskih skupština) on the tourist tax for each year

## 1. eVisitor

eVisitor (www.evisitor.hr) is the national system, run by the Croatian National Tourist Board
(HTZ), for guest check-in and check-out, the tourist tax and statistics. The local tourist board
opens the account.

**Deadlines** (ZoTP čl. 22):
- Accommodation providers, including domaćinstvo and OPG: **check in every guest within 24 h of
  arrival, and check out within 24 h of departure** (čl. 22(1)).
- Holiday-home owners (vikendaši): register occupants within 24 h of arrival and deregister on the
  last day (čl. 22(2)). Flat-rate holiday-home owners register when they pay the flat amount (čl. 22(3)).
- Guests exempt under čl. 5(1) points 3, 4, 6 and 7 are not registered (čl. 22(9)). Children under 12
  **are** registered; they are exempt from the tax only.

**Data per guest**: name, sex, date and place of birth, citizenship, identity document type and
number, residence (country, city), arrival and departure dates, and the tax category
(exempt/50%/full). The guest must present an ID document. Collect only what eVisitor needs (GDPR
minimisation → `croatia:hr-legal-compliance`).

**Guest list / guest book**: eVisitor contains the official guest list (popis turista). Tourist
boards state that, under the guest-book rulebook (Pravilnik o knjizi gostiju …), a separate manual
guest list or guest book is no longer needed for renters who use eVisitor. **VERIFY** the current
rulebook. ZUD čl. 32(1)(5) still requires a guest list "in the prescribed form", and eVisitor is
that form.

**Foreign guests and MUP**: check-in through eVisitor also serves as the registration of the stay of
foreigners with the police (MUP), so no separate police registration is needed. **VERIFY** the
exact legal basis in the Zakon o strancima and the eVisitor FAQ.

**Ways to check in**: the eVisitor web app, the mVisitor mobile app, or a channel manager / PMS
connected to the eVisitor API. Several commercial tools offer document scanning; no endorsement.
Self check-in by guests is possible only through such tools. The host stays responsible.

**Developer notes:**
- eVisitor exposes a web-service interface for authorised software. Integration requires
  credentials issued per facility. Check the HTZ technical documentation (eVisitor wiki) for the
  current API and test environment. **VERIFY**.
- Store ID scans only if necessary. Many hosts keep only the eVisitor record. Define a retention
  period (`croatia:hr-legal-compliance`).

## 2. Tourist tax (turistička pristojba)

### Who pays
- Every person staying overnight in a facility in a municipality where they do not live (ZoTP čl. 4(1)1).
- The host collects it (in domaćinstvo it is included in the price) and pays it to the tourist board system.

### Exemptions and reductions
- **Exempt** (čl. 5(1)): children **under 12**; persons with ≥ 70% disability and one companion;
  people staying in the municipality for work (with proof); professional crews; approved school
  trips; social welfare beneficiaries; students living outside their home town during studies.
- **50%** (čl. 6): ages **12–18**; members of international youth-hostel organisations under 29.
- Proof is required (čl. 7).

### Per night (hotels, obrt and company facilities, and anyone not on the flat rate)

National range (Pravilnik NN 71/2019 čl. 2(1)). The county sets the exact local amount:

| Period | Minimum | Maximum |
|---|---|---|
| 1 Apr – 30 Sep | 10.00 kn ≈ **€1.33** | 20.00 kn ≈ **€2.65** |
| Rest of year | 7.00 kn ≈ **€0.93** | 14.00 kn ≈ **€1.86** |
| Camps, 1 Apr – 30 Sep | 8.00 kn ≈ €1.06 | 15.00 kn ≈ €1.99 |
| Camps, rest of year | 5.00 kn ≈ €0.66 | 10.00 kn ≈ €1.33 |

- The county may set up to two seasonal periods (ZoTP čl. 15(5)), and up to 30% less in assisted
  areas (development groups I–IV) (čl. 15(6); Pravilnik čl. 4(2)).
- **Collection** (non-flat payers): collect at payment, show it separately on the invoice (čl. 16),
  and remit for the **1st–15th and 16th–end of month periods** within **7 days** (čl. 17(1)).
- Euro rounding: county decisions express the amounts in euro. **VERIFY** the local decision. Some
  counties cap their maximum at €1.33 off-season.

### Flat amount for domaćinstvo and OPG (paušal turističke pristojbe)

- **Annual amount per bed** (main **and extra** beds), per camp unit, or per robinson capacity (ZoTP čl. 12).
- National range (Pravilnik NN 71/2019 čl. 2(2)):

| | Min / year | Max / year |
|---|---|---|
| Domaćinstvo, per bed | 350 kn = **€46.45** | 1,000 kn = **€132.72** |
| OPG, per bed | 200 kn ≈ **€26.54** | 500 kn = **€66.36** |
| Domaćinstvo camp / kamp odmorište / robinson, per unit | 500 kn = €66.36 | 1,000 kn = €132.72 |
| OPG camp / robinson, per unit | 250 kn ≈ €33.18 | 500 kn = €66.36 |

- If the county adopts no decision, the minimum applies (Pravilnik čl. 4(1)).
- The exact amount for each municipality or settlement is in the **county decision** (e.g. "Odluka o
  visini turističke pristojbe za 2026. godinu"). Some counties differentiate by settlement or zone.
  eVisitor shows the charge under "Financije".
- **Deadline** (ZoTP čl. 17(2)): the full amount by **31 July**, or three equal instalments by
  **31 July, 31 August and 30 September**. Use the payment slips from eVisitor (correct IBAN and
  reference number per municipality).
- First year or mid-year rješenje: eVisitor prorates or shows the obligation. Ask the local TZ. **VERIFY**.
- The flat rate is owed **regardless of occupancy**. The guest still sees "tourist tax included" in
  the price. Do not add it on top unless the price list says so (ZUD čl. 32(1)(2)).

**Calculation example** (illustrative): 2 apartments with 4 main beds and 2 extra beds = 6 beds.
In a municipality where the county set €90 per bed: 6 × €90 = **€540 per year**, either by 31 July
or as €180 on each of 31 Jul, 31 Aug and 30 Sep.

### Holiday-home owners (vikendaši): not tourism businesses, for context
- Owners of a non-commercial holiday house or flat pay for themselves and close family a flat amount
  per person (Pravilnik čl. 3): first and second member 60–250 kn (€7.96–33.18), each further member
  25–100 kn (€3.32–13.27), with a 70% reduction for the owner and close family (ZoTP čl. 13(2)).
  Deadline: **15 July** (čl. 17(3)). Others staying pay per night.
- Hosting paying guests in such a property without a rješenje is illegal renting, not "vikendaš" use.

### Fines (ZoTP čl. 26–29)
The consolidated text still lists kuna. Converted amounts are indicative. **VERIFY** the euro amounts
in Narodne novine:
- Domaćinstvo: missing the flat-rate deadline or not registering guests: 2,000–10,000 kn
  (≈ €265–1,327); repeat offence 4,000–20,000 kn (≈ €531–2,654); on-the-spot fine 1,000 kn
  (≈ €133) (čl. 28).
- Operators (obrt/company) not remitting, collecting, or registering guests: up to 25,000 kn
  (≈ €3,318), and 50,000 kn (≈ €6,636) for a repeat offence (čl. 26–27).
- Debts lapse after 5 years (čl. 18).

## 3. Tourist board membership fee (turistička članarina)

- **Who**: renters in domaćinstvo and OPG who do not keep business books pay an **annual flat fee
  per bed** (Zakon o članarinama u TZ čl. 11). Bookkeeping businesses (obrt on real income, d.o.o.)
  pay a percentage of turnover instead.
- **2026 amounts** (unchanged since 2023, per tourist board notices for 2026):
  - domaćinstvo: **€5.97 per main bed**, **€2.99 per extra bed** (50%);
  - OPG: €2.65 per bed;
  - camp in domaćinstvo: €13.94 per unit; robinson: €2.65 per bed.
  - **VERIFY**: the implementing rulebook may differentiate by the tourist class (turistički razred)
    of the municipality. Most coastal tourist boards publish €5.97 / €2.99.
- **TZ-2 form**: file **electronically via ePorezna by 15 January** for the previous year. The FINA
  e-form service is a paid alternative. Select the **municipality where the property is**, not your
  residence. File one TZ-2 per municipality. The form also asks for last year's turnover from the EP
  book, which is informational and does not change the fee.
- **Payment**: in one sum by **31 July**, or in three instalments: **31 July, 31 August, 30 September**.
  A renter who got the rješenje during the year pays once **by 31 December**.
- Pay to the municipality's account with the reference number (poziv na broj) from the local TZ or
  Porezna instructions.
- Fines for not filing TZ-2: €500–5,000 (per tourist-board guidance, 2026). **VERIFY** in the act.

## 4. Who to ask
- Local **turistička zajednica** (TZ): eVisitor account, flat-rate amounts, payment slips.
- **HTZ eVisitor help desk**: technical issues.
- **Porezna uprava** local office: TZ-2, flat-rate income tax, PDV-ID.
- **County** official gazette: the tourist tax decision.
