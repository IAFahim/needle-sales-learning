=== R124
Round 124: Breaker wins.

**Attack:** Shadow testing cannot show whole call harm because the real call follows the big model after any difference.
**My defense:** Release uses the agent's own calls, not shadow logs.
**Judge:** Shadow traces go off policy after the first difference, so the whole call bound was not measured.
**Fix:** Use shadow agreement only to pick candidates, and take bounds only from calls Needle actually drove, with a staged ramp.

=== R125
Round 125: I win.

**Attack:** The model's confidence hides how much probability fell outside the allowed choices.
**My defense:** The commit gate is plain word matching that does not depend on that confidence.
**Judge:** Several other layers make that confidence irrelevant at the commit.

=== R126
Round 126: I win.

**Attack:** Hundreds of separate bounds mean some bad states will pass by luck.
**My defense:** The claim rests on one whole call budget, and every bound must pass.
**Judge:** Needing every bound to pass makes release stricter, not looser.

=== R127
Round 127: I win.

**Attack:** Training data from the big model may carry style tells the model learns instead of intent.
**My defense:** Synthetic data never certifies anything, only real audited calls do.
**Judge:** Real audited calls would expose any such shortcut.

=== R128
Round 128: I win.

**Attack:** Invented rise tokens in training data differ from what the real detector produces.
**My defense:** The rise rule is plain code, independent of what Needle learned.
**Judge:** A wrong rise only forces a simple re ask, so it fails safe.

=== R129
Round 129: I win.

**Attack:** Retraining on everything could leak test items and canaries into training.
**My defense:** The release test uses fresh real traffic and sealed holdouts.
**Judge:** Fresh calls cannot be inside data frozen before they happened.

=== R130
Round 130: I win.

**Attack:** Removing rare phrases may strip out dialect and unusual names.
**My defense:** Only rare repeated patterns are removed, not rare words.
**Judge:** Dialect forms are common across many callers, and dialect transforms keep them in training.

=== R131
Round 131: Breaker wins.

**Attack:** Group tests need a dialect label for every audited call, and that label is shaky and sensitive.
**My defense:** Labels exist only in the audit set and never touch the customer record.
**Judge:** The design never says how groups are labeled, and noisy labels can hide the very gaps it checks for.
**Fix:** Label groups by observable speech features using two trained reviewers, measure their agreement, and correct estimates for it.

=== R132
Round 132: Breaker wins.

**Attack:** Alarms on very rare harms take weeks or months to notice a problem.
**My defense:** Every call gets the do not call sweep.
**Judge:** The sweep reuses the same model pass, so it cannot detect a drop in the model's own quality.
**Fix:** Watch label free signals on all traffic, such as event mix, near ties and hang ups, with fast change detection.

=== R133
Round 133: I win.

**Attack:** Boosting rare safety events shifts the model's priors each release.
**My defense:** Each release is re measured on real audited traffic with its own weights.
**Judge:** Rates are not carried over, so any swing is measured and blocks that release.
