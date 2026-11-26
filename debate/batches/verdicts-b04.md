# Verdicts, batch b04

## A1
Winner: Breaker
Why: The design's core safety claims (every commit path passes READ_BACK, no Needle price writer) are proven only on the exported graph by our own checker (R69); nothing in design.md or final-plan.md checks that the StateSmith-generated, compiled C matches that graph. The existing checks the defense cites (R49 quote-hash commit, R23 config-hash binding, R87 lexical gate) are themselves logic inside the same generated machine, and no outbox-side check requires a READ_BACK playout mark before CONTRACT_SENT. The defense admits the gap, and its real answers (translation validation, independent trace monitor, reproducible build) are all NEW.
Fix needed: Vendor StateSmith and the compiler by hash with reproducible builds; at release, enumerate the compiled binary's (state, event, abstract-guard) transition relation by harness and diff it against the exported graph (any extra edge fails the release); and add an independently written runtime trace monitor at the outbox that refuses CONTRACT_SENT or any commit effect unless the committed trace contains READ_BACK with a playback-engine completion mark for the same quote hash.
Worth adding: Diverse double-compile with a second toolchain for the generated C.

## A2
Winner: Designer
Why: The existing design already has the mechanism for admitting a new runtime build: R3 makes every candidate build replay all states' frozen human-audited gold sets, and R53 requires cross-node bit-identical replay before release, so a patched runtime that reproduces every audited real call bit-for-bit carries the same evidence rather than needing 300,000 fresh calls. Most of the CVEs named (OpenSSL, glibc networking) sit outside the "runtime/kernel build" the R53 key names, and states that diverge fall to the existing per-state deterministic fallback rather than the fleet staying on a vulnerable build.
Worth adding: State explicitly that a certificate re-keys to a patched runtime on bitwise-identical replay of the state's full gold set plus canary corpus, and keep Needle inference in a minimal sandbox (no network, no PII store) so perimeter patches never touch the certified hash.

## A3
Winner: Breaker
Why: R60 makes vendor webhooks/APIs the only source of signature status, but nothing in the design authenticates those events, binds an envelope id to the session, or blocks out-of-order transitions; R55 idempotency keys stop exact replays only, not forged events with other ids. A forged "completed" starts the cancellation clock and schedules install, and a forged "declined/voided" kills a real sale. The defense concedes this, and its fixes are all NEW.
Fix needed: Treat any inbound webhook as a wake-up hint only: on receipt, pull envelope status from the vendor API with the system's own credentials and make only that pulled status a StateSmith event; also require HMAC verification (with a build check that it is enabled), timestamp windows, envelope id stored in the session's outbox record with unknown or mismatched ids rejected, and monotonic status (void after completed goes to human review).

## A4
Winner: Designer
Why: Wrong ASR text on a degraded channel still has to pass the design's ASR-independent checks: digit-wise confirmation of Tier A numbers (R26), critical-slot read-back that turns a single error into a caller correction (R2), the grounding gate (R61), the ambiguous-polarity closed re-ask (R77), and a commit gate that needs a short lexical affirm to the read-back question id (R81/R87). So the realistic result is more clarifies and fallbacks, which the R33 drift alarms then catch, not committed harm. US PSTN audio is mostly narrowband G.711 already, so "certified on wideband" overstates the shift. The certification-validity gap is real but its consequences fail safe.
Worth adding: Make channel class (codec, sample rate, trunk/route) a certification stratum and key, run the golden-audio canary through each trunk's codec chain, and alarm per trunk on confidence and clarify rate within minutes.

## A5
Winner: Designer
Why: R66 makes the post-call DNC sweep a precondition "before any redial," so the scenario's region-B and retry-queue calls (all redials placed before the first call's sweep committed) are already forbidden by the design; a replica-lag implementation that allows them breaks a stated invariant rather than showing a design gap. Mid-call opt-outs end the call and write DNC at once (R24, R75), and caps are evaluated for the most restrictive jurisdiction (R41, R70). The attack fairly notes that the concurrency primitive is unspecified, and the defense's permit only makes the existing ordering concrete.
Worth adding: Implement the pre-dial gate as a linearizable per-number check-and-reserve (no read replicas, in-flight reservations counted, pending_sweep lock cleared only when the sweep commits, fail closed), with a TLA+-style spec as a release check.

## A6
Winner: Breaker
Why: Every calling-hours guard reads the host clock and the OS tz database, yet neither is in the content-hashed bundle and the design has no clock-integrity check, guard band or dial-time canary; R68 pinned ASR for exactly this kind of silent dependency drift, but time was left out. A missing or broken tz database (e.g. falling back to UTC) or a bad time source is fleet-wide and simultaneous, so one fault yields thousands of 16 CFR 310.4(c) violations. The existing most-restrictive-candidate logic only helps when address and area code differ. The defense concedes this, and every mitigation it gives is NEW.
Fix needed: Pin tzdata in the certified bundle and make the dial gate use only that copy; take time from at least three authenticated sources and fail closed when offset or uncertainty exceeds a small bound; shrink the lawful window by a guard band (wider on DST-transition days); and property-test the gate over every zone across DST boundaries, plus a daily per-zone test-dial canary.
Worth adding: Two independent tz implementations whose disagreement blocks the dial.

## A7
Winner: Breaker
Why: The final plan puts the policy table inside the content-hashed bundle, and R66/R67 roll back to "the previous certified artifact," so a rollback brings back yesterday's prices, the recalled inverter's warranty and the missing disclosure, together with a certificate that was valid for that bundle. Effective dates protect nothing here, because yesterday's table did not know its rows would be superseded. "Certificates expire when a cited policy row changes" is never triggered by a rollback, and the design never tracks the current effective table separately from the bundle. The defense admits rollback is not policy-aware, and all its fixes are NEW.
Fix needed: Take the policy table out of rollback: it is forward-only, and recalled or withdrawn rows become tombstones no bundle can cite. Rollback restores graph, weights, fragments and ASR only, always runs against the current effective table, and may target only a retained bundle that is continuously re-checked (lints, fact-key coverage, gold replay) as compatible with that table; otherwise QUOTE/READ_BACK states drop to lead-gen or callback fallback. The runtime refuses any row outside its effective_from/until window.

## A8
Winner: Designer
Why: The SIM-swap fraudster gains nothing and cannot get the contract to lien or install. The design schedules a site survey as the next step after signature (whole-call scope) and ROOF_FIRST inspection, both needing physical access at the victim's home; install waits out the longest cancellation window (R17); and signers come from record-owner lookup on the validated address, with capacity flags going to human review (R88). The lender runs its own application and KYC, and the voice channel never collects SSN, bank or card data (R45, R89), so the call leaves the fraudster nothing to monetize. The shared-factor weakness the attack names is real, but its harm is caught before anything irreversible happens.
Worth adding: A carrier SIM-change/port-out check before IDENTITY and before the OTP (a recent change means no sale on the call), plus a mailed notice to every record owner at the validated address through the existing print-and-mail outbox.

## A9
Winner: Designer
Why: The two-second rule concerns what the callee hears after their greeting, and in this design that is the compiled, unskippable PREAMBLE (R31), started deterministically by OPENING once the callee answers (R35), with no Needle inference. Later slowness on a degraded fleet causes delays, which the wall-clock budget counters turn into WRAP_UP (R69), and failing states drop to fallback; neither is an "abandoned call" in the regulatory sense. The dial list is limited to PEWC and warm leads (R59), and callback bookings already have CONFLICT handling (R55). The attack assumes predictive overdial pacing that the design never specifies.
Worth adding: Admission control that ties each dial permit to a live Needle capacity token, 1:1 pacing by default, a per-campaign rolling abandonment counter in the pre-dial gate, and callback slots drawn from a staffed-capacity calendar.

## A10
Winner: Designer
Why: The existing design already limits what labelers can hear and who may keep it: data minimization with no account, income or credit data (R7), real-time audio mute of payment data (R45), lint bans on requesting SSN, DOB, bank or card data (R89), NO_RETAIN without affirmative retention consent, a pipeline that rejects transcripts lacking the consent flag, processors barred from training (R40), and deletable gold sets (R7). Certification needs only audited samples from consented calls, not every call. The "outsourced labeling vendor" is the attacker's assumption, and the remaining exposure is the ordinary QA-recording risk of any call center, not a structural flaw specific to this safety case.
Worth adding: Label only in a controlled enclave (streaming VDI, no download, watermarking, access logs), mute IDENTITY-state and address segments by state timestamps, separate audio from name and number, and put a retention TTL on raw audio.
