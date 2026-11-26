=== R274
Round 274: I win.

**Attack:** The training data lets the model guess the answer from the state's context alone, so it confidently marks an off-script reply as a yes.
**My defense:** The sale is only committed by a plain word check on what the caller actually said, so a hedge like "my wife has to see the paperwork first" just gets asked again.
**Judge:** The harm can't happen, and real audited calls would expose the leaked guess anyway.

=== R275
Round 275: I win.

**Attack:** The big model quietly treats dialect speakers worse, so the small model learns to mislabel them as unclear or hostile.
**My defense:** Release never trusts the big model's labels; humans listening to audio set the truth, and each dialect has its own bound that blocks release.
**Judge:** A biased teacher would block a release rather than ship, and the cited outcomes are mild re-reads or clarifying questions.

=== R276
Round 276: Breaker wins.

**Attack:** The safety-trained big model refuses or softens realistic suicidal and threatening wording, so the small model only catches explicit phrasing like "I am feeling suicidal."
**My defense:** Real audited calls count a missed sensitive turn as serious harm, and word lists catch obvious cases.
**Judge:** Oblique phrasing was a known open gap, and nothing checked the generator for sanitizing.
**Fix:** Count missed sensitive turns as top-tier harm, audit the generator for sanitizing, use human-written examples, and add indirect phrases to the word lists.

=== R277
Round 277: I win.

**Attack:** Fake speech errors written by the big model don't match the real speech recognizer's mistakes, so the noise tests overstate how well we cope.
**My defense:** Noise numbers from synthetic data never certify anything; certification uses the real pinned recognizer's output, split by channel type.
**Judge:** The real error profile is what gets measured, so a mismatch costs capability, not hidden harm.

=== R278
Round 278: I win.

**Attack:** When a new event is split off, old data still carries the old label and teaches the wrong answer for goodbyes.
**My defense:** Certification is per call on whole real audited calls with human labels, so confused goodbyes show up as real errors and block release.
**Judge:** Stale labels make learning harder but can't produce a false certificate.

=== R279
Round 279: I win.

**Attack:** Training examples aren't tied to the tool graph version they were labeled against, so renamed or split tools mix incompatible labels.
**My defense:** Certificates are keyed to the tool list and earned only on real calls under the new list, so a wrong booking choice is an audited error that blocks the state.
**Judge:** Messy old supervision hurts learning but can't get past the gate.

=== R280
Round 280: I win.

**Attack:** The big model that made the training data can be changed or retired, so a certified build can't be rebuilt.
**My defense:** Certification rests on the exact weights' behavior on real audited calls, and those weights are kept as immutable bundles that replay identically.
**Judge:** A hotfix adds to the kept data instead of regenerating it, so a retired teacher can't break it.

=== R281
Round 281: Breaker wins.

**Attack:** Human labelers see the model's suggested label first, so they tend to accept it and the measured harm looks lower than it is.
**My defense:** The commit check is a plain word match that ignores the model, so a pre-filled yes can't commit a sale by itself.
**Judge:** Nothing required blind labeling, so biased gold would understate harm for stop and consent.
**Fix:** Make top-tier labeling blind, double-label a random share, seed known-answer checks, and allow pre-filled labels only for lower tiers.

=== R282
Round 282: I win.

**Attack:** Engineers keep tuning against the same audited pools every release, so the pools quietly become training data.
**My defense:** Tuning uses an exploration sample, while certification uses a fresh sample collected after the decision and used only once.
**Judge:** That rule already closes the problem, and fresh traffic is audited after release too.

=== R283
Round 283: I win.

**Attack:** Fixing a new stop phrase needs retraining, and new weights void every certificate for months.
**My defense:** Stop is the union of a word list and the model, so adding "unsubscribe me" to the list needs no retrain and can only add stops.
**Judge:** The urgent fix needs no new weights, and a slow cadence costs coverage, not safety.
