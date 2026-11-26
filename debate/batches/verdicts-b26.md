## A1
Winner: Designer
Why: The attack describes a yes/no commit question, but R144 already replaced it with an action-production prompt that tells the buyer the exact words to say, so a willing buyer is one short, explicit instruction away from a clean commit. "Why not" and "can't argue with that" are exactly the hedged assents that R77 and R289 are meant to keep out of a binding commit. A re-ask leads to a written proposal plus a booked consult (R239(3), R293) rather than losing the buyer, and fallback rate is bounded per state (R36) and throttles dialing (R263), so false rejects are measured indirectly.
Worth adding: A per-dialect "clear assent, re-asked" false-reject metric at COMMIT as a release blocker, plus a certified set of action-phrase variants ("send it", "send it over") accepted only when the clause carries no negation, conditional or reported-speech marker.

## A2
Winner: Designer
Why: The premise is false. A written-proposal effect is used throughout the design (R56, R152, R225, R238, R239, R289 to R291), and "my husband and I will read it tonight" is defers_decision(to=spouse), which R243 routes to a written proposal plus a booked human consult. R232 holds the price until quote_valid_until, so read-first buyers have a real path to signing; only the binding contract waits for READ_BACK, which is deliberate.
Worth adding: An explicit request_written_proposal() event in QUOTE, READ_BACK and COMMIT, and a short verified return path (inbound or booked callback, OTP, then READ_BACK) with proposal-path conversion tracked.

## A3
Winner: Designer
Why: The read-back is already segmented (R39), each segment can be repeated on its own through repair_request (R48), a compact recap replays before the commit and a digression cap moves the buyer to a written proposal (R291), and budgets count agent loops rather than caller time (R293). Teach-back (R15, R144), year-one-only figures (R231), ACCESSIBLE_AUDIO (R238) and a written SMS read-back in CAPTION_MODE (R237) also exist. Retention isn't the only safety basis either, since the signed document, cancellation window and survey-contingent price (R159) back it.
Worth adding: Send a link-free written terms sheet matching the read-back to every buyer at READ_BACK entry, not only in CAPTION_MODE, and lint segments to at most three numbers each.

## A4
Winner: Designer
Why: The cited link-disabling applies to iMessage from unknown senders, while the design sends contract delivery and link-free OTPs on separate registered branded SMS campaigns (R260, R272) from a number the lead was told at consent (R259), and the anti-phishing line names only SSN, bank and card numbers (R171). The buyer is still on the call during WAITING_FOR_SIGNATURE, where help_with_screen offers resend, wait or callback (R60), and paper, mailed or consultant-assisted signing exist (R120, R123, R304), so a filtered text delays rather than kills the sale.
Worth adding: A fixed fragment naming the sender and first words before the send, plus an on-call "did the text arrive?" check that routes "no" to a fixed tip about the filtered or unknown-senders folder.

## A5
Winner: Designer
Why: R225 already requires lender_verified terms from a lender-hosted soft-pull decision before any financed COMMIT, so a frozen file shows up before the commit, and the call can commit only to cash or end in a written proposal. Lender status comes only from a versioned API enum (R60), so no envelope is built on a missing decision, and R232 holds the price while the buyer lifts the freeze.
Worth adding: A file_frozen lender status with a fixed, compliance-approved "lift the freeze and reopen the same link" fragment, an outbox copy of the lender link valid until quote expiry, and a booked callback.

## A6
Winner: Designer
Why: QUALIFY does ask. R208(1) is a neutral question about any expected change in ownership "such as a sale, refinance, divorce or estate", and any yes exits as NOT_SUITABLE before a quote. The lender title pull checks filings before the lien (R208(3)), install waits out the cancellation window (R17), and the cancel saga voids lender, UCC and install legs (R216), so a late-discovered conflict costs the buyer nothing.
Worth adding: Reword R208 to name home-equity loans, other home purchases and anything in progress now, with a pending_mortgage_activity row that means no same-call close.

## A7
Winner: Designer
Why: There aren't two calculators for financed terms. R225 makes the financed read-back speak lender_verified rate, term and payment, only the lender API can write that provenance (R5), and any envelope whose terms differ from the read-back gets a new quote hash and written re-disclosure. R224 (full Reg Z schedule), R309 (all-in tax price) and R23 (read-back bound to config hash) mean a mismatch must be re-read before signing, not discovered at signature, and no bank data is taken by voice, so autopay can't be assumed silently (R45, R89).
Worth adding: Have the lender API return the exact TILA box for the funded amount, speak the no-autopay APR and payment as primary, and run a to-the-cent pre-send check of envelope fields against the read-back values.

## A8
Winner: Breaker
Why: The cited elements handle the utility account holder only for usage data (R156(2) authorization, R209 savings figure, R233 service history). That blocks a savings figure, but nothing stops a price-only close when the account holder isn't a record owner, and nothing makes the interconnection application a signed document. R158 only detects the stalled PTO after the fact as a "paying, not operating" harm, so the existing design lets a willing buyer close into an install that can't be energized.
Fix needed: Add an interconnection_signer slot written only by the utility authorization API. If the account holder is not a signing record owner, block the same-call close, send a written proposal stating that a utility account transfer is required, and have a human consult handle the transfer. Make the utility interconnection application a required signer role in the envelope, and block install until the utility confirms the account holder has signed.

## A9
Winner: Designer
Why: Identity answers come only from independent records and KYC sources, never from partner lead fields (R162), so a vendor typo isn't the key. R146's token-set matcher accepts an address match plus any surname-token match, ignores first-name variants such as Bill and William, sends partial matches to clarify or a human rather than WRONG_PARTY, and already has a release-blocking false-WRONG_PARTY stratum. The OTP to the number of record (R195) gives true owners a correction path an impostor can't reproduce.
Worth adding: Measure the false-WRONG_PARTY bound on live audited calls per dialect, and send lead-versus-record mismatches to a vendor data-quality metric.

## A10
Winner: Designer
Why: The concrete rough-guess exits are already blocked: a NOT_SUITABLE resting only on a spoken slot needs an explicit lexical affirm, and a conflict with permit or aerial records goes to ROOF_FIRST or a survey, never an exit (R287). Roof age and shade are cross-checked against permits and aerial or LIDAR data (R211, R230), and the critical-slot read-back confirms or clarifies hedged values (R2). Over-exiting isn't free, because the pass metric is the bot's own signed-and-kept rate (R20) and variants are never tuned on conversion (R151).
Worth adding: A sampled false-NOT_SUITABLE audit against an independent rubric with a per-row over-exit bound as a release blocker, and hedged answers that straddle a threshold routed to a survey rather than an exit.
