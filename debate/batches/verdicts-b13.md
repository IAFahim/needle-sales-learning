## A1
Winner: Breaker
Why: R154, R32 and R85 make the spoken financing terms come from the lender rate sheet and require "financing terms (Reg Z)" in READ_BACK, but nothing says which payment in a multi-step schedule gets spoken. R157's year-1/final-year rule covers escalator leases only, and R150's affordability check doesn't say which step it tests. The Designer concedes this gap, and the defense rests on new hardening. R155/R140 stop an expired 25D row from cutting the price, but a re-amortizing loan still quotes the pre-step payment.
Fix needed: Every lender product row carries its full Reg Z payment schedule. Where a product assumes a voluntary prepayment or re-amortizes, READ_BACK speaks every scheduled step ("<pay_1> until month <n>, then <pay_2>") with the no-prepayment payment as the payment owed, and the R150 affordability row is tested against the highest step. Products whose payment depends on a tax credit the customer can't be shown to receive are excluded from on-call close.
Worth adding: A fragment lint that refuses any payment key without its schedule-step index.

## A2
Winner: Designer
Why: The design already blocks an assumed tier. Credit band is accepted only with lender-prequal provenance and never from speech (R90). The calculator takes lender prequal as an input (R79), and missing inputs mean no figure (R29). The lints ban voice credit consent and "pre-qualified" (R89/R96). If the decision later moves the terms, R60, R23 and R154(3) invalidate the quote hash and force a new read-back, so a mismatched envelope can't go out.
Worth adding: State explicitly that a financed COMMIT needs lender_verified rate, term and payment (cash-only commit or a written proposal otherwise), and ban "as low as" fragments from READ_BACK.

## A3
Winner: Breaker
Why: R157's "customer's exact tariff schedule (e.g. NBT hourly export)" values exports under NBT. It still reads as the customer's current import schedule, but CPUC's NBT decision requires solar customers to take service on an eligible high-differential/electrification TOU rate. The design never names a separate post-solar tariff, and the Designer admits this. So the baseline and the post-solar bill can be priced on a tariff the customer will lose.
Fix needed: The calculator computes two bills on verified interval data: the baseline on the current schedule, and the post-solar bill on a policy-table interconnection_tariff row (the mandated rate per utility and program). Savings = baseline minus post-solar. READ_BACK must state the rate change. If several eligible rates are possible, use the least favorable one or give no figure.

## A4
Winner: Breaker
Why: Nothing in the design records the generation provider. Calculator rows are keyed by utility and tariff_class (R212), so a CCA customer's generation rate, export adders and cash-out policy can silently default to IOU rows. "Exact tariff, else no figure" (R157) can't fire when the system doesn't know a different rate-setter exists. The Designer concedes the missing slot.
Fix needed: Add a generation_provider slot, written only by the utility API or bill extractor. Key calculator rows by (delivery utility, generation provider, schedule), and add CCA rate/export/cash-out rows watched by the tariff-filing monitor. An unknown provider or missing row means no figure and a written proposal.

## A5
Winner: Designer
Why: CARE/FERA and medical baseline are part of the customer's billed tariff schedule. At PG&E, for example, CARE customers are on distinct schedules, and the utility API reports them. R157 requires that exact schedule, else no figure, and R156 restricts the data source to the utility API or bill extractor. A calculator that multiplies by the standard residential rate already breaks an existing rule. Matched-pair tests were never the control for calculation correctness.
Worth adding: A bill-reconciliation gate: the calculator must reproduce the customer's actual billed amounts for the authorized months within tolerance, else no figure. This also catches A3, A4 and A6 classes. Also make discount-program households a Tier A audit stratum.

## A6
Winner: Designer
Why: The scenario's key line, "near zero bill", is already a banned claim (R18) that the runtime lint checks on rendered replies (R29). A calculator bound to the exact tariff schedule on interval data (R157) must bill fixed and non-bypassable components, which carry through both bills and can't be offset away. The design doesn't spell out the post-solar bill composition, but the existing rule already forbids the "100% offset of the bill" shortcut the attack relies on.
Worth adding: A build check that a tariff row can't be cited unless it has its fixed, minimum-bill and non-bypassable fields, plus a required READ_BACK "residual utility bill about <x>/month" key.

## A7
Winner: Designer
Why: Production doesn't come from speech. R79 puts the roof/shade data lookup into calculator inputs, R211(3) cross-checks shade against aerial data, and R61 forbids savings or sizing from spoken estimates. Shade is only a qualification slot that routes suitability (R71). R159 makes the contract contingent on a survey-confirmed price, with re-disclosure and a no-penalty exit. A spoken "not really" can't become a certified production figure.
Worth adding: Name a modeled_production provenance class (pinned irradiance model over aerial/LIDAR geometry) that the claims lint requires for every savings or payback fill.

## A8
Winner: Breaker
Why: The design lets multi-year projections be spoken with R157's "estimate, assumes X" qualifier, but no rule requires a lifetime or payback figure to subtract predictable costs the system already knows about, such as inverter replacement within the term or detach-and-reset for a roof that passed suitability but won't outlast the term. A qualifier on assumptions doesn't cure a material omission. The Designer calls it a completeness gap and relies on new bans and expected-cost rows.
Fix needed: Ban lifetime-savings and payback keys from phone fragments: only year-one savings on the call, multi-year figures only in the written proposal. Any multi-year figure must subtract policy-table expected_cost rows keyed on equipment type versus term (inverter replacement), remaining roof life versus term (detach-and-reset) and jurisdiction (insurance and property tax). A suitability row sends any roof whose remaining life is shorter than the term to ROOF_FIRST.

## A9
Winner: Designer
Why: The envelope is bound to the read-back. R49 commits only the quote hash read back, R23 ties the read-back to a config hash over versioned inputs, and the R134 outbox monitor refuses CONTRACT_SENT without READ_BACK for that same hash. So the envelope carries v41, and a later table bump doesn't rewrite it. Certificate expiry stops new calls from speaking retired rows. It isn't contract validity. Any later price change goes through R159's re-disclosure path.
Worth adding: A quote_valid_until key spoken in READ_BACK and printed in the envelope, plus a model-checked WAITING_FOR_SIGNATURE->EXPIRED edge. Also state that R140's effective-window refusal does not apply when re-deriving values for a sent envelope's frozen quote hash.

## A10
Winner: Designer
Why: The design deliberately chooses the conservative, truthful path. Figures come only from verified usage (R61/R156), sizing is capped to verified meter usage (R210), and spoken future loads can't upsize anything. They are only recorded as customer-mentioned provenance slots (R4), and any projection must use R157's assumption-typed qualifier. The mixed-occupant scenario is also weak, because account-holder usage authorization (R156(2)) normally returns only the current account holder's data, not the prior occupant's.
Worth adding: Read service_start_date from the utility API. With fewer than 12 months under the current account holder, give no figure on the call, only a written proposal after the survey. A savings fragment given after a load_change mention must say it is "based on your past usage, not including <load_change>".
