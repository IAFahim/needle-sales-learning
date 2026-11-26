## A1
TOPIC: Shadow-mode evaluation cannot measure Needle's whole-call harm: after its first divergent label, the real call follows the big model's path
SCENARIO: Build phase: big model drives a live call, Needle runs in shadow. Turn 4: big model labels "objection_price", Needle labels "acknowledge". The real call continues down the big model's branch; Needle's branch (skip rebuttal, move to QUOTE, different read-back timing) never happens. Turns 5-20 are scored for Needle only on inputs produced by the other policy. The team reports Needle's "whole-trace harm" from these shadow logs and certifies states for live use.
WHY IT BREAKS: The design certifies on "whole audited call traces", but shadow traces are off-policy after the first disagreement: callers react to what was actually said, not what Needle would have said. Compounding-error results (Ross et al., DAgger, 2011) show per-step agreement understates on-policy error. The only true trace measurement is putting the uncertified Needle on real callers first.

## A2
TOPIC: Constrained decoding renormalizes probability over allowed events, so the near-tie margin hides how much mass the model put outside the schema
SCENARIO: In COMMIT, the caller says something truly novel. Unconstrained, Needle would spread mass over junk tokens; 85% of its first-token mass is off-schema. Constrained decoding masks those, leaving "affirm" 0.12 vs "unclear" 0.03 among allowed tokens. After renormalizing, affirm is 0.80, unclear 0.20: a wide margin, no clarify. Multi-token event names make it worse: the margin is computed on a shared first token ("stop"/"stop_dnc", "request_human"/"request_caller_identity") before the meaningful token is chosen.
WHY IT BREAKS: Grammar-constrained decoding distorts the model's distribution and gives outputs whose likelihood does not reflect the model (Park et al., "Grammar-Aligned Decoding", NeurIPS 2024). The design's near-tie gate reads confidence after masking, so out-of-distribution inputs look most confident exactly where the schema is narrowest: the commit state.

## A3
TOPIC: Multiple comparisons and winner's curse: hundreds of per-state, per-group, per-tier 95% bounds let bad states certify by chance
SCENARIO: The graph has ~300 states, ~6 dialect strata and 3 severity tiers: ~5,000 separate 95% upper-bound tests per release. The team tunes thresholds and fragments, reruns, and promotes whichever states pass; failing states go to fallback and are retried next release with fresh luck. A state whose true Tier A rate is 3e-5 passes once by sampling luck and is promoted; the release-level claim "every live state is under 1e-5" is published.
WHY IT BREAKS: A 95% bound is wrong 5% of the time per test. Across thousands of tests and repeated retries with selection on passing, false certifications are expected, not rare. With no family-wise or false-discovery correction and no fresh holdout after tuning, the certificate's confidence level is invalid by construction.

## A4
TOPIC: Shortcut learning on generator artifacts: big-model synthetic examples carry label-correlated style tells that Needle learns instead of intent
SCENARIO: The big model writes 200k "stop/DNC" paraphrases. They are polite, complete, often start with "Please" and contain "list" or "call". Its "objection_price" items mention money words. Needle hits 99.9% on held-out synthetic data. A real caller mutters "ugh, don't bother me again, got it?" with none of those tells: labeled "acknowledge". Another says "I'd rather put the money in my 401k, please stop": money word wins, labeled objection_price.
WHY IT BREAKS: Crowd-written NLI data has annotation artifacts so strong a hypothesis-only classifier gets ~67% on SNLI without seeing the premise (Gururangan et al., NAACL 2018). Generator-written data has stronger, more uniform artifacts. Held-out synthetic accuracy measures how well Needle reads the generator's style, not callers.

## A5
TOPIC: Train/serve skew on prosody tokens: synthetic training text carries "final-rise" tokens invented by the big model, not produced by the prosody detector
SCENARIO: The commit gate excludes rising-pitch answers using a final-rise token from the prosody front end. Synthetic transcripts have no audio, so the big model inserts final-rise tokens where it thinks questions are. In production, the detector fires on list intonation, regional uptalk and line noise, and misses flat-pitch questions. Needle learned "final-rise implies question" from clean invented placements; it now ignores the token on uptalk "yes" or over-trusts it on noise, flipping commit gating.
WHY IT BREAKS: A feature that exists only in serving, simulated by guesswork in training, is classic training/serving skew. The token gates the most consequential decision (COMMIT), yet its training distribution was written by the big model, not measured from the pinned detector on real audio. No amount of synthetic volume fixes a mismatched feature distribution.

## A6
TOPIC: Train/test contamination: "finetune on the union of all data each release" absorbs red-team items, regression suites and golden canaries
SCENARIO: Release 7's red-team finds 400 failing attacks; they are labeled and added to the union. The golden-audio canary transcripts, reviewed for a breach last month, were also labeled and added. Release 8 passes 100% of past red-team attacks and the daily canary. The team reads this as robustness. Near-duplicate paraphrases of the canary set also sit in the synthetic pool from the same generator prompts.
WHY IT BREAKS: Once evaluation items or their near-duplicates enter training, those sets measure memorization, not generalization. A 26M model easily memorizes a few thousand items. The design states no frozen, never-trained-on holdout or deduplication between training and test pools, so its regression and canary gates become self-fulfilling and detect nothing new.

## A7
TOPIC: Rare n-gram quarantine (anti-poisoning) systematically removes dialect, code-switched and rare-name data, starving the groups the per-group bounds protect
SCENARIO: The anti-poisoning filter quarantines rare n-grams. Real calls containing "finna", "ion want it" (I don't want it), Spanglish "no, gracias, ya tengo", Gullah or Cajun forms, and uncommon surnames are rare by definition and get quarantined with the true attacks. Each release, minority-dialect real data shrinks relative to synthetic Standard English. Needle's stop recall for those speakers stalls; their states never pass the per-group bound.
WHY IT BREAKS: Rarity is the shared signature of both triggers and minority speech; a frequency filter cannot tell them apart. NLP tools already misread African-American English as non-English (Blodgett et al., EMNLP 2016). The quarantine turns a security control into a disparate-performance generator, and per-group blockers then keep those callers on fallback or exclude them.

## A8
TOPIC: Dialect/accent stratification needs a group label for every audited call, which is itself an unreliable and sensitive inference
SCENARIO: To enforce per-group bounds, each audited call must be assigned a dialect/accent group. Callers don't self-report it. Auditors guess from audio, or an accent classifier does. A Black caller with a Midwestern General American accent is binned "majority"; a Nigerian-English speaker is binned with Caribbean English. Failures land in the wrong strata, diluting the true minority-group error rate below its alarm threshold, while the group label is stored per customer.
WHY IT BREAKS: Group-wise guarantees are only as good as group labels; misclassified membership biases per-group estimates toward the pooled rate and hides disparities. ASR error gaps are large (WER 0.35 vs 0.19 for Black vs white speakers; Koenecke et al., PNAS 2020), so the metric matters, yet inferring ethnicity-linked dialect from voice is itself sensitive data.

## A9
TOPIC: Drift alarms at 1e-5 rates have detection delays of weeks to months, so harm accrues long before audited sampling can notice
SCENARIO: Fleet: 100,000 calls/day; 1% audited (1,000/day). A news story about "solar scam calls" changes how callers refuse; Tier A misses jump tenfold from 1e-5 to 1e-4. Expected audited Tier A events: one every 10 days. A per-state alarm split over many states sees almost nothing. Meanwhile the fleet produces ~10 Tier A harms every day. Detection needs several events per state: months.
WHY IT BREAKS: The detection delay of any sampled-rate monitor scales with 1/(rate x sample size); at 1e-5 rates statistical power is near zero. The design monitors only labeled audited outcomes, with no unlabeled input-distribution drift detection (embedding or event-mix shift) to trigger early. Delayed labels make it slower. Thousands of harms can occur before rollback.

## A10
TOPIC: Label-prior shift: upsampled rare safety events and per-source caps change Needle's class priors each release, silently moving stop and commit error rates
SCENARIO: Real calls contain stop/DNC in ~2% of turns; the training union is rebalanced to 15% to teach it, and per-source caps change the mix again in each release. Needle's implicit prior swings: release 9 over-fires "stop" on "not right now" (false exits), release 10 under-fires after synthetic stop items are capped. The clarify margin, fixed in config, now sits at a different point on each release's score scale.
WHY IT BREAKS: Classifier posteriors depend on training class priors; when they differ from deployment priors, outputs and thresholds are miscalibrated (label-shift literature, e.g., Lipton et al., ICML 2018). The design re-mixes data every release but states no prior correction or per-release threshold recalibration on real traffic, so certified error rates do not carry over.
