## A1
Winner: Designer
Why: The design already fails safe on slow certification: "states that can't reach the bound stay on deterministic fallback", R124's ramp audits 100% of the canary cohort, and R66 rollback plus R132 alarms pull a known-bad state back to fallback instead of leaving it live. The scenario's own trigger, a missed stop phrase, has a same-day fix that needs no finetune: stop = lexicon ∪ GLOBAL (R66, R93), plus the post-call sweep. The certification cost is real, but it shows up as fallback time, not as uncertified exposure or a stuck known-bad bundle.
Worth adding: The monotone-patch class (superset stop set proven by replay over all retained audio inherits the Tier A certificate), plus sequential certification that carries evidence forward for states whose gold replay is unchanged, so routine releases do not each need ~300k fresh calls.

## A2
Winner: Breaker
Why: The design makes per-dialect bounds (R93) and per-disability bounds (R147) release blockers, and R131 holds the worst cluster "to the same bound". At 1e-5 per call, small groups cannot reach that bound, so the release is blocked by arithmetic. The runtime cannot route by group because R131 keeps group labels out of runtime. R46's prohibited-basis invariant covers the product-policy table, not dial-list or campaign selectors, so the ZIP or surname exclusion workaround is not blocked by anything existing. The defense's working parts (blocker redefinition, selector invariant) are new.
Fix needed: Redefine per-group release blockers as the pooled absolute call-level bound plus per-group non-inferiority tests on turn-level Tier A rates, with a stated power analysis. A group with too little evidence gets acoustic-condition routing (low ASR confidence or worst cluster goes to a human), never exclusion. Extend the prohibited-basis build invariant to every campaign and dial-list selector (only consent, DNC, registration and suitability keys may filter), and add a reach-parity report comparing dialed share with the consent pool by census tract.

## A3
Winner: Designer
Why: The disparity source the attack names, ASR and clarify routing, is already measured where the base rates give power: R111 makes per-group false-unintelligible and fallback rates release blockers, R121 tracks "reached quote or human" parity, and R131 holds the worst acoustic cluster to the bound. Fallback leads to a human quoting from the same R46 menu (R56), so routing changes timing, not the offer. Matched pairs test the menu and process rates test the routing, which together cover what close-rate tests would detect too late.
Worth adding: Time-to-quote and quote-reached rate per acoustic cluster as a release blocker, and a pooled (hierarchical, multi-quarter) outcome-disparity review run with counsel.

## A4
Winner: Designer
Why: The attack says labeler recall "was never measured", but it is: R200 mixes planted known-answer calls, including correct stops, blind into every labeler's queue and drops labels from labelers who fail; R281 double-labels a random share of Tier A blind with adjudication; R131 corrects estimates with a two-auditor confusion matrix. Labelers hear clipped turns, not 10-minute vigils (R143), and the 100% post-call sweep (R66) and outcome proxies (R113) are independent detectors. The defense cited weaker items and missed R200/R281, but the design holds.
Worth adding: Publish the Tier A bound divided by the lower confidence bound of measured labeler recall, plus a capture-recapture estimate across human, sweep and complaint channels.

## A5
Winner: Breaker
Why: The design says plainly that "changing a row decertifies every branch that cites it" and "certificates expire and must be re-earned". It has no exemption for a value-only change. R135's bitwise-identical inheritance is written for patched runtimes, and R140/R155 do not change expiry. A weekly lender repricing therefore expires QUOTE, READ_BACK and COMMIT every week. The defense's working mechanism, typed value-only rows that re-validate without audit, is new.
Fix needed: Type every policy-row change. A value-only change (same key, unit and authored spoken form, value inside the row's declared certified range, no new Reg Z trigger term) re-validates automatically through lints, calculator property tests, the R105 audio round-trip and bitwise gold replay, with no new audited calls. A structural change (new key, new wording, a value outside the range, a new trigger term) expires the certificate and needs audited recertification.

## A6
Winner: Designer
Why: The 60% preamble hang-up premise fits cold lists. This list is consent-only, the consent names the seller and an AI voice (R59), and the call shows branded caller ID with A-level attestation. R142 keeps pacing at 1:1 with frequency caps, which keeps per-number volume low, and R59 already monitors answer rate and spam labels per number. The design never rotates numbers, and R170 suppresses a lead after two preamble hang-ups, which cuts repeat short calls. The disclosure itself is a legal floor.
Worth adding: Make short-call rate and analytics-label status per number a throttle input to the R138 dial permit, use a fixed registered number pool with per-number daily caps, and tell the lead the calling number and window at consent capture.

## A7
Winner: Designer
Why: The design sends its outbox texts from a registered short code (R89; short codes named as a channel in R115). Short codes are not under T-Mobile's 10DLC brand daily caps, and only commits send envelopes, a small share of calls. A delivery failure is a delay with modeled exits, not a lost or harmful close: WAITING_FOR substates with TIMEOUT handlers (R55), resend/wait/callback (R60), mailed or consultant signing (R120) and per-number SMS budgets (R196).
Worth adding: SMS capacity as an admission token reserved at QUOTE, priority classes in the outbox (OTP and envelope first), and carrier delivery receipts as WAITING_FOR events with vendor voice/email OTP fallback.

## A8
Winner: Breaker
Why: No existing element checks texting hours when the outbox drains. The defense itself says "the calling-hours check sits on the dial gate, not at outbox send time". R122 and R149 put registration and consent on outbound texts, R41 clamps callback booking times, and R55 stops duplicates, but none of them stops a midnight flush of solicitation texts to Florida (FTSA 8am-8pm, texts included) after a vendor outage. The working fix is new.
Fix needed: Give every outbox SMS and email effect a [not_before, not_after] window, computed at enqueue by the pinned-tz calling-hours gate for the most restrictive candidate jurisdiction, and re-check it in the executor at send time. Add a model-checked invariant that no message effect is released outside its window. Never send expired session-bound items (OTP, envelope) late; re-plan them as one next-day, in-hours notice or a human callback. Rate-limit the drain after an outage and deduplicate it by idempotency key.

## A9
Winner: Designer
Why: "No data = no dial" is a deliberate fail-closed choice, matching R114. Its cost is availability and spend, not consumer harm. Nothing in the design requires a live query on every attempt. Safe harbor needs a check against the most recent RND data, so an answer stays valid for the current data release, and R142 pacing, frequency caps and the consent-only list (R59) keep attempts per contact low. Leads with no data can still reach the agent through INBOUND_OPEN (R30).
Worth adding: Batch-query the next day's dial list off-peak into a cache keyed by (number, consent date, RND data release), have the dial permit read it, and fail closed only when the current release cannot be confirmed.

## A10
Winner: Designer
Why: Most fallback in a noise storm never reaches a live queue. R169 ends unintelligible calls with no booking, R137 sends uncertified channel classes to callback fallback, and R56 transfers warm only to an open queue and otherwise books a consult. Because the operator controls outbound arrivals, R142 admission control and R132 drift alarms can stop new dials. The real gap is that the dial permit reserves Needle capacity but not human capacity. That is a valid optimization, but nothing breaks without it.
Worth adding: A human-capacity token in the dial permit (live fallback rate × transfer share vs staffed headroom), warm transfer only when a closer is free now, and otherwise an immediate concrete booked slot instead of hold audio.
