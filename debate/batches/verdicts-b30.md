## A1
Winner: Designer
Why: The design never relies on more teacher data converging. Release is gated only on human-audited real-call bounds (R2), and a state that plateaus stays on deterministic fallback, which costs money but causes no harm. The attack's own example is handled by existing elements: one numeric slot per QUALIFY question (R186), the neutral ownership-change question where any yes leads to NOT_SUITABLE (R208), condition_stated (R289) and critical-slot read-back (R2). All of these are in design.md.
Worth adding: Add a per-state learning-curve check (no audited gain over two data doublings means stop adding data and split the question or keep the fallback), plus soft targets from an offline teacher-assistant model.

## A2
Winner: Designer
Why: The premise that audits fall back to random sampling only is false in the existing design. R132 runs label-free monitors on 100% of traffic, including lexicon-vs-Needle disagreement, hang-up-after-turn and out_of_scope growth, and any alarm triggers an audit surge. Missed rescinds also surface through the revocation and complaint intake (R115, R271), the post-call sweep with the cancel lexicon (R66, R189) and capture-recapture (R257). DAgger keeps an expert, because human audit (R20, R33) and the offline-only big model (R36) both remain.
Worth adding: Relabel retired-state transcripts nightly with the offline big model and a second model family, send their disagreements to the audit queue, and give every call later linked to a rescind or complaint a 100% audit.

## A3
Winner: Designer
Why: Contradictory labels on short answers produce near-ties, and near-ties route to clarify (R53, R77). That fails safe. The high-stakes cases do not depend on Needle's context. A commit needs a lexical affirm bound to the instance-scoped read-back qid (R87, R337) and an action-production phrase (R144), and conditions such as "only if my son's on" are captured when spoken (R289, R243). An accuracy ceiling therefore lowers throughput but does not create harm, and the real-call gate measures it.
Worth adding: Use observation-matched labeling, where the teacher and humans see Needle's exact view and a separate field records the whole-call reading, plus a per-release detector that collapses identical (state, text) pairs with conflicting labels to clarify.

## A4
Winner: Designer
Why: Coverage in the existing design does not come from RLHF paraphrases. Dialect variation comes from rule-based Multi-VALUE transforms (R93), noise from TTS plus the pinned ASR and an empirical confusion model, with LLM-written ASR errors banned (R277), and the core data is real on-policy calls that are never replaced (R20, R33). Synthetic counts never certify (R2), and per-dialect and worst-cluster real bounds block release (R131, R255), so a training-coverage gap shows up as a failed gate rather than shipped harm.
Worth adding: Measure coverage as the nearest-neighbour distance from real build-phase turns to the training set, broken out by length and token shape, and seed generation for uncovered regions with real fragments.

## A5
Winner: Designer
Why: The attack's chain from spoken entity to wrong tariff row does not exist. Calculator rows are keyed by delivery utility, generation provider and tariff_class, which only the utility API or the bill extractor can write (R156, R212, R227). The bill-reconciliation gate must reproduce actual billed amounts or no figure is given (R228). Roof suitability comes from roof data and LIDAR lookups plus a ROOF_FIRST inspection (R79, R230, R71), and utility is a read-back critical slot (R2).
Worth adding: Move entity canonicalization into a deterministic alias resolver (EIA-861 utilities, CCAs, retail providers) filtered to the geocoded territory, where zero or several matches lead to clarify.

## A6
Winner: Designer
Why: The slots that drive pricing and identity are not learned values that Needle passes through. Numbers go through a deterministic normalizer and extractor (R43, R61), spoken amounts only fill coarse routing bands (R72), and savings use verified usage only (R156). The attack's own "two-eighty-seven, two-ninety" example is the R185 two-value clarify case, and identity uses a deterministic challenge-response with a token-set matcher for compound and hyphenated names (R73, R146). Certification on real gold (R2, R7) would expose any remaining skew.
Worth adding: Use shape-preserving surrogates sampled from real verbalization patterns and census name lists, plus a release check comparing slot-shape histograms between real gold and training data.

## A7
Winner: Designer
Why: The premise is wrong, because thresholds are fitted on a real audited calibration split with label-shift correction to live priors (R133), not on synthetic data. Commit does not trust Needle's confidence at all: it is lexical, voicing-gated and action-phrase based, with a safety-mass veto (R87, R104, R144, R190). Further drift under shift is caught by 100% label-free CUSUM monitors on clarify rate, near-tie rate and off-schema mass (R132).
Worth adding: Check selective risk per stratum at the chosen threshold, and add a divergence alarm for clarify rate falling while hang-ups or out_of_scope rise.

## A8
Winner: Designer
Why: R124 already requires that whole-trace bounds and rule-of-three counts come only from calls where Needle drove the transitions, in a canary with 100% human audit. Certification evidence is therefore gathered at Needle's own latency, and the fresh confirmatory sample (R126) is collected after promotion. Timers are fitted on real ASR timestamps and A/B tested (R65), and event-mix drift triggers audit surges (R132).
Worth adding: Tag build-phase turns with the preceding agent gap and down-weight turns after gaps over 700 ms. Compare turn-length and overlap distributions between the build phase and the canary before widening the ramp.

## A9
Winner: Designer
Why: Mislabeled hedges cannot produce a commit, because the commit path is lexical, requires a short direct answer and an action-production phrase, and is independent of Needle's label (R87, R81, R144). A soft deferral mislabeled as stop is conservative, a business cost and not a harm (R254). Hedges have their own classes, ambiguous_polarity and indirect_decline (R77, R145), and Tier A gold is human-labeled blind (R281).
Worth adding: Relabel generated boundary items blind with a different model family, and block release for any class whose label-noise rate, measured on a blind human sample, is above threshold.

## A10
Winner: Designer
Why: A seed cannot reach production on synthetic scores. Each weights hash is a new certificate (R53) that must pass shadow, a 100% audited Needle-driven canary and a fresh confirmatory sample (R124, R126), and frozen real gold is replayed on every build (R3). The safety tails are largely seed-independent: stop is the union with a deterministic lexicon including dialect patterns (R66, R93, R24), commit is lexical (R87), and dialect matched-pair tests are release blockers (R275).
Worth adding: Train K seeds, select by the worst case over the stress suites, track seed churn on real gold as a release metric, and run GLOBAL as an OR-ensemble of seeds (a monotone superset under R254).
