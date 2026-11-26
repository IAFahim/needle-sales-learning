=== R294
Round 294: Breaker wins.

- **Attack:** A caller says "stop" right over the agent's own word "stop", and the echo filter throws their word away as echo.
- **My defense:** Any caller sound during agent speech pauses the agent, and stop words left over from overlap trigger a check question and a hold on the number.
- **Judge:** The echo filter removes matching words before anything else sees them, so the caller's "stop" never reaches the overlap check or the after call sweep.
- **Fix:** The echo filter may never delete a stop word, and the after call sweep reads the raw transcript.

=== R295
Round 295: I win.

- **Attack:** A caller plays the radio under their voice so the TV detector tags them as background media and drops their opt out.
- **My defense:** The TV detector only asks whether to call back; the stop word check runs on every transcript regardless of how the audio is tagged.
- **Judge:** The media tag is a question, not a filter, so "take me off your list" still ends the call.

=== R296
Round 296: I win.

- **Attack:** A lead partner spoofs the owner's number and plays cloned "yes" clips to fake a verified commit.
- **My defense:** Caller ID never proves identity; only a code texted to the number on record unlocks the sale, and signing needs a photo ID check.
- **Judge:** The code goes to the real owner's phone, and a recorded "yes" cannot say "send the contract" or pass the ID check at signing.

=== R297
Round 297: Breaker wins.

- **Attack:** A caller repeats "no" hundreds of times to make the stop word patterns run so slowly that the shared front end stalls other calls.
- **My defense:** Turns are split into bounded segments, callers are rate limited, and pressing a key to opt out bypasses speech entirely.
- **Judge:** Nothing in the design bounds how long the pattern matching can take, and the segment limit only covers the model's input.
- **Fix:** Use pattern engines that always run in linear time, and give each call a hard time limit that falls back to the safe stop question.

=== R298
Round 298: I win.

- **Attack:** During the build phase, a caller talks to the big model labeling the call and tricks it into ignoring a stop or logging a yes.
- **My defense:** The big model never decided stops or commits alone; a fixed word list ends the call and a commit needs the exact phrase "send the contract".
- **Judge:** The hijacked label changes nothing live, and safety training labels come from blind human review, not the big model.

=== R299
Round 299: Breaker wins.

- **Attack:** A caller names two numbers to put on the do not call list, and the card number blanker wipes out the second number.
- **My defense:** The line that was dialled still goes on the list, and every blanked span is logged with its time and reason.
- **Judge:** The design has no way to record a second number named in a do not call request, since contact details are blanked before anything reads them.
- **Fix:** Pull named numbers from the raw transcript into the do not call list before blanking, and make the card pattern stop at non digit words.

=== R300
Round 300: I win.

- **Attack:** A competitor floods the agent with tricky calls so error alarms trip and the whole fleet falls back to human closers.
- **My defense:** Falling back to the safe path is the intended outcome, and call farms cannot reach the closing steps without a code from the number on record.
- **Judge:** The attack costs money, not customer harm, and the checks before closing make it hard to reach at scale.

=== R301
Round 301: I win.

- **Attack:** Timing the agent's reply speed lets an attacker map which phrasings leave the model unsure.
- **My defense:** Unsure answers already lead to a clarifying question, and stops and commits are decided by fixed word checks, not the model's confidence.
- **Judge:** Knowing where the model hesitates gives the attacker nothing that leads to harm.

=== R302
Round 302: I win.

- **Attack:** A lead record with the name "Alexa" makes the agent wake smart speakers in the customer's home.
- **My defense:** By default the agent speaks no names, and every spoken name passes a sound alike blocklist first.
- **Judge:** Names come from public records after verification and the default scripts carry none, so hostile text does not get spoken.

=== R303
Round 303: I win.

- **Attack:** A relative makes noise whenever the elderly owner objects, then says a clear "yes" to the agent's follow up.
- **My defense:** Any repeated question at the close blocks a same call sale, and the closing voice must match the verified owner.
- **Judge:** A bare "yes" from another voice cannot close, and every buyer gets a private confirmation call before install.
