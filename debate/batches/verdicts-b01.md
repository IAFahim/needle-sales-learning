## A1
Winner: Designer
Why: The existing design limits what a phantom "yeah" can do. confirm_order only reaches CONTRACT_SENT. The sale exists only after an OTP e-signature by all record owners, confirmed by vendor webhook (R17/R22/R60/R88), and the R15 teach-back requires the real customer to state payment and term before the close. A hallucinated affirm sends an envelope the customer can ignore, and the false-commit rate is already Tier A on human-audio-labeled real calls. The design does not check that speech actually happened, but that gap causes no binding harm.
Fix needed: n/a
Worth adding: The voicing-evidence gate on commit tokens (ASR word timestamps aligned with pinned VAD/voicing frames) plus a non-speech red-team stratum at AWAIT_CONFIRM.

## A2
Winner: Breaker
Why: The certified bundle (R67/R68) hashes the graph, weights, fragments, tool lists, ASR and policy table, but not the TTS engine, voice, text normaliser or seed. R59 even adds runtime voice/prosody variation. The golden-audio canary replays ASR input, not agent output. A vendor TTS or normaliser update can change how a READ_BACK escalator or rate sounds after certification, and every text-level check still passes. The written contract does not cure a spoken READ_BACK that the design itself makes mandatory (R85).
Fix needed: Pin the TTS engine, voice, normaliser config and seed in the certified bundle. Give every policy row an authored spoken form that code verbalises before TTS, so no symbols or abbreviations reach the normaliser. Pre-render every fact-bearing clip at build time with an audio hash and a pinned-ASR round-trip check against the spoken form. Extend the daily canary to compare output audio, and decertify on any diff.
Worth adding: n/a

## A3
Winner: Designer
Why: R14 enters AWAIT_* only after the commit question finishes playing, and treats anything overlapping agent playback as backchannel. A "yes" given while the caller still hears the cancellation clause comes before the question. With a 400 ms one-way delay it reaches the server while the question is still playing, so it is discarded and cannot commit. Teach-back (R15) and the written cancellation notice (R17) cover the rest. The delay only blurs the last few hundred milliseconds of the question itself.
Fix needed: n/a
Worth adding: Measure one-way delay per call (RTCP RR/DLSR) and widen the overlap and playback windows by that delay plus a jitter margin. Lint the commit question as a separate fragment after a fixed pause.

## A4
Winner: Breaker
Why: In the scenario the hellos come before the PREAMBLE. The PREAMBLE then plays uninterrupted into a dead path, so the R39 barge-in replay never triggers and the playback engine writes the delivered flags. Playout marks prove transmission, not receipt. Nothing in the design detects one-way RTP. If the path recovers during IDENTITY, the callee goes on to the pitch without ever having heard the AI designation, recording notice or opt-out.
Fix needed: Make media health a root telephony event. Write a mandatory segment's delivered flag only if far-end RTCP receiver reports show the agent's RTP arriving with acceptable loss across that segment's span. If reports are missing, or the callee keeps repeating "hello?" or giving no response, enter MEDIA_FAULT: hang up and book a lawful callback that starts again from PREAMBLE, or replay the full PREAMBLE once the path is confirmed. Add one-way-RTP fault injection in every state.
Worth adding: n/a

## A5
Winner: Designer
Why: The existing design already gives the caller the floor back. Every fragment ends at a question and AWAIT state. Any detected uplink burst is a barge-in that stops playout (R10/R14). A stop repeated in turn hits the Tier-1 lexicon or GLOBAL, and DTMF opt-out keys (R75) are a channel echo suppression cannot gate. Losing words the handset never transmits is a channel limit that no design, human or AI, can fully overcome. The new yield and residue rules only polish this.
Fix needed: n/a
Worth adding: Treat a hangup during agent playback, or overlap residue containing stop-adjacent tokens, as suppress-pending until review. Add a maximum-fragment-duration lint.

## A6
Winner: Breaker
Why: The TSR's abandonment rule (16 CFR 310.4(b)(1)(iv)) requires connection within 2 seconds of the completed greeting, and FCC 64.1200(a)(7) has the same rule. The safe harbor caps abandonment at 3% per campaign per 30 days, with a recorded message. The design's OPENING waits for more speech and runs AMD with no timing invariant and no abandonment counter, and the defense concedes both. A pre-rendered PREAMBLE removes inference latency but not the AMD wait, and AMD on greeting length can play VOICEMAIL to a live person.
Fix needed: Add a regulation-profile invariant that the first PREAMBLE segment starts within about 1.5 s of the completed greeting, measured per call. AMD may not delay past that deadline, and an unresolved AMD result is treated as human. Enter VOICEMAIL only on a beep or confirmed machine cue, never on greeting length alone. Add a per-campaign 30-day abandonment counter capped at 3%, with the safe-harbor recorded message on abandon, and halt dialing on a breach.
Worth adding: n/a

## A7
Winner: Designer
Why: A false <rise> fails safe. It only excludes a turn from the commit set and sends the call to a closed re-ask, then to callback or human (R80/R56). It never produces a false yes. R26 already sets per-group clarification and error bounds by dialect as release blockers, which catches an uptalk dialect stuck in re-asks. R28 tracks time-on-fallback per close state. The remaining cost is throughput, not harm.
Fix needed: n/a
Worth adding: Certify the prosody detector on its own, with per-pitch-range false-rise bounds. Abstain (emit no token) when voicing confidence is low, and normalise against the caller's own F0 baseline from earlier turns.

## A8
Winner: Breaker
Why: R15's vulnerability counter explicitly counts unclear(), so atypical speech that Needle cannot parse can drive NO_SALE_SAFE_EXIT, which also suppresses redial. The design's strata (R26/R93) cover dialect and accent only, so no release blocker measures disability-correlated denial. The Breaker is wrong that such exits count as successes (only NOT_SUITABLE does). The disparate-denial gap stands on existing elements, and the defense concedes it.
Fix needed: Add speech-disability strata (dysarthria, hypophonia, stuttering, electrolarynx, aphasia) to the gold sets, using consented data. Make per-group false-unintelligible, false-vulnerability and fallback rates release blockers. Exclude unintelligible, low-ASR-confidence and pure-ASR-quality unclear events from the vulnerability counter. After repeated unintelligible re-asks, route to an ACCESS_PATH (DTMF answers, SMS/web self-serve, or a human with extra time) that is counted as an access failure, never a safe exit, and never suppresses redial.
Worth adding: n/a

## A9
Winner: Breaker
Why: R9's speaker_change() only resets identity. A second adult at the same address can pass the IDENTITY challenge and reach READ_BACK and the commit without ever hearing the AI designation, recording notice or opt-out. Disclosures are delivered once per call (R31/R39), and silent listeners are never addressed. NO_RETAIN covers retention in all-party states but not the AI or opt-out disclosures, and the defense concedes the missing replay.
Fix needed: Make speaker_change() enter a NEW_PARTY state that replays the compiled disclosure block (AI designation, seller, purpose, recording, opt-out) as mandatory segments before any further pitch, and revert recording to NO_RETAIN until the new party consents. Play a short compiled re-disclosure at the start of READ_BACK to cover silent listeners. Require the affirming speaker's diarization id to match the VERIFIED speaker at the commit gate.
Worth adding: n/a

## A10
Winner: Breaker
Why: The design's "post-call DNC sweep of every transcript" (R66) can run on the live in-memory ASR transcript, so that half of the attack mostly fails. But the sweep re-runs the same deterministic lexicon and GLOBAL on the same text that live Needle missed, so it adds little for these calls. Human audio audit and the certification gate exclude every NO_RETAIN call, and that is the default for all-party-consent states without affirmative consent (R40). A large, non-random share of production traffic is therefore outside the per-call harm bound and the drift alarms, and the existing design neither handles this nor reports it.
Fix needed: Make the teardown sweep mandatory before purge, with an attestation log, and suppress the number if the sweep fails or no transcript exists (fail closed, including for recording or transcript fork faults). Treat NO_RETAIN as its own stratum with a conservative profile: any unresolved unclear in the closing turns or any Tier-2 stop suppresses redial. Bound its harm with outcome proxies (later complaints, repeat DNC requests, rescissions) compared against the retained stratum, and state the coverage gap explicitly in the certification report.
Worth adding: Where lawful, ask for consent to a short-lived, audit-only retention so that a sample of NO_RETAIN-profile calls can be human-labeled.
