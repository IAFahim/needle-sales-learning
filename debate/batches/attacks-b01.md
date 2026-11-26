## A1
TOPIC: The COMMIT gate's acceptance shape (short lexical "yeah/okay") is exactly the shape of ASR insertions and hallucinations on non-speech
SCENARIO: READ_BACK ends with "Do you want to go ahead?" The homeowner exhales, coughs, and a TV murmurs in the next room. The ASR emits "yeah." with decent confidence. Prosody shows no rise (nothing to rise), no overlap, no conditional, no reported speech. It is short, direct and lexical: every gate passes. Needle labels affirm, grounding finds "yeah" in the final text, and CONTRACT_SENT fires on a "yes" that nobody said.
WHY IT BREAKS: Every filter checks for features of hedged speech. None checks that speech happened. Short fillers are the most common ASR insertions. Koenecke et al. (FAccT 2024, "Careless Whisper", arXiv 2402.08021) found hallucinated text in about 1% of Whisper transcriptions, often during non-speech, so the confidence pre-gate does not filter it out.

## A2
TOPIC: TTS is not in the certified bundle, so certified text is not certified audio
SCENARIO: A fragment fills a hole with policy rows "2.99%", "$0.0049/kWh escalator" and "Rd." from the lender's address. The TTS normaliser reads "two point nine nine", then "zero dollars and zero cents per kilowatt hour", and says "Road" as "R D". A vendor TTS update changes how it reads "%" in some contexts. The trace replays bit-identically as text. The customer heard a different escalator from the one logged as read back.
WHY IT BREAKS: The bundle hashes graph, weights, fragments, tool lists, ASR and policy table, but not the TTS engine, voice, text normaliser or audio. Disclosure law is about what was conveyed, and neural TTS can sample nondeterministically. The audit replays text, so a mispronounced material term passes every lint and canary that checks text.

## A3
TOPIC: Network latency makes server-side "overlap" and "uninterrupted" flags wrong from the caller's point of view
SCENARIO: A mobile caller has about 400 ms of delay in each direction. The read-back's last clause ("...you may cancel within three business days") finishes on the server. The caller says "yes" while still hearing "you may cancel". Their "yes" reaches the server about 400 ms after playback ended, so it is marked non-overlapping and immediate. The commit is accepted, and the disclosure is logged as delivered uninterrupted.
WHY IT BREAKS: The commit gate excludes overlapping answers and counts mandatory segments only on uninterrupted playback, but it measures both on the server's clock. Round-trip delay hides real overlap. ITU-T G.114 recommends under 150 ms one way, and mobile VoIP routinely exceeds it. A "yes" given before the cancellation term was heard becomes a clean commit.

## A4
TOPIC: One-way audio: the preamble plays into a dead media path and is logged as delivered
SCENARIO: A NAT or SBC fault means the agent's RTP never reaches the callee, while the callee's audio does reach the agent. The callee says "Hello? ...Hello?" The OPENING sees speech and plays the compiled PREAMBLE (AI designation, recording notice, opt-out) with no interruption. Re-INVITE fixes the path 20 seconds later, in the middle of DISCOVERY. The callee never heard a disclosure, but the log says all segments played uninterrupted.
WHY IT BREAKS: "Uninterrupted playback" is measured as transmitted, not received, and no telephony event signals that audio is going one way. Repeated "hello?" is labeled unclear or small_talk, not media failure. The AI designation and recording notice under CIPA are certified as delivered on calls where they were provably silent.

## A5
TOPIC: The caller's half-duplex speakerphone or echo canceller removes their "stop" while the agent is talking
SCENARIO: An elderly homeowner on a cheap cordless phone uses speakerphone. During the pitch they say "Stop calling me, take me off your list." The handset's echo suppressor gates the uplink while the far end is loud, so the server receives near-silence plus a clipped "...list." The no-speech pre-gate drops it and the pitch continues. The post-call DNC sweep reads the transcript, which never contained the stop.
WHY IT BREAKS: Speakerphones and many handsets use half-duplex switching or aggressive double-talk suppression, which mutes the near-end talker while far-end audio plays. The design's stop lexicon, GLOBAL pass and post-call sweep all depend on the words reaching ASR. A refusal spoken over the agent is the case most likely to be erased, and the backstop cannot recover audio that was never sent.

## A6
TOPIC: The OPENING's wait-for-callee and machine detection create TSR "abandoned calls" and dead-air hang-ups
SCENARIO: The callee answers "Hello?" The OPENING waits for more speech and runs AMD to rule out a machine greeting, then renders the first fragment. That is about 2.5 to 3.5 seconds of silence. Many callees hang up on silence. On a long human greeting ("Hi, Smith residence, who's this?"), AMD says machine and the agent plays VOICEMAIL to a live person.
WHY IT BREAKS: Under TSR 16 CFR 310.4(b)(1)(iv), a call is abandoned if the person is not connected to a sales representative within two seconds of their completed greeting. The safe harbor (310.4(b)(4)) caps abandonment at 3% per campaign per 30 days and requires a recorded message. The design adds deliberate latency to the opening and has no 2-second timing invariant or abandonment-rate counter.

## A7
TOPIC: The final-rise prosody token fails on narrowband telephone audio and on habitual uptalk
SCENARIO: A low-voiced caller (fundamental about 100 Hz) answers "Yes." on a G.711 line. The pitch tracker, with no fundamental to see, makes an octave error on the final syllable and reports a rise, so the agent gives a closed re-ask, then falls back. A second caller who habitually uptalks says "Yes, let's do it?" three times and can never commit, so they are routed to callback.
WHY IT BREAKS: The telephone band is about 300 to 3400 Hz, which removes the fundamental of most adult male voices. Pitch must be inferred from harmonics, where octave and halving errors are common. Uptalk is a feature of some groups' dialects, and the per-group bounds only measure dialect or accent at the ASR and Needle level. A noisy prosody veto creates false refusals that are spread unevenly, and certification never measures the prosody front end on its own.

## A8
TOPIC: Atypical speech (dysarthria, Parkinson's, post-stroke, electrolarynx) routed into "unintelligible" or vulnerability exits
SCENARIO: A competent homeowner with Parkinson's hypophonia, or one using an electrolarynx after a laryngectomy, answers clearly to a human. ASR confidence is low, so they get an unintelligible re-ask, then clarify once, then fallback. Or slurred-sounding speech pushes the vulnerability counter and they get NO_SALE_SAFE_EXIT. Every call from a speech-disabled owner ends with no service, and the logs label each one an "honest safe exit".
WHY IT BREAKS: Release strata cover dialect and accent, not speech disability, so no per-group bound blocks release. Koenecke et al. (2024) found that hallucination rates rise for speakers with aphasia. A vulnerability heuristic based on how speech sounds treats disability as incapacity, which risks Unruh Act and ADA claims of a disability-based denial of service, and none of it appears in harm metrics that count exits as successes.

## A9
TOPIC: A party who joins mid-call (extension pickup, three-way merge) never hears the preamble, and there is no telephony event to say so
SCENARIO: After the PREAMBLE, the wife picks up the bedroom extension on the same landline, or the husband merges his brother in by three-way calling. Media just mixes, and no SIP or telephony event fires. The new listener talks, hears the price, and later answers the commit question. Nobody told them that the voice is an AI, that the call is recorded, or how to opt out.
WHY IT BREAKS: Mandatory segments are "delivered" once per call, not once per listener. A shared landline line or carrier conference bridge produces no event at the StateSmith root. CIPA (Penal Code 632) needs consent from all parties to a confidential communication, and the AI designation must reach the person deciding. The speaker-change detector, if it fires at all, relabels a turn but does not replay the PREAMBLE.

## A10
TOPIC: No-retain and recording-failure calls blind the post-call DNC sweep and drop out of the audited harm measure
SCENARIO: A Californian says "Don't record me." The agent enters no-retain mode, or the SIPREC recording fork fails silently on one SBC. Later the caller says "just stop calling" in a mumble, and live Needle misses it, which the design lists as an open item. The post-call DNC sweep has no audio or transcript to scan, so the number is redialed. These calls are also never in the human-audio audit sample.
WHY IT BREAKS: The design's backstop for missed voice stops, "post-call DNC sweep of every transcript", assumes retention. Privacy-asserting callers and silent recording faults are exactly the calls it cannot sweep. Certification measures harm "only on real calls labeled by humans listening to audio", so these calls are excluded from the gate. That is selection bias toward callers who stay calm and agree to recording.
