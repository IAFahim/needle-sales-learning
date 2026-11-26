## A1
TOPIC: Culturally deferential "yes" (face-saving acquiescence) passing the lexical COMMIT gate
SCENARIO: A first-generation Vietnamese-American homeowner, fluent in English, treats the caller as an authority. Throughout READ_BACK she says "yes" after each item to mean "I am listening, I respect you", the norm she grew up with. At the commit question id she says a flat, falling, unhedged "Yes." No condition, no rising pitch, no overlap. The gate sees a short, direct lexical affirm to the right question id and fires CONTRACT_SENT. She believed she had agreed to receive information.
WHY IT BREAKS: Every COMMIT exclusion is acoustic or syntactic (conditional, reported, rising, overlapping). Acquiescent "yes" is pragmatic, culturally patterned, and textually identical to consent. Needle labels text, so no feature exists to separate it. Per-dialect release strata measure ASR error, not pragmatic meaning, so the audit labels this call "correct commit".

## A2
TOPIC: High-context indirect refusals ("I'll consider it", "that's a little difficult") routed into booked callbacks
SCENARIO: A Japanese-American retiree, asked to book a follow-up, answers "Hmm, that may be a little difficult... I will consider it." In his norms this is a firm no; saying "no" outright is rude. Needle labels it a soft objection/defer, not stop. The graph books a callback inside frequency caps. On the callback he repeats the same polite formula; another callback is booked. He never says a stop-lexicon word, so the post-call DNC sweep finds nothing.
WHY IT BREAKS: Stop is a lexicon plus a GLOBAL event trained on explicit refusals. Culturally indirect refusal is a known pragmatic pattern, not a hedge on the words "don't call". The design converts a polite no into a recurring sales pipeline, which under TSR 310.4(b)(1)(i) and state harassment rules is repeated calling of a consumer who declined.

## A3
TOPIC: Non-Western name structures and gendered honorifics breaking the identity challenge and the greeting slot holes
SCENARIO: Lead record stores "Maria Garcia Lopez" as first "Maria", last "Lopez"; county title says "Garcia". Challenge-response against the lead record mismatches when she confirms "Garcia", so she lands in WRONG_PARTY and is dropped. Another lead, a Korean name stored family-name-first, is greeted by given name as surname. A third, a trans homeowner whose purchased lead still says "Mr.", is greeted "Mr." in every certified fragment.
WHY IT BREAKS: Identity is a deterministic string match against a vendor record, so false WRONG_PARTY rates track ethnicity, a disparate-impact pattern the per-accent audit never stratifies. Honorific and name-order slots are filled from lead data the caller never controls, and fragments are certified by id, not by how the filled name sounds.

## A4
TOPIC: Speech disabilities (dysarthria, aphasia, stammer, electrolarynx) filtered out by the ASR pre-gate with no disability stratum in certification
SCENARIO: A homeowner with post-stroke dysarthria answers every QUALIFY question correctly but slowly and slurred. ASR confidence falls under threshold: unintelligible re-ask, then "clarify once, then fallback" to a callback. The callback repeats the same path. A laryngectomee with an electrolarynx is classified by the media/far-field detector as device audio and ignored. Neither ever reaches a human or a quote.
WHY IT BREAKS: The release blockers stratify by dialect/accent only; speech disability is not a group with its own bound, so systematic exclusion never trips a gate. A business that serves everyone except people with speech impairments risks disability-discrimination claims (e.g. California Unruh Act, Civ. Code 51) and loses legitimate buyers.

## A5
TOPIC: Coerced owner: a relative, caregiver or abusive partner in the room scripting the owner's answers
SCENARIO: An adult son, deep in debt, wants the solar loan so he can later refinance against the house. He holds the phone on speaker and whispers each answer; his mother, the verified record owner, repeats them clearly: "Yes, I own it." "No, not moving." At commit she says "Yes." Whispers fall under the no-speech gate; side talk is never transcribed. Identity, suitability and COMMIT all pass on her own clean voice.
WHY IT BREAKS: Every safeguard keys on the verified speaker's words. Coercion is invisible in a transcript of compliant answers, and the vulnerability counter detects confusion, not duress. FinCEN's April 2024 elder-exploitation analysis singles out theft by people the victim knows, family and caregivers (fincen.gov). The design certifies the exact pattern exploiters use.

## A6
TOPIC: E-sign SMS to "all record owners" exposing a domestic-violence survivor to an estranged co-owner
SCENARIO: A woman who fled an abusive husband still shares title with him pending divorce. She agrees to solar. CONTRACT_SENT texts envelopes to all record owners, using the husband's number from a data vendor. He receives an SMS naming the company, the property, financing terms and that she is active and making decisions. He also never consented to texts from this seller.
WHY IT BREAKS: The design treats co-owners as signers, not as people whose contact may be dangerous, and has no "do not contact co-owner" household state. It sends a commercial text to a cell number without that person's prior express consent (TCPA risk) and broadcasts a survivor's activity and location-linked data to her abuser. Needle never hears anything that would block it.

## A7
TOPIC: Financial distress and affordability absent from suitability: desperate homeowners pushed into liens they cannot carry
SCENARIO: Caller: "We're two months behind on the mortgage; anything that cuts the power bill, I'll do it." Ownership, roof, shade, move horizon all pass. "Behind on the mortgage" is not a suitability column, and the vulnerability counter tracks confusion, not hardship. QUOTE offers financing with a UCC lien; the lender, not the agent, decides credit. The customer signs out of panic; savings do not cover the payment.
WHY IT BREAKS: CFPB's Aug 2024 solar-financing spotlight documents dealer fees and payments exceeding savings; its PACE ability-to-repay rule took effect March 1, 2026 (consumerfinance.gov). A suitability table blind to stated hardship lets the best-converting segment be the most financially vulnerable, and "not rescinded, installed" counts it a success.

## A8
TOPIC: Yes-ladder conditioning inside DISCOVERY/QUALIFY (the lint bans yes-eliciting openers only)
SCENARIO: After the preamble, approved discovery fragments ask: "You'd like lower bills, right?" "You care about your family's future?" "Makes sense to lock in a rate?" Each is a certified question with an expected "yes". By READ_BACK the customer has said "yes" eleven times. The commit question gets a habituated "yes" that the gate accepts as short, direct and lexical.
WHY IT BREAKS: Foot-in-the-door and commitment-consistency effects are well documented (Freedman & Fraser 1966). The design guards against yes-eliciting language only at OPENING; mid-call leading questions pass every lint and are exactly what success-tuned wording selection will favour. The COMMIT gate checks form of the yes, not whether earlier fragments manufactured it.

## A9
TOPIC: Hypomanic or manic buyers: high enthusiasm reads as the ideal close, not as vulnerability
SCENARIO: A homeowner in a manic episode talks fast, interrupts to say "Yes, yes, I want it, biggest system, sign me up," answers every slot crisply, and needs no clarify. No confusion markers, no repeated questions, so the vulnerability counter stays at zero. READ_BACK plays; he affirms instantly at the commit id. Two weeks later his family finds a $60,000 lien.
WHY IT BREAKS: The vulnerability counter is built on confusion signals (repetition, contradictions, clarify loops). Mania shows the opposite: fluency, certainty, eagerness, which every sales-derived signal scores as a strong buyer. Contracts by persons of unsound mind are voidable in many states (e.g. Cal. Civ. Code 39), and the design has no detector for this profile.

## A10
TOPIC: Lonely, isolated but lucid customers buying to keep the conversation going
SCENARIO: A widowed 74-year-old living alone enjoys the call. Small talk about weather and grandchildren is an internal transition, so the agent keeps returning warmly via approved icebreaker variants. She is lucid, passes every suitability row, and answers precisely. She says yes because the friendly caller "has been so kind" and she wants a reason for the installer to visit.
WHY IT BREAKS: Social isolation is a top fraud-risk factor for older adults, independent of cognition. The design only exits on confusion or sensitive events; rapport is treated as a free sales asset and small_talk as an unbudgeted loop. A deterministic warm voice that never tires is the ideal companion for an isolated person, and the audit labels the sale suitable.
