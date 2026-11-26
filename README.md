# Needle sales agent: learning notes

Research for an outbound solar sales call agent where Needle, a small tool-calling model, only labels what the caller said, and a StateSmith state machine does everything else.

| File | What it is |
|---|---|
| `final-plan.md` | the plan as it stands: runtime, call structure, safety gates, certification |
| `states/doc.md` | the 96 states a call can be in, in 9 groups |
| `states/states.json` | the same states as data |
| `states/call-state-atlas.html` | the states as a page to open in a browser |
| `rounds.md` | every debate round: attack, defence, verdict |
| `design.md` | the full design as it grew round by round |
| `base-design.md` | the design the debate started from |
| `breaker-brief.md`, `breaker-brief-v2.md` | the briefs the attacking side worked from |
| `batches/` | the raw rounds, 30 batches: attacks, defences, verdicts, logs and the scripts that merged them |

The state machines themselves live in a separate repo, `needle-sales-demo`.
