=== R304
Round 304: Breaker wins.

**Attack:** Signing texts to a co owner's Canadian mobile fall under Canada's anti spam law, and the agent treats every +1 number as American.
**My defense:** Texts never go to a co owner unless they opt in themselves, and every text passes a consent gate.
**Judge:** Once they opt in, the text still goes to a Canadian phone with no sender identification or unsubscribe, because nothing checks the country.
**Fix:** Map every +1 number to its country and send nothing to Canada without a certified Canadian profile.

=== R305
Round 305: Breaker wins.

**Attack:** A caller asks for a Saturday evening callback at home in Ottawa, and the agent dials a Canadian number under US rules.
**My defense:** A stated move adds that place as a candidate jurisdiction, and the dial gate fails closed when registry checks can't pass.
**Judge:** Those rules are built around US states and time zones, so nothing actually blocks a Canadian callback after the 6pm weekend limit.
**Fix:** Any place without a certified rule profile, including any foreign country, gets no calls or texts, and such callbacks are refused when booked.

=== R306
Round 306: I win.

**Attack:** A court could void Puerto Rico's net metering law while the certified savings row stays unchanged.
**My defense:** Only first year savings at today's rates are spoken, and a tariff monitor expires rows the moment rates actually change.
**Judge:** A ruling only matters once the regulator changes the tariff, which the existing monitor and manual override already catch.

=== R307
Round 307: Breaker wins.

**Attack:** Louisiana bans sales calls on Sundays and legal holidays, and Mardi Gras is a holiday only in some parishes.
**My defense:** The dial gate already works out the callee's local date and treats state calling rules as data rows.
**Judge:** The local date is right, but there is no day or holiday rule type and no way to scope a holiday below the state.
**Fix:** Add day and holiday rules with parish or city scope from the home's location, treating unknown scope as statewide.

=== R308
Round 308: Breaker wins.

**Attack:** New York City and Suffolk County require home improvement licences that a state level profile never sees.
**My defense:** Installer licences are already checked against the property's jurisdiction, and a stale feed blocks the quote.
**Judge:** Those checks use state boards, and the switch to a licensed salesperson works only by state, so city and county licences slip through.
**Fix:** Stack the rules by state, county, city and tribal land, and default any unverified locality to a lead only call.

=== R309
Round 309: I win.

**Attack:** A Colorado city tax the calculator misses makes the total cost read back on the call wrong.
**My defense:** The signed contract must equal the read back total, and the company honors that price.
**Judge:** Any extra tax would be an unagreed price rise with a free exit, so the seller pays it, not the customer.

=== R310
Round 310: I win.

**Attack:** A home on a rural co op gets savings quoted at the big utility's net metering rate because of its mailing city.
**My defense:** Usage and utility come only from the customer's actual utility account, and a missing tariff row means no figure at all.
**Judge:** The utility is never guessed from the mailing city, and the bill check would fail on a mismatched tariff.

=== R311
Round 311: I win.

**Attack:** A winter only Florida home exports power while empty, and the annual payout at a low rate wipes out the quoted savings.
**My defense:** Savings are modeled hour by hour on real usage data under the customer's exact tariff, and promises of a zero bill are banned.
**Judge:** Hourly modeling already captures the empty months, so making payout fields mandatory only tightens a sound rule.

=== R312
Round 312: I win.

**Attack:** Holidays and time zones inside a state could make a timely cancellation look late.
**My defense:** Every buyer gets the longest five business day window, and install waits until it is over.
**Judge:** A day three cancel is well inside that window wherever the buyer lives, and spoken cancels are honored at once.

=== R313
Round 313: Breaker wins.

**Attack:** An Arkansas home with a Texas mailing address gets Texas rules, and nothing on the call corrects it.
**My defense:** Owner records, county parcel data and the utility account are already read from the validated address.
**Judge:** None of those sets the jurisdiction, so a lookup that finds the Arkansas owner would still leave Texas rules in charge.
**Fix:** Take the state, county and city from the parcel, never the postal address, and send any mismatch to a person before any close.
