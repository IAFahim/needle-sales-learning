## A1
TOPIC: Tax-credit "re-amortization" loans: the quoted monthly payment is a teaser that jumps when the customer doesn't prepay the assumed credit
SCENARIO: Lender product in the policy table is a 25-year solar loan built around a voluntary prepayment of ~30% at month 18. The calculator quotes the pre-re-amortization payment ($189). READ_BACK speaks "financing terms" from table keys: rate, term, $189/month. Customer, a retiree with no tax liability (and no 25D credit at all for 2026 installs), never prepays. At month 19 the payment re-amortizes to ~$270. The commit was gated on a number that was never the real payment.
WHY IT BREAKS: CFPB's 2024 solar financing spotlight flags exactly this structure: payments rise sharply if the assumed tax-credit prepayment isn't made. The design's read-back lists what to say, not that the spoken payment must be the payment the customer will actually owe. Lints check Reg Z trigger terms, not payment-shock structure. Source: files.consumerfinance.gov/f/documents/cfpb_solar-financing-issue-spotlight_2024-08.pdf

## A2
TOPIC: Financing terms read back before the lender's credit decision, so the commit is gated on an assumed credit tier
SCENARIO: The lender runs the application after the call (the design keeps underwriting with the lender). To read back "financing terms" on the call, the calculator has to assume a tier, in practice the best one ("as low as"). Customer says "yes" to $162/month at 3.99%. The lender approves them at tier C, 9.99%, $231/month, in the e-sign envelope. Either the read-back carried hypothetical terms, or the agent pulls credit mid-call, which is a hard inquiry on a cold call.
WHY IT BREAKS: The COMMIT gate certifies agreement to read-back values. When the lender owns the decision, those values can't be lender_verified at commit time. "Same menu for all" makes this worse: everyone hears the top-tier price, and lower-credit buyers, who are disproportionately protected groups, get the surprise.

## A3
TOPIC: Interconnecting forces a rate-plan switch, so savings are computed against a tariff the customer won't be on after install
SCENARIO: Verified usage comes from a California customer on a tiered or legacy TOU plan. The calculator prices avoided cost at that plan's rates. Under the Net Billing Tariff, solar customers must take service on an eligible TOU rate, and utilities put them on high-differential electrification rates with low midday value and an expensive 4-9pm peak. The savings fragment's baseline (current plan) and post-solar (new mandatory plan) are different tariffs. The quoted savings compare apples to a rate the customer will lose.
WHY IT BREAKS: The design says "savings only from verified usage". Usage is verified, but the rate it is multiplied by is chosen by the utility because of the sale itself. That's not a forecast (A206). It's a known, mandatory, present-day change the calculator ignores. Source: CPUC NBT decision D.22-12-056; cpuc.ca.gov/nem

## A4
TOPIC: Community Choice Aggregator customers: generation rates and export credits are set by the CCA, not the utility tariff the calculator uses
SCENARIO: Customer in Marin or San Diego gets generation service from a CCA (MCE, SDCP) and delivery from the IOU. The policy table holds IOU tariffs keyed by utility territory. The calculator values offset and exports at IOU generation rates and IOU NEM rules. The CCA has different generation rates, its own export-credit adders and an annual cash-out policy, and can change them by board vote without CPUC rate cases.
WHY IT BREAKS: Utility territory isn't the rate-setter for about a quarter of California load. Nothing in the slot store records the generation provider, and verified usage (kWh) doesn't reveal it. Every savings number for CCA customers is computed against the wrong tariff while being "certified" as calculator_output with a substantiation id.

## A5
TOPIC: Discount-rate households (CARE/FERA, medical baseline) get savings computed at full price, overstating benefit for the poorest customers
SCENARIO: Customer is on CARE, which is roughly a 30-35% discount on the electric bill, plus a lower income-graduated fixed charge. Verified usage gives kWh, and the calculator multiplies it by the standard residential rate. It reads back "$140/month savings" against a bill that really costs them about $90 at discounted rates. The loan payment is real dollars, and the "savings" are against prices the customer never paid. Medical-baseline customers get the same distortion.
WHY IT BREAKS: The rate discount isn't a usage fact, so "verified usage" doesn't fix it. The error falls entirely on low-income and medically vulnerable households, the group that A199's affordability gap and the fair-lending matched-pair tests are meant to protect. A matched-pair test passes because both pairs get the same wrong rate.

## A6
TOPIC: The savings baseline includes charges solar can't offset (fixed charges, minimum bills, non-bypassable charges)
SCENARIO: Customer's verified bill is $210. The calculator computes offset as 100% of annual kWh, so the fragment says "your bill drops to near zero". In California, the income-graduated fixed charge adopted May 2024 (about $24/month for most customers) plus non-bypassable charges on all imports keep being billed regardless of production. Other utilities have minimum bills or grid-access charges. Year one, the customer pays the loan plus about $40-60/month in electric bills they were told would disappear.
WHY IT BREAKS: The design checks where each number comes from, not what it means. A "savings" fact assembled as bill minus production value is unsubstantiated if parts of the bill aren't volumetric. FTC s5 and the TSR forbid misrepresenting material costs. Sources: utilitydive.com/news/california-puc-approves-income-based-fixed-charge/715748/; sce.com fixed-charge FAQ

## A7
TOPIC: Production is self-reported: savings need modeled kWh from roof azimuth, tilt and shading that a phone call can't verify
SCENARIO: QUALIFY asks "Any shade on your roof?" and the customer says "Not really". The calculator assumes standard south-facing production for the size. The roof is actually east-west split, 14° tilt, with a neighbor's oak shading it after 2pm. Real production is 30% below the estimate, so the savings and payback in the read-back are off by a third, even though usage was verified to the kWh.
WHY IT BREAKS: The design pins verified provenance on usage only. Production, the other half of every savings number, gets no slot provenance class (no "verified_design"). So a self-reported spoken "not really" feeds a certified calculator_output. Garbage in, certified fact out.

## A8
TOPIC: Lifetime savings and payback omit known future costs: inverter replacement, remove-and-reinstall for a reroof, insurance and property tax
SCENARIO: The policy table's "25-year savings" sums avoided bills minus loan payments. String inverters are typically warranted for 10-12 years, so a replacement around year 12 costs about $2-4k. QUALIFY recorded a 15-year-old roof that passed suitability, but it will need reroofing during the term, which means about $3-6k for detach-and-reset. Homeowner's insurance riders and, in some states, property tax on added value also go unmentioned. The read-back states the lifetime number as certified fact.
WHY IT BREAKS: Every cost the system has on record (roof age, equipment type, term) predicts these expenses, and the deterministic calculator ignores them. A substantiation id proves the formula ran, not that the claim is complete. An omitted material cost is deceptive under FTC s5 even when each number shown is true.

## A9
TOPIC: Quote validity across WAITING_FOR_SIGNATURE: the price table changes between the spoken read-back and a signature days later
SCENARIO: Tuesday: READ_BACK speaks $3.10/W, policy table v41, and the envelope is sent. Wednesday: equipment cost update ships v42 at $3.35/W, and certificates citing v41 expire. Saturday: customer signs. Which price is the contract? If the envelope froze v41, the company sells at a retired price with an expired certificate. If it regenerates, the signed price differs from the one the commit gate verified. Either way, there's a re-send question the graph never models.
WHY IT BREAKS: The design tracks status "only from vendor webhooks" and expires certificates when rows change. It has no quote-expiry date in the read-back, no binding of envelope to table version, and no re-read-back path when they diverge. The verbal-commit-to-paper link breaks exactly at a version bump.

## A10
TOPIC: The verified usage history isn't the household's future load: new owners, prior occupants, planned EVs and heat pumps
SCENARIO: Customer bought the house 7 months ago. The utility's 12-month history is half the previous owner's (two people, no AC) and half theirs (five people, AC). Or the customer mentions "we're getting an EV next month". The calculator sizes and prices savings on the verified 12 months anyway, because only verified_usage may feed savings and the EV remark is ungrounded speech. The system ends up undersized, and the savings fragment is wrong in either direction.
WHY IT BREAKS: "Verified" means the utility confirms past kWh, not that it represents this household's next 25 years. The design forbids using spoken load changes (no provenance), so it must either quote known-wrong savings or none. Sizing rules (often 100-120% of historical usage) lock the error in at interconnection.
