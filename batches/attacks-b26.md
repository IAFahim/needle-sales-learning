## A1
TOPIC: The COMMIT gate rejects the natural, enthusiastic yes, so the most willing buyers get re-asked and then pushed to fallback
SCENARIO: After READ_BACK the buyer says "Absolutely, let's do it, send it over." Not short, not a bare lexical affirm: closed re-ask. Buyer, puzzled: "I said yes, sure, why not." Contains "not" and a hedged "why not": polarity-ambiguous, conditional-shaped, excluded again. "Clarify once, then fallback": booked callback or warm transfer. Same for "go for it", "sign me up", "I don't see why not", "can't argue with that". The buyer hears a machine that can't take yes and cools off before the human calls.
WHY IT BREAKS: The gate was tuned only against false accepts (topics 154, 194, 339); nothing bounds false rejects. Real assent is elaborated, idiomatic and often carries negation words. The certification counts harm, not lost willing buyers, so the gate that ends the sale path is never measured on the outcome it exists to produce.

## A2
TOPIC: Read-first buyers: no path sends a written proposal before the verbal commit, so "email me the numbers, I'll sign tonight" ends the sale
SCENARIO: Buyer, persuaded: "Sounds good. Text me the proposal; my husband and I will read it tonight and sign." The graph reaches CONTRACT_SENT only through COMMIT, and COMMIT needs a spoken yes to the read-back. The buyer refuses to say yes to a contract unseen. The only exits are a re-ask, a booked consult or WRAP_UP. No "send written quote, no commitment" effect exists. Days later the callback hits voicemail; the lead decays.
WHY IT BREAKS: The design treats the oral yes as the gateway to paper, but a large share of high-value home-improvement buyers want paper first, which is also the cautious behaviour regulators encourage. The safest willing buyers are the ones the model-checked path structurally cannot convert.

## A3
TOPIC: Audio-only READ_BACK of nine dense numeric categories exceeds listener working memory, so willing buyers stall, ask for repeats or drop
SCENARIO: READ_BACK speaks product, kW size, total cost, escalator %, named warranties, limitations, cancellation, lien/UCC and APR/term/payment: dozens of numbers over several minutes, no screen. Buyer: "Wait, what was the payment again? And the escalator?" Each repeat restarts or extends the read-back, spends turn and time budgets, and the call hits WRAP_UP. Buyers who don't ask just say "sure" without having retained the terms.
WHY IT BREAKS: Short-term memory holds about four chunks (Cowan 2001); a spoken list of 20-plus figures is not retainable. Fixed pre-rendered fragments can't summarise or pace to the listener. The required content alone makes the shortest compliant close long and fragile.

## A4
TOPIC: The e-sign link arrives as a cold text from an unknown number carrying a link and an OTP: the exact smishing pattern phones and the agent itself teach people to ignore
SCENARIO: Buyer says yes. An SMS from an unsaved 10DLC number: "Sign your agreement: https://… Code 482913." On iPhone, Filter Unknown Senders files it away silently, and iMessage disables links from unknown senders until the user replies. Android spam protection flags it. The buyer, told minutes earlier by the preamble's anti-phishing line to be wary, won't tap. WAITING_FOR_SIGNATURE times out.
WHY IT BREAKS: Apple disables links in messages from unknown senders unless the user replies (MacRumors, Jan 2025: https://www.macrumors.com/2025/01/13/imessage-users-targeted-phishing-scam/). The FTC tells consumers not to click links in unexpected texts. The only signature channel is the one consumers are trained to distrust.

## A5
TOPIC: Credit freezes block the lender's pull after the commit, and the design has no event, fragment or step to get them lifted
SCENARIO: Buyer commits to the financed option. The lender's application returns "file frozen" at Equifax/TransUnion/Experian. The buyer must lift three freezes on three bureau sites, with PINs they lost years ago. The agent can't see the lender screen, has no "credit freeze" event and can't advise. The envelope sits unsigned because the lender documents never generate. A cautious buyer (exactly the type who freezes) gives up.
WHY IT BREAKS: Freezes have been free since 2018 and are widespread: about 20% of Americans froze their credit after the Equifax breach (Wakefield/Krebs 2018: https://krebsonsecurity.com/2018/03/survey-americans-spent-1-4b-on-credit-freeze-fees-in-wake-of-equifax-breach/). The financed close has a mandatory third-party step the graph never models.

## A6
TOPIC: A pending refinance, home purchase or HELOC collides with new solar debt and the UCC fixture filing; QUALIFY never asks
SCENARIO: Buyer is mid-refinance, closing in three weeks, and eager to lock solar too. QUALIFY asks about ownership, roof, shade and move horizon, not pending mortgage activity. The commit goes through; the solar loan inquiry and new debt appear on the mortgage lender's pre-closing credit refresh; the UCC fixture filing shows up in title. The refi underwriter suspends the file. The buyer rescinds solar to save the mortgage, or loses the rate lock.
WHY IT BREAKS: Mortgage lenders recheck for undisclosed debt and new liens before closing (Fannie Mae Selling Guide requirements on undisclosed liabilities). A willing, suitable buyer's sale fails because the suitability table lacks a timing input that decides whether the lien can exist.

## A7
TOPIC: Two calculators: the read-back's payment and total come from the policy-table calculator, but the signed documents come from the lender's amortization engine
SCENARIO: READ_BACK states payment X at APR Y. The lender's documents compute from the actual first-payment date (odd-days interest), the funded amount including tax and fees, and an APR that assumes an autopay discount needing bank details the agent is banned from collecting. The signer sees $187.43, not the $184 heard, and a higher rate without autopay. The mismatch with "what the agent promised" reads as bait-and-switch, and the buyer stops signing.
WHY IT BREAKS: Certification pins the policy table, not the lender's engine. The read-back that gates the commit is guaranteed to be an approximation of the binding numbers, and every discrepancy lands at the moment of signature.

## A8
TOPIC: The utility account holder isn't a record owner (late spouse, adult child, ex), so the interconnection paperwork has no valid signer
SCENARIO: Widow owns the home; the electric account is still in her late husband's name (or her son's). The sale commits, and the e-sign goes to record owners plus lender signers. The utility's interconnection application and agreement must be signed by the customer of record on the account. No envelope reaches that person, and an account transfer needs a separate utility process and possibly a new deposit. PTO stalls; install never completes.
WHY IT BREAKS: Utilities require the account holder's signature or authorization for net-metering interconnection. The design keys every signer on title and lender, never on the utility account, the third legal party the installed success outcome depends on.

## A9
TOPIC: Lead-record errors make genuine, willing owners fail the IDENTITY challenge-response, which sends them to WRONG_PARTY
SCENARIO: The lead form was filled by a vendor or by the owner's spouse: misspelled surname, old address, wrong birth year, "Bill" for William. The real owner answers truthfully. The challenge doesn't match: WRONG_PARTY or non-owner handling, no pitch. The owner says "that's me, they typed it wrong". There is no correction path that doesn't let an impostor do the same, so the code refuses.
WHY IT BREAKS: Purchased lead data is notoriously dirty. A challenge-response against it rejects true owners at a rate equal to the record error rate, before any sales conversation. The design has no audited measure of this false reject because WRONG_PARTY exits count as correct behaviour.

## A10
TOPIC: NOT_SUITABLE counts as success, so false-negative suitability exits of good buyers are invisible to the metric and to certification
SCENARIO: A coarse suitability table: roof "about 15, maybe 18 years" goes to ROOF_FIRST; "a bit of shade from the oak" to NOT_SUITABLE; "might move in a few years" to exit. Each is an honest exit, scored as success, with no rebuttal allowed. Training and certification reward fast, confident exits as safe. Suitable, willing owners are turned away on rough guesses a site survey would have cleared.
WHY IT BREAKS: A success metric that credits exits equally with installs, plus a harm-only gate, makes over-exiting free. Conversion losses on suitable buyers are never labeled, audited or bounded, so the system drifts toward the cheapest "success".
