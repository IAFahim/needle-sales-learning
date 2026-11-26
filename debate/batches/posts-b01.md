=== R104
Round 104: I win.

**Attack:** A cough or a TV in the background gets heard as a quiet "yeah" and triggers the order.
**My defense:** A false yes can only send a signing envelope, and nothing binds until the customer signs.
**Judge:** Nobody is bound by a phantom yes, so the harm is small.

=== R105
Round 105: Breaker wins.

**Attack:** A speech engine update could read a rate or escalator differently from the text we logged.
**My defense:** Binding terms come in a written contract, so audio does not decide them.
**Judge:** The certified bundle never pinned the voice engine, so the spoken terms can change after certification.
**Fix:** Pin the voice engine and text normaliser, write out every number as spoken words, and pre render and check the audio of every fact clip.

=== R106
Round 106: I win.

**Attack:** Phone delay of 400 ms makes a yes spoken during the cancellation notice look like a clean answer.
**My defense:** The yes still reaches the server while the question is playing, so it is thrown away.
**Judge:** Answers during playback are ignored, so this cannot commit anything.

=== R107
Round 107: Breaker wins.

**Attack:** A broken audio path means the opening disclosure plays to nobody but is logged as delivered.
**My defense:** Interrupting hellos would make the disclosure replay.
**Judge:** The disclosure played without interruption into a dead line, and nothing checks that it was received.
**Fix:** Only mark a disclosure delivered when far end reports show the audio arrived, and hang up and call back if not.

=== R108
Round 108: I win.

**Attack:** A cheap speakerphone swallows the caller's "stop" while the agent is talking.
**My defense:** Any burst of sound makes the agent stop and listen, and keypad opt out still works.
**Judge:** The agent hands the floor back, and a phone that never sends the words is a limit no design can beat.

=== R109
Round 109: Breaker wins.

**Attack:** Waiting and machine checks leave dead air at the start, and a long greeting can be mistaken for a voicemail.
**My defense:** The opening is pre recorded, so delay is small.
**Judge:** The rules require connecting within about two seconds, and the design had no timer or abandonment count.
**Fix:** Start the disclosure within 1.5 seconds, treat unclear machine results as human, and cap abandoned calls at 3 percent per campaign.

=== R110
Round 110: I win.

**Attack:** A low voice or a habit of rising tone makes the pitch detector wrongly block a real yes.
**My defense:** A false rise only causes a simple re ask, then a callback, never a wrong yes.
**Judge:** The failure is safe and costs only time.

=== R111
Round 111: Breaker wins.

**Attack:** People with speech disabilities get pushed into unclear answers and then a no sale exit.
**My defense:** Fallback means a callback or a person, not a denial.
**Judge:** Unclear speech feeds the vulnerability counter, and no test measures denial for speech disabilities.
**Fix:** Add speech disability test groups, make their denial rates release blockers, and keep unclear audio out of the vulnerability counter.

=== R112
Round 112: Breaker wins.

**Attack:** Someone joining the call late never hears the AI and recording notices.
**My defense:** A new voice resets identity, so they must verify again.
**Judge:** A second adult can pass identity and reach the commit without ever hearing the disclosures.
**Fix:** Replay the full disclosure when a new speaker appears, and stop recording until they agree.

=== R113
Round 113: Breaker wins.

**Attack:** Calls with no recording leave the do not call check with nothing to scan, and they escape audits.
**My defense:** The check reads the live transcript, not the recording.
**Judge:** The check reuses the same rules that missed the stop, and these calls are left out of human audits.
**Fix:** Make the check run before deletion with a log, stop redials if it fails, and treat these calls as their own audited group.
