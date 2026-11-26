## A1
Winner: Breaker
Why: The design's financing advertising controls are Reg Z only (R32 co-occurrence lint, R85 read-back of Reg Z financing terms); R180 types lease rows but attaches no lease-advertising rule set, so a QUOTE fragment stating a lease payment or "$0 down" passes every existing check. The registry and Reg M co-occurrence lint the Designer offers are all new, and the existing design fails the attack as written.
Fix needed: Every typed financing row must name its advertising rule set (Reg Z for credit, Reg M 12 CFR 1013.7 for consumer leases under the ceiling, state lease rules) or the build fails; a Reg M co-occurrence lint forces any lease payment or down-payment phrase to render, in the same mandatory segment, that it is a lease, the total due at signing, the number and period of payments and any security deposit, all from table keys, with an undelivered segment (R39) triggering a written disclosure.
Worth adding: Ban lease payment figures before QUOTE, as R32 already does for Reg Z trigger terms.

## A2
Winner: Designer
Why: The scenario's promo row says "free", and R18's banned-claims lint (free/no-cost) plus R222's extension of that lint to policy-table row text block it at build time, so the certified "free" fragment cannot exist. A bundle with no free-type wording over a padded price is a pricing-integrity issue, not a 16 CFR 251 violation, and R140's forward-only history already keeps the price record needed to audit it.
Worth adding: Require an unbundled price row for every bundled add-on and a history check that blocks a promo if its base price row rose within the prior 30 days.

## A3
Winner: Breaker
Why: Nothing in the existing design bars a referral reward from being offered as an inducement during the sales call; R74 only governs how referred contacts are reached, R220 merely tags referral fragments as marketing (keeping them out of SERVICE calls, not sales calls), and R72 blocks the fragment only if its lint happens to read "offset" as savings wording. "I can't afford $180" is not in R150's hardship lexicon, so it can still route to objection handling, and the Designer concedes no rule bars the inducement.
Fix needed: Give referral-reward keys a regulation-profile row (CA B&P 7157 and state referral-selling bans) and a model-checked invariant that no referral-reward fragment is reachable before signature plus the cancellation window (and never in banning states, only by separate outbox message elsewhere), plus a lint banning any fragment that pairs a payment or affordability key with a reward or promo key.
Worth adding: Route affordability statements ("can't afford") to the R150 suitability check, never to objection handling.

## A4
Winner: Designer
Why: The attack's premise that pulling a SKU needs weeks of recertification is wrong: R140 makes the policy table forward-only, explicitly turns recalled rows into tombstones no bundle can cite, refuses rows outside their effective window, drops QUOTE/READ_BACK to lead-gen or callback fallback, and keeps rollback from resurrecting them; R160's supply-status field and WAITING_FOR_BOM_MATCH hold uninstalled contracts. A tombstoned SKU row also starves any upsell fragment that cites it, so the agent does not keep selling the recalled unit.
Worth adding: A daily CPSC and manufacturer recall feed that sets supply_status=recalled automatically and fails closed, plus pre-dial suppression of marketing campaigns to owners of recalled units.

## A5
Winner: Breaker
Why: R157's qualifier and R83's material-limitation rows exist, but nothing in the design models a third-party program that can discharge the customer's battery: no limitation row for it, no consent to third-party control, and R83's outage_backup product-fit rule checks the product, not program enrollment, so a backup buyer is never warned. The defense's real fixes (no earnings claims, enrollment only after PTO, mandatory discharge limitation, backup conflict rule) are all new.
Fix needed: Type VPP rows as third_party_program; ban earnings fragments on the sales call; offer enrollment only after PTO by outbox under the program's own terms and consent; make a "programs may discharge your battery and reduce backup" limitation mandatory in READ_BACK whenever a battery is quoted, and flag outage_backup plus any program default as a product-fit conflict.
Worth adding: Warranty rows state throughput limits and whether program cycling counts against them.

## A6
Winner: Breaker
Why: The existing calculator (R157) uses the customer's current exact tariff but models only the add-on, and the existing_solar slot (R82) and suitability table (R71) carry no tariff vintage or expansion threshold, so an upsell that pushes a grandfathered system onto the successor tariff can show positive savings while making the customer worse off. The Designer concedes the gap, and every remedy offered is new.
Fix needed: Add a tariff_vintage slot (legacy tariff, interconnection date, grandfather end) from the utility API and interconnection agreement, per-utility expansion_rule rows, a whole-system calculator delta including lost legacy-tariff value, sizing capped at the threshold or NOT_SUITABLE when the delta is negative, no figure when vintage is unknown, and a mandatory READ_BACK row when the add-on crosses the threshold.
Worth adding: Keep existing-customer upsell campaigns in lead-gen mode until that profile is certified.

## A7
Winner: Designer
Why: The attack's dilemma rests on a misreading: R46 is "all options to all, non-protected keys only", so the product-policy table may branch on property jurisdiction while matched-pair tests vary only prohibited-basis fields, and a per-state menu breaks no invariant. The table is already jurisdiction-keyed (R46, R47, R178) and every mandatory READ_BACK fragment is signed by outside counsel per regulation profile (R265), so nothing in the design forces a PPA onto Florida callers.
Worth adding: A default-deny product_legality row per (financing type, state, utility territory) with a legal attestation, and a model-checked invariant that QUOTE offers exactly the attested lawful set for the property's jurisdiction.

## A8
Winner: Breaker
Why: R144, R223 and R45 make the commit deliberate and keep payment off the voice channel, but the design has no notion of a recurring or auto-renewing service: no clear-and-conspicuous renewal terms, no consent captured specifically for the renewal, no acknowledgment, and R216's cancel saga cannot cancel only the plan. A renewing care plan bundled into the product line rides on the single contract commit, which the Designer concedes; the negative_option typing and ARL/ROSCA flow are new.
Fix needed: Type recurring or auto-renewing rows as negative_option and bar them from voice QUOTE and READ_BACK; sell them only in writing through an ARL/ROSCA flow with clear terms, a separate affirmative checkbox and signature, an acknowledgment and an online cancel path; give cancel_or_rescind a target (contract or plan); lint "renews" tokens out of voice fragments.

## A9
Winner: Breaker
Why: R71's ROOF_FIRST (inspection before any quote) blocks the exact "Roof + Solar" quote in that branch, but R178's licence invariant checks only that the installer's licence is valid in the jurisdiction, not the trade class each line item needs, and R159 actually routes reroofing and panel work into the same contract as change orders. An EV-charger circuit or a reroof change order can therefore be contracted under a solar-only classification, and the per-line-item class check is new.
Fix needed: Give every quote line item and change order a required_license_class per jurisdiction, extend the R178 invariant so each needs a matching valid class on the contracting licensee's row (or an attested incidental-work rule), split the contract otherwise, and name the licensee and licence number per line item in READ_BACK and the contract.

## A10
Winner: Designer
Why: The existing design already blocks this: R78's lint bans fake urgency and unverifiable external-fact fragments, so a deadline fragment and a "your street was selected" claim cannot be certified; R92 allows social proof only as audited aggregates and bans references to specific addresses; R153 plays "There's no need to decide today." before READ_BACK; and R15/R145 send hesitation into the vulnerability counter and decline handling rather than a persuasion fragment. The history-based rolling-deadline detector is polish on a sound defense.
Worth adding: A build check over table history rejecting promos re-issued with a new end date within 12 months.
