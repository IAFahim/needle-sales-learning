## A1
TOPIC: Anger with no opt-out word: hostile venting has no event, so "clarify once, then fallback" makes a furious caller repeat the rant, then books another call
SCENARIO: 1) Caller: "Unbelievable. Fifth solar call this week, you people are vultures." 2) No stop word, no request_human; GLOBAL sees nothing, LOCAL picks out_of_scope or unclear. 3) Agent plays the clarify fragment: "Sorry, could you say that again?" 4) Caller, angrier: "Are you deaf? I said you're vultures." Still not an event. 5) Clarify budget spent, so the fallback fires: "I can have someone call you back at a better time." 6) A callback goes into the outbox for a person who just said the calls are the problem.
WHY IT BREAKS: Hostility has no event, no de-escalation state and no counter. Since April 11, 2025, consent can be revoked "by any reasonable means" (47 CFR 64.1200(a)(10), FR 2024-23605), and "why do you keep calling" is arguably such a means. The design's safe fallback turns anger into another call and a complaint.

## A2
TOPIC: Conversational "stop" ("wait, stop, go back to the price") trips the union stop lexicon, and the caller's "no, keep going" can't legally undo it
SCENARIO: 1) During QUOTE, an interested caller says: "Stop, stop, go back. What was the monthly?" 2) The deterministic lexicon matches "stop". Stop is a union, so Needle's LOCAL reading (repair request) can't veto it. 3) The DNC exit plays, the call ends and the number is suppressed. 4) Variant: the exit starts and the caller cuts in: "No! I meant keep going!" The machine is already past the terminal state.
WHY IT BREAKS: A union lexicon has no idea of scope: "stop" as a discourse marker, as surprise ("stop, really?") or as a repair request all become DNC. Prior express written consent for artificial-voice telemarketing (64.1200(a)(2)) can't be restored by an oral "keep going", so the design either drops buyers or keeps calling without valid consent.

## A3
TOPIC: Crying, sighing and groaning are dropped as non-speech, so the bot's first reply to a sobbing person is "I didn't catch that"
SCENARIO: 1) DISCOVERY: "What got you thinking about your energy bills?" 2) Caller starts to cry (the bills went up since the divorce). For eight seconds there is only sobbing and breathing. 3) The ASR-confidence/no-speech pre-gate drops it as no speech or low confidence, so it becomes an unintelligible re-ask: "Sorry, I didn't catch that, could you repeat?" 4) The caller manages "...never mind." That gets labeled acknowledge, and QUALIFY continues.
WHY IT BREAKS: The only paralinguistic feature is a final-rise token. Laughter, sobs, sighs and groans carry most of the emotional signal in real calls, and the pre-gate removes them before Needle runs. sensitive_event can't fire on words that were never sent. An "unintelligible" re-ask to a crying person is the worst possible reply, and the pre-gate makes it certain.

## A4
TOPIC: Joking hyperbole in qualifying answers is grounded as a literal slot value ("roof's older than me", "a million trees")
SCENARIO: 1) QUALIFY: "How old is your roof?" A playful caller: "Ha, about a hundred years, like me." 2) Needle extracts roof_age=100. "hundred" is in the ASR text, so the grounding gate passes. 3) Suitability table gives ROOF_FIRST or NOT_SUITABLE, an honest exit with no rebuttal, and the call ends. 4) Variant: "Shade? I live in a forest, buddy," when there's one maple. Needle sets shade=heavy, and that outcome is logged against the lead.
WHY IT BREAKS: Grounding checks only that the words are present, not that they were sincere. Laughter, the main cue for joking, is stripped (see A3). Joking is common with friendly, engaged prospects, exactly the buyers the system wants. The "no rebuttal" NOT_SUITABLE exit means a one-liner permanently disqualifies a suitable home, and nothing lets the caller say "I'm kidding".

## A5
TOPIC: Haggling: the agent has no authority to concede, so negotiators are routed to humans who can discount, and price ends up depending on assertiveness
SCENARIO: 1) After QUOTE: "I'll sign tonight if you knock off two grand." 2) The price comes only from the table, so the agent plays the fixed "our price is set" fragment. 3) Caller: "Then put me through to your manager." That's request_human, a warm transfer. 4) The closer has the dealer markup room every solar sale carries and takes off $2,000. 5) A quieter caller on the same campaign signs the certified table price.
WHY IT BREAKS: In residential solar, negotiating is normal, not an edge case. A zero-discretion bot plus humans with discretion means "ask for a human" becomes the discount path. Prices then depend on who pushes, which breaks the design's own "same menu for all" fair-lending claim (matched pairs never haggle). The final price also bypasses the certified table and READ_BACK provenance.

## A6
TOPIC: Condition laundering: the closed re-ask after a conditional yes drops the condition, and the caller's next "yes" still assumes it
SCENARIO: 1) READ_BACK ends, and the agent asks for agreement. 2) Caller: "Yes, as long as you install before Christmas and throw in the critter guard." 3) It's a conditional, so the gate fires the closed re-ask: "To confirm, do you agree to the terms I read? Yes or no." 4) Caller: "Yes." In their mind, the terms include what they just said. 5) The COMMIT passes: short, direct, lexical. 6) The envelope has no install date and no critter guard.
WHY IT BREAKS: The design treats a conditional as noise to filter out, not as a counter-offer to answer. The closed binary re-ask never says "we can't promise that". A caller's yes to a question that ignored their condition reasonably reads as acceptance of it. That's a misrepresentation by omission (FTC s5, TSR 310.3(a)(4)), and a guaranteed cancellation later.

## A7
TOPIC: A soft retraction seconds after the commit ("...hm, actually, let me sleep on it") has no event, because nothing has been signed yet to cancel
SCENARIO: 1) The COMMIT gate passes and the outbox drains on that committed turn, so the e-sign SMS with OTP goes out. 2) Two seconds later: "Hm. Actually, hold on, let me think about it overnight." 3) This is not cancel_or_rescind, because there's no contract yet. Needle's labels are acknowledge, small_talk or out_of_scope. 4) The machine stays in WAITING_FOR_SIGNATURE and plays the "check your texts to sign" fragment. 5) The OTP envelope sits on the phone of a person who just took back their yes.
WHY IT BREAKS: People change their minds right after saying yes all the time. The event schema puts revocation only after a signature (cancel/rescind) and puts nothing between the commit and the signature. The outbox already sent the envelope, nothing withdraws it, and the agent keeps steering toward signing. That's high-pressure conduct the TSR and state UDAP laws target.

## A8
TOPIC: Interruptions during READ_BACK: the design never defines whether to resume or restart, and both choices break the commit
SCENARIO: 1) Item 4 of 9 in the READ_BACK (escalator). Caller: "Wait, what's an escalator?" 2) The agent answers with the definition fragment. 3) Resume option: the agent continues at item 5, so the commit covers a read-back the caller never heard in one piece, and the earlier items are minutes and two digressions back. 4) Restart option: the caller asks about item 7, the read-back restarts, then again for item 8. After three nine-item loops the budget counter fires WRAP_UP on a willing buyer.
WHY IT BREAKS: "Every commit path passes READ_BACK" is checked at the graph level, but an interrupted read-back doesn't make sense to a listener. Resuming wrecks comprehension and restarting wrecks the call budget. The model check proves the read-back nodes were visited, not that the caller understood the terms, which is what TSR 310.3(a)(1) disclosure is for.

## A9
TOPIC: Meta-questions testing the bot ("is a real person listening?", "will you learn from this call?", "are you reading a script?") have no events, and the truthful answers are yes
SCENARIO: 1) A sceptical caller tests it: "Is anyone listening to this right now? Do you learn from what I say?" 2) There's no GLOBAL event for it. request_caller_identity covers the company, not data use. It gets labeled out_of_scope, then a clarify, then a fallback. 3) Or a nearby fragment says "This call may be recorded for quality." 4) In fact, third-party labelers will listen to the audio, and the call goes into Needle's training union permanently.
WHY IT BREAKS: Testing questions are how people decide whether to trust an AI caller. The truthful answers (human audit, training use) are exactly what the preamble's recording notice leaves out. Dodging a direct question about data use is a deceptive omission under FTC s5. CCPA notice at collection must name training use and third-party review, and an "out_of_scope" answer confirms the caller's suspicion.

## A10
TOPIC: Storytellers run out the call budget: time and turn counters fire WRAP_UP mid-anecdote on engaged buyers, mostly older ones
SCENARIO: 1) Caller: "Let me tell you about my neighbor Frank's panels..." and keeps going for three minutes, warmly. 2) Speculation is off for the long turn, and dangling-word endpointing waits. 3) Two more stories in QUALIFY, each correctly labeled small_talk. 4) The turn and time budgets fill up, and WRAP_UP fires: "I'll let you go, we'll follow up." 5) The caller was ready to buy, and the call ends before QUOTE.
WHY IT BREAKS: Budgets meant to stop bot loops can't tell a rapport-building story from a stall. Long narrative turns go with age and culture, so the counter cuts some groups off more than others. The NOT_SUITABLE-style end and the automatic follow-up are an automated decision under CPPA ADMT and Colorado SB 26-189 that no one can explain beyond "you talked too long".

Sources: FCC revocation rule, FR 2024-23605 (https://www.govinfo.gov/content/pkg/FR-2024-10-11/html/2024-23605.htm); waiver/delay of the "revoke-all" provision only (https://www.kelleydrye.com/viewpoints/blogs/ad-law-access/fcc-issues-one-year-limited-waiver-of-new-tcpa-consent-revocation-rule).
