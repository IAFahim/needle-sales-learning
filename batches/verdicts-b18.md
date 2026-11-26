## A1
Winner: Designer
Why: The harm in the scenario can't happen with the existing design. The commit gate is lexical over final ASR tokens and ignores Needle's output (R87). Conditional answers are excluded (R86), and the caller must say "send the contract" (R144), so a leaked confident affirm on "my wife has to see the paperwork first" only causes a re-ask. Synthetic sets never certify (R2), and the Needle-driven canary with 100% audit (R124) measures the real affirm rate, so a leaked prior shows up as real errors instead of passing on a synthetic score.
Worth adding: The context-only leakage probe (state, tool list and fragment with no caller text must not beat the per-state class prior), plus generation prompted by target event with a balanced mix per state.

## A2
Winner: Designer
Why: Teacher labels never gate a release. Gold labels come from humans listening to audio, with per-group clarification and error bounds (R26). Per-dialect bounds block release (R93), and R131 adds feature-based strata, two auditors and a label-free worst-cluster check, so extra clarifies or misroutes for AAE speakers block release instead of shipping. Dialect transforms are rule-based and keep the source label (R93), and the cited outcomes (dispute re-read, clarify) are not hostile exits.
Worth adding: Measure teacher-vs-human disagreement per dialect stratum each release, and bar teacher labels for any stratum where the disparity is above threshold.

## A3
Winner: Breaker
Why: The existing design names euphemisms as an open item and has no rule for training the oblique tail of sensitive_event. Nothing checks whether the aligned generator refuses or sanitizes these classes. R2 lists sensitive misses under neither tier (Tier A is opt-out, confirm_order, consent and critical slots), so they can fall under model-agreement labels. A sanitized teacher and a student that both call "won't be around for the install" small_talk agree, and that turn is seen only through random-agreement audit. The defense's real closure (sanitization audit, non-refusing writers, passive-ideation lexicon rows, recall-biased threshold) is all new.
Fix needed: Make missed sensitive_event and unlawful_request turns Tier A, with human-audited gold only. Run a sanitization audit per class each release that compares generator refusal rate and explicitness against a human-written oblique set, and block release if it fails. Source oblique examples from consented, crisis-informed human writers. Add passive-ideation and indirect-threat lexicon rows to the deterministic pre-emption, with the scripted sensitive exit, and give sensitive_event a recall-biased per-event threshold in the R189 multi-label GLOBAL pass.

## A4
Winner: Designer
Why: Synthetic noise numbers never certify (R2). Certification runs on live text from the pinned ASR (R26, R68), stratified by channel class (R137), so the real confusion profile is what gets measured, and the canonicalizer is applied the same way in training and certification. A mismatch costs capability (more states stay on fallback), not unmeasured harm.
Worth adding: Ban LLM-written ASR errors. Build noisy text only from TTS through channel simulation, the pinned ASR and the canonicalizer, plus an empirical confusion model fitted on audited real calls (the R128 precedent applied to text).

## A5
Winner: Designer
Why: The attack's key claim, that the new event "certifies only on its own small fresh test set", is false. Bounds are per call over whole audited real traces (R66), on human audio labels (R26), and goodbyes happen on almost every call, so a confused boundary shows up as real errors and blocks the state. Stale labels make it harder to learn the new event, but they can't produce a false certificate. R33 forbids replacing real data, not relabeling it.
Worth adding: A schema-migration step: a label-map spec for each schema version, parent-labeled items marked stale on a split, human relabeling or regeneration, masking of unresolved items, and a build check on the stale fraction.

## A6
Winner: Designer
Why: Tool lists are derived from handlers (R52), and the certificate is keyed on the tool-list hash (R34, R53). It is earned only on Needle-driven real calls under the new list (R124), so mapping "come out to my house" to book_video is an audited error that blocks the state. Inconsistent old supervision degrades learning, but it can't be certified past the gate.
Worth adding: Store (graph version, tool-list hash, description hash, label-map version) on every training item, re-render state context from the current graph at train time, and mask any item that has no verified migration path.

## A7
Winner: Designer
Why: The certificate rests on the hashed weights' behaviour on human-audited real calls (R2, R53), not on re-running training. Those weights sit in immutable retained bundles with bit-identical replay (R67). Training each release on the union of all data (R33, R3) means the generated corpus is kept and added to, not regenerated, so a retired teacher can't break a hotfix.
Worth adding: Content-hash each release's training corpus, with teacher model id and version, prompts, seeds and sampling parameters, into the bundle manifest and WORM archive, and prefer a self-hosted, version-pinned teacher.

## A8
Winner: Breaker
Why: The certification ground truth is the whole safety argument, yet the design nowhere requires event labelers to be blind to the model's label. R26 says only "humans listening to audio". R131's two auditors and agreement measures cover dialect-strata labels, not event labels, and R221's blind rule covers only complaint labels. The lexical commit gate saves the one example given, but pre-filled labels would bias stop, consent and critical-slot labels downward for every Tier A state, and the defense concedes that blind labeling "must be explicit".
Fix needed: Label Tier A gold blind: the UI shows no Needle or teacher label, playback is fixed at 1x, and a random share is double-labeled blind with adjudication. Seed known-answer items and remove labelers who fall below an accuracy floor. Allow pre-fill only for Tier B, and correct those estimates by the bias measured against blind double labels.

## A9
Winner: Designer
Why: R126 already closes this. Tuning and promotion use an exploration sample, and certification uses a fresh confirmatory sample collected after the promotion decision and used once, with family-wise alpha and pre-registered sequential retries. Calibration has its own split (R133), the golden canary is a bit-diff regression test rather than a bound (R68), and continuous audits on fresh traffic plus label-free drift monitors (R33, R132) cover what happens after release.
Worth adding: Log a per-release query budget on the exploration pool, and seal each confirmatory sample by content hash at collection.

## A10
Winner: Designer
Why: The scenario's fix needs no retrain. Stop is the union of the deterministic lexicon and GLOBAL (R66), so adding "unsubscribe me" as a lexicon row can only add stops, and the post-call sweep catches misses before any redial. Sensitive (R19), unlawful (R86) and hardship (R150) events have the same lexicon lanes, and a degraded LOCAL state falls back to deterministic fallback (R132), which is safe rather than uncertified. Slow cadence costs coverage, not safety.
Worth adding: A same-day lexicon hotfix lane that replays all retained gold sets for false-stop rate before compliance sign-off, plus separately trained and hashed GLOBAL and LOCAL weights, so a safety retrain doesn't void LOCAL certificates.
