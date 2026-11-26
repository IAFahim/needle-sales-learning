## A1
TOPIC: Model-checked graph is not the binary that runs: StateSmith codegen and C toolchain supply chain
SCENARIO: Invariants (every commit path passes READ_BACK, no price writer from Needle) are proven on the exported graph. The C that actually runs is produced by StateSmith (an open-source generator pulled from a package registry) plus a compiler and build image. A compromised or buggy generator release emits a transition from QUOTE straight to CONTRACT_SENT under one rare guard combination. The graph still model-checks clean; the binary skips READ_BACK and the bundle hash faithfully certifies the wrong artifact.
WHY IT BREAKS: Verification targets the model, not the compiled artifact; nothing in the design proves generated C refines the graph (no translation validation, no reproducible build, no diverse double-compile). Build-chain backdoors are real: xz-utils CVE-2024-3094 hid in release tarballs, not source. A sampled 1e-5 audit cannot find a guard-gated path.

## A2
TOPIC: Security patching vs a certificate keyed on runtime build and hardware class
SCENARIO: A critical CVE lands in the inference runtime, glibc, OpenSSL or the GPU/CPU driver on the pinned Needle fleet. Patching changes the runtime build hash, so every certificate on every state expires at once. Options: keep serving calls on a known-vulnerable fleet that holds live customer PII and payment-adjacent data, or drop the entire fleet to deterministic fallback while recertifying on fresh human-audited real calls.
WHY IT BREAKS: Rule-of-three at 1e-5 needs ~300,000 clean audited calls per bound; recertification after every patch means weeks to months dark. The design forces a standing choice between being insecure and being offline, and patch cadence (monthly at minimum) outruns certification cadence.

## A3
TOPIC: Forged or replayed e-sign webhooks advancing calls to SALE_PENDING
SCENARIO: "Status only from vendor webhooks." The webhook endpoint is a public URL. An attacker (or a rogue lead vendor wanting commissions) replays a captured "envelope-completed" payload, or posts a forged one with another envelope id. The state machine moves WAITING_FOR_SIGNATURE to SALE_PENDING, starts the cancellation clock and schedules install against a contract nobody signed; conversely a forged "declined/voided" kills real sales.
WHY IT BREAKS: DocuSign Connect HMAC signing is an opt-in feature the integrator must enable and verify (docusign.com/blog/developers/dsdev-connect-feature-hmac); replay protection and envelope-to-call binding are not in the design. The graph treats vendor events as ground truth with no authentication or idempotency spec.

## A4
TOPIC: Carrier failover changing codec and sample rate outside the certified bundle
SCENARIO: The primary SIP trunk degrades; traffic fails over to a second carrier. Audio now arrives as AMR-NB transcoded to G.711 at 8 kHz with heavier packet-loss concealment instead of the wideband path ASR was certified on. ASR version and ITN flags are unchanged, so the bundle hash still matches, but word error rate on numbers and negations jumps. Needle gets cleaner-looking but wrong text all afternoon.
WHY IT BREAKS: The certificate pins ASR software, not the acoustic channel (codec, sample rate, jitter buffer, transcoding hops, carrier noise suppression). Narrowband and transcoded audio measurably raise ASR WER. Per-dialect bounds were measured on one channel; failover silently invalidates them while every hash check passes.

## A5
TOPIC: Distributed dialer race on frequency caps and DNC across workers and regions
SCENARIO: Ten dialer workers in two regions share caps and suppression through a replicated store. A number gets a call at 10:00 that ends in an opt-out; the post-call DNC sweep runs after transcript processing. Meanwhile workers in region B, reading a lagged replica, place two more calls on the same campaign, and a fourth from a retry queue. Florida's three-calls-in-24-hours cap and the opt-out are both breached.
WHY IT BREAKS: The pre-dial gate is specified as logic, not as a linearizable check-and-reserve. Fla. Stat. 501.059(8)(a) caps calls at three per 24 hours on the same subject; each extra call is a per-call statutory violation. Eventually consistent counters plus asynchronous DNC sweeps make over-dial a property of the architecture, not a bug.

## A6
TOPIC: Clock, NTP and tzdata outside the content-hashed bundle drive calling-hours compliance
SCENARIO: Calling-hours guards depend on the host clock and the OS time-zone database. A container image ships stale tzdata, an NTP source fails and the clock drifts, or a DST transition is mishandled in one region. On the November fall-back day the dialer computes local time an hour off and places a wave of calls at 7:15 a.m. or 9:20 p.m. local across a whole time zone.
WHY IT BREAKS: The bundle pins graph, weights, ASR and policy table, but not time source or tzdata, which every hours guard reads. TSR 16 CFR 310.4(c) bans calls before 8 a.m./after 9 p.m.; several states are stricter. One bad clock is fleet-wide and simultaneous, so harm arrives as thousands of violations at once.

## A7
TOPIC: Blue/green rollback resurrecting superseded prices, warranties and legal rows
SCENARIO: A new bundle ships a price increase, a recalled inverter removed from the warranty table and a new state disclosure effective today. The golden-audio canary trips on an unrelated latency regression; auto-rollback restores yesterday's bundle. The old policy table is now live again: lower prices, the recalled inverter's warranty, and no new disclosure, all quoted under a still-valid certificate for that old bundle.
WHY IT BREAKS: "Certificates expire when a cited policy row changes," but rollback makes the old row current again, and its certificate was never revoked. Rollback is treated as safe by construction, yet legal and commercial facts are time-dependent; nothing checks a restored bundle against today's effective-dated obligations.

## A8
TOPIC: SIM-swap or port-out hijack defeats challenge-response identity and SMS-OTP e-sign
SCENARIO: A fraudster SIM-swaps a homeowner's number. The outbound call (or a callback) rings the fraudster, who passes the identity challenge using breached address and household data matching the lead record. They qualify, accept the read-back, then receive the e-sign link and OTP by SMS on the hijacked number. A solar contract, a lender application and a UCC/lien filing now sit on the victim's home.
WHY IT BREAKS: Both factors ride the same phone number, and knowledge-based challenges use data sold in breach dumps. FBI IC3 logged 1,611 SIM-swap complaints and over $68M losses in 2021 alone (ic3.gov/PSA/2022/PSA220208). The design has no number-port/SIM-change check or out-of-band verification.

## A9
TOPIC: Predictive-dialer pacing outrunning Needle fleet capacity causes abandoned calls
SCENARIO: The dialer paces outbound connects on expected Needle throughput. A host failure or latency spike halves fleet capacity. The dialer keeps connecting live humans; turns queue, the PREAMBLE starts late or not at all, and callees hear seconds of silence and hang up. Fallback "callback or human" piles up booked callbacks that human staff cannot absorb.
WHY IT BREAKS: TSR 16 CFR 310.4(b)(4) and 47 CFR 64.1200(a)(7) require connection within two seconds of the greeting and abandonment at or below 3% per campaign per 30 days. Nothing couples dial pacing to live model capacity; an infrastructure outage becomes a regulatory abandonment breach at full fleet scale.

## A10
TOPIC: Human-audit and replay pipeline forces retention of full raw audio with third-party labelers
SCENARIO: Certification and drift alarms require humans listening to real call audio, all disagreements plus random samples, and bit-identical replay needs the inputs kept. So raw audio with identity answers, addresses, finances and household details is retained and shipped to an outsourced labeling vendor. That vendor is breached, or a labeler exfiltrates recordings, exposing thousands of homeowners' voices and verified personal data.
WHY IT BREAKS: "No-retain mode" and "PII surrogates" cannot apply to audio that the release gate needs humans to hear. The safety case structurally depends on the largest, least-controlled copy of customer data. Third-party file-transfer breaches (MOVEit, 2023) show vendor tiers are the usual leak point; voiceprints also enable cloning.
