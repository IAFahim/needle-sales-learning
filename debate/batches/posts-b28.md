=== R374
Round 374: I win.

**Attack:** When the model is torn between "stop" and "keep going", the agent asks the caller to repeat instead of ending the call.
**My defense:** Safety events are scored one by one, each against its own threshold tuned to keep missed stops rare, so there is no stop tie to break.
**Judge:** The attack pictured a tie that the safety pass cannot produce, and the stop threshold is already set with the cost of a missed stop in mind.

=== R375
Round 375: I win.

**Attack:** People speak slowly and stiffly when asked to repeat, and the speech recognizer handles that worse, so the single retry usually fails.
**My defense:** Every real retry turn from the agent's own calls is in the audited data, and a failed retry goes to keypad, text or a person.
**Judge:** Retry speech is measured on real calls, and a failed retry ends in a safe handoff rather than a harmful mistake.

=== R376
Round 376: Breaker wins.

**Attack:** The model's own confusion on an unfamiliar dialect gets counted as the caller being confused, so a clear thinking caller is ended as vulnerable.
**My defense:** Release fails if any speaker group is wrongly flagged as vulnerable more often than others.
**Judge:** That check works only across many calls, while each individual caller can still be wrongly turned away by the model's uncertainty.
**Fix:** Count only signs about the caller as vulnerability, and send the model's own uncertainty to a person or another way to answer.

=== R377
Round 377: I win.

**Attack:** Live health checks rely on the model's own confidence, so a confidently wrong step looks healthy while a careful one gets shut down.
**My defense:** Live checks also watch shifts in answer patterns, disagreements with the word list and hang ups, and releases must pass human audited test sets first.
**Judge:** Confident errors are caught by human labeled checks before and after release, not by confidence signals alone.

=== R378
Round 378: Breaker wins.

**Attack:** The decision thresholds live outside the signed release, so someone can loosen them without anyone recertifying.
**My defense:** Thresholds are recalibrated each release and the threshold version is logged on every turn.
**Judge:** Logging shows a change after the fact but does not stop it, and the certificate stays valid while the rules it measured have moved.
**Fix:** Build every threshold into the compiled release so it is covered by the signature and cannot be changed at runtime.

=== R379
Round 379: I win.

**Attack:** The recognizer's average confidence can be high while one key word like "can't" was misheard.
**My defense:** Key qualifying answers are read back before anything depends on them, and spoken amounts never set prices or contract terms.
**Judge:** One misheard word becomes a correction or a minor misroute, never a signed contract on wrong terms.

=== R380
Round 380: Breaker wins.

**Attack:** When the agent fails to understand an answer and books a callback, the same agent calls back and fails at the same spot again.
**My defense:** Calls that fail because the caller can't be heard book nothing and go to a person.
**Judge:** That covers only calls where the caller can't be heard, not calls where the model can't decide, and nothing remembers which step failed for that lead.
**Fix:** Record the failed step for each lead and block any automated redial into it, so follow up comes only from a person or a self serve option.

=== R381
Round 381: Breaker wins.

**Attack:** The agent has no way to store "I don't know", so an honest unknown roof age turns into a guessed number treated as fact.
**My defense:** Numbers are checked against what they refer to, and roof age is cross checked against permit records.
**Judge:** Those checks catch misplaced numbers, but a caller who truly doesn't know is still pushed into a guess that looks like a stated fact.
**Fix:** Add an "I don't know" answer and an unknown value for each qualifying question, resolved by records, inspection or an honest exit.

=== R382
Round 382: I win.

**Attack:** Training on single hard labels teaches the model that nothing is ambiguous, so it never pauses on truly unclear answers.
**My defense:** Ambiguous answers have their own trained label, and a vague "I guess" can never close a sale because closing needs a specific spoken phrase.
**Judge:** The harm the attack describes has no route to a signed contract, and ambiguity is learned as a label, not left to scores alone.

=== R383
Round 383: I win.

**Attack:** Callers say "yeah" to a misheard number read back to them, and that wrong number then becomes the customer's confirmed fact.
**My defense:** Spoken amounts only sort calls into rough bands, and savings come only from verified utility data.
**Judge:** A wrongly confirmed bill amount can never drive savings or system size, so the described harm cannot happen.
