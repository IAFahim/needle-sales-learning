## A1
TOPIC: E-sign OTP and "outbox copy" texts to a Canadian (+1) mobile fall under Canada's anti-spam law (CASL), which the compliance gates never model
SCENARIO: Ontario snowbird couple owns a Florida house. The husband passes IDENTITY on his US number. The wife, a record owner, has only her +1-905 Ontario mobile, so the envelope SMS goes there. The deterministic outbox also sends her the "copy" of contact info and DNC policy. It's NANP +1, so the dialer treats it as a domestic number. She gets SMS from a US solar seller with no CASL consent record, and no CASL identification or unsubscribe content in the fixed fragment.
WHY IT BREAKS: The design checks consent and SMS rules only under the TCPA and 10DLC. CASL covers commercial electronic messages sent to Canadian devices. It needs its own consent, sender identification and an unsubscribe mechanism, and penalties run up to C$10M. NANP +1 numbers make Canadian mobiles indistinguishable unless the NPA is checked, and the gate never checks it.

## A2
TOPIC: Booked callbacks and warm-transfer follow-ups to Canadian numbers trigger the CRTC telemarketing regime (DNCL registration, Canadian calling hours, ADAD rules)
SCENARIO: A snowbird calls INBOUND from her Canadian cell. Mid-call she says "call me back Saturday evening, I'll be home in Ottawa." The callback is booked to a +1-613 number. The pre-dial gate runs the US national DNC, the RND and US calling hours for the "most restrictive candidate" state. At 7pm Saturday the agent dials an artificial-voice sales call into Canada.
WHY IT BREAKS: The CRTC Unsolicited Telecommunications Rules require registering with the National DNCL operator and paying fees before calling Canadians. Weekend calling must end at 6pm local time, and automatic dialing-announcing device (ADAD) solicitation needs express consent. None of this is in the regulation profile. Sources: crtc.gc.ca/eng/phone/telemarketing/tobligations/rules-regles.htm; Telecom Decision CRTC 2007-48.

## A3
TOPIC: US territories: Puerto Rico's net-metering law is under a federal oversight board's lawsuit, so a territory's "certified" policy-table row can be voided by PROMESA litigation, not by legislative change
SCENARIO: A 787 lead in Bayamón gets a QUOTE. The policy table cites Act 10-2024, which extends retail net metering in Puerto Rico, as the basis for savings. The fragment is certified, and the certificate expires only "when a cited policy row changes." Meanwhile the FOMB's suit to nullify Act 10 under PROMESA §204/§108 moves forward in federal court. A ruling or a regulator order lands, and no row edit ever happens.
WHY IT BREAKS: Certificate expiry keys on edits to table rows, not on legal events like an injunction or nullification. Territory law sits under a federal board that can void statutes, a layer no state profile has. Sources: FOMB Act 10 FAQ (oversightboard.pr.gov/act-10-faq); Canary Media on the FOMB lawsuit; KSAT (Jul 26 2024).

## A4
TOPIC: Day-of-week and legal-holiday telemarketing bans, including parish-only holidays and territory dates across the International Date Line, absent from a pre-dial gate built on hours and frequency
SCENARIO: The campaign runs on Mardi Gras Tuesday. In New Orleans that day is a legal holiday under Louisiana law, but only in certain parishes. Next weekend the dialer schedules Guam leads (UTC+10) for "Saturday 6pm Pacific," which is already Sunday in Guam. The gate checks the calling-hour window and frequency caps for the most restrictive candidate jurisdiction. It has no calendar-day rule and no parish-level holiday table.
WHY IT BREAKS: Louisiana's telephone-solicitation law (La. R.S. 45:844 series; LPSC DNC rules) bars calls on Sundays and state legal holidays, and Mardi Gras is a holiday only in listed parishes. Other states have similar Sunday or holiday bans. Rules keyed to the calendar date need the callee's local date and a sub-state holiday calendar. Sources: legis.la.gov RS 45:844.31; lpsc.louisiana.gov General Order R-35852.

## A5
TOPIC: Sub-state licensing: home improvement contractor and salesperson licences required by New York City and by suburban counties where the state has none, so a lead-gen mode keyed by state misses them
SCENARIO: New York has no statewide home-improvement salesperson registration, so the profile puts NY in full-close mode. The agent quotes and closes a homeowner in Suffolk County, then one in Queens. The Suffolk County Consumer Affairs home-improvement licence, the NYC DCWP Home Improvement Contractor licence and the NYC home-improvement salesperson licence all require a licensed person to solicit and sign. The policy table has no county or city rows.
WHY IT BREAKS: The design switches to "lead-gen mode in salesperson-registration states," which is state granularity. Licensing that lives at the city and county level goes unmodeled. Under NYC rules and county licensing, an unlicensed sale can make the contract unenforceable and void the seller's right to collect.

## A6
TOPIC: Address-level tax jurisdiction: the "total cost" read back depends on home-rule city and county sales-tax options and on ZIP codes that straddle city lines
SCENARIO: A Colorado lead's ZIP spans two municipalities. The calculator prices statewide: state sales tax exempts renewable-energy components. The house is actually in a home-rule city that has not adopted the local exemption, so the city charges its own sales or use tax on the equipment. READ_BACK states a "total cost" with zero tax. The installer later invoices the tax, or the contract total is wrong.
WHY IT BREAKS: Colorado exempts solar components from state tax, but local and home-rule jurisdictions decide for themselves whether to exempt them. The correct total needs a rooftop-level tax jurisdiction, not the state or ZIP. A materially wrong total read at the COMMIT gate defeats the read-back. Sources: tax.colorado.gov sales-use-tax-topics-renewable-energy-components; EnergyBot "Local Option" exemption.

## A7
TOPIC: Municipal utilities and electric co-ops are exempt from state net-metering statutes, and their service territories don't follow city, ZIP or county lines
SCENARIO: A lead's mailing city is served by the investor-owned utility, so the calculator applies the state's statutory net-metering tariff. The parcel actually sits in a rural electric co-op's territory. The co-op's board sets its own buy-all/sell-all export rate and a solar fixed charge, both outside the state NEM law. Savings are quoted at retail-rate netting the customer will never get.
WHY IT BREAKS: In many states the net-metering mandates bind only regulated investor-owned utilities, while munis and co-ops set rules locally and change them by board vote. The utility serving a house is determined by service-territory maps at the parcel level, which the design never consults. The certified savings fragment is wrong at the source.

## A8
TOPIC: Snowbird seasonal vacancy: a part-year home produces most when it is empty, and annual true-up or avoided-cost cash-outs erase the credits the savings figure assumes
SCENARIO: A Michigan couple's Florida house is occupied November to April. Verified usage shows low summer bills because the house sits empty with the AC off. The system is sized to annual kWh and pitched as "covers your bill." From May to October, peak production exports into a vacant house, credits pile up, and the annual true-up pays the excess at avoided cost, a fraction of retail. The real bill savings are a fraction of what was quoted.
WHY IT BREAKS: QUALIFY asks "move horizon" but not occupancy pattern. Verified usage averages over vacancy, and the calculator nets annually at retail. For seasonal residents, timing mismatch and true-up rules make the savings claim unsubstantiated.

## A9
TOPIC: Cancellation-window arithmetic: "midnight of the third business day" depends on the buyer's state holiday calendar and on time-zone lines inside states and reservations
SCENARIO: A buyer in Arizona's Navajo Nation portion (which observes DST, unlike the rest of Arizona) or in Florida's Central-time panhandle signs Friday before a state-only holiday. Ops code computes the window on the federal holiday calendar and the dialer's or the state capital's time zone. It treats a cancel emailed at 11:20pm local on day three as late and schedules install for the "day after the longest window."
WHY IT BREAKS: Business-day counts exclude state-specific holidays, and the cutoff is midnight where the buyer is. Time-zone boundaries split states and counties, so neither the state nor the county gives the zone. A timely rescission gets refused and work starts inside a live cancellation right.

## A10
TOPIC: Border towns: rural mailing addresses use a post office across the state line, so the lead record puts the house in the wrong state and nothing in the call ever corrects it
SCENARIO: A house in Arkansas has a "Texarkana, TX" mailing address, a regional area code and a ZIP whose post office is in Texas. The profile loads Texas rules: contract law, home-solicitation cancellation, licensing and the Texas utility market. The caller confirms "yes, Texarkana" during IDENTITY. jurisdiction_changed never fires because the caller never contradicts the record. Contract, disclosures, utility and AHJ are all wrong-state.
WHY IT BREAKS: The jurisdiction_changed guard reacts only to in-call cues. Here the record and the caller agree and are both wrong. USPS city and state reflect the delivering post office, not the parcel's state, county or AHJ, and only a parcel/geocode lookup at the pre-dial gate would catch it.
