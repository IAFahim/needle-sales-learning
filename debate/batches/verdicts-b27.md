## A1
Winner: Designer
Why: The attack assumes a fixed vendor endpointer at 500-800 ms, but the design already has semantic endpointing (R25: incomplete() in every state plus a dangling-word rule, "threshold short when complete"), and timers fit from real calls and A/B tested (R65). After the endpoint, the remaining work is two passes of a ~26M model and a C transition. The longer Tier A wait is a deliberate safety trade, and R100 already measures per-state p95 reply latency.
Worth adding: The silence-onset precompute and a per-state "caller-perceived gap" plus "hello?"/re-speak rate metric, so the trade-off in Tier A states is measured, not assumed.

## A2
Winner: Designer
Why: The existing design already removes the timing signal the attack relies on: R301 quantizes reply onset to a fixed post-endpoint delay bucket per state "whether speculation hit, missed or clarified", with a timing-indistinguishability CI test. A lien or cancellation question therefore can't be audibly slower than a routine turn in the same state. Fact answers are also pre-rendered at build time (R105), so a miss adds no TTS time.
Worth adding: The defense's onset-by-event-class test should be folded into R301's CI test, and the defense should have cited R301 rather than proposing it as new.

## A3
Winner: Designer
Why: Under R301 the onset of a stop or cancel reply is the same fixed bucket as a cache hit, so safety exits are not "guaranteed the worst latency". Tier 1 stop phrases are a deterministic lexicon that ends the call immediately (R24), GLOBAL runs every turn, and hang-ups are root telephony events with a POST_CALL handler (R173), so the next state is defined. The DNC write and the written confirmation are meant to happen even after a hang-up.
Worth adding: Keep GLOBAL exit fragments resident in the playout buffer and give exit onset its own p99 bound.

## A4
Winner: Designer
Why: The pressured "uh, yeah, okay I guess" cannot close the sale in the existing design: R144 requires the action phrase "send the contract", not a yes, R77 limits commits to a narrow affirm set, and any re-ask at COMMIT means no same-call close and a written proposal with cooling-off (R239-3). The silence may make the caller uncomfortable, but it cannot turn that discomfort into a contract.
Worth adding: A fixed "No rush, you can also get this in writing" fragment on a silence(duration_bucket) event in AWAIT_CONFIRM, and hedge tokens added to the hesitation lexicon.

## A5
Winner: Breaker
Why: The defense agrees that the agent has no continuer, and its fix (continuers, a channel_check event) is entirely new. The existing pieces don't close the gap. The R44 merger joins segments inside one turn, but a caller's "you still there?" ends that turn, so the rest of the story arrives as a new turn. Worse, R107 treats repeated "hello?" as a media fault and hangs up. On a phone line, 20+ seconds of total silence from the listener reliably makes callers check the line, which breaks up the suitability answers that matter most.
Fix needed: Add a certified continuer set ("mm-hm", "I see", "go on", no assent words) that plays only in intra-turn pauses scored non-final by incomplete(), after about 6 s of caller speech, never over voiced frames and never in AWAIT_CONFIRM. Add a channel_check event that answers "Yes, I'm here, go ahead" and keeps the long turn open so the R44 merger joins both sides. Exclude channel_check from the R107 "hello?" counter, and add a fragmentation-rate bound on a long-narrative stratum.

## A6
Winner: Breaker
Why: The design does define barge-in, but that rule produces the attack's first horn: R108 stops playout on any near-end burst and says "Sorry, go ahead", and R39 replays an interrupted mandatory segment from the start. A caller who says "mm-hm" every few seconds can therefore stop the preamble or READ_BACK from ever completing, and the agent keeps apologising. That is a systematic failure for heavy-backchannel dialects and age groups, the very groups the per-group bounds protect. The defense's fix (duck-then-decide) is new.
Fix needed: Duck-then-decide: a burst during playback ducks audio and holds it for up to about 400 ms while the lexicon classifies the residue. A short backchannel with no stop-adjacent token resumes from the current clause and keeps the delivered flag. Anything else stops playout and goes to PAUSE as now. After 3 backchannel overlaps, switch to short chunks with pauses (the R238 profile). Backchannel overlaps don't count toward the R152 barge-in signal. Add a high-backchannel stratum with per-group completion and replay bounds as release blockers.

## A7
Winner: Designer
Why: The "you first" move the attack says is missing already exists: R108 yields into PAUSE with "Sorry, go ahead", and PAUSE is an internal transition that doesn't spend the clarify budget. A truncated "So what about—" ends on a dangling word, so R25's incomplete() holds the turn open for 2-3 s and the caller's restart joins the same turn instead of being labeled unclear. Ordinary replies resume at the current question (R24), and R69 budgets bound any loop.
Worth adding: Deterministic backoff on repeated collisions (a longer silent window after each yield) and a per-call collision-rate drift metric.

## A8
Winner: Designer
Why: R14 says AWAIT_* states are entered only when the question finishes playing, and an affirmation overlapping agent speech is a backchannel with no event. R25 excludes overlapped text and R106 extends that window by path delay, with a closed re-ask in the guard band. A "Yeah" at "home" therefore can't write the ownership slot, and system size comes from the calculator and goes through READ_BACK anyway.
Worth adding: A fragment lint against "A or B" slot and offer questions, and a played_fraction field on slot provenance.

## A9
Winner: Designer
Why: The harm the attack describes, a filler "yeah" being accepted as a commit, is blocked: R144 needs the caller to say "send the contract", R77 rejects conditional and hedged turns, and any re-ask at COMMIT means no same-call close (R239-3). R145 indirect_decline and R289 condition_stated also catch "sounds good, but...". What's left is a couple of seconds of dead air before a soft no is honoured, which is a cost to the call's feel, not a broken safeguard.
Worth adding: A trail-off class (turn-final "but/so/I mean/though" with level or falling prosody ends the turn after about 700 ms) that routes to the indirect_decline question in READ_BACK and COMMIT.

## A10
Winner: Designer
Why: The bit-identical CI test (R64) claims only that speculation can't leak into state. The closed-loop safety claim rests on the audited real-call harm gate, which already includes whatever timing speculation produces. The attack's scenario (speculation off makes the reply 900 ms later) is also largely closed by R301, which releases reply onset at the same fixed per-state bucket whether speculation hit, missed or was off.
Worth adding: Stratify the audited harm measure by speculation mode and reply-gap bucket, and run a small randomized speculation-off holdout arm.
