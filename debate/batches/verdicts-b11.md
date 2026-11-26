# Verdicts b11

Note on citations: the Designer's R-numbers in this batch are mostly shifted by about three from design.md. Survey contingency is R159, not R156. Independent-source identity and the phone-to-record-owner match are R162, not R159. The co-owner envelope rule is R149, not R146. Independent per-signer contact and verification is R123, not R120. The partial-match name rule is R146, not R143. Usage authorization is R156, not R153. Exact tariff is R157, not R154. I checked each claim against the content in design.md rather than the label. Every cited mechanism exists, but under the corrected number.

## A1
Winner: Breaker
Why: Nothing in the design asks about HOA, CC&R or common-element governance, and the Designer concedes this. R159's survey contingency covers price changes found by a physical survey; it does not cover a board's approval, insurance or removal-for-reroof conditions. R83's material limitations are product limits, not title or governance limits. The claim that R88's record-owner lookup returns the association parcel is wrong for a townhouse unit, whose parcel names the unit owner. The contract, financing and lien can therefore be signed on a roof the buyer cannot authorize.
Fix needed: Add a governance slot sourced from county parcel data (common-interest development or recorded CC&R flag), plus one neutral QUALIFY question. An HOA or common-element roof goes to an HOA_APPROVAL_FIRST suitability row: no price and no close on the call, lead-gen plus a written proposal. Where a close is allowed, a policy-table row "association approval required; may impose insurance, maintenance and removal duties" is mandatory in READ_BACK and the contract, with a no-penalty cancel on denial or conditions. Install is blocked until written approval is on file.

## A2
Winner: Breaker
Why: Ownership is still a single boolean. The Designer's defense depends on the county parcel naming the park owner so that the R162 phone-to-record-owner match fails, but many manufactured homes appear on assessor or HCD records under the homeowner. In that case the match can succeed and the call closes. The certified lien/UCC READ_BACK fragment would then describe a real-property or fixture security interest that is legally wrong for chattel collateral. Park-landlord consent and HUD-code roof load are also unmodeled, and the Designer concedes the lien fragment is not keyed to collateral type.
Fix needed: Add a structure_type slot from the parcel use code and the state manufactured-housing title registry (HCD in CA), never from speech. Manufactured, chattel-titled or land-lease homes go to NOT_SUITABLE for the residential product row (honest exit plus referral) or to human review. Make the lien/UCC READ_BACK fragment a policy-table key per collateral type, chosen only by the lender's stated security instrument. Add a HUD-code roof-load row.

## A3
Winner: Designer
Why: R88 explicitly routes "capacity flags (conservatorship/trust/POA) from records and lender checks -> human review path", so a trust-titled property never gets an automatic envelope. R123 blocks any lien or install until every owner is independently verified with per-signer ID. A deceased co-trustee cannot pass that check, so a lien signed in the wrong capacity cannot file.
Worth adding: Run the deceased-list check against every record owner on title, and have the human path obtain a certification of trust with "as trustee" signature blocks for the current trustees.

## A4
Winner: Designer
Why: Title still names the deceased parent. Under R162 the caller fails the independent-source identity and phone-to-record-owner match, so the call becomes lead-gen only. R123 blocks any lien until every record owner is independently verified, which a decedent cannot do. The lexicon pre-emption for sensitive_event(bereavement) is a likely extra stop, but the design does not depend on it.
Worth adding: Add an estate/probate lexicon and event that blocks quote and close, and suppress properties with a deceased record owner from sales campaigns until title transfers.

## A5
Winner: Designer
Why: The core harm, one spouse encumbering without the other's consent, is blocked by existing rules. R149 bars envelopes to vendor-sourced contact data, and R123 requires independently sourced contact data, no shared phone between signers, and per-signer ID verification for any lien. R162 adds lender-grade ID for each record owner. A lien therefore needs the estranged spouse's own verified signature, which is the written consent Fam. Code 2040 asks for. The hidden forced sale is a caller-honesty issue no qualifying script can fully close.
Worth adding: Ask one neutral QUALIFY question about any expected ownership change (sale, refinance, divorce, estate), and have the lender's title pull check for a lis pendens or family-law filing before the lien.

## A6
Winner: Breaker
Why: The design has no owner-occupancy or bill-payer slot, and the Designer concedes this. R156 routes an account-holder vs record-owner mismatch to a written-authorization path, so a tenant-authorized usage record can still become "verified_usage". The savings it produces would be told to a landlord who does not pay that bill. The certified consumer framing (home-solicitation cancel, TILA-style financing read-back) is also spoken to a business-purpose buyer, even though the lender decides the credit purpose.
Fix needed: Add an owner_occupied slot: one QUALIFY question cross-checked against homestead-exemption and mailing-address records, with disagreement going to clarify and then a human. Non-owner-occupied goes to NOT_SUITABLE for the consumer product, with referral to a human commercial desk. Any savings figure requires bill_payer equal to a signing record owner, else no figure. Add an invariant that consumer-credit and home-solicitation fragments are reachable only when owner_occupied is verified.

## A7
Winner: Designer
Why: The attack assumes the system is sized to the whole roof, but R61 already says "savings/sizing figures only from verified bill or usage data". R157 requires the exact tariff on verified interval data from the authorized account, else no figure. Sizing, tariff and savings therefore all key to the one meter that was authorized, and they stay consistent with that meter's interconnection. R159's survey contingency turns any second-service or interconnection change into a re-disclosed change order with a no-penalty exit.
Worth adding: Add a unit_count slot from the parcel use code and a service-point list from the utility API, and have READ_BACK name the meter the system ties into.

## A8
Winner: Designer
Why: The R73 challenge-response matches the stated address against the record, and R146 sends partial matches to clarify or a human. If wrong-house answers still get through, R79's aerial shade lookup is a calculator input. R159 schedules the physical survey inside the cancellation window, with roof-structure slots, a no-penalty exit and install blocked until it finishes. A 25-year roof under pines is therefore caught before install, and the Breaker's stated harm (install on an unsuitable roof) does not occur. The missing property referent in QUALIFY and READ_BACK is a real quality gap, but it is not an unguarded harm.
Worth adding: Put the validated street slot into QUALIFY fragments and require the property address in READ_BACK by lint. Cross-check roof age against permit records, with any disagreement going to ROOF_FIRST.

## A9
Winner: Designer
Why: The core harm is residential-rate savings on an agricultural account. R157 blocks it: the calculator must use "the customer's exact tariff schedule ... on verified interval data, else no figure", and R72 requires a calculator_output with a substantiation id. An LLC record owner fails the R162 record-owner match, which makes the call lead-gen only. A ground mount becomes an R159 survey change order.
Worth adding: Add an explicit tariff_class key on calculator rows from the utility API. Any non-residential class goes to NOT_SUITABLE for the residential product, and entity owners go to human review with no same-call close.

## A10
Winner: Designer
Why: Both harms are blocked by existing rules. R149 forbids any co-owner envelope to vendor-sourced contact data, so the seller-vendor is never sent an SMS without the occupants' own choice. Because the occupants are not record owners, the R162 pre-dial phone-to-record-owner match fails and the call becomes lead-gen only. R123 also blocks any lien until every record owner is independently verified.
Worth adding: Add an OWNERSHIP_MISMATCH state with one fixed question and an honest written explanation, plus a land-contract lexicon that leads to NOT_SUITABLE with a note to check the contract's alteration and lien clauses.
