## A1
Winner: Breaker
Why: R38 is a text matcher that discards incoming words matching the agent's rendered text inside a time window, before Needle, so a caller's "stop" spoken over the agent's own "stop" in the opt-out sentence is removed by construction. R108's check question and suppress-pending act on "overlap residue", which is what survives the filter, and nothing in the design says the lexicon or the post-call sweep reads pre-filter text. The PAUSE on near-end energy gives the caller a chance to repeat, but does not honor the stop already spoken.
Fix needed: The echo filter may never discard a stop, cancel or DNC lexicon token: any matched span containing one is treated as overlap residue (R24 check question at once, number suppress-pending until human review). Near-end energy above a double-talk threshold is never classed as echo. The post-call sweep runs on the raw pre-filter ASR, and the opt-out sentence is linted so "stop" is not its final word.
Worth adding: A red-team stratum of stop words timed over the agent's own matching words, with a Tier A false-continue bound.

## A2
Winner: Designer
Why: R98 defines media/far-field as an event that plays a fixed callback question and enters HOLD, not as a filter that withholds text from the stop pass. The independent safety detector runs on every utterance and the stop decision is the lexicon/GLOBAL union on ASR text (R66, R189), so "take me off your list, don't call again" hits Tier 1 regardless of the acoustic tag; the HOLD question itself suppresses on any negative.
Worth adding: A model-checked invariant that no front-end tag (media, echo, no-speech) can keep text from the lexicon and GLOBAL stop pass.

## A3
Winner: Designer
Why: Caller ID never authenticates: R195 makes only an OTP entered from the number of record unlock VERIFIED or QUALIFY, so a spoofed inbound call sends the code to the real owner's handset, and R141 checks for SIM swap. Even past that, R144 requires the action phrase "send the contract", not a "yes" clip, and R162 requires document-plus-selfie or KBA for each record owner at e-sign, with a mailed notice and install hold.
Worth adding: Never pay lead partners on verbal commits, appointments or callback requests, only on independently labeled installed outcomes.

## A4
Winner: Breaker
Why: The design never requires a linear-time pattern engine, never bounds worst-case runtime of the lexicon, canonicalizer or redactor patterns, and never says what happens when the front-end pass misses a deadline; the defense itself calls engine choice "the real gap". R188's segment cap sizes Needle's encoder window rather than the regex input, and R142's admission control protects Needle capacity, not shared front-end CPU, so a crafted long turn can stall other calls' stop path.
Fix needed: Compile every lexicon, canonicalizer and redactor pattern to a linear-time automaton (RE2/Hyperscan class) with a build check banning backreferences and lookaround and CI worst-case runtime fuzzing; cap per-turn front-end input length; run each session's front end under a CPU quota with a hard deadline, where a missed deadline fails toward the R24 check question plus suppress-pending.
Worth adding: A per-ANI front-end latency monitor feeding the inbound rate limiter.

## A5
Winner: Designer
Why: The build-phase stand-in never had sole authority over stop or commit: the independent safety detector and Tier 1 lexicon ("stop calling") end the call whatever the LLM labels, and commit is lexical over final ASR tokens (R87) and needs the action phrase (R144). Tier A supervision is human gold labeled blind (R2, R281) with planted gold calls (R200) and n-gram quarantine (R51), so an injected label does not become certified ground truth.
Worth adding: An injection-phrase lexicon that sends the call to full human audit and bars that call's teacher labels from training.

## A6
Winner: Breaker
Why: The dialled line's DNC write survives, but the design has no mechanism to capture a second number the caller names in a DNC request: R45's redactor runs ahead of everything, R74 deliberately redacts third-party contact details, and the sweep reads the redacted transcript. The defense agrees that the named second number "needs closing", and every element it offers for that is new.
Fix needed: Tighten the card pattern (Luhn plus valid IIN, never spanning a non-digit word, NANP 10-digit groups excluded), and run a deterministic in-memory dnc_number extractor on raw ASR before redaction whenever a stop token occurs in the turn, writing each named number to the DNC ledger through the R115 bus; any redacted turn containing a stop token keeps the number suppress-pending until compliance reviews the R273 span log.
Worth adding: Confirm the suppressed numbers back to the caller in the outbox text.

## A7
Winner: Designer
Why: The attack forces the system toward deterministic fallback, which is the design's intended safe direction (R2); it costs throughput, not consumer harm. Reaching READ_BACK at scale is also hard: outbound dials only double-opt-in numbers with velocity controls (R197), inbound needs an OTP from the number of record before QUALIFY (R195), and per-ANI caps apply (R87, R202).
Worth adding: Attribute audited errors to source clusters (ANI range, consent source, carrier route) so a concentrated breach quarantines that cluster instead of the whole fleet.

## A8
Winner: Designer
Why: A near-tie map buys nothing harmful: near-ties already route to clarify (R53), stop is the union with a deterministic lexicon (R66), and commit is lexical with an action phrase (R87, R144) under a safety-mass veto (R190). Unverified inbound callers cannot reach QUALIFY or commit states (R195), and the call's own visible outcome is already a stronger oracle than a 300 ms timing difference.
Worth adding: Quantize reply onset per state so speculation hit, miss and clarify are indistinguishable in timing.

## A9
Winner: Designer
Why: R62 makes name-free fragment variants the default and runs a phonetic blocklist on every spoken slot, the compiled greeting and preamble carry no name holes (R31), and personalized fragments need VERIFIED (R73, R195). Identity data comes from independent sources, not partner lead fields (R162), and double opt-in (R197) blocks a hostile form from targeting a victim's line.
Worth adding: List every assistant wake word and its phonetic neighbours explicitly in the R62 blocklist, checked on the ASR round-trip of the rendered audio.

## A10
Winner: Designer
Why: The jammed path cannot close: any re-ask at COMMIT removes the same-call close (R239), a bare "yes" is not a commit (R144 action phrase), the affirming speaker must match the VERIFIED speaker's diarization id (R112), and any second voice in QUALIFY/READ_BACK/COMMIT means no close (R148). Near-end bursts trigger PAUSE (R108), and every buyer gets an owner-only confirmation call before install (R241).
Worth adding: Count speech-present turns rejected by the pre-gate in QUALIFY/READ_BACK/COMMIT, and block a same-call close after one until a human has heard those spans.
