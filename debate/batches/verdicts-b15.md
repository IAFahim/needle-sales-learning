## A1
Winner: Breaker
Why: The design has no event for a spoken privacy request. Multi-label GLOBAL (R189) and the root UNEXPECTED_EVENT log (R52) only make sure a DNC write happens and the turn is logged. Nothing opens a deletion or opt-out-of-sale request, starts the 45-day or 15-business-day clock, or tells the caller how to submit one, as 11 CCR 7020 requires for a request sent by a method the business did not designate. The Designer concedes that "no event opens the CCPA clock", so the defense rests on the new privacy_request event.
Fix needed: Add a GLOBAL privacy_request(kind: delete, know, correct, opt_out_sale_share, limit_sensitive) event, detected by lexicon plus Needle, that co-fires with DNC and never replaces it. It plays a fixed acknowledgement fragment. Its outbox effect opens a DSAR ticket stamped with the statutory due date and sends written confirmation with submission instructions. Deletion then spares only the TSR WORM set, legal_hold and a hashed-number suppression entry. Extend the post-call sweep to privacy phrasings and add a Tier A red-team stratum.
Worth adding: Add an SLA alarm on DSAR tickets nearing day 45.

## A2
Winner: Breaker
Why: The cited elements (R7, R118, R119, R131, R143, R90) do shrink what is held, but labels, outcomes, reason codes, vulnerability or sensitive_exit flags and transcripts still exist. No element maps a person to those artifacts. R162 covers identity answers in the call, not a 7062-grade verification standard for a request for specific pieces. The Designer concedes both gaps, and its answer (registry, OTP plus mailed code plus declaration) is new.
Fix needed: Build a subject-artifact registry. Every written artifact carries a session id, and only the DSAR service can resolve number/lead → sessions → manifest (lead record, slots with provenance, outcome, reason codes, flags, audit labels, transcripts, derived paraphrases) through a keyed surrogate map. A request for specific pieces needs OTP to the verified number, a code mailed to the property of record and a signed declaration, and falls back to a categories response if verification fails. A release check fails any artifact type that is not registered.
Worth adding: Disclose inferences only as plain-language reason codes, never raw model scores.

## A3
Winner: Designer
Why: The attack assumes the consent proof exists only at the broker, and the design already says otherwise. R74 requires a per-number PEWC artifact (timestamp, seller, disclosure version) at the seller's own dial gate. R162 requires an independent consent-capture provider. R116 keeps the consent artifact in the seller's WORM record set for 5+ years under a legal obligation the broker's DROP purge does not reach. A DROP deletion at a broker is not a TCPA revocation of consent given to this seller, and stale resold copies still have to pass the seller-side artifact gate.
Worth adding: Escrow the consent artifact into the seller's WORM store at lead intake, and make vendors forward DROP processing notices into the R115 bus as suppressions.

## A4
Winner: Breaker
Why: The deterministic fallback keeps calls running, but only as callbacks or humans, so the AI product itself is gone. Needle is finetuned on "the union of all data" and seed transcripts do feed intent training (R18). The design has no per-source lineage and no certified model that excludes the seed data. R7's "deletion = data operation, no retrain" removes data, not what the weights learned, which is exactly what FTC disgorgement orders target. The Designer concedes there is no clean target, so the defense rests on the new lineage manifest and clean-room variant.
Fix needed: Give each release a source-lineage manifest (per-source content hashes plus a legal-basis/purpose record), and have the build reject any source without one. Train and certify a standing "clean-room" Needle on synthetic plus consented on-policy data only, as the disgorgement fallback. Require written legal review before any legacy seed source is used for AI training.
Worth adding: Make per-source ablation retrains a periodic drill, so the recertification time is known.

## A5
Winner: Designer
Why: The attack misreads the design. R33 means real data is never replaced by synthetic data, not that it is kept forever. R7 explicitly puts real utterances in deletable gold sets, with deletion as a data operation. R135 re-keys equivalence against whatever gold set is retained, so deleting an item does not break replay. R143 sets a raw-audio TTL, R40 and R113 provide NO_RETAIN, and R116 has a defined 5-year period. Erasure is possible by design. The missing published schedule is a notice item, covered under A10.
Worth adding: Publish a per-category retention schedule. Make the real-data training pool a rolling window, age out short NOT_SUITABLE and no-sale calls sooner, and recount rule-of-three after deletions.

## A6
Winner: Designer
Why: The existing design contradicts the scenario's key steps. R40 already bars processors from training on call data, the core term that makes a vendor a CCPA service provider rather than a third party. R7 applies surrogates before the big model sees transcripts. R143 confines labeling to an in-house or vetted enclave with no download, not an open subcontracted crowd. R68 pins ASR and prefers self-hosting. Ambriz v. Google is still pending on a capability theory, but it turned on vendor terms that allowed the vendor's own use, which R40 forbids here. The leftover risk is that vendor terms are not pinned with the bundle, which is a polish item.
Worth adding: Put a vendor/subprocessor register (service-provider contract, no own use, zero retention, flow-down approval) into the certified bundle hash. Require self-hosted ASR in all-party-consent states, and name "service providers, including AI services" in the recording notice.

## A7
Winner: Designer
Why: Under 28 CFR 202.204, "biometric identifiers" are voice prints and patterns "enrolled in a biometric system and the templates created by the system". R118 bans persisting any speaker embedding or template, so raw call audio does not count toward the 1,000-person voice threshold. The agent collects no account, income or credit data (R7). Credit facts are never spoken (R73) and exist only as lender-provenance slots (R90), so labelers, who get clipped and muted audio in a no-download enclave (R143), do not receive bulk financial data. The scenario's offshore-subcontractor route is excluded by R143's in-house or vetted labeling.
Worth adding: Make "vetted" explicit as a Part 202 covered-person screen (ownership, location, employment). Keep processing US-only, and give external red-team crowds only synthetic data.

## A8
Winner: Breaker
Why: Arranging or brokering consumer financing plausibly makes the seller a GLBA financial institution under the FTC's rules. Information a consumer gives in order to obtain financing is NPI even without an SSN. The design's financing gate covers only Reg Z and ECOA: there is no initial privacy notice, no opt-out before NPI goes to nonaffiliated partners, no Safeguards program (Qualified Individual, MFA, encryption, risk assessment) and no 30-day FTC notification path for 500 or more consumers. The cited elements (R45, R89, R90, R143) cut down sensitive fields but do not meet these duties, and the Designer concedes the gap.
Fix needed: Add a GLBA row to the regulation profile. The initial privacy notice goes in the e-sign packet and the outbox. A build invariant on the lead-gen/partner handoff effect blocks NPI sharing with nonaffiliated parties unless there is an opt-out or a 313.13 service-provider or joint-marketing contract. Stand up a 16 CFR 314 Safeguards program, keep only lender reference tokens in replay stores, and add an incident runbook with FTC notice within 30 days for 500 or more consumers.

## A9
Winner: Breaker
Why: Minimization (R7, R118, R119, R131, R143, R116) limits what a breach exposes, but nothing maps people and data elements to artifacts. Big-model paraphrases can carry details the scrubber missed, and the design never says where the surrogate-to-real map lives or that it is kept apart from the training bucket. Counsel could not reliably list affected residents per state, or which elements were exposed, inside 30-day deadlines. The Designer concedes the lineage gap.
Fix needed: Reuse the A2 subject-artifact registry, tagged with data-element classes and jurisdiction from the validated address, so a breach query returns affected residents per state. Keep the surrogate-to-real map in a separate KMS-protected vault, never co-located with training data. Re-scrub every big-model paraphrase and reject outputs with address or loan patterns. Run a yearly tabletop drill against the 30-day statutes.

## A10
Winner: Breaker
Why: The PREAMBLE is the right mechanism, being compiled, unskippable, playout-marked and profile-driven (R31, R39, R75), but its certified segment set has no CCPA notice at collection: categories, purposes including AI training, sold/shared status, retention, and a policy link. CCPA requires that notice at or before collection, including orally on the phone. The weaker half of the attack is that R47 does not show a third-party lead sale (the salesperson of record may be in-house), but the missing notice alone is a gap, and the Designer concedes it.
Fix needed: Add a CCPA profile row: a short oral notice-at-collection segment (categories, purposes including AI training, sold/shared yes or no, retention, link) with a lint against the 7012 element list, plus an outbox SMS with the full notice. Add a GLOBAL opt_out_sale_share event. A build invariant blocks any partner handoff unless the notice segment is playout-marked and no opt-out is set, or the partner is contracted as a service provider.
Worth adding: Keep the oral segment short and chunked under R165's preamble timing limits.
