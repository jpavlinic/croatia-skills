# Choosing the legal form – 2026

Status: researched 2026-10-25. Figures are for **2026**. **VERIFY** marks unconfirmed points. Detail per form:
`pausalni-obrt.md`, `obrt-dohodak.md`, `doo-jdoo.md`.

Contents: 1 Forms in one line · 2 Comparison table · 3 How to choose · 4 Typical paths · 5 Activity codes and
regulated activities

---

## 1. The forms in one line

- **Obrt** (sole trader, Zakon o obrtu): the owner (obrtnik) is the business; **unlimited personal liability**.
  Three tax regimes:
  - **paušalni obrt** – fixed tax by class, receipts ≤ €60,000, not in VAT;
  - **obrt na dohodak** – real income (receipts − expenses), books KPI/DI;
  - **obrt na dobit** – profit tax, double-entry books (mandatory above €1M receipts).
- **Slobodno zanimanje** (liberal profession, ZPD čl. 29 st. 2): lawyers, doctors, architects, engineers,
  translators, consultants etc. registered with their chamber; real income only, no paušal.
- **j.d.o.o.** (simple LLC): capital from €1, max 5 members and 1 director, template founding, 1/4 of profit to
  reserves until capital reaches €2,500 (ZTD čl. 390.a).
- **d.o.o.** (LLC): capital €2,500 (ZTD čl. 389), liability limited to the company's assets.
- **d.d.** (joint-stock company): capital €25,000 (ZTD čl. 162). Not for a small business.
- **Udruga / zadruga:** non-profit association / cooperative – not vehicles for an owner's profit (`doo-jdoo.md` §9).

## 2. Comparison table (2026)

| | Paušalni obrt | Obrt na dohodak | j.d.o.o. / d.o.o. |
|---|---|---|---|
| **Setup cost** | Registration free (since 1.9.2021, per guides – **VERIFY**); fiscal certificate, software | Same | START: court fee only (guides: ~€4 j.d.o.o. / ~€27 d.o.o. – **VERIFY**); notary route roughly €150–500 (market estimate) + capital (€1 / €2,500, at least €625 paid in for d.o.o.) |
| **Setup time** | Online e-Obrt/START: days; law allows up to 15 days | Same | START: typically a few working days (**VERIFY**); notary route 1–2 weeks |
| **Liability** | Unlimited, all personal assets | Unlimited | Limited to company assets (director liability for breaches) |
| **Tax on profit** | Fixed: €203.40–€1,080/yr (12% of class income) | City rates 15–23% / 25–33% (threshold €60,000 base) | Profit tax 10% (< €1M revenue) / 18% |
| **Owner contributions** | €290.98/month (main activity) or annual reduced (employed elsewhere) or 0 (pensioner) | €472.84/month (base €1,295.45) | Director not employed elsewhere: €727.45/month (base €1,993) even with no salary; otherwise salary contributions |
| **Bookkeeping** | KPR only; PO-SD by 15.1. – usually DIY | KPI, DI, annual DOH by end Feb – accountant advisable | Double entry, GFI to FINA by 30.4., PD by 30.4. – accountant in practice (~€100–250/mo, estimate) |
| **VAT** | Must be outside VAT (≤ €60,000) | Exempt ≤ €60,000 or VAT payer | Exempt ≤ €60,000 or VAT payer |
| **Taking money out** | Free (owner's money) | Free | Salary (taxed) or dividend 12% after 10% profit tax (≈ 20.8% total) |
| **Chamber fees** | HOK €11.40/month (first 2 years free) | Same | HGK (small companies often exempt – **VERIFY**) |
| **Ending** | Odjava (deregistration) – simple, free | Same | Liquidation (months) or shortened procedure without liquidation (ZTD čl. 472.a) |
| **Best for** | Solo service business, low costs, ≤ €60k | High expenses / above €60k but simple | Liability protection, partners, investors, retained profits, > ~€60–100k |

All tax/contribution figures: sources in the detail files and `sources.md`.

## 3. How to choose – questions that decide it

1. **Expected annual receipts and expenses.** ≤ €60,000 and low expenses → paušal is usually the cheapest.
2. **Employed elsewhere or a pensioner?** Paušal next to a job costs much less in contributions (annual, ≈ 17.5% of
   the class base); a pensioner pays none. A d.o.o. director who is employed elsewhere also avoids the €727.45.
3. **Liability risk** (contracts with damages exposure, employees, inventory, debt) → company.
4. **Partners or investors** → d.o.o. (j.d.o.o. for up to 5 members with little capital).
5. **Reinvest profit instead of spending it?** Company: 10% now, 12% more only when distributed.
6. **Clients:** large corporates or public tenders sometimes prefer a d.o.o.; VAT-registered B2B clients do not
   care about VAT; consumers do (25% price difference).
7. **Regulated activity?** Vezani obrt or slobodno zanimanje requirements (§5).
8. **Admin appetite:** paušal can be DIY; a d.o.o. needs an accountant.

Give the user a short comparison with their numbers (ranges, assumptions stated), not a single verdict. Use
`scripts/pausal_estimate.py` for the paušal side.

## 4. Typical paths

- Start as paušal → above €60,000 move to obrt na dohodak or found a d.o.o. (assets of the obrt can be
  transferred; **VERIFY** VAT/tax consequences of transferring a business).
- Start a j.d.o.o. with €1–€100 capital → convert reserves to capital to reach €2,500.
- Side project next to employment → paušal (low contributions) or drugi dohodak for occasional jobs.

## 5. Activity codes (NKD) and regulated activities

- **NKD 2025** (national classification aligned with NACE Rev. 2.1) applies from 1.1.2025 (NN 47/2024). Examples:
  62.10 computer programming, 58.29 other software publishing, 63.10 hosting/data processing (legal skill 04 §6).
  Pick the main activity carefully: it drives statistics, some fees and sometimes eligibility for grants.
- **Obrt types (Zakon o obrtu):** slobodni obrti (free – no qualification), **vezani obrti** (require a
  qualification: master's exam / vocational qualification – e.g. electricians, hairdressers, car mechanics),
  povlašteni obrti (special approval). The list is in the Pravilnik o vezanim i povlaštenim obrtima (**VERIFY**
  current version on zakon.hr).
- A d.o.o. carrying on a regulated activity needs a person meeting the conditions (employee or director) –
  **VERIFY** per activity.
- Other licences: food (HAH/inspection), tourism (`croatia:hr-tourism-rentals`), real estate agency
  (`croatia:hr-real-estate`), transport, financial services – outside this skill.
