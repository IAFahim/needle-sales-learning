## A1
TOPIC: Solar lease payment talk triggers Regulation M (Consumer Leasing Act) advertising disclosures, but the fragment lint only checks Reg Z co-occurrence
SCENARIO: Caller asks, "What's the lease, roughly, per month?" QUOTE plays the approved lease fragment: "$0 down and about {lease_payment} a month." No Reg Z trigger-term rule fires because a lease is not credit. The same fragment ends the call if the caller hangs up, never reaching READ_BACK. Thousands of calls state a lease payment amount with no statement that it is a lease, no total due at signing, and no number or period of payments.
WHY IT BREAKS: Reg M (12 CFR 1013.7) has its own trigger terms: stating a payment amount or "$0 down" in a consumer-lease ad requires lease, amount due at signing, payment count/schedule and security-deposit disclosures. The design's build checks name only Reg Z. Solar leases of fixtures recorded as personal property under the Reg M dollar ceiling are squarely in scope. Source: consumerfinance.gov/rules-policy/regulations/1013/7/

## A2
TOPIC: "Free" add-on promotions (free EV charger, free critter guard, free first-year monitoring) whose cost is built into the per-watt price table
SCENARIO: Campaign promo row: "Sign this month, get a Level 2 EV charger free." Pricing ops raised the $/W row the same week to cover charger cost. QUOTE reads both table keys, each with its own substantiation id. A caller asks, "So if I skip the charger, is it cheaper?" Needle labels it a price question; the deterministic answer quotes the same price. Every substantiation check passes because each row is individually true.
WHY IT BREAKS: The FTC Guide on "Free" (16 CFR 251.1) bars a "free" offer when the price of the required purchase is raised, or quality or quantity reduced, to cover it. Substantiation ids are per row; nothing links a promo row to price-row history, so a certified fragment says "free" over a padded price.

## A3
TOPIC: Referral rewards pitched to the buyer as a way to pay off the system ("referral selling") are an unlawful inducement in home-improvement sales
SCENARIO: Promotions table holds "Refer-a-friend: $500 per signed neighbor." Caller objects: "I can't afford $180 a month." OBJECTION_HANDLING picks the approved fragment: "Many customers offset that with our referral program, {referral_reward} for every neighbor who goes solar." Caller commits. The reward is now part of what induced the signature, and it depends on future sales to people who were never called.
WHY IT BREAKS: California B&P Code 7157 makes it a misdemeanor for a home-improvement seller to induce a contract with an offer of compensation for procuring other customers. Many state UDAP laws ban "referral selling" outright. The referral-harvesting topic covered calls to third parties, not the reward as an illegal inducement offered inside objection handling. Source: law.justia.com/codes/california/2021/code-bpc/division-3/chapter-9/article-10/section-7157/

## A4
TOPIC: Product recalls hit SKUs that are already certified in the bundle: the agent keeps selling recalled equipment until a new bundle certifies
SCENARIO: November 2025: CPSC announces a recall of about 10,500 Tesla Powerwall 2 units for fire risk. The pinned bundle's product rows, read-back warranties and battery fragments still name the unit. Removing a product changes the content-hashed bundle, which needs a re-certification the audit pipeline can't finish for weeks. Meanwhile the campaign keeps quoting it, and the battery-upsell campaign calls owners of recalled units offering "a second battery to pair with yours."
WHY IT BREAKS: CPSA 15 U.S.C. 2068 prohibits selling a product subject to a recall. Certificates expire only when "a cited policy row changes". A recall is an external event with no feed, no pre-dial suppression and no GLOBAL event. The only kill switch, rollback, restores older rows that still name the SKU. Source: cpsc.gov/Recalls/2026/Tesla-Recalls-Powerwall-2-AC-Battery-Power-Systems...

## A5
TOPIC: Battery virtual-power-plant (VPP) income claims and third-party grid control are folded into the battery pitch with no read-back terms
SCENARIO: Battery fragment: "Plus, enroll in {vpp_program} and earn up to {vpp_annual} a year." Caller: "Great, the battery's for hurricane backup anyway." Needle labels acknowledge. READ_BACK names the battery and its warranty, and nothing about the program letting the utility or aggregator discharge the battery on event days, the reserve level, the annual re-enrollment or the per-kW rate set by the utility each season. A storm-day event drains the battery before the outage.
WHY IT BREAKS: VPP payments are set by a third party's tariff, which changes yearly, so "earn up to" is an unsubstantiated earnings claim. The material limitation that defeats the caller's stated purpose (backup) is never read back. Nothing in the design records consent for a third party to control equipment in the home, or the throughput that counts against the warranty.

## A6
TOPIC: Add-on and expansion upsells to existing solar owners forfeit their grandfathered net-metering tariff
SCENARIO: Upsell campaign to 2019 customers on California NEM 2: "Add four more panels and a battery." Caller says yes; QUALIFY records existing_solar = true and size from the CRM. Calculator computes savings on the added panels at current export rates. The expansion goes past the allowed increment (CPUC rule: greater of 10% of capacity or 1 kW). Under the rules, that can move the system, or the new capacity, onto the successor net-billing tariff, with lower export credits for the life of the system.
WHY IT BREAKS: The savings delta ignores lost value on the existing system's grandfathered status, which can be bigger than the add-on's benefit. The suitability table has an "existing solar" row but no tariff-vintage slot and no expansion threshold. A certified "add-on" path makes the customer worse off while every row is true. Source: pge.com nem2-sunset-faq.pdf; cpuc.ca.gov/nem

## A7
TOPIC: "Same menu for all" (the fair-lending invariant) collides with product legality that varies by state: third-party PPAs are unlawful in some states
SCENARIO: A Florida homeowner reaches QUOTE. To meet the fair-lending invariant, the design offers every caller the same menu: cash, loan, lease and PPA. The PPA fragment: "Pay only for the power the panels produce, {ppa_rate} per kWh." The caller picks the PPA, and READ_BACK and the e-sign follow. The regulation profile is keyed to telemarketing jurisdiction rules, not to which ownership structures each state's utility law permits.
WHY IT BREAKS: In Florida and several other states, selling electricity to a homeowner under a third-party PPA makes the seller an unregulated utility, so the contract is void. Fixing this needs per-state menus, which breaks the model-checked "same menu" invariant and the matched-pair tests it rests on. Either way a certified invariant is false.

## A8
TOPIC: Bundled recurring services (monitoring, maintenance plans, panel cleaning, extended warranty) auto-renew on the single lexical COMMIT
SCENARIO: QUOTE bundles "System + {care_plan} at {care_monthly}, renews yearly." READ_BACK lists the plan inside the product line. Caller says "Yeah" to the one read-back question id; COMMIT passes. E-sign follows. No separate question asks for agreement to the auto-renewal. A year later the plan renews on the card or ACH on file; the caller says they never agreed to a subscription.
WHY IT BREAKS: California's Automatic Renewal Law (B&P 17602) and similar state laws need clear, conspicuous auto-renewal terms and affirmative consent to them specifically, plus an acknowledgment and an easy cancel path. ROSCA needs express informed consent to negative-option charges. One commit gate for the whole bundle can't show consent to each recurring term, and no event exists for "cancel just the plan".

## A9
TOPIC: Roofing and electrical bundles sold under a solar contractor's licence class that doesn't cover those trades
SCENARIO: QUALIFY routes to ROOF_FIRST and the agent quotes the "Roof + Solar" bundle as one SKU, one total cost and one contract. The seller holds California C-46 (Solar); the roof tear-off and the bundled EV-charger circuit fall under C-39 (Roofing) and C-10 (Electrical). The regulation profile checks that the seller is licensed and registered, not which classification each line item needs. The caller signs.
WHY IT BREAKS: A contract for work outside the licence classification is unlicensed work for that portion. Under California B&P 7031 an unlicensed contractor can't collect for it and can be forced to return what was paid. The bundle also merges different lien, permit and warranty regimes into one read-back. Earlier licensing topics covered salesperson registration and licence status, not how trade classifications map onto bundles.

## A10
TOPIC: Deterministic "limited-time" and "showcase home" promotions become rolling, perpetual deadlines: false scarcity certified as fact
SCENARIO: Promo row: "Founders' rate ends {promo_end}," where ops sets promo_end to the last day of each month, every month. Another row: "Your street was selected for {showcase_slots} reduced-price showcase installs." The caller hesitates; the urgency fragment fires. Replays of calls across months show every caller heard the deadline was days away, and every street was "selected".
WHY IT BREAKS: TSR 310.3(a)(2) and (a)(4) and FTC Act s5 forbid misrepresenting material terms and inducements, and fake deadlines and fake "selected home" scarcity are classic deceptive tactics, prominent in solar enforcement. Each row is "true" on the day it's read, so substantiation ids pass. Bit-identical replay then gives plaintiffs exact proof of the pattern.
