## A1
Winner: Designer
Why: The scenario assumes GLOBAL is an argmax with a stop-vs-acknowledge tie, but R189 (in design.md) made GLOBAL multi-label with a per-event calibrated threshold, and acknowledge is not a GLOBAL event, so no stop tie exists there. R133 sets those thresholds against a target false-continue rate, which is already the cost-weighted rule the attack asks for, and R145 indirect_decline, R190's safety-mass veto, R66 sweep and R169 lock back it up.
Worth adding: The stop-suspect band (sub-threshold stop mass goes to the R24 check question, never a generic "say that again") and the "quit" family in Tier 1, expanded through the R277 confusion model.

## A2
Winner: Designer
Why: R20 certifies on the agent's own on-policy calls and R277 fits its confusion model on real audited calls, so post-clarify speech is in the measured data, not assumed away. A failed second try lands in R111/R121 access routing (DTMF, text/web, human) with per-group fallback rates as release blockers, which is a safe, bounded outcome rather than a harm.
Worth adding: A post-clarify certification stratum with per-group bounds, and offering DTMF in the same breath on numeric re-asks.

## A3
Winner: Breaker
Why: R15's vulnerability counter counts unclear()/clarify events, and R111 only excludes unintelligible, low-ASR-confidence and pure-ASR-quality unclear events; a Needle margin near-tie on clean AAE audio is none of those, so model ignorance still drives a lucid caller to NO_SALE_SAFE_EXIT with redial suppressed. Per-group false-vulnerability blockers (R111) and R275 matched pairs catch this only in aggregate at release, and the defense itself names the near-tie gap; the CRM-flag part of the attack is wrong (R203), but the per-call conflation stands.
Fix needed: The vulnerability counter takes only caller-content signals (confused(), contradictions between committed slots, wrong_party_reference, R152 overcommitment). Margin near-ties, OOD-floor unclear and grounding misses go to a separate model_uncertainty counter that routes to a human or ACCESS_PATH as an access failure, never to NO_SALE_SAFE_EXIT, never suppresses redial and never disables speculation as a "confusion" signal.

## A4
Winner: Designer
Why: The live monitors are not only self-reported confidence: R132 runs CUSUM on event-mix shift, lexicon-vs-Needle disagreement and hang-up-after-turn rate with audit surges, and a release-induced overconfidence on fifty/fifteen must first pass R3 human-audited gold replay, sealed holdouts and the R133 calibration split, plus R26 digit-wise confirmation of Tier A numbers. Confident errors are caught by label-based pre-release gates and continuous audited sampling, not by clarify rates.
Worth adding: A per-state "high-confidence decision later contradicted" rate (read-back corrections, dispute_prior_statement, role-binding disagreement) and an explicit audit surge on any post-release drop in clarify or near-tie rate.

## A5
Winner: Breaker
Why: R133 re-sets thresholds per release and R273 logs the threshold version, but nothing in design.md puts the gate thresholds into the content-hashed bundle or certificate key: R53/R3 key on weights, runtime, hardware and facts table, and R328 covers only alarm thresholds. A runtime config change therefore leaves the certificate valid while moving the operating point it was measured at; logging detects it later, it does not prevent it.
Fix needed: Make every gate parameter (margin, softmax/OOD floor, ASR and word-confidence floors, veto threshold, vulnerability counts, call budgets, endpointing timers) a compile-time constant in the generated C, included in the bundle hash and certificate key, with no runtime config path and a build check that fails if any guard reads a non-hashed value.

## A6
Winner: Designer
Why: A garbled "can't" can mis-set a budget slot, but R72 keeps spoken amounts in coarse routing bands only, R2 reads back every qualification-critical slot before a transition depends on it, and binding terms come only from the price table, verified usage and READ_BACK plus the R144 action-production commit. So one misheard pivotal word becomes a caught correction or a band misroute, not a contract harm.
Worth adding: A word-level confidence floor on pivotal tokens (digits, negations, modals) with n-best polarity disagreement forcing a contrastive clarify, plus a can/can't, fifteen/fifty minimal-pair audio stratum.

## A7
Winner: Breaker
Why: R169 and R121 stop the loop only for unintelligible fallback; a near-tie clarify-then-fallback in QUALIFY can still end in a booked callback by the same bundle, and nothing in design.md records per lead which state failed or bars the AI from re-entering it. Frequency caps (R41) and the R284 hostility exit only end the loop after the caller has been called repeatedly and angered, which is the harm.
Fix needed: Write a lead-level failed_state record (state id plus bundle hash) on any clarify-then-fallback; the R138 dial permit refuses any AI redial that would re-enter that state under the same or an equivalent bundle, so follow-up is only a human, DTMF/SMS self-serve or a written proposal, and the fallback fragment says plainly that a person will follow up.

## A8
Winner: Breaker
Why: R186 does stop the specific "six years" misbinding, but the existing slot model has no caller-unknown value: after "no idea" the design can only clarify for a number, so the caller's guess is stored as a crisp value with "spoken" provenance or the call falls to fallback. The UNKNOWN handling the defense cites (R159, R227, R319, R341) covers other slots and table enums, not QUALIFY answers, and R211 permit cross-checks only help where a record exists.
Fix needed: Add a dont_know(slot) event and an UNKNOWN value for every QUALIFY slot, a caller_estimate provenance for hedged answers, and mandatory suitability-table rows for UNKNOWN and near-cutoff estimates that resolve via permit/aerial records to ROOF_FIRST or NOT_SUITABLE (build check enforces the rows); no clarify asks for a number after the caller says they don't know.

## A9
Winner: Designer
Why: Ambiguity is not left to the margin alone: R77 trains an explicit audio-informed ambiguous_polarity class mapped to clarify, R133 calibrates on a real audited split, and an utterance like "I guess it makes sense" cannot commit anyway because R144 requires an action-production phrase and the COMMIT gate takes only a short lexical affirm. The overconfident hard-label harm the attack describes has no commit path.
Worth adding: Soft-label targets from two-auditor disagreement and K-teacher sampling, with calibration error on high-disagreement items as a per-state release metric.

## A10
Winner: Designer
Why: The scenario's harm cannot occur: R72 confines spoken amounts to coarse routing bands and R156 makes the utility API or bill extractor the only writer for verified_usage, so savings and size are never computed from a caller-confirmed $250. R239's safe-option re-asks and echo filter, R26/R22 digit-wise confirmation and R273's n-best decision record limit both the acceptance bias and the blame-the-customer audit trail.
Worth adding: A separate agent_echo_confirmed provenance and contrastive n-best confirmation ("one-fifty, two-fifty, or something else?") instead of single-value echoes.
