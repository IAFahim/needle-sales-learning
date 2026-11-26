# Verdicts, batch b21

## A1
Winner: Breaker
Why: R149, R123 and R122 are real and stop the default case, so an envelope never goes to vendor-sourced data. But once the wife opts in herself, the envelope SMS still goes to a +1-905 number. R196 explicitly treats all NANP mobiles as domestic, so no CASL profile is ever applied. CASL's s.6(6) transactional exemption removes only the consent requirement. The sender-identification and unsubscribe content are still required, and no fixed fragment carries them. The defense concedes the country check is missing and closes the gap only with NEW NPA resolution.
Fix needed: Resolve every outbound number from NPA to country (with a carrier lookup) before any SMS or email effect. Treat Canadian and Caribbean NPAs as foreign jurisdictions. With no certified CASL profile, the outbox refuses and signing falls back to mail or consultant-assisted signing. Add a build check that every outbox fragment carries the profile's required identification and unsubscribe keys.
Worth adding: Model-check that no SMS effect exists for a number whose country is unresolved.

## A2
Winner: Breaker
Why: R70 and R183 exist, but both are US-state-shaped. jurisdiction_changed takes a state, and current_location adds only a time zone, which for Ottawa is the same Eastern zone as Florida. The R114 and R122 "every candidate state" invariants are never shown to fail closed for a non-US candidate that has no rows at all. Nothing in the existing design models the CRTC weekend 18:00 cutoff, DNCL registration or ADAD consent. The +1-613 callback passes R196 as domestic. The fail-closed default for an unprofiled country is the defense's NEW addition.
Fix needed: Any candidate jurisdiction without a certified regulation profile is a hard no-dial and no-SMS. This covers any non-US country, whether identified by NPA or by stated location. callback_request is refused at booking with a fixed fragment and a written follow-up instead. Add the invariant that no callback books to an unprofiled jurisdiction.

## A3
Winner: Designer
Why: The attack assumes no row ever changes. But a ruling only alters what the customer gets once PREB or the utility changes the tariff, and the R157 tariff-filing monitor expires rows on exactly that. R78's manual compliance override covers lag. R231 and R157 limit the call to year-one savings at today's rates, and future NEM terms are only ever assumption-qualified. That residual risk is the same as any NEM change in any state.
Worth adding: A legal_basis and docket-watch field on statute-backed rows that marks contested rows as assumption-only, and territories as lead-gen until a profile is certified.

## A4
Winner: Breaker
Why: The local date is handled: R41 and R139 use address tz with pinned tzdata, so Guam's Sunday is computed correctly. R8 facts rows could hold a statewide Sunday ban. Louisiana's telephone-solicitation rules do bar Sunday and legal-holiday calls. But the existing gate has no typed calendar-day rule and no holiday scope below state level, so a parish-only Mardi Gras holiday cannot be expressed, which the defense concedes.
Fix needed: Add calendar_rule rows (day-of-week bans and legal-holiday lists) to each profile. Give each holiday a geographic scope (state, parish or county, municipality) resolved from the parcel geocode, and treat unknown scope as statewide. Evaluate every candidate zone on its local date. Add a full-year property test and the invariant that no DIAL happens on a banned local date.

## A5
Winner: Breaker
Why: R178's installer_license invariant is real, but its rows are state boards (CSLB, ROC, DBPR). For New York, which has no state board, nothing forces a NYC or Suffolk row to exist. R47's lead-gen switch, which governs who may solicit and sign, is explicitly state-granular. R181's sub-state layer covers only tribal land. The NYC home-improvement salesperson licence therefore goes unmodeled, and the defense relies on a NEW layer stack.
Fix needed: Make the regulation profile a layer stack (state, county, municipality, tribal) resolved from the parcel geocode, with contractor and salesperson rows allowed on any layer. A locality whose licensing coverage isn't attested defaults to lead-gen. Add the invariant that no on-call price is given unless every layer's salesperson row permits it.

## A6
Winner: Designer
Why: R154 binds the e-sign contract amount to the read-back amount, and R232 makes the company honor that price. R159 treats any later increase as a re-disclosed change order with a no-penalty exit, and an unconsented increase as Tier A harm. A missed local use tax therefore costs the seller, not the customer, and the read-back total stays the amount the customer actually owes. In Colorado, contractor use tax on materials is usually the contractor's own cost anyway.
Worth adding: A rooftop-geocode tax_jurisdiction slot with local exemption rows, so the quoted price is accurate rather than merely honored.

## A7
Winner: Designer
Why: The design never infers the utility from the mailing city. R156 makes the utility API or bill extractor the only writer for verified_usage, from the account holder's actual utility. R227 keys calculator rows by delivery utility with "missing row means no figure", and the R228 bill-reconciliation gate would fail if an IOU tariff were applied to co-op bills. All three are in the design as cited.
Worth adding: Co-op and municipal tariff rows must cite the board's own tariff, with a short effective_until and a board-meeting monitor.

## A8
Winner: Designer
Why: The attack assumes annual retail netting, but R157 requires the exact tariff schedule on verified interval data, and R226 models the post-solar bill on that data. Summer vacancy and its exports therefore appear in the model. R18 bans "zero bill", R229 forces a spoken residual bill, and R210 caps sizing to verified usage. Making true-up and cash-out mandatory tariff fields polishes an already-sound "exact tariff" rule.
Worth adding: A build check that every tariff row has true-up period, carryover and cash-out rate fields, plus a neutral year-round occupancy question.

## A9
Winner: Designer
Why: R15 applies the longest window (5 business days) to every buyer, and install waits it out. A cancel on day three of a three-day statutory window is therefore well inside the design's own window, wherever the buyer is and whatever state holiday intervenes. R216 accepts oral cancels, R194 freezes the window in the customer's favour, and R139 pins tzdata.
Worth adding: A single certified deadline function using the parcel's zone and the union of federal, state and local holidays.

## A10
Winner: Breaker
Why: The parcel and utility reads exist (R88, R204, R205, R156, R212), but no rule makes the parcel the jurisdiction key. R22 validates the postal address, which returns Texarkana, TX. The fail-closed "no fee owner" clause sits in R181's tribal fix and triggers only if the lookup happens to fail. A geocoding vendor would find the Arkansas owner and pass, leaving the Texas profile to drive contract, cancellation and licensing. The defense concedes the gap.
Fix needed: A pre-dial resolver geocodes to a rooftop point and then a parcel (state, county, municipality, AHJ, tribal, tax and utility territory). Postal city and state are never the jurisdiction key. If postal and parcel states disagree, both become candidates with most-restrictive-wins, and there is no close until a human confirms the parcel. The utility API's service address must match the parcel state.
