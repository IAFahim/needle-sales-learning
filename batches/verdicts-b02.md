# Verdicts, batch b02

## A1
Winner: Breaker
Why: The design's pre-dial gate (R8) lists only "National + internal DNC scrub". "State mini-TCPA rules as facts rows" (R8) and most-restrictive-wins (R70) are general hooks, but no step ever names scrubbing against state registries or their own exemption tests. The Designer agrees the gap exists, and the defense depends on the NEW state_dnc_registry rows.
Fix needed: Add a state_dnc_registry row for each state that runs a list (IN, TX, CO, PA, MO and others). Each row carries its own exemption predicate and is never mapped to federal PEWC. Scrub against every candidate jurisdiction's list before each dial, and do not dial when a list is stale or unavailable or its exemption can't be proven. Add a model-checked invariant: no DIAL edge unless every candidate state's registry check passes.
Worth adding: Track each state list's download date and the refresh cadence its statute requires as a certificate input. A stale list then decertifies dialing in that state.

## A2
Winner: Breaker
Why: Every revocation path in the design is voice or DTMF: the lexicon, GLOBAL, the R66 transcript sweep and R75 DTMF. The design itself opens text channels (the e-sign SMS, the R89 short code, the R84 outbox mail), and nothing routes replies on those channels to the consent ledger. Under 64.1200(a)(10), revocation by any reasonable means, such as a text reply, has to be honored within 10 business days. The R74 gate rechecks the ledger before every dial, but that does not help when the revocation never reaches the ledger.
Fix needed: Build a revocation intake bus. The e-sign vendor, SMS short codes, email, the web form, installers and CRM notes all feed the stop lexicon plus the GLOBAL stop classifier. A hit writes the DNC ledger within 1 business day, unmatched replies go to human review, the ledger is read at every dial (scheduled callbacks included), and vendor contracts require replies and STOP events to be forwarded. Add Tier A fault-injection tests for each channel.
Worth adding: Treat a STOP keyword on any short code as global revocation for every campaign tied to that number.

## A3
Winner: Designer
Why: The scenario depends on not being able to rebuild the played message after a rollback. The design rules this out: bundles are immutable and kept, each session is stamped with its bundle hash (R67), the deterministic wording choice is logged (R59), playout marks are recorded (R39), and the PEWC artifact is stored (R74). With all of that, the exact unique message can be reproduced bit for bit. NO_RETAIN (R40) covers caller content, not the agent's own render log or the consent ledger. The 5-year WORM retention is only polish.
Worth adding: Set an explicit retention schedule: CDRs, consent artifacts, render logs and every fragment wording kept 5 or more years in WORM storage regardless of privacy mode, with NO_RETAIN defined in writing as covering caller content only.

## A4
Winner: Breaker
Why: The design has no event for a legal threat and no preservation hold. Routine surrogate replacement, scrubbing and gold-set deletion (R7, "deletion = data operation") therefore keep running after litigation becomes reasonably foreseeable. The Designer agrees on both gaps. NO_RETAIN only protects calls that were never recorded, and the defense rests on the NEW legal_threat event and hold flag.
Fix needed: Add a legal_threat GLOBAL event, fired by a lexicon or by Needle. It plays a fixed neutral fragment, offers a human, ends the pitch and sets legal_hold. The hold freezes every deletion, surrogate and scrub job for that session and number, keeps the original audio and transcript, and alerts legal. Inbound complaint and demand channels and the post-call sweep set the same hold. Add Tier A tests of hold versus deletion.

## A5
Winner: Designer
Why: The attack's premise is false. The self-echo filter compares text (R38), speaker_change is a Needle event over words (R9), identity is a spoken challenge-response (R73), and prosody is a single per-utterance F0 final-rise token (R80). Nothing in the design computes or keeps a speaker embedding or voiceprint.
Worth adding: Add a build check that bans speaker embeddings and diarization identity vectors, including in vendor ASR settings pinned under R68, and allows front-end acoustic features only per utterance and in memory.

## A6
Winner: Breaker
Why: sensitive_event(medical_emergency) exists (R19), and wherever retention consent is given (R40), its label and the spoken health content stay in retained transcripts, audit samples and the per-release training union. Retention consent is not the separate MHMDA opt-in. "Medical_dependency" is not the design's label, but medical_emergency serves the same purpose. PII surrogates (R7) remove names, not health content linked to a phone number and call record. The Designer agrees on this gap.
Fix needed: Add a health-data quarantine. When a medical sensitive_event or a health lexicon hit fires, redact those spans from every retained transcript, audit sample and training set, and persist only a type-less sensitive_exit label. In MHMDA (and NV/CT) profiles, keep no health-derived data beyond the in-memory routing decision. Train the medical classes only on synthetic or consented data, have the build pipeline reject health-tagged real spans, and publish a consumer health data policy.

## A7
Winner: Breaker
Why: Nothing in the design checks for ESIGN 7001(c) consent that "reasonably demonstrates" the consumer can access the records, and it offers no accessible or paper alternative. The landline/mailed fallback is still an open item (R22). Waiting on webhooks (R60) and on the cancellation window (R17) does not help if the required disclosures were never validly delivered, because then the window may never start.
Fix needed: Before CONTRACT_SENT, ask a fixed question: electronic documents, or paper or an in-person signing? Paper, or any stated access need, routes to a mailed or consultant-assisted signing. The envelope runs a 7001(c) demonstration step (a code visible only inside a sample record in the contract's format). The vendor must meet WCAG 2.1 AA with tagged PDFs. Install waits until delivery of the disclosures is verified.

## A8
Winner: Designer
Why: The existing fallback is "callback or human". R1 books a consult, and R56 gives a warm transfer to staffed humans or a booked consultant call, and a human can quote. So the design is not a structural dead end, and R25/R15 already lengthen thresholds. The Unruh theory is also weak. Without an ADA violation, Unruh requires intentional discrimination (disparate impact is not enough), and the ADA's reach to remote, non-physical sales is limited in the Ninth Circuit.
Worth adding: Route repeated unintelligible turns with clear speech-present audio straight to a human. Never give such a call an AI callback, and flag the lead human-only. Add a consented atypical-speech stratum with "reached quote or human" parity as a release metric.

## A9
Winner: Breaker
Why: R47 covers contractor or salesperson licensing (CA HIS), not telemarketer registration and bonding. No row in the design checks Texas ch. 302 registration, which after SB 140 also covers texts, or registration in other states. The Designer agrees the row is missing, and the defense depends on the NEW seller_registration rows.
Fix needed: Add a seller_registration row per state (TX ch. 302 as amended by SB 140, UT, WA and others) with registration id, bond or security, and expiry. Use it as a pre-dial and outbox guard, with texts counted as solicitation. Add a model-checked invariant: no DIAL and no SMS effect without valid registration in every candidate state. Raise an alert 30 days before expiry.

## A10
Winner: Breaker
Why: R74 does stop the caller from dictating the co-owner's number. But R22 sends the signing link and gates the envelope with an OTP "to dialed number", while R88 puts every record owner on the signer list. As written, then, every owner's OTP goes to the phone of the person on the call, and one spouse can sign for both. Lender KYC covers only borrowers, not a non-borrowing co-owner on title.
Fix needed: Each signer needs independently sourced contact data (their own consent or lead record, or a phone verified by lender KYC), and no two signers may share a phone or email. Any envelope that creates a lien or UCC filing requires per-signer vendor ID verification, with a notary or in-person consultant as the fallback. No lien filing or install proceeds until every owner has been independently verified.
