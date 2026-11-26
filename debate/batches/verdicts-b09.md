# Verdicts, batch b09

Note on citations: several of the Designer's R numbers are off by a few. The content does exist in design.md under other numbers: action-production prompt = R144, binary transition-relation enumeration and trace monitor = R134, webhook-as-hint and monotonic status = R136, single reserved event tokens = R125, calibration = R133, equivalence re-keying = R135, admission control = R142, stop-adjacent tokens = R108, render log with wording id = R116, leading-question lint = R151, overcommitment signals = R152. I judged on the content.

## A1
Winner: Breaker
Why: The commit example is blocked by existing parts: R87 makes the commit gate lexical, R144 asks for the action phrase "send the contract", and R77 sends hedged answers to a re-ask. But the attack is about the certificate and replay claims. R53 keys the certificate on weights, kernel build and hardware, and promises cross-node bit-identical replay. R135 re-keys runtimes on bitwise-identical margin decisions. Nothing in the design pins batch composition or uses batch-invariant kernels, so those reproducibility claims, the daily canary and the equivalence re-keying are not guaranteed under production co-batching. The Designer concedes this, and the remedy is entirely new.
Fix needed: Run certified inference with batch-invariant kernels (fixed reduction order and split sizes), or at batch size 1 per pass. Put the batching policy in the certificate key. Add a release CI test that replays every gold set under random co-batched load at sizes 1..N and requires bitwise-identical tokens and margin decisions.
Worth adding: Log the batch size per Needle call so any production/replay divergence can be traced.

## A2
Winner: Designer
Why: R61 does not describe a substring search. It requires the value to be "found by deterministic extractor in the turn's final ASR span", and R43's normalizer produces whole numeric entities with unit and period tags. A fragment such as "5" from "15", or "150" applied to the summer period, therefore does not match. Existing layers also limit the damage: spoken bills only set coarse bands (R72), sizing and savings use only verified usage (R61/R72), roof age goes through critical-slot read-back (R2), and addresses are postal-validated with the house number confirmed digit by digit (R22).
Worth adding: State in R61 that grounding means exact equality with one complete extracted entity at token boundaries. Two candidate values for one slot go to clarify(slot), and argument truncation counts as an error.

## A3
Winner: Designer
Why: R2's critical-slot read-back names roof age, and R71 makes move horizon a qualification slot. A swapped pair is read back ("roof about twenty, staying about eight") before suitability uses it. R44 adds a summary read-back after multi-fact turns, and R52's correct_fact sends a correction back through the flow. Harm needs both a binding error and a caller who confirms the wrong read-back, which is the two-error structure R2 was built for.
Worth adding: A deterministic negation-scope and slot-cue cross-check in the extractor, and one numeric slot per QUALIFY question.

## A4
Winner: Designer
Why: Certification counts only real calls (R2), so it measures the constrained decoder as deployed, distortions included. The premise that it is certified on unconstrained data is wrong. R125 already makes each event name a single reserved token. A forced "25" for "250" is not an extracted entity, so R61 sends the turn to clarify, and bills only set bands (R72). The remaining effect is a higher clarify rate, which costs availability but causes no harm.
Worth adding: Compile argument masks at token level over the tokenizer vocabulary. Use reserved single tokens for argument enums (e.g. battery vs battery_backup). Decode fine-tuning data through the same grammar.

## A5
Winner: Designer
Why: The example commit fails existing gates that never see Needle's input. R81 requires a short direct answer turn, R86 excludes conditional affirms, and R87 checks the full final ASR tokens lexically. Long turns already go through R44's segmenter, are handled per segment, and form their own Tier A stratum. GLOBAL's fixed ~8-tool list (R34) keeps the safety pass short. Nowhere does the design state an explicit window-fit check, but the harmful paths in the attack are already gated.
Worth adding: A build check that tool-schema tokens plus the maximum segment fit the encoder window in every state, with silent truncation disabled and over-length input routed to re-segmentation and then clarify.

## A6
Winner: Breaker
Why: R63 constrains decoding to exactly one call, and the final plan repeats that for GLOBAL. So a bundled turn can only keep one safety intent. DNC is partly covered by the lexicon union (R66) and the post-call sweep before any redial. However, R24's Tier 1 list ("don't call", "take me off"...) does not clearly match "put me on your do-not-call list". R108's stop-adjacent check applies only to overlap residue during agent playback, and R44's segmenter covers long turns only. The cancel case has no backstop at all: cancel_or_rescind is a Needle-only GLOBAL event with no lexicon (R76), and the post-call sweep checks only DNC. "Cancel it, and who am I even talking to?" therefore loses the cancel by construction.
Fix needed: Make GLOBAL multi-label: each safety event gets its own calibrated threshold and every event above it fires, handled in a fixed order (DNC write, then cancel, then identity/human answers; any transfer carries the DNC flag and is service-only). Add a cancel/rescind lexicon to the deterministic union, and extend the post-call sweep to cancel intents. Add "do-not-call" and "do not call list" to Tier 1, plus a bundled-intent Tier A stratum.

## A7
Winner: Designer
Why: The example caller cannot commit under existing rules: "yes, but..." is excluded by R86, R144 requires the phrase "send the contract" rather than "yes", and R87's gate is lexical and short-answer only (R81). R133 calibrates both passes to target false-commit rates, and R152's overcommitment signals block a same-call close. A caller who says only "send the contract" is unlikely to carry heavy request_human mass. The lack of a formal joint rule is a refinement, not an open path to harm.
Worth adding: A joint safety-mass veto: in commit-capable states, any calibrated GLOBAL safety probability above a low threshold blocks commit and triggers one closed question about that event.

## A8
Winner: Designer
Why: The premise fails on the design itself. Needle maps "one utterance + the current state's tool schema" (Runtime section), and affirm/deny carry the target question id deterministically (R58), so the agent's wording is not part of Needle's input. "No, go ahead" cannot commit anyway: R144's action phrase, R87's lexical gate, R77's ambiguous_polarity re-ask and R38's no-answer-words rule all stop it. R59 chooses wordings deterministically and logs them, so production traffic has the same wording mix as the certified traffic. R116's render log records the wording id, so per-wording rates can already be measured.
Worth adding: For fragments that come before AWAIT_* states, key the certificate on (fragment id, wording id), so a new wording starts uncertified. Add a lint that bans compound questions in AWAIT fragments.

## A9
Winner: Designer
Why: The final plan states "GLOBAL exits from any state" as a model-checked invariant over the exported graph. The attack's claim that this checks only whether a root edge exists is an assumption, not a fact stated in the design. R134 already enumerates the compiled binary's effective (state, event) relation, which follows child-first resolution, so a shadowed pair would appear in the artifact the checker uses. R60 already gives envelope help its own events (help_with_screen: resend/wait/callback), so the design never needed to reuse cancel_or_rescind locally. The risk is real enough that the check should be spelled out.
Worth adding: An explicit per-pair invariant that, for every state and every GLOBAL event, the effective handler on the enumerated binary relation is the root exit. Add a lint that fails the build if any substate declares a trigger named in the GLOBAL set.

## A10
Winner: Breaker
Why: The existing parts serialize effects and harden webhooks. R13 only lets effects leave through the outbox on committed turns. R136 treats a webhook as a wake-up hint with pulled, monotonic status. R134's trace monitor guards commit effects. None of these says who calls dispatch() or from which thread. StateSmith generates plain dispatch code with no queue or re-entrancy protection, so Needle results, webhooks, WAITING_FOR timers (R55) and telephony events (R35) can interleave on the current-state variable and the slot store, outside anything the graph checker verifies. The Designer concedes the "glue re-entrancy" gap, and the fix is new.
Fix needed: Use a single-writer actor per session. All event sources enqueue into one FIFO mailbox, drained by one thread that calls dispatch() run-to-completion. dispatch asserts non-reentrancy and fails closed. Events carry a session epoch, and stale ones are dropped. Model-check the mailbox glue over all interleavings (e.g. TLA+), and add random-interleaving fault injection that must yield only legal traces.
