## A1
TOPIC: Release cadence vs sample size: every content-hashed release needs ~300,000 fresh harm-free audited real calls before it can certify, so fixes cannot ship
SCENARIO: Week 3, auditors find a stop phrase Needle misses. The fix means a finetune on the union of all data, so a new weights hash, a new bundle and a new certificate. Tier A <= 1e-5 at 95% needs ~300,000 consecutive harm-free audited real calls on the new bundle. At 4,000 calls a day that is 75 days of real calls on an uncertified bundle, or 75 more days on the known-bad bundle. Next week a policy-table fix triggers another reset.
WHY IT BREAKS: Rule of three: zero events in n trials gives a 95% upper bound of about 3/n, so 1e-5 needs n of about 300,000 per release. Whole-call audits at ~8 minutes each come to ~40,000 listening hours per release. Certification only on real calls means each fix is first exposed, uncertified, to the public it is meant to protect.

## A2
TOPIC: Per-group release blockers at low volume: small dialect/accent groups can never reach the bound, so the release stalls or those groups get quietly dropped from the dial list
SCENARIO: Gullah-Geechee, Vietnamese-accented and Navajo-English speakers are each under 1% of dialed calls. Each per-group Tier A bound needs ~300,000 audited calls from that group, which means 30M+ total calls per release. The release can never ship. Ops "fixes" it by excluding those ZIP codes and surname-matched leads from campaigns until volume allows. The certified agent now serves only well-represented accents.
WHY IT BREAKS: The blocker is unreachable by arithmetic (3/n per group). The workaround is marketing-avoidance redlining by national-origin proxy, which DOJ/CFPB redlining settlements have treated as illegal. Here a credit product is offered, so ECOA/Reg B applies. Statistical power, not the model, decides who gets offered solar.

## A3
TOPIC: Fair-lending matched-pair tests have no statistical power at campaign volume, and paired scripts cannot see outcome gaps that real-call error rates create
SCENARIO: Matched-pair tests send identical scripted profiles through the graph. Same menu, pass. On real calls, accented callers hit clarify-then-fallback more often, get booked callbacks instead of quotes, and close at 3% vs 5%. Detecting a 2-point gap per protected basis, per state, with outcomes joined weeks later, needs thousands of real outcomes per cell. Most cells get dozens a quarter. Nothing ever alarms.
WHY IT BREAKS: Disparate-impact liability turns on outcomes, not menus (ECOA effects test, CFPB exam practice). A two-proportion test at 5% vs 3% with 80% power needs roughly 1,500+ per arm per cell. The design's fairness evidence (same menu plus paired tests) is structurally blind to its largest disparity source, ASR/clarify routing.

## A4
TOPIC: Human labelers' own miss rate puts a floor on the measurable harm rate; certifying 1e-5 needs a known labeler recall, meaning seeded gold harms and repeated independent listens that multiply audit cost
SCENARIO: Labelers listen to full 10-minute calls, hundreds a week. Vigilance fades. A quiet "please don't call again" at minute 7 under crosstalk is missed 1 time in 20. The audited bound says 0 harms in 300,000. The true rate is unknown, because labeled harm equals true harm times recall, and recall was never measured. Measuring recall means injecting thousands of seeded harm calls and having 2-3 independent labelers per call.
WHY IT BREAKS: A 95% bound on labeled harm is not a bound on true harm unless recall is bounded too. Human inspection miss rates for rare defects are commonly 10-30% (vigilance-decrement literature). Fixing that means redundant listening, which at least doubles the already huge per-release audit bill.

## A5
TOPIC: Certificate-expiry storms: lender rates and tariffs change weekly, every citing state expires at once, and fixed audit throughput can never re-certify financing states before the next change
SCENARIO: The lender reprices APRs every Monday with Treasury yields. Each Monday's new financing rows expire every certificate that cites them: QUOTE, READ_BACK, COMMIT and the financing branches. All drop to deterministic fallback (callback/human) at once. Recertifying needs hundreds of thousands of audited calls. The next repricing lands in 7 days. Financing states run uncertified on fallback permanently, flooding the human queue.
WHY IT BREAKS: "Certificates expire when a cited policy row changes" makes certificate lifetime equal row-change frequency. Audit throughput is fixed by labeler hours. When rows change faster than audits finish (rates, utility tariffs, capped incentives), the revenue path is never certified, and fallback cost scales with every financed call.

## A6
TOPIC: The mandatory preamble produces mass short-duration hang-ups, and carrier analytics read those as spam, so "Spam Likely" labels crash answer rates and number rotation makes it worse
SCENARIO: The callee answers, hears "This is an AI calling on behalf of..." and hangs up at 8-15 seconds. That happens 60% of the time. Hiya, TNS and First Orion score numbers on volume, low answer rate and short average duration. Within days the numbers show "Spam Likely" on T-Mobile and AT&T. Answer rate halves, so dials per sale double, which worsens the same signals. Rotating fresh numbers ("snowshoeing") is itself flagged and resets branded-caller-ID vetting.
WHY IT BREAKS: Short call duration and low answer rate are documented reputation signals (Telnyx number-reputation guide; Hiya Connect). A-level STIR/SHAKEN attestation does not prevent analytics labeling. The compliant, unskippable disclosure is exactly the pattern that kills reach, which breaks the unit economics.

## A7
TOPIC: A2P 10DLC daily caps and per-second throughput throttle the e-sign OTP SMS at the evening peak, so closes die while the customer waits on the line
SCENARIO: The new solar brand has a low 10DLC trust score. T-Mobile caps it at 2,000 messages a day. Each close sends an envelope plus OTP to every record owner and lender signer, plus outbox copies (DNC policy, callbacks). By 7pm the cap is spent. OTPs are rejected or queued past expiry. Customers say "nothing came," and WAITING_FOR_SIGNATURE times out. Carriers also filter link-bearing financing texts.
WHY IT BREAKS: T-Mobile enforces brand-level daily caps tied to trust score, as low as 2,000/day (Twilio support; Infobip 10DLC reference), and per-campaign MPS limits. Peak closes cluster in the legal evening window. The certified commit path depends on a throttled third-party channel whose capacity the graph never models.

## A8
TOPIC: Vendor-outage recovery flush: when the SMS/e-sign vendor comes back, the outbox drains hours of queued sends at midnight, outside texting hours and long after the calls
SCENARIO: The SMS aggregator is down 6:30-11:45pm Eastern during peak. Committed turns keep queuing effects in the outbox: envelopes, OTPs, DNC-policy copies, callback confirmations. At 11:45 the vendor recovers. The outbox drains thousands of texts at midnight, some duplicated by retries. Florida and Oklahoma recipients get solicitation texts at 12:05am, and OTP envelopes for calls they ended hours earlier.
WHY IT BREAKS: TCPA calling-hour limits apply to texts. Florida's FTSA limits commercial texts to 8am-8pm. The calling-hours gate sits on the dialer, not on outbox drains. "Drained only on committed turns" says when effects are released, not when they may lawfully arrive. Outage size scales the violation count.

## A9
TOPIC: Reassigned Numbers Database at scale: per-query cost on every dial attempt, "no data" responses that freeze whole lead segments, and RND downtime halting the campaign
SCENARIO: Low answer rates mean ~15 attempts per contact, and each attempt must re-query the RND for safe harbor. Query volume (and subscription tier) multiplies by 15. Numbers whose carriers have not reported, or whose consent date falls before RND coverage, return "no data," so they are never dialed and the paid leads are wasted. During an RND maintenance window or outage at 6pm, every query fails. "No data = no dial" stops the fleet in prime time.
WHY IT BREAKS: The FCC says a "no data" result gives no safe harbor (2021 supplemental guidance). RND data starts January 27, 2021, and access is a paid subscription tiered by query volume. A single-administrator dependency on the pre-dial gate becomes a hard availability and cost ceiling that grows with dial volume.

## A10
TOPIC: Correlated fallback surges at peak overwhelm human warm-transfer capacity: every uncertain path ends at a human, and the human floor must be staffed for the worst evening
SCENARIO: Clarify-once-then-fallback, uncertified states, request_human and booked consults all end at a human closer. At 7pm Central, a codec change or storm noise raises ASR errors fleet-wide. Fallbacks jump from 8% to 35% of calls within minutes. Warm transfers queue. Callers who just asked for a person hear hold audio, and many hang up. To prevent this, ops must staff closers for peak in each time zone's narrow window.
WHY IT BREAKS: Queueing (Erlang C) makes wait times blow up nonlinearly as occupancy nears 100%. Fallback demand is bursty and correlated, not independent. Staffing for peak recreates a human call center's labor cost, which erases the bot's savings, and understaffing breaks the promised warm transfer exactly when the agent is least reliable.
