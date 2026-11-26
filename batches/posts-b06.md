=== R154
Round 154: I win.

**Attack:** A lender's dealer fee could be hidden in the financed price, so financed buyers pay far more than the quote said.
**My defense:** The design already counts the dealer fee as a finance charge, and a new lender amount cancels the old quote.
**Judge:** Existing rules target this attack, and the one leftover gap is a hardening step, not a break.

=== R155
Round 155: Breaker wins.

**Attack:** A quote that includes a limited first come rebate could become false if the funding runs out before install.
**My defense:** I agreed a capped rebate behaves like a queue, not a fixed fact.
**Judge:** A proof that a program exists does not show this customer gets the money, and the install delay makes it worse.
**Fix:** Label rebates by type, never lower the price for capped ones, say "if approved", and allow a no penalty cancel if the rebate fails.

=== R156
Round 156: I win.

**Attack:** Verified usage is hard to get on a cold call, so either no savings figure is given or someone adds a spoken bill shortcut.
**My defense:** The design gives no figure when inputs are missing, and a spoken bill writer would fail the build.
**Judge:** The design fails safe as intended, and weaker sales are a cost, not a safety break.

=== R157
Round 157: Breaker wins.

**Attack:** Savings depend on future rates and export credits that are guesses, yet they are stated as facts.
**My defense:** Tariff tables are versioned, but I conceded a flat export rate and an escalation row look more certain than they are.
**Judge:** The checks look at where inputs came from, not whether the forecast is right.
**Fix:** Mark future rate rows as assumptions with required estimate wording, default to today's rates, and use the customer's exact tariff on real usage data.

=== R158
Round 158: Breaker wins.

**Attack:** A system can be installed and billed for months before the utility lets it run, yet it still counts as a success.
**My defense:** Release depends on audio audits, but I admitted the success label stops at install and the read back skips utility risk.
**Judge:** An audio audit cannot see harm that happens months later.
**Fix:** Count success only after permission to operate and months of real production, and disclose utility approval risk and payment start in the read back.

=== R159
Round 159: Breaker wins.

**Attack:** After signing, a site survey can add thousands in extra costs once the cancellation window has already closed.
**My defense:** A changed price needs a new read back, but I admitted nothing enforces that after the call.
**Judge:** Nothing governs change orders, and the install delay guarantees they land after cancellation rights expire.
**Fix:** Do the survey inside the cancellation window, and require a new quote, fresh signatures and a restarted window for every change order.

=== R160
Round 160: Breaker wins.

**Attack:** The installer could swap in different equipment after signing, so the named product and warranty become false.
**My defense:** I conceded nothing compares what is installed to what was signed.
**Judge:** The install step is never gated on a match, so the read back can be silently falsified.
**Fix:** Block install until the planned equipment matches the signed setup, and require written notice and a new signature with a free cancel if it differs.

=== R161
Round 161: I win.

**Attack:** If the installer goes bankrupt, the warranties we named have no one standing behind them.
**My defense:** Warranty claims live in one owned table that expires on any change, and the lender handles disbursement.
**Judge:** A warranty was true when stated, and a sales agent cannot make a company solvent, so the real gap is only a trigger.

=== R162
Round 162: Breaker wins.

**Attack:** A dishonest lead partner could fake the identity answers and use an accomplice's phone to sign for an elderly owner's home.
**My defense:** I admitted the challenge uses partner supplied data and a code only proves phone possession.
**Judge:** Nothing ties the signer's phone to the actual titleholder, as the design's own open item shows.
**Fix:** Use independent sources for challenges, match phones to owners before dialing, require lender grade identity checks, and mail a notice.

=== R163
Round 163: Breaker wins.

**Attack:** Installers and staff paid on low complaints could edit the records used as success labels and hide bad branches.
**My defense:** Release relies on audio audits, but I conceded training and metrics read from records that interested people write.
**Judge:** The signals for later harm all pass through a CRM written by people paid on those numbers.
**Fix:** Use independent outcome sources first, make records append only with approved edits, sample audits from the signed contract list, and unlink bonuses from training labels.
