# Verdicts b06

## A1
Winner: Designer
Why: The CFPB scenario rests on a dealer fee hidden in the price so the APR looks low. R32 in design.md already puts the dealer fee in the finance charge and takes the representative example from a versioned lender rate sheet. R23 and R60 bind consent to the config/quote hash, and a new lender amount invalidates it. The Designer admits one residual gap: no invariant yet forces the e-sign contract amount to equal the read-back amount. That is hardening on a mechanism that already targets the attack.
Worth adding: A build and runtime invariant that the e-sign contract amount and lender amount equal the quote-hash amount read back, with cash and financed price stated side by side in READ_BACK.

## A2
Winner: Breaker
Why: Nothing in the design stops a policy-table rebate row from reducing the spoken or read-back price. A substantiation id proves the program exists, not that this customer gets the money. R78's "unverifiable external fact" lint is about urgency and weather pretexts, not queue-state incentives. Certificates expire only on row edits, so a filled funding step leaves a certified net-price claim that is now false, made worse by the install delay the design itself imposes.
Fix needed: Type incentive rows (guaranteed / capped / reservation_required). Capped and reservation rows can never reduce the quoted or read-back price. READ_BACK states the gross contract price and the incentive only as "if approved, not guaranteed". A net price may be spoken only with a program_reserved provenance slot set by a program or installer API event. A daily program-status feed expires capped rows. The contract carries an incentive-failure no-penalty cancel clause, and the reservation is filed inside the cancellation window.

## A3
Winner: Designer
Why: The existing design fails safe exactly as intended. R61 allows savings only from verified bill or usage data, R72 enforces slot-source allowlists at build time (so a "spoken bill" writer fails the build), and R29 gives "insufficient inputs -> no figure, offer survey". R28 already tracks time-on-fallback as a throughput metric. Weaker conversion is a cost, not a safety or compliance break, and the design cannot be quietly loosened.
Worth adding: A usage-authorization outbox effect (Green Button Connect or utility-portal link, or a bill upload with a deterministic extractor) as the only writer of verified_usage, authorized by the utility account holder, with an OTP-gated resume to deliver the savings figure.

## A4
Winner: Breaker
Why: R29's "versioned tariff tables" and R72's calculator_output provenance check where the inputs came from, not whether the model is right. Nothing requires hourly Net Billing Tariff export values, and nothing marks rate-escalation or future-tariff rows as assumptions. A single export rate or a 4%/yr escalator carrying a substantiation id is a forecast stated as fact. The Designer concedes both points.
Fix needed: Add an "assumption" provenance type for escalation and future-rate rows. Any fragment filled from one must carry a lint-enforced "estimate, assumes X, not guaranteed" qualifier. The default savings figure uses today's rates only, and any projection is paired with a zero-escalation case. The calculator must use the customer's exact tariff schedule (e.g. NBT hourly export) on verified interval data, else no figure. A tariff-filing monitor expires rows. Escalator-lease READ_BACK states the year-1 and final-year payments.

## A5
Winner: Breaker
Why: The claim that certification uses these labels is wrong: R2 and R66 gate release on audio-audited per-call harm. But the design's own success label (R71: installed, not rescinded, no complaint, which feeds training reward, the pass criterion and R50 branch metrics) counts systems that are installed but not operating. READ_BACK (R85) has no required disclosure of utility approval risk, upgrade cost or when payments start relative to PTO. An audio audit cannot see harm that happens months after the call.
Fix needed: Redefine success as PTO granted plus N months of monitored production plus no complaint across the whole window, with labels provisional until then. Add policy-table rows required in READ_BACK and the contract: utility interconnection approval required, possible utility-side upgrade cost and who pays it, and the exact loan first-payment event. Make an install-to-PTO lag over threshold, and any "paying, not operating" state, Tier A harm signals per branch.

## A6
Winner: Breaker
Why: R23, R49 and R60 bind consent to the hash read back on the call, but nothing in the design governs an installer's post-signature change order. Suitability (R71) has no electrical-service slot. Because install waits out the cancellation window (R17), every change order lands after cancellation rights expire. The Designer concedes that enforcement downstream of the call and the timing are missing.
Fix needed: Schedule the site survey inside the cancellation window and make the contract contingent on a survey-confirmed price. Every change order becomes a new quote hash with written re-disclosure, a fresh e-sign by all signers, a no-penalty exit and a restart of the cancellation window. Install is blocked until then. Add main-panel amperage and roof-structure slots. When they are unknown, READ_BACK must state "price subject to survey" with policy-table cost ranges. An unconsented price increase is Tier A harm.

## A7
Winner: Breaker
Why: R82 and R23 make the named product part of the consented config, but no step compares what is installed to what was signed. The design controls install release (an outbox effect that waits for the cancellation window) yet never gates it on a bill-of-materials match. So the certified read-back can be silently falsified by substitution, which the Designer admits.
Fix needed: Gate the install effect on WAITING_FOR_BOM_MATCH, comparing the installer's planned SKUs (then installed serials) to the signed config hash. On a mismatch, block install and require a written re-disclosure of the new product, warranty and degradation terms plus a fresh e-sign with a no-penalty cancel. Add a supply-status field to product rows that expires discontinued or tariff-hit SKUs. Count an un-reconsented substitution as Tier A harm.

## A8
Winner: Designer
Why: A warranty term in a signed contract is a true statement when made. The design already has the mechanism to pull it everywhere: one owned policy table, separate warranty keys (R91), and certificate expiry on row change. A sales-call agent cannot make a counterparty solvent, and milestone disbursement is the lender's domain. The real weakness is that pulling a row depends on someone editing it, which is a trigger gap rather than a failure of the agent's design.
Worth adding: A counterparty-health monitor (bankruptcy filings, missed-milestone rates, lender watch-lists) that automatically expires a partner's warranty rows and suppresses dialing, plus READ_BACK naming who backs each warranty and preferring warranties with a backing instrument.

## A9
Winner: Breaker
Why: R73's challenge-response checks answers against the partner-supplied lead record, and R74's consent artifact can come from the same fraudulent partner. R22 sends the e-sign OTP to the dialed number. R88 sets the signer names from public records, but delivery and OTP still go to the fraudster's phone, so nothing ties the signer to the titleholder. The design leaves this open, as its own "lead-vendor consent audit" open item shows.
Fix needed: Draw identity-challenge answers only from independent sources (public records, KYC vendor), never from partner lead fields. Run a pre-dial phone-to-record-owner match (carrier or identity graph); with no match, the call is lead-gen only. Require lender-grade identity verification (document plus selfie or KBA) for each record owner at e-sign. Mail a contract summary with cancel instructions to the property address of record and hold install for a set time after it. Track per-partner fraud metrics with auto-suspension, and use an independent consent-capture provider.

## A10
Winner: Breaker
Why: The release gate is audio-based (R2/R66), so the "certifies it" claim is overstated. But post-call harm is invisible on audio. The only signals for it are the R71 success label, R50 cancellation-rate-per-branch tracking and the sampled suitability audit, and all of them flow through a CRM written by people paid on those numbers. R51's "no self-reported labels" targets customer poisoning, not operator edits, and nothing specifies where audit samples come from.
Fix needed: Source outcome labels first from independent feeds (outbox post-install customer survey, AG/CFPB/BBB complaint feeds, lender disputes and delinquency, cancellation API logs, utility PTO records), which override CRM fields. Make CRM outcome fields append-only with signed, attributed edits and two-person approval for reclassifications or backdates. Sample suitability audits from the e-sign webhook list of all signed contracts. Raise a Tier A alarm on divergence between CRM and independent complaint rates per installer, and decouple ops and installer bonuses from training labels.
