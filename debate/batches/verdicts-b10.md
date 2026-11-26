# Verdicts: batch b10

## A1
Winner: Designer
Why: A forged DNC only stops our own calls, and the DNC ledger is never shared, so it fails safe for the consumer. A forged rescission is not silent: R76's CANCEL state sends written confirmation and a right-to-cancel reminder to the contract's channels, and R141 mails a notice to every record owner at the property address, so the real customer learns of it and can re-sign through the normal flow. Keeping cancels frictionless on a knowledge-only check is the correct legal posture, and the remaining harm is a business loss that the design already surfaces.
Worth adding: The inbound-cancel anomaly alarm (STIR/SHAKEN B/C/none, cancel clusters per lead source) and a customer-only "this wasn't me" reinstate that needs an OTP to the number of record and a fresh e-sign.

## A2
Winner: Breaker
Why: Inbound IDENTITY gives an observable difference: a match moves on to VERIFIED and QUALIFY wording, while a mismatch goes to clarify or WRONG_PARTY. R87's rate limits are keyed by caller, so rotating spoofed ANIs gets round them. R132's CUSUM can only detect a surge after it starts, not stop a slow one. The Designer concedes the membership disclosure and the missing per-lead keying. Every element that closes the oracle (constant-shape response, OTP unlock, per-lead counters) is new.
Fix needed: Inbound IDENTITY must answer match and mismatch with the same fixed fragment and timing ("we'll text a code to the number on file"). Only an OTP entered from the number of record unlocks VERIFIED or any personalized or QUALIFY fragment. Add attempt counters keyed by lead and address across all ANIs, with lockout to human-only plus a mailed notice, and a red-team test that timing and fragment ids can't be told apart.

## A3
Winner: Designer
Why: Under the existing design, SMS reaches only consented numbers that are gated and owner-matched. R22 sends to the dialed number only, R149 extends the consent gate to every SMS, R122 adds the registration guard, R74 blocks Needle-created contacts, and R162's phone-to-record-owner match sends a planted revenue-share number to lead-gen only, so it never gets to CONTRACT_SENT. Getting 50,000 bots through identity, suitability, READ_BACK and the R144 action-production commit is not plausible, and R55 idempotency keys plus R69 call budgets limit repeats within a call. The missing spend cap is defense in depth, not a hole the attack can drive through.
Worth adding: Per-number, per-session and per-campaign SMS budgets; a NANP-mobile-only deny-list for premium and IPRN ranges; a global SMS-spend circuit breaker; and DNC-policy copies sent at most once per number per 30 days.

## A4
Winner: Breaker
Why: The Designer concedes the core gap: a form filled with the victim's real name, address and phone passes R74's PEWC record, R162's consent-capture provider and the phone-to-record-owner match, because the identity graph matches a real person's real data. Nothing in the existing design proves the subscriber controls the number. The caller carries the burden of proving consent, so 20,000 dials is class-action exposure. Number-possession proof is entirely new.
Fix needed: A PEWC artifact is valid only if the form-filler entered a one-time code sent at submission to that number (double opt-in), and the verification record is stored in the consent artifact. Add form velocity controls per IP, device and ASN, with burst quarantine (never dialed). Add a consent_dispute event ("I never signed up") that writes DNC and quarantines the whole submission cluster, with a per-source dispute-rate Tier A metric and auto-suspension.

## A5
Winner: Breaker
Why: The agent itself can't write contact or payee data (R5, R45, R62). But the R99 tickets and R56 warm transfers have no defined payload. The Designer concedes they can carry a bare VERIFIED that humans will read as strong authority, even though it only reflects a knowledge-based check that brokered facts can pass. In the existing design, nothing stops the impostor's request from reaching ops with the agent's vouching attached. That is the BEC pattern the attack describes, and every control that closes it is new.
Fix needed: Use a typed handoff contract carrying verification_strength (knowledge_only / otp_number_of_record / lender_kyc), never a bare VERIFIED. Ticket and transfer schemas get no fields for a new phone, email, address or payee, and callbacks go only to the contact of record. Add a CRM-enforced rule that no contact, payee or autopay change comes from an agent-originated ticket or transfer without an out-of-band OTP to the old contact of record, a mailed notice and a cooling delay.

## A6
Winner: Breaker
Why: R59 says wording selection is "deterministic" but never restricts what feeds it, and the Designer concedes the selector's inputs are unrestricted and that audits aren't stratified by wording id. That is exactly what makes a 0.3% senior-skewed trigger possible and keeps random audits from finding it. R18's lexical lint and single compliance sign-off may miss a paraphrase like "nothing out of pocket", and R18 lists whole-path net-impression review as still open. R116's WORM log only finds the trigger after the harm. The closing controls (selector input restriction, two-person signed commits, per-wording audit quotas) are new.
Fix needed: Add a build check that the wording selector's only input is hash(session_id, fragment_id), so no slot or customer attribute reaches it. Every wording needs two-person approval (author plus an independent compliance reviewer) with signed commits. Add a quantifier and aggregate lint ("most", "nothing out of pocket") that requires a table key. Each new wording gets a 100%-audited canary and a minimum live audit quota per release, plus a matched-pair test of the wording-id distribution across age bands.

## A7
Winner: Designer
Why: The attack's key premise is wrong: R132's drift monitors are label-free and run on 100% of traffic. The worst harms are also blocked structurally, regardless of labels, by the R85 model-checked invariant and R134's independent outbox monitor refusing commits without READ_BACK. Missed stops are also caught by the label-independent lexicon sweep (R66). R131's two auditors with a confusion matrix, R143's in-house or vetted enclave with anomaly alerts, and R163/R113's independent outcome feeds give several cross-checks, so a single corrupt labeler can't quietly certify a state. A whole corrupt vendor is still a residual risk, which the suggested addition closes.
Worth adding: Blind planted gold calls in every labeler's queue, with a gold-accuracy gate and retroactive label drops; per-labeler and per-vendor concentration caps per stratum; adjudicators distinct from first-pass labelers; and an independent second-vendor re-audit slice before certification.

## A8
Winner: Breaker
Why: No GLOBAL event covers threats to others. R117's legal_threat hold covers litigation, and R149's household_safety covers the caller's own household, so a credible threat to crews falls into sensitive_event or out_of_scope and ends politely. R116's WORM keeps the CDR and agent-side audio, not the caller's words. R113's pre-purge sweep is a DNC sweep with no threat lexicon. Nothing pages a human or holds a dispatch. The Designer concedes both gaps.
Fix needed: Add a threat_to_others GLOBAL event (lexicon plus Needle, also re-run in the post-call sweep). It plays a fixed neutral fragment, ends the call and sets a safety_hold. The hold reuses legal_hold to freeze deletion and keeps caller audio where the profile allows, or otherwise an incident record. It pages a staffed safety team and blocks every consult, survey and install dispatch to that address and number until a human clears it. Add a red-team stratum with a Tier A false-negative bound.

## A9
Winner: Breaker
Why: The flooding half is largely contained: R56 falls back from a full queue to a booking, and R87, R142 and R132 limit and detect surges. The lure half is not. An inbound caller who passes the knowledge-only challenge with brokered facts satisfies R9's identity && owner && adult guard and R88's record-owner lookup. R162's phone-to-record-owner match is a pre-dial check and doesn't apply to inbound. The Designer concedes that rep safety and repeat bookings at one address aren't modeled, and the closing controls are all new.
Fix needed: An in-home consult needs an OTP to the independently sourced number of record; otherwise the booking is a phone or video consult. Cap active consults at one per address and N per ANI or range per week, with a repeat-address alarm. Give OTP-verified callers transfer priority, and give unverified request_human a guaranteed callback to the number of record. Add a rep safety protocol: daylight slots by default, check-in and check-out with an escalation timer, a second person on flagged bookings, and a pre-visit confirmation call to the number of record.

## A10
Winner: Designer
Why: The attack assumes the closer gets "the full slot store", but the design never says that. R7 keeps the agent to coarse facts with no account, income or credit data. R119 persists only a type-less sensitive_exit label. R15 sends high-vulnerability callers to NO_SALE_SAFE_EXIT with decision-maker-only follow-up, so they are not warm-transferred to a closer. Off-channel poaching by commissioned staff is a generic sales-org insider risk that the agent doesn't make worse, and R141's mailed notice plus R148's owner-only confirmation call put a human check on any side deal.
Worth adding: An allowlisted handoff schema (name, verification_strength, product interest, quote-hash pointer) that never carries the vulnerability counter or hardship flags. Closers work only in a recorded softphone or CRM with access logging and bulk-export blocks.
