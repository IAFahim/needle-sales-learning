=== R194
Round 194: I win.

**Attack:** A rival spoofs caller IDs and passes the identity check with brokered facts to cancel contracts and opt leads out.
**My defense:** A forged opt-out only silences our own calls, and a forged cancel sends written confirmation and a mailed notice, so the real customer finds out.
**Judge:** The harm is visible and fixable, and a customer can re-sign through the normal flow.

=== R195
Round 195: Breaker wins.

**Attack:** Callers can tell a matched identity guess from a wrong one by what the agent says next.
**My defense:** Partial matches go to clarify or a human, and rate limits would flag a surge.
**Judge:** Limits keyed by caller are beaten by rotating numbers, and monitors only notice after the leak starts.
**Fix:** Answer every attempt the same way, unlock personal wording only with a code to the number on file, and count attempts per lead.

=== R196
Round 196: I win.

**Attack:** Fraud rings could pump text message fees by driving bots to request resends and codes again and again.
**My defense:** Texts only go to the dialed number, behind consent and owner checks, so planted numbers never reach the signing stage.
**Judge:** Getting thousands of bots through every gate is not plausible, and a spend cap is extra protection, not a hole.

=== R197
Round 197: Breaker wins.

**Attack:** Someone fills our web form with real victims' phone numbers, so the dialer calls people who never consented.
**My defense:** Consent must come from the subscriber, and an owner match plus per partner suspension stops bulk planting.
**Judge:** A form with a victim's real details passes every check, and nothing proves the subscriber controls the number.
**Fix:** Require a one time code to the number at submission, throttle forms by device, and add a dispute event that blocks the cluster.

=== R198
Round 198: Breaker wins.

**Attack:** An impostor passes the weak identity check, and staff trust the "verified" tag when changing payment details.
**My defense:** The agent itself cannot write contact or payee data, and voice never takes payment.
**Judge:** Tickets and transfers carry no defined payload, so a bare verified tag can lend false authority to the impostor.
**Fix:** Tag handoffs with verification strength, give them no fields for new contact or payee details, and require a code to the old contact plus a delay.

=== R199
Round 199: Breaker wins.

**Attack:** An insider adds a wording that is chosen only for a narrow slice of mostly older callers.
**My defense:** Aggregate and free claims must trace to a policy table key, and every wording is logged and archived by id.
**Judge:** Nothing limits what feeds the wording selector, and random audits would rarely hit a rare trigger.
**Fix:** Let the selector see only a hash, require two person approval, lint vague quantities, and fully audit new wordings.

=== R200
Round 200: I win.

**Attack:** Bribed labelers could mark harmful calls as fine and certify an unsafe state.
**My defense:** The worst harms are blocked structurally by the read back rule, and the drift monitors use no labels at all.
**Judge:** Several independent checks mean one corrupt labeler cannot quietly certify a state, and a whole corrupt vendor is a small leftover risk.

=== R201
Round 201: Breaker wins.

**Attack:** A caller threatens violence against installers, and the call ends politely with nothing kept and nobody told.
**My defense:** Audio and records are already kept in permanent storage, and a pre deletion sweep can read the transcript.
**Judge:** No event covers threats to others, nothing pages a human, and nothing holds the dispatch.
**Fix:** Add a threat event that ends the call, freezes deletion, pages a safety team, and blocks every visit to that address until a human clears it.

=== R202
Round 202: Breaker wins.

**Attack:** Bots flood human requests and book home visits, and one fake owner lures a rep to an address they control.
**My defense:** A full queue falls back to a booking, and rate limits and surge detection contain the flood.
**Judge:** The flood is contained, but a caller passing the knowledge check can still book a real looking address.
**Fix:** Require a code to the number of record for any home visit, cap visits per address, and add a rep safety protocol.

=== R203
Round 203: I win.

**Attack:** Human closers get the full customer record and could poach customers or sell the transfer feed.
**My defense:** The agent only collects coarse facts, and vulnerable callers are routed to a safe exit instead of a closer.
**Judge:** The attack assumes the closer sees everything, which the design never says, and poaching is a general sales risk the agent does not worsen.
