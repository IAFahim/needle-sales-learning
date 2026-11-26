## A1
Winner: Breaker
Why: 64.1200(b)(3) requires the opt-out mechanism to be announced within two seconds of the identification. The design's R75 only requires an opt-out sentence with a position lint (order, not timing), and the final plan's compiled preamble puts the opt-out after purpose, AI designation and recording notice, well past 2 s. The defense admits the lint has no timing bound. Its fix (opt-out moved into segment 1, a duration-sum build check) is entirely new.
Fix needed: Make the (b)(3) profile row place the opt-out clause immediately after the seller name inside segment 1. Add a build check that sums the pre-rendered clip durations (R105) between the end of the identification and the start of the opt-out and fails above 1.5 s, add a per-call playout-mark check that flags any breach as a Tier A harm, and add the deadline to the timed model.
Worth adding: Make the same timing invariant cover NEW_PARTY replays and the abbreviated replay after barge-in.

## A2
Winner: Breaker
Why: The race itself is resolved by existing elements: R192's per-pair root-handler invariant and R339's TERMINAL region make the stop win in OPENING, and the sales segment becomes unreachable, so branch 1 is impossible. Branch 2 remains. The stop exit speaks an artificial-voice confirmation (R75 "fixed confirmation") that nothing requires to name the seller. R31's DISCLOSED invariant only covers paths into sales, so an answered call can end without the identification that 64.1200(b)(1) and TSR 310.4(d) require.
Fix needed: Compile every TERMINAL fragment that can be the first agent speech to begin with the seller identity and callback number, enforced by a lint on the seller and callback keys. Add a model-checked invariant that every path from a human answer to HANGUP plays an identification-bearing fragment, and send a DNC confirmation SMS naming the seller.

## A3
Winner: Designer
Why: R109 already requires PREAMBLE segment 1 to start within about 1.5 s of the completed greeting, measured per call, with unresolved AMD treated as human. That leaves no room for a re-ask-first opening. R169 removes the worst outcome: an unintelligible fallback books nothing. "Who IS this?" is GLOBAL request_caller_identity, which has a fixed identity answer. Masking clarify in OPENING tightens a constraint that already exists.
Worth adding: A model-checked "first audio" invariant: the first agent fragment on an answered call is PREAMBLE segment 1, an identity-bearing TERMINAL fragment or the VOICEMAIL message.

## A4
Winner: Designer
Why: Nothing in OPENING can write interest, consent or a callback. Consent comes only from the R74 PEWC ledger, bookings need identity && owner && adult (R9), and COMMIT needs a lexical affirm to a read-back question id, so a clipped "...I'm interested" does no harm. Onset clipping removes only the first few hundred milliseconds, so in the attack's own example "don't call here" survives and reaches the lexicon. The preamble's opt-out sentence (R75) also gives the callee a fresh chance seconds later.
Worth adding: Buffer early media from 200 OK and flag onset-truncated first turns with stop-adjacent residue for the R24 check question and suppress-pending.

## A5
Winner: Designer
Why: The question in the attack ("when's a good time to reach them?") is not in the design. R9 lets only identity && owner && adult write a booking, and R176 sends any non-record-owner down the no-close non-owner path. R7 limits collection to coarse facts. R74 redacts third-party details, and R143 mutes IDENTITY-state answers for labelers. A volunteered "home alone" remark is a residual retention issue, not an exploit the design invites.
Worth adding: A lint banning any fragment that asks about another person's whereabouts or return time, plus a minor/alone lexicon that ends the call and quarantines the span in the same way as R119.

## A6
Winner: Designer
Why: The cited law is California's, and R40 already puts all-party-consent jurisdictions in NO_RETAIN (in memory only) until affirmative retention consent is given. The build pipeline rejects transcripts without the consent flag. R118 keeps front-end features per-utterance and discards them, and R249 requires self-hosted ASR in those states. Whether later consent could cover the pre-notice span retroactively is a narrow clarification, not a failure on every call.
Worth adding: A pre-notice quarantine in every jurisdiction: audio before the recording-notice playout mark feeds only the live stop pass and the teardown sweep, and is never retained, labeled or trained on.

## A7
Winner: Designer
Why: After a transfer the new voice is a speaker_change. R112's NEW_PARTY replays the full disclosure, so the resident does hear the preamble. R209's owner_occupied cross-check, R176's record-owner binding and R148's no-close-after-second-voice stop the sale. 227(b)(1)(A)(ii) also exempts calls made with the called party's prior express consent, and the resident is the consenting lead. The harms in the attack are already blocked.
Worth adding: A GLOBAL institutional_answer event (facility or switchboard greeting) that ends the call without asking for anyone, plus pre-dial suppression of numbers on licensed-facility registries.

## A8
Winner: Designer
Why: R9 makes the decline detector speaker-agnostic. R192 puts the root GLOBAL handler over screener and VOICEMAIL substates, and R295 model-checks that no front-end tag keeps text from the lexicon and GLOBAL stop pass. OPENING already runs ASR on greetings to expose machine_greeting() (R35). R66 sweeps every transcript before a redial, and R113 fails closed when none exists. A synthetic-voice "remove me" therefore hits the same stop path.
Worth adding: State explicitly that the post-call sweep covers greeting and screener legs, and add an OS screening canned-reply red-team stratum.

## A9
Winner: Breaker
Why: R111's hypophonia stratum covers quiet voiced speech, not unvoiced whisper. R169's human review of low-confidence spans applies only to calls that end on unintelligible fallback, not to a callee who whispers and hangs up. R295 and the raw-ASR sweep help only if ASR emits text, which energy/voicing-based endpointing may never pass on for a whisper. With no whisper stratum, a systematic miss would not block release, and a whispered opt-out could leave the number dialable.
Fix needed: Add a non-identifying unvoiced-speech detector ahead of the pre-gate so a whisper is never treated as silence or a timeout. End the call on a detected whisper with a fixed low-gain exit, count it as indirect_decline, and put the number under suppress-pending until a human has reviewed the span. Add a whispered-speech certification stratum with Tier A false-continue bounds.

## A10
Winner: Designer
Why: A device-played fake disconnect tone is built to fool dialers. It is not a clear statement to the caller that consent is revoked, so treating it as revocation by "reasonable means" is a stretch. Both outcomes in the attack are safe or bounded. Marking the number invalid stops calls, which is what the callee wants. Otherwise R170's END writeback, the two-hang-up suppression and the R138 permit govern any redial, and R73 alone decides reassignment.
Worth adding: Treat an in-band SIT after answer supervision and near-end speech as callee_device_objection (internal DNC), and never as a vacated-number signal.
