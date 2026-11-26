=== R224
Round 224: Breaker wins.

**Attack:** A solar loan quotes a low payment that jumps about $80 a month if the customer never prepays an assumed tax credit.
**My defense:** Spoken financing terms come from the lender's rate sheet and must be read back.
**Judge:** Nothing says which payment in a multi step schedule gets spoken.
**Fix:** Loans store full payment schedules, the call speaks every step, and affordability uses the highest payment.

=== R225
Round 225: I win.

**Attack:** The call has to read back financing terms before the lender decides, so customers hear the best credit tier and get a worse deal later.
**My defense:** Credit information can only come from the lender's own verified check, never from speech, and no credit pull happens on the call.
**Judge:** If the lender's decision changes the terms, the quote is invalidated and a new read back is required before anything is sent.

=== R226
Round 226: Breaker wins.

**Attack:** Solar customers must move to a different rate plan, so savings priced on the current plan can be wrong.
**My defense:** The calculator must use the customer's exact rate schedule on real usage data, or give no figure.
**Judge:** The design never names a separate plan for after solar, so both bills could use a plan the customer will lose.
**Fix:** The calculator prices the post solar bill on the mandated plan and the read back states the change.

=== R227
Round 227: Breaker wins.

**Attack:** A customer on a community choice energy provider could get figures built on standard utility generation rates.
**My defense:** A figure needs the exact rate schedule, or none is given.
**Judge:** No slot records the provider, so the exact rate rule never fires.
**Fix:** A provider slot filled only from utility data keys the calculator rows, and an unknown provider means no figure.

=== R228
Round 228: I win.

**Attack:** The calculator multiplies by the standard residential rate and ignores low income discount programs, overstating or understating savings for those households.
**My defense:** Savings need the customer's exact billed rate schedule from utility data, and discount programs are part of that schedule.
**Judge:** A calculator using the standard rate already breaks an existing rule, so this is a calculation bug and not a design gap.

=== R229
Round 229: I win.

**Attack:** The agent promises a near zero bill, but fixed and minimum charges still remain after solar is installed.
**My defense:** A near zero bill is already a banned claim, checked when the code is built and again on every reply.
**Judge:** The exact rate schedule includes fixed and non bypassable charges, so the shortcut the attack relies on is already forbidden.

=== R230
Round 230: I win.

**Attack:** A customer says their roof is shaded "not really", and that spoken answer gets turned into an inflated production figure.
**My defense:** Production never comes from speech. Roof and shade data come from aerial lookups, and spoken estimates are never used for savings or sizing.
**Judge:** Shade only routes suitability, and the contract depends on a survey confirmed price with a no penalty exit.

=== R231
Round 231: Breaker wins.

**Attack:** A multi year savings figure leaves out costs the system already knows about, like replacing the inverter or resetting the panels for a roof repair.
**My defense:** Future figures must carry an estimate qualifier, and roofs that fail suitability are routed to repair first.
**Judge:** A qualifier on assumptions doesn't cure a material omission of predictable costs.
**Fix:** Lifetime and payback figures are banned on calls, and any written multi year figure must subtract known expected costs.

=== R232
Round 232: I win.

**Attack:** The price table changes after the call, so the contract envelope might carry different terms than the customer heard.
**My defense:** The contract is bound to the exact quote that was read back, and a table update never rewrites an envelope already sent.
**Judge:** The system refuses to send a contract without a matching read back, and any later price change requires new disclosure and a fresh signature.

=== R233
Round 233: I win.

**Attack:** A new account holder's usage history belongs partly to a prior occupant, or ignores a planned electric vehicle, so the system is sized wrongly.
**My defense:** Figures come only from verified usage, sizing is capped to it, and spoken future loads can never upsize the system.
**Judge:** The design fails toward a smaller, truthful system, and utility data normally returns only the current account holder's history.
