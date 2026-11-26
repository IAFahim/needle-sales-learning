## A1
Winner: Breaker
Why: The existing design handles hostility only when Needle labels it small_talk(valence=negative) (R167), and even then its fixed reply offers "I can call another day" to someone complaining about repeated calls. If the turn is labeled out_of_scope, the design's own uncertainty branch (R1, line 11: "one scripted clarify attempt, then safe fallback (callback scheduling...)") replays a clarify and books a callback. R169's "books nothing" covers only unintelligible fallbacks, and the Tier 1 lexicon has no "keep calling" or "Nth call" forms, as the Designer concedes.
Fix needed: Add a GLOBAL call_frequency_complaint/hostility class (lexicon plus Needle: "keep calling", "Nth call this week", "stop harassing", "you people") that counts as revocation by reasonable means. It writes DNC through the R115 bus and plays a fixed apology-and-end fragment. Add a model-checked invariant that no callback or consult effect is reachable after a negative-valence, complaint or hostility turn, so the out_of_scope fallback there ends with suppression. Change the R167 negative-valence fragment so it never offers another call. Add a red-team stratum of non-lexical hostile revocations with a Tier A false-continue bound.
Worth adding: Make the clarify for a high-ASR-confidence out_of_scope the R24 check question ("keep going, or let you go?") rather than "say that again".

## A2
Winner: Designer
Why: R24 (line 54-58) already splits stop handling. Only caller-directed forms ("stop calling", "take me off") are Tier 1. A bare "stop" is Tier 2: the agent pauses with no DNC write, and a topic continuation such as "go back, what was the monthly?" resumes the call through the resume window and R48 repair_request. The check question comes before any DNC write, so no oral re-consent is ever needed, and R127 already requires minimal pairs mixing money words with stop.
Worth adding: Name "stop" plus a repair cue ("go back", "what was", "really?") as an explicit Tier 2 pattern, with a per-marker false-stop release bound.

## A3
Winner: Breaker
Why: R63 sends the no-speech/low-confidence pre-gate straight to unintelligible, so sobbing after a question (not during playback, where R108's yield would apply) gets the "didn't catch that" re-ask. R19's distress lexicon can't fire on audio that never becomes words, and "never mind" then continues QUALIFY as acknowledge. The Designer concedes that non-speech vocalizations are not a feature anywhere in the design.
Fix needed: Add a pinned, per-utterance, non-identifying non-speech vocalization detector (sob, sigh, laugh, groan) that complies with R118 and runs before the pre-gate. A sob or sustained voiced non-speech turn routes to sensitive_event(distress) with a fixed "Take your time, is this a bad moment? I can let you go" fragment, no pitch and no same-call close. A following "never mind"/acknowledge counts as indirect_decline. Add per-stratum certification bounds and a rendered-crying red-team stratum as release blockers.

## A4
Winner: Designer
Why: The existing design catches the joke before it decides anything. R43 per-slot ranges send roof_age=100 to clarify, and R186 role-binding flags "like me" as a binding mismatch. R2's critical-slot read-back confirms every qualification-gating slot ("About a hundred years, is that right?") before a transition depends on it. R211 also cross-checks roof age with permits and shade with aerial records, R27 trains on hyperbole, and R90 gives any NOT_SUITABLE a correction link.
Worth adding: A NOT_SUITABLE resting only on a spoken slot that conflicts with permit or aerial records should go to survey, never to an honest exit.

## A5
Winner: Breaker
Why: R37 and R5 bind the agent's pricing, but nothing in the design binds the human closer reached through R56 request_human. R203 passes only a quote-hash pointer, and the Designer concedes the human channel isn't tied to the same table. So "ask for a manager" becomes a discretionary discount path. That is the classic discretionary-markup disparity that matched-pair tests (R46) can't see, because their pairs never haggle or escalate.
Fix needed: Use one pricing authority. The closer CRM has no free price field, and any human concession is an R37 policy row applied by the same calculator with a reason code and evidence id, producing a new quote hash, a READ_BACK/written re-disclosure and R134 monitor coverage. Offer any concession row to every buyer who qualifies, and add haggle and request-human arms to the matched-pair tests, with price gaps between arms counted as Tier A fair-lending harm.

## A6
Winner: Breaker
Why: R86 and R81 only exclude a conditional affirm from commit. Nothing in the design answers the stated condition, and R5's claim_prior_promise covers claimed earlier promises, not a condition attached to acceptance. R144's action-production prompt changes the wording of the re-ask, but the caller can still say "send the contract" believing the critter guard and the Christmas date are included. The Designer concedes the re-ask never says the condition is refused.
Fix needed: Add a condition_stated(topic) event. Before any re-ask, a fixed policy-table fragment answers the condition ("Installation is estimated <range>; we can't promise earlier", "<add_on> is not included", or "The contract includes only what I read"). Any unmet condition blocks a same-call close and leads to a written proposal listing what is not included, plus a consult. Log customer-asserted conditions for the R144 post-sign check, and add a Tier A stratum of a conditional affirm followed by a bare yes.

## A7
Winner: Breaker
Why: Between commit and signature, the design voids the envelope only on cancel_or_rescind (R173). A soft "let me sleep on it" lands as defers_decision, which only feeds the R15 counter, or as acknowledge. So the envelope stays live, the WAITING_FOR_SIGNATURE help (R60) still steers toward signing, and R172's unsigned-envelope reminders keep coming. R172's "nothing is final until you sign" softens the pressure but doesn't stop it, and the Designer concedes the gap.
Fix needed: In CONTRACT_SENT and WAITING_FOR_SIGNATURE, map defers_decision, indirect_decline or a hesitation lexicon hit ("think about it", "sleep on it", "hold on, actually") to an envelope void through the vendor API, with a fixed "No problem, I've withdrawn the link, nothing was signed" fragment and a written proposal. Add an invariant of no sign prompt and no reminder after a defer, release the envelope only after the commit turn's endpointing plus the R173 listen window, and track signature after an in-call retraction as a Tier A metric.

## A8
Winner: Designer
Why: Resume semantics already exist. R39 replays an interrupted mandatory segment from its start and sets completion flags only on uninterrupted playback, and R134's monitor refuses CONTRACT_SENT without those marks for the quote hash. Repeated barge-in during the read-back is an R152 overcommitment signal that leads to a written proposal and a human consult, not a silent loss. R144's delayed teach-back and R44's summary read-back test understanding beyond node visits.
Worth adding: A single uninterrupted recap before the commit question after any digression, and keep READ_BACK repair turns out of the R69 turn budget.

## A9
Winner: Designer
Why: The attack's central premise is false. R253 already adds an oral CCPA notice-at-collection segment to the preamble whose purposes include AI training, linted against the 7012 element list, plus an SMS with the full notice. R40 adds retention consent and decline_recording, and R8 ask_if_human and R20 recording_question give scripted truthful answers. A direct "do you learn from this?" lacking its own event is a coverage polish, not a deceptive omission of something already disclosed.
Worth adding: A GLOBAL data_use_question event whose fixed answer names live listening (none), human quality review and model-improvement use, and routes to decline_recording.

## A10
Winner: Designer
Why: Hitting the budget ends in R69 WRAP_UP with a text summary, and a high small_talk ratio leads to R153's written proposal with cooling-off. Neither is NOT_SUITABLE or an eligibility or credit decision, so the ADMT "adverse decision" claim does not hold. Long turns are handled by R44 segmentation and R25 endpointing, and R131's worst-cluster check plus R46 path-divergence metrics already measure disparity between groups. The cost is a slower sale, not harm to the caller.
Worth adding: Count budgets on agent-side loops rather than caller talk time, and route budget exhaustion with no negative signal to a booked consult at a named time.
