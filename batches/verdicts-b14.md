# Verdicts b14

## A1
Winner: Designer
Why: The existing design blocks the interpreted close at several points that are really in design.md. R112 requires the committing voice to match the VERIFIED speaker's diarization id. R148 means no close on any second voice during QUALIFY/READ_BACK/COMMIT, so Mrs. Tran's Vietnamese on speaker blocks the close. R144 requires an action phrase plus a teach-back. For an 82-year-old, R148's human owner-only call before install would expose that the owner never understood the deal. The residual case is a grandson who answers IDENTITY himself and interprets off-mic. That is impersonation more than interpretation, and R123's per-signer ID verification and the human call still stand in front of install.
Worth adding: An interpreting lexicon ("I'm translating", "let me tell her") and an audio language-ID on near-end segments that set negotiation_language=mixed, so the call gets no English close and goes to an in-language human with a professional interpreter.

## A2
Winner: Designer
Why: R144 turned the commit into an action-production prompt ("say 'send the contract'"), so a misheard "ya ya ya" or "ne, ne" can't commit anything. R24 treats a bare "no" as Tier 2 at most: one check question, then a polite end. A false stop costs a sale but doesn't harm the caller. R77's per-dialect discourse-marker certification and R16's mixed counter already exist.
Worth adding: A false-friend particle table (Polish/Czech "no", Greek "ne", Spanish "ya") that feeds the mixed counter, plus a Tier A L1 false-friend red-team stratum.

## A3
Winner: Breaker
Why: The live stop lexicon, Needle GLOBAL and the R66 post-call sweep all run on the same English ASR text. A garbled "ya no me llamen" is missed in both places, and R16 itself lists "English-only ASR anglicizing speech" as open. The defender overstates the existing backstops. R113's "unresolved unclear suppresses" applies only to the NO_RETAIN stratum. R147 sends the number to a human on next contact, and that is still a redial after a company-specific DNC request. The defense rests mainly on its NEW multilingual ASR and lexicon.
Fix needed: Run an audio spoken-language-ID on every near-end segment. Any non-English or low-confidence turn gets a multilingual ASR second pass checked against a stop/revocation lexicon in the service area's top languages, both live and in the post-call sweep. Any non-English turn the system can't resolve sets suppress-pending (no redial of any kind) until a human reviews the audio. Add a Tier A foreign-language revocation red-team stratum.
Worth adding: Count a mid-call bilingual handoff after a non-English turn as a possible revocation until the receiving human or build confirms otherwise.

## A4
Winner: Designer
Why: One of the defender's claims is wrong: R106 measures network audio delay from RTCP and echo lag, not caption-service lag, so it does not see CapTel delay. The decisive layers do exist and hold. R144 means a late "yes" on the wrong question id can't commit, because the commit needs the spoken phrase "send the contract". R15's teach-back has the customer state the payment and term while code compares them, so a mis-captioned figure she believes produces a mismatch rather than a signed wrong deal. R148's human call and R141's mailed summary sit before install.
Worth adding: A CAPTION_MODE profile, triggered by mentions of captions or a caption phone or by a DTMF key: long answer windows, one question in flight, numbers also sent by SMS, and no same-call close.

## A5
Winner: Designer
Why: The stated break, that a bluffer's clean "yeah"s pass the gate, is false against the existing design. R144 requires an action phrase and forces a delayed teach-back after 3+ consecutive bare affirms. R15's teach-back makes the caller state payment and term, which someone who didn't hear can't do. R148 adds a human call for this 80-year-old before install. R48's repair_request does exist. The defender rightly concedes that its repeat variants are not slower or louder, but that is an accessibility-quality gap, not a path to a harmful contract.
Worth adding: repair_request kind ∈ {rate, volume} switches to a pre-rendered, round-trip-checked ACCESSIBLE_AUDIO profile (about 0.75x, louder, shorter chunks). A second such repair means no same-call close and a human consult with extra time.

## A6
Winner: Designer
Why: Under R144 the binary re-ask no longer decides the commit. A recency-biased "yes" is not the action phrase, and the close still needs R15's teach-back, where a number has to be produced, which echolalia can't supply. R15's counter also takes unclear answers and contradictions toward NO_SALE_SAFE_EXIT, and R144's "consent understood" audit label would count such closes as harm. The Breaker missed the sharper variant: R144's prompt ends with the commit phrase itself, which an echolalic caller would repeat. The teach-back still stands behind it.
Worth adding: Lint so that every closed re-ask ends on the safe option ("..., or not?") and the commit phrase is never the final words of its prompt. A commit-turn answer that echoes the prompt's final words doesn't count and adds to the confused counter.

## A7
Winner: Breaker
Why: R88 does name "capacity flags (conservatorship/trust/POA) from records and lender checks". But the records the design actually sources are title/record-owner and lender data, which normally don't carry probate conservatorship or guardianship orders, and the defender concedes this residual gap. So a lucid conservatee alone on the line passes IDENTITY, READ_BACK, COMMIT and R148's "anyone else asking you?" call, and signs a void or voidable contract. The POA daughter is stopped from closing by R112/R148, but an authority claim has no event, so the agent has no defined path for it. The defense for the main scenario rests on the NEW probate-index search.
Fix needed: Before the envelope, run a court-records (probate conservatorship/guardianship index) search through a vendor for every record owner; a hit suppresses sales and routes to human review. Add an authority_claim(POA|conservator|guardian) GLOBAL subtype with a lexicon: no pitch and no close, routed to an AUTHORITY_REVIEW human path that verifies the instrument. The agent never resumes selling to the principal on that call.

## A8
Winner: Designer
Why: R15 already sets the "longest statutory cancellation window (CA 65+ 5 business days) for all", and the final plan has install wait out the longest window. READ_BACK can therefore state five business days to every CA buyer without knowing anyone's age, and R46's prohibited-basis tags bar age as an input. The one real inconsistency is R148's "owners 65+" trigger, which implies an age source. The defender removes it.
Worth adding: Make R148's owner-only confirmation call universal (or key it to non-age signals), and lint that no fragment or contract template states a shorter window than the max-across-profiles policy row.

## A9
Winner: Breaker
Why: R85's READ_BACK list (total cost, escalator, material restrictions, cancellation, lien/UCC, financing) has no invariant tying it to the actual e-sign template. Arbitration, class-action waiver, assignment and data-sharing clauses can sit in the binding document without ever being spoken. R120's paper or consultant signing triggers only on a stated access need, which low-literacy buyers rarely state. The defender concedes the gap and closes it with a NEW clause-coverage invariant.
Fix needed: Give every clause of the e-sign template a policy-table key tagged material or not. A build invariant requires every material key (arbitration and opt-out, class waiver, assignment plus the FTC Holder Rule notice, credit-pull authorization, data sharing) to have a plain-language READ_BACK fragment. A template with an untagged clause, or a mismatch between the template version and the READ_BACK version, fails the release. The mailed summary repeats these clauses.

## A10
Winner: Designer
Why: R15 really does define defers_decision(to) as a Needle signal leading to NO_SALE_SAFE_EXIT: "no close reachable, suppress redial, decision-maker-only follow-up". "My son handles these things" is the core case, so the graph can't go on to ask about the roof. R56 gives a booked human consult with a written proposal. R74 and R213 keep the son from being cold-contacted without the owner's written choice.
Worth adding: A SUPPORT_PERSON path: a fixed fragment that honours the request, then a human consult booked at a time she names with support_person_expected set. The son gets the NEW_PARTY disclosure, no AI close is allowed, and the son is contacted only on her written opt-in.
