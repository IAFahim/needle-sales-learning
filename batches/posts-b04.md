=== R134
Round 134: Breaker wins.

**Attack:** Safety was proven on the design drawing, but the running program is built by outside tools that could be compromised.
**My defense:** Other checks might catch a skipped step, but I admitted nothing proves the program matches the drawing.
**Judge:** Those other checks live inside the same generated machine, and every real answer was new.
**Fix:** Pin the build tools, compare the built program against the drawing, and add an independent monitor that blocks a sale without a read-back.

=== R135
Round 135: I win.

**Attack:** A security patch changes the runtime, so every certificate expires at once and we must choose between staying vulnerable and going offline.
**My defense:** A patched runtime that gives identical answers on every audited call keeps the same evidence, and failing states use the fallback.
**Judge:** The design already replays all saved audited calls on any new build, so no fresh 300,000 calls are needed.

=== R136
Round 136: Breaker wins.

**Attack:** Anyone could post a fake or replayed e-sign message and push a call to sale pending, or kill a real sale.
**My defense:** Install waits out the cancellation window, but I agreed nothing checks who sent the message.
**Judge:** Nothing in the design authenticates those events, and replay protection only stops exact copies.
**Fix:** Treat each message as a hint, fetch the real status from the vendor, require signature checks, bind envelope ids to the call, and send odd reversals to a human.

=== R137
Round 137: I win.

**Attack:** A backup phone carrier changes the audio quality, so speech recognition makes more mistakes on numbers while every hash still matches.
**My defense:** Digit by digit confirmation, read-backs and a strict yes check still catch wrong text.
**Judge:** The gap is real, but the likely result is more clarifying questions and fallbacks, not committed harm.

=== R138
Round 138: I win.

**Attack:** Several dialer workers reading stale data could place too many calls to one number and ignore an opt-out.
**My defense:** The design already requires the opt-out sweep to finish before any redial, and caps use the strictest state.
**Judge:** A sloppy implementation would break a rule the design already states, so it is not a design gap.

=== R139
Round 139: Breaker wins.

**Attack:** Calling hour checks depend on the server clock and time zone data, which are uncertified, so one fault breaks the rules fleet wide.
**My defense:** Hours already use the strictest candidate zone, but I admitted time sources are not pinned.
**Judge:** Nothing checks the clock or time zone data, and the strictest zone logic only helps in some cases.
**Fix:** Pin the time zone data, use three trusted time sources, add a safety margin, and test every zone across daylight saving changes.

=== R140
Round 140: Breaker wins.

**Attack:** Rolling back to yesterday's bundle brings back old prices, a recalled product's warranty and missing legal notices under a still valid certificate.
**My defense:** Facts carry effective dates, but I admitted rollback is not aware of them.
**Judge:** The policy table lives inside the bundle, so a rollback never triggers the expiry rule.
**Fix:** Make the policy table move forward only, let rollback restore everything else, and fall back to lead capture when no retained bundle fits today's table.

=== R141
Round 141: I win.

**Attack:** A fraudster who hijacks a homeowner's phone number could pass identity checks and receive the signing code.
**My defense:** The lender runs its own checks, a site survey needs the home, and install waits out the cancellation window.
**Judge:** The fraudster cannot reach anything irreversible or collect money data, so the harm is caught in time.

=== R142
Round 142: I win.

**Attack:** Dialing faster than the model fleet can handle could leave people in silence and count as abandoned calls.
**My defense:** The opening greeting is a pre recorded fixed clip that needs no model, and the dial list is consented leads only.
**Judge:** Slowness causes delays handled by the time budget, not legal abandonment, and the attack assumes overdialing the design never uses.

=== R143
Round 143: I win.

**Attack:** Human review needs real call audio, so private recordings go to an outside labeling vendor that could be breached.
**My defense:** The design collects little sensitive data, mutes payment details, and keeps only consented, deletable samples.
**Judge:** That leaves the ordinary risk of any call center recording, not a flaw unique to this design.
