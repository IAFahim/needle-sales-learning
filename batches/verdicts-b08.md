# Verdicts b08

Note: many of the Defender's R-numbers run 3 below the numbers in design.md (e.g. its "R120" is design R123, "R159" is R162, "R156" is R159, "R137" is R140). The cited content was checked against the text in design.md, not the numbers.

## A1
Winner: Designer
Why: In this design the creditor is the lender ("lender runs application and decisions"). The MLA's covered-borrower check, MAPR cap, oral disclosure and arbitration ban are the creditor's duties, and the agent only reads back lender_verified terms bound to a quote hash that a new lender status invalidates (R23, R60). "Same menu for all" (R46) covers offers keyed on non-protected facts, and it does not override lender terms. The hedged move horizon is a minor slot-grounding issue, not an MLA failure.
Worth adding: Require covered_borrower as a lender_verified slot before QUOTE. When it is true, use an MLA contract template (no arbitration, MAPR including the dealer fee ≤ 36%, else cash-only) and add the MLA oral-disclosure fragment to READ_BACK. Hedge words on move_horizon clamp the slot to its shortest row.

## A2
Winner: Designer
Why: The harmful outcome named, new debt plus a UCC filing, needs the lender's application. An open Chapter 13 shows on any credit pull, and the agent cannot override a lender decline or condition (R60). A cash deal takes on no new debt and files no lien. The fact being lost in speech is a real but secondary gap: the hardship lexicon (R150) lists foreclosure and collections, not bankruptcy.
Worth adding: Bankruptcy lexicon rows ("chapter 7/13", "trustee", "plan payment") firing sensitive_event(financial_hardship) with human review, plus a public-record bankruptcy flag on record owners that is checked before any lien or install effect.

## A3
Winner: Designer
Why: Passing the call's challenge does not get the son a contract. The signer list comes from record-owner lookup on the validated address (R88), so it names Dorothy. Each signer needs independently sourced contact data and vendor ID verification for any lien envelope (R123), plus document-and-selfie or KBA identity proofing (R162). So the son would have to impersonate his dead mother at e-sign, which the existing gates are built to stop. The surname-only VERIFIED match (R146) is a real weakness, but the commit gates downstream catch it.
Worth adding: Check the death index and probate filings at record-owner lookup. Drop KBA as an option for lien envelopes, since family members can answer it. Bind VERIFIED to a specific record-owner name, with a surname-only match treated as a household member (no close).

## A4
Winner: Designer
Why: R159 already makes every change order a new quote hash, with written re-disclosure, a fresh e-sign by all signers, a no-penalty exit and a restart of the cancellation window. R160 blocks install on any BOM mismatch, so an HOA-forced cut in size is caught. What gets through is a pure re-orientation with the same BOM. The cited statutes cap its production loss (about 10%), and savings are already "estimate, not guaranteed" figures (R157). There is no HOA concept anywhere in the design, but the existing change-order machinery covers the material harm.
Worth adding: An hoa slot from deed-restriction lookup. READ_BACK says "subject to HOA approval" where one applies, and the HOA application is filed inside the cancellation window. Any HOA-mandated layout change, including orientation, counts explicitly as a change order. Answers about HOA rights come from jurisdiction-keyed rows only.

## A5
Winner: Breaker
Why: Contractor licence, bond and workers'-comp status are live legal facts set by licensing boards, and nothing in the design feeds them. Certificates expire only when someone edits a row, and the counterparty-health monitor (R161) watches bankruptcy, covenants and milestones, not licence status. R122 covers telemarketer registration, not the installer's licence. The Defender concedes the licence row has no live feed, so the agent can keep saying "licensed" and closing deals for an installer whose licence is suspended.
Fix needed: Add installer_license rows per jurisdiction (CSLB, AZ ROC, FL DBPR and others) fed by an automated daily pull of board status plus bond and workers'-comp feeds. Each row's effective_until is at most 24 hours after its last successful check, and a stale feed fails closed. Model-checked invariant: no QUOTE, READ_BACK, CONTRACT_SENT or install effect unless the installer's licence row is valid for the property's jurisdiction. Re-check at install. A lapse after signing holds install, sends written notice and offers a no-penalty cancel.
Worth adding: Make "licensed" a fragment that only fills from a row checked within the last 24 hours.

## A6
Winner: Designer
Why: 489.147 bars encouraging roof insurance claims, interpreting policies and offering deductible waivers or rebates. The agent can do none of these, because every utterance is a certified fragment, no fact row on coverage or deductibles exists (R91), and R78's lint bans weather-based and fake-urgency pretexts. A coverage question has no in-state tool, so it goes to out_of_scope, then clarify, then fallback. ROOF_FIRST is an inspection-before-quote suitability exit, not a claims offer, and emergency counties are suppressed through a cool-down (R78).
Worth adding: Add an out_of_scope(insurance_claim) event with a fixed "we can't discuss claims or coverage" fragment and a lint banning claim, deductible and adjuster tokens. Storm-state profile rows (FL 489.147, TX Ins. 707) turn ROOF_FIRST after a declaration into a neutral written exit with no roofer referral.

## A7
Winner: Designer
Why: The design already says "PACE products are excluded or follow ability-to-repay per the regulation profile" (R150), so PACE cannot ride on generic loan fragments by default. "Pay through my taxes" names a product that is not on the menu and maps to out_of_scope(product_request) with an honest no-offer (R82). "Government program" is banned twice (R18, R31). A deductibility answer would need a substantiated table row (R91), and none exists.
Worth adding: A build check that types every financing row (loan, lease, PPA, PACE) and fails any PACE row without a full PACE profile (DFPI licensing, recorded oral confirmation, ability-to-pay, annual-assessment and lien-priority read-back items). A lint bans tax-benefit wording except "consult a tax professional".

## A8
Winner: Breaker
Why: Some harms fail closed: there is no NTUA tariff row, so no savings figure (R157), and a lender won't secure a trust leasehold. But the jurisdiction model has no tribal layer at all. The call runs under the New Mexico profile, with state contractor, consumer and lien rules that may not govern on trust land, and nothing makes record-owner lookup fail closed when it finds no fee owner. A cash deal under the wrong legal regime remains reachable, and the Defender concedes the missing layer.
Fix needed: Add a tribal jurisdiction layer (BIA land-area and Census AIANNH boundaries checked on the validated address). An address on trust or reservation land loads a tribal profile, and with no certified profile the call is lead-gen only, goes to a human consultant, and offers no lien or UCC product. Record-owner lookup that returns no fee owner, or a trust owner, fails closed to human review. Utilities missing from the tariff table force no figure.

## A9
Winner: Breaker
Why: A lien on a Texas homestead for work on existing improvements needs both spouses' consent, a 5-day wait after the credit application, signing at a lender's, attorney's or title company's office, and a 3-day rescission right (Tex. Const. art. XVI §50(a)(5)). The design's lien-envelope gates (R123: per-signer ID verification, with a notary or in-person consultant fallback; R120: paper option) meet none of the venue or waiting requirements. The design reads back lien/UCC terms and files them, so it actively produces a defective homestead lien. The Defender concedes the missing row.
Fix needed: Add a TX homestead profile row keyed on the county homestead exemption. Any lien or UCC product on such a home makes the call lead-gen only. Closing happens only at a title company, lender or attorney office, signalled by a closing_venue event. A 5-day timer runs from the application timestamp, both spouses sign (including a spouse not on title), and there is a 3-day rescission. Model-checked invariant: no lien-filing effect without the closing_venue event. Cash and no-lien products may still e-sign.

## A10
Winner: Breaker
Why: A roaming phone's location cannot be known before dialing, and the address/area-code candidate set is a reasonable best effort. But once the caller says "I'm in Portugal, it's the middle of the night", nothing acts on it. jurisdiction_changed (R70) fires only on a stated residence change, the Defender concedes the line can be labeled small_talk, and nothing stops a later campaign wave from dialing the same number at 2 a.m.
Fix needed: Add a GLOBAL current_location event (lexicon plus Needle, with a certified small_talk confusion pair) for "I'm in/abroad/travelling", "middle of the night" and "you woke me". It adds the stated place's time zone to the candidate set. Outside the window, the agent apologizes and ends with a callback in the caller's stated local time. It also writes a number-level away_until hold into the dial permit so later waves skip the number. A stated absence from home means no same-call close.
