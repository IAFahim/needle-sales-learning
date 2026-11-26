## A1
Winner: Designer
Why: R24 Tier 1 really does list "goodbye" (and "not interested") as caller-directed endings that end the call at once, and the stop path is the union of that lexicon and Needle GLOBAL. So the attack's premise, that no event covers a goodbye and the pitch keeps going, is false. R145 indirect_decline also exists. The remaining gap is narrower: lexicon variants ("bye now", "gotta go", "I'm done") and the lack of a polite closing line before hang-up.
Worth adding: A leave_taking lexicon class (bye / bye now / gotta go / heard enough) that plays one fixed "Thanks for your time, goodbye" fragment, then hangs up and suppresses the lead as an indirect_decline. Also add a pre-closing red-team stratum.

## A2
Winner: Designer
Why: R108's yield rule hands the turn to the caller at once, and R107 sends a repeated "hello?" to MEDIA_FAULT. R69 per-state visit and turn counters put a hard bound on any replay loop. The R31 invariant (no path to QUALIFY or SALES without DISCLOSED) means the worst case is a short call that ends with no pitch, which is safe, not an undisclosed pitch. The 30-second monologue costs conversion, but it is not a safety or legal failure.
Worth adding: An ordered preamble with a short lint-capped first segment (seller, sales purpose, AI), a cap of 2 replays per segment followed by a polite end, and a per-segment interruption-rate metric.

## A3
Winner: Breaker
Why: The consent infrastructure does exist (R74 PEWC artifact, R162 independent capture, R115 revocation bus). But nothing routes a caller's "where'd you get my number?" or "I never signed up" into any of it. The Designer concedes the turn falls into out_of_scope, the call moves on to IDENTITY, and the denial is never recorded, so the next campaign can redial. The defense rests on two new events.
Fix needed: Add a GLOBAL consent_source_question event. Its fixed fragment states the seller, capture date and capture channel from the R74 artifact, and the outbox texts a copy of the consent record. Add a GLOBAL consent_dispute event (lexicon plus Needle): no further pitch, a DNC or suppression write through the R115 bus, legal_hold on the session (R117), an increment to the R162 partner-fraud counter, and a human audit of that lead's consent. Add a red-team stratum of consent-denial phrasings and a Tier A metric for a denial followed by a redial.

## A4
Winner: Designer
Why: The attack's premise is false: R63 defines small_talk(valence), so the design already carries a sentiment slot. R153's lint bans rapport and flattery fragments and caps small_talk, R151 requires neutral discovery wording, and R19 sensitive_event(distress) plus R150 hardship rows cover serious bad news. "Great to hear!" would have to pass human approval despite those lints. What's missing is only an explicit build check that ties acknowledgment wording to the valence value.
Worth adding: A lint that allows a valence-presuming acknowledgment only on the matching valence. valence=negative gets a sympathetic fragment plus "Is now a bad time?", which routes to a callback or a polite end.

## A5
Winner: Breaker
Why: No existing state or event detects that the caller is driving. R65 HOLD and callback only fire if the caller asks for them, and R120 and R153 don't stop the agent from reading a dense READ_BACK and then telling the driver to open an SMS and enter an OTP. The Designer concedes the gap, and the whole defense is new.
Fix needed: Add a GLOBAL unsafe_context(driving | operating_machinery | working) event, fired by a lexicon ("driving", "on the freeway", "behind the wheel") or by Needle. It plays a fixed fragment ("Please don't use your phone while driving. When's a better time?") and routes to callback_request or a polite end. Add a model-checked invariant: once unsafe_context is set, READ_BACK, COMMIT and CONTRACT_SENT/OTP are unreachable on that call, and no fragment may tell the caller to act on the handset.

## A6
Winner: Breaker
Why: The booking half is refuted, since R41 books only a confirmed time. The hidden opt-out half stands. R108's stop-adjacent residue check covers only overlap during agent playback. R113's "unresolved unclear in closing turns suppresses redial" applies only to the NO_RETAIN stratum, not to every call as the Designer implies. R111/R121's ACCESS_PATH explicitly "never suppresses redial". So a garbled "don't call again" on a windy line can end in fallback with redial allowed, and a lexicon sweep over the garbled ASR finds nothing.
Fix needed: Any call that ends on unintelligible fallback books nothing and ends with "I'm having trouble hearing you; I'll let you go." The number stays under the R138 pending_sweep lock until a human has listened to every low-confidence or unintelligible span for an opt-out. A stop-adjacent token in any such span means DNC. The ACCESS_PATH no-suppression exception applies only after that human review clears the call.

## A7
Winner: Designer
Why: The legally decisive case is handled. R73's WRONG_PARTY state really does "DNC number, flag lead", and R73's identity challenge comes before QUALIFY, so a caller who isn't the consenting lead reaches WRONG_PARTY, not NOT_SUITABLE. R15 and R145 suppress redial on vulnerability exits and indirect declines, and R41/R142 frequency caps bound early hang-up redials. What remains (redialing a NOT_SUITABLE owner-tenant or a preamble hang-up within the caps) is campaign-hygiene waste, not the TCPA wrong-number exposure the attack claims.
Worth adding: An outcome-to-suppression table in the policy table (NOT_SUITABLE suppresses for a period set by its suitability row; two preamble hang-ups close the lead) and a model-checked invariant that every END state writes back an effect that the R138 dial permit reads.

## A8
Winner: Designer
Why: R73's challenge-response asks only for name and address, which the system already holds. R89 lints out any request for SSN, DOB, bank, card or credit data, and R89's verify_agent short-code text gives the caller an out-of-band way to check the caller. FTC guidance targets sensitive data, not a name and address. A careful caller who refuses gets clarify, then fallback or an end with no pitch, which costs the funnel but harms no one.
Worth adding: An identity_refusal event that approves of the caution, sends the verify_agent text, offers the published inbound number and ends without a pitch. Also make the anti-phishing line list exactly what is never asked ("Social Security, bank or card numbers").

## A9
Winner: Designer
Why: Every template needs compliance sign-off and must pass R18's TSR-mapped banned-claims lint and claims audit. Sale status is set only by the webhook (R17/R60). The e-sign packet carries the cancellation notice (R17), and R141 mails cancel instructions to every record owner, so a misleading goodbye cannot remove or hide the cancellation right. The attack depends on a reviewer approving a misleading fragment, not on a structural gap. Still, a state-keyed status lint is a cheap, sensible addition.
Worth adding: A status-claim lint keyed to state. Before SALE_SIGNED, ban "all set", "welcome", "congratulations", "you're done" and "purchased". The CONTRACT_SENT closing fragment must say nothing is final until signing and give {cancel_window}.

## A10
Winner: Designer
Why: In the scenario the caller speaks two seconds before BYE, which means during the goodbye audio. R108's yield rule stops any playout on near-end energy and enters PAUSE, so the turn is taken and GLOBAL cancel_or_rescind can fire. R66's sweep re-runs GLOBAL (not only DNC), and R113 makes it mandatory and fail-closed. A missed cancel at that point leaves only an unsigned envelope (R17), backed by the cancellation window and R141's mailed notice. The real but small gap is speech after the audio ends and the routing of non-DNC sweep hits.
Worth adding: A short listen window (endpointing plus about 2 s) in WRAP_UP before BYE, with late ASR routed to a POST_CALL handler. A sweep hit for cancel_or_rescind voids the envelope through the vendor API and sends written confirmation.
