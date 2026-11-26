I went back through all 400 rounds (numbered 1 to 100 and 104 to 403) and pulled out every state a call can be in. There are **96 states**, in **9 groups**, from before the phone rings to after the system is switched on.

This list has states only. It has no transitions, no connections and no choice of model, because those come later. Nothing here changes the plan doc.

## How sure I am

- **Very sure, about 95%,** that the main stages are all here: before the call, pickup, the opening, the sale talk, the close, the ending and after the call. Every round I read lands in at least one of them.
- **Fairly sure, about 80%,** about the groups "What's happening on the line" and "What the person really means". The rounds kept finding new variations there, so more will turn up.
- **Least sure, about 70%,** about "After the call". The rounds only reached those states when something went wrong, so ordinary steps like a reminder or an inspection may be missing.
- The rounds were attacks, so they over-sample things going wrong and under-sample calls that go smoothly.
- I worked from each round's attack summary, so a few rounds may hold a state I didn't catch.

## One thing worth knowing for later

The groups aren't all the same kind of thing. Some say where the conversation is, like Quote. Some say what's happening on the line right now, like Bad line. Some say what the person really means, which can't be heard directly. A call can be in one of each at the same moment, for example Quote, Bad line and Polite yes. I haven't decided what that means for the model. It's noted here so it isn't lost.

## Before the call (7)

The call doesn't exist yet. The lead waits to be dialed, or is stopped from being dialed.

| State | What it means | Shows up in |
|---|---|---|
| Lead on file | A lead record exists with a name, number and address, which may be wrong or faked. | Round 162, Round 362 |
| Dial check | The pre-dial gate checks consent, do-not-call lists, calling hours and registration. | Round 114, Round 391 |
| Held back | The lead may not be dialed right now: do-not-call, emergency pause, or consent withdrawn elsewhere. | Round 78, Round 115 |
| Waiting for a set time | A callback or a later attempt is queued for a time the person named. | Round 41, Round 305 |
| Dialing | The number is ringing, often for the 10th or 15th attempt on the same person. | Round 262, Round 142 |
| No answer | Nobody picked up. | Round 262 |
| Labeled as spam | The carrier or the phone marks the call as spam or blocks it before anyone hears it. | Round 259, Round 59 |

## Pickup (9)

Something answered. It isn't yet clear what, or who.

| State | What it means | Shows up in |
|---|---|---|
| Silent pickup | The line opened but nobody speaks yet. | Round 65, Round 109 |
| Voicemail | An answering machine or voicemail greeting picked up. | Round 35 |
| Screening assistant | The phone's own call-screening assistant answers and the owner reads along. | Round 351, Round 9 |
| A bot answers | Another AI, such as a scam-baiter or a bot farm, is on the other end. | Round 69, Round 202 |
| Relay or captions | A relay operator or a captioned phone sits between the agent and the person. | Round 42, Round 237 |
| One-way audio | The agent is talking into a dead line and the person hears nothing. | Round 107 |
| Already talking | The person starts talking as they lift the handset. | Round 347 |
| A business answers | The number reaches a business, not a home. | Round 350 |
| Inbound call | The person called in, so the call starts from their side. | Round 195, Round 305 |

## Opening and who's there (8)

The agent says who it is and finds out who it's speaking with.

| State | What it means | Shows up in |
|---|---|---|
| Disclosures playing | The fixed opening plays: company, purpose, that it's an AI, recording and how to opt out. | Round 344, Round 385 |
| Identity check | The agent confirms it's speaking with the owner named on the lead. | Round 171, Round 146 |
| Wrong person | Someone else answered: a child, a tenant, or a new owner of a reassigned number. | Round 348, Round 73 |
| Owner not here | The right person isn't available, or says someone else handles these things. | Round 243 |
| Owner has died | An heir or executor answers for an owner who has died. | Round 176, Round 207 |
| Someone speaks for the owner | An interpreter, relative or caregiver is talking on the owner's behalf. | Round 234, Round 303 |
| New person joins | Another person picks up an extension or is merged in partway through. | Round 112 |
| Talking to someone in the room | The person turns away to speak to a spouse or child, not to the agent. | Round 24, Round 349 |

## Talking about the sale (18)

The middle of the call, where the agent learns about the home and makes an offer.

| State | What it means | Shows up in |
|---|---|---|
| Small talk | Friendly chat before or between business. | Round 167, Round 293 |
| Discovery | The agent asks what got them thinking about their bills. | Round 286 |
| Qualifying | Questions about ownership, roof age, shade and how long they'll stay. | Round 204, Round 381 |
| Ownership is complicated | The home is in a trust, an HOA, a land contract, a divorce or a lease park. | Round 206, Round 213 |
| Checking usage | The agent needs the person's real electricity usage and utility details. | Round 156, Round 233 |
| Roof first | The roof needs replacing before solar can go on. | Round 322, Round 389 |
| Not suitable | The home or situation doesn't fit a sale. | Round 170, Round 336 |
| Quote | Price, system size, savings and monthly payment are on the table. | Round 392, Round 314 |
| Financing choice | Cash, loan or lease options are being compared. | Round 320, Round 224 |
| Answering a question | The person asks a plain question, like what an escalator is. | Round 291, Round 364 |
| Objection | The person pushes back on price, timing, the roof or a move. | Round 71, Round 284 |
| Bargaining | The person names conditions or asks for a discount before agreeing. | Round 288, Round 289 |
| Changing the offer | The person wants a smaller system or another option, so the offer is redone. | Round 337, Round 23 |
| Existing customer | The person already has panels or bought before, so this is an upsell or service matter. | Round 319, Round 82 |
| Repeat that, please | The agent didn't understand and asked again. | Round 380, Round 376 |
| Service problem raised | The person brings up a problem with something they already own. | Round 198, Round 99 |
| Privacy question | The person asks where their number came from, or asks for their data to be deleted. | Round 166, Round 244 |
| Asking about the AI | The person asks who is listening, or whether the call is recorded or used to learn. | Round 292, Round 40 |

## Closing (7)

The offer is spelled out and the person decides.

| State | What it means | Shows up in |
|---|---|---|
| Read-back | Every term of the deal is read out: product, size, cost, warranties, cancellation, lien, financing. | Round 217, Round 356 |
| Waiting for the answer | The agent has asked for agreement and is waiting. | Round 367, Round 372 |
| Agreed | The person said yes and the agreement is recorded. | Round 354, Round 184 |
| Contract sent | The e-sign link and code have gone out by text or email. | Round 355, Round 357 |
| Signing during the call | The person is opening and signing the documents while still on the phone. | Round 60, Round 342 |
| Credit check | The lender is running the application, which can come back frozen or denied. | Round 358, Round 225 |
| Wrapping up | The agent says goodbye and the call is about to end. | Round 172, Round 173 |

## What's happening on the line (14)

These can show up at any point in the call, on top of where the conversation is.

| State | What it means | Shows up in |
|---|---|---|
| Talking over each other | Both sides speak at once, or the person cuts the agent off. | Round 370, Round 371 |
| Thinking pause | The person goes quiet to think, not because they've finished. | Round 25, Round 367 |
| Bad line | Wind, dropouts or delay make the person hard to hear or hard to reach. | Round 169, Round 165 |
| Mm-hm | The person makes listening sounds that aren't answers. | Round 14, Round 369 |
| Long story | The person talks for a long time, with corrections along the way. | Round 44, Round 368 |
| Other language | The person is more comfortable in another language, or mixes two. | Round 16, Round 236 |
| Hard of hearing | The person needs the agent to slow down or speak up. | Round 238, Round 237 |
| Speech difficulty | A stutter, stroke or other condition makes the person hard for the system to understand. | Round 111, Round 147 |
| Upset | The person is crying, grieving, or shares bad news. | Round 286, Round 19 |
| Angry or threatening | The person is hostile, or threatens the company or its crews. | Round 284, Round 201 |
| Busy elsewhere | The person is driving, at a hospital or otherwise can't really talk. | Round 168, Round 352 |
| Testing the agent | The person is probing or trying to trip the agent up on purpose. | Round 87, Round 294 |
| Background audio | A TV, radio or speaker is playing near the phone. | Round 98, Round 295 |
| Waiting on the agent | The agent is slow to answer and the person starts repeating themselves. | Round 401, Round 364 |

## Ending the call (10)

The ways a call can end.

| State | What it means | Shows up in |
|---|---|---|
| Stop calling me | The person asks not to be called again. | Round 345, Round 339 |
| Not interested | The person says no and the agent lets them go. | Round 21, Round 164 |
| Callback booked | The person asks to be called back another time. | Round 145, Round 305 |
| Handed to a human | The call goes to a human closer or supervisor. | Round 263, Round 190 |
| Appointment booked | An in-home or video consultation is set up. | Round 330, Round 55 |
| Gentle exit | The agent ends the call because the person seems vulnerable or confused. | Round 15, Round 325 |
| Safety exit | The call ends because of a threat or a medical emergency. | Round 201, Round 19 |
| Call dropped | The line drops before the call is finished. | Round 30 |
| Person hung up | The person hangs up, often within seconds of hearing it's an AI. | Round 259 |
| Goodbye | The call ends normally after the goodbye. | Round 173 |

## After the call (13)

A yes on the phone is only the start. Success is a system that's really installed.

| State | What it means | Shows up in |
|---|---|---|
| Waiting for signature | The contract is out and hasn't been signed yet. | Round 342, Round 357 |
| Signed | The contract is signed and the sale is pending. | Round 123, Round 136 |
| Cancellation window | The person can still cancel by law, often 3 or 5 days. | Round 216, Round 241 |
| Cancelled | The person cancelled or rescinded the deal. | Round 76, Round 216 |
| Financing decided | The lender approves or declines the loan after the call. | Round 358, Round 50 |
| Site survey | Someone checks the house, which can change the price or the equipment. | Round 159, Round 160 |
| Waiting to install | Permits, interconnection queues and scheduling are in progress. | Round 219, Round 158 |
| Installed | The system is on the roof. | Round 219, Round 158 |
| Turned on | The utility gives permission to operate, so the system actually runs. | Round 158 |
| Follow-up call | A later call for service, confirmation or an upsell. | Round 220, Round 99 |
| Complaint or dispute | The person complains to a regulator, sues or disputes the deal. | Round 271, Round 265 |
| Life changes | The home is sold, or the owner files for bankruptcy, while the loan runs. | Round 218, Round 215 |
| Data request | The person asks to see or delete everything held about them. | Round 245 |

## What the person really means (10)

These can't be heard directly. The words can sound the same while the truth underneath is different.

| State | What it means | Shows up in |
|---|---|---|
| Really interested | The person genuinely wants to go ahead. | Round 354 |
| Polite yes, not agreeing | Yes is said out of politeness or habit, not agreement. | Round 144, Round 235 |
| Polite no | "I'll think about it" or "that's a little difficult" really means no. | Round 145, Round 372 |
| Confused | The person doesn't understand what they're agreeing to. | Round 242, Round 48 |
| Sarcastic | The words say yes, the tone says no. | Round 27 |
| Pressured by someone | A relative, caregiver or partner in the room is steering the answers. | Round 148, Round 303 |
| Can't legally agree | Dementia, a conservatorship or a court order means they can't sign. | Round 15, Round 240 |
| Vulnerable but clear | Lonely, grieving or overexcited, yet speaking clearly. | Round 153, Round 152 |
| Can't afford it | The payment is beyond what they can carry. | Round 150, Round 316 |
| Not who they say | A fraudster or a planted lead is pretending to be the owner. | Round 162, Round 195 |

## What I left out on purpose

Many rounds weren't about the call at all. They were about how the agent is trained, certified, audited, stored and regulated, for example rounds 116 to 135, 247 to 283 and 394 to 403. Those are states of the company and its pipeline, not states a call can be in, so they're not on this list.

I also left out the agent's own internal machinery, such as pre-rendering a likely answer or queuing a text message, because those are how the agent works, not where the call is.
