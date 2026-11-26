## A1
Winner: Designer
Why: The attack misreads the statute. Cal. PUC 2873 lets an ADAD run "pursuant to a prior agreement ... whereby the person called has agreed ... to receive such calls ... or as specified in Section 2874", so prior consent and the 2874 live intro are alternative paths, and 2872(f) excludes non-random dialing to people who asked for the call. The existing R8/R74/R197 per-number written-consent gate (no random or sequential dialing) already puts these calls on the consent path, and Indiana and Illinois also allow consented recorded messages. The Designer's admission that an ADAD row is missing doesn't change the outcome on the law.
Worth adding: An explicit adad_rule row per profile that records the consent-path basis (PUC 2873 / 2872(f)) and blocks dialing where consent is missing or a layer has no consent alternative, rather than adding a human live-intro operator.

## A2
Winner: Breaker
Why: 47 CFR 64.1200(b)(2) requires every artificial or prerecorded voice message to state a callback number other than the dialer's, during or after the message, on every call. The existing design gives the number only on request (R84), through caller ID, or at consent capture (R259), and none of those satisfies the per-call spoken duty. R75's profile-segment mechanism is real, but the segment is absent, and the defense says so.
Fix needed: Add a callback_number policy key: a staffed line, not the dialed ANI, that accepts DNC requests and is live-tested daily. Make it a profile-mandated preamble segment (counted only on uninterrupted playback) and repeat it in every agent-initiated END fragment. Add a model-checked invariant that no path from DISCLOSED reaches an agent hang-up without a playout mark on it, proven per call through the R116 render log.

## A3
Winner: Designer
Why: Social proof can only be an audited aggregate policy-table fact with a substantiation id (R92), any quantifier needs a table key (R199), and counsel judges net impression through the path book (R326). Under FTC substantiation doctrine a survivorship-filtered sample doesn't substantiate "9 in 10 of our customers", so the scenario needs the audit itself to fail. Also, R163's post-install survey is a labeling feed, and the design names no satisfaction row. R222's attestation covers warranty and terms rows, not social proof, so citing it overstates the defense, but the remaining controls are enough.
Worth adding: A typed sampling_frame on every review or satisfaction aggregate, with a build check that rejects frames filtered on outcome, satisfaction or complaint status (it must be all signed contracts, cancelled included, with the response rate stated).

## A4
Winner: Breaker
Why: R242 lists the Holder notice as a material clause of the seller's e-sign template, but nothing checks that the lender's own credit contract carries the verbatim 16 CFR 433.2 notice. Nothing bans a recovery-cap clause either, which the FTC's 2022 advisory opinion calls unlawful. R217 admits lender programs on draw-schedule grounds only, and R154 checks amounts, not clauses. So the seller can accept loan proceeds under a defective lender form, and the defense concedes the cap gap.
Fix needed: Hash each admitted lender loan-document version into the bundle. Admit a lender program only if the verbatim 433.2 notice is present and no recovery-cap pattern appears (extend the R222 lint to lender docs). At runtime, refuse CONTRACT_SENT and accept no milestone funding unless the lender envelope's document hash matches an admitted version.

## A5
Winner: Designer
Why: The overnight soft-pull path contradicts the design. R225 makes the soft pull customer-initiated on a lender-hosted page, R7 holds no credit data, and R90 accepts a credit band only with lender-prequal provenance, so the agent never selects or pitches on credit. Leads are PEWC opt-in leads with per-lead source ids (R268) and vendor attestations (R246), so any prescreen exposure from a vendor's credit-filtered segment is a sourcing-contract matter, not something the call path creates.
Worth adding: A required selection_criteria field on each lead-source attestation that rejects any credit-derived criterion, plus a build check that no pre-dial job calls a bureau or lender API.

## A6
Winner: Designer
Why: The design has no in-call second-seller sale. ROOF_FIRST is "inspection before any quote" (R71), warm transfers go to the seller's own staffed queue (R56/R333), third-party battery programs are post-PTO outbox enrollments on the program's own terms (R318), recurring services are barred from voice (R321), and no payment data exists to pass on (R45). Partner data flows are gated by R253, R251 and R203. The "lead-gen warm transfer to a partner" gap the defense concedes isn't a path in the design.
Worth adding: A model-checked invariant that no effect whose counterparty differs from the preamble seller can fire during a live call without a compiled seller-change disclosure and a lexical affirm.

## A7
Winner: Designer
Why: The scenario's content violations can't render. SMS templates are certified with a lint against promotional wording (R272), the drain re-reads the revocation ledger and drops every marketing intent in a stop turn (R342), and sends are deduplicated (R196) and windowed (R261). Under the FCC's revocation order, a confirmation sent after five minutes isn't per se unlawful (the sender must show the delay was reasonable), and a DNC policy the caller asked for isn't an unsolicited message.
Worth adding: A dedicated revocation_confirmation template with not_after = revocation time + 5 minutes, top priority class, dropped rather than sent late, and one per revocation.

## A8
Winner: Breaker
Why: R8 checks seller, AI/artificial voice and not-a-condition, and it names "state mini-TCPA rules as facts rows", but nothing compares the stored disclosure text (R269 hash) with each state's required consent elements. Florida's FTSA defines consent by authorization of an "automated system ... or the playing of a recorded message", and a consent naming only "AI voice" may not meet that. The defense concedes the per-state element check is missing, and the FTSA carries a $500-per-call private right of action.
Fix needed: Add consent_form_element rows to each profile layer (FL 501.059 technology wording, authorized number, not-a-condition, and the OK and MD analogues). Have a counsel-maintained registry classify each consent disclosure-text hash against every layer's elements, and make the R138 dial permit require the hash to be approved for every candidate jurisdiction (unknown hash = no dial).

## A9
Winner: Breaker
Why: R85 and R309 make the total all-in at READ_BACK and in the contract, but nothing controls which price figure is spoken first in QUOTE. Nothing prevents a monthly or per-watt figure before the total, or mandatory fees that appear only in the envelope. Massachusetts 940 CMR 38 requires the total with mandatory fees whenever a price is first presented, and the defense concedes no lint or invariant constrains this ordering.
Fix needed: Type fee rows as mandatory or optional, and add a calculator build check that folds every mandatory fee into total_price (nothing mandatory may appear only in the envelope). Add a fragment-sequence invariant that the first price-typed fill in any call is total_price, with monthly figures allowed only inside the same fragment, and ban per-watt keys from voice in every profile.

## A10
Winner: Breaker
Why: GBL 349-a defines personalized algorithmic pricing very broadly: "pricing that fluctuates dependent on conditions" set by "a computational automated process that uses a set of rules", using data "reasonably linked" to a consumer. Its express carve-out for rideshare mileage pricing shows that rule-based calculators fall inside it otherwise. The calculator total depends on this household's usage, roof geometry and rooftop tax address (R230, R309), so even a fixed per-configuration price table (R46) doesn't keep the total outside the statute. No fragment carries the disclosure, and certificates expire only on a cited row change, not on a new statute. The GLBA exemption reaches only financing activity.
Fix needed: Add an algorithmic_pricing_disclosure key with the verbatim statutory text to the NY layer, with a co-occurrence lint that places it in the same fragment as every calculator_output price fill, spoken and written. Add a legislative-change monitor with an attestation effective_until date per profile layer, so a new statute or a lapsed re-attestation drops the layer to lead-gen (no price) until counsel re-attests.
