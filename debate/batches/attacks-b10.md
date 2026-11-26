## A1
TOPIC: Competitor sabotage by spoofed inbound calls that rescind signed contracts and opt out live leads
SCENARIO: A rival installer buys the same aged lead list. Inside the cancellation window, it spoofs each signed customer's caller ID into INBOUND_OPEN. It passes the identity challenge with name, address and roof facts from data brokers, then says "cancel my contract, I changed my mind." cancel_or_rescind runs with no persuasion and no friction. Unsigned leads get "put me on your do-not-call list." Then the rival calls the same homeowners, who have now been "rescinded".
WHY IT BREAKS: Inbound ANI can be spoofed. STIR/SHAKEN attestation is often B or C on inbound, or missing. The challenge-response only checks facts from the lead record, and those are public or brokered. The design treats a cancel or DNC request as irreversible and frictionless by design. That gives no confirmation step on the e-sign channel, and it leaves no way to undo a forged rescission.

## A2
TOPIC: Identity challenge-response as a PII enumeration oracle for fraudsters and data brokers
SCENARIO: An attacker scripts thousands of inbound calls, rotating spoofed numbers. Each call answers the IDENTITY challenge with a guessed name and address pair or a guessed co-owner. VERIFIED goes on to QUALIFY, where the agent asks about "your home" and its roof age. WRONG_PARTY branches differently. The deterministic timing and fragment ids tell the two outcomes apart. The attacker learns who owns which home, which homeowners are leads, and who is mid-purchase, then sells that as "solar-intent, verified owner" data or uses it for targeted scams.
WHY IT BREAKS: A deterministic verifier gives a distinguishable answer on every guess. The design has no rate limit by lead, no attempt counter across numbers, no constant-shape failure path and no lockout. Confirming that a record matches is itself a disclosure of lead data. This turns topic #125 (passive leakage) into an active oracle the attacker can query again and again.

## A3
TOPIC: SMS pumping and toll fraud through the e-sign OTP, envelope resends and "outbox copy" messages
SCENARIO: A fraud ring plants leads, or reaches INBOUND_OPEN, using number ranges it shares revenue on. Bots run each call through to CONTRACT_SENT, then ask "resend the link" and "text me your DNC policy" again and again. Every request triggers a vendor SMS plus an OTP. Across 50,000 bot calls, the company pays carrier termination fees that the ring splits. The e-sign vendor also flags the account and suspends it, which stalls real signings.
WHY IT BREAKS: OTP flows are the main channel for SMS pumping (artificially inflated traffic). Twitter put its losses at about $60M a year. The outbox drains on every committed turn, and the design has no cap per number, cap per call or check on number reputation. WAITING_FOR_SIGNATURE models webhooks, not cost or abuse. Sources: https://www.group-ib.com/blog/sms-pumping/ , https://cybelangel.com/blog/sms-pumping-fraud-telecom-attack/

## A4
TOPIC: Consent bombing: third parties file "prior express written consent" forms for numbers they don't own
SCENARIO: An extortionist, or a plaintiff's firm's recruiter, fills the company's own web lead form 20,000 times. Each form uses a victim's real phone number and ticks the box naming the seller and the AI voice. The pre-dial gate sees valid per-number consent, Reassigned Numbers Database "no change" and no DNC, so the dialer calls them all. The victims never consented. A class action follows, along with a demand letter offering to settle quietly.
WHY IT BREAKS: Under the TCPA, consent must come from the called party (the subscriber or customary user). A form record is not proof of that. The gate checks whether consent exists, not who gave it. It has no double opt-in by SMS reply from that number and no link between form device and number. Damages run $500–1,500 per call, with no cap on the class.

## A5
TOPIC: "AI-verified" tickets and warm transfers launder an impostor's requests to human ops
SCENARIO: The attacker passes the inbound identity check with brokered facts, as in A1. They raise service_issue: "my installer needs my new number and email for the install, and change my loan autopay account." The agent opens a ticket and sends a warm transfer tagged VERIFIED. Ops staff trust the AI's verification and update contact and payment details. The next e-sign OTPs, installer messages and refund checks go to the attacker.
WHY IT BREAKS: The design's verification is a weak knowledge check, but its outputs carry authority downstream. That is the business email compromise pattern, with the agent vouching for the caller. Nothing in the slot provenance marks "verified by challenge" as too weak for changes to account, contact or payee. A human acting on an agent-made ticket is outside every certified invariant.

## A6
TOPIC: Insider logic bomb hidden among a fragment's approved alternative wordings
SCENARIO: A disgruntled script approver adds wording #7 to the savings fragment. It passes every lexical lint: no literal numbers, no banned claims, Reg Z co-occurrence satisfied. It says "most of our customers end up paying nothing out of pocket." The deterministic selector picks #7 only when the hash of certain slots (for example age band plus a financing selection) falls in a narrow bucket, about 0.3% of calls, and skewed toward seniors. Random audit samples almost never hit it.
WHY IT BREAKS: "Human-approved" means one person can be the single point of failure. Lints are syntactic, while deception is semantic. Deterministic wording selection keyed on slot values gives an insider a precise trigger. Audits stratified by dialect and state do not stratify by wording id crossed with slot conditions. The design has no two-person rule and no requirement that every wording is audited on live calls.

## A7
TOPIC: Corrupt or infiltrated human audit labelers poison the ground truth that gates certification
SCENARIO: A labeling vendor's staff, or one bribed lead labeler, mark harmful closes as "no harm" and correct stops as "missed buying signal" in one or two target states. Disagreement adjudication sends those calls to the same small pool. The per-state 1e-5 bound certifies the bad state. Drift alarms stay quiet because they read the same labels. Retraining on the "union of all data" then teaches Needle the corrupted labels.
WHY IT BREAKS: The whole safety case rests on "humans listening to audio," but the design never threat-models the labelers. It has no blind gold calls planted to catch dishonest labelers, no rotation, no limit on labeler concentration per state, no conflict-of-interest controls and no independent re-audit. Topic #212 covers CRM success labels. This attack hits the harm labels behind certification itself.

## A8
TOPIC: Threats of violence, swatting and doxxing aimed at installers and reps hit a closed scripted exit
SCENARIO: A caller says "send your installer to my street and he won't leave," or "I know where your crew lives, I'll burn down the next house you put panels on." Needle has no threat event. The nearest options are sensitive_event (scripted sympathetic exit) or out_of_scope. The call ends politely. The call ran in no-retain mode, so nothing is preserved, and no human safety team is told. The crew is sent on schedule.
WHY IT BREAKS: GLOBAL has about 8 events and none is "threat to others." Closed-world forcing makes a credible threat look like distress or noise. The design has no escalation duty, no evidence hold that overrides no-retain or automated deletion, and no hold on install or visit dispatch. A competitor or harasser can also use the same gap to threaten without leaving a trace.

## A9
TOPIC: Flooding request_human and booked in-home consults to exhaust closers and lure reps to an address
SCENARIO: A rival's bot farm calls in, or answers outbound calls, and says "I want to talk to a real person" or "book me an in-home consult." Warm transfers tie up the few human closers, so real buyers wait or abandon. Booked consults pull reps across the county to empty lots. In one case, a fake owner passes the brokered-fact identity check and books a 7 pm consult at a house the attacker controls to rob the rep.
WHY IT BREAKS: request_human is a GLOBAL exit that is always honored, and the design treats it as a safe fallback with no limit on abuse. Booked consults are outbox effects whose WAITING_FOR substates model only booked, conflict, timeout and error. They do not check address ownership against record owners, flag one address booked many times, or send bot-scored callers to a callback queue. Door-to-door reps already face real safety risk.

## A10
TOPIC: Insider poaching at the human handoff: closers divert transferred customers to side deals or rivals
SCENARIO: A human closer receives warm transfers carrying the full slot store: verified usage, the quoted price, financing appetite, record owners and the vulnerability counter. Off the recorded line, by personal cell, they offer the "same system, $3k cheaper through my other company." Or they sell the warm-transfer feed to a competitor. Customers sign elsewhere, and the high-vulnerability flags tell the insider who is easiest to pressure.
WHY IT BREAKS: Certification ends where request_human starts. The design gives humans everything and constrains nothing: it has no data minimization in the handoff, no masking of vulnerability flags, no monitoring of contact outside the recorded channel and no alarm on transfer-to-close leakage. Passing a vulnerability flag to a commissioned human turns a safety signal into a targeting list.
