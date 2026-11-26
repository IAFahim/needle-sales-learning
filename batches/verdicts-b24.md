## A1
Winner: Designer
Why: The design never specifies history pseudostates; GLOBAL events are root-handled (R192), and the residence remark is itself a GLOBAL jurisdiction_changed event that re-evaluates guards with unvalidated places added as candidates under most-restrictive-wins (R70, R189 multi-label). R47's lead-gen invariant is model-checked across all profiles, so any return path into a price state under a lead-gen profile would fail the check rather than pass vacuously.
Fix needed:
Worth adding: The lint banning shallow and deep history and forcing re-entry through the parent's guarded entry choice point, so the guarantee is explicit rather than implied.

## A2
Winner: Designer
Why: Silence is a deterministic front-end event delivered to whatever state is current (R65), waits are explicit graph substates with their own timers and a build completeness check (R55), and the mailbox drops stale events by epoch (R193). The attack's mechanism, a free-floating timestamp read by a shared `do` handler, is not how the design models time, and exit states play only scripted no-pitch fragments (R19).
Fix needed:
Worth adding: A build-time fragment-to-state allowlist enforced by the renderer (fail closed), plus timers scoped to (state id, epoch) so leaving the arming state cancels them.

## A3
Winner: Breaker
Why: The design checks invariants over reachable states, not guard determinism: nothing requires outgoing guards at a choice point to be mutually exclusive, and R6 precedence applies to Needle event sets, not to graph guards. R71 says the table yields NOT_SUITABLE or ROOF_FIRST but defines no resolution when several rows match, and R134's diff compares the binary to the (already redrawn) exported graph, so a reordered diagram passes. The defense's closing elements (severity order, SMT exclusivity check, golden suitability regression) are all new.
Fix needed: Give suitability rows a fixed severity order (NOT_SUITABLE > ... > ROOF_FIRST > OK) with the table returning the most severe match, and add a build check (SMT over the abstract guard domain) that outgoing guards at every choice point are pairwise exclusive and jointly exhaustive, so behaviour-order numbers can never decide an outcome; replay a golden suitability suite every release with compliance sign-off on any changed outcome.
Worth adding:

## A4
Winner: Designer
Why: The commit is already bound to content: read-back is bound to the config hash (R23), accept_offer commits only the quote hash read back immediately before the yes (R49), affirms carry the target question id (R58), and the independent outbox monitor refuses CONTRACT_SENT without a playback completion mark for the same quote hash (R134). An interrupted read-back #2 has no completion mark (R39, R14), and "yes, the one you said first" fails the short-direct-affirm check (R81) and routes to the reference resolver (R4).
Fix needed:
Worth adding: Make the read-back question id instance-scoped (hash of quote hash plus nonce) so the binding is visible in the id itself.

## A5
Winner: Designer
Why: R69's budget counters already include total turns, per-state visits, backtracks and wall-clock, so a 40-minute ping-pong hits the wall-clock and visit limits regardless of any per-state clarify counter reset. R49 audits the slot abstraction against live calls and runs random walks over loops.
Fix needed:
Worth adding: A lint that budget counters are root-owned and monotonic (increment-only), plus an independent runtime wall-clock watchdog outside StateSmith.

## A6
Winner: Designer
Why: "No pitch after decline" is already a whole-graph model-checked invariant (R21), Tier 1 stops end immediately (R24), the DTMF and leave-taking paths are confirm-then-hang-up (R75, R164), and R189 orders the DNC write first and makes any transfer service-only with the DNC flag. A return to QUOTE after a stop would break R21 on the checked relation (R134).
Fix needed:
Worth adding: Put terminal exits in a region that does not inherit root GLOBAL sales handlers and state the invariant over the DNC flag rather than state names.

## A7
Winner: Designer
Why: The decisive safeguard is not a name-based property: R134's independent outbox monitor refuses any commit effect unless the committed trace holds a read-back completion mark for the same quote hash, so a fast path to COMMIT_LOAN is blocked at the outbox. Tool lists are derived from handlers (R52) and new states start uncertified on fallback (R3).
Fix needed:
Worth adding: Turn on vacuity checking (every antecedent needs a reachability witness) and write properties over derived predicates such as "state exposes a commit-class tool".

## A8
Winner: Designer
Why: Under R71 the suitability decision is an outcome produced by the compliance-owned table, not a graph switch on roof material, so a new SLATE or WOOD_SHAKE row carries its own outcome. Certificates are keyed on the facts-table version and must be re-earned by gold replay (R3), and R140 drops QUOTE/READ_BACK to fallback when a bundle is not compatible with the current table.
Fix needed:
Worth adding: A build and runtime exhaustiveness check over every table-owned enum, with unknown values going fail-closed to human review, and a lint banning sales-forward `else` defaults at policy choice points.

## A9
Winner: Designer
Why: Effects are only outbox intents drained on committed turns (R13), and the drain is gated: consent gate on every SMS (R149), DNC write ordered before cancel in the same turn (R189), SMS guards and budgets (R122, R196), and the cancel saga plus envelope void (R216, R173). A reminder intent from an exit action meets a revoked contact at the drain.
Fix needed:
Worth adding: A lint banning effect intents in entry and exit actions, and a drain that re-reads the revocation ledger at send time and drops sales-purpose intents in any stop or cancel turn.

## A10
Winner: Designer
Why: Time limits are enforced by runtime code rather than claimed by the untimed proof: wall-clock budget to WRAP_UP (R69), immediate stop handling (R24), per-call preamble deadline and abandonment counter (R109, R142), and a dial gate with pinned tzdata, authenticated time and a guard band (R139). The hours rules govern initiating solicitations, so continuing a lawfully started call is not the violation the attack claims, and later SMS go through their own outbox guards.
Fix needed:
Worth adding: Have the dial permit refuse a dial when the remaining lawful window (most restrictive zone, Florida's 8 pm included) is shorter than the maximum call budget, and have the outbox refuse sales SMS after that deadline.
