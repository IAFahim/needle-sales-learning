=== R114
Round 114: Breaker wins.

**Attack:** A homeowner on a state do not call list gets dialed because only the national list is checked.
**My defense:** State rules are covered by general hooks.
**Judge:** No step actually checks state lists or their own exemptions.
**Fix:** Add a row for each state list with its own exemption rules, and check every possible state before each dial.

=== R115
Round 115: Breaker wins.

**Attack:** A stop sent by text or email never reaches the dialing system.
**My defense:** Every redial passes a per number check.
**Judge:** Every stop path in the design is voice or keypad, and nothing routes text replies to the ledger.
**Fix:** Build one intake that feeds text, email, web and installer stops into the do not call ledger within a business day.

=== R116
Round 116: I win.

**Attack:** Five year record rules clash with no retain mode and the many possible wordings.
**My defense:** Old versions are kept, so the played message can be rebuilt.
**Judge:** Stored bundle versions and logged wording choices let us recreate exactly what was said.

=== R117
Round 117: Breaker wins.

**Attack:** A caller says a lawyer is recording, yet routine deletion keeps running.
**My defense:** No recording exists in no retain calls, so nothing was lost.
**Judge:** The design has no legal threat event and no hold, so deletion continues once a dispute is foreseeable.
**Fix:** Add a legal threat event that ends the pitch and freezes every deletion for that call and number.

=== R118
Round 118: I win.

**Attack:** Speaker change and echo filters might count as collecting voiceprints under Illinois law.
**My defense:** None of them keep a voice pattern, they only compare words and one pitch token.
**Judge:** The attack's premise is false, since no voice data is stored.

=== R119
Round 119: Breaker wins.

**Attack:** Health clues from medical exits could break Washington's health data law.
**My defense:** These labels are coarse and only route to a safe exit.
**Judge:** Health content stays in retained transcripts, and retention consent is not the separate health opt in.
**Fix:** Strip health details from every kept record and keep only a plain exit label unless the separate consent is given.

=== R120
Round 120: Breaker wins.

**Attack:** A blind customer cannot properly consent to or use the electronic signing.
**My defense:** Binding happens only after a completed signature.
**Judge:** Nothing checks that the customer can access electronic records, and there is no accessible alternative.
**Fix:** Ask first about electronic or paper signing, and route anyone needing paper to a mailed or assisted signing.

=== R121
Round 121: I win.

**Attack:** Callers with speech disabilities could be left with no service.
**My defense:** Fallback goes to a callback or a person who can quote.
**Judge:** The design is not a dead end, since a human can finish the job.

=== R122
Round 122: Breaker wins.

**Attack:** State seller registration and bonding is not checked before dialing.
**My defense:** Per state licensing is already gated.
**Judge:** The licensing row covers salespeople, not telemarketer registration and bonds.
**Fix:** Add a registration row per state with bond and expiry, and block dialing and texting without it.

=== R123
Round 123: Breaker wins.

**Attack:** One spouse can sign for every owner because the code goes to the phone on the call.
**My defense:** The caller cannot dictate another owner's number.
**Judge:** Every owner's code still goes to the one phone on the call, so one person can sign for all.
**Fix:** Source each signer's contact separately, never let two signers share a phone, and require per signer ID checks for liens.
