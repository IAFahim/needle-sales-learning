# Verdicts, batch b03

## A1
Winner: Breaker
Why: The existing certification text (R2) says outright that Needle "runs in shadow on live build-phase calls" and is compared to the big model and a gold sample, and rule-of-three sizes are "computed on those live samples per state". After the first divergence those traces are off-policy, so the whole-trace bound in R66 does not hold for Needle as the driver. R20's "on-policy" means the disclosed agent's calls with the big model as classifier, not Needle driving. R36's A/B handoff lift only suggests some Needle-driven traffic and does not say the bound is computed on it. The Designer's key remedy, "only Needle-driven traces enter the gate", plus a staged ramp, is new.
Fix needed: Treat shadow agreement only as evidence for nominating a state. Whole-trace Tier A/B bounds and rule-of-three counts come only from calls where Needle actually drove the transitions. Promotion runs as a staged ramp: shadow, then a Needle-driven canary cohort with 100% human audit, then a wider cohort. The bound is recomputed at each stage, and any breach sends the state back to deterministic fallback.
Worth adding: Log per call which policy drove each transition, so audited traces can be split cleanly into on-policy and off-policy.

## A2
Winner: Designer
Why: The scenario's harm, a confident wrong affirm at COMMIT, is blocked by existing parts that do not depend on Needle. R87 makes the commit gate lexical over the final ASR tokens. R77 and R81 require a short, direct, narrow-set affirm aimed at the read-back question id. A truly novel utterance therefore cannot commit, whatever label Needle picks. The shared-first-token and post-mask margin problems are real calibration flaws, but in other states they lead to Tier B mislabels that real-traffic certification measures. They do not cause an irreversible failure.
Worth adding: Single reserved token per event name, pre-mask off-schema mass as the OOD score (R19 should say it is read before masking), and full-sequence scoring of each allowed event for the margin.

## A3
Winner: Designer
Why: The release claim rests on per-call, per-severity budgets over whole audited traces (R66), not on thousands of separate per-state claims. Per-state and per-group bounds are release blockers, so every one of them must pass, which makes the release more conservative. Tier A also has sealed holdouts and a post-release shadow window (R3), and continuous audited sampling with rollback (R33, R66) re-tests any state that passed by luck. Retry-until-pass at the per-state level is a genuine weakness, but existing fresh-data and monitoring layers bound it.
Worth adding: Cumulative evidence for retried states (alpha-spending on all data so far, no restart from zero), and certification on a confirmatory sample collected after the promotion decision.

## A4
Winner: Designer
Why: The attack targets held-out synthetic accuracy, which the design explicitly never uses to certify (R2: "Synthetic data trains Needle and finds bugs; it never certifies"). Shortcut learning would show up in the real, audio-labeled gate. The money-word example also fails on structure: stop is decided in the separate GLOBAL pass, which has no objection_price (R34), and is unioned with the deterministic lexicon (R66, R24). Lexicon coverage of "don't bother me again" is not certain, but such a miss is a measured stop-recall error on real calls, not hidden by synthetic scores.
Worth adding: A per-source surface-only artifact probe each release, plus counterfactual minimal pairs (money words + stop, polite non-stop) as a Tier A red-team stratum.

## A5
Winner: Designer
Why: The rise token's safety role is deterministic. R80 excludes affirm with <rise> from the commit set inside the lexical gate that is independent of Needle (R87). A false rise only forces a closed re-ask (R77). A missed rise still needs a short, direct lexical affirm to the read-back question id (R81). Whatever Needle mislearned about the token, commit gating stays safe, and other effects are measured on real audio-labeled traffic (R26, R68).
Worth adding: Ban the big model from writing <rise>. Prosody tokens in training come only from the pinned detector run on real or TTS audio, or else are stripped from Needle's input. Per-dialect false-rise and missed-rise rates should be tracked.

## A6
Winner: Designer
Why: The gate is fresh, human-audited live traffic plus sealed Tier A holdouts (R2, R3, R33), and none of it can be in a training union frozen before it was collected. The golden-audio canary (R68) is a "diff -> block" determinism check, so memorizing it fools nothing. Red-team pass rates are not the certification gate. One real gap remains: R3 replays "frozen human-audited gold sets" while training on "the union of all data", so Tier B gold-set replay may measure memorization. That does not defeat the live-traffic gate.
Worth adding: Content-hash denylist plus a near-duplicate and generator-lineage filter between every eval pool and the training union, enforced by a build check. Fixed red-team items should be reported separately from a fresh, never-trained red-team round each release.

## A7
Winner: Designer
Why: R51 quarantines rare *repeated* n-grams, not every rare form. R93 applies Multi-VALUE dialect transforms to all synthetic data, which keeps dialect features frequent in the training union. The stop lexicon has dialect patterns (R93, R66). Certification gold sets are real audited data, separate from the quarantine path, and per-dialect bounds are release blockers. So starvation would surface as a visible failing bound, not a hidden harm. The attack correctly notes that the filter's criteria are thin, but the existing design does not turn it into a silent disparity.
Worth adding: Require source concentration and label skew before quarantine, track the quarantine rate per dialect stratum with a disparity alarm, and give quarantined real items human review with a return path.

## A8
Winner: Breaker
Why: R26 requires per-group bounds on dialect/accent strata but does not say how a call gets its group label. Label noise biases each per-group estimate toward the pooled rate and can hide exactly the disparity the blocker exists to catch. The Designer's existing points (the per-call bound still holds overall, deletable gold sets in R7, and R46 matched-pair tests, which are about the lending menu and not ASR or labeling error) do not restore the per-group guarantee. Feature-based strata, inter-rater correction and label-free worst-cluster checks are all new.
Fix needed: Define strata by observable linguistic and accent features (a Multi-VALUE feature checklist and L1-accent family), annotated by two trained auditors. Measure inter-rater agreement and use the confusion matrix to correct per-group estimates. Keep labels only on audit records under surrogate IDs, never in CRM, runtime or model inputs, and delete them with the gold item. Add a label-free worst-group check: unsupervised clusters over acoustic and ASR-confidence embeddings, with the worst cluster held to the same bound.

## A9
Winner: Breaker
Why: The existing drift alarms (R33) run on audited samples, and at 1e-5-scale rates with roughly 1% audit they need weeks to months to fire. The post-call DNC sweep (R66) covers 100% of calls but re-runs the same Needle GLOBAL pass plus the lexicon. It prevents redials, but it does not detect a Needle drift that the lexicon also misses, and the in-call harm has already happened (the design's own open item says "missed voice stop caught post-call, not instantly"). Fallback, repair and cancellation rates (R36, R48, R50) exist as metrics but are not wired as Tier A drift triggers. The label-free leading alarms are new.
Fix needed: Run label-free drift monitors on 100% of traffic: per-state event-mix shift, clarify and near-tie rate, pre-mask off-schema mass, lexicon-vs-Needle disagreement rate, out_of_scope cluster growth, and hang-up-after-turn rate, all with CUSUM or sequential tests. Any alarm triggers an immediate 100% audit surge on the affected states. Affected Tier A states revert automatically to deterministic fallback until the surge clears.
Worth adding: Queue every lexicon-vs-Needle stop disagreement for human audit, since it is the cheapest early signal of stop drift.

## A10
Winner: Designer
Why: Error rates are not carried between releases. The certificate is keyed to the weights hash (R3, R53), and each release is re-certified on real, human-audited traffic (R2). False-stop and false-continue are Tier A metrics (R24), so a prior swing in either direction is measured and blocks that release. The lexicon union (R66) keeps under-firing from dropping lexical stops. A fixed clarify margin on a shifting score scale costs accuracy and throughput, and is a tuning gap rather than a hidden safety failure.
Worth adding: A per-release calibration step on a separate real, audited split (temperature scaling plus BBSE/EM prior correction to measured deployment priors), with the calibrated thresholds shipped in the hashed bundle.
