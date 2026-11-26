# Verdicts b12

## A1
Winner: Designer
Why: The scenario depends on the agent saying "the Elm St solar account" and on campaign calls going on after the husband raises the issue. R73's challenge-response has the caller state the name and address, so the agent never says either. R99 already suppresses all sales campaigns while a service ticket is open, so the out_of_scope(service_issue) label the Breaker assumes would itself stop the three follow-up calls. The Rosenthal theory is also weak: a marketing call that never mentions the debt is not a communication "in connection with the collection" of it. One caveat: R146's address-plus-surname match could mark a spouse VERIFIED. That is why the new lint on lender and payment fragments is worth having.
Worth adding: Use the lender delinquency feed (R163) as a pre-dial suppression input for every existing-customer campaign. Add a lint that bans fragments naming the existing loan, lender, balance or payment, and a Tier A third-party-disclosure red-team stratum with spouses and relatives who pass the R146 match.

## A2
Winner: Designer
Why: No existing path collects a debt. There is no voice payment (R45) and no fragment asks for bank data (R89). Under R46 every option goes to everyone, so an offer cannot hinge on whether a loan is in good standing. "I'm in bankruptcy" lands on R150/R19 hardship (scripted exit, no pitch) or on service_issue, which brings R99 campaign suppression. Marketing a new product with no collection content is not an act to collect a pre-petition or discharged debt. The real gap is that the design never checks bankruptcy status, so the conversation is the only way it finds out. That is worth closing, but the harm in the scenario rests on a "good standing" fragment the design would not produce.
Worth adding: Run a PACER/servicer bankruptcy scrub in the pre-dial gate, with suppression that only counsel can lift. Add a sensitive_event(bankruptcy) subtype that sets legal_hold, and a lint that bans eligibility wording tied to the status of an existing debt.

## A3
Winner: Breaker
Why: R76 does call the contractor cancellation API and send written confirmation, and R55 gates the spoken confirmation on that effect succeeding. So the seller side is real. But cancellation is one effect aimed at one party. The design has no step that voids the separate lender envelope, terminates or holds the UCC filing, or releases the installer. It also has no invariant that blocks loan funding while a cancellation is open. The Designer's fan-out saga is entirely new.
Fix needed: Turn CANCEL into a saga. One cancel intent fans out to the seller contract API, the lender envelope void or loan cancellation, a UCC hold or termination, and the installer slot release. Each party gets its own WAITING_FOR substate and idempotency key, and the customer is told cancellation is complete only after every party acknowledges. Add an invariant: no loan funding, UCC filing or install while any cancel is open. Treat oral cancellation to the agent as valid notice under the contract, and also send the pre-filled statutory form by e-sign and mail. The spoken fragment says "started", not "recorded/done".

## A4
Winner: Breaker
Why: R47's lead-gen mode keeps the on-call read-back out of California, but the deposit (R45) and the lender's disbursement still happen. Nothing in the design caps the deposit (Cal. B&P 7159.5: $1,000 or 10%, whichever is less) or stops payment ahead of work performed. The contract template's 7159 fields (start date, completion date, progress-payment schedule) are left to template authors, with no required keys. The Designer admits enforcement is missing.
Fix needed: Add a home_improvement_contract row in each regulation profile (CA 7159 and analogues) with required keyed fields: estimated start and completion dates (ranges allowed when tied to permits) and a progress-payment schedule. A build and runtime check fails any contract or read-back that lacks them. Compute the deposit effect as at most min(cap amount, cap %) from the profile, and have the outbox refuse anything larger. Admit a lender program into a profile only if its draw milestones never pay ahead of work performed. Make paying for work not yet done a Tier A harm signal.

## A5
Winner: Designer
Why: Resale is already treated as material in the existing design. R71 makes move/sale horizon a suitability slot leading to NOT_SUITABLE, bans the claim "transfers to the buyer" and requires a written resale disclosure in the contract. R83 and R85 require material-limitation rows in every read-back. R157 has escalator leases state the year-1 and final-year payments. A buyout figure fits as a calculator_output over a table formula (R72, R91), so the no-literal-numbers rule does not block it. Adding a specific transfer_on_sale row is content inside those mechanisms, not a new mechanism.
Worth adding: Add a mandatory transfer_on_sale material-limitation row for every lease and PPA (transferee credit check, possible conditions from the buyer's lender, assume/buyout/prepay options), with buyout values at fixed contract years in READ_BACK and a full table in the contract.

## A6
Winner: Breaker
Why: Every ownership check the Designer cites runs at or around signing. R88 looks up record owners, R123 verifies signer identity, and R141/R159 happen early in or near the cancellation window. None of them re-checks title just before the install or the lien. R158's success label would eventually record the harm, but only after roof penetrations and a lien on property someone else now owns. The Designer admits the gap and the WAITING_FOR_TITLE_RECHECK gate is new.
Fix needed: Add a WAITING_FOR_TITLE_RECHECK gate within N days before install and again immediately before any UCC filing. It re-runs the record-owner lookup and checks recorded deeds and transfers, listing and escrow feeds, the deceased list and capacity flags, and every signer reconfirms through their verified channel. Any change blocks install and filing and goes to human review. The current owners must re-sign, or the contract is cancelled with no penalty. A stale-title install is Tier A harm.

## A7
Winner: Designer
Why: The attack's legal harm requires calls that rely on the existing-customer relationship instead of consent. Every dial in this design passes R74's per-number PEWC gate, which names the seller and the AI voice, plus federal and state DNC scrubs (R59, R114). So a call with marketing content is lawful telemarketing under the design's own consent model. Ops cannot quietly swap in a scheduling preamble: R31's preamble is compiled, R67 hashes the bundle, and R134 diffs the binary against the certified graph. A "sales call" disclosure on a call that also schedules is over-disclosure, not a false purpose.
Worth adding: Make call_purpose a typed field on both campaign and bundle, enforced by the dialer, and give the SERVICE profile a model-checked invariant that no marketing-tagged fragment is reachable.

## A8
Winner: Designer
Why: Release certification does not rest on Needle's labels. It uses humans listening to the audio, covering all disagreements plus random agreements (R2, R26, R66). The R163 success label takes independent feeds first, including AG/CFPB/BBB complaint feeds, lender disputes and cancellation logs, and these override the CRM. So the claim that regulator complaints never enter the join is false. The leftover risk is mislabeling a complaint as service_issue on follow-up calls. Audits catch that, and the new links between follow-up tickets and the original sales branch tighten it.
Worth adding: Define "complaint" in policy, independent of the routing label. Count every existing-customer service_issue as a complaint against its originating sales branch until a human clears it, and make the per-branch service_issue rate a Tier A metric.

## A9
Winner: Designer
Why: The agent's read-back accurately states the seller's own warranty term. Whether that term is lawful is a legal review, and the design already assigns it to compliance sign-off and the claims audit on every row a template cites (R18), on a versioned, owned table (R10). Withdrawn rows are tombstoned (R140). No lint could judge lawfulness, so the attack is really about human legal review, which exists. The Designer is right that the banned-claims lint covers fragments, not row text. The FTC's 2024 "warranty void if" warnings make that extension cheap and worthwhile.
Worth adding: Extend the banned-claims lint to policy-table row text, contract templates and backer instruments, flagging tie-in and void-on-repair patterns. Require a per-jurisdiction legal attestation field (MMWA 2302(c), state right-to-repair) before a warranty row can be cited.

## A10
Winner: Designer
Why: The scenario assumes an oral bank-debit authorization, and the design never takes one. R45 says the voice channel takes no payment and the deposit goes through a processor-hosted page, and R89 bans asking for bank data. The authorization is therefore a written electronic one, which TSR 310.3(a)(3)(i) accepts. Redaction and NO_RETAIN destroy no evidence because none is spoken, and R116 keeps the TSR record set in WORM storage in every privacy mode.
Worth adding: Specify the hosted page's capture: amount, dates, number of debits, last 4 digits, account-holder name, customer-service number, E-SIGN signature and joint-holder attestation. Store it in the R116 WORM set keyed to the session, and add an invariant: no debit effect without a stored authorization.
