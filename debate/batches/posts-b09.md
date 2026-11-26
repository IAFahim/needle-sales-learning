=== R184
Round 184: Breaker wins.

**Attack:** The same call can get a different near-tie decision depending on how many other calls the server batches with it, so replay does not match production.
**My defense:** The commit itself never rests on the model's margin, because a plain word check decides it.
**Judge:** That covers commits, but the replay and certificate claims still assume results that co-batching can change.
**Fix:** Run certified inference with batch-invariant kernels, put the batching policy in the certificate key, and test every gold set under random co-batched load.

=== R185
Round 185: I win.

**Attack:** A check that only looks for the value in the transcript lets fragments through, like "150" found inside "1500".
**My defense:** The check requires a whole extracted number with its unit and period, not a piece of text.
**Judge:** A fragment such as "5" from "15" cannot match a whole entity, and bills and roof age have extra safeguards.

=== R186
Round 186: I win.

**Attack:** The right number can be attached to the wrong role, such as swapping roof age and how long they plan to stay.
**My defense:** Roof age and move horizon are read back to the caller and confirmed before anything uses them.
**Judge:** Harm needs both a binding mistake and a caller who confirms the wrong read-back, and the design was built for that two-error case.

=== R187
Round 187: I win.

**Attack:** Token-level decoding limits may make some valid argument values unreachable or force odd tokenizations.
**My defense:** Certification counts only real calls through the deployed decoder, so any distortion is already measured.
**Judge:** A forced wrong number is not a verified value, so the turn goes to a clarifying question, which costs time but causes no harm.

=== R188
Round 188: I win.

**Attack:** A long caller turn plus the tool list could overflow the input window and silently cut the caller's last words.
**My defense:** Commits use a short-answer check and a word-level gate that never see the truncated input.
**Judge:** The harmful paths in the attack are already gated, so the missing window-fit check is a refinement.

=== R189
Round 189: Breaker wins.

**Attack:** When a caller bundles two safety requests, the one-event rule keeps only one, so "cancel it, and who am I talking to?" loses the cancel.
**My defense:** The do-not-call request is also caught by a word list and a sweep after the call.
**Judge:** Cancel has no word list and no sweep, and the do-not-call phrasing is not clearly covered either.
**Fix:** Let every safety event fire on its own threshold in a fixed order, and add a cancel word list and sweep.

=== R190
Round 190: I win.

**Attack:** A strong but sub-threshold safety signal is discarded while the commit path goes ahead.
**My defense:** A hedged answer like "yes, but" cannot commit, because commits need the exact phrase "send the contract".
**Judge:** The caller has no open path to harm, and the missing joint rule is a refinement.

=== R191
Round 191: I win.

**Attack:** Changing how a question is worded changes what the model sees, but certification is tied to the question, not its wording.
**My defense:** Something like "No, go ahead" cannot commit, because the commit needs the action phrase and a mixed answer triggers a re-ask.
**Judge:** Wording is chosen deterministically and logged, so production matches what was certified.

=== R192
Round 192: I win.

**Attack:** A substate that handles the same event could shadow the root exit for safety requests.
**My defense:** The checker enumerates the compiled machine's real handlers, so a shadowed pair would show up there.
**Judge:** The attack assumes a weak check the design does not describe, though the per-pair rule should be spelled out.

=== R193
Round 193: Breaker wins.

**Attack:** The state machine has no event queue, so model results, webhooks, timers and phone events can interleave on shared state.
**My defense:** Effects only leave through an outbox on committed turns, and webhooks are treated as hints.
**Judge:** Nothing says who calls dispatch or from which thread, so the glue sits outside the model check.
**Fix:** Use one single-writer mailbox per session, fail closed on re-entry, drop stale events, and model-check the interleavings.
