## A1
Winner: Designer
Why: The attack's premise is weak: a seller placing calls through a carrier is that carrier's customer, not the originating provider, and the 24-hour duty under 64.1200(n)(1) falls on the provider, which then asks the seller. An ITG request arrives as number + time + caller ID, and the existing R116 WORM record set (CDR with real number, time, caller ID, plus consent artifact, render log and agent audio) already answers it from that key, with R74's PEWC artifact answering "what consent". What is missing is an on-call process and a Call-ID join, which is operational speed, not missing evidence.
Worth adding: Store SIP Call-ID and SHAKEN origid in the CDR at dial permit, staff a traceback responder with a 4-hour internal SLA, and keep sales trunks separate from service lines.

## A2
Winner: Designer
Why: Scripted and prerecorded telemarketing is already routinely treated as a common question, so determinism does not create the class exposure; it bounds it. R67 stamps every session with its bundle hash, so any defect is confined to the calls on that bundle and path, and R124's audited canary ramp, R21's model-checked "no pitch after decline" invariant and R18's compliance sign-off attack the defect itself. Consent, the usual TCPA battleground, stays individual and documented per number (R74).
Worth adding: A defect-recall procedure (quarantine bundle, list affected sessions by hash, suppress and send cure notices) and a volume cap on each new bundle until its first audit window closes.

## A3
Winner: Designer
Why: Every real compliance process has a residual error rate; the design's figure is a 95% upper bound on undetected harm paired with rollback on breach (R66), fallback for states that can't meet it (R2), the post-call DNC sweep before any redial and R132 audit surges, which is the written-procedures-plus-correction posture the DNC safe harbor and good-faith analysis reward. The documents show active detection and remediation, not a priced decision to violate.
Worth adding: Present the figure as "maximum undetected rate, target zero", keep a remediation record for every detected Tier A event, and give every open item an owner, deadline and interim control.

## A4
Winner: Breaker
Why: R79 does keep the graph, fragments and policy table out of the blast radius, but Needle's weights are trained on the union of seeds, big-model paraphrases derived from them and real calls, and nothing in the existing design records which training items descend from which source. R7's "deletion = data operation" covers gold sets, not weights; R129's lineage check guards eval contamination, not provenance; R40's consent flag does not catch consent that was defective at the source. Certificates are keyed on the weights hash (R53), so a forced deletion wipes the certified runtime with no way to prove a retrained release is clean; the defense's lineage ledger, taint drill and clean-room model are all new.
Fix needed: Add a training-data lineage ledger (every item, real or synthetic, carries source id, consent-artifact id and parent seed hashes; every release manifest lists its item-hash set), a per-release taint drill that drops one source plus its transitive closure, retrains and replays gold sets within a set time, and a standby clean-room Needle trained only on first-party consented on-policy calls, with certification evidence kept only from those calls.

## A5
Winner: Breaker
Why: The existing hooks are adjacent but do not cover this: R122 is a per-state telemarketer registration row, R162 suspends partners on fraud metrics rather than legal orders, and R18's sign-off is internal with no outside approver. Nothing in the design can express "this seller, by order" terms such as an age ban (which the data-minimised lead record can't even evaluate), monitor pre-approval of releases, or screening of vendors under their own bans; the defense itself names the order row type and outside signer as the gap and supplies them only as new hardening.
Fix needed: Add party-scoped obligation_order rows (seller, vendor, principal, successor) whose terms compile into pre-dial predicates, lints and retention rules under most-restrictive-wins; make the release pipeline require a monitor's signing key whenever an active order demands pre-approval; screen vendors and principals against FTC/AG orders at onboarding and weekly, check each lead's source id at dial, and fail closed on age-limited orders when record-sourced DOB is missing.

## A6
Winner: Designer
Why: The premise that the seller holds only a flag is false: R74 requires a per-number PEWC artifact (timestamp, seller, disclosure version) before any dial, and R116 keeps that consent artifact in seller-controlled WORM storage for 5+ years, joined to each call's CDR, which outlasts the 4-year federal limitations period. R117's legal hold freezes deletion once a dispute appears, and R162 adds an independent consent-capture provider.
Worth adding: Copy the full evidence package (rendered form, disclosure text hash, phone as entered, IP, user agent, session replay) into seller WORM at ingestion, reject pointer-only consent at the gate, and store the consent-artifact hash on each CDR.

## A7
Winner: Designer
Why: Pieces was penalised for misstating a metric's basis; this design is built to state it, publishing only the family-wise corrected claim (R126), stating coverage gaps in the certification report (R113), correcting group estimates with a measured confusion matrix (R131) and producing manifests, budgets and drift monitors per release that answer a TRAIGA-style CID. The scenario's "99.999% compliant" deck line is a governance misuse the design never authorises, and the banned-claims lint keeps such claims out of the agent's speech.
Worth adding: An external-claims policy requiring any outside quotation of the metric to carry its exact definition, strata, exclusions and open items, with legal review and a ban on "X% compliant" phrasing.

## A8
Winner: Designer
Why: The existing design does not rely on CRM-only labels: R163 already sources outcomes first from independent AG/CFPB/BBB complaint feeds, lender disputes and surveys that override CRM fields, R59 monitors spam labels per number (the carrier and blocking-app signal), and R132's label-free monitors flag a bad branch without any complaint. Sentinel is closed to companies for everyone, and R117 already routes complaint and demand channels into legal hold.
Worth adding: Feed served FCC informal complaints, ITG traceback notices and carrier blocking reports into the R115 intake bus, match them to sessions by number and time, and count each match as a Tier A candidate that triggers an audit surge.

## A9
Winner: Designer
Why: The texts are transactional responses to the caller's own on-call choice, not uninvited marketing: R120 asks the channel question before CONTRACT_SENT, R149 puts every outbound SMS through the consent gate, and R89 sends from a registered short code. The scenario's harm (deals stranded, opt-out confirmations stopped) is blunted by R120's paper and consultant-assisted signing path, R55's timeout/error handlers on every effect and R84's email and print-and-mail DNC-policy delivery. The defense's citation of R122 as an SMS registration control is a stretch (that row is state telemarketer registration), but the rest stands.
Worth adding: Separate 10DLC/short-code campaigns per use case with CTIA-linted certified SMS templates, a use-case tag checked against campaign id, and a sender-health monitor that fails WAITING_FOR_SIGNATURE over to email and mail.

## A10
Winner: Designer
Why: Routine, documented, pre-dispute deletion is not spoliation; the duty starts when litigation is reasonably anticipated, and R117's legal hold then freezes every deletion and keeps original audio and transcript, firing on complaint channels, mid-call threats and the post-call sweep. Because ASR and weights are pinned and bundles immutable (R53, R67, R68), retained audio regenerates every confidence, softmax and margin bit-identically, and speculative branches provably cannot affect committed traces (R64). The payment redactor (R45) implements a legal duty not to retain card data.
Worth adding: A compact per-turn decision record (ASR n-best and confidences, pre-gate scores, top-k scores and margin, mask/threshold version, lexicon hits) kept with the R116 set so decisions stay explainable after raw-audio TTL, plus redaction span logs.
