=== R334
Round 334: I win.

**Attack:** After a side question, the agent jumps back into the loan quote without checking whether the caller's new house address still allows quoting there.
**My defense:** The address change is itself a safety event that rechecks every rule for the new place, and quoting is blocked by a checked rule wherever only lead collection is allowed.
**Judge:** The design never uses that kind of blind jump back, and the address change triggers its own recheck.

=== R335
Round 335: I win.

**Attack:** A silence timer left running after an emergency exit could make the agent ask about sending the agreement.
**My defense:** Silence arrives as an event handled by whatever step the call is in now, and emergency exits can only play their own fixed, no sales lines.
**Judge:** The design does not keep loose timers, so the leftover prompt cannot fire inside an exit.

=== R336
Round 336: Breaker wins.

**Attack:** When a caller fits two outcomes at once, such as an old roof and a planned move, the order of arrows in a drawing decides between the sales path and the honest exit.
**My defense:** The suitability decision comes from one compliance owned table, not from competing arrows in the drawing.
**Judge:** Nothing in the design says which outcome wins when several table rows match, or checks that choices never overlap.
**Fix:** Rank suitability outcomes so the most cautious one always wins, and fail the build if any choice point has overlapping conditions.

=== R337
Round 337: I win.

**Attack:** A yes meant for the first, rejected offer could send a contract for the second offer, because both read backs share one question label.
**My defense:** A commit only counts for the exact offer read back in full right before the yes, and an independent check refuses any contract without that match.
**Judge:** The commit is already tied to the offer's content, and the interrupted read back leaves nothing to agree to.

=== R338
Round 338: I win.

**Attack:** Counters that reset each time a step is reentered let a caller be stuck hearing the price for forty minutes.
**My defense:** The call also counts total turns, repeat visits, backtracks and elapsed time, and any of them ends the call.
**Judge:** The elapsed time and visit limits catch the loop no matter how a single counter behaves.

=== R339
Round 339: I win.

**Attack:** A question asked while the agent is confirming an opt out could send the call back into the sales pitch.
**My defense:** No pitch after a decline is a checked rule over the whole call, and a stop records the opt out first and then hangs up.
**Judge:** A return to selling after a stop would fail that rule, and any transfer is marked as service only.

=== R340
Round 340: I win.

**Attack:** After the contract step is split and renamed, old safety checks still pass because they name a step that no longer exists.
**My defense:** An independent check at the send stage refuses any contract unless the same offer was fully read back, whatever the steps are called.
**Judge:** That final check does not depend on step names, so the shortcut is blocked where it matters.

=== R341
Round 341: I win.

**Attack:** New roof types added to the policy table fall through a catch all branch straight to quoting.
**My defense:** The suitability outcome comes from the table itself, and changing the table forces every affected step to be certified again.
**Judge:** New roof rows carry their own outcome in the table, so nothing falls through to sales.

=== R342
Round 342: I win.

**Attack:** A reminder text tied to leaving the signing step could go out right after the customer cancels.
**My defense:** Every text passes a consent and opt out gate before it is sent, and the opt out is recorded first in the same turn.
**Judge:** The gates at the send stage stop the reminder even if it gets queued.

=== R343
Round 343: I win.

**Attack:** The checker ignores clock time, so a call started just before the evening cutoff could run past it and send a text late.
**My defense:** Time limits are enforced by running code, with a call length cap and a dialing window that leaves a safety margin.
**Judge:** The rules limit starting calls at night, and the runtime limits cover the rest.
