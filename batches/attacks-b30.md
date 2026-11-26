## A1
TOPIC: Teacher-student capacity gap: a frontier teacher is the wrong teacher for a 26M student, and hard event labels throw away what little it could pass on
SCENARIO: The build phase labels every turn with the big model's single top event. Needle is finetuned on those one-hot labels. On QUALIFY turns like "we might be moving, depends on my wife's job", the teacher's decision rests on discourse reasoning a 26M encoder cannot represent. Needle fits the label surface instead ("moving" -> move_horizon slot). Adding more teacher data and a stronger teacher in later releases does not lift Needle's accuracy on these turns; it plateaus or drops.
WHY IT BREAKS: Distillation degrades when the teacher-student gap is too large: a bigger, more accurate teacher can produce a worse small student (Cho & Hariharan, ICCV 2019; Mirzadeh et al., "Teacher Assistant" KD, AAAI 2020). The plan has no intermediate teacher and no soft targets, and it assumes "more big-model data" converges. Needle's ceiling is set by its capacity, not by data volume.

## A2
TOPIC: Retiring the big model deletes the second opinion that drives audit sampling and DAgger, so post-retirement audits are random-only and lose almost all detection power
SCENARIO: Before retirement, the audit pulls "all disagreements" between Needle (shadow) and the big-model stand-in, plus random agreements. Most harms surface as disagreements. State QUOTE retires. Now only Needle labels the turn, so no disagreements exist. Audit falls back to random sampling at a fixed budget. A new failure mode (a rescind phrasing after a tariff headline) appears at 1 in 20,000 calls; random sampling of a few hundred calls a week effectively never draws it.
WHY IT BREAKS: Disagreement-triggered review is the design's main way to find errors cheaply. It needs a second classifier, which retirement removes by definition. DAgger also requires an expert to label the learner's new states (Ross et al., AISTATS 2011). After retirement there is none, so the "measure, then fix" loop runs blind just when the model is alone.

## A3
TOPIC: Privileged-information teacher: the big model labels turns using whole-call context that Needle never sees, so identical Needle inputs carry contradictory labels
SCENARIO: In the build phase the stand-in classifier sees the full transcript. "Yeah, that's fine" is labeled affirm after a price read-back where the caller asked for it, acknowledge after a long monologue, and request_human where the caller earlier said "only if my son's on". Needle's input is the current turn plus state tools only. Training sees the same (state, text) pair with three labels and learns the average, a near-tie, which then clarifies or flips depending on the release.
WHY IT BREAKS: Imitating an expert that acts on information the learner cannot observe causes an "imitation gap" that more data cannot close (Weihs et al., NeurIPS 2021, "Bridging the Imitation Gap"). This is not a cross-turn runtime bug. The training targets themselves are inconsistent for Needle's observation space, which caps attainable accuracy on exactly the high-stakes short answers.

## A4
TOPIC: RLHF-tuned generators collapse paraphrase diversity, so synthetic "coverage" is dense around fluent typical phrasings and empty where real callers talk
SCENARIO: The big model is asked for 5,000 paraphrases of "not interested" with noise and dialect transforms. Outputs cluster: "I'm not really interested right now", "No thanks, I'm all set", polite, complete sentences. Real callers say "nah, we good", "uh-uh", "ain't doin' that", or a sigh plus "what". Coverage dashboards show thousands of examples per branch. The real mass sits in short, ungrammatical fragments, the region with the fewest training points.
WHY IT BREAKS: RLHF measurably reduces the output diversity of LLMs compared with supervised models (Kirk et al., ICLR 2024). Asking for more samples gives more of the same modes, not new regions. "Covers every branch" counts examples per label, not how much of the input space the examples span.

## A5
TOPIC: A 26M model cannot hold the domain's entity knowledge (utilities, CCAs, co-ops, roof materials, lenders), and the grounding gate checks only that a string was said, not that it maps to the right key
SCENARIO: QUALIFY asks "who's your electric company?" The caller says "Oncor, well, TXU bills me." Needle sets utility=TXU (a retailer, not the wires utility). Another caller says "the co-op", "MCE", or "it's a TPO roof". Needle snaps each to the nearest seen entity or roof type. Each value appears in the ASR text, so grounding passes. Wrong tariff and suitability rows are chosen deterministically from there.
WHY IT BREAKS: The U.S. has roughly 3,000 electric utilities plus retail providers and CCAs (EIA). Memorizing that mapping and its aliases is world knowledge, which scales with parameters. A 26M model has little room for it. Presence-in-text grounding validates the span, not the canonical key, so confident mis-mapping passes every gate.

## A6
TOPIC: PII scrubbing of seed transcripts deletes the very spans Needle must learn to extract as slots, and LLM-filled surrogates don't look like real ones
SCENARIO: Seed calls are scrubbed: names, addresses, dollar amounts, bill figures and dates become [NAME], [ADDR], [AMOUNT], or big-model surrogates ("John Smith", "$150", "123 Main St"). Needle learns slot extraction on round numbers, Anglo names and tidy formats. Live, a caller says "bill's like two-eighty-seven, two-ninety in summer" or gives a hyphenated surname. Needle extracts "two-ninety" for the bill, or nothing, at rates the synthetic eval never showed.
WHY IT BREAKS: Scrubbing is applied to exactly the label-bearing spans, so the real distribution of slot values never reaches training. Generated surrogates follow the generator's priors (common names, round values), not the callers'. It is a train/serve skew created by the privacy step, and it hits the slots that drive pricing and identity.

## A7
TOPIC: Margin and softmax thresholds are tuned on synthetic held-out data, and a small model's calibration collapses under shift, so "clarify" fires least where Needle is most wrong
SCENARIO: Per state, the clarify margin is set to give 3% clarifies at 99.9% accuracy on held-out synthetic turns. On real calls (terse, noisy, novel phrasings), Needle stays confident: margins are wide on wrong labels. The clarify rate on real traffic is lower than on synthetic data while the error rate is several times higher. The deterministic gates trust a confidence signal whose meaning changed when the inputs moved.
WHY IT BREAKS: Calibration measured in-distribution does not survive dataset shift. Ovadia et al. (NeurIPS 2019) show that calibration from post-hoc methods like temperature scaling degrades sharply under shift, and confidence stays high on wrong predictions. Every uncertainty gate in the design inherits thresholds fitted to the wrong distribution.

## A8
TOPIC: The build-phase data captures callers adapting to big-model latency, a conversational rhythm that disappears once fast Needle runs
SCENARIO: During the build phase, the live stand-in classifier adds 700-1500 ms per turn. Callers adapt: "hello?", repeating themselves, talking over the gap, shorter answers. DAgger data and the shadow labels are full of these patterns. After retirement Needle answers in about 100 ms with pre-rendered audio. Callers now produce longer, more complex turns and different turn-taking. The state-by-state certification evidence was gathered on a different conversation.
WHY IT BREAKS: A response gap of about 700 ms or more is perceived as a problem and changes what people say next (Roberts et al., on silence after requests; turn-taking norms around 200 ms, Stivers et al., PNAS 2009). The teacher's latency shaped the training distribution. Removing it is a deployment-time covariate shift that the build data cannot represent.

## A9
TOPIC: Label-by-construction: generated hard cases drift off the event they were requested for, and synthetic data underperforms most on subjective boundaries like affirm vs acknowledge vs unclear
SCENARIO: The generator is asked for "ambiguous-but-still-affirm" commits and "soft stop" requests. It writes "Sure, I guess we could look at it" tagged affirm and "I'm kinda busy, maybe not" tagged stop, labels taken from the prompt, not from a reading of the output. Many such outputs are really hedges. Needle learns that hedges are commits and that vague deferrals are opt-outs. No human reads the millions of boundary items.
WHY IT BREAKS: Li et al. (EMNLP 2023, "Synthetic Data Generation with LLMs for Text Classification") find that synthetic training data helps least, and hurts most, on high-subjectivity tasks. Labeling by request puts the noisiest labels exactly on the decision boundaries the safety gates depend on.

## A10
TOPIC: Underspecification: training runs with equal offline scores behave differently on real callers, so which weights enter real-call audit is a coin flip the synthetic suite can't call
SCENARIO: Each release retrains on the union of all data. Five seeds score the same on synthetic branch suites and red-team sets. One seed misses "take me off" phrasings in one dialect 4x more often. Another flips 2% of near-tie commit turns. Engineering picks seed 3 by the suite. Real-call audit then needs months of traffic to separate it from seed 5, and the next release is a fresh draw.
WHY IT BREAKS: D'Amour et al. (JMLR 2022, "Underspecification Presents Challenges for Credibility in Modern ML") show that models with identical held-out performance diverge widely under shift and stress tests. Synthetic evaluation cannot rank them. Rare safety classes, measured at 1e-5, show the most seed-to-seed churn.
