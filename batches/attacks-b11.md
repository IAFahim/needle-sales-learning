## A1
TOPIC: Condo/HOA owner "owns" the home but the roof is association common area needing board approval, insurance and roof-removal duties
SCENARIO: Agent calls a townhouse owner in an HOA. QUALIFY asks "Do you own your home?" ("Yes"), roof age ("about 10"), shade ("none"). The suitability table passes, QUOTE runs, READ_BACK covers price, warranties, lien and cancellation, and the owner says "yes" and signs. The roof is a common element. The board takes months, attaches removal-for-reroof and liability-insurance conditions, or turns down the requested placement. The signed contract, financing and lien sit on a system that may never be installed as sold.
WHY IT BREAKS: Ownership and roof age are the only title-type inputs. The design has no HOA, CC&R or common-area slot and no approval-contingency fragment. Cal. Civ. Code 714.1 and 4746 let associations require approval, insurance, maintenance and removal for repairs on shared roofs. Those are material limitations the READ_BACK never states. Sources: california.public.law/codes/civil_code_section_4746, codes.findlaw.com/ca/civil-code/civ-sect-714-1

## A2
TOPIC: Manufactured/mobile home on a leased park lot: chattel title, no land ownership, wrong lien instrument
SCENARIO: The lead record shows a residential address. The caller says "Yes, I own it." They own a manufactured home in a land-lease park. QUALIFY records ownership, roof age and shade, and the suitability table passes. READ_BACK recites a "lien/UCC" on the property. The home is titled as personal property (in California through HCD, not the county), the park owner controls roof additions and the lot, and the lender's real-property lien or fixture filing does not attach.
WHY IT BREAKS: "Ownership" is one boolean. Nothing separates the structure from the land or real property from a chattel-titled home, and the park landlord's consent is not modeled. The read-back's lien/UCC disclosure is certified as one fragment, so it describes a security interest that is legally wrong for this collateral. Roof-load limits on HUD-code homes are not in the suitability table either.

## A3
TOPIC: Home held in a revocable living trust: record owner is a trustee capacity, not a person with a phone
SCENARIO: Title reads "Jane Doe and John Doe, Trustees of the Doe Family Trust." Jane answers, passes the identity challenge and says "We own it." John died last year, and their adult son is now successor co-trustee. The "all record owners" step fans out e-sign envelopes to the people on the lead record, Jane and the late John, by SMS. Jane signs as an individual, not as trustee, and the son is never contacted.
WHY IT BREAKS: "Record owners + lender signers" assumes owners are natural persons with phone numbers. The design has no trust, trustee-capacity or successor-trustee slot and no check of who currently holds signing power. A contract or lien signed in the wrong capacity can be unenforceable or a cloud on title. The deceased-list check covers the dialed lead, not a dead co-trustee on title.

## A4
TOPIC: Executor or heir in a probate estate encumbering a decedent's house without court or beneficiary authority
SCENARIO: The adult child living in the late parent's house answers. They say, matter-of-factly, "Mom passed last year, I'm the executor, it's basically mine." Nothing distressing is said, so sensitive_event never fires. The challenge-response matches the household, and QUALIFY records "owner." QUOTE, READ_BACK and COMMIT proceed, and an e-sign envelope with a financed lien goes to the executor.
WHY IT BREAKS: The design has no estate or probate state. Under California's independent administration, encumbering estate real property needs Notice of Proposed Action to the heirs (Prob. Code 10510 ff.), and without such authority it needs court approval. Heirs can void or contest the lien, and the "installed, no complaint" success label fires anyway. Source: law.justia.com/codes/california/2009/prob/10510-10520.html

## A5
TOPIC: Pending divorce: automatic restraining orders forbid encumbering the home, and the "move horizon" answer hides a court-ordered sale
SCENARIO: One spouse on title answers mid-divorce. The other spouse lives elsewhere. The caller wants the house "improved" before the property split and says "I'm staying put." They pass identity, and the e-sign SMS goes to both record owners. The estranged spouse's phone number on the lead record is stale, so a number the caller controls receives it. The caller signs both envelopes, and a financed lien is recorded.
WHY IT BREAKS: California Family Code 2040 automatic temporary restraining orders (ATROs) bar either party from "encumbering" any property without the other's written consent or a court order once a petition is served. The design has no marital-status or pending-dissolution slot. Move horizon is self-reported, and a forced sale makes the honest answer different from the one given.

## A6
TOPIC: Non-owner-occupied rental: tenant pays the electric bill, so certified savings go to someone else, and the loan stops being consumer credit
SCENARIO: A landlord is called about a single-family rental listed in the lead record. They own it, the roof is new, and there is no shade, so the suitability table passes. The savings fragment uses "verified usage" from the tenant's utility account. READ_BACK recites Reg Z financing terms and senior/home-solicitation cancellation rights. The landlord signs.
WHY IT BREAKS: The design never asks who pays the utility bill or whether the owner lives there. The savings claim is substantiated against an account the buyer doesn't pay, which is deceptive as to that buyer. Credit to improve non-owner-occupied rental property counts as business purpose (Reg Z 12 CFR 1026.3(a), Comment 3(a)-5). The certified TILA disclosures and cancellation statements then misstate the buyer's rights.

## A7
TOPIC: Duplex/triplex with separate meters: system sized and priced on one unit's usage, interconnected to one meter
SCENARIO: An owner-occupant of a duplex qualifies. "Verified usage" pulls the owner's own meter. The calculator sizes the system to the whole roof, and the savings fragment states savings for that system. The roof covers both units, which have separate meters and a house meter. Net metering credits only the meter the system ties into. The quoted savings assume a usage profile that one meter doesn't have, and splitting the credit needs a different tariff and interconnection.
WHY IT BREAKS: The slot store has one usage value and one meter. The calculator, the policy table and the certified savings fragment assume one dwelling with one service. No QUALIFY question asks unit count or meter count. Duplexes look like single-family homes in lead data, so the calculator output is certified and substantiated yet wrong for the building.

## A8
TOPIC: Owner of several properties answers qualifying questions about the house they're in while the contract binds the lead-record address
SCENARIO: The lead record is a lake house. The owner answers on their mobile from their primary home. "Roof age?" "Replaced 2019" (the primary home). "Shade?" "None" (the primary home). "Planning to move?" "No." Every answer passes the argument grounding gate because the owner really said it. The quote, read-back address and lien all point to the lake house, which has a 25-year-old roof under heavy pines.
WHY IT BREAKS: Slots carry provenance (spoken) but not referent: which property the speaker means. The read-back never states the property address before COMMIT, and no fragment ties QUALIFY answers to an address. Suitability is satisfied by true statements about the wrong house. This defeats the success metric's own suitability audit only after installation.

## A9
TOPIC: Farmhouse on a shared agricultural meter: "verified usage" includes irrigation pumps and barns on a farm tariff
SCENARIO: A farm family's residence and barns share one agricultural service. Utility data authorizes fine, and usage comes back huge in summer. The calculator sizes a large residential system and the certified savings fragment quotes big savings at residential rates. The account is on an ag time-of-use tariff, the property may be owned by the family's farm LLC, and the system may need a ground mount on cropland.
WHY IT BREAKS: Verified usage is trusted because of its provenance, not checked for what it measures. The policy table has no tariff-class key, so residential rate assumptions apply to an ag tariff. Entity ownership (LLC or partnership), ground-mount siting and the meter's mixed business load fall outside the residential suitability table, yet the substantiation id still validates the claim.

## A10
TOPIC: Contract-for-deed (land installment) buyer: occupant believes they own it, while legal title and the e-sign recipient are a third-party seller
SCENARIO: A family bought their house on a land contract eight years ago. They say "We own it, we pay the mortgage." The suitability table's "record owners" lookup returns the seller-vendor. The design sends e-sign envelopes to "all record owners," so the seller gets an SMS about the buyers' solar deal and loan. Or the seller ignores it, the deal stalls, and the occupants have already made commitments.
WHY IT BREAKS: The design assumes speaker ownership plus record owners equals the buyers. It has no equitable-versus-legal title state, so it either discloses the occupants' financial dealings to a stranger or encumbers property the occupants can't encumber. Many land contracts make new liens or alterations a default, which risks forfeiture of years of equity.
